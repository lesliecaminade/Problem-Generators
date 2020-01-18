from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import algebra_engine as ae
import cmath

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

SIDE_MIN = 5
SIDE_MAX = 30
ANGLE_MIN_TRIANGLE = 10
ANGLE_MAX_TRIANGLE = 150
WRONG_CHOICES = 3
AIRSPEED_MIN = 500
AIRSPEED_MAX = 1000
WINSPEED_MIN = 10
WINSPEED_MAX = 50
BUILDING_HEIGHT_MIN = 50
BUILDING_HEIGHT_MAX = 200
ANGLE_ELEVATION_MIN = 10
ANGLE_ELEVATION_MAX = 80
SHADOW_LENGTH_MIN = 4
SHADOW_LENGTH_MAX = 10

IDENTITIES_RECIPROCAL = [
'sin(x) = 1/csc(x)',
'csc(x) = 1/sin(x)',
'cos(x) = 1/sec(x)',
'sec(x) = 1/cos(x)'
]

IDENTITIES_QUOTIENT = [
'tan(x) = sin(x)/cos(x)',
'cot(x) = cos(x)/sin(x)'
]

IDENTITIES_PYTHAGOREAN = [
'sin^2(x) + cos^2(x) = 1',
'sec^2(x) = 1 + tan^2(x)',
'csc^2(x) = 1 + cot^2(x)'
]

IDENTITIES_SUM_OF_ANGLES = [
'sin(a + b) = sin(a) cos(b) + cos(a) sin(b)',
'cos(a + b) = cos(a) cos(b) - sin(a) sin(b)',
'tan(a + b) = [tan(a) + tan(b)] / [1 - tan(a) tan(b) ]'
]

IDENTITIES_DOUBLE = [
'sin(2x) = 2sin(x)cos(x)',
'cos(2x) = cos^2(x) - sin^2(x)',
'cos(2x) = 2cos^2(x) - 1',
'cos(2x) = 1 - 2sin^2(x)',
'tan(2x) = 2tan(x) / [ 1 - tan^2(x) ]'
]

IDENTITIES_HALF = [
'sin^2(x/2) = [1 - cos(x)]/2',
'cos^2(x/2) = [1 + cos(x)]/2',
'tan^2(x/2) = [1 - cos(x)]/[1 + cos(x)]'
]

IDENTITY_TYPES = [
'reciprocal identities',
'quotient identities',
'pythagorean identities',
'sum of angles identities',
'double angle identities',
'half angle identities'
]


DIRECTIONS = ['n_e', 'e_s', 's_w', 'w_n', 'e_n', 's_e', 'w_s', 'n_w', 'eofn', 'nofe', 'sofe', 'eofs', 'wofs', 'sofw', 'nofw', 'wofn']
DIRECTIONS_SET_1 = ['n_e', 'e_s', 's_w', 'w_n', 'e_n', 's_e', 'w_s', 'n_w']
DIRECTIONS_SET_2 = ['eofn', 'nofe', 'sofe', 'eofs', 'wofs', 'sofw', 'nofw', 'wofn']
def angle_news(angle, direction):
    
    direction.lower()

    if direction == 'n_w' or direction == 'wofn':
        if 0 <= angle.degrees < 90:
            new_angle = c.angle(angle.degrees + 270, 'degrees')
        else:
            new_angle = c.angle(angle.degrees - 90, 'degrees')

    elif direction == 'w_s' or direction == 'sofw':
        if 0 <= angle.degrees < 180:
            new_angle = c.angle(angle.degrees + 180, 'degrees')
        else:
            new_angle = c.angle(angle.degrees - 180, 'degrees')

    elif direction == 's_e' or direction == 'eofs':
        if 0 <= angle.degrees < 270:
            new_angle = c.angle(angle.degrees + 90, 'degrees')
        else:
            new_angle = c.angle(angle.degrees - 270, 'degrees')

    elif direction == 'e_n' or direction == 'nofe':
        new_angle = angle

    elif direction == 'n_e' or direction == 'eofn':
        if 0 <= angle.degrees <= 90:
            new_angle = c.angle(90 - angle.degrees, 'degrees')
        else:
            new_angle = c.angle(450 - angle.degrees, 'degrees')

    elif direction == 'e_s' or direction == 'sofe':
        if angle.degrees == 0:
            new_angle = c.angle(0, 'degrees')
        else:
            new_angle = c.angle(360 - angle.degrees, 'degrees')

    elif direction == 's_w' or direction == 'wofs':
        if 0 <= angle.degrees <= 270:
            new_angle = c.angle(270 - angle.degrees, 'degrees')
        else:
            new_angle = c.angle(630 - angle.degrees, 'degrees')

    elif direction == 'w_n' or direction == 'nofw':
        if 0 <= angle.degrees <= 180:
            new_angle = c.angle(180 - angle.degrees, 'degrees')
        else:
            new_angle = c.angle(540 - angle.degrees, 'degrees')

    else:
        print('error angle_news converter')

    return [new_angle, direction]

