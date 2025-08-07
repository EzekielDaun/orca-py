import struct
from dataclasses import dataclass
from typing import Literal

from pymodbus.pdu import ModbusPDU

from .orca_constant import ORCA_ERROR, ORCA_MODE, ORCA_MODE_SUBCODE


# ========== Start of Management PDU ==========
class OrcaStreamManageResponsePDU(ModbusPDU):
    function_code = 0x41

    def decode(self, data):
        data = data[2:]  # skip the 2-byte sub code
        self.__baudrate, self.__delay = struct.unpack(">IH", data)

    @classmethod
    def calculateRtuFrameSize(cls, _data: bytes):
        # 1 addr + 1 func + 2 sub_func + 4 baud rate + 2 delay + 2 crc
        return 12

    @property
    def baudrate(self):
        return self.__baudrate

    @property
    def delay(self):
        return self.__delay


class OrcaStreamManageRequestPDU(ModbusPDU):
    function_code = 0x41
    rtu_frame_size = 12  # 1 addr + 1 func + 2 sub_func + 4 baud rate + 2 delay + 2 crc

    def __init__(self, enable: bool, baudrate: int, delay: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__enable = enable
        self.__baudrate = baudrate
        self.__delay = delay

    def encode(self):
        return struct.pack(
            ">HIH", 0xFF00 if self.__enable else 0x0000, self.__baudrate, self.__delay
        )


# ========== End of Management PDU ==========


@dataclass(frozen=True)
class OrcaStreamInfo:
    position: int
    force: int
    power: int
    temperature: int
    voltage: int
    error: list[ORCA_ERROR]

    @staticmethod
    def parse_errors(error: int):
        return [ORCA_ERROR(error & (1 << i)) for i in range(16) if error & (1 << i)]


# ========== Start of Command PDU ==========
class OrcaStreamCommandResponsePDU(ModbusPDU):
    function_code = 0x64

    def decode(self, data):
        (
            self.__position_value,  # 4 bytes
            self.__force_value,  # 4 bytes
            self.__power_value,  # 2 bytes
            self.__temperature_value,  # 1 bytes
            self.__voltage_value,  # 2 bytes
            self.__errors,  # 2 bytes
        ) = struct.unpack(">IIHBHH", data)

    @classmethod
    def calculateRtuFrameSize(cls, _data: bytes):
        # 1 addr + 1 func + ... + 2 crc
        return 19

    @property
    def stream_info(self):
        return OrcaStreamInfo(
            position=self.__position_value,
            force=self.__force_value,
            power=self.__power_value,
            temperature=self.__temperature_value,
            voltage=self.__voltage_value,
            error=OrcaStreamInfo.parse_errors(self.__errors),
        )


class OrcaStreamCommandRequestPDU(ModbusPDU):
    function_code = 0x64
    rtu_frame_size = 9  # 1 addr + 1 func + 1 sub code + 4 data + 2 crc

    def __init__(self, subcode: ORCA_MODE_SUBCODE, data: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__subcode = subcode  # 1 bytes
        self.__data = data  # 4 bytes

    def encode(self):
        return struct.pack(">Bi", self.__subcode, self.__data)


# ========== End of Command PDU ==========


# ========== Start of Read PDU ==========
class OrcaStreamReadResponsePDU(ModbusPDU):
    function_code = 0x68

    def decode(self, data):
        (
            self.__register_value,  # 4 bytes
            self.__mode_of_operation,  # 1 bytes
            self.__position_value,  # 4 bytes
            self.__force_value,  # 4 bytes
            self.__power_value,  # 2 bytes
            self.__temperature_value,  # 1 bytes
            self.__voltage_value,  # 2 bytes
            self.__errors,  # 2 bytes
        ) = struct.unpack(">IBIIHBHH", data)

    @classmethod
    def calculateRtuFrameSize(cls, _data: bytes):
        # 1 addr + 1 func + ... + 2 crc
        return 24

    @property
    def register_value(self):
        return self.__register_value

    @property
    def mode_of_operation(self):
        return ORCA_MODE(self.__mode_of_operation)

    @property
    def stream_info(self):
        return OrcaStreamInfo(
            position=self.__position_value,
            force=self.__force_value,
            power=self.__power_value,
            temperature=self.__temperature_value,
            voltage=self.__voltage_value,
            error=OrcaStreamInfo.parse_errors(self.__errors),
        )


class OrcaStreamReadRequestPDU(ModbusPDU):
    function_code = 0x68
    rtu_frame_size = 7  # 1 addr + 1 func + 2 register address + 1 width + 2 crc

    def __init__(
        self,
        register_address: int,
        register_width: Literal[1] | Literal[2],
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.__register_address = register_address  # 2 bytes
        self.__register_width = register_width  # 1 bytes

    def encode(self):
        return struct.pack(">HB", self.__register_address, self.__register_width)


# ========== End of Read PDU ==========


# ========== Start of Write PDU ==========
class OrcaStreamWriteResponsePDU(ModbusPDU):
    function_code = 0x69

    def decode(self, data):
        (
            self.__mode_of_operation,  # 1 bytes
            self.__position_value,  # 4 bytes
            self.__force_value,  # 4 bytes
            self.__power_value,  # 2 bytes
            self.__temperature_value,  # 1 bytes
            self.__voltage_value,  # 2 bytes
            self.__errors,  # 2 bytes
        ) = struct.unpack(">BIIHBHH", data)

    @classmethod
    def calculateRtuFrameSize(cls, _data: bytes):
        # 1 addr + 1 func + ... + 2 crc
        return 20

    @property
    def mode_of_operation(self):
        return ORCA_MODE(self.__mode_of_operation)

    @property
    def stream_info(self):
        return OrcaStreamInfo(
            position=self.__position_value,
            force=self.__force_value,
            power=self.__power_value,
            temperature=self.__temperature_value,
            voltage=self.__voltage_value,
            error=OrcaStreamInfo.parse_errors(self.__errors),
        )


class OrcaStreamWriteRequestPDU(ModbusPDU):
    function_code = 0x69
    rtu_frame_size = (
        7  # 1 addr + 1 func + 2 register address + 1 width + 4 data + 2 crc
    )

    def __init__(
        self,
        register_address: int,
        register_width: Literal[1] | Literal[2],
        data: int,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.__register_address = register_address  # 2 bytes
        self.__register_width = register_width  # 1 bytes
        self.__data = data  # 4 bytes

    def encode(self):
        return struct.pack(
            ">HBi", self.__register_address, self.__register_width, self.__data
        )


# ========== End of Write PDU ==========
