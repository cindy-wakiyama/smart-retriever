# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# will need to do install using sudo pip3 install adafruit-circuitpython-motorkit to raspberry pi

"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper # this adds more controls to the onestep() function

# connects to the hat
kit = MotorKit(i2c=board.I2C())

# we can test motors one at a time
print("tests starting")

# Motor 1 connects to terminals M1 and M2 on the hat
print("testing stepper motor 1")
for i in range(100):
    # onestep() is one single coil step for the motor
    kit.stepper1.onestep()
    time.sleep(0.01)

# Motor 2 connects to the terminals M3 and M4 on the hat
print("testing stepper motor 2")
for i in range(100):
    kit.stepper2.onestep()
    time.sleep(0.01)


# onestep() has two options:
#   direction:
#       - stepper.FORWARD (defualt)
#       - stepper.BACKWARD
#   style:
#       - stepper.SINGLE (default) --> a full step rotation where one single coil is powered
#       - stepper.DOUBLE --> a full step rotation where two coils are powered providing more torque which means stronger than single
#       - stepper.INTERLEAVE --> a half step rotation interleaving single and double coil positions and torque - smoother trasnsition
#       - stepper.MICROSTEP --> a microstep rotation to a position where both coils are partially active - slower than single but more precise

print("testing stepper motor 1 with backward motion")
for i in range(100):
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    time.sleep(0.01)

print("testing stepper motor 2 with backward motion")
for i in range(100):
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    time.sleep(0.01)

print("testing stepper motor 1 with double coil motion")
for i in range(100):
    kit.stepper1.onestep(style=stepper.DOUBLE)
    time.sleep(0.01)

print("testing stepper motor 2 with double coil motion")
for i in range(100):
    kit.stepper2.onestep(style=stepper.DOUBLE)
    time.sleep(0.01)

print("testing stepper motor 1 with interleaving motion")
for i in range(100):
    kit.stepper1.onestep(style=stepper.INTERLEAVE)
    time.sleep(0.01)

print("testing stepper motor 2 with interleaving motion")
for i in range(100):
    kit.stepper2.onestep(style=stepper.INTERLEAVE)
    time.sleep(0.01)

print("testing stepper motor 1 with microstep motion")
for i in range(100):
    kit.stepper1.onestep(style=stepper.MICROSTEP)
    time.sleep(0.01)

print("testing stepper motor 2 with microstep motion")
for i in range(100):
    kit.stepper2.onestep(style=stepper.MICROSTEP)
    time.sleep(0.01)

print("tests finished")