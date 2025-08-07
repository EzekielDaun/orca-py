import asyncio

import numpy as np

from orca_py.actuator import Actuator
from orca_py.orca_constant import ORCA_MODE

A1_SERIAL_ADDRESS = "/dev/tty.usbserial-FT878BFG"
A2_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8ESWCO"
A3_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F0YKB"
A4_SERIAL_ADDRESS = "/dev/tty.usbserial-FTU7JPNF"
A5_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F11PO"
A6_SERIAL_ADDRESS = "/dev/tty.usbserial-FTU7JOOC"
A7_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F0SER"
A8_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8EQ4MF"
A9_SERIAL_ADDRESS = "/dev/tty.usbserial-FT878A04"

#################################################
# Connections:
# PC --> USB Hub --> 9*USB-RS422 Cables --> 9*Splitters --> 9*Orca Actuators
#################################################

# 0mm-->50mm-->0mm
TRAJECTORY_SINGLE = [
    int(x) for x in 25 * 1000 * (1 - np.cos(np.linspace(0, 2 * np.pi, 512)))
]

# copy for all 9 actuators
TRAJECTORIES = np.array([TRAJECTORY_SINGLE for _ in range(9)]).T

# baud rate
BAUDRATE = 115200


async def async_main():
    actuators = await asyncio.gather(
        Actuator.create(A1_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A2_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A3_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A4_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A5_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A6_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A7_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A8_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A9_SERIAL_ADDRESS, BAUDRATE),
    )

    # set all actuators to sleep mode
    for a in actuators:
        while await a.get_mode() != ORCA_MODE.SleepMode:
            await a.set_mode(ORCA_MODE.SleepMode)

    kp = 3000
    ki = 300
    kdv = 000
    kde = 500
    time_step = 25
    delay = 0

    # TUNE PID
    await asyncio.gather(
        *[a.tune_pid_controller(300000, kp, ki, kdv, kde) for a in actuators]
    )

    # ASSIGN A HOME POSITION (SLOT 0)
    await asyncio.gather(
        *[
            a.configure_motion(0, int(TRAJECTORIES[0][index]), 5000, 0, 1, 0, 0)
            for index, a in enumerate(actuators)
        ]
    )

    # TRIGGER KINEMATIC MODE. MOTORS WILL GO TO HOME POSITION. MAKE SURE HOME POSITION IS SET PROPERLY!!
    for a in actuators:
        while await a.get_mode() != ORCA_MODE.KinematicMode:
            await a.set_mode(ORCA_MODE.KinematicMode)

    print("Trigger start location")

    # CONFIGURE & TRIGGER THE STARTING LOCATION SLOWLY
    await asyncio.gather(
        *[
            a.configure_motion(1, int(TRAJECTORIES[0][index]), 5000, 0, 2, 0, 0)
            for index, a in enumerate(actuators)
        ]
    )
    await asyncio.gather(*[a.kinematic_trigger(1) for a in actuators])

    print("Trajectory start")
    # start trajectory
    MAX_SLOT = 32
    for trajectory_index, rho in enumerate(TRAJECTORIES):
        slot_index = trajectory_index % MAX_SLOT
        for a in actuators:  # make sure no overlapping
            while True:
                kinematic_status = (await a.kinematic_status()).registers[0]
                running_flag = bool(kinematic_status & 0b1000000000000000)
                current_kin_id = int(kinematic_status & 0b0111111111111111)
                if (not running_flag) or slot_index != current_kin_id:
                    break
        for index, a in enumerate(actuators):
            try:
                await a.configure_motion(
                    slot_index,
                    int(rho[index]),
                    time_step,
                    delay,
                    (slot_index + 1) % MAX_SLOT,
                    0,
                    0,
                )
            except Exception as e:
                print(
                    f"Error configuring motion at slot {slot_index} for actuator {index + 1}: {e}"
                )
        await asyncio.gather(*[a.kinematic_trigger(slot_index) for a in actuators])
        print(f"Step {trajectory_index+1} at slot {slot_index} triggered")

    print("Done!")


if __name__ == "__main__":
    asyncio.run(async_main())
