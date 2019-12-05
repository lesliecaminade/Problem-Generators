from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import integral_calculus_engine as engine
from mathsub import algebra_engine

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables


class antiderivative():
    def __init__(self):

        main = engine.Antiderivative()
        main.init_random()

        self.question = f"""Evaluate the antiderivative: {main.function}"""
        self.answer = f"""{main.antiderivative}"""

class equation_point_and_slope():
    def __init__(self):

        main = engine.EquationPointAndSlope()
        main.init_random()

        self.question = f"""Find an equation of the curve passing through the point {main.point.string} and having slope {main.slope} at every point (x, y)."""
        self.answer = f"""y = {main.curve}"""

class arc_length_of_conic_section():

    def __init__(self):

        main = engine.ArcLength()
        main.init_random()

        self.question = f"""Determine the length of arc of the curve {main.curve} from the points {main.point1.string} to {main.point2.string}"""

        self.answer = f"""{main.arclength}"""

class area_between_conic_section_and_line():
    def __init__(self):

        main = engine.AreaBetweenConicAndLine()
        main.init_random()

        self.question = f"""Determine the area between the curve {main.curve} and the line {main.line}"""

        self.answer = f"""{main.area}"""

class area_between_two_conics():
    def __init__(self):

        main = engine.AreaBetweenTwoConics()
        main.init_random()

        self.question = f"""Determine the area between the curve {main.curve1} and the line {main.curve2}"""

        self.answer = f"""{main.area}"""    

class volume_solid_of_revolution_parabola_line():
    def __init__(self):

        main = engine.SolidOfRevolution()
        main.init_random()

        self.question = f"""Determine the volume of the solid of revolution if the area between the curves {main.curve1} and {main.curve2} is rotated around the line {main.axis_of_rotation}"""

        self.answer = f"""{main.volume}"""     


class centroid_between_two_conics():
    def __init__(self):
        main = engine.CentroidBetweenTwoConics()
        main.init_random()

        self.question = f"""Determine the coordinates of the centroid of area between the curves {main.curve1} and {main.curve2}."""
        self.answer = f"""{main.centroid}"""

























































































































 
















        
















 































































