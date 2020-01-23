import randomizer
import math
import random
import sympy
import stringHandling
import math_common

from common_names import *
#from sympy import *

#symbols for sympy
spa, spb, spc, spd, spx, spy, spz = sympy.symbols('a b c d x y z', real = True)
spn = sympy.symbols('n', real = True)
spk = sympy.symbols('k', real = True)

title_string = """Remainder and Factor Theorem
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""


class genericClass:

    def __init__(self):
        form = random.randint(1,7) #check
        if form == 1:
            exp1 = sympy.Mul((spx + random.randint(1,9)),(spx - random.randint(1,9)),Evaluate = False) + random.randint(1,9)
            exp2 = spx
            solution = sympy.solveset(sympy.Eq(exp1,exp2),spx)
            exp1_string = str(exp1)
            
            question = """When {exp1:s} is divided by x - k, the remainder is k, find the value of k.""".format(
            exp1 = exp1_string
            )
            
            soln = str(solution)
            
        if form == 2:
            a = random.randint(1,9)
            c = random.randint(1,9)
            exp1 = a*spx**2 + spk*spx + c
            discriminant = spk**2 - 4*a*c
            k = sympy.solveset(sympy.Eq(discriminant,0),spk)
            
            question = """Find k in the equation {exp1:s} = 0 so that it will only have one real root.""".format(
            exp1 = str(exp1)
            )
            
            soln = str(k)
            
        if form == 3:
            exp1 = spx**12 + random.randint(1,9)
            const = sympy.sqrt(random.randint(1,9))
            exp2 = spx - const
            q, r = sympy.div(exp1,exp2,spx)
            
            question = """Find the remainder when {exp1:s} is divided by {exp2:s}""".format(
            exp1 = str(exp1),
            exp2 = str(exp2)
            )
            
            soln = str(r)
            
        if form == 4:
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,9)
            d = random.randint(1,9)
            
            e = random.randint(1,9)
            f = random.randint(1,9)
            
            exp1 = a*spx**3 - b*spx**2*spy + c*spx*spy**2 + d*spy**3
            exp2 = spx**2 - e*spx*spy + f*spy**2
            
            q, r = sympy.div(exp1,exp2,spx)
            
            question = """If {exp1:s} is divided by {exp2:s}, the remainder is:""".format(
            exp1 = str(exp1),
            exp2 = str(exp2)
            )
            
            soln = str(r)
            
        if form == 5:
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,19)
            d = random.randint(1,9)
            
            e = random.randint(1,9)
            f = random.randint(1,9)
            
            exp1 = a*spy**3 + b*spy + c*spy**2 - d
            exp2 = e*spy + f
            
            q, r = sympy.div(exp1,exp2,spy)
            
            question = """If {exp1:s} is divided by {exp2:s}, the remainder is""".format(
            exp1 = str(exp1),
            exp2 = str(exp2)
            )
            
            soln = str(r)
            
        if form == 6:
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,9)
            d = random.randint(1,9)
            
            e = random.randint(1,9)
            f = random.randint(1,9)
            
            exp1 = spx**3 + a*spx**2 - b*spx + c
            exp2 = spx - e
            
            
            q, r = sympy.div(exp1,exp2,spx)
            
            question = """The polynomial {exp1:s} is divided by {exp2:s}. What is the remainder?""".format(
            exp1 = str(exp1),
            exp2 = str(exp2)
            )
            
            soln = str(r)
            
        if form == 7:
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,9)
            d = random.randint(1,9)
            e = random.randint(1,9)
            
            f = random.randint(1,9)
            g = random.randint(1,9)
            
            exp1 = a*spx**5 - b*spx**3 + c*spx**2 + d*spx + e
            exp2 = spx**3 - f*spx**2 + g
            
            q,r = sympy.div(exp1,exp2,spx)
            
            question = """Find the quotient of {exp1:s} divided by {exp2:s}.""".format(
            exp1 = str(exp1),
            exp2 = str(exp2)
            )
            soln = str(r)
            
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
