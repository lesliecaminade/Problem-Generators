import randomizer
import math
import random
from sympy import *
import sympy as sp
import stringHandling

#http://www.math-aids.com/cgi/pdf_viewer_12.cgi?script_name=algebra1_equations_multiple_decimals.pl&form_0=1&form_1=1&form_2=1&form_3=1&form_4=1&form_5=1&form_6=1&form_7=1&form_8=1&form_9=1&form_10=1&language=0&memo=&answer=1&x=132&y=31
#symbols for sympy
a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)


class percentageCalculationsClass:

    def __init__(self):
        #try:
        coe = []
        form = random.randint(1,3)
        for i in range(0,20):
            coe.append(round(random.randint(10,99),2))
        if form == 1:
            problem = """What is {a:d} percent of {b:d}?""".format(a = coe[1], b = coe[2])
            soln = round((coe[1]/100)*coe[2],2)
            trap = round((coe[1]/100)/coe[2],2)
        if form == 2:
            problem = """{a:d} is {b:d} percent of what? """.format(a = coe[1], b = coe[2])
            soln = round(coe[1]/(coe[2]/100),2)
            trap = round(coe[1]*(coe[2]/100),2)
        if form == 3:
            problem = """What percent of {a:d} is {b:d}?""".format(a = coe[1], b = coe[2])
            soln = round((coe[2]/coe[1])*100,2)
            trap = round((coe[2]*coe[1])/100,2)
            soln = str(soln) + "%"
            trap = str(trap) + "%"
            
        #repeated part

        self.question = problem
        self.soln = soln
        self.trap = trap
        #except:
            #self.soln = 0
            #self.eqn = "0"
            
for i in range (1,10):
    A = percentageCalculationsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print("""T1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.trap)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
