#implements trig functions
import math

#find the sine
def get_sine(x):
    #x is in degrees
    angle_rad = math.radians(x)
    angle_sin = math.sin(angle_rad)

    return angle_sin

def get_tan(y):
    angle_rad = math.radians(y)
    angle_tan = math.tan(angle_rad)

    return angle_tan

def get_cos(z):
    angle_rad = math.radians(z)
    angle_cos = math.cos(angle_rad)

    return angle_cos