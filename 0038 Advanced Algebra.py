import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import algebra as alg
from generator import random_handler as ran

x, y = sym.symbols('x y', real = True)

TESTMODE = True

print('Created by: Leslie Caminade')

questionList = (
alg.algebra_1(),
alg.algebra_2(),
alg.algebra_3(),
alg.algebra_4(),
alg.algebra_5(),
alg.algebra_6(),
alg.algebra_7(),
alg.algebra_8(),
alg.algebra_9(),
alg.algebra_10(),
alg.algebra_11(),
alg.algebra_12(),
alg.algebra_13(),
alg.algebra_14(),
alg.algebra_15(),
alg.algebra_16(),
alg.algebra_17(),
alg.algebra_18(),
alg.algebra_19(),
alg.algebra_20(),
alg.algebra_21(),
alg.algebra_22(),
alg.algebra_23(),
alg.algebra_24(),
alg.algebra_25(),
alg.algebra_26(),
alg.algebra_27(),
alg.algebra_28(),
alg.algebra_29(),
alg.algebra_30(),
alg.algebra_31()
)



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
