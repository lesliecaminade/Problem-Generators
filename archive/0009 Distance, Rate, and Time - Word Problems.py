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


class distanceRateTimeWordProblemsClass:

    def __init__(self):
        #try:
        low = 10
        high = 99
        
        coe = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []

        form = random.randint(1,9)
        for i in range(0,20):
            coe.append(round(random.randint(low,high),2))
            
            
        fname = random.sample(femaleNames,5)
        mname = random.sample(maleNames,5)
        name = random.sample(allNames,5)
        sport = random.sample(allSports,5)
        day = random.sample(daysOfTheWeek,7)
        town = random.sample(towns,5)
        landVehicle = random.sample(landVehicles,3)
        
        if form == 1:
            
            if coe[2] < coe[1]:
                temp = coe[2]
                coe[2] = coe[1]
                coe[1] = temp
            
            ex1 = coe[1]*x + coe[1]*coe[3]
            ex2 = coe[2]*coe[3]
            soln = solveset(Eq(ex1,ex2),x,domain=sp.S.Reals).args[0]
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """{name0:s} left {town0:s} traveling {a:g} mph. {name1:s}, to catch up, left some time later driving at {b:g} mph. {name1:s} caught up after {c:g} hours. How long was {name0:s} driving before {name1:s} caught up?""".format(a = coe[1], b = coe[2], c = coe[3], name0 = mname[0],name1 = fname[0], town0=town[0])
            
        if form == 2:
            ex1 = 3*x + 2*x
            ex2 = 2*(x + coe[1])
            soln = solveset(Eq(ex1,ex2),x,domain=sp.S.Reals).args[0]
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " mph"
            problem = """{name0:s} left downtown {town0:s}, and three hours later, {name1:s} left going {a:g} mph faster to catch up. After another two hours, {name1:s} caught up. Find {name0:s}'s average speed.""".format(a = coe[1], b = coe[2], c = coe[3], name0 = mname[0],name1 = fname[0], town0=town[0])

        if form == 3:
            ex1 = coe[1]*x + coe[2]*x
            ex2 = coe[3]
            soln = solveset(Eq(ex1,ex2),x,domain=sp.S.Reals).args[0]
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """ {name0:s} left {town0:s} with a speed of {a:g} mph. {name1:s} also left at the same time in the opposite direction at a speed of {b:g} mph. Find how many hours {name1:s} must travel before they are {c:g} miles apart.""".format(a = coe[1], b = coe[2], c = coe[3], name0 = mname[0],name1 = fname[0], town0=town[0])

        if form == 4:
            plane_speed1 = randomizer.toInt(300,50)
            plane_speed2 = randomizer.toInt(300,50)
            return_time = randomizer.toInt(12,3)
            
            distance = plane_speed2*return_time
            forward_time = distance/plane_speed1
            soln = forward_time
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """A plane set off to {town0:s} at a speed of {a:g} mph. On the return flight of {b:g} hours, the plane cruised at {c:g} mph. How many hours long was the flight to {town0:s}""".format(a = plane_speed1, b = return_time, c = plane_speed2, name0 = mname[0],name1 = fname[0], town0=town[0])
            
        if form == 4:
            speed_forward = randomizer.toInt(300,50)
            speed_return = randomizer.toInt(300,50)
            
            if speed_forward > speed_return:
                temp = speed_forward
                speed_forward = speed_return
                speed_return = temp
            
            ex1 = speed_forward*(x + 2)
            ex2 = speed_return*x
            soln = solveset(Eq(ex1,ex2),x).args[0]
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """ A cargo plane flew from the US across the Atlantic at {a:g} mph, and flew back to the US at {b:g} mph. Given that the first trip took two hours longer, how long was the return trip""".format(a =speed_forward, b = speed_return, name0 = mname[0],name1 = fname[0], town0=town[0])

        if form == 5:
            time_forward = randomizer.toInt(6,4)
            time_return = randomizer.toInt(6,4)
            
            speed_return = randomizer.toInt(80,20)
            
            speed_forward = (speed_return*time_return)/time_forward
            soln = speed_forward
            
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " hours"
            problem = """ {fname0:s} traveled to {town0:s} by {landVehicle0:s}. Going there took {a:g} hours, and the return trip lasted {b:g} hours. {fname0:s} averaged a speed of {c:g} mph while returning. Find the average speed of the trip there""".format(a =time_forward, b = time_return, c = speed_return, fname0 = fname[0], town0=town[0],landVehicle0 = landVehicle[0]) 

        if form == 6:
            person2_latency = randomizer.toInt(6,4)
            person2_speed_delta = randomizer.toInt(80,20)
            person2_caught_up_time = randomizer.toInt(6,2)
            
            ex1 = person2_latency*x + person2_caught_up_time*x
            ex2 = person2_caught_up_time*(x + person2_speed_delta)
            
            person1_speed = solveset(Eq(ex1,ex2),x).args[0]
            soln = person1_speed
            
            
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " mph"
            problem = """{fname0:s} left the city for vacation. {fname1:s} left {a:g} hours later going {b:g} mph faster to catch up. After {c:g} hours {fname1:s} caught up. What was {fname0:s}'s average speed?""".format(a =person2_latency, b = person2_speed_delta, c = person2_caught_up_time, fname0 = fname[0],fname1 = fname[1], town0=town[0])

        if form == 7:
            person2_latency = randomizer.toInt(6,4)
            person2_speed_delta = randomizer.toInt(80,20)
            person2_caught_up_time = randomizer.toInt(6,2)
            
            ex1 = person2_latency*x + person2_caught_up_time*x
            ex2 = person2_caught_up_time*(x + person2_speed_delta)
            
            person1_speed = solveset(Eq(ex1,ex2),x).args[0]
            soln = person1_speed
            
            
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " mph"
            problem = """{fname0:s} left the city for vacation. {fname1:s} left {a:g} hours later going {b:g} mph faster to catch up. After {c:g} hours {fname1:s} caught up. What was {fname0:s}'s average speed?""".format(a =person2_latency, b = person2_speed_delta, c = person2_caught_up_time, fname0 = fname[0],fname1 = fname[1], town0=town[0])       

        if form == 8:
            #vehicle0_speed = unknown
            vehicle1_speed = randomizer.toInt(50,20)
            vehicle1_latency = randomizer.toInt(6,4)
            vehicle1_caught_up_time = randomizer.toInt(6,4)
            
            ex1 = vehicle1_latency*x + vehicle1_caught_up_time*x
            ex2 = vehicle1_caught_up_time*vehicle1_speed
          
            vehicle0_speed = solveset(Eq(ex1,ex2),x).args[0]
            soln = vehicle0_speed
            
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " mph"
            problem = """A {landVehicle0:s} left for {town0:s}, and {a:g} hours later, a {landVehicle1:s} traveling {b:g} mph tried catching up to the {landVehicle0:s}. After {c:g} hours, the {landVehicle1:s} caught up. What was the {landVehicle0:s}'s average speed?""".format(a = vehicle1_latency, b = vehicle1_speed, c = vehicle1_caught_up_time, name0 = mname[0],name1 = fname[0], town0=town[0],landVehicle0=landVehicle[0], landVehicle1=landVehicle[1])   
        
        if form == 9:
            #vehicle1_speed = unknown
            vehicle0_speed = randomizer.toInt(50,20)
            time = randomizer.toInt(6,4)
            distance = randomizer.toInt(600,100)
            
            ex1 = vehicle0_speed*time
            ex2 = x*time
            ex3 = distance
            
            vehicle1_speed = solveset(Eq(ex1+ex2,ex3),x).args[0]
            
            
            soln = vehicle1_speed
            
            soln = float(soln)
            soln = round(soln,2)
            soln = str(soln) + " mph"
            problem = """A {landVehicle0:s} and {landVehicle1:s} left from {town0:s} in opposite directions. The {landVehicle0:s} traveled for {a:g} hours at {b:g} mph. The vehicles were {c:g} miles apart. Find the {landVehicle1:s}'s average speed?""".format(a = time, b = vehicle0_speed, c = distance, name0 = mname[0],name1 = fname[0], town0=town[0], landVehicle0=landVehicle[0], landVehicle1=landVehicle[1])        
            
        self.question = problem
        self.soln = soln

            
    
            
                
            
print('DISTANCE, RATE, TIME, WORD PROBLEMS')
print()

for i in range (1,10):
    A = distanceRateTimeWordProblemsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
