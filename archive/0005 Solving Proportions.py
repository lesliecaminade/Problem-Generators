import randomizer
import math
import random
from sympy import *
import sympy as sp
import stringHandling

#http://www.math-aids.com/cgi/pdf_viewer_12.cgi?script_name=algebra1_equations_multiple_decimals.pl&form_0=1&form_1=1&form_2=1&form_3=1&form_4=1&form_5=1&form_6=1&form_7=1&form_8=1&form_9=1&form_10=1&language=0&memo=&answer=1&x=132&y=31
#symbols for sympy
a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)


class solvingProportionsClass:

    def __init__(self):
        #try:
        coe = []
        form = random.randint(1,10)
        for i in range(0,20):
            coe.append(round(random.randint(-50,50),2))
        if form == 1:
            exp1 = coe[1]/x
            exp2 = Rational(coe[11],coe[12])
        if form == 2:
            exp1 = x/coe[1]
            exp2 = Rational(coe[11],coe[12])
        if form == 3:
            exp1 = (coe[1]*x + coe[2])/coe[3]
            exp2 = Rational(coe[11],coe[12])
        if form == 4:
            exp1 = Rational(coe[1],coe[2])
            exp2 = coe[11]/(coe[12]*x + coe[13])
        if form == 5:
            exp1 = coe[1]/(coe[2]*x + coe[3])
            exp2 = Rational(coe[11],coe[12])
        if form == 6:
            exp1 = (coe[1]*x)/coe[2]
            exp2 = (coe[11]*x + coe[12])/coe[13]
        if form == 7:
            exp1 = Rational(coe[1],coe[2])
            exp2 = coe[3]/(coe[4]*x)
        if form == 8:
            exp1 = coe[1]*x/coe[2]
            exp2 = (coe[4]*x + coe[5])/coe[3]
        if form == 9:
            exp1 = coe[1]/(coe[2]*x + coe[3])
            exp2 = coe[4]/(coe[5]*x)
        if form == 10:
            exp1 = Rational(coe[1],coe[2])
            exp2 = (coe[3]*x + coe[4])/(coe[5]*x + coe[6])
            

        soln = sp.solveset(sp.Eq(exp1,exp2),x,domain = sp.S.Reals)

        self.question = str(exp1)+" = "+str(exp2)
        self.soln = str(soln)
  
            
print('SOLVING PROPORTIONS: Solve for x.')
print()

for i in range (1,10):
    A = solvingProportionsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
