# functions to handle button presses in GUI

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# will need to do install using sudo pip3 install adafruit-circuitpython-motorkit to raspberry pi

"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
#import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper # this adds more controls to the onestep() function

# connects to the first hat using the base address 0x60
kit1 = MotorKit()

# connects to the second hat using next address
kit2 = MotorKit(address=0x61)

def pickUp():
    # lower magnet
    for i in range(900):
        kit2.stepper1.onestep()
        time.sleep(0.01)

    # turn on magnet
    kit2.motor3.throttle = 1.0
    time.sleep(0.1)

    # pull magnet up
    for i in range(950):
        kit2.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

def dropOff():
    # lower magnet
    for i in range(900):
        kit2.stepper1.onestep()
        time.sleep(0.01)

    # turn off magnet
    kit2.motor3.throttle = 0
    time.sleep(0.1)

    # pull magnet up
    for i in range(950):
        kit2.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

def retrieve1():
    for i in range(1000):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    pickUp()

    for i in range(1000):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

def retrieve2():
    for i in range(1000):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    pickUp()

    for i in range(1000):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

def retrieve3():
    for i in range(1000):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)
    
    pickUp()

    for i in range(1000):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    dropOff()

def retrieve4():
    for i in range(550):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    pickUp()

    for i in range(550):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

def retrieve5():
    for i in range(550):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    pickUp()

    for i in range(550):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

def retrieve6():
    for i in range(550):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)
    
    pickUp()

    for i in range(550):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    dropOff()

def retrieve7():
    for i in range(950):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    pickUp()

    for i in range(950):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

def retrieve8():
    for i in range(450):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    pickUp()

    for i in range(450):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

#RETURN FUNCTIONS
def return1():
    pickUp()

    for i in range(1000):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep()
        time.sleep(0.01)

    dropOff()

    for i in range(1000):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

def return2():
    pickUp()

    for i in range(1000):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep()
        time.sleep(0.01) 

    dropOff()

    for i in range(1000):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    dropOff()

def return3():
    pickUp()

    for i in range(1000):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)
    
    dropOff()

    for i in range(1000):
        kit1.stepper1.onestep()
        time.sleep(0.01)

def return4():
    pickUp()

    for i in range(550):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    dropOff()

    for i in range(550):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(950):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

def return5():
    pickUp()

    for i in range(550):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    dropOff()

    for i in range(550):
        kit1.stepper1.onestep()
        time.sleep(0.01)

    for i in range(450):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

def return6():
    pickUp()

    for i in range(550):
        kit1.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)
    
    dropOff()

    for i in range(550):
        kit1.stepper1.onestep()
        time.sleep(0.01)

def return7():
    pickUp()

    for i in range(950):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    dropOff()

    for i in range(950):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)

def return8():
    pickUp()

    for i in range(450):
        kit1.stepper2.onestep()
        time.sleep(0.01)
    
    dropOff()

    for i in range(450):
        kit1.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)