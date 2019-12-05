from sympy import *
from sympy import Symbol, exp, I
from sympy.functions import Abs
from sympy import oo

#symbols for sympy
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#an is for real part of zn, bn is imaginary part of zn
a1 = Symbol('a1')
b1 = Symbol('b1')
a2 = Symbol('a2')
b2 = Symbol('b2')

def sind(angleD):
    angleR = angleD*(pi/180)
    x = sin(angleR)
    return x

def cosd(angleD):
    angleR = angleD*(pi/180)
    x = cos(angleR)
    return x

def tand(angleD):
    angleR = angleD*(pi/180)
    x = tan(angleR)
    return x

def asind(x):
    angleR = asin(x)
    angleD = angleR*(180/pi)
    return angleD

def acosd(x):
    angleR = acos(x)
    angleD = angleR*(180/pi)
    return angleD
    
def atand(x):
    angleR = atan(x)
    angleD = angleR*(180/pi)
    return angleD