def angle_news_string(angle_and_direction_list):

    angle = angle_and_direction_list[0]
    direction = angle_and_direction_list[1]
    if direction == 'n_e':
        return f"""N {round(angle.degrees, 2)}deg E"""
    elif direction == 'e_n':
        return f"""E {round(angle.degrees, 2)}deg N"""
    elif direction == 's_e':
        return f"""S {round(angle.degrees, 2)}deg E"""
    elif direction == 'e_s':
        return f"""E {round(angle.degrees, 2)}deg S"""
    elif direction == 's_w':
        return f"""S {round(angle.degrees, 2)}deg W"""
    elif direction == 'w_s':
        return f"""W {round(angle.degrees, 2)}deg S"""
    elif direction == 'n_w':
        return f"""N {round(angle.degrees, 2)}deg W"""
    elif direction == 'w_n':
        return f"""W {round(angle.degrees, 2)}deg N"""
    elif direction == 'nofe':
        return f"""{round(angle.degrees, 2)}deg N of E"""
    elif direction == 'eofn':
        return f"""{round(angle.degrees, 2)}deg E of N"""
    elif direction == 'eofs':
        return f"""{round(angle.degrees, 2)}deg E of S"""
    elif direction == 'sofe':
        return f"""{round(angle.degrees, 2)}deg S of E"""
    elif direction == 'sofw':
        return f"""{round(angle.degrees, 2)}deg S of W"""
    elif direction == 'wofs':
        return f"""{round(angle.degrees, 2)}deg W of S"""
    elif direction == 'wofn':
        return f"""{round(angle.degrees, 2)}deg W of N"""
    elif direction == 'nofw':
        return f"""{round(angle.degrees, 2)}deg N of W"""
    else:
        print('error angle_news_string')








