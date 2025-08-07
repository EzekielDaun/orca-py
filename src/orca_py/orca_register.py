from enum import Enum
from collections import namedtuple

Register = namedtuple("Register", ["address", "width"])


# Define the ORCA_REGISTER as an Enum
class ORCA_REGISTER(Enum):
    CTRL_REG_0 = Register(address=0, width=1)  # Control Register 1
    CTRL_REG_1 = Register(address=1, width=1)  # Control Register 2
    CTRL_REG_2 = Register(address=2, width=1)  # Control Register 3
    CTRL_REG_3 = Register(address=3, width=1)  # Control Register 4
    CTRL_REG_4 = Register(address=4, width=1)  # Control Register 5
    CTRL_REG_5 = Register(address=5, width=1)  # Control Register 6
    CTRL_REG_6 = Register(address=6, width=1)  # Control Register 7
    CTRL_REG_7 = Register(address=7, width=1)  # Control Register 8
    GUI_PERIOD_CMD = Register(
        address=8, width=1
    )  # Commanded period between IrisControls GUI frames in milliseconds.
    KIN_SW_TRIGGER = Register(
        address=9, width=1
    )  # Software trigger for initiating kinematic movements over Modbus.

    # Non-contiguous addresses. 10 free registers. 10 - 19

    HBA_DUTY_CMD = Register(
        address=20, width=1
    )  # Manual control of Hbridge A duty (-32767 to 32767)
    HBB_DUTY_CMD = Register(
        address=21, width=1
    )  # Manual control of Hbridge B duty (-32767 to 32767)
    HBC_DUTY_CMD = Register(
        address=22, width=1
    )  # Manual control of Hbridge C duty (-32767 to 32767)
    HBD_DUTY_CMD = Register(
        address=23, width=1
    )  # Manual control of Hbridge D duty (-32767 to 32767)
    HBA_CURRENT_CMD = Register(
        address=24, width=1
    )  # Manual control of Hbridge A current in mA
    HBB_CURRENT_CMD = Register(
        address=25, width=1
    )  # Manual control of Hbridge B current in mA
    HBC_CURRENT_CMD = Register(
        address=26, width=1
    )  # Manual control of Hbridge C current in mA
    HBD_CURRENT_CMD = Register(
        address=27, width=1
    )  # Manual control of Hbridge D current in mA
    FORCE_CMD = Register(
        address=28, width=1
    )  # Commanded actuator output force in millinewtons. Lower 2 bytes.
    FORCE_CMD_H = Register(
        address=29, width=1
    )  # Commanded actuator output force in millinewtons. Upper 2 bytes.
    POSITION_CMD = Register(
        address=30, width=1
    )  # Commanded actuator position in encoder counts. Lower 2 bytes.
    POSITION_CMD_H = Register(
        address=31, width=1
    )  # Commanded actuator position in encoder counts. Upper 2 bytes.

    # Non-contiguous addresses. 1 free registers. 32 - 32

    STATOR_CAL_VERSION = Register(address=33, width=1)  # Stator calibration version.
    BS_GAIN_CMD = Register(address=34, width=1)  # Hall sensor analog circuit gain.
    CS_GAIN_CMD = Register(address=35, width=1)  # Current sensor analog circuit gain.
    H0Z = Register(address=36, width=1)  # Saved zero value for Hall sensor 0.
    H1Z = Register(address=37, width=1)  # Saved zero value for Hall sensor 1.
    H2Z = Register(address=38, width=1)  # Saved zero value for Hall sensor 2.
    H3Z = Register(address=39, width=1)  # Saved zero value for Hall sensor 3.
    H4Z = Register(address=40, width=1)  # Saved zero value for Hall sensor 4.
    H5Z = Register(address=41, width=1)  # Saved zero value for Hall sensor 5.
    H6Z = Register(address=42, width=1)  # Saved zero value for Hall sensor 6.
    H7Z = Register(address=43, width=1)  # Saved zero value for Hall sensor 7.
    C0Z = Register(address=44, width=1)  # Saved zero value for current sensor 0.
    C1Z = Register(address=45, width=1)  # Saved zero value for current sensor 1.
    C2Z = Register(address=46, width=1)  # Saved zero value for current sensor 2.
    C3Z = Register(address=47, width=1)  # Saved zero value for current sensor 3.
    C4Z = Register(address=48, width=1)  # Saved zero value for current sensor 4.
    C5Z = Register(address=49, width=1)  # Saved zero value for current sensor 5.
    C6Z = Register(address=50, width=1)  # Saved zero value for current sensor 6.
    C7Z = Register(address=51, width=1)  # Saved zero value for current sensor 7.
    CTFN = Register(address=52, width=1)  # -
    R0 = Register(address=53, width=1)  # Total resistance of motor phase 0.
    R1 = Register(address=54, width=1)  # Total resistance of motor phase 1.
    R2 = Register(address=55, width=1)  # Total resistance of motor phase 2.
    R3 = Register(address=56, width=1)  # Total resistance of motor phase 3.
    I0A = Register(address=57, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I1A = Register(address=58, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I2A = Register(address=59, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I3A = Register(address=60, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I4A = Register(address=61, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I5A = Register(address=62, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I6A = Register(address=63, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I7A = Register(address=64, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I0B = Register(address=65, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I1B = Register(address=66, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I2B = Register(address=67, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I3B = Register(address=68, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I4B = Register(address=69, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I5B = Register(address=70, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I6B = Register(address=71, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I7B = Register(address=72, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I0C = Register(address=73, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I1C = Register(address=74, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I2C = Register(address=75, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I3C = Register(address=76, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I4C = Register(address=77, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I5C = Register(address=78, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I6C = Register(address=79, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I7C = Register(address=80, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I0D = Register(address=81, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I1D = Register(address=82, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I2D = Register(address=83, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I3D = Register(address=84, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I4D = Register(address=85, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I5D = Register(address=86, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I6D = Register(address=87, width=1)  # STATOR_CAL_SECTION | Width: 1 | -
    I7D = Register(address=88, width=1)  # STATOR_CAL_SECTION | Width: 1 | -

    # Non-contiguous addresses. 7 free registers. 89 - 95

    SHAFT_CAL_VERSION = Register(address=96, width=1)  # Shaft calibration version.
    H0M = Register(
        address=97, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 0.
    H1M = Register(
        address=98, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 1.
    H2M = Register(
        address=99, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 2.
    H3M = Register(
        address=100, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 3.
    H4M = Register(
        address=101, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 4.
    H5M = Register(
        address=102, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 5.
    H6M = Register(
        address=103, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 6.
    H7M = Register(
        address=104, width=1
    )  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 7.
    S45 = Register(address=105, width=1)  # SHAFT_CAL_SECTION | Width: 1 | -
    S90 = Register(address=106, width=1)  # SHAFT_CAL_SECTION | Width: 1 | -

    # Non-contiguous addresses. 5 free registers. 107 - 111

    FORCE_CAL_VERSION = Register(
        address=112, width=1
    )  # FORCE_CAL_SECTION | Width: 1 | Force calibration version.
    AAL = Register(address=113, width=1)  # FORCE_CAL_SECTION | Width: 1 | -
    BAL = Register(address=114, width=1)  # FORCE_CAL_SECTION | Width: 1 | -
    CAL = Register(address=115, width=1)  # FORCE_CAL_SECTION | Width: 1 | -
    DAL = Register(address=116, width=1)  # FORCE_CAL_SECTION | Width: 1 | -
    F30 = Register(address=117, width=1)  # FORCE_CAL_SECTION | Width: 1 | -
    F60 = Register(address=118, width=1)  # FORCE_CAL_SECTION | Width: 1 | -
    F90 = Register(address=119, width=1)  # FORCE_CAL_SECTION | Width: 1 | -

    # Non-contiguous addresses. 8 free registers. 120 - 127

    TUNING_VERSION = Register(
        address=128, width=1
    )  # TUNING_SECTION | Width: 1 | Tuning calibration version.
    CC_PGAIN = Register(
        address=129, width=1
    )  # TUNING_SECTION | Width: 1 | Current controller proportional gain.
    CC_IGAIN = Register(
        address=130, width=1
    )  # TUNING_SECTION | Width: 1 | Current controller integral gain.
    CC_FGAIN = Register(
        address=131, width=1
    )  # TUNING_SECTION | Width: 1 | Current controller forward gain.
    CC_MAX_DUTY = Register(
        address=132, width=1
    )  # TUNING_SECTION | Width: 1 | Current controller maximum duty cycle.
    PC_PGAIN = Register(
        address=133, width=1
    )  # TUNING_SECTION | Width: 1 | Position controller proportional gain.
    PC_IGAIN = Register(
        address=134, width=1
    )  # TUNING_SECTION | Width: 1 | Position controller integral gain.
    PC_DVGAIN = Register(
        address=135, width=1
    )  # TUNING_SECTION | Width: 1 | Position controller velocity gain.
    PC_DEGAIN = Register(
        address=136, width=1
    )  # TUNING_SECTION | Width: 1 | Position controller error derivative gain.
    PC_FSATU = Register(
        address=137, width=1
    )  # TUNING_SECTION | Width: 1 | Position controller maximum force output. Lower 2 bytes.
    PC_FSATU_H = Register(
        address=138, width=1
    )  # TUNING_SECTION | Width: 1 | Position controller maximum force output. Upper 2 bytes.
    USER_MAX_TEMP = Register(
        address=139, width=1
    )  # TUNING_SECTION | Width: 1 | User configurable maximum motor temperature before over temperature error in degrees Celsius.
    USER_MAX_FORCE = Register(
        address=140, width=1
    )  # TUNING_SECTION | Width: 1 | User configurable maximum force output in millinewtons. Lower 2 bytes.
    USER_MAX_FORCE_H = Register(
        address=141, width=1
    )  # TUNING_SECTION | Width: 1 | User configurable maximum force output in millinewtons. Upper 2 bytes.
    USER_MAX_POWER = Register(
        address=142, width=1
    )  # TUNING_SECTION | Width: 1 | User configurable maximum power burn in watts.
    SAFETY_DGAIN = Register(
        address=143, width=1
    )  # TUNING_SECTION | Width: 1 | Speed damping gain value used when communications are interrupted.

    # Non-contiguous addresses. 6 free registers. 144 - 149

    PC_SOFTSTART_PERIOD = Register(
        address=150, width=1
    )  # TUNING_SECTION | Width: 1 | Time in ms over which the position controller max force output will ramp from zero any time a mode of operation in which the position controller used is entered
    FORCE_UNITS = Register(
        address=151, width=1
    )  # TUNING_SECTION | Width: 1 | Determines whether forces will be interpreted in legacy unitless form or in millinewtons.

    # Non-contiguous addresses. 8 free registers. 152 - 159

    USR_OPT_VERSION = Register(
        address=160, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | User options section version.

    # Non-contiguous addresses. 1 free registers. 161 - 161

    LOG_PERIOD = Register(
        address=162, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Period between data log entries.
    USER_COMMS_TIMEOUT = Register(
        address=163, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Time between successful force or position commands before a communications error occurs. In milliseconds.
    USR_MB_BAUD_LO = Register(
        address=164, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Default Modbus baudrate low 16 bits. Leaving this register at 0 will use the system default of 19200 bps.
    USR_MB_BAUD_HI = Register(
        address=165, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Default Modbus baudrate high 16 bits. Leaving this register at 0 will use the system default of 19200 bps.
    FORCE_FILT = Register(
        address=166, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Force output IIR filter alpha value. Maps 0-65535 to alpha values of 0 to 1.
    POS_FILT = Register(
        address=167, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Position output IIR filter alpha value. Maps 0-65535 to alpha values of 0 to 1.
    USR_MB_DELAY = Register(
        address=168, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Default Modbus interframe delay in microseconds. Default value is 2000 us.
    USR_MB_ADDR = Register(
        address=169, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Start up Modbus address. Default value is 1.
    MB_RS485_MODE = Register(
        address=170, width=1
    )  # USER_OPTIONS_SECTION | Width: 1 | Determines whether the Modbus transmitter will be disabled during reception to enable RS485 compliant communications.

    # Non-contiguous addresses. 92 free registers. 171 - 262

    UART0_UP_RATE = Register(
        address=263, width=1
    )  # COUNT_SECTION | Width: 1 | Number of bytes transmitted in the last second by UART0.
    UART1_UP_RATE = Register(
        address=264, width=1
    )  # COUNT_SECTION | Width: 1 | Number of bytes transmitted in the last second by UART1.
    UART0_DOWN_RATE = Register(
        address=265, width=1
    )  # COUNT_SECTION | Width: 1 | Number of bytes received in the last second by UART0.
    UART1_DOWN_RATE = Register(
        address=266, width=1
    )  # COUNT_SECTION | Width: 1 | Number of bytes received in the last second by UART1.
    GUI_DROPPED_FRAMES = Register(
        address=267, width=1
    )  # COUNT_SECTION | Width: 1 | Total number of skipped IrisControls GUI transactions.
    GUI_DROPPED_FPS = Register(
        address=268, width=1
    )  # COUNT_SECTION | Width: 1 | Number of dropped frames per second.
    LOOP_FREQ = Register(
        address=269, width=1
    )  # COUNT_SECTION | Width: 1 | Main loop run frequency in kilohertz.
    SHAFT_CAL_COUNT = Register(address=270, width=1)  # COUNT_SECTION | Width: 1 | -
    STATOR_CAL_COUNT = Register(address=271, width=1)  # COUNT_SECTION | Width: 1 | -
    MOTOR_FRAME_COUNT = Register(
        address=272, width=1
    )  # COUNT_SECTION | Width: 1 | Number of complete motor frames in the last second.
    MB_FREQ = Register(
        address=273, width=1
    )  # COUNT_SECTION | Width: 1 | Number of successful Modbus messages in the last second.

    # Non-contiguous addresses. 39 free registers. 274 - 312

    GUI_PERIOD = Register(
        address=313, width=1
    )  # STATUS_SECTION | Width: 1 | Period between IrisControls GUI communications in milliseconds.
    SHAFT_SIGNAL_STR = Register(address=314, width=1)  # STATUS_SECTION | Width: 1 | -
    BS_GAIN_ACT = Register(
        address=315, width=1
    )  # STATUS_SECTION | Width: 1 | Hall sensor analog circuit gain.
    CS_GAIN_ACT = Register(
        address=316, width=1
    )  # STATUS_SECTION | Width: 1 | Current sensor analog circuit gain.
    MODE_OF_OPERATION = Register(
        address=317, width=1
    )  # STATUS_SECTION | Width: 1 | Active mode the actuator is currently running in.
    CALIBRATION_STATUS = Register(
        address=318, width=1
    )  # STATUS_SECTION | Width: 1 | A value other than zero indicates a calibration routine is in process.
    KINEMATIC_STATUS = Register(
        address=319, width=1
    )  # STATUS_SECTION | Width: 1 | Indicates the state of the kinematic controller, and which motion is currently being performed.
    HBA_TARGET = Register(
        address=320, width=1
    )  # STATUS_SECTION | Width: 1 | Active Hbridge A target duty cycle value. Ranges from -32768 to 32767.
    HBB_TARGET = Register(
        address=321, width=1
    )  # STATUS_SECTION | Width: 1 | Active Hbridge B target duty cycle value. Ranges from -32768 to 32767.
    HBC_TARGET = Register(
        address=322, width=1
    )  # STATUS_SECTION | Width: 1 | Active Hbridge C target duty cycle value. Ranges from -32768 to 32767.
    HBD_TARGET = Register(
        address=323, width=1
    )  # STATUS_SECTION | Width: 1 | Active Hbridge D target duty cycle value. Ranges from -32768 to 32767.
    CCA_TARGET = Register(
        address=324, width=1
    )  # STATUS_SECTION | Width: 1 | Active current controller Hbridge A target current value in milliamps.
    CCB_TARGET = Register(
        address=325, width=1
    )  # STATUS_SECTION | Width: 1 | Active current controller Hbridge B target current value in milliamps.
    CCC_TARGET = Register(
        address=326, width=1
    )  # STATUS_SECTION | Width: 1 | Active current controller Hbridge C target current value in milliamps.
    CCD_TARGET = Register(
        address=327, width=1
    )  # STATUS_SECTION | Width: 1 | Active current controller Hbridge D target currentfrom collections import namedtuple
    FC_TARGET = Register(
        address=328, width=1
    )  # STATUS_SECTION | Width: 1 | Active force controller target force value in millinewtons.
    FC_TARGET_H = Register(
        address=329, width=1
    )  # STATUS_SECTION | Width: 1 | Active force controller target force value in millinewtons. High 2 bytes.
    PC_TARGET = Register(
        address=330, width=1
    )  # STATUS_SECTION | Width: 1 | Active position controller target position value in micrometers. Low 2 bytes.
    PC_TARGET_H = Register(
        address=331, width=1
    )  # STATUS_SECTION | Width: 1 | Active position controller target position value in micrometers. High 2 bytes.

    # Non-contiguous addresses. 4 free registers. 332 - 335

    STATOR_TEMP = Register(
        address=336, width=1
    )  # SENSOR_SECTION | Width: 1 | Current stator temperature in degrees Celsius.
    DRIVER_TEMP = Register(
        address=337, width=1
    )  # SENSOR_SECTION | Width: 1 | Temperature of the motor driver in degrees Celsius.
    VDD_FINAL = Register(
        address=338, width=1
    )  # SENSOR_SECTION | Width: 1 | Motor supply voltage in volts.
    SHAFT_PHASE_FINAL = Register(address=339, width=1)  # SENSOR_SECTION | Width: 1 | -
    SHAFT_PIXEL = Register(address=340, width=1)  # SENSOR_SECTION | Width: 1 | -
    SHAFT_PIXEL_H = Register(address=341, width=1)  # SENSOR_SECTION | Width: 1 | -
    SHAFT_POS_UM = Register(
        address=342, width=1
    )  # SENSOR_SECTION | Width: 1 | Shaft absolute position in micrometers. Lower 2 bytes.
    SHAFT_POSITION_H = Register(
        address=343, width=1
    )  # SENSOR_SECTION | Width: 1 | Shaft absolute position in micrometers. Upper 2 bytes.
    SHAFT_SPEED_MMPS = Register(
        address=344, width=1
    )  # SENSOR_SECTION | Width: 1 | Shaft speed in millimeters per second. Lower 2 bytes.
    SHAFT_SHEED_H = Register(
        address=345, width=1
    )  # SENSOR_SECTION | Width: 1 | Shaft speed in millimeters per second. Upper 2 bytes.
    SHAFT_ACCEL_MMPSS = Register(
        address=346, width=1
    )  # SENSOR_SECTION | Width: 1 | Shaft acceleration in millimeters per second per second. Lower 2 bytes.
    SHAFT_ACCEL_H = Register(
        address=347, width=1
    )  # SENSOR_SECTION | Width: 1 | Shaft acceleration in millimeters per second per second. Upper 2 bytes.
    FORCE = Register(
        address=348, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed actuator output force in millinewtons. Lower 2 bytes.
    FORCE_H = Register(
        address=349, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed actuator output force in millinewtons. Upper 2 bytes.
    POWER = Register(
        address=350, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed actuator output power in watts.
    HBA_CURRENT = Register(
        address=351, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge A, in milliamps.
    HBB_CURRENT = Register(
        address=352, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge B, in milliamps.
    HBC_CURRENT = Register(
        address=353, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge C, in milliamps.
    HBD_CURRENT = Register(
        address=354, width=1
    )  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge D, in milliamps.
    AVG_POWER = Register(
        address=355, width=1
    )  # SENSOR_SECTION | Width: 1 | Average sensed actuator output power in watts.
    COIL_TEMP = Register(
        address=356, width=1
    )  # SENSOR_SECTION | Width: 1 | Estimated coil temperature in degrees Celsius.

    # Non-contiguous addresses. 7 free registers. 357 - 363

    RAW_LOCK = Register(address=364, width=1)  # RAW_SECTION | Width: 1 |
    H0_RAW = Register(address=365, width=1)  # RAW_SECTION | Width: 1 |
    H1_RAW = Register(address=366, width=1)  # RAW_SECTION | Width: 1 |
    H2_RAW = Register(address=367, width=1)  # RAW_SECTION | Width: 1 |
    H3_RAW = Register(address=368, width=1)  # RAW_SECTION | Width: 1 |
    H4_RAW = Register(address=369, width=1)  # RAW_SECTION | Width: 1 |
    H5_RAW = Register(address=370, width=1)  # RAW_SECTION | Width: 1 |
    H6_RAW = Register(address=371, width=1)  # RAW_SECTION | Width: 1 |
    H7_RAW = Register(address=372, width=1)  # RAW_SECTION | Width: 1 |
    C0_RAW = Register(address=373, width=1)  # RAW_SECTION | Width: 1 |
    C1_RAW = Register(address=374, width=1)  # RAW_SECTION | Width: 1 |
    C2_RAW = Register(address=375, width=1)  # RAW_SECTION | Width: 1 |
    C3_RAW = Register(address=376, width=1)  # RAW_SECTION | Width: 1 |
    C4_RAW = Register(address=377, width=1)  # RAW_SECTION | Width: 1 |
    C5_RAW = Register(address=378, width=1)  # RAW_SECTION | Width: 1 |
    C6_RAW = Register(address=379, width=1)  # RAW_SECTION | Width: 1 |
    C7_RAW = Register(address=380, width=1)  # RAW_SECTION | Width: 1 |
    VDD_RAW = Register(address=381, width=1)  # RAW_SECTION | Width: 1 |
    T0_RAW = Register(address=382, width=1)  # RAW_SECTION | Width: 1 |
    T1_RAW = Register(address=383, width=1)  # RAW_SECTION | Width: 1 |
    T2_RAW = Register(address=384, width=1)  # RAW_SECTION | Width: 1 |
    T3_RAW = Register(address=385, width=1)  # RAW_SECTION | Width: 1 |

    # Non-contiguous addresses. 14 free registers. 386 - 399

    PARAM_VERSION = Register(
        address=400, width=1
    )  # PARAM_SECTION | Width: 1 | Parameter calibration version.
    MAX_TEMP = Register(
        address=401, width=1
    )  # PARAM_SECTION | Width: 1 | Absolute maximum motor temperature before over temperature error.
    MIN_VOLTAGE = Register(
        address=402, width=1
    )  # PARAM_SECTION | Width: 1 | Minimum motor voltage in volts before invalid voltage error.
    MAX_VOLTAGE = Register(
        address=403, width=1
    )  # PARAM_SECTION | Width: 1 | Maximum motor voltage in volts before invalid voltage error.
    MAX_CURRENT = Register(
        address=404, width=1
    )  # PARAM_SECTION | Width: 1 | Maximum motor current output in milliamps.
    MAX_POWER = Register(
        address=405, width=1
    )  # PARAM_SECTION | Width: 1 | Maximum motor power burn in watts.
    SERIAL_NUMBER_LOW = Register(
        address=406, width=1
    )  # PARAM_SECTION | Width: 1 | Actuator serial number. Lower 2 bytes.
    SERIAL_NUMBER_HIGH = Register(
        address=407, width=1
    )  # PARAM_SECTION | Width: 1 | Actuator serial number. Upper 2 bytes.
    MAJOR_VERSION = Register(
        address=408, width=1
    )  # PARAM_SECTION | Width: 1 | Firmware major version.
    RELEASE_STATE = Register(
        address=409, width=1
    )  # PARAM_SECTION | Width: 1 | Firmware minor version.
    REVISION_NUMBER = Register(
        address=410, width=1
    )  # PARAM_SECTION | Width: 1 | Firmware revision number.
    COMMIT_ID_LO = Register(
        address=411, width=1
    )  # PARAM_SECTION | Width: 1 | Firmware commit ID lower 2 bytes.
    COMMIT_ID_HI = Register(
        address=412, width=1
    )  # PARAM_SECTION | Width: 1 | Firmware commit ID upper 2 bytes.
    CC_MIN_CURRENT = Register(
        address=413, width=1
    )  # PARAM_SECTION | Width: 1 | Current controller minimum current output in milliamps.
    HW_VERSION = Register(
        address=414, width=1
    )  # PARAM_SECTION | Width: 1 | Target hardware version for this firmware.
    PWM_FREQ = Register(
        address=415, width=1
    )  # PARAM_SECTION | Width: 1 | Frequency of the PWM signals in hertz.
    ADC_FREQ = Register(
        address=416, width=1
    )  # PARAM_SECTION | Width: 1 | Frequency of the sensor data acquisition loop in hertz.
    COMMS_TIMEOUT = Register(
        address=417, width=1
    )  # PARAM_SECTION | Width: 1 | Time between successful force or position commands before a communications error occurs. In milliseconds.
    STATOR_CONFIG = Register(
        address=418, width=1
    )  # PARAM_SECTION | Width: 1 | Physical stator configuration type.

    # Non-contiguous addresses. 13 free registers. 419 - 431

    ERROR_0 = Register(
        address=432, width=1
    )  # ERROR_SECTION | Width: 1 | Currently active error flags. Only reflects error conditions that have not been cleared.
    ERROR_1 = Register(
        address=433, width=1
    )  # ERROR_SECTION | Width: 1 | Currently active error flags. Only reflects error conditions that have not been cleared.
    RX_TDRE_ERROR = Register(address=434, width=1)  # ERROR_SECTION | Width: 1 |
    RX_TC_ERROR = Register(address=435, width=1)  # ERROR_SECTION | Width: 1 |
    TX_RDRF_ERROR = Register(address=436, width=1)  # ERROR_SECTION | Width: 1 |
    ADC_DATA_COLLISION = Register(address=437, width=1)  # ERROR_SECTION | Width: 1 |

    # Non-contiguous addresses. 26 free registers. 438 - 463

    MB_CNT0 = Register(
        address=464, width=1
    )  # MODBUS_SECTION | Width: 1 | Return bus message count. Refer to Modbus specification.
    MB_CNT1 = Register(
        address=465, width=1
    )  # MODBUS_SECTION | Width: 1 | Return bus communication error. Refer to Modbus specification.
    MB_CNT2 = Register(
        address=466, width=1
    )  # MODBUS_SECTION | Width: 1 | Return server exception error count. Refer to Modbus specification.
    MB_CNT3 = Register(
        address=467, width=1
    )  # MODBUS_SECTION | Width: 1 | Return server message count. Refer to Modbus specification.
    MB_CNT4 = Register(
        address=468, width=1
    )  # MODBUS_SECTION | Width: 1 | Return server no response count. Refer to Modbus specification.
    MB_CNT5 = Register(
        address=469, width=1
    )  # MODBUS_SECTION | Width: 1 | Return server NAK count. Refer to Modbus specification.
    MB_CNT6 = Register(
        address=470, width=1
    )  # MODBUS_SECTION | Width: 1 | Return server busy count. Refer to Modbus specification.
    MB_CNT7 = Register(
        address=471, width=1
    )  # MODBUS_SECTION | Width: 1 | Return bus character overrun count. Refer to Modbus specification.
    MB_CNT8 = Register(
        address=472, width=1
    )  # MODBUS_SECTION | Width: 1 | Rx line error.
    MB_CNT9 = Register(
        address=473, width=1
    )  # MODBUS_SECTION | Width: 1 | Ignoring state error.
    MB_CNT10 = Register(
        address=474, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected interchar.
    MB_CNT11 = Register(
        address=475, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected interframe.
    MB_CNT12 = Register(
        address=476, width=1
    )  # MODBUS_SECTION | Width: 1 | Timeout sequence error.
    MB_CNT13 = Register(
        address=477, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected interframe.
    MB_CNT14 = Register(
        address=478, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected reception.
    MB_CNT15 = Register(
        address=479, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected reception.
    MB_CNT16 = Register(
        address=480, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected reception.
    MB_CNT17 = Register(
        address=481, width=1
    )  # MODBUS_SECTION | Width: 1 | Unexpected interframe.
    MB_BAUD = Register(
        address=482, width=1
    )  # MODBUS_SECTION | Width: 1 | Modbus serial baudrate. Lower 2 bytes.
    MB_BAUD_H = Register(
        address=483, width=1
    )  # MODBUS_SECTION | Width: 1 | Modbus serial baudrate. Upper 2 bytes.
    MB_IF_DELAY = Register(
        address=484, width=1
    )  # MODBUS_SECTION | Width: 1 | Modbus interframe delay in microseconds.
    MB_ADDRESS = Register(
        address=485, width=1
    )  # MODBUS_SECTION | Width: 1 | Modbus server address.

    # Non-contiguous addresses. 10 free registers. 486 - 495

    MESSAGE_0_SIZE = Register(
        address=496, width=1
    )  # MODBUS_SECTION | Width: 1 | Size of last received Modbus message in bytes.
    MESSAGE_0 = Register(address=497, width=128)  # MODBUS_SECTION | Width: 128 | -
    HAPTIC_VERSION = 640  # HAPTIC_SECTION | Width: 1 | Haptic configuration version.

    # Non-contiguous addresses. 15 free registers. 641 - 640

    HAPTIC_STATUS = Register(
        address=641, width=1
    )  # HAPTIC_SECTION | Width: 1 | Enabled state of effects.
    CONSTANT_FORCE_MN = Register(
        address=642, width=1
    )  # HAPTIC_SECTION | Width: 1 | Value of constant force effect in milliwnewtons, low 2 bytes.
    CONSTANT_FORCE_MN_H = Register(
        address=643, width=1
    )  # HAPTIC_SECTION | Width: 1 | Value of constant force effect in milliwnewtons, high 2 bytes
    S0_GAIN_N_MM = Register(
        address=644, width=1
    )  # HAPTIC_SECTION | Width: 1 | Strength of spring force
    S0_CENTER_UM = Register(
        address=645, width=1
    )  # HAPTIC_SECTION | Width: 1 | Location of spring center, low 2 bytes
    S0_CENTER_UM_H = Register(
        address=646, width=1
    )  # HAPTIC_SECTION | Width: 1 | Location of spring center, high 2 bytes
    S0_COUPLING = Register(
        address=647, width=1
    )  # HAPTIC_SECTION | Width: 1 | Coupling type, 0 (Both), 1 (Positive), 2 (Negative),
    S0_DEAD_ZONE_MM = Register(
        address=648, width=1
    )  # HAPTIC_SECTION | Width: 1 | Zone from center where no spring effect exists
    S0_FORCE_SAT_N = Register(
        address=649, width=1
    )  # HAPTIC_SECTION | Width: 1 | Maximum force that the spring can output
    S1_GAIN_N_MM = Register(
        address=650, width=1
    )  # HAPTIC_SECTION | Width: 1 | Strength of spring force
    S1_CENTER_UM = Register(
        address=651, width=1
    )  # HAPTIC_SECTION | Width: 1 | Location of spring center, low 2 bytes
    S1_CENTER_UM_H = Register(
        address=652, width=1
    )  # HAPTIC_SECTION | Width: 1 | Location of spring center, high 2 bytes
    S1_COUPLING = Register(
        address=653, width=1
    )  # HAPTIC_SECTION | Width: 1 | Coupling type, 0 (Both), 1 (Positive), 2 (Negative),
    S1_DEAD_ZONE_MM = Register(
        address=654, width=1
    )  # HAPTIC_SECTION | Width: 1 | Zone from center where no spring effect exists
    S1_FORCE_SAT_N = Register(
        address=655, width=1
    )  # HAPTIC_SECTION | Width: 1 | Maximum force that the spring can output
    S2_GAIN_N_MM = Register(
        address=656, width=1
    )  # HAPTIC_SECTION | Width: 1 | Strength of spring force
    S2_CENTER_UM = Register(
        address=657, width=1
    )  # HAPTIC_SECTION | Width: 1 | Location of spring center, low 2 bytes
    S2_CENTER_UM_H = Register(
        address=658, width=1
    )  # HAPTIC_SECTION | Width: 1 | Location of spring center, high 2 bytes
    S2_COUPLING = Register(
        address=659, width=1
    )  # HAPTIC_SECTION | Width: 1 | Coupling type, 0 (Both), 1 (Positive), 2 (Negative),
    S2_DEAD_ZONE_MM = Register(
        address=660, width=1
    )  # HAPTIC_SECTION | Width: 1 | Zone from center where no spring effect exists
    S2_FORCE_SAT_N = Register(
        address=661, width=1
    )  # HAPTIC_SECTION | Width: 1 | Maximum force that the spring can output
    D0_GAIN_NS_MM = Register(
        address=662, width=1
    )  # HAPTIC_SECTION | Width: 1 | Strength of damping force
    I0_GAIN_NS2_MM = Register(
        address=663, width=1
    )  # HAPTIC_SECTION | Width: 1 | Strength of inertia force
    O0_GAIN_N = Register(
        address=664, width=1
    )  # HAPTIC_SECTION | Width: 1 | Amplitude of periodic effect
    O0_TYPE = Register(
        address=665, width=1
    )  # HAPTIC_SECTION | Width: 1 | Type of periodic effect 0 (square), 1 (sine), 2 (triangle), 3 (sawtooth)
    O0_FREQ_DHZ = Register(
        address=666, width=1
    )  # HAPTIC_SECTION | Width: 1 | Period of oscillation
    O0_DUTY = Register(
        address=667, width=1
    )  # HAPTIC_SECTION | Width: 1 | Pulse width modulation of signal as a % of duty cycle max value
    O1_GAIN_N = Register(
        address=668, width=1
    )  # HAPTIC_SECTION | Width: 1 | Amplitude of periodic effect
    O1_TYPE = Register(
        address=669, width=1
    )  # HAPTIC_SECTION | Width: 1 | Type of periodic effect 0 (square), 1 (sine), 2 (triangle), 3 (sawtooth)
    O1_FREQ_DHZ = Register(
        address=670, width=1
    )  # HAPTIC_SECTION | Width: 1 | Frequency of periodic effect
    O1_DUTY = Register(
        address=671, width=1
    )  # HAPTIC_SECTION | Width: 1 | Pulse width modulation of signal as a % of duty cycle max value
    CONST_FORCE_FILTER = Register(
        address=672, width=1
    )  # HAPTIC_SECTION | Width: 1 | Amount of filtering on constant force inputs.

    # Non-contiguous addresses. 82 free registers. 673 - 754

    ILOOP_MSG_FLAG = Register(
        address=755, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Flag produced by receiving a Seagull modbus command and consumed by the current loop controller
    ILOOP_DIN = Register(
        address=756, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Status of Ceagle digital inputs. Each input represented by a bit.
    ILOOP_OUT_CH1 = Register(
        address=757, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | 4-20 mA output channel 1.
    ILOOP_OUT_CH2 = Register(
        address=758, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | 4-20 mA output channel 2.
    ILOOP_IN = Register(
        address=759, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | 4-20 mA input.
    ILOOP_SECTION_VERSION = 760  # CURRENT_LOOP_SECTION | Width: 1 |
    ILOOP_CONFIG = Register(
        address=761, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Configuration for 4-20mA control.
    ILOOP_FORCE_MIN = Register(
        address=762, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 4 mA. Low 2 bytes. In millinewtons.
    ILOOP_FORCE_MIN_HI = Register(
        address=763, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 4 mA. High 2 bytes. In millinewtons.
    ILOOP_FORCE_MAX = Register(
        address=764, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 20 mA. Low 2 bytes. In millinewtons.
    ILOOP_FORCE_MAX_HI = Register(
        address=765, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 20 mA. High 2 bytes. In millinewtons.
    ILOOP_POS_MIN = Register(
        address=766, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 4 mA. Low 2 bytes. In micrometers.
    ILOOP_POS_MIN_HI = Register(
        address=767, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 4 mA. High 2 bytes. In micrometers.
    ILOOP_POS_MAX = Register(
        address=768, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 20 mA. Low 2 bytes. In micrometers.
    ILOOP_POS_MAX_HI = Register(
        address=769, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 20 mA. High 2 bytes. In micrometers.
    ILOOP_KIN_TYPE = Register(
        address=770, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Type of trigger behaviour
    ILOOP_D0_HIGH = Register(
        address=771, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for rising edge digital 0
    ILOOP_D0_LOW = Register(
        address=772, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for falling edge digital 0
    ILOOP_D2_HIGH = Register(
        address=773, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for rising edge digital 1
    ILOOP_D2_LOW = Register(
        address=774, width=1
    )  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for falling edge digital 1

    # Non-contiguous addresses. 3 free registers. 775 - 777

    KINEMATIC_SECTION_VERSION = Register(
        address=778, width=1
    )  # KINEMATIC_SECTION | Width: 1 | Kinematic controller configuration.
    KIN_CONFIG = Register(
        address=779, width=1
    )  # KINEMATIC_SECTION | Width: 1 | Kinematic controller configuration.
    KIN_MOTION_0 = Register(address=780, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_1 = Register(address=786, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_2 = Register(address=792, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_3 = Register(address=798, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_4 = Register(address=804, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_5 = Register(address=810, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_6 = Register(address=816, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_7 = Register(address=822, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_8 = Register(address=828, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_9 = Register(address=834, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_10 = Register(address=840, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_11 = Register(address=846, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_12 = Register(address=852, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_13 = Register(address=858, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_14 = Register(address=864, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_15 = Register(address=870, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_16 = Register(address=876, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_17 = Register(address=882, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_18 = Register(address=888, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_19 = Register(address=894, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_20 = Register(address=900, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_21 = Register(address=906, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_22 = Register(address=912, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_23 = Register(address=918, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_24 = Register(address=924, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_25 = Register(address=930, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_26 = Register(address=936, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_27 = Register(address=942, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_28 = Register(address=948, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_29 = Register(address=954, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_30 = Register(address=960, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_31 = Register(address=966, width=6)  # KINEMATIC_SECTION | Width: 6 |
    KIN_HOME_ID = Register(
        address=972, width=1
    )  # KINEMATIC_SECTION | Width: 1 | ID of kinematic motion triggered when Kinematic mode enabled or when Home signal asserved from Analog interface
