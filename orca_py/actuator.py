import struct

from pymodbus.client.serial import AsyncModbusSerialClient

from .orca_constant import ORCA_MODE
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
    async def create(cls, comport: str):
        """
        Asynchronous factory method to initialize the class with an asynchronous operation.
        """
        actuator = cls(comport)
        await actuator.__client.connect()
        return actuator

    # do not directly instantiate this class
    def __init__(self, comport: str):
        self.__client = AsyncModbusSerialClient(
            comport, parity="E", baudrate=921600, timeout=0.1, retries=3
        )

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

    # TODO: read/write motor streams

    ################################
    # Orca Functions
    ################################

    # Change Orca's mode of operation
    async def set_mode(self, mode: ORCA_MODE):
        return await self.write_register(ORCA_REGISTER.CTRL_REG_3, mode)

    async def get_mode(self):
        return ORCA_MODE(
            (await self.read_registers(ORCA_REGISTER.MODE_OF_OPERATION)).registers[0]
        )

    # Trigger Kinematic Motion
    async def kinematic_trigger(self, motion_id: int):
        return await self.write_register(ORCA_REGISTER.KIN_SW_TRIGGER, motion_id)

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
            ORCA_REGISTER.KIN_MOTION_0 + motionID * 6, configuration
        )

    # Tune PID Values
    async def tune_pid_controller(self, saturation, p_gain, i_gain, dv_gain, de_gain):
        # saturationL_H = obj.int32_to_u16(saturation); %split 32 bit into 2 16 bit, low first hi second
        # configuration = [p_gain, i_gain, dv_gain, de_gain , saturationL_H];
        # obj.write_multi_registers(133, 6, configuration);  % PC_PGAIN 133, num consecutive registers 6, register values  configuration
        saturationL, saturationH = _int32_to_uint16s(saturation)
        configuration = [p_gain, i_gain, dv_gain, de_gain, saturationL, saturationH]
        return await self.write_multi_registers(ORCA_REGISTER.PC_PGAIN, configuration)

    # Check Kinematic Status
    async def kinematic_status(self):
        return await self.read_registers(ORCA_REGISTER.KINEMATIC_STATUS)
