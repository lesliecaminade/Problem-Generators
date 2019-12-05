from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import algebra_engine
from mathsub import analytic_geometry_engine
from mathsub import differential_calculus_engine
import wolframalpha

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

VARIATIONS = 16
WOLFRAM_NAME = 'ProblemGenerator'
WOLFRAM_APPID = 'VV7LX5-5V58TH8KJX'
client = wolframalpha.Client(WOLFRAM_APPID)
class Antiderivative():
    def __init__(self):
        pass

    def init_random(self):
        print('antiderivative...')
        tryagain = True
        while tryagain:
            variation = random.randint(1, VARIATIONS)
            print(variation)

            if variation == 1:
                function = algebra_engine.random_coeff() * x **algebra_engine.random_power()
                tryagain = False
            elif variation == 2:
                function = algebra_engine.random_coeff() * x **(-algebra_engine.random_power())
                tryagain = False
            elif variation == 3:
                function = algebra_engine.random_coeff() * x **(algebra_engine.random_positive_fraction())
                tryagain = False
            elif variation == 4:
                function = algebra_engine.random_coeff() * x **(algebra_engine.random_negative_fraction())
                tryagain = False
            elif variation == 5:
                function = algebra_engine.Polynomial().init_random()
                tryagain = False
            elif variation == 6:
                function = algebra_engine.ShortPolynomial().init_types('linear-constant') * sym.sqrt(x)
                tryagain = False
            elif variation == 7:
                function = (algebra_engine.ShortPolynomial().init_types('linear-constant'))**2
                tryagain = False
            elif variation == 8:
                function = algebra_engine.Polynomial().init_random() / algebra_engine.Polynomial().init_random()
                tryagain = False
            elif variation == 9:
                function = (algebra_engine.ShortPolynomial().init_types('cubic-linear'))**2 * algebra_engine.random_coeff()*x**2
                tryagain = False
            elif variation == 10:
                function = algebra_engine.ShortPolynomial().init_types('cubic-linear')**algebra_engine.random_positive_fraction() * algebra_engine.random_coeff() * x**2 
                tryagain = False   
            elif variation == 13:
                function = algebra_engine.random_coeff() * x * (algebra_engine.ShortPolynomial().init_types('quadratic-constant'))**(1/2)
                tryagain = False
            elif variation == 14:
                function = (algebra_engine.ShortPolynomial().init_types('quadratic-constant'))**(1/3)
                tryagain = False
            elif variation == 15:
                function = algebra_engine.random_coeff() * sym.sin(x)**2 * sym.cos(x)
                tryagain = False
            elif variation == 16:
                function =(algebra_engine.random_coeff() * sym.cos(x**1/2)) / x**(1/2)
                tryagain = False
            else:
                tryagain = True



        string_query = f"""integral of {function} with respect to x"""
        wolfram = client.query(string_query)


        self.function = sym.Integral(function, x)
        self.antiderivative = next(wolfram.results).text

        
class EquationPointAndSlope():
    def __init__(self):
        pass

    def init_random(self):
        print('EquationPointAndSlope...')
        point = analytic_geometry_engine.Point()
        point.init_random()

        slope = algebra_engine.Polynomial()
        slope.init_random()

        curve = sym.Integral(slope.expression, x).doit()
        

        self.curve = curve
        self.point = point
        self.slope = slope.expression

        print('EquationPointAndSlope done.')

class ArcLength():
    def __init__(self):
        pass

    def init_random(self):
        print('Arc length')

        conic_section = algebra_engine.Bivariable().init_random_conic_section()

        print(type(conic_section))
        point1 = conic_section.point()

        point2 = conic_section.point()

        string_query = f"""arc length of {conic_section.general_string} from x = {point1.x} to x = {point2.x}"""


        wolfram = client.query(string_query)





        self.curve = conic_section.general_string
        self.point1 = point1
        self.point2 = point2
        self.arclength = next(wolfram.results).text

class AreaBetweenConicAndLine():
    def __init__(self):
        pass

    def init_random(self):

        polynomial = algebra_engine.Polynomial()
        polynomial.init_random()

        print(type(polynomial))
        point1 = polynomial.point()

        point2 = polynomial.point()

        line = analytic_geometry_engine.Line()
        line.init_two_points(point1, point2)

        string_query = f"""area between the curves of y = {polynomial.expression} and {line.string}"""


        wolfram = client.query(string_query)

        self.curve = f"""y = {polynomial.expression}"""
        self.line = line.string
        self.area = next(wolfram.results).text

class AreaBetweenTwoConics():

    def __init__(self):
        pass

    def init_random(self):
        conic_section1 = algebra_engine.Bivariable().init_random_conic_section_no_hyperbola()
        conic_section2 = algebra_engine.Bivariable().init_random_conic_section_no_hyperbola()

        string_query = f"""area between the curves {conic_section1.general_string} and {conic_section2.general_string}"""

        wolfram = client.query(string_query)

        self.curve1 = conic_section1.general_string
        self.curve2 = conic_section2.general_string
        self.area = next(wolfram.results).text

# class CentroidBetweenTwoConics():

#     def __init__(self):
#         pass

#     def init_random(self):
#         conic_section1 = algebra_engine.Bivariable().init_random_conic_section_no_hyperbola()
#         conic_section2 = algebra_engine.Bivariable().init_random_conic_section_no_hyperbola()

#         string_query = f"""centroid of the area between the curves {conic_section1.general_string} and {conic_section2.general_string}"""

#         wolfram = client.query(string_query)

#         self.curve1 = conic_section1.general_string
#         self.curve2 = conic_section2.general_string
#         self.centroid = next(wolfram.results).text

# class SolidOfRevolution():

#     def __init__(self):
#         pass

#     def init_random(self):
#         #create a parabola
#         parabola = analytic_geometry_engine.Parabola()
#         orientation = random.choice(['concave upward', 'concave downward'])
#         parabola.init_random(orientation = orientation)

#         #picktwopoints at the parabola
#         point1, point2 = parabola.points_in_line()

#         #create a line from these two points
#         line = analytic_geometry_engine.Line()
#         line.init_two_points(point1, point2)

#         #pick an axis of rotation
#         axis_rotation_types = ['x-axis', 'y-axis']
#         aor = random.choice(axis_rotation_types)

#         # #create the axis of rotation equation
#         # aor = analytic_geometry_engine.Line()
#         # random_point = analytic_geometry_engine.Point()
#         # random_point.init_random()
#         # another_point = analytic_geometry_engine.Point()

#         # if axis_rotation_type == 'vertical':
#         #     another_point.init_define(random_point.x, random_point.y + 1)
#         #     aor.init_two_points(random_point, another_point)
#         # elif axis_rotation_type == 'horizontal':
#         #     another_point.init_define(random_point.x + 1, random_point.y)
#         #     aor.init_two_points(random_point, another_point)
#         # elif axis_rotation_type == 'line':
#         #     aor.init_random()
#         # else:
#         #     raise InternalError('invalid axis or rotation type')



#         string_query = f"""rotate the region between | {parabola.general_string} | {line.string} | x from 0 to 1 | around the {aor}"""

#         wolfram = client.query(string_query)

#         self.curve1 = parabola.general_string
#         self.curve2 = line.string
#         self.axis_of_rotation = aor
#         try:
#             self.volume = next(wolfram.results).text
#         except:
#             self.volume = wolfram










































































































        




























































