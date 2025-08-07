import struct
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


class Actuator:

    # use a class method to initialize the class while await for async connection
    @classmethod
    async def create(cls, comport: str, baudrate: int):
        """
        Asynchronous factory method to initialize the class with an asynchronous operation.
        """
        actuator = cls(comport, baudrate)
        if not await actuator.__client.connect():
            raise ConnectionError(f"Failed to connect to {comport}.")
        return actuator

    # do not directly instantiate this class
    def __init__(self, comport: str, baudrate: int):
        self.__client = AsyncModbusSerialClient(
            comport, parity="E", baudrate=baudrate, timeout=0.1, retries=3
        )

    @property
    def client(self):
        return self.__client

    ################################
    # Base ModBus Communication Functions
    ################################

    # write single register
    async def write_register(self, register_address: int, value: int):
        if not self.__client.connected:
            raise RuntimeError("Client is not connected.")
        return await self.__client.write_register(register_address, value)

    # write multiple registers
    async def write_multi_registers(
        self,
        registers_start_address: int,
        register_data: list[int],
    ):
        if not self.__client.connected:
            raise RuntimeError("Client is not connected.")
        return await self.__client.write_registers(
            registers_start_address,
            register_data,
            # no_response_expected=True,
        )

    # read multiple registers
    async def read_registers(
        self, registers_start_address: int, num_registers: int = 1
    ):
        if not self.__client.connected:
            raise RuntimeError("Client is not connected.")
        return await self.__client.read_holding_registers(
            registers_start_address, count=num_registers
        )

    ################################
    # Orca Functions
    ################################

    # Change Orca's mode of operation
    async def set_mode(self, mode: ORCA_MODE):
        return await self.write_register(ORCA_REGISTER.CTRL_REG_3.value.address, mode)

    async def get_mode(self):
        return ORCA_MODE(
            (
                await self.read_registers(ORCA_REGISTER.MODE_OF_OPERATION.value.address)
            ).registers[0]
        )

    # Trigger Kinematic Motion
    async def kinematic_trigger(self, motion_id: int):
        return await self.write_register(
            ORCA_REGISTER.KIN_SW_TRIGGER.value.address, motion_id
        )

    # Configure Kinematic Motion
    async def configure_motion(
        self, motionID: int, position: int, time, delay, nextID, type, autonext
    ):
        # positionL_H = obj.int32_to_u16(position);
        # timeL_H = obj.int32_to_u16(time);
        # next_type_auto = bitshift(nextID, 3) + bitshift(type, 1) + autonext;
        # configuration = [positionL_H, timeL_H, delay,next_type_auto];
        # obj.write_multi_registers(780 + motionID*6, 6, configuration);  % KIN_MOTION_0 780

        positionL, positionH = _int32_to_uint16s(position)
        timeL, timeH = _int32_to_uint16s(time)
        next_type_auto = (nextID << 3) + (type << 1) + autonext
        configuration = [positionL, positionH, timeL, timeH, delay, next_type_auto]
        return await self.write_multi_registers(
            ORCA_REGISTER.KIN_MOTION_0.value.address + motionID * 6, configuration
        )

    # Tune PID Values
    async def tune_pid_controller(self, saturation, p_gain, i_gain, dv_gain, de_gain):
        # saturationL_H = obj.int32_to_u16(saturation); %split 32 bit into 2 16 bit, low first hi second
        # configuration = [p_gain, i_gain, dv_gain, de_gain , saturationL_H];
        # obj.write_multi_registers(133, 6, configuration);  % PC_PGAIN 133, num consecutive registers 6, register values  configuration
        saturationL, saturationH = _int32_to_uint16s(saturation)
        configuration = [p_gain, i_gain, dv_gain, de_gain, saturationL, saturationH]
        return await self.write_multi_registers(
            ORCA_REGISTER.PC_PGAIN.value.address, configuration
        )

    # Check Kinematic Status
    async def kinematic_status(self):
        return await self.read_registers(ORCA_REGISTER.KINEMATIC_STATUS.value.address)

    # Position Command
    async def position_command(self, position: int):
        return await self.write_multi_registers(
            ORCA_REGISTER.POSITION_CMD.value.address, list(_int32_to_uint16s(position))
        )


