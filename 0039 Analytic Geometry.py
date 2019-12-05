import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import analytic_geometry as source
from generator import random_handler as ran

x, y = sym.symbols('x y', real = True)

print('Created by: Leslie Caminade')

TESTMODE = False

questionList = [
source.distance_between_two_points(),
source.quadrant_identification(),
source.midpoint_of_two_points(),
source.extension_of_line_segment(),
source.division_of_line_segment(),
source.equation_of_a_line_two_points(),
source.equation_of_a_line_point_slope(),
source.equation_of_a_line_slope_intercept(),
source.equation_of_a_line_intercepts(),
source.line_parallel_to_line(),
source.line_perpendicular_to_line(),
source.angle_between_two_lines(),
source.distance_from_point_to_line(),
source.distance_from_line_to_line(),
source.area_of_3_points()
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
