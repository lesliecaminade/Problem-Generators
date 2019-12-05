import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import integral_calculus as source
from generator import random_handler as ran

x, y = sym.symbols('x y', real = True)

print('Generating...')

TESTMODE = True

questionList = [
source.antiderivative(),
source.equation_point_and_slope(),
source.arc_length_of_conic_section(),
source.area_between_conic_section_and_line(),
source.area_between_two_conics(),
#source.volume_solid_of_revolution_parabola_line()
# source.centroid_between_two_conics()
]

#hard to generate questions

tryagain = True
while tryagain:
    try:
        additional_questionlist = [
        #insert hard to generate questions here
        ]
        tryagain = False
    except:
        pass



questionList = questionList + additional_questionlist



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
    print(item.answer + '        --------------------------------- answer')
    print()
    print()

    try:
        print(item.choices)
        print()
    except:
        pass

print()
print('Finished.')
stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
