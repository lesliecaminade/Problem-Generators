import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import analytic_geometry as source
from generator import random_handler as ran
import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
folderpath = os.path.dirname(os.path.realpath(__file__))

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

file_name = 'analytic_geometry 2'

questionList = [
source.Conic_section_derivation(),
source.Circle_standard_to_general(),
source.Circle_circumference_from_general(),
source.Circle_general_from_three_points(),
source.Circle_coefficient_from_general_and_radius(),
source.Circle_distance_from_point(),
source.Circle_center_from_general(),
source.Circle_area_from_general(),
source.Circle_area_from_center_and_tangent_line(),
source.Circle_center_to_line_distance(),
source.Circle_length_of_tangent_from_general_and_point(),
source.Circle_ratio_of_circumference(),
source.Circle_diameter_from_general(),
source.Parabola_diameter_from_general(),
source.Parabola_latus_rectum_from_general(),
source.Parabola_latus_rectum_from_directrix_and_focus(),
source.Parabola_from_three_points(),
source.Parabola_from_vertex_and_focus(),
source.Parabola_focus_from_general(),
source.Parabola_directrix_from_general(),
source.Ellipse_eccentricity_from_general(),
source.Ellipse_eccentricity_from_major_minor()
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

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')
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