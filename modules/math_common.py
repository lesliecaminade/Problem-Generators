import math
import numpy as np #this is just for back compatibility



def quadFP(a, b, c):
    x = (-b + math.sqrt(abs(b**2 - 4*a*c)))/(2*a)
    return x

def quadFN(a, b, c):
    x = (-b - math.sqrt(abs(b**2 - 4*a*c)))/(2*a)
    return x   

def sind(angleD):
    angleR = angleD*((math.pi)/180)
    x = math.sin(angleR)
    return x

def cosd(angleD):
    angleR = angleD*((math.pi)/180)
    x = math.cos(angleR)
    return x

def tand(angleD):
    angleR = angleD*((math.pi)/180)
    x = math.tan(angleR)
    return x

def asind(x):
    angleR = math.asin(x)
    angleD = angleR*(180/(math.pi))
    return angleD

def acosd(x):
    angleR = math.acos(x)
    angleD = angleR*(180/(math.pi))
    return angleD
    
def atand(x):
    angleR = math.atan(x)
    angleD = angleR*(180/(math.pi))
    return angleD
   
#for back compatibility only ==================================
# Solving following system of linear equation
# 1a + 1b = 35
# 2a + 4b = 94
def sysLin2(a1, b1, c1, a2, b2, c2):
    a = np.array([[a1, b1],[a2,b2]])
    b = np.array([c1, c2])

    return np.linalg.solve(a,b)