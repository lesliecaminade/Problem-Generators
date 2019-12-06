import sympy
import math
import random
from generator import constants_conversions as c

x, y, z, t = sympy.symbols('x y z t', real = True)#generic variables

X_RANGE = 10
Y_RANGE = 10
EXTEND_FACTOR_MIN = 2
EXTEND_FACTOR_MAX = 5

FRAC_MIN = 1
FRAC_MAX = 9
FRAC_VALUE_MIN = 0
FRAC_VALUE_MAX = 1

SLOPE_MAX = 5

RADIUS_MIN = 1
RADIUS_MAX = 5

ELLIPSE_MINOR_AXIS_MIN = 1
ELLIPSE_MINOR_AXIS_MAX = 5
ELLIPSE_MAJOR_AXIS_MAX = 5

HYPERBOLA_FOCAL_LENGTH_MIN = 1
HYPERBOLA_FOCAL_LENGTH_MAX = 4
HYPERBOLA_CONJUGATE_AXIS_MIN = 2
HYPERBOLA_CONJUGATE_AXIS_MAX = 5
HYPERBOLA_TRANSVERSE_AXIS_MIN = 2
HYPERBOLA_TRANSVERSE_AXIS_MAX = 5

HYPERBOLA_X_RANGE = 20
HYPERBOLA_Y_RANGE = 20

PARABOLA_DIRECTIONS = ['concave upward', 'concave downward', 'concave left', 'concave right']

ELLIPSE_DIRECTIONS = ['horizontal', 'vertical']

HYPERBOLA_DIRECTIONS = ['horizontal', 'vertical']


CONIC_SECTIONS_LIST = [
['Circle', 'What conic section is produced when the cutting plane intersects the cone parallel to the base not hitting the apex'],
['Parabola', 'What conic section is produced when the cutting plane intersects the cone parallel to one of its slant heights, but not exactly at the edge'],
['Ellipse', 'What conic section is produced when the cutting plane intersects the cone in such a way that the intersection is a closed curve'],
['Hyperbola', 'What conic section is produced when the cutting plane intersects the cone perpendicular to the base'],
['Point', 'What conic section is produced when the cutting plane intersects the cone parallel to the base and exactly at the apex'],
['Line', 'What conic section is produced when the cutting plane intersects the cone parallel to the base exactly at the edges'],
['Two lines', 'What conic section is produced when the cutting plane intersects the cone perpendicular to the base hitting the apex'],
['Parabola', 'The set of all fixed points in a plane equidistant from a fixed point and a fixed line'],
['Asymptote', 'Refers to a straight line towards which a curve approaches but never meets']
]

