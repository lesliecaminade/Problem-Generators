import randomizer
import random_handler as ran
import sympy_handler as symh
import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import oo

import math
import math_common
import random
import stringHandling


import amplitude_modulation as am

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Amplitude Modulation
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
am.schaums_ec_3_1(),
am.schaums_ec_3_2(),
am.schaums_ec_3_3(),
am.schaums_ec_3_4(),
am.schaums_ec_3_5(),
am.schaums_ec_3_6(),
am.schaums_ec_3_7(),
am.schaums_ec_3_8(),
am.schaums_ec_3_9(),
am.schaums_ec_3_10(),
am.schaums_ec_3_11(),
am.schaums_ec_3_12(),
am.schaums_ec_3_13(),
am.schaums_ec_3_14(),
am.schaums_ec_3_15(),
am.schaums_ec_3_16(),
am.schaums_ec_3_17(),
am.schaums_ec_3_19(),
am.schaums_ec_3_20(),
am.schaums_ec_3_21(),
am.jma_1_40_a(),
am.jma_1_40_b(),
am.jma_1_42(),
am.jma_1_43_a(),
am.jma_1_43_b(),
am.jma_1_46_a(),
am.jma_1_46_b(),
am.jma_1_46_c(),
am.jma_1_47_a(),
am.jma_1_47_b(),
am.jma_1_49(),
am.jma_1_50(),
am.jma_1_52_a(),
am.jma_1_52_b()
)


#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(0.25 * len(questionList)))


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
