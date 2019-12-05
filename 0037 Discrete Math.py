import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import discrete_math as discrete
from generator import random_handler as ran

x, y = sym.symbols('x y', real = True)

print('Created by: Leslie Caminade')

TESTMODE = True

questionList = [
discrete.binomial_1(),
discrete.binomial_2(),
discrete.binomial_3(),
discrete.binomial_4(),
discrete.binomial_5(),
discrete.binomial_6(),
discrete.binomial_7(),
discrete.binomial_8()
]



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
if not TESTMODE:
    items_list = random.sample(total_items_list, round(1 * len(questionList)))
else:
    items_list = total_items_list

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