class Identity():
    def __init__(self):
        identity_type = random.choice(IDENTITY_TYPES)

        if identity_type == IDENTITY_TYPES[0]:
            correct = random.choice(IDENTITIES_RECIPROCAL)
            wrong_list = IDENTITIES_QUOTIENT + IDENTITIES_PYTHAGOREAN + IDENTITIES_SUM_OF_ANGLES + IDENTITIES_DOUBLE + IDENTITIES_HALF
        elif identity_type == IDENTITY_TYPES[1]:
            correct = random.choice(IDENTITIES_QUOTIENT)
            wrong_list = IDENTITIES_PYTHAGOREAN + IDENTITIES_SUM_OF_ANGLES + IDENTITIES_DOUBLE + IDENTITIES_HALF + IDENTITIES_RECIPROCAL
        elif identity_type == IDENTITY_TYPES[2]:
            correct = random.choice(IDENTITIES_PYTHAGOREAN)
            wrong_list = IDENTITIES_QUOTIENT + IDENTITIES_SUM_OF_ANGLES + IDENTITIES_DOUBLE + IDENTITIES_HALF + IDENTITIES_RECIPROCAL
        elif identity_type == IDENTITY_TYPES[3]:
            correct = random.choice(IDENTITIES_SUM_OF_ANGLES)
            wrong_list = IDENTITIES_QUOTIENT + IDENTITIES_PYTHAGOREAN + IDENTITIES_DOUBLE + IDENTITIES_HALF + IDENTITIES_RECIPROCAL
        elif identity_type == IDENTITY_TYPES[4]:
            correct = random.choice(IDENTITIES_DOUBLE)
            wrong_list = IDENTITIES_QUOTIENT + IDENTITIES_PYTHAGOREAN + IDENTITIES_SUM_OF_ANGLES + IDENTITIES_HALF + IDENTITIES_RECIPROCAL
        elif identity_type == IDENTITY_TYPES[5]:
            correct = random.choice(IDENTITIES_HALF)
            wrong_list = IDENTITIES_QUOTIENT + IDENTITIES_PYTHAGOREAN + IDENTITIES_SUM_OF_ANGLES + IDENTITIES_DOUBLE + IDENTITIES_RECIPROCAL
        else:
            print('ERROR: identity not found')


        self.type = identity_type
        self.correct = correct
        wrong_list = random.sample(wrong_list,WRONG_CHOICES)
        self.wrong_list = wrong_list

def herons(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt((s - a)* (s - b)*(s - c) * s)
    return area

class Triangle():
    def __init__(self):
        pass

    def init_define_ASA(self, A, b, C):
        self.A = c.angle(A, 'degrees')
        self.b = b
        self.C = c.angle(C, 'degrees')

        self.B = c.angle(180 - A - C, 'degrees')

        self.a = b * math.sin(self.A.radians) / math.sin(self.B.radians)
        self.c = b * math.sin(self.C.radians) / math.sin(self.B.radians)
        self.area = (1/2) * self.a * self.b * math.sin(self.C.radians)

    def init_random(self):

        self.a = random.randint(SIDE_MIN, SIDE_MAX)
        self.b = random.randint(SIDE_MIN, SIDE_MAX)
        self.C = c.angle(random.randint(ANGLE_MIN_TRIANGLE, ANGLE_MAX_TRIANGLE), 'degrees')

        

        self.c = math.sqrt( self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(self.C.radians))

        #refine the sides so that they become integers
        self.c = int(self.c)

        #resolve the angle
        self.C = c.angle(math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)), 'radians')

        self.A = c.angle(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)), 'radians')

        self.B = c.angle(math.pi - self.A.radians - self.C.radians)


        self.area = (1/2) * self.a * self.b * math.sin(self.C.radians)
        self.perimeter = self.a + self.b + self.c
        self.semiperimeter = self.perimeter / 2

    def given(self, given, units = ''):
        given.lower()

        if given == 'sss':
            return f"""a = {self.a} {units}, b = {self.b} {units}, and c = {self.c} {units}"""
        elif given == 'sas':
            return f"""a = {self.a} {units}, b = {self.b} {units}, and C = {round(self.C.degrees, 2)} degrees"""
        elif given == 'asa':
            return f"""A = {round(self.A.degrees, 2)} degrees, c = {self.c}, and B = {round(self.B.degrees, 2)} degrees"""
        else:
            print('given()_ERROR')  

    def median(self, side):
        side.lower()

        a = self.a
        b = self.b
        c = self.c

        if side == 'a':
            return (1/2) * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
        elif side == 'b':
            return (1/2) * math.sqrt(2 * c**2 + 2 * a**2 - b**2)
        elif side == 'c':
            return (1/2) * math.sqrt(2 * a**2 + 2 * b**2 - c**2)
        else:
            print('median_error')

    def angular_bisector(self, side):
        side.lower()

        a = self.a
        b = self.b
        c = self.c
        s = self.semiperimeter

        if side == 'a':
            return (2 / (b + c)) * math.sqrt(b * c * s * (s - a))
        elif side == 'b':
            return (2 / (a + c)) * math.sqrt(a * c * s * (s - b))
        elif side == 'c':
            return (2 / (a + b)) * math.sqrt(a * b * s * (s - c))
        else:
            print('angular_bisector error')

    def altitude(self, side):
        side.lower()

        a = self.a
        b = self.b
        c = self.c
        area = self.area

        if side == 'a':
            base = a
        elif side == 'b':
            base = b
        elif side == 'c':
            base = c
        else:
            print('altitude_error')

        return 2 * area / base

    def inradius(self):

        return self.area / self.semiperimeter

    def circumradius(self):

        return self.a * self.b * self.c / (4 * self.area)

    def exradius(self, side):

        side.lower()

        if side == 'a':
            side_length = self.a
        elif side == 'b':
            side_length = self.b
        elif side == 'c':
            side_length = self.c
        elif side == 'smallest':
            side_length = min(self.a, self.b, self.c)
        elif side == 'largest':
            sides_length = max(self.a, self.b, self.c)
        else:
            print('exradius_error')

        return self.area / (self.semiperimeter - side_length)

