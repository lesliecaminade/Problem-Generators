import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import analytic_geometry as source
from generator import random_handler as ran

def write_to_file(some_object):   
    if FILEMODE: 
        file.write(some_object.question)
        file.write('\n')
        file.write(some_object.answer)
        file.write('\n\n')

def print_taks(some_object):
    print(some_object.question)
    print()
    print(some_object.answer)
    print()
    print()

TESTMODE = True
FILEMODE = True

file_name = 'analytic_geometry'

questionList = [
#insert hard to generate questions here
source.Distance_between_two_points(),
#source.Quadrant_identification()
source.Midpoint(),
source.Extension_of_line_segment(),
source.Extension_of_line_segment_by(),
source.Division_of_line_segment(),
source.Equation_of_a_line_two_points(),
source.Equation_of_a_line_point_slope(),
source.Equation_of_a_line_slope_intercept(),
source.Equation_of_a_line_intercepts(),
source.Line_parallel_to_line(),
source.Line_perpendicular_to_line(),
source.Angle_between_the_lines(),
source.Distance_from_point_to_line(),
source.Distance_from_line_to_line(),
source.Area_of_three_points()
]

questionList = questionList



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

file = open(f"{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')
for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print_taks(item)
    write_to_file(item)

print()
file.close()
print('Finished.')
stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False