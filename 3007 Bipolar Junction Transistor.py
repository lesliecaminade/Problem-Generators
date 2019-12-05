
import random_handler as ran
import sympy as sym
import math
import random
import bipolar_junction_transistors as bjt

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *


title_string = """Bipolar Junction Transistors
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
bjt.boylestad_4_1(),
bjt.boylestad_4_2(),
bjt.boylestad_4_3(),
bjt.boylestad_4_6(),
bjt.boylestad_4_8(),
bjt.boylestad_4_12(),
bjt.boylestad_4_14(),
bjt.boylestad_4_16(),
bjt.boylestad_4_17(),
bjt.boylestad_4_18(),
bjt.boylestad_4_19(),
bjt.boylestad_4_20(),
bjt.boylestad_4_27(),
bjt.boylestad_4_28(),
bjt.boylestad_4_29(),
bjt.boylestad_4_30(),
bjt.boylestad_4_31(),
bjt.boylestad_4_32(),
bjt.boylestad_4_35(),
bjt.boylestad_4_36(),
bjt.boylestad_4_37()
)


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