class Point():
    def __init__(self):
        pass

    def init_random(self):
        abcissa = random.randint(-X_RANGE, X_RANGE)
        ordinate = random.randint(-Y_RANGE, X_RANGE)

        self.x = abcissa
        self.y = ordinate
        self.string = f"""({self.x}, {self.y})"""

    def init_define(self, abcissa, ordinate):
        self.x = abcissa
        self.y = ordinate
        self.string = f"""({self.x}, {self.y})"""

    def quadrant(self):

        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x == 0 and (not self.y == 0):
            return 'y-axis'
        elif (not self.x == 0) and self.y == 0:
            return 'x-axis'
        else: 
            return 'origin'

    def distance(self, point_object):
        return math.sqrt((self.x - point_object.x)**2 + (self.y - point_object.y)**2)

    def midpoint(self, point_object):
        i = Point()

        abcissa = (self.x + point_object.x ) / 2
        ordinate = (self.y + point_object.y ) / 2

        i.init_define(abcissa, ordinate)

        return i

    def extend(self, point_object, factor):
        #self is FROM, point_object is TO

        abcissa = self.x + (point_object.x - self.x) * factor
        ordinate = self.y + (point_object.y - self.y) * factor

        point = Point()
        point.init_define(abcissa, ordinate)
        return point

    def area_shoelace_3_points(self, p2, p3):

        area = abs(0.5 *((self.x * p2.y  + p2.x * p3.y + p3.x * self.y)-(p2.x * self.y + p3.x * p2.y + self.x * p3.y)))

        return area

    def above(self, units = None):
        
        p = Point()
        if units:
            p.init_define(self.x, self.y + units)
            return p
        else:
            p.init_define(self.x, self.y + random.randint(1, Y_RANGE))
            return p

    def below(self, units = None):
        p = Point()
        if units:
            p.init_define(self.x, self.y - units)
            return p
        else:
            p.init_define(self.x, self.y - random.randint(1, Y_RANGE))
            return p

    def right(self, units = None):
        p = Point()
        if units:
            p.init_define(self.x + units, self.y)
            return p
        else:
            p.init_define(self.x + random.randint(1, X_RANGE), self.y)
            return p

    def left(self, units = None):
        p = Point()
        if units:
            p.init_define(self.x - units, self.y)
            return p
        else:
            p.init_define(self.x - random.randint(1, X_RANGE), self.y)
            return p

    def round(self, decimals = 2):
        try:
            self.x = round(self.x, decimals)
            self.y = round(self.y, decimals)
            self.string = f"""({self.x}, {self.y})"""
        except:
            pass



class Line():
    def __init__(self):
        pass

    def init_two_points(self, point1, point2):
        try:
            self.general = (point2.x - point1.x) * y - (point2.y - point1.y) *x + point2.y * point1.x - point1.y * point2.x
            self.slope = (point2.y - point1.y) / (point2.x - point1.x)
            self.string = f"""{self.general} = 0"""
        except:
            self.general = x - point1.x
            self.string = f"""{self.general} = 0"""
            self.slope = 'undefined'


    def init_point_slope(self, point, slope):

        self.general = slope * x - y - slope * point.x + point.y
        self.slope = slope
        self.string = f"""{self.general} = 0"""
    def init_slope_intercept(self, slope, yintercept):

        self.general = slope * x - y + yintercept 
        self.string = f"""{self.general} = 0"""
        self.slope = slope
    def init_intercepts(self, a, b):

        self.general = b * x + a * y - a * b 
        self.slope = - b / a
        self.string = f"""{self.general} = 0"""

    def perpendicular(self):
        return -1/self.slope

    def parallel(self):
        return self.slope

    def init_random(self):

        point1 = Point()
        point2 = Point()
        point1.init_random()
        point2.init_random()

        self.general = (point2.x - point1.x) * y - (point2.y - point1.y) *x + point2.y * point1.x - point1.y * point2.x
        try:
            self.slope = (point2.y - point1.y) / (point2.x - point1.x)
        except:
            self.slope = 'undefined'
        self.string = f"""{self.general} = 0"""

    def inclination(self):

        return c.angle(math.atan(self.slope), 'radians')

    def angle_to_line(self, line):

        tan_theta = (self.slope - line.slope)/(1 + self.slope*line.slope)

        if tan_theta > 0:
            return c.angle(math.atan(tan_theta))
        else:
            return c.angle(math.pi - math.atan(tan_theta))

    def distance(self, object_input):
        if type(object_input) is Point:
            general = self.general
            A = general.coeff(x)
            B = general.coeff(y)
            #coeffs = general.all_coeffs()
            C = general.func(*[term for term in general.args if not term.free_symbols])
            print(A)
            print(B)
            print(C)

            distance = abs((A * object_input.x + B * object_input.y + C) / (math.sqrt(A**2 + B**2)))
            return distance

        if type(object_input) is Line:
            general = self.general
            general2 = object_input.general
            A1 = general.coeff(x)
            B1 = general.coeff(y)

            A2 = general2.coeff(x)
            B2 = general2.coeff(y)

            #coeffs = general.all_coeffs()
            #coeffs2 = general2.all_coeffs()
            C1 = general.func(*[term for term in general.args if not term.free_symbols])
            C2 = general2.func(*[term for term in general2.args if not term.free_symbols])


            distance = abs((C2 - C1) / (math.sqrt(A1**2 + B1**2)))
            return distance

    def point(self):
        x1 = random.randint(-X_RANGE, X_RANGE)
        temp1 = sympy.solveset(sympy.Eq(self.general.subs(x, x1), 0), y)
        temp2 = list(temp1)
        y1 = random.choice(temp2)

        point = Point()
        point.init_define(x1, y1)
        return point

    def y_in_terms_of_x(self):
        try:
            return random.choice(list(sympy.solveset(sympy.Eq(self.general, 0), y)))
        except:
            print('error ', list(sympy.solveset(sympy.Eq(self.general, 0), y)))

