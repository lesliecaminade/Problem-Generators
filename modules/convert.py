import math



METERS_PER_MILE = 1609.34

def cmToM(input):
    output = input/100
    return output
    
def gToKg(input):
    output = input/1000
    return output
    
def milesperhourTometerspersecond(input):
    output = input * METERS_PER_MILE / 3600
    return output

def kilometersperhourTometerspersecond (input):
    output = input * 1000/3600
    return output
    
    
def degreesToradians (input):
    output = input * math.pi/360
    return output
    
def peakTormssine (input):
    output = input / math.sqrt(2)
    return output 
    
    
def inchTometer (input):
    output = input / 39.37
    return output
    
def dBToneper (input):
    output = input / 8.686
    return output
    
def mileTofeet(input):
    output = input*5280
    return output