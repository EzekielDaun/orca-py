import asyncio
from contextlib import AsyncExitStack

import numpy as np

from orca_py.actuator import Actuator
from orca_py.orca_constant import ORCA_MODE_SUBCODE
from orca_py.orca_register import ORCA_REGISTER

# import pymodbus
# pymodbus.pymodbus_apply_logging_config()

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


async def async_main():
    async with AsyncExitStack() as stack:
        enterers = [
            stack.enter_async_context(
                Actuator(addr, BAUDRATE, reconnect_delay=0.1, timeout=3, retries=3)
            )
            for addr in [
                A4_SERIAL_ADDRESS,
                A5_SERIAL_ADDRESS,
                A6_SERIAL_ADDRESS,
                A11_SERIAL_ADDRESS,
                A12_SERIAL_ADDRESS,
                A21_SERIAL_ADDRESS,
                A22_SERIAL_ADDRESS,
                A31_SERIAL_ADDRESS,
                A32_SERIAL_ADDRESS,
            ]
        ]
        actuators = await asyncio.gather(*enterers)

        for a in actuators:
            baudrate, delay = await a.stream_enable(115200, 50)
            print(
                f"High-Speed Stream Realized with Baudrate: {baudrate}, Delay: {delay}"
            )
            await a.stream_motor_command(ORCA_MODE_SUBCODE.SleepDataStream, None)
            await a.stream_motor_write(
                ORCA_REGISTER.POS_FILT.value.address,
                ORCA_REGISTER.POS_FILT.value.width,
                0,
            )
            await a.stream_tune_pid_controller(p=3000, i=300, dv=0, de=500, sat=300000)

        time_start = asyncio.get_event_loop().time()
        for i, x in enumerate(TRAJECTORY_SINGLE):
            infos = await asyncio.gather(
                *[
                    a.stream_motor_command(
                        ORCA_MODE_SUBCODE.PositionControlStream, int(x)
                    )
                    for a in actuators
                ]
            )
            print(f"Step {i}:")
            for info in infos:
                print(info)
        time_elapsed = asyncio.get_event_loop().time() - time_start
        print(
            f"Time elapsed: {time_elapsed}, frequency: {len(TRAJECTORY_SINGLE) / time_elapsed}Hz"
        )


if __name__ == "__main__":
    asyncio.run(async_main())
