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
source.derivation_of_conic_sections(),
#circles
source.standard_to_general_circle(),
source.circumference_from_general(),
source.general_from_three_points(),
source.coefficient_from_general_and_radius(),
source.distance_from_circle_and_point(),
source.center_from_general(),
source.area_from_general(),
source.area_from_center_and_tangent_line(),
source.center_to_line_distance(),
source.length_of_tangent_from_general_and_point(),
source.ratio_of_circumferences(),
source.diameter_from_general(),

#parabolas
source.focal_length_from_general(),
source.latus_rectum_from_general(),
source.latus_rectum_from_directrix_and_focus(),
source.parabola_from_three_points(),
source.parabola_from_vertex_and_focus(),
source.parabola_from_directrix_and_point(),
source.focus_from_general_parabola(),
source.directrix_from_general_parabola(),
source.concavity_from_general_parabola(),
source.area_bounded_by_parabola_and_latus_rectum(),

#ellipse
source.eccentricity_from_general_ellipse(),
source.eccentricity_from_major_axis_minor_axis(),
source.area_from_general_ellipse(),
source.longest_focal_radius_ellipse_from_point_center_orientation(),
source.longest_focal_radius_ellipse_from_distance_between_vertices_eccentricity(),
source.circumference_from_general_equation_ellipse(),
source.general_from_sum_of_distances_two_foci__eccentricity_ellipse(),
source.semi_major_axis_from_distance_between_foci_and_eccentricity_ellipse(),
source.major_axis_from_general_ellipse(),
source.distance_from_y_axis_to_focus_ellipse_vertical(),
source.center_from_general_ellipse(),
source.distance_between_directrices_from_general_ellipse(),
source.directrix_equation_from_general_ellipse(),
source.latus_rectum_length_from_general_ellipse(),

#hyperbola
source.center_from_general_hyperbola(),
source.eccentricity_from_general_hyperbola(),
source.equation_of_asymptotes_from_general_hyperbola(),
source.latus_rectum_from_general_hyperbola(),
source.general_hyperbola_from_asymptotes_and_point(),
source.general_hyperbola_difference_between_distance_foci(),
source.semi_conjugate_axis_from_general_hyperbola()
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
