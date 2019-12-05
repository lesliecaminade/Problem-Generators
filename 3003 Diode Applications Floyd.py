
import random_handler as ran
import sympy as sym
import math
import random
import diodes as d

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *

solutions_flag = False

title_string = """Diode Applications
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
d.floyd_2_1_a(),
d.floyd_2_1_b(),
d.floyd_2_2(),
d.floyd_2_3(),
d.floyd_2_4(),
d.floyd_2_5(),
d.floyd_2_6(),
d.floyd_2_7(),
d.floyd_2_8(),
d.floyd_2_9(),
d.floyd_2_10(),
d.floyd_2_11(),
d.floyd_2_12(),
d.floyd_2_13(),
d.floyd_3_5(),
d.floyd_3_6(),
d.floyd_3_7(),
d.floyd_3_8_a()
)


class genericClass:

    def __init__(self):
        question = ""
        answer = ""
        
        solution = ""
      
        temp = random.randint(0,len(questionList)-1)
        try:
            q = questionList[temp]
            self.question = q.question
            self.answer = q.answer
            try:
                self.choices = q.choices
            except:
                self.choices = ''
            
            try:
                self.solution = q.solution
                
            except:
                self.solution = 'no solution provided'
        except:
            pass

            



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(1 * len(questionList)))


print(title_string)
print()
print(items_list)

for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print(item.question)
    print()
    print(item.answer)

stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
