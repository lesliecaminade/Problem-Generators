import randomizer
import math
import random
import sympy as sp
import stringHandling

from common_names import *
from sympy import *

#symbols for sympy
a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)


class workWordProblemsClass:

    def __init__(self):
        #try:
        low = 2
        high = 99
        
        coe = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []

        form = random.randint(1, 4)
        
        for i in range(0,20):
            coe.append(round(random.randint(low,high),2))
            
            
        fname = random.sample(femaleNames,5)
        mname = random.sample(maleNames,5)
        name = random.sample(allNames,5)
        sport = random.sample(allSports,5)
        day = random.sample(daysOfTheWeek,7)
        town = random.sample(towns,5)
        landVehicle = random.sample(landVehicles,3)
        fruit = random.sample(fruits,3)
        activity = random.sample(activities,2)
        
        time1 = randomizer.toInt(15,10)
        time2 = randomizer.toInt(15,10)
            
        rate1 = 1/time1
        rate2 = 1/time2
            
        total_rate = rate1 + rate2    
        total_time = 1/total_rate
        total_time = round(total_time,2)
        
        if form == 1:

            
            soln = total_time
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """{name0:s} takes {a:g} hours to {act:s}. It takes {name1:s} {b:g} hours to do the same thing. How long would it take if they worked together?""".format(
            a = time1, 
            b = time2, 
            name0 = name[0],
            name1 = name[1],
            act = activity[0])
        
        if form == 2:
            
            soln = time1
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """{name0:s} and {name1:s} were able to {act:s} in {a:g} hours together. It takes {name1:s} {b:g} hours to finish the same job alone. Without help, how long would it take {name0:s} to finish the same job?""".format(
            a = total_time, 
            b = time2, 
            name0 = name[0],
            name1 = name[1],
            act = activity[0])

        if form == 3:
            soln = total_time
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """For {name0:s}, it takes {a:g} hours to paint a house. However, {name1:s} takes {b:g} hours to finish this job. If working together, how long would they take?""".format(
            a = time1, 
            b = time2, 
            name0 = name[0],
            name1 = name[1])            

        if form == 4:
            soln = total_time
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """{name0:s} can {act:s} in {a:g} hours. If {name1:s} helps, it takes them {b:g} hours. Without help, how long would it take {name1:s} to finish the same job?""".format(
            a = time1, 
            b = time2, 
            name0 = name[0],
            name1 = name[1],
            act = activity[0])  
            
        self.question = problem
        self.soln = soln

  
print('WORK WORD PROBLEMS')
print()

for i in range (1,10):
    A = workWordProblemsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