class Vehicle():
    def __init__(self):

        air_speed = random.randint(AIRSPEED_MIN, AIRSPEED_MAX)
        air_angle = c.angle(random.randint(1,35) * 10, 'degrees')
        wind_speed = random.randint(WINSPEED_MIN, WINSPEED_MAX)
        wind_angle = c.angle(random.randint(1,35) * 10, 'degrees')

        air_velocity = cmath.rect(air_speed, air_angle.radians)
        wind_velocity = cmath.rect(wind_speed, wind_angle.radians)

        ground_velocity = air_velocity + wind_velocity

        print(air_velocity)
        print(wind_velocity)
        print(ground_velocity)

        ground_angle = cmath.phase(ground_velocity)
        ground_speed = abs(ground_velocity)

        if ground_angle < 0:
            ground_angle = ground_angle + math.pi * 2

        ground_angle = c.angle(ground_angle, 'radians')


        self.air_speed = air_speed
        self.air_angle = air_angle
        self.wind_speed = wind_speed
        self.wind_angle = wind_angle
        self.ground_speed = round(ground_speed, 2)
        self.ground_angle = ground_angle

        self.air_string = angle_news_string(angle_news(self.air_angle, random.choice(DIRECTIONS)))
        self.wind_string = angle_news_string(angle_news(self.wind_angle, random.choice(DIRECTIONS)))
        self.ground_string = angle_news_string(angle_news(self.ground_angle, random.choice(DIRECTIONS)))

class Person_Building():
    def __init__(self):

        building_height = random.randint(BUILDING_HEIGHT_MIN, BUILDING_HEIGHT_MAX)
        angle_elevation = c.angle(random.randint(ANGLE_ELEVATION_MIN, ANGLE_ELEVATION_MAX), 'degrees')
        distance_from_building = building_height / math.tan(angle_elevation.radians)

        self.building_height = building_height
        self.angle_elevation = angle_elevation
        self.distance_from_building = round(distance_from_building, 2)

class Two_Persons_Building():
    def __init__(self):

        building_height = random.randint(BUILDING_HEIGHT_MIN, BUILDING_HEIGHT_MAX)
        angle_elevation = c.angle(random.randint(ANGLE_ELEVATION_MIN, ANGLE_ELEVATION_MAX), 'degrees')
        angle_elevation_2 = c.angle(random.randint(ANGLE_ELEVATION_MIN, int(angle_elevation.degrees) - 1), 'degrees')

        distance_between_persons = building_height /  math.tan(angle_elevation_2.radians) - building_height/ math.tan(angle_elevation.radians)

        self.building_height = building_height
        self.angle_elevation = angle_elevation
        self.angle_elevation_2 = angle_elevation_2
        self.distance_between_persons = round(distance_between_persons, 2)







        




























































