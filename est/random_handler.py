import random
import math

def main(input, *args, **kwargs):
    regen = True
    while regen:
        regen = False
        intFlag = False
        factor = 0.5
        
        roundFlag = True
        
        for kwarg in kwargs:
            if kwarg == 'factor':
                factor = kwargs[kwargs]
        
        for arg in args:
            if arg == 'spread':
                factor = 0.7
        input = input + random.uniform(-input*factor,factor*input)
        
        for arg in args:
            if arg =='noround':
                roundFlag= False
                
        for arg in args:
            if arg == 'int':
                intFlag = True                
                
        if roundFlag:
            if abs(input) >=0 and abs(input) < 1:
                input = round(input,2)
            if abs(input) >= 1 and abs(input) < 10:
                input = round(input,1)
            if abs(input) >= 10 and abs(input) < 100:
                input = round(input,0)
            if abs(input) >= 100 and abs(input) < 1000:
                input = round(input,0)
            if abs(input) >= 1000:
                input = round(input,0)
                
        if intFlag:
            input = int(input)
            if input == 0:
                input = 1
                
        for arg in args:
            if arg == 'even':
                if input % 2 == 1:
                    regen = True
        
        
    # for arg in args:
        # if arg == '%':
            # input = input/100
        
    return input
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    