import random
import math

def main(input_value, *args,**kwargs):
    sigma = 2
    positive_flag = None

    if input_value > 0:
        positive_flag = True
    else:
        positive_flag = False

    for key ,value in kwargs.items():
        if key == 'sigma':
            sigma = value


    if positive_flag:
        return abs(round(random.gauss(input_value, sigma),2))
    else:
        return -abs(round(random.gauss(input_value, sigma),2))
    
    
    
    
    
    
    
    
    
    
    
    
#legacy codes ------------------------------------------
def point(input):
    x = random.randint(-input,input)
    y = random.randint(-input,input)
    return x,y
    
def low_high(input):
    x = random.randint(-input,input)
    y = x + random.randint(0,input)
     
    return x,y
    
def c(input): #any number 
    output = random.randint(-input,input)
    return output
    
def cpos(input): #positive only
    output = random.randint(1,input)
    return output
    
def cneg(input): #negative only
    output = random.randint(-input,-1)
    return output
    
def cnz(input): #no zero
    output = random.randint(-input,input)
    while output == 0:
        output = random.randint(-input,input)
    return output
    
def r(input):
    if abs(input) >= 0 and abs(input) < 300:
        output = ten(input)
    
    if abs(input) >= 300:
        output = hundred(input)
        
    return output
    
def ten(input):
    if input >= 0:
        pos = True
    else:
        pos = False
    
    
    retry = True
    while retry:
        output = random.randint(input-10,input+10)
        
        if pos and output > 0:
            retry = False
        
        if (not pos) and output < 0:
            retry = False
        
    return output
    



def hundred(input):
    if input >= 0:
        pos = True
    else:
        pos = False
    
    
    retry = True
    while retry:
        output = random.randint(input-100,input+100)
        
        if pos and output >= 0:
            retry = False
        
        if (not pos) and output <= 0:
            retry = False
        
    return output

    
def u(*args):
    for arg in args:
        try:
            input = args[0]
            output = round(random.gauss(input,random.uniform(0.1,0.9)),2)
        except:
            output = round(random.uniform(0.1,0.9),2)
    return output
    
    
def round_sigfigs(num, sig_figs):
    """Round to specified number of sigfigs.

    >>> round_sigfigs(0, sig_figs=4)
    0
    >>> int(round_sigfigs(12345, sig_figs=2))
    12000
    >>> int(round_sigfigs(-12345, sig_figs=2))
    -12000
    >>> int(round_sigfigs(1, sig_figs=2))
    1
    >>> '{0:.3}'.format(round_sigfigs(3.1415, sig_figs=2))
    '3.1'
    >>> '{0:.3}'.format(round_sigfigs(-3.1415, sig_figs=2))
    '-3.1'
    >>> '{0:.5}'.format(round_sigfigs(0.00098765, sig_figs=2))
    '0.00099'
    >>> '{0:.6}'.format(round_sigfigs(0.00098765, sig_figs=3))
    '0.000988'
    """
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0
    