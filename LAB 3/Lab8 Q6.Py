import math
def getInput():
    angle_degrees = float(input("Enter an angle in degrees: "))
    return angle_degrees

def convertDeg(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return angle_radians

def showValue(result):
    print(f"The angle in radians is: {result}")

d = getInput()
r = convertDeg(d)
showValue(r)