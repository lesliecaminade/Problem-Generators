import random
from mathsub import differential_calculus as source

print('Generating...')
file_name = 'differential_calculus'

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

questionList = [
source.continuity_piecewise_function_linear_linear(),
source.continuity_piecewise_function_parabola_linear(),
source.discontinuity_piecewise_function_point(),
source.discontinuity_piecewise_function_jump(),

#first derivatives
source.Derivative_explicit()
# source.first_derivative_explicit_yofx_xoft_dydt(),
# source.first_derivative_explicit_xoft_yoft_dydx(),
# source.first_derivative_implicit(),

# #second derivatives
# source.second_derivative_implicit(),

# #tangent and normal lines
# source.tangent_line_from_conic_section(),
# source.normal_line_from_conic_section()
]

#hard to generate questions
if not TESTMODE:
    tryagain = True
    while tryagain:
        try:
            additional_questionlist = [
            # #relative maxima and minima
            # source.polynomial_critical_numbers(),
            # source.polynomial_relative_maxima(),
            # source.polynomial_relative_minima(),
            # source.polynomial_increasing_interval(),
            # source.polynomial_decreasing_interval(),

            # #maxima minima
            # source.product_of_two_numbers_x_y(),
            # source.product_of_two_numbers_xsquared_y(),
            # source.paper_with_margins(),
            # source.ships_moving_at_axis(),
            # source.can_with_minimum_area_open(),
            # source.can_with_minimum_area_closed(),
            # source.manufacturing_items(),
            # source.man_in_rowboat(),
            # source.rectangular_fence(),
            # source.wall_and_beam_and_building()
            ]
            tryagain = False
        except:
            pass
else:
    additional_questionlist = [
    #relative maxima and minima
    # source.polynomial_critical_numbers(),
    # source.polynomial_relative_maxima(),
    # source.polynomial_relative_minima(),
    # source.polynomial_increasing_interval(),
    # source.polynomial_decreasing_interval(),

    # #maxima minima
    # source.product_of_two_numbers_x_y(),
    # source.product_of_two_numbers_xsquared_y(),
    # source.paper_with_margins(),
    # source.ships_moving_at_axis(),
    # source.can_with_minimum_area_open(),
    # source.can_with_minimum_area_closed(),
    # source.manufacturing_items(),
    # source.man_in_rowboat(),
    # source.rectangular_fence(),
    # source.wall_and_beam_and_building()
    ]



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
file = open(f"{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')
for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print_taks(item)
    write_to_file(item)


    try:
        print(item.choices)
        print()
    except:
        pass


stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
