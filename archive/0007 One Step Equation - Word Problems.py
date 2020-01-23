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


class oneStepEquationWordProblemsClass:

    def __init__(self):
        #try:
        coe = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []

        form = random.randint(1,14)
        
        for i in range(0,20):
            coe.append(round(random.randint(10,30),2))
            
        fname = random.sample(femaleNames,5)
        mname = random.sample(maleNames,5)
        sport = random.sample(allSports,2)
        
        if form == 1:
            variable = coe[1] + coe[2]
            soln = coe[2]
            problem = """ There were {a:g} bales of hay in the barn and {b:g} bales in the shed. {name0:s} stacked more bales in the barn today. There are now {c:g} bales of hay in the barn. How many bales did he store in the barn?""".format(a = coe[1], b = coe[3], c = variable, name0 = mname[0])
        if form == 2:
            variable = coe[1] + coe[2]
            soln = coe[2]
            problem = """ {name0:s} found {a:g} seashells and {b:g} starfishes on the beach. She gave {name1:s} some of her seashells. She has {c:g} seashell left. How many seashells did she give to {name1:s}?""".format(a = variable, b = coe[3], c = coe[1], name0 = fname[0], name1 = fname[1])
        if form == 3:
            variable = coe[1] + coe[2]
            soln = coe[2]
            problem = """ {name0:s} had {a:g} peaches and {b:g} pears left at her roadside fruit stand. She went to the orchard and picked more peaches to stock up the stand. There are now {c:g} peaches at the stand, how many did she pick  ?""".format(a = variable, b = coe[3], c = coe[1], name0 = fname[0])
        if form == 4:
            variable = coe[1] + coe[2]
            soln = coe[2]
            problem = """ {name0:s} received {a:g} dollars and {c:g} movie tickets for his birthday. He went to a sporting goods store and bought a baseball glove, baseball, and bat. He had {b:g} dollars left over, how much did he spent on the baseball gear?""".format(a = variable, b = coe[1], c = coe[3], name0 = mname[0])
        if form == 5:
            variable = coe[1] + coe[2]
            soln = coe[2]
            problem = """ {name0:s}'s high school played {a:g} {sport:s} games this year. The team won most of their games. They were defeated during {b:g} games. How many games did they win?""".format(a = variable, b = coe[1], c = coe[3], name0 = mname[0], sport = sport[0]) 
        if form == 6:
            variable = coe[1] + coe[2]
            soln = coe[2]
            problem = """ {name0:s} has {a:g} books and {b:g} magazines in his library. He bought several books at a yard sale over the weekend. He now has {c:g} books in his library. How many books did he buy at the yard sale?""".format(a = variable, b = coe[1], c = coe[3], name0 = mname[0])
        if form == 7:
            variable = coe[1] + coe[2]
            soln = variable
            problem = """ After paying {a:g} dollars for the pie, {name0:s} has {b:g} dollars left, her friend has {c:g} dollars. How much money did she have before buying the pie?""".format(a = coe[1], b = coe[2], c = coe[3], name0 = fname[0]) 
        if form == 8:
            variable = coe[1]*coe[2]
            soln = coe[2]
            problem = """ The store has CD's and DVD's that you need. How many packs of DVD's can you buy with {a:g} dollars if one pack costs {b:g} dollars?""".format(a = variable, b = coe[1], c = coe[3], name0 = fname[0]) 
        if form == 9:
            variable = coe[1]+coe[2]
            soln = coe[2]
            problem = """ {name0:s} is baking a cake. The recipe calls for {a:g} cups of flour and {b:g} cups of sugar. She already put in {c:g} cups of flour. How many more cups of flour does she need to add?""".format(a = variable, b = coe[3], c = coe[1], name0 = fname[0])
        if form == 10:
            variable = coe[1]*coe[2]
            soln = coe[2]
            problem = """  The company has large and small ink cartridges in stock. How many ink cartridges can you buy with {a:g} dollars if one cartridge costs {b:g} dollars?""".format(a = variable, b = coe[1], c = coe[3], name0 = fname[0])   
        if form == 11:
            variable = coe[1]+coe[2]
            soln = coe[2]
            problem = """Last week {name0:s} had {a:g} dollars and {name1:s} had {b:g} dollars. {name0:s} washed cars over the weekend and now has {c:g} dollars. How much money did {name0:s} make washing cars?""".format(a = coe[1], b = coe[3], c = variable, name0 = mname[0], name1 = mname[1]) 
        if form == 12:
            variable = coe[1]*3
            soln = variable
            problem = """After eating at the restaurant, {name0:s}, {name1:s}, and {name2:s} decided to divide the bill evenly. {name1:s} did not have dessert. If each person paid {a:g} dollars, what was the total of the bill?""".format(a = coe[1], b = coe[3], c = variable, name0 = mname[0], name1 = fname[0], name2 = fname[1])            
        if form == 13:
            variable = coe[1]+coe[2]
            soln = coe[2]
            problem = """ There were {a:g} red roses and {b:g} white roses in the vase. {name0:s} cut some more roses from her flower garden. There are now {c:g} red roses in the vase. How many red roses did she cut?""".format(a = coe[1], b = coe[3], c = variable, name0 = fname[0], name1 = fname[0], name2 = fname[1])  
        if form == 14:
            variable = coe[1]+coe[2]
            soln = coe[2]
            problem = """ There are {a:g} oak trees and {b:g} popular trees currently in the park. Park workers will plant more oak trees today. When the workers are finished there will be {c:g} oak trees in the park. How many oak trees did the workers plant today?""".format(a = coe[1], b = coe[3], c = variable, name0 = fname[0], name1 = fname[0], name2 = fname[1]) 

        self.question = problem
        self.soln = soln

            
print('ONE STEP WORD PROBLEMS')
print()

for i in range (1,10):
    A = oneStepEquationWordProblemsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
