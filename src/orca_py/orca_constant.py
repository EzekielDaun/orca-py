from enum import IntEnum


class ORCA_MODE(IntEnum):
    SleepMode = 1
    ForceMode = 2
    PositionMode = 3
    HapticMode = 4
    KinematicMode = 5


class ORCA_MODE_SUBCODE(IntEnum):
    ForceControlStream = 0x1C
    PositionControlStream = 0x1E
    KinematicDataStream = 0x20
    HapticDataStream = 0x22
    SleepDataStream = 0x00  # all else


class ORCA_ERROR(IntEnum):
    ConfigurationError = 0x001F
    ForceClipping = 0x0020
    TemperatureExceeded = 0x0040
    ForceExceeded = 0x0080
    PowerExceeded = 0x0100
    ShaftImageFailed = 0x0200
    VoltageInvalid = 0x0400
    CommsTimeout = 0x0800
