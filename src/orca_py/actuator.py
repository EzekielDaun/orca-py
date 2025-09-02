import struct
from dataclasses import dataclass, field
from typing import Literal, Optional

from pymodbus import ExceptionResponse
from pymodbus.client.serial import AsyncModbusSerialClient

from .orca_constant import ORCA_MODE, ORCA_MODE_SUBCODE
from .orca_high_speed_stream_pdu import (
    OrcaStreamCommandRequestPDU,
    OrcaStreamCommandResponsePDU,
    OrcaStreamManageRequestPDU,
    OrcaStreamManageResponsePDU,
    OrcaStreamReadRequestPDU,
    OrcaStreamReadResponsePDU,
    OrcaStreamWriteRequestPDU,
    OrcaStreamWriteResponsePDU,
)
from .orca_register import ORCA_REGISTER


def _int32_to_uint16s(value):
    # Pack the int32 value as 4 bytes
    packed = struct.pack("<i", value)  # '<i' specifies little-endian 4-byte signed int

    # Unpack it as two unsigned 16-bit integers
    lower_16, upper_16 = struct.unpack(
        "<HH", packed
    )  # '<HH' specifies two little-endian 2-byte unsigned ints

    return lower_16, upper_16


@dataclass(slots=True)
class Actuator:
    comport: str
    baudrate: int
    reconnect_delay: float
    timeout: float
    retries: int
    dev_id: int = 1
    client: AsyncModbusSerialClient = field(
        init=False,
    )

    async def __aenter__(self):
        self.client = AsyncModbusSerialClient(
            self.comport,
            baudrate=self.baudrate,
            parity="E",
            reconnect_delay=self.reconnect_delay,
            timeout=self.timeout,
            retries=self.retries,
        )
        self.client.register(OrcaStreamManageResponsePDU)
        self.client.register(OrcaStreamCommandResponsePDU)
        self.client.register(OrcaStreamReadResponsePDU)
        self.client.register(OrcaStreamWriteResponsePDU)
        assert await self.client.connect(), f"Failed to connect to {self.comport}."
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.set_mode(ORCA_MODE.SleepMode)
        self.client.close()

    async def set_mode(self, mode: ORCA_MODE):
        return await self.client.write_register(
            ORCA_REGISTER.CTRL_REG_3.value.address, mode
        )

    async def get_mode(self):
        return ORCA_MODE(
            (
                await self.client.read_holding_registers(
                    ORCA_REGISTER.MODE_OF_OPERATION.value.address
                )
            ).registers[0]
        )

    async def tune_pid_controller(
        self, saturation: int, p_gain: int, i_gain: int, dv_gain: int, de_gain: int
    ):
        saturationL, saturationH = _int32_to_uint16s(saturation)
        configuration = [p_gain, i_gain, dv_gain, de_gain, saturationL, saturationH]
        return await self.client.write_registers(
            ORCA_REGISTER.PC_PGAIN.value.address, configuration
        )

    async def position_command(self, position: int):
        return await self.client.write_registers(
            ORCA_REGISTER.POSITION_CMD.value.address, list(_int32_to_uint16s(position))
        )

    async def kinematic_trigger(self, motion_id: int):
        return await self.client.write_register(
            ORCA_REGISTER.KIN_SW_TRIGGER.value.address, motion_id
        )

    async def configure_motion(
        self, motionID: int, position: int, time, delay, nextID, type, autonext
    ):
        positionL, positionH = _int32_to_uint16s(position)
        timeL, timeH = _int32_to_uint16s(time)
        next_type_auto = (nextID << 3) + (type << 1) + autonext
        configuration = [positionL, positionH, timeL, timeH, delay, next_type_auto]
        return await self.client.write_registers(
            ORCA_REGISTER.KIN_MOTION_0.value.address + motionID * 6, configuration
        )

    async def kinematic_status(self):
        return await self.client.read_holding_registers(
            ORCA_REGISTER.KINEMATIC_STATUS.value.address
        )

    # ========== Below are Streamed Only ==========

    async def __set_stream_enable(self, enable: bool, baudrate: int, delay: int):
        response: OrcaStreamManageResponsePDU = await self.client.execute(
            False,
            OrcaStreamManageRequestPDU(enable, baudrate, delay, dev_id=self.dev_id),
        )  # type: ignore
        return response.baudrate, response.delay

    async def stream_enable(self, baudrate: int, delay: int):
        await self.set_mode(ORCA_MODE.SleepMode)
        self.client.comm_params
        return await self.__set_stream_enable(True, baudrate, delay)

    async def stream_disable(self):
        return await self.__set_stream_enable(False, 0, 0)

    async def stream_motor_command(
        self, subcode: ORCA_MODE_SUBCODE, data: Optional[int]
    ):
        match subcode:
            case ORCA_MODE_SUBCODE.ForceControlStream:
                assert data is not None, "ForceControlStream requires data."
            case ORCA_MODE_SUBCODE.PositionControlStream:
                assert data is not None, "PositionControlStream requires data."
            case ORCA_MODE_SUBCODE.KinematicDataStream:
                data = 0x00
            case ORCA_MODE_SUBCODE.HapticDataStream:
                assert data is not None, "HapticDataStream requires data."
            case ORCA_MODE_SUBCODE.SleepDataStream:
                data = 0x00
            case _:
                raise ValueError("Invalid subcode.")
        response: OrcaStreamCommandResponsePDU = await self.client.execute(
            False, OrcaStreamCommandRequestPDU(subcode, data, dev_id=self.dev_id)  # type: ignore
        )
        if type(response) is ExceptionResponse:
            raise RuntimeError(f"Motor Error: Exception Response: {response}")
        elif response.stream_info.error:
            raise RuntimeError(f"Motor Error: {response.stream_info.error}")
        return response.stream_info

    async def stream_motor_read(self, address: int, width: Literal[1] | Literal[2]):
        response: OrcaStreamReadResponsePDU = await self.client.execute(
            False, OrcaStreamReadRequestPDU(address, width, dev_id=self.dev_id)  # type: ignore
        )
        if response.stream_info.error:
            raise RuntimeError(f"Motor Error: {response.stream_info.error}")
        return response.register_value, response.mode_of_operation, response.stream_info

    async def stream_motor_write(
        self, address: int, width: Literal[1] | Literal[2], data: int
    ):
        response: OrcaStreamWriteResponsePDU = await self.client.execute(
            False, OrcaStreamWriteRequestPDU(address, width, data, dev_id=self.dev_id)  # type: ignore
        )
        if response.stream_info.error:
            raise RuntimeError(f"Motor Error: {response.stream_info.error}")
        return response.stream_info

    async def stream_tune_pid_controller(
        self, p: int, i: int, dv: int, de: int, sat: int
    ):
        sat_lo, sat_hi = _int32_to_uint16s(sat)
        await self.stream_motor_write(
            ORCA_REGISTER.PC_PGAIN.value.address, ORCA_REGISTER.PC_PGAIN.value.width, p
        )
        await self.stream_motor_write(
            ORCA_REGISTER.PC_IGAIN.value.address, ORCA_REGISTER.PC_IGAIN.value.width, i
        )
        await self.stream_motor_write(
            ORCA_REGISTER.PC_DVGAIN.value.address,
            ORCA_REGISTER.PC_DVGAIN.value.width,
            dv,
        )
        await self.stream_motor_write(
            ORCA_REGISTER.PC_DEGAIN.value.address,
            ORCA_REGISTER.PC_DEGAIN.value.width,
            de,
        )
        await self.stream_motor_write(
            ORCA_REGISTER.PC_FSATU.value.address,
            ORCA_REGISTER.PC_FSATU.value.width,
            sat_lo,
        )
        return await self.stream_motor_write(
            ORCA_REGISTER.PC_FSATU_H.value.address,
            ORCA_REGISTER.PC_FSATU_H.value.width,
            sat_hi,
        )
