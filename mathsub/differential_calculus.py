from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import differential_calculus_engine as engine
from mathsub import algebra_engine

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

def ask():
    ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
    return random.choice(ask_words)

def parse(string_input):
    string_input = str(string_input)
    return string_input.replace('**', '^').replace('*', ' ')    



class continuity_piecewise_function_linear_linear():
    def __init__(self):

        piecewise = engine.ContinuousPiecewise()
        piecewise.init_random(parts = 2, type = 'line.line')

        self.question = f"""The piecewise function {piecewise.function} is continuous. Determine the values inside the function that makes the function continuous."""
        self.answer = f"""ANSWERS GENERATED ABOVE"""

class continuity_piecewise_function_parabola_linear():
    def __init__(self):

        piecewise = engine.ContinuousPiecewise()
        piecewise.init_random(parts = 2, type = 'parabola.line')

        self.question = f"""The piecewise function {piecewise.function} is continuous. Determine the values inside the function that makes the function continuous."""
        self.answer = f"""ANSWERS GENERATED ABOVE"""

class discontinuity_piecewise_function_point():
    def __init__(self):

        piecewise = engine.PointDiscontinuity()
        piecewise.init_random()

        self.question = f"""Identify what type of discontinuity the function {piecewise.function} has."""
        self.answer = f"""{piecewise.type}, discontinuous at x = {piecewise.point_of_discontinuity}"""

class discontinuity_piecewise_function_jump():
    def __init__(self):

        piecewise = engine.JumpDiscontinuity()
        piecewise.init_random()

        self.question = f"""Identify what type of discontinuity the function {piecewise.function} has."""
        self.answer = f"""{piecewise.type}, discontinuous at x = {piecewise.point_of_discontinuity} with a magnitude of {piecewise.magnitude}."""

# class first_derivative_explicit():
#     def __init__(self):

#         problem = engine.DerivativeExplicit()
#         problem.init_random()

#         self.question = f"""Differentiate {problem.function_string}."""
#         self.answer = f"""{problem.derivative()}"""

class Derivative_explicit():
    def __init__(self):
        BATTERIES = []
        CHOICES = []
        suffix = ''
        prefix = ''
        for i in range(4):
            #battery = engine.Some_class_from_engine
            battery = engine.Derivative_explicit()
            #data = battery.Some_attribute_from_battery         
            data =  parse(battery.derivative())
            BATTERIES.append(battery)
            CHOICES.append(prefix + str(data) + suffix) 
        main = BATTERIES[0]
        CHOICES[0] = str(CHOICES[0]) + ' #'
        random.shuffle(CHOICES)
        #edit below
        self.question = f"""{ask()} the first derivative of the function f(x) = {parse(main.function)}."""

        self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class first_derivative_explicit_yofx_xoft_dydt():
    def __init__(self):

        problem = engine.DerivativeExplicit_yofx_xoft_dydt()
        problem.init_random()

        self.question = f"""If y(x) = {problem.y_of_x} and x(t) = {problem.x_of_t}, determine the value of dy/dt at t = {problem.t}."""
        self.answer = f"""{problem.dydt_at_t}"""

class first_derivative_explicit_xoft_yoft_dydx():
    def __init__(self):

        problem = engine.DerivativeExplicit_xoft_yoft_dydx()
        problem.init_random()

        self.question = f"""If x(t) = {problem.x_of_t}, and y(t) = {problem.y_of_t}, determine the value of dy/dx at t = {problem.t}."""
        self.answer = f"""{problem.dydx_at_t}"""

class first_derivative_implicit():
    def __init__(self):

        problem = engine.DerivativeImplicit_Bivariable()
        problem.init_random()

        self.question =  f"""For the function {problem.expression} = 0, determine the value of dy/dx."""
        self.answer = f"""{problem.dydx}"""

class second_derivative_implicit():
    def __init__(self):

        problem = engine.DerivativeImplicit_Bivariable()
        problem.init_random()

        self.question =  f"""For the function {problem.expression} = 0, determine the value of d^2y/dx^2."""
        self.answer = f"""{problem.dydx}"""

class tangent_line_from_conic_section():
    def __init__(self):

        problem = engine.TangentLine_from_ConicSection()
        problem.init_random()

        self.question = f"""For the graph of the function {problem.general_string}, determine the equation of the line tangent to the curve at the point {problem.point_of_tangency.string}."""
        self.answer = f"""{problem.tangent_line.string}"""

class normal_line_from_conic_section():
    def __init__(self):

        problem = engine.NormalLine_from_ConicSection()
        problem.init_random()

        self.question = f"""For the graph of the function {problem.general_string}, determine the equation of the line normal to the curve at the point {problem.point_of_tangency.string}."""
        self.answer = f"""{problem.normal_line.string}"""

class polynomial_critical_numbers():
    def __init__(self):
        tryagain = True
        while tryagain:
            try:
                problem = engine.RelativeExtrema_Polynomials()
                problem.init_random()

                WORDING_LIST = ['critical points', 'relative extrema']

                self.question = f"""Determine the {random.choice(WORDING_LIST)} of the function f(x) = {problem.polynomial.expression}."""
                
                points_string = ""

                for i in range(len(problem.critical_points)):
                    points_string = points_string + problem.critical_points[i].string + ' '

                self.answer = f"""{points_string}"""
                tryagain = False
            except:
                pass

