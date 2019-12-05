import math
import numpy as np #this is just for back compatibility
DEGREES = math.pi/180


def quadFP(a, b, c):
    x = (-b + math.sqrt(abs(b**2 - 4*a*c)))/(2*a)
    return x

def quadFN(a, b, c):
    x = (-b - math.sqrt(abs(b**2 - 4*a*c)))/(2*a)
    return x   

def npr(nval,rval):
    """This function evaluate the number of n elements permuted r at a time"""
    n = int(nval)
    r = int(rval)
    npr = math.factorial(n)/math.factorial(n-r)
    ncr = npr/math.factorial(r)
    return npr

    
def ncr(nval,rval):
    """This function evaluates the combinations of two n elemens taken r at a time"""
    n = int(nval)
    r = int(rval)
    npr = math.factorial(n)/math.factorial(n-r)
    ncr = npr/math.factorial(r)
    return ncr
   
def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

# change the values of num1 and num2 for a different result
num1 = 54
num2 = 24 

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

#print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
#for back compatibility only ==================================
# Solving following system of linear equation
# 1a + 1b = 35
# 2a + 4b = 94
def sysLin2(a1, b1, c1, a2, b2, c2):
    a = np.array([[a1, b1],[a2,b2]])
    b = np.array([c1, c2])

    return np.linalg.solve(a,b)
    
#for back compatibility, do not delete
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