from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import trigonometry_engine as te
from num2words import num2words
from mathsub import algebra_engine as ae

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

GIVEN_TYPES_TRIANGLE = ['sss', 'sas', 'asa']


class median():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, determine the length of the smallest median."""
        self.answer = f"""{round(min(t.median('a'), t.median('b'), t.median('c')), 2)} units"""


class angular_bisector():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, determine the length of the smallest angular bisector."""
        self.answer = f"""{round(min(t.angular_bisector('a'), t.angular_bisector('b'), t.angular_bisector('c')), 2)}"""


class altitude():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, determine the length of the smallest altitude."""
        self.answer = f"""{round(min(t.altitude('a'), t.altitude('b'), t.altitude('c')), 2)}"""




class inradius_SSS():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions a = {t.a}, b = {t.b}, and c = {t.c}, determine the radius of the circle than can be inscribed in the given triangle."""

        self.answer = f"""Radius of the inscribed circle: {round(t.inradius(),2)}""" 

class inradius_SAS():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions a = {t.a}, b = {t.b}, and C = {round(t.C.degrees, 2)} degrees, determine the radius of the circle that can be inscribed in the given triangle."""

        self.answer = f"""Radius of the inscribed circle: {round(t.inradius(), 2)}"""

class inradius_ASA():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given('asa')}, determine the radius of the circle that can be inscribed in the given triangle."""

        self.answer = f"""Radius of the inscribed circle: {round(t.inradius(), 2)}"""

class inradius():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, determine the radius of the circle that can be inscribed in the given triangle."""
        self.answer = f"""Radius of the inscribed circle: {round(t.inradius(), 2)}"""

class circumradius():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, determine the radius of the circle that circumscribes the given triangle."""

        self.answer = f"""Radius of the circumscribing circle: {round(t.circumradius(), 2)}"""

class exradius():
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, determine the radius of the smallest excircle of the given triangle."""
        self.answer = f"""{round(min(t.exradius('a'), t.exradius('b'), t.exradius('c')))}"""

class identity:
    def __init__(self):

        i = te.Identity()

        choice_a = i.correct + '*'
        choice_b = i.wrong_list[0]
        choice_c = i.wrong_list[1]
        choice_d = i.wrong_list[2]

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Which of the following shows one of the trigonometric {i.type}?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class area:
    def __init__(self):
        t = te.Triangle()
        t.init_random()

        self.question = f"""Given a triangle with dimensions {t.given(random.choice(GIVEN_TYPES_TRIANGLE))}, calculate the area of the given triangle."""
        self.answer = f"""{round(t.area, 2)} units^2"""

class airplane:
    def __init__(self):
        problem = te.Vehicle()

        questions = [f"""An airplane has velocity of {problem.air_speed} km/h {problem.air_string} in calm air. That same airplane now attempts to go in the said direction in the presence of wind that has a velocity of {problem.wind_speed} km/h {problem.wind_string}. Determine the resulting speed of the airplane.""",
        f"""An airplane wants to travel in the direction of {problem.ground_string} with a speed of {problem.ground_speed} km/h in the presence of a wind with a speed of {problem.wind_speed} km/h that is blowing to the direction of {problem.wind_string}. Determine the required airspeed the airplane should have."""]
        answers = [f"""{problem.ground_speed} km/h, {problem.ground_string}""", 
        f"""{problem.air_speed} km/h, {problem.air_string}"""]

        number = random.randint(0, len(questions)- 1)

        self.question = questions[number]
        self.answer = answers[number]

class elevation_person_building():
    def __init__(self):
        p = te.Person_Building()

        self.question = f"""A person standing {p.distance_from_building} m from a building looks at the top of the building at notices that the angle of elevation he has to look up is {p.angle_elevation.degrees} degrees. Determine the height of the building. Disregard the person's height."""

        self.answer = f"""{p.building_height} m"""

class elevation_two_person_building():
    def __init__(self):
        p = te.Two_Persons_Building()

        self.question = f"""Two persons are standing at the same side of a certain building and observe that the angle of elevation they observe when they both look at the top of the building are {p.angle_elevation_2.degrees} degrees and {p.angle_elevation.degrees} degrees respectively. If they are {round(p.distance_between_persons, 2)} m away from each other, determine the height of the building. Disregard the persons' height."""
        self.answer = f"""{p.building_height} m"""

class inclined_post():
    def __init__(self):
        t = te.Triangle()

        tryagain = True
        while tryagain:
            pole_inclination = c.angle(random.randint(5, 20), 'degrees')
            angle_elevation = c.angle(random.randint(te.ANGLE_ELEVATION_MIN, te.ANGLE_ELEVATION_MAX), 'degrees')
            shadow_length = random.randint(te.SHADOW_LENGTH_MIN, te.SHADOW_LENGTH_MAX)

            if angle_elevation.degrees + pole_inclination.degrees + 90 < 180:
                tryagain = False

        t.init_define_ASA(angle_elevation.degrees, shadow_length, pole_inclination.degrees + 90)

        self.question = f"""A pole casts a shadow {shadow_length} m long when the angle of elevation of the sun is {angle_elevation.degrees} degrees. The pole is inclined {pole_inclination.degrees} degrees with the vertical directly towards the sun. Determine the length of the pole."""

        self.answer = f"""Length of the pole: {round(t.a, 2)} m"""





        
















 































