class polynomial_relative_maxima():
    def __init__(self):
        tryagain = True
        while tryagain:
            try:
                problem = engine.RelativeExtrema_Polynomials()
                problem.init_random()


                self.question = f"""Determine the relative maxima of the function f(x) = {problem.polynomial.expression}."""
                
                points_string = ""

                for i in range(len(problem.relative_maxima)):
                    points_string = points_string + problem.relative_maxima[i].string + ' '

                self.answer = f"""{points_string}"""    
                tryagain = False
            except:
                tryagain = True    

class polynomial_relative_minima():
    def __init__(self):

        problem = engine.RelativeExtrema_Polynomials()
        problem.init_random()


        self.question = f"""Determine the relative minima of the function f(x) = {problem.polynomial.expression}."""
        
        points_string = ""

        for i in range(len(problem.relative_minima)):
            points_string = points_string + problem.relative_minima[i].string + ' '

        self.answer = f"""{points_string}""" 

class polynomial_increasing_interval():
    def __init__(self):

        problem = engine.RelativeExtrema_Polynomials()
        problem.init_random()


        self.question = f"""Determine the interval that the function f(x) = {problem.polynomial.expression} is increasing"""
        
        self.answer = f"""{problem.interval_increasing}"""

class polynomial_decreasing_interval():
    def __init__(self):

        problem = engine.RelativeExtrema_Polynomials()
        problem.init_random()


        self.question = f"""Determine the interval that the function f(x) = {problem.polynomial.expression} is decreasing"""
        
        self.answer = f"""{problem.interval_decreasing}"""

class product_of_two_numbers_x_y():
    def __init__(self):

        problem = engine.ProductOfTwoNumbers_x_y()
        problem.init_random()


        self.question = f"""Among those positive real numbers u and v whose sum is {problem.sum_of_numbers}, find the choice of u and v that makes their product P as much as possible"""
        
        self.answer = f"""{problem.number1}, {problem.number2}"""    

class product_of_two_numbers_xsquared_y():
    def __init__(self):

        problem = engine.ProductOfTwoNumbers_xsquared_y()
        problem.init_random()


        self.question = f"""Divide the number {problem.sum_of_numbers} into two parts such that the product P of one part and the square of the other is a maximum."""
        
        self.answer = f"""{problem.number1}, {problem.number2}""" 

class paper_with_margins():
    def __init__(self):

        paper = engine.PaperWithMargins()
        paper.init_random()

        self.question = f"""A sheet of paper for a poster is to be {paper.area} cm^2 in area. The margins at the top and bottom are to be {paper.margin_length_one_side} cm and at the sides to be {paper.margin_width_one_side} cm. What should be the dimensions of the sheet to maximize the printed area?"""
        self.answer = f"""{paper.length} cm x {paper.width} cm"""

class ships_moving_at_axis():
    def __init__(self):

        ships = engine.MovingAtAxis()
        ships.init_random()

        self.question = f"""At t = 0, Ship B is {ships.B_initial_distance_from_A} miles due east of another ship A. Ship B is then sailing due west at {ships.B_velocity} miles per hpour, and A is sailing due south at {ships.A_velocity} miles per hour. If they continue on their respective courses, when will they be nearest one another, and how near?"""
        self.answer = f"""{ships.time_nearest} hours, {ships.distance_nearest} miles"""

class can_with_minimum_area_open():
    def __init__(self):

        can = engine.CanWithMinimumArea_Open()
        can.init_random()

        self.question = f"""A cylinder container with circular base is to hold {can.volume} cm^3. Find its dimensions so that the amount (surface area) of metal required is minimum when the container is an open can."""
        self.answer = f"""radius: {can.radius} cm, height: {can.height} cm"""


class can_with_minimum_area_closed():
    def __init__(self):

        can = engine.CanWithMinimumArea_Closed()
        can.init_random()

        self.question = f"""A cylinder container with circular base is to hold {can.volume} cm^3. Find its dimensions so that the amount (surface area) of metal required is minimum when the container is an closed can."""
        self.answer = f"""radius: {can.radius} cm, height: {can.height} cm"""
        
class manufacturing_items():
    def __init__(self):

        plant = engine.Manufacturing()
        plant.init_random()

        self.question = f"""The total cost of producing x radio sets per day is PHP {plant.cost_function}, and the price per set at which they may be sold is PHP {plant.price_function}. What should be the daily output to obtain a maximum total profit?"""

        self.answer = f"""{plant.items_at_profit_max} items"""


class man_in_rowboat():
    def __init__(self):

        boat = engine.ManInRowBoat()
        boat.init_random()

        self.question = f"""A man in a rowboat at P, {boat.PA_distance} miles from the nearest point A on a straight shorem wishes to reach a point B, {boat.AB_distance} miles from A along the shore, in shortest time. Where should he land if he can row {boat.row_speed} miles per hour and walk {boat.walk_speed} miles per hour?"""

        self.answer = f"""{boat.distance_at_time_smallest} miles from point A, {boat.time_smallest} hours"""

class rectangular_fence():
    def __init__(self):

        fence = engine.RectangularFence()
        fence.init_random()

        self.question = f"""A given rectangular area that is {fence.area} m^2 is to be fenced off in a field that lies along a stright river. If no fencing is need along the river, determine the least amount of fencing required."""
        self.answer = f"""{fence.perimeter} m"""

class wall_and_beam_and_building():
    def __init__(self):

        structure = engine.WallAndBuilding()
        structure.init_random()

        self.question = f"""A wall of a building is to be braced by a beam that must pass over parallel wall {structure.wall_height} ft high and {structure.wall_distance} ft from the building. Find the length of the shortest beam that can be used."""
        self.answer = f"""{structure.beam_length} ft"""


























































































































 
















        
















 































