class Circle():
    def __init__(self):
        pass

    def init_random(self):
        center = Point()
        center.init_random()

        radius = random.randint(RADIUS_MIN, RADIUS_MAX)

        self.center = center
        self.radius = radius
        self.general = sympy.expand((x - center.x)**2 + (y - center.y)**2 - radius**2)
        self.standard = sympy.Eq((x - center.x)**2 + (y - center.y)**2, radius**2)
        self.general_string = f"""{self.general} = 0"""
        self.standard_string = f"""{sympy.pretty(self.standard)}"""

        self.diameter = self.radius * 2

        self.equation = sympy.Eq(self.general, 0)

        self.xmax = self.center.x + self.radius
        self.xmin = self.center.x - self.radius

        self.ymax = self.center.y + self.radius
        self.ymin = self.center.y - self.radius

    def init_define(self, c, r):
        center = c
        radius = r

        self.center = center
        self.radius = radius
        self.general = sympy.expand((x - center.x)**2 + (y - center.y)**2 - radius**2)
        self.standard = sympy.Eq((x - center.x)**2 + (y - center.y)**2, radius**2)
        self.general_string = f"""{self.general} = 0"""
        self.standard_string = f"""{sympy.pretty(self.standard)}"""

        self.diameter = self.radius * 2

        self.xmax = self.center.x + self.radius
        self.xmin = self.center.x - self.radius

        self.ymax = self.center.y + self.radius
        self.ymin = self.center.y - self.radius

        self.equation = sympy.Eq(self.general, 0)

    def area(self):
        self.area = math.pi * self.radius**2

        return self.area

    def circumference(self):
        self.circumference = 2 * math.pi * self.radius
        return self.circumference

    def general_coefficients(self):
        self.A = self.general.coeff(x**2)
        self.B = self.general.coeff(x).coeff(y)
        self.C = self.general.coeff(y**2)
        self.D = self.general.coeff(x)
        self.E = self.general.coeff(y)
        self.F = self.general.func(*[term for term in self.general.args if not term.free_symbols])

        return [self.A, self.B, self.C, self.D, self.E, self.F]

    def point(self):
        p1 = Point()

        x1 = random.randint(self.xmin, self.xmax)
        temp = sympy.solveset(self.general.subs(x, x1), y)
        temp2 = list(temp)
        y1 = random.choice(temp2)
        p1.init_define(x1, y1)

        return p1


    def three_points(self):

        p1 = Point()
        p2 = Point()
        p3 = Point()

        x1 = random.randint(self.xmin, self.xmax)
        x2 = random.randint(self.xmin, self.xmax)
        x3 = random.randint(self.xmin, self.xmax)

        temp = sympy.solveset(self.general.subs(x, x1), y)
        temp2 = sympy.solveset(self.general.subs(x, x2), y)
        temp3 = sympy.solveset(self.general.subs(x, x3), y)

        temp4 = list(temp)
        temp5 = list(temp2)
        temp6 = list(temp3)

        y1 = random.choice(temp4)
        y2 = random.choice(temp5)
        y3 = random.choice(temp6)

        p1.init_define(x1, y1)
        p2.init_define(x2, y2)
        p3.init_define(x3, y3)

        return [p1, p2, p3]

    def distance_to_center(self, object):
        if type(object) is Point:
            return math.sqrt((self.center.x - object.x)**2 + (self.center.y - object.y)**2)


