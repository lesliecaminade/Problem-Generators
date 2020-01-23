import randomizer
import math
import random
import sympy as sp
import stringHandling

from common_names import *
from sympy import *
#http://www.math-aids.com/cgi/pdf_viewer_12.cgi?script_name=algebra1_equations_multiple_decimals.pl&form_0=1&form_1=1&form_2=1&form_3=1&form_4=1&form_5=1&form_6=1&form_7=1&form_8=1&form_9=1&form_10=1&language=0&memo=&answer=1&x=132&y=31
#symbols for sympy
a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)


class twoStepEquationWordProblemsClass:

    def __init__(self):
        #try:
        coe = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []
        form = random.randint(1, 11)

        for i in range(0,20):
            num = random.randint(10,99)
            while num%2 == 0:
                num = random.randint(10,99)
            oddNumbers.append(num)

        for i in range(0,20):
            num = random.randint(10,99)
            while num%2 != 0:
                num = random.randint(10,99)
            evenNumbers.append(num)

        for i in range(0,20):
            coe.append(round(random.randint(10,30),2))
            #coeSmall.append(round(random.randint(10,20),2))
            
        fname = random.sample(femaleNames,5)
        mname = random.sample(maleNames,5)
        name = random.sample(allNames,5)
        sport = random.sample(allSports,5)
        day = random.sample(daysOfTheWeek,7)
        
        
        if form == 1:
            variable = coe[1] + coe[2]*coe[3]
            soln = coe[3]
            problem = """{name0:s} bought a soft drink for {a:g} dollars and {b:g} candy bars. He spent a total of {c:g} dollars. How much did each candy bar cost?""".format(a = coe[1], b = coe[2], c = variable, name0 = mname[0])
        if form == 2:
            variable = (coe[1]/2) + coe[2]
            soln = coe[1]
            problem = """{name0:s} sold half of her comic books and then bought {a:g} more. She now has {b:g}. How many did she begin with?""".format(a = coe[2], b = variable, c = variable, name0 = fname[0])
        if form == 3:
            variable = coe[1]*coe[2] + coe[3]
            soln = coe[1]
            problem = """{name0:s} had {a:g} dollars to spend on {b:g} books. After buying them she had {c:g} dollars. How much did each book cost?""".format(a = variable, b = coe[2], c = coe[3], name0 = fname[0]) 
        if form == 4:
            variable = coe[1]*coe[2] + coe[3]
            soln = coe[1]
            problem = """{name0:s} had {a:g} dollars to spend on {b:g} books. After buying them she had {c:g} dollars. How much did each book cost?""".format(a = variable, b = coe[2], c = coe[3], name0 = fname[0])
        if form == 5:
            variable = coe[1]*coe[2] + coe[3]
            soln = coe[1]
            problem = """On Monday, {a:g} students went on a trip to the zoo. All {b:g} buses were filled and {c:g} students had to travel in cars. How many students were in each bus?""".format(a = variable, b = coe[2], c = coe[3], name0 = fname[0])  
        if form == 5:
            variable = coe[1]*coe[2] + coe[3]
            soln = coe[1]
            problem = """On {day0:s}, {a:g} students went on a trip to the zoo. All {b:g} buses were filled and {c:g} students had to travel in cars. How many students were in each bus?""".format(a = variable, b = coe[2], c = coe[3], name0 = fname[0], day0 = day[0])  
        if form == 6:
            variable = (coe[1]+coe[2])/2
            soln = coe[1]
            problem = """{name0:s} bought {a:g} new {sport:s} trading cards to add to his collection. The next day his dog ate half of his collection. There are now only {b:g} cards left. How many cards did {name0:s} start with ?""".format(a = coe[2], b = variable, c = coe[3], name0 = mname[0], day0 = day[0],sport = sport[0])   
        if form == 7:
            variable = (coe[1]/2)+coe[2]
            soln = coe[1]
            problem = """{name0:s} spent half of her allowance going to the movies. She washed the family car and earned {a:g} dollars. What is her weekly allowance if she ended with {b:g} dollars ?""".format(a = coe[2], b = variable, c = coe[3], name0 = fname[0], day0 = day[0],sport = sport[0])  
        if form == 8:
            variable = coe[1] + (coe[1]+1) + (coe[1]+2)
            soln = coe[1]
            problem = """The sum of three consecutive numbers is {a:g}. What is the smallest of the three numbers ?""".format(a = variable, b = variable, c = coe[3], name0 = fname[0], day0 = day[0],sport = sport[0])
        if form == 9:
            variable = oddNumbers[1] + (oddNumbers[1]+2) + (oddNumbers[1]+4)
            soln = oddNumbers[1]
            problem = """The sum of three consecutive odd numbers is {a:g}. What is the smallest of the three numbers?""".format(a = variable, b = variable, c = oddNumbers[3], name0 = fname[0], day0 = day[0],sport = sport[0])
        if form == 10:
            variable = evenNumbers[1] + (evenNumbers[1]+2) + (evenNumbers[1]+4)
            soln = evenNumbers[1]
            problem = """The sum of three consecutive even numbers is {a:g}. What is the smallest of the three numbers ?""".format(a = variable, b = variable, c = evenNumbers[3], name0 = fname[0], day0 = day[0],sport = sport[0])
        if form == 11:
            variable = coe[1]*coe[2] + coe[3]
            soln = coe[1]
            problem = """ {name0:s}'s Bike Shop charges {a:g} dollars plus {b:g} dollars an hour for renting a bike. {name0:s} paid {c:g} dollars to rent a bike. How many hours did he pay to have the bike checked out ?""".format(a = coe[3], b = coe[2], c = variable, name0 = name[0], day0 = day[0],sport = sport[0])
        #repeated part

        self.question = problem
        self.soln = soln
        #except:
            #self.soln = 0
            #self.eqn = "0"
            
print('TWO STEP WORD PROBLEMS')
print()

for i in range (1,10):
    A = twoStepEquationWordProblemsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