class StreamedActuator:

    # use a class method to initialize the class while await for async connection
    @classmethod
    async def create(
        cls, comport: str, baudrate: int, timeout: float, retries: int, dev_id: int = 1
    ):
        """
        Asynchronous factory method to initialize the class with an asynchronous operation.
        """
        actuator = cls(comport, baudrate, timeout, retries, dev_id)
        await actuator.__client.connect()
        return actuator

    # do not directly instantiate this class
    def __init__(
        self, comport: str, baudrate: int, timeout: float, retries: int, dev_id: int
    ):
        self.__client = AsyncModbusSerialClient(
            comport, parity="E", baudrate=baudrate, timeout=timeout, retries=retries
        )
        self.__client.register(OrcaStreamManageResponsePDU)
        self.__client.register(OrcaStreamCommandResponsePDU)
        self.__client.register(OrcaStreamReadResponsePDU)
        self.__client.register(OrcaStreamWriteResponsePDU)
        self.__dev_id = dev_id

    async def __set_stream_enable(self, enable: bool, baudrate: int, delay: int):
        response: OrcaStreamManageResponsePDU = await self.__client.execute(
            False, OrcaStreamManageRequestPDU(enable, baudrate, delay, dev_id=1)
        )  # type: ignore
        return response.baudrate, response.delay

    async def enable_stream(self, baudrate: int, delay: int):
        await self.__client.write_register(
            ORCA_REGISTER.CTRL_REG_3.value.address, ORCA_MODE.SleepMode
        )
        return await self.__set_stream_enable(True, baudrate, delay)

    async def disable_stream(self):
        return await self.__set_stream_enable(False, 0, 0)

    async def motor_command(self, subcode: ORCA_MODE_SUBCODE, data: Optional[int]):
        match subcode:
            case ORCA_MODE_SUBCODE.ForceControlStream:
                if data is None:
                    raise ValueError("ForceControlStream requires data.")
            case ORCA_MODE_SUBCODE.PositionControlStream:
                if data is None:
                    raise ValueError("PositionControlStream requires data.")
            case ORCA_MODE_SUBCODE.KinematicDataStream:
                data = 0x00
            case ORCA_MODE_SUBCODE.HapticDataStream:
                if data is None:
                    raise ValueError("HapticDataStream requires data.")
            case ORCA_MODE_SUBCODE.SleepDataStream:
                data = 0x00
            case _:
                raise ValueError("Invalid subcode.")
        response: OrcaStreamCommandResponsePDU = await self.__client.execute(
            False, OrcaStreamCommandRequestPDU(subcode, data, dev_id=self.__dev_id)  # type: ignore
        )
        if type(response) is ExceptionResponse:
            raise RuntimeError(f"Motor Error: Exception Response: {response}")
        elif response.stream_info.error:
            raise RuntimeError(f"Motor Error: {response.stream_info.error}")
        return response.stream_info

    async def motor_read(self, address: int, width: Literal[1] | Literal[2]):
        response: OrcaStreamReadResponsePDU = await self.__client.execute(
            False, OrcaStreamReadRequestPDU(address, width, dev_id=self.__dev_id)  # type: ignore
        )
        if response.stream_info.error:
            raise RuntimeError(f"Motor Error: {response.stream_info.error}")
        return response.register_value, response.mode_of_operation, response.stream_info

    async def motor_write(
        self, address: int, width: Literal[1] | Literal[2], data: int
    ):
        response: OrcaStreamWriteResponsePDU = await self.__client.execute(
            False, OrcaStreamWriteRequestPDU(address, width, data, dev_id=self.__dev_id)  # type: ignore
        )
        if response.stream_info.error:
            raise RuntimeError(f"Motor Error: {response.stream_info.error}")
        return response.stream_info

    async def tune_pid_controller(self, p: int, i: int, dv: int, de: int, sat: int):
        sat_lo, sat_hi = _int32_to_uint16s(sat)
        await self.motor_write(
            ORCA_REGISTER.PC_PGAIN.value.address, ORCA_REGISTER.PC_PGAIN.value.width, p
        )
        await self.motor_write(
            ORCA_REGISTER.PC_IGAIN.value.address, ORCA_REGISTER.PC_IGAIN.value.width, i
        )
        await self.motor_write(
            ORCA_REGISTER.PC_DVGAIN.value.address,
            ORCA_REGISTER.PC_DVGAIN.value.width,
            dv,
        )
        await self.motor_write(
            ORCA_REGISTER.PC_DEGAIN.value.address,
            ORCA_REGISTER.PC_DEGAIN.value.width,
            de,
        )
        await self.motor_write(
            ORCA_REGISTER.PC_FSATU.value.address,
            ORCA_REGISTER.PC_FSATU.value.width,
            sat_lo,
        )
        return await self.motor_write(
            ORCA_REGISTER.PC_FSATU_H.value.address,
            ORCA_REGISTER.PC_FSATU_H.value.width,
            sat_hi,
        )