class Parabola():
    def __init__(self):
        pass
    def init_random(self, **kwargs):
        concavity = None
        for key, value in kwargs.items():
            if key == 'orientation':
                concavity = value

        if concavity == None:
            concavity = random.choice(PARABOLA_DIRECTIONS)
        vertex = Point()
        vertex.init_random()


        if concavity == 'concave upward':
            focus = vertex.above()
            focal_length = focus.y - vertex.y
            general = (x - vertex.x)**2 - 4 * focal_length * (y - vertex.y)
            
            directrix = y - vertex.y + focal_length

        elif concavity == 'concave downward':
            focus = vertex.below()
            focal_length = focus.y - vertex.y
            general = (x - vertex.x)**2 - 4 * focal_length * (y - vertex.y)
            
            directrix = y - vertex.y - focal_length

        elif concavity == 'concave right':
            focus = vertex.right()
            focal_length = focus.x - vertex.x
            general = (y - vertex.y)**2 - 4 * focal_length * (x - vertex.y)
            directrix = x - vertex.x + focal_length

        elif concavity == 'concave left':
            focus = vertex.left()
            focal_length = focus.x - vertex.x
            general = (y - vertex.y)**2 - 4 * focal_length * (x - vertex.y)
            directrix = x - vertex.x - focal_length

        else:
            raise InputError('invalid concavity direction for parabolas')

        latus_rectum = 4 * abs(focal_length)

        self.concavity = concavity
        self.vertex = vertex
        self.focus = focus
        self.focal_length = focal_length
        self.general = sympy.expand(general)
        self.general_string = f"""{self.general} = 0"""
        self.directrix = directrix
        self.directrix_string = f"""{directrix} = 0"""
        self.latus_rectum = latus_rectum


    def point(self):

        if self.concavity == 'concave upward' or self.concavity == 'concave downward':
            x1 = random.randint(-X_RANGE, X_RANGE)
            temp = sympy.solveset(sympy.Eq(self.general.subs(x, x1), 0), y, domain = sympy.S.Reals)
            temp2 = list(temp)
            y1 = random.choice(temp2)

        elif self.concavity == 'concave right' or self.concavity == 'concave left':
            y1 = random.randint(-Y_RANGE, Y_RANGE)
            temp = sympy.solveset(sympy.Eq(self.general.subs(y, y1), 0), x, domain = sympy.S.Reals)
            temp2 = list(temp)
            x1 = random.choice(temp2)

        point = Point()
        point.init_define(x1, y1)

        return point

    def points_in_line(self):
        point1 = Point()
        point2 = Point()
        if self.concavity == 'concave upward':
            random_y = random.randint(self.vertex.y + 1, Y_RANGE)
            x_solutions = sympy.solveset(self.general.subs(y, random_y), x, domain = sympy.S.Reals)

            x1 = x_solutions.args[0]
            x2 = x_solutions.args[1]

            point1.init_define(x1, random_y)
            point2.init_define(x2, random_y)

        if self.concavity == 'concave downward':
            random_y = random.randint(-Y_RANGE, self.vertex.y - 1)
            x_solutions = sympy.solveset(self.general.subs(y, random_y), x, domain = sympy.S.Reals)

            x1 = x_solutions.args[0]
            x2 = x_solutions.args[1]

            point1.init_define(x1, random_y)
            point2.init_define(x2, random_y)

        if self.concavity == 'concave right':
            random_x = random.randint(self.vertex.x +1 , X_RANGE)
            y_solutions = sympy.solveset(self.general.subs(x, random_x), y, domain = sympy.S.Reals)

            y1 = y_solutions.args[0]
            y2 = y_solutions.args[1]

            point1.init_define(random_x, y1)
            point2.init_define(random_x, y2)

        if self.concavity == 'concave left':
            random_x = random.randint(-X_RANGE, self.vertex.x - 1)
            y_solutions = sympy.solveset(self.general.subs(x, random_x), y, domain = sympy.S.Reals)

            y1 = y_solutions.args[0]
            y2 = y_solutions.args[1]

            point1.init_define(random_x, y1)
            point2.init_define(random_x, y2)

        return [point1, point2]


    def points(self, n = 3):

        points = []

        for i in range(n):

            if self.concavity == 'concave upward' or self.concavity == 'concave downward':
                x1 = random.randint(-X_RANGE, X_RANGE)
                temp = sympy.solveset(sympy.Eq(self.general.subs(x, x1), 0), y)
                temp2 = list(temp)
                y1 = random.choice(temp2)

            elif self.concavity == 'concave right' or self.concavity == 'concave left':
                y1 = random.randint(-Y_RANGE, Y_RANGE)
                temp = sympy.solveset(sympy.Eq(self.general.subs(y, y1), 0), x)
                temp2 = list(temp)
                x1 = random.choice(temp2)
            else:
                raise InputError('invalid concavity')

            point = Point()
            point.init_define(x1, y1)
            points.append(point)

        return points

    def y_in_terms_of_x(self):
        temp1 = sympy.solveset(sympy.Eq(self.general, 0), y)
        temp2 = list(temp1)
        return random.choice(temp2)

    def area_parabola_and_latus_rectum(self):

        return (8/3) * abs(self.focal_length)**2

