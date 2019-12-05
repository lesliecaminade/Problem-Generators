import randomizer
import math
import random
from sympy import *
import stringHandling

#http://www.math-aids.com/cgi/pdf_viewer_12.cgi?script_name=algebra1_equations_multiple_decimals.pl&form_0=1&form_1=1&form_2=1&form_3=1&form_4=1&form_5=1&form_6=1&form_7=1&form_8=1&form_9=1&form_10=1&language=0&memo=&answer=1&x=132&y=31
#symbols for sympy
a, b, c, d, e, x, y, z = symbols("a b c d e x y z")


class multiStepEquationDecimalClass:

    def __init__(self):
        form = random.randint(1,10)
        try:
            coe = []
            for i in range(0,20):
                coe.append(round(random.uniform(-50,50),2))
            if form == 1:
                exp1 = Add(coe[1]*x, coe[2]*x, evaluate = False)
                exp2 = coe[11]
              
            if form == 2:
                exp1 = Add(coe[1]*x, coe[2], coe[3]*x, evaluate = False)
                exp2 = coe[11]
       
            if form == 3:
                exp1 = Mul(coe[1], coe[2]*x + coe[3],evaluate = False)
                exp2 = coe[11]
              
            if form == 4:
                exp1 = Add(coe[1], Mul(coe[2], x - coe[3], evaluate = False),evaluate = False)
                exp2 = coe[11]
             
            if form == 5:
                exp1 = Add(coe[1]*x,coe[2]*x,evaluate = False)
                exp2 = coe[11]
                        
            if form == 6:
                exp1 = Add(coe[1],Mul(coe[2],Add(coe[3], coe[4]*x,evaluate = False),evaluate = False),evaluate =False)
                exp2 = coe[11]
            
            if form == 7:
                exp1 = Mul(coe[1],Add(coe[2]*x,coe[3]),evaluate=False)
                exp2 = Add(coe[11],coe[12]*x)
                
            if form == 8:
                exp1 = Add(coe[1]*x,coe[2],coe[3],evaluate=False)
                exp2 = coe[11]
               
            if form == 9:
                exp1 = Mul(coe[1],coe[2]*x + coe[3],evaluate=False)
                exp2 = coe[11]
             
            if form == 10:
                exp1 = Mul(coe[1],coe[2] + coe[3]*x,evaluate =False)
                exp2 = coe[11] 
            
            soln = solveset(Eq(exp1,exp2),x)
            soln = float(soln.args[0])
            self.question = str(exp1)+" = "+str(exp2)
            self.soln = 'x = '+str(round(soln,2)) 
        except:
            self.soln = 0
            self.question = "0"

print('MULTI - STEP EQUATIONS (Decimals): Solve for x.')
print()

for i in range (1,10):
    A = multiStepEquationDecimalClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
