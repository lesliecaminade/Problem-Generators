
import random_handler as ran
#import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
#import algebra
#import analytic_geometry
import constants_conversions as c
#import common_names
#import collections
#import randomizer_2 as ran2

x, y, z = sym.symbols('x y z', real = True)#generic variables

def find_sigfigs(x):
    '''Returns the number of significant digits in a number. This takes into account
       strings formatted in 1.23e+3 format and even strings such as 123.450'''
    # change all the 'E' to 'e'
    x = x.lower()
    if ('e' in x):
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        return len( myStr[0] ) - 1 # to compenstate for the decimal point
    else:
        # put it in e format and return the result of that
        ### NOTE: because of the 8 below, it may do crazy things when it parses 9 sigfigs
        
        n = ('%.*e' %(8, float(x))).split('e')
        # remove and count the number of removed user added zeroes. (these are sig figs)
        if '.' in x:
            s = x.replace('.', '')
            #number of zeroes to add back in
            l = len(s) - len(s.rstrip('0'))
            #strip off the python added zeroes and add back in the ones the user added
            n[0] = n[0].rstrip('0') + ''.join(['0' for num in xrange(l)])
        else:
            #the user had no trailing zeroes so just strip them all
            n[0] = n[0].rstrip('0')
        #pass it back to the beginning to be parsed
    return find_sigfigs('e'.join(n))


class fibonacci_1:
    def __init__(self,*args,**kwargs): 
            
        n = random.randint(20,100)
        
        self.question = f"""Determine F_{n} of the Fibonnaci sequence."""
        
        fn = (1 / math.sqrt(5)) * ( ((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5)) / 2)**n )
        
        self.answer = f"""F_{n} = {fn}"""
            
class lucas_1:
    def __init__(self,*args,**kwargs): 
        
        n = random.randint(20,100)
        
        self.question = f"""Determine L_{n} of the Lucas sequence."""
        
        ln = ((1+math.sqrt(5))/2)**n + ((1-math.sqrt(5)) / 2)**n 
        
        self.answer = f"""L_{n} = {ln}"""
        

        
        
class digits_1:
    def __init__(self,*args,**kwargs): 
        
        base = random.randint(10, 100)
        exponent = random.randint(10, 100)
        self.question = f"""Determine the number of digits of the number {base}^{exponent}."""
        
        digits = 1 + math.floor( exponent * math.log( base, 10 )  )
        
        self.answer = f"""Number of digits = {digits}"""
        
class digits_2:
    def __init__(self,*args,**kwargs): 
        
        number = random.randint(50,300)
        self.question = f"""Determine the number of digits {number}!."""
        
        digits = 1 + math.floor(
        math.log(math.sqrt(2 * math.pi * 100), 10) + number * math.log(number/math.exp(1), 10))
        
        self.answer = f"""Number of digits = {digits}"""
        
class trailingZeroes_1:
    def __init__(self,*args,**kwargs): 
        
        number = random.randint(50,300)
        self.question = f"""Determine the number of trailing zeroes of {number}!."""
        
        zeros = 0
        for i in range(10):
            zeros = zeros + math.floor(number/5**i)
            
        self.answer = f"""Number of trailing zeroes = {zeros}"""
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        