class Ellipse():
    def __init__(self):
        pass

    def init_random(self):
        self.center = Point()
        self.center.init_random()


        self.orientation = random.choice(ELLIPSE_DIRECTIONS)
        
        self.semi_minor_axis = random.randint(ELLIPSE_MINOR_AXIS_MIN, ELLIPSE_MINOR_AXIS_MAX)

        self.semi_major_axis = random.randint(self.semi_minor_axis + 1, ELLIPSE_MAJOR_AXIS_MAX)

        self.focal_length = sympy.sqrt(self.semi_major_axis**2 - self.semi_minor_axis**2)


        self.major_axis = 2 * self.semi_major_axis
        self.minor_axis = 2 * self.semi_minor_axis
        self.eccentricity = self.focal_length / self.semi_major_axis
        self.directrix_distance = self.semi_major_axis / self.eccentricity

        if self.orientation == 'horizontal':
            self.focus1 = self.center.right(self.focal_length)
            self.focus2 = self.center.left(self.focal_length)
            self.vertex1 = self.center.right(self.semi_major_axis)
            self.vertex2 = self.center.left(self.semi_major_axis)
            self.covertex1 = self.center.above(self.semi_minor_axis)
            self.covertex2 = self.center.below(self.semi_minor_axis)

            self.general = sympy.expand((x - self.center.x)**2/self.semi_major_axis**2 + (y - self.center.y)**2/self.semi_minor_axis**2 - 1) * self.semi_major_axis**2 * self.semi_minor_axis**2

            self.directrix1 = x - self.center.x - self.directrix_distance
            self.directrix2 = x - self.center.x + self.directrix_distance
            
        elif self.orientation == 'vertical':
            self.focus1 = self.center.above(self.focal_length)
            self.focus2 = self.center.below(self.focal_length)
            self.vertex1 = self.center.above(self.semi_major_axis)
            self.vertex2 = self.center.below(self.semi_major_axis)
            self.covertex1 = self.center.right(self.semi_minor_axis)
            self.covertex2 = self.center.left(self.semi_minor_axis)

            self.general = sympy.expand((y - self.center.y)**2/self.semi_major_axis**2 + (x - self.center.x)**2/self.semi_minor_axis**2 - 1) * self.semi_major_axis**2 * self.semi_minor_axis**2

            self.directrix1 = y - self.center.y - self.directrix_distance
            self.directrix2 = y - self.center.y + self.directrix_distance

        else:
            raise InputError('input invalid in ellipse orientation')

        self.general_string = f"""{self.general} = 0"""
        
        self.area = math.pi * self.semi_major_axis * self.semi_minor_axis
        self.circumference = math.pi * (3*(self.semi_major_axis + self.semi_minor_axis) - math.sqrt(10*self.semi_major_axis*self.semi_minor_axis + 3*(self.semi_major_axis**2 + self.semi_minor_axis**2)))
        #circumference formula reference
        #https://en.wikipedia.org/wiki/Ellipse
        self.directrix1_string = f"""{self.directrix1} = 0"""
        self.directrix2_string = f"""{self.directrix2} = 0""" 

        self.latus_rectum = sympy.sympify(2 * self.semi_minor_axis**2 / self.semi_major_axis)

    def init_define(self, center, a, b, orientation):
        self.center = center
        self.orientation = orientation
        
        self.semi_minor_axis = b

        self.semi_major_axis = a

        if self.semi_minor_axis > self.semi_major_axis:
            raise InputError('semi-major axis should be larger than semi-minor axis (a > b)')

        self.focal_length = sympy.sqrt(self.semi_major_axis**2 - self.semi_minor_axis**2)


        self.major_axis = 2 * self.semi_major_axis
        self.minor_axis = 2 * self.semi_minor_axis
        self.eccentricity = self.focal_length / self.semi_major_axis
        self.directrix_distance = self.semi_major_axis / self.eccentricity

        if self.orientation == 'horizontal':
            self.focus1 = self.center.right(self.focal_length)
            self.focus2 = self.center.left(self.focal_length)
            self.vertex1 = self.center.right(self.semi_major_axis)
            self.vertex2 = self.center.left(self.semi_major_axis)
            self.covertex1 = self.center.above(self.semi_minor_axis)
            self.covertex2 = self.center.below(self.semi_minor_axis)

            self.general = sympy.expand((x - self.center.x)**2/self.semi_major_axis**2 + (y - self.center.y)**2/self.semi_minor_axis**2 - 1) * self.semi_major_axis**2 * self.semi_minor_axis**2

            self.directrix1 = x - self.center.x - self.directrix_distance
            self.directrix2 = x - self.center.x + self.directrix_distance
            
        elif self.orientation == 'vertical':
            self.focus1 = self.center.above(self.focal_length)
            self.focus2 = self.center.below(self.focal_length)
            self.vertex1 = self.center.above(self.semi_major_axis)
            self.vertex2 = self.center.below(self.semi_major_axis)
            self.covertex1 = self.center.right(self.semi_minor_axis)
            self.covertex2 = self.center.left(self.semi_minor_axis)

            self.general = sympy.expand((y - self.center.y)**2/self.semi_major_axis**2 + (x - self.center.x)**2/self.semi_minor_axis**2 - 1) * self.semi_major_axis**2 * self.semi_minor_axis**2

            self.directrix1 = y - self.center.y - self.directrix_distance
            self.directrix2 = y - self.center.y + self.directrix_distance

        else:
            raise InputError('input invalid in ellipse orientation')

        self.general_string = f"""{self.general} = 0"""
        
        self.area = math.pi * self.semi_major_axis * self.semi_minor_axis
        self.circumference = math.pi * (3*(self.semi_major_axis + self.semi_minor_axis) - math.sqrt(10*self.semi_major_axis*self.semi_minor_axis + 3*(self.semi_major_axis**2 + self.semi_minor_axis**2)))
        #circumference formula reference
        #https://en.wikipedia.org/wiki/Ellipse
        self.directrix1_string = f"""{self.directrix1} = 0"""
        self.directrix2_string = f"""{self.directrix2} = 0"""  

        self.latus_rectum = sympy.sympify(2 * self.semi_minor_axis**2 / self.semi_major_axis )

    def point(self):
        if self.orientation == 'horizontal':
            x1 = random.randint(math.ceil(self.vertex2.x), math.floor(self.vertex1.x))
            temp = sympy.solveset(sympy.Eq(self.general.subs(x, x1), 0), y)
            temp2 = list(temp)
            y1 = random.choice(temp2)


        elif self.orientation == 'vertical':
            y1 = random.randint(math.ceil(self.vertex2.y), math.floor(self.vertex1.y))
            temp = sympy.solveset(sympy.Eq(self.general.subs(y, y1), 0), x)
            temp2 = list(temp)
            x1 = random.choice(temp2)

        else:
            raise InputError('ellipse orientation error')

        point = Point()
        point.init_define(x1, y1)
        return point

