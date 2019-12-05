import random_handler as ran
import sympy as sym
import math
import random
import field_effect_transistors as fet

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *

title_string = """Field Effect Transistors
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
fet.boylestad_7_1(),
fet.boylestad_7_2(),
#fet.boylestad_7_3(),
fet.boylestad_7_4(),
fet.boylestad_7_5(),
fet.boylestad_7_6(),
#fet.boylestad_7_7()
fet.boylestad_7_8(),
fet.boylestad_7_10(),
fet.boylestad_7_11(),
fet.boylestad_8_7(),
fet.boylestad_8_8(),
fet.boylestad_8_9(),
fet.boylestad_8_10(),
fet.boylestad_8_11(),
fet.boylestad_8_12()
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
