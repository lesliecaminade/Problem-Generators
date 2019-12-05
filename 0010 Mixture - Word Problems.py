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


class mixtureWordProblemsClass:

    def __init__(self):
        #try:
        low = 2
        high = 99
        
        coe = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []
        form = random.randint(1,10)

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
        
        if form == 1:
            volume1 = randomizer.toInt(9,5)
            volume2 = randomizer.toInt(14,5)
            concentration1 = randomizer.toInt(20,5)
            concentration2 = randomizer.toInt(64,5)
            vinegar1 = volume1 * (concentration1/100)
            vinegar2 = volume2 * (concentration2/100)
            
            total_vinegar = vinegar1 + vinegar2
            total_volume = volume1 + volume2
            total_concentration = (total_vinegar / total_volume)*100
            
            soln = total_concentration
            soln = round(soln,2)
            soln = str(soln) + " %"
            problem = """A {a:g} L solution that was {b:g} % vinegar was mixed with a {c:g} L solution that was {d:g} % vinegar. Find the new concentration of vinegar.""".format(
            a = volume1, 
            b = concentration1, 
            c = volume2, 
            d = concentration2)
        
        if form == 2:
            volume1 = randomizer.toInt(10,5)
            volume2 = randomizer.toInt(6,5)
            concentration1 = randomizer.toInt(9,5)
            concentration2 = randomizer.toInt(24,5)
            clay1 = volume1 * (concentration1/100)
            clay2 = volume2 * (concentration2/100)
            
            total_clay = clay1 + clay2
            total_volume = volume1 + volume2
            total_concentration = (total_clay / total_volume)*100
            
            soln = total_concentration
            soln = round(soln,2)
            soln = str(soln) + " %"
            problem = """{name0:s} mixed {a:g} oz of soil containing {b:g} % clay with {c:g} oz of soil with {d:g} % clay. What is the clay content in the mixture?""".format(
            a = volume1, 
            b = concentration1, 
            c = volume2, 
            d = concentration2,
            name0 = name[0])

        if form == 3:
            volume1 = randomizer.toInt(10,5)
            volume2 = randomizer.toInt(12,5)
            concentration2 = randomizer.toInt(50,5)
            total_concentration = randomizer.toInt(46,5)
            
            salt2 = volume2 * (concentration2/100)
            total_volume = volume1 + volume2
            total_salt = total_volume * (total_concentration/100)
            salt1 = total_salt - salt2
            concentration1 = (salt1/volume1)*100
          
            
            soln = concentration1
            soln = round(soln,2)
            soln = str(soln) + " %"
            problem = """{name0:s} mixed {a:g} mL of a salt solution with {b:g} mL of a {c:g} % salt solution, to make a {d:g} % salt solution. Find the percent salt concentration of the first solution""".format(
            a = volume1, 
            b = volume2, 
            c = concentration2, 
            d = total_concentration,
            name0 = name[0])      
        
        if form == 4:
            mass1 = round(randomizer.toFloat(5.0,4),2)
            mass2 = round(randomizer.toFloat(5.0,4),2)
            total_mass = mass1 + mass2
            
            concentration1 = round(randomizer.toInt(50,25),2)
            concentration2 = round(randomizer.toInt(50,25),2)
            
            silver1 = mass1 * (concentration1/100)
            silver2 = mass2 * (concentration2/100)
            total_silver = silver1 + silver2
            
            total_concentration = round((total_silver/total_mass)*100,2)
       
            soln = mass1
            soln2 = mass2
            soln = round(soln,2)
            soln2 = round(soln2,2)
            
            concentration1 = round(concentration1,2)
            concentration2 = round(concentration2,2)
            soln = str(soln) +" lb of " +str(concentration1) + " % and " +str(soln2) + " lb of " + str(concentration2) + " %"
            problem = """{name0:s} needs {a:g} lb of metal with {b:g} % silver. If {name0:s} combines one metal with {c:g} % silver, and another with {d:g} % silver, how much of each metal does {name0:s} need?""".format(
            a = total_mass, 
            b = total_concentration, 
            c = concentration1, 
            d = concentration2,
            name0 = name[0])

        if form == 5:
            mass1 = randomizer.toInt(14,5)
            mass2 = randomizer.toInt(9,5)
            concentration1 = randomizer.toInt(43,5)
            concentration2 = randomizer.toInt(41,5)
            redApple1 = mass1 * (concentration1/100)
            redApple2 = mass2 * (concentration2/100)
            
            total_redApple = redApple1 + redApple2
            total_mass = mass1 + mass2
            total_concentration = (total_redApple / total_mass)*100
       
            soln = total_concentration
            soln = round(soln,2)
            soln = str(soln) +" %"
            
            problem = """{name0:s} dumped {a:g} lbs of a bag of apples with {b:g} % red apples, into a bag of {c:g} lbs which contained {d:g} % red apples. What is the new percent of red apples?""".format(
            a = mass1, 
            b = concentration1, 
            c = mass2, 
            d = concentration2,
            name0 = name[0])

        if form == 6:
            mass1 = randomizer.toInt(10,5)
            mass2 = randomizer.toInt(10,5)
            mass3 = randomizer.toInt(10,5)
            cost1 = randomizer.toInt(10,5)
            cost2 = randomizer.toInt(10,5)
            cost3 = randomizer.toInt(10,5)
            
            total_cost = mass1*cost1 + mass2*cost2 + mass3*cost3
            total_mass = mass1 + mass2 + mass3
            cost_per_mass = total_cost/total_mass
            
            soln = cost_per_mass
            soln = round(soln,2)
            soln = str(soln) +" $/lb"
            
            problem = """{name0:s}'s trail mix was made combining {a:g} lbs of peanuts that cost {b:g} $/lb, {c:g} lbs of raisins at {d:g} $/lb, and {e:g} lbs of cashews at {f:g} $/lb. What was the cost per lb of the mixture?""".format(
            a = mass1, 
            b = cost1, 
            c = mass2, 
            d = cost2,
            e = mass3,
            f = cost3,
            name0 = name[0])

        if form == 7:
            mass1 = round(randomizer.toFloat(5.0,4),2)
            mass2 = round(randomizer.toFloat(5.0,4),2)
            total_mass = mass1 + mass2
            
            concentration1 = round(randomizer.toInt(50,25),2)
            concentration2 = round(randomizer.toInt(50,25),2)
            
            peanuts1 = mass1 * (concentration1/100)
            peanuts2 = mass2 * (concentration2/100)
            total_peanuts = peanuts1 + peanuts2
            
            total_concentration = round((total_peanuts/total_mass)*100,2)
            
            soln = mass1
            soln2 = mass2
            soln = round(soln,2)
            soln2 = round(soln2,2)
            
            concentration1 = round(concentration1,2)
            concentration2 = round(concentration2,2)
            soln = str(soln) +" lb of " +str(concentration1) + " % and " +str(soln2) + " lb of " + str(concentration2) + " %"
            
            problem = """{name0:s} has two bags of nuts; one with {a:g} % peanuts, and the other with {b:g} % peanuts. To make a {c:g} lb bag of {d:g} % peanuts, how much of each should {name0:s} use?""".format(
            a = concentration1, 
            b = concentration2, 
            c = total_mass, 
            d = total_concentration,
            name0 = name[0])

        if form == 8:
            volume1 = round(randomizer.toInt(5,4),2)
            volume2 = round(randomizer.toInt(5,4),2)
            total_volume = volume1 + volume2
            
            concentration1 = round(randomizer.toInt(50,25),2)
            concentration2 = round(randomizer.toInt(50,25),2)
            
            peanuts1 = volume1 * (concentration1/100)
            peanuts2 = volume2 * (concentration2/100)
            total_peanuts = peanuts1 + peanuts2
            
            total_concentration = round((total_peanuts/total_volume)*100,2)
            
            soln = concentration1
            soln = round(soln,2)  
            
            soln = str(soln) +" %"
            
            problem = """{name0:s} mixed {a:g} L of cranberry juice into {b:g} L of apple juice, that had {c:g} % sugar. If the cranapple mixture was {d:g} % sugar, what was the percent of sugar in the cranberry juice?""".format(
            a = volume1, 
            b = volume2, 
            c = concentration2, 
            d = total_concentration,
            name0 = name[0])            
 
        if form == 9:
            mass1 = round(randomizer.toInt(5,4),2)
            mass2 = round(randomizer.toInt(5,4),2)
            total_mass = mass1 + mass2
            
            concentration1 = round(randomizer.toInt(50,25),2)
            concentration2 = 100
            
            gold1 = mass1 * (concentration1/100)
            gold2 = mass2 * (concentration2/100)
            total_gold = gold1 + gold2
            
            total_concentration = round((total_gold/total_mass)*100,2)
            
            soln = mass1
            soln = round(soln,2)  
            
            soln = str(soln) +" g"
            
            problem = """How many g of gold should a coin of {a:g} % gold be if when combined with a {b:g} g pure gold necklace, it forms a metal that is {c:g} % gold""".format(
            a = concentration1, 
            b = mass2, 
            c = total_concentration, 
            d = total_concentration,
            name0 = name[0])

        if form == 10:
            volume1 = round(randomizer.toInt(5,4),2)
            volume2 = round(randomizer.toInt(5,4),2)
            total_volume = volume1 + volume2
            
            concentration1 = round(randomizer.toInt(50,25),2)
            concentration2 = round(randomizer.toInt(50,25),2)
            
            acid1 = volume1 * (concentration1/100)
            acid2 = volume2 * (concentration2/100)
            total_acid = acid1 + acid2
            
            total_concentration = round((total_acid/total_volume)*100,2)
            
            soln = concentration1
            soln = round(soln,2)  
            
            soln = str(soln) +" %"
            
            problem = """{name0:s} mixed {a:g} mL of an acidic solution with {b:g} mL of a {c:g} % acidic solution, to make a {d:g} % acidic solution. Find the percent acid concentration of the first solution.""".format(
            a = volume1, 
            b = volume2, 
            c = concentration2,
            d = total_concentration, 
            name0 = name[0])
            
        self.question = problem
        self.soln = soln

print('MIXTURE WORD PROBLEMS')
print()

for i in range (1,10):
    A = mixtureWordProblemsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