class Hyperbola():
    def __init__(self):
        pass

    def init_random(self):
        self.center = Point()
        self.center.init_random()


        self.orientation = random.choice(HYPERBOLA_DIRECTIONS)
        
        self.semi_transverse_axis = random.randint(HYPERBOLA_TRANSVERSE_AXIS_MIN, HYPERBOLA_TRANSVERSE_AXIS_MAX)

        self.semi_conjugate_axis = random.randint(HYPERBOLA_CONJUGATE_AXIS_MIN, HYPERBOLA_CONJUGATE_AXIS_MAX)

        self.focal_length = sympy.sqrt(self.semi_transverse_axis**2 + self.semi_conjugate_axis**2)


        self.transverse_axis = 2 * self.semi_transverse_axis
        self.conjugate_axis = 2 * self.semi_conjugate_axis
        self.eccentricity = self.focal_length / self.semi_transverse_axis
        self.directrix_distance = self.semi_transverse_axis / self.eccentricity

        self.asymptote1 = Line()
        self.asymptote2 = Line()

        if self.orientation == 'horizontal':
            self.focus1 = self.center.right(self.focal_length)
            self.focus2 = self.center.left(self.focal_length)
            self.vertex1 = self.center.right(self.semi_transverse_axis)
            self.vertex2 = self.center.left(self.semi_transverse_axis)

            self.general = sympy.expand((x - self.center.x)**2/self.semi_transverse_axis**2 - (y - self.center.y)**2/self.semi_conjugate_axis**2 - 1) * self.semi_transverse_axis**2 * self.semi_conjugate_axis**2

            self.directrix1 = x - self.center.x - self.directrix_distance
            self.directrix2 = x - self.center.x + self.directrix_distance

            self.asymptote1.init_point_slope(self.center ,self.semi_conjugate_axis/self.semi_transverse_axis)
            self.asymptote2.init_point_slope(self.center, -self.semi_conjugate_axis/self.semi_transverse_axis)
            
        elif self.orientation == 'vertical':
            self.focus1 = self.center.above(self.focal_length)
            self.focus2 = self.center.below(self.focal_length)
            self.vertex1 = self.center.above(self.semi_transverse_axis)
            self.vertex2 = self.center.below(self.semi_transverse_axis)

            self.general = sympy.expand((y - self.center.y)**2/self.semi_transverse_axis**2 - (x - self.center.x)**2/self.semi_conjugate_axis**2 - 1) * self.semi_transverse_axis**2 * self.semi_conjugate_axis**2

            self.directrix1 = y - self.center.y - self.directrix_distance
            self.directrix2 = y - self.center.y + self.directrix_distance

            self.asymptote1.init_point_slope(self.center, self.semi_transverse_axis/self.semi_conjugate_axis)
            self.asymptote2.init_point_slope(self.center, -self.semi_transverse_axis/self.semi_conjugate_axis)

        else:
            raise InputError('input invalid in hyperbola orientation')

        self.general_string = f"""{self.general} = 0"""
        
        #circumference formula reference
        #https://en.wikipedia.org/wiki/Ellipse
        self.directrix1_string = f"""{self.directrix1} = 0"""
        self.directrix2_string = f"""{self.directrix2} = 0""" 

        self.latus_rectum = sympy.sympify(2 * self.semi_conjugate_axis**2 / self.semi_transverse_axis )

    def point(self):
        if self.orientation == 'horizontal':
            x1 = random.randint(math.ceil(self.vertex2.x), math.floor(self.vertex1.x))

            while self.vertex2.x < x1 < self.vertex1.x:
                x1 = random.randint(-HYPERBOLA_X_RANGE , HYPERBOLA_X_RANGE)

            temp = sympy.solveset(sympy.Eq(self.general.subs(x, x1), 0), y)
            temp2 = list(temp)
            y1 = random.choice(temp2)


        elif self.orientation == 'vertical':
            y1 = random.randint(math.ceil(self.vertex2.y), math.floor(self.vertex1.y))

            while self.vertex2.y < y1 < self.vertex1.y:
                y1 = random.randint(-HYPERBOLA_Y_RANGE, HYPERBOLA_Y_RANGE)

            temp = sympy.solveset(sympy.Eq(self.general.subs(y, y1), 0), x)
            temp2 = list(temp)
            x1 = random.choice(temp2)

        else:
            raise InputError('ellipse orientation error')

        point = Point()
        point.init_define(x1, y1)
        return point


