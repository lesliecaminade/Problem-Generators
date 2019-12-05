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
import integral_calculus
import analytic_geometry
import differential_equations
import algebra
#import physics
import strength_of_materials as strength

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Strength of Materials - Singer and PYtel
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""

questionList = (
strength.singer_104(),
strength.singer_105(),
strength.singer_106(),
strength.singer_107(),
strength.singer_108(),
strength.singer_109(),
strength.singer_110(),
strength.singer_115(),
strength.singer_116(),
strength.singer_117(),
strength.singer_125(),
strength.singer_126(),
strength.singer_127(),
strength.singer_133(),
strength.singer_134(),
strength.singer_135(),
strength.singer_136(),
strength.singer_138(),
strength.singer_141(),
strength.singer_142(),
strength.singer_206(),
strength.singer_207(),
strength.singer_208(),
strength.singer_209(),
strength.singer_211(),
strength.singer_223(),
strength.singer_225(),
strength.singer_226(),
strength.singer_227(),
strength.singer_228(),
strength.singer_233(),
strength.singer_234(),
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
