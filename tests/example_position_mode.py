import asyncio

import numpy as np

from orca_py.actuator import Actuator
from orca_py.orca_constant import ORCA_MODE

A4_SERIAL_ADDRESS = "/dev/tty.usbserial-FT878BFG"
A5_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8ESWCO"
A6_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F0YKB"
A11_SERIAL_ADDRESS = "/dev/tty.usbserial-FTU7JPNF"
A12_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F11PO"
A21_SERIAL_ADDRESS = "/dev/tty.usbserial-FTU7JOOC"
A22_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F0SER"
A31_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8EQ4MF"
A32_SERIAL_ADDRESS = "/dev/tty.usbserial-FT878A04"

#################################################
# Connections:
# PC --> USB Hub --> 9*USB-RS422 Cables --> 9*Splitters --> 9*Orca Actuators
#################################################

BAUDRATE = 115200

# 0mm-->50mm-->0mm
TRAJECTORY_SINGLE = [
    int(x) for x in 25 * 1000 * (1 - np.cos(np.linspace(0, 2 * np.pi, 512)))
]

# copy for all 9 actuators
TRAJECTORIES = np.array([TRAJECTORY_SINGLE for _ in range(9)]).T


async def async_main():
    actuators = await asyncio.gather(
        Actuator.create(A4_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A5_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A6_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A11_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A12_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A21_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A22_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A31_SERIAL_ADDRESS, BAUDRATE),
        Actuator.create(A32_SERIAL_ADDRESS, BAUDRATE),
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

    # TUNE PID
    await asyncio.gather(
        *[a.tune_pid_controller(300000, kp, ki, kdv, kde) for a in actuators]
    )

    # set all actuators to position mode
    for a in actuators:
        while await a.get_mode() != ORCA_MODE.PositionMode:
            await a.set_mode(ORCA_MODE.PositionMode)

    # position commands
    for trajectory_index, rho in enumerate(TRAJECTORIES):
        print(f"Trajectory point {trajectory_index}")

        try:
            await asyncio.gather(
                *[a.position_command(rho[index]) for index, a in enumerate(actuators)]
            )
        except Exception as e:
            print(f"Error during trajectory {trajectory_index}: {e}")

        await asyncio.sleep(time_step * 1e-3)  # 25ms

    # set all actuators to sleep mode
    for a in actuators:
        while await a.get_mode() != ORCA_MODE.SleepMode:
            await a.set_mode(ORCA_MODE.SleepMode)

    print("Done!")


if __name__ == "__main__":
    asyncio.run(async_main())
