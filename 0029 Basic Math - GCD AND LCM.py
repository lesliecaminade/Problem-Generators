import randomizer
import math
import random
import sympy as sp
import stringHandling
import math_common

from common_names import *
#from sympy import *

#symbols for sympy
spa, spb, spc, spd, spx, spy, spz = sp.symbols('a b c d x y z', real = True)
spn = sp.symbols('n', real = True)


title_string = """GCD AND LCM
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""


class genericClass:

    def __init__(self):
        form = random.randint(1,3) #check
        if form == 1:
            a = random.randint(1,500)
            b = random.randint(1,500)
            
            lcm = math_common.lcm(a,b)
            gcd = math_common.gcd(a,b)
            
            
            question = """Calculate LCM({a:g},{b:g}) + GCD({a:g},{b:g}).""".format(
            a = a,
            b = b)
            
            soln = int(lcm + gcd)
        if form == 2:
            a = 2*random.randint(2,5)*random.randint(6,9)
            b = 2*random.randint(2,5)*random.randint(6,9)
            c = 2*random.randint(2,5)*random.randint(6,9)
            
            gcd1 = math_common.gcd(a,b)
            gcd2 = math_common.gcd(c,gcd1)

            question = """A choir director at your school wants to divide the choir into smaller groups. There are {a:g} sopranos, {b:g} altos, and {c:g} tenors. Each group will have the same number of each type of voice. What is the greatest number of groups that can be formed?""".format(
            a = a,
            b = b,
            c = c
            )
            
            soln = gcd2
        
        if form == 3:
            a = 2*random.randint(1,30)
            b = 2*random.randint(1,30)
            c = 2*random.randint(1,30)
            
            lcm1 = math_common.lcm(a,b)
            lcm2 = math_common.lcm(c,lcm1)
            
            t = random.randint(2,9)
            
            frame = t*60

            times = math.floor(frame/lcm2)
            soln = times

            question = """A beacon flashes its light every {a:g} seconds, another every {b:g} seconds and a third every {c:g} seconds. At 12:00 noon the three flash simultaneously. Find out how many times when the three flash simultaneously again in the next {t:g} minutes.""".format(
            a = a,
            b = b,
            c = c,
            t = t
            )
            
            
        
        self.question = question
        self.soln = soln
        
            
    


print(title_string)
print()




for i in range (1,10):
    A = genericClass()
    print(str(stringHandling.cleanAst(A.question))) 
    print("""{a:s}*""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
