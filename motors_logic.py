
def cameraSearch ():
    return true

def pickUp ():
    return 0

def dropOff ():
    return 0

def takeToDrop(i):
    return 0

def moveToNextLocation(i):
    return 0

for i in range(1, 8, 1):
    #search for item
    if(cameraSearch()):
        pickUp()
        takeToDrop(i)
        dropOff()
        break
    else:
        moveToNextLocation(i)


