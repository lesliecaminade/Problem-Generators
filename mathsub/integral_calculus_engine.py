from generator import constants_conversions as c
from generator import random_handler as ran

import sympy
import math
import random

x, y, z, t = sympy.symbols('x y z t', real = True)#generic variables

def choice(number, *args, **kwargs):
    try:
        suffix = args[0]
    except:
        suffix = ''

    try:
        rounding_level = kwargs['round']
    except:
        rounding_level = 2

    new = round(random.gauss(number, 0.1 * number), rounding_level)
    if number%1 == 0:
        return f"""{int(new)} {suffix}"""
    else:
        return f"""{new} {suffix}"""

class besavilla_470_a():
    def __init__(self):
        
        choice_a = '0.57 #'
        choice_b = choice(0.57)
        choice_c = choice(0.57)
        choice_d = choice(0.57)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the moment of inertia with respect to the y - axis if the area bounded in the first quadrant bounded by the parabola y^2 = 4x, the line x = 1 and the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_470_b():
    def __init__(self):
        
        choice_a = '1.07 #'
        choice_b = choice(1.07)
        choice_c = choice(1.07)
        choice_d = choice(1.07)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the moment of inertia with respect to the y - axis if the area bounded in the first quadrant bounded by the parabola y^2 = 4x, the line x = 1 and the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_471_a():
    def __init__(self):
        
        choice_a = '9.14 #'
        choice_b = choice(9.14)
        choice_c = choice(9.14)
        choice_d = choice(9.14)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the moment of inertia with respect to the x - axis of the area bounded in the first quadrant by the parabola x^2 = 8y, the line y = 2 and the x - axis"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_471_b():
    def __init__(self):
        
        choice_a = '17.07 #'
        choice_b = choice(17.07)
        choice_c = choice(17.07)
        choice_d = choice(17.07)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the moment of inertia with respect to the x - axis of the area bounded in the first quadrant by the parabola x^2 = 8y, the line y = 2 and the y - axis"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_472_b():
    def __init__(self):
        
        choice_a = '914e+6 #'
        choice_b = choice(914e6)
        choice_c = choice(914e6)
        choice_d = choice(914e6)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A parabola has an equation of y = x^2 / 200. Compute the moment of inertia of the area with respect to the x - axis"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_472_c():
    def __init__(self):
        
        choice_a = '146e+6 #'
        choice_b = choice(146e6)
        choice_c = choice(146e6)
        choice_d = choice(146e6)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A parabola has an equation of y = x^2 / 200. Compute the moment of inertia about the x - axis that passes through the centroid of the area."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_473_b():
    def __init__(self):
        
        choice_a = '3 #'
        choice_b = choice(3)
        choice_c = choice(3)
        choice_d = choice(3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The curve is expressed as x = 2 sqrt( 2y ). Find the centroid of this curve with the lines x = 4 and y = 0"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_473_c():
    def __init__(self):
        
        choice_a = '1.52 #'
        choice_b = choice(1.52)
        choice_c = choice(1.52)
        choice_d = choice(1.52)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The curve is expressed as x = 2 sqrt( 2y ) with the lines x = 4 and y = 0. Compute the moment of inertia of this curve with respect to the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_474_b():
    def __init__(self):
        
        choice_a = '0.30 #'
        choice_b = choice(0.30)
        choice_c = choice(0.30)
        choice_d = choice(0.30)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of x^2 = 16 y bounded with the lines x = 4 and the x - axis on the first quadrant. Compute the centroid of the area of this curve from the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_474_c():
    def __init__(self):
        
        choice_a = '2.51 cubic units #'
        choice_b = choice(2.51, 'cubic units')
        choice_c = choice(2.51, 'cubic units')
        choice_d = choice(2.51, 'cubic units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of x^2 = 16 y bounded with the lines x = 4 and the x - axis on the first quadrant. If we revolve this area with respect to the x - axis, what is the volume generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_475():
    def __init__(self):
        
        choice_a = '8256 # '
        choice_b = choice(8256)
        choice_c = choice(8256)
        choice_d = choice(8256)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the moment of inertia of the area enclosed by the curve x ^2 + y^2 - 36 = 0 with respect to the line y - 8 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_476():
    def __init__(self):
        
        choice_a = '1005 #'
        choice_b = choice(1005)
        choice_c = choice(1005)
        choice_d = choice(1005)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the moment of inertia of the area enclosed by the curve x^2 + y^2 - 16 = 0 with respect to the line y - 4 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_479():
    def __init__(self):
        
        choice_a = '2730.67e+3 #'
        choice_b = choice(2730.67e3)
        choice_c = choice(2730.67e3)
        choice_d = choice(2730.67e3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Given the equation of the curve y = 0.10 ( 1600 - x^2 ). Compute the moment of inertia with respect to y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_480_a():
    def __init__(self):
        
        choice_a = '0.60 #'
        choice_b = choice(0.60)
        choice_c = choice(0.60)
        choice_d = choice(0.60)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Compute the centroid of the curve bounded by the parabola x^2 = 8y and the line y = 0 and x = 4 with respect to the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_480_b():
    def __init__(self):
        
        choice_a = '1.52 #'
        choice_b = choice(1.52)
        choice_c = choice(1.52)
        choice_d = choice(1.52)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Compute the moment of inertia of the curve x^2 = 8y with respect to the line y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_481():
    def __init__(self):
        
        choice_a = '4935 #'
        choice_b = choice(4935)
        choice_c = choice(4935)
        choice_d = choice(4935)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Using the 2nd proposition of pappus, find the volume generated by revolving the area enclosed by the curve x^2 + y^2 = 25 about the line x - 10 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_482():
    def __init__(self):
        
        choice_a = '3948 #'
        choice_b = choice(3948)
        choice_c = choice(3948)
        choice_d = choice(3948)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving the area enclosed by the curve x^2 + y^2 = 25 about the line y - 8 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_483():
    def __init__(self):
        
        choice_a = '8527 #'
        choice_b = choice(8527)
        choice_c = choice(8527)
        choice_d = choice(8527)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the volume generated by rotating the area enclosed by the curve x^2 + y^2 = 36 about the line x + 12 = 0"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_484():
    def __init__(self):
        
        choice_a = '9949 #'
        choice_b = choice(9949)
        choice_c = choice(9949)
        choice_d = choice(9949)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the volume generated by rotating the area enclosed by the curve x^2 + y^2 = 36 about the line y + 14 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_485():
    def __init__(self):
        
        choice_a = '2960 #'
        choice_b = choice(2960)
        choice_c = choice(2960)
        choice_d = choice(2960)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The area enclosed by the curve x^2 + y^2 - 10 x = 0 is revolved about the line y = - 6. Find the the volume generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_486():
    def __init__(self):
        
        choice_a = '3454 #'
        choice_b = choice(3454)
        choice_c = choice(3454)
        choice_d = choice(3454)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The area enclosed by the curve x^2 + y^2 - 10x = 0 is rotated about the line x = -2. What volume is generated?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_487():
    def __init__(self):
        
        choice_a = '6.7 #'
        choice_b = choice(6.7)
        choice_c = choice(6.7)
        choice_d = choice(6.7)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line y - 1 = 0 the area bounded by the curve x^2 = 4y and the line y = 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_488():
    def __init__(self):
        
        choice_a = '268 #'
        choice_b = choice(268)
        choice_c = choice(268)
        choice_d = choice(268)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line x - 4 = 0 the area bounded by the curve x^2 = 8y and the line y - 2 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_489():
    def __init__(self):
        
        choice_a = '1234 #'
        choice_b = choice(1234)
        choice_c = choice(1234)
        choice_d = choice(1234)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line x - 5 = 0 the area in the first and second quadrants included by the curve x^2 + y^2 = 25 and the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_490():
    def __init__(self):
        
        choice_a = '45.4 #'
        choice_b = choice(45.4)
        choice_c = choice(45.4)
        choice_d = choice(45.4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line x - 2 = 0 the area in the first and fourth quadrants, bounded by the curve x^2 + y^2 - 4 = 0 and the line x = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_491():
    def __init__(self):
        
        choice_a = '380 #'
        choice_b = choice(380)
        choice_c = choice(380)
        choice_d = choice(380)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line x - 3 = 0 the area in the second and third quadrants bounded by the curve x^2 + y^2 - 9 = 0 and the line x = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_492():
    def __init__(self):
        
        choice_a = '76.8 #'
        choice_b = choice(76.8, round = 1)
        choice_c = choice(76.8, round = 1)
        choice_d = choice(76.8, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line x - 3 = 0 the area in the first quadrant bounded by the curve x^2 + y^2 - 9 = 0 and the line x = 0, y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_493():
    def __init__(self):
        
        choice_a = '1249 #'
        choice_b = choice(1249)
        choice_c = choice(1249)
        choice_d = choice(1249)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the line y + 8 = 0, the area in the first quadrant bounded by the curve x^2 + y^2 - 25 = 0 and the line x = 0 and y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_494():
    def __init__(self):
        
        choice_a = '8705 #'
        choice_b = choice(8705)
        choice_c = choice(8705)
        choice_d = choice(8705)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The closed curve x^2 + y^2 - 14 x - 14 y + 49 = 0 revolves about the line y = - 2. Determine the volume generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_495():
    def __init__(self):
        
        choice_a = '9762 #'
        choice_b = choice(9762)
        choice_c = choice(9762)
        choice_d = choice(9762)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The closed curve x^2 + y^2 - 14x - 14 y + 49 = 0 revolves about the line x = -3. Determine the volume generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_496():
    def __init__(self):
        
        choice_a = '0.55 #'
        choice_b = choice(0.55)
        choice_c = choice(0.55)
        choice_d = choice(0.55)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving the area enclosed by the line x - y = 0 and the curve y^2 - 2x = 0 about the line x - y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_497():
    def __init__(self):
        
        choice_a = '4.86 #'
        choice_b = choice(4.86)
        choice_c = choice(4.86)
        choice_d = choice(4.86)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving the area enclosed by the line x - y = 0 and the curve y^2 = 4x, about the line x - y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_498_a():
    def __init__(self):
        
        choice_a = '( 3.6, 4.5 ) #'
        choice_b = '( '+choice(3.6, round = 1)+', ' + choice(4.5, round = 1)+')'
        choice_c = '( '+choice(3.6, round = 1)+', ' + choice(4.5, round = 1)+')'
        choice_d = '( '+choice(3.6, round = 1)+', ' + choice(4.5, round = 1)+')'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of y^2 = 9x. Compute the centroid of the area bounded by the curve and the line x - y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_498_b():
    def __init__(self):
        
        choice_a = '53.95 #'
        choice_b = choice(53.95)
        choice_c = choice(53.95)
        choice_d = choice(53.95)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has the equation y^2 = 9x. Compute the volume generated if we revolve the area bounded by said curve and x - y = 0 about the line x - y = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_499():
    def __init__(self):
        
        choice_a = '52.4 #'
        choice_b = choice(52.4, round = 1)
        choice_c = choice(52.4, round = 1)
        choice_d = choice(52.4, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the volume formed by revolving about the x - axis the area bounded by the x - axis, the lines x = 1, x = 3, and the curve xy = 5."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_499_a():
    def __init__(self):
        
        choice_a = '2.09 #'
        choice_b = choice(2.09)
        choice_c = choice(2.09)
        choice_d = choice(2.09)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A hyperbola has an equation of  xy = 1. Find the volume generated by revolving about the x - axis the area bounded by the hyperbola, the x - axis, and the abcissa x = 1 and x = 3."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_499_b():
    def __init__(self):
        
        choice_a = '58.64 cu. units #'
        choice_b = choice(58.64, 'cu. units')
        choice_c = choice(58.64, 'cu. units')
        choice_d = choice(58.64, 'cu. units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of yx^2 = 8. Determine the volume generated if we revolve this area about the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_499_b_2():
    def __init__(self):
        
        choice_a = '2.33 #'
        choice_b = choice(2.33)
        choice_c = choice(2.33)
        choice_d = choice(2.33)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of yx^2 = 8. Determine the centroid of this area with respect to the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_500():
    def __init__(self):
        
        choice_a = '160.8 #'
        choice_b = choice(160.8)
        choice_c = choice(160.8)
        choice_d = choice(160.8)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the volume generated formed by revolving about the x - axis the area bounded by the lines x = 1, x = 5 and the x - axis and the curve xy = 8?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_501():
    def __init__(self):
        
        choice_a = '2.45 #'
        choice_b = choice(2.45)
        choice_c = choice(2.45)
        choice_d = choice(2.45)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the x - axis the area bounded by the curve y = sin(x) and the x - axis, from x = 0 to x = pi / 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_502_b():
    def __init__(self):
        
        choice_a = '53.36 #'
        choice_b = choice(53.36)
        choice_c = choice(53.36)
        choice_d = choice(53.36)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by revolving about the x - axis the area bounded by the curve xy = 5, and the lines  x = 3, x = 1 and the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_502_c():
    def __init__(self):
        
        choice_a = '1.55 units #'
        choice_b = choice(1.55, 'units')
        choice_c = choice(1.55, 'units')
        choice_d = choice(1.55, 'units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Compute the distance of the centroid of the area bounded by the x - axis, the lines x = 1, x = 3, and the curve xy = 5 from the x - axis"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_503_a():
    def __init__(self):
        
        choice_a = '1.70 #'
        choice_b = choice(1.70)
        choice_c = choice(1.70)
        choice_d = choice(1.70)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has the equation 9x^2 + 16y^2 = 144. What is the distance from the centroid of the first quadrant from the y-axis?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_503_b():
    def __init__(self):
        
        choice_a = '5.55 units #'
        choice_b = choice(5.55, 'units')
        choice_c = choice(5.55, 'units')
        choice_d = choice(5.55, 'units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has the equation 9x^2 + 16y^2 = 144. Determine the length of the curve on the first quadrant of the curve."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_503_c():
    def __init__(self):
        
        choice_a = '100.67 cu. units #'
        choice_b = choice(100.67, 'cu. units')
        choice_c = choice(100.67, 'cu. units')
        choice_d = choice(100.67, 'cu. units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has the equation 9x^2 + 16y^2 = 144. If the area enclosed by the curve on the first quadrant is revolved about the y - axis, what is the volume generated?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_504_a():
    def __init__(self):
        
        choice_a = '135.21 #'
        choice_b = choice(135.21)
        choice_c = choice(135.21)
        choice_d = choice(135.21)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A circle has an equation x^2 + y^2 = 4. If the area on the first quadrant is revolved about the line x + 6 = 0, find the volume of the solid generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_504_b():
    def __init__(self):
        
        choice_a = '1.27 #'
        choice_b = choice(1.27)
        choice_c = choice(1.27)
        choice_d = choice(1.27)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A circle has an equation x^2 + y^2 = 4. Locate the centroid of the first quadrant arc of the circle from the x - axis."""   
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_504_c():
    def __init__(self):
        
        choice_a = '25.07 #'
        choice_b = choice(25.07)
        choice_c = choice(25.07)
        choice_d = choice(25.07)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A circle has an equation x^2 + y^2 = 4. Find the surface area generated by revolving the first quadrant arc of the circle about the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_505_a():
    def __init__(self):
        
        choice_a = '968.21 #'
        choice_b = choice(968.21)
        choice_c = choice(968.21)
        choice_d = choice(968.21)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A circle having a radius of 6 units has its center at the origin. If the area on the 2nd quadrant of the curve is revolved about the line y = 8, determine the volume of the solid generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_505_b():
    def __init__(self):
        
        choice_a = '8256.11 #'
        choice_b = choice(8256.11)
        choice_c = choice(8256.11)
        choice_d = choice(8256.11)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A circle having a radius of 6 units has its center at the origin. What is the moment of inertial of the circle with respect to the line y = 8?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_506_a():
    def __init__(self):
        
        choice_a = '9.88 #'
        choice_b = choice(9.88)
        choice_c = choice(9.88)
        choice_d = choice(9.88)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""An ellipse has an equation equal to x^2/25 + y^2/16 = 1. Compute the distance of the centroid of area on the 2nd quadrant of the curve from the line x + 12 = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_506_b():
    def __init__(self):
        
        choice_a = '167.81 #'
        choice_b = choice(167.81)
        choice_c = choice(167.81)
        choice_d = choice(167.81)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""An ellipse has an equation equal to x^2/25 + y^2/16 = 1. If this area is revolved about the x - axis, what is the volume generated?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_506_c():
    def __init__(self):
        
        choice_a = '28.45 #'
        choice_b = choice(28.45)
        choice_c = choice(28.45)
        choice_d = choice(28.45)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""An ellipse has an equation equal to x^2/25 + y^2/16 = 0. Compute the total length of the curve."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_507():
    def __init__(self):
        
        choice_a = '83.8 #'
        choice_b = choice(83.8, round = 1)
        choice_c = choice(83.8, round = 1)
        choice_d = choice(83.8, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the volume generated by revolving the area in the first and second quadrants bounded by the ellipse 4x^2 + 25y^2 = 100 and the x - axis about the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_508():
    def __init__(self):
        
        choice_a = '628.3 #'
        choice_b = choice(628.3, round =  1)
        choice_c = choice(628.3, round =  1)
        choice_d = choice(628.3, round =  1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the volume generated by rotating the area in the third and fourth quadrants bounded by the curve 25x^2 + 36y^2 = 900 and the x - axis, about the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_509():
    def __init__(self):
        
        choice_a = '37.6 #'
        choice_b = choice(37.6, round = 1)
        choice_c = choice(37.6, round = 1)
        choice_d = choice(37.6, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the volume generated by the area bounded by the ellipse 4x^2 + 9y^2 = 36 in the first quadrant if revolved about the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_510():
    def __init__(self):
        
        choice_a = '226 #'
        choice_b = choice(226)
        choice_c = choice(226)
        choice_d = choice(226)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The area bounded by the first quadrant of the ellipse 9x^2 + 36y^2 = 324 is revolved about the y - axis. Find the volume generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_511_b():
    def __init__(self):
        
        choice_a = '1.5 #'
        choice_b = choice(1.5, round = 1)
        choice_c = choice(1.5, round = 1)
        choice_d = choice(1.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A given curve has an equation of y = 3x^2. Locate the centroid of the curve from the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_511_c():
    def __init__(self):
        
        choice_a = '75.4 cu. units #'
        choice_b = choice(75.4, 'cu. units')
        choice_c = choice(75.4, 'cu. units')
        choice_d = choice(75.4, 'cu. units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A given curve has an equation of y = 3x^2. What volume is generated if the curve is revolved about the y-axis?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_512_b():
    def __init__(self):
        
        choice_a = str(round(math.pi / 8, 4)) + ' #'
        choice_b = choice(math.pi/8, round = 4)
        choice_c = choice(math.pi/8, round = 4)
        choice_d = choice(math.pi/8, round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of y = sin(x). Determine the centroid of area bounded by the curve y = sin(x) from x = 0 to x = pi from the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_512_c():
    def __init__(self):
        
        choice_a = '4.935 #'
        choice_b = choice(4.935, round = 3)
        choice_c = choice(4.935, round = 3)
        choice_d = choice(4.935, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A curve has an equation of y = sin(x). If the area bounded by the curve y = sin(x) from x = 0 to x = pi is revolved about the x - axis, determine the volume generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_513_b():
    def __init__(self):
        
        choice_a = str(round((math.pi - 2)/2, 4)) + ' #'
        choice_b = choice((math.pi - 2)/2, round = 4)
        choice_c = choice((math.pi - 2)/2, round = 4)
        choice_d = choice((math.pi - 2)/2, round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The curve has an equation of y = cos(x). Find the centroid of the area on the first quadrant bounded by the curve and the two axes with respect to the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_513_c():
    def __init__(self):
        
        choice_a = str(round(math.pi * (math.pi - 2), 4)) + ' #'
        choice_b = choice(math.pi * (math.pi - 2), round = 4)
        choice_c = choice(math.pi * (math.pi - 2), round = 4)
        choice_d = choice(math.pi * (math.pi - 2), round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The curve has an equation of y = cos(x). Find the volume formed by the area on the first quadrant bounded by the curve and the two axes with respect to the y - axis about the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_514_b():
    def __init__(self):
        
        choice_a = '0.582 #'
        choice_b = choice(0.582, round = 3)
        choice_c = choice(0.582, round = 3)
        choice_d = choice(0.582, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The curve has an equation y = e^x. Compute the centroid of the area from the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_514_c():
    def __init__(self):
        
        choice_a = '4.512 #'
        choice_b = choice(4.512, round = 3)
        choice_c = choice(4.512, round = 3)
        choice_d = choice(4.512, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The curve has an equation y = e^x. Compute the volume generated by the area if revolved about the line x = 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_515_b():
    def __init__(self):
        
        choice_a = '3 #'
        choice_b = random.randint(1,10)
        choice_c = random.randint(1,10)
        choice_d = random.randint(1,10)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Given a curve having an equation of y^2 = 4x. How far is the centroid of the curve bounded by the line  y = 4 and x = 0 from the x - axis?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_515_c():
    def __init__(self):
        
        choice_a = '100.5 #'
        choice_b = choice(100.5, round = 1)
        choice_c = choice(100.5, round = 1)
        choice_d = choice(100.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Given a curve having an equation of y^2 = 4x, compute the volume generated by the area if revolved about the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_515_A_b():
    def __init__(self):
        
        choice_a = '153.94 cm^2 #'
        choice_b = choice(153.94, 'cm^2')
        choice_c = choice(153.94, 'cm^2')
        choice_d = choice(153.94, 'cm^2')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A headlight is frequently designed so that the cross section through its axis is a parabola, having the light center as focus. If the light center is 2.25 cm from the vertex and the diameter of the headlight is 12 cm, compute the surface area of the headlight."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_515_A_c():
    def __init__(self):
        
        choice_a = '226.19 #'
        choice_b = choice(226.19)
        choice_c = choice(226.19)
        choice_d = choice(226.19)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A headlight is frequently designed so that the cross section through its axis is a parabola, having the light center as focus. If the light center is 2.25 cm from the vertex and the diameter of the headlight is 12 cm, compute the volume of the solid formed by the headlight."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_516_b():
    def __init__(self):
        
        choice_a = '1.84 #'
        choice_b = choice(1.84)
        choice_c = choice(1.84)
        choice_d = choice(1.84)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A parabola has an equation of y^2 = 16 x. Compute the distance of the centroid of this area from the y - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_516_c():
    def __init__(self):
        
        choice_a = '268.02 cu. units #'
        choice_b = choice(268.02, 'cu. units')
        choice_c = choice(268.02, 'cu. units')
        choice_d = choice(268.02, 'cu. units')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A parabola has an equation of y^2 = 16 x. If the area between the curve and the line is revolved about the x - axis, compute the volume of the solid generated."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_517_b():
    def __init__(self):
        
        choice_a = '1.80 #'
        choice_b = choice(1.80)
        choice_c = choice(1.80)
        choice_d = choice(1.80)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Two curves having an equation of x^2 = 4y and y^2 = 4x intersect each other. Compute the centroid of the area between the two curves from the line x = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_517_c():
    def __init__(self):
        
        choice_a = '60.28 #'
        choice_b = choice(60.28)
        choice_c = choice(60.28)
        choice_d = choice(60.28)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Two curves having an equation of x^2 = 4y and y^2 = 4x intersect each other. Compute the volume of the solid generated if we revolve the area between the two curves with respect to the line x = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_611():
    def __init__(self):
        
        choice_a = str(round(32 * 9.81, 4)) + ' #'
        choice_b = choice(32 * 9.81, round = 4)
        choice_c = choice(32 * 9.81, round = 4)
        choice_d = choice(32 * 9.81, round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A rectangular plate is 4 m long and 2 m wide. It is submerged vertically in water with the upper 4 m edge parallel to and 3 m below the surface. Find the magnitude of the resultant force against one side of the plate."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_612():
    def __init__(self):
        
        choice_a = '58.86 kN #'
        choice_b = choice(58.86)
        choice_c = choice(58.86)
        choice_d = choice(58.86)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the force on one face of right triangle of sides 4 m and altitude of 3 m. The altitude is submerged vertically with the 4 m side in the surface."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_613():
    def __init__(self):
        
        choice_a = '150.093 kN #'
        choice_b = choice(150.093, round = 3)
        choice_c = choice(150.093, round = 3)
        choice_d = choice(150.093, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A horizontal cylindrical boiler 6 m. In diameter is half full of oil having sp.gr. of 0.80. Find the force on one end."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_614():
    def __init__(self):
        
        choice_a = '502.2 kN #'
        choice_b = choice(502.2, 'kN', round = 1)
        choice_c = choice(502.2, 'kN', round = 1)
        choice_d = choice(502.2, 'kN', round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A plate in the form of a parabolic segment of base 12 m and height 4 m  is submerged in water so that base is in the surface of the liquid. Find the force on a face of the plate."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_615():
    def __init__(self):
        
        choice_a = '4931 kN #'
        choice_b = choice(4931, 'kN')
        choice_c = choice(4931, 'kN')
        choice_d = choice(4931, 'kN')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A circular water main 4 meters in diameter is closed by a bulkhead whose center is 40 meters below the surface of the water in the reservoir. Find the force on the bulkhead."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_616():
    def __init__(self):
        
        choice_a = '993.26 kN #'
        choice_b = choice(993.26, 'kN')
        choice_c = choice(993.26, 'kN')
        choice_d = choice(993.26, 'kN')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A plate in the form of a parabolic segment is 12 m. in height and 4 m deep and is partly submerged in water so that its axis is parallel to end 3m below the water surface. Find the force acting on the plate."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_617():
    def __init__(self):
        
        choice_a = '7.68 J #'
        choice_b = choice(7.68, 'J')
        choice_c = choice(7.68, 'J')
        choice_d = choice(7.68, 'J')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A spring with a natural length of 10 cm is stretched by 0.5 cm by a 12 N force. Find the work done is stretching the spring from 10 cm to 18 cm."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_618():
    def __init__(self):
        
        choice_a = '6.28 J #'
        choice_b = choice(6.28, 'J')
        choice_c = choice(6.28, 'J')
        choice_d = choice(6.28, 'J')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""According to Hooke's law, the force required to stretch a helical spring is proportional to the distance stretched. The natural length of a given spring is 8 cm. A force of 4 kgf will stretch it to a total length of 10 cm. Find the work done in stretching it from its natural length to a total length of 16 cm."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_619():
    def __init__(self):
        
        choice_a = '160 ft lb #'
        choice_b = choice(160, 'ft lb')
        choice_c = choice(160, 'ft lb')
        choice_d = choice(160, 'ft lb')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A 5 lb monkey is attached to a 20 ft hanging rope that weighs 0.3 lb/ft. The monkey climbs the rope up to the top. How much work has it done?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""