class Point_3D():
    def __init__(self):
        pass

    def init_random(self):
        abcissa = random.randint(-X_RANGE, X_RANGE)
        ordinate = random.randint(-Y_RANGE, Y_RANGE)
        applicate = random.randint(-Z_RANGE, Z_RANGE)

        self.x = abcissa
        self.y = ordinate
        self.z = applicate
        self.string = f"""({self.x}, {self.y}, {self.z})"""

    def init_define(self, abcissa, ordinate):
        self.x = abcissa
        self.y = ordinate
        self.z = applicate
        self.string = f"""({self.x}, {self.y}, {self.z})"""

    def ocatant(self):
        #not implemented yet
        return None

    def distance(self, point_object):
        return math.sqrt((self.x - point_object.x)**2 + (self.y - point_object.y)**2 + (self.z - point_object.z)**2)

    def midpoint(self, point_object):
        i = Point_3D()
        abcissa = (self.x + point_object.x ) / 2
        ordinate = (self.y + point_object.y ) / 2
        applicate = (self.z + point_object.z) / 2
        i.init_define(abcissa, ordinate, applicate)
        return i

    def extend(self, point_object, factor):
        #self is FROM, point_object is TO
        abcissa = self.x + (point_object.x - self.x) * factor
        ordinate = self.y + (point_object.y - self.y) * factor
        applicate = self.z + (point_object.z - self.z) * factor
        point = Point_3D()
        point.init_define(abcissa, ordinate, applicate)
        return point

    def area_shoelace_3_points(self, p2, p3):
        #to be implemented
        return None

    def round(self, decimals = 2):
        try:
            self.x = round(self.x, decimals)
            self.y = round(self.y, decimals)
            self.z = round(self.z, decimals)
            self.string = f"""({self.x}, {self.y}, {self.z})"""
        except:
            pass

#-------------------------------QUESTIONS-------------------------


class Distance_between_two_points():
    def __init__(self):
        point_1 = Point()
        point_2 = Point()
        point_1.init_random()
        point_2.init_random()
        self.point_1 = point_1
        self.point_2 = point_2
        self.distance = point_1.distance(point_2)

class Quadrant_identification():
    def __init__(self):
        point_1 = Point()
        point_1.init_random()
        self.point_1 = point_1
        self.quadrant = point_1.quadrant()












































        




























































