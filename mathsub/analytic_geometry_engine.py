import sympy
import math
import random
from generator import random_handler as ran
from generator import constants_conversions

x, y, z, t = sympy.symbols('x y z t', real = True)#generic variables

X_RANGE = 10
Y_RANGE = 10
Z_RANGE = 10

EXTEND_FACTOR_MIN = 2
EXTEND_FACTOR_MAX = 5

FRAC_MIN = 1
FRAC_MAX = 9
FRAC_VALUE_MIN = 0
FRAC_VALUE_MAX = 1

SLOPE_MAX = 5

RADIUS_MIN = 1
RADIUS_MAX = 9

ELLIPSE_MINOR_AXIS_MIN = 1
ELLIPSE_MINOR_AXIS_MAX = 5
ELLIPSE_MAJOR_AXIS_MAX = 10

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

def parse(string_input):
	string_input = str(string_input)
	return string_input.replace('**', '^').replace('*', ' ')

class Point():
	def __init__(self):
		pass

	def init_random(self):
		abcissa = random.randint(-X_RANGE, X_RANGE)
		ordinate = random.randint(-Y_RANGE, X_RANGE)

		self.x = abcissa
		self.y = ordinate
		self.string = parse(f"""({self.x}, {self.y})""")

		return self

	def init_define(self, abcissa, ordinate):
		self.x = abcissa
		self.y = ordinate
		self.string = parse(f"""({self.x}, {self.y})""")

		return self

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
		x_coordinate = round(self.x, decimals)
		y_coordinate = round(self.y, decimals)
		point = Point()
		point.init_define(x_coordinate, y_coordinate)
		return point

	def to_polar(self):
		return Point_Polar(math.sqrt(self.x**2 + self.y**2), math.atan2(point.y, point.x))

ORIGIN = Point()
ORIGIN.init_define(0, 0)

class Point_Polar():
	def __init__(self):
		pass

	def init_define(self, r, theta):
		self.r = r
		self.theta = constants_conversions.angle(theta, 'radians')

	def to_rectangular(self):
		return Point(self.r * math.cos(self.theta.radians), self.r * math.sin(self.theta.radians))

class Point_3_Dimensions():
	def __init__(self):
		pass

	def init_define(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
		self.rectangular = f"""({self.x:.4}, {self.y:.4}, {self.z:.4})"""

		self.rho = math.sqrt(self.x**2 + self.y**2)
		self.phi = constants_conversions.angle(math.atan2(self.y, self.x), 'radians')
		self.cylindrical = f"""({self.rho:.4}, {self.phi.radians:.4}, {self.z:.4})"""

		self.r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		self.theta = constants_conversions.angle(math.atan2(self.z, self.r), 'radians')
		self.spherical = f"""({self.r:.4}, {self.theta.radians:.4}, {self.phi.radians:.4})"""

		self.types = {'rectangular':self.rectangular, 'cylindrical':self.cylindrical, 'spherical':self.spherical, 'cartesian':self.rectangular}

	def init_random(self):
		self.x = float(random.randint(-X_RANGE, X_RANGE))
		self.y = float(random.randint(-Y_RANGE, Y_RANGE))
		self.z = float(random.randint(-Z_RANGE, Z_RANGE))
		self.rectangular = f"""({self.x:.4}, {self.y:.4}, {self.z:.4})"""

		self.rho = math.sqrt(self.x**2 + self.y**2)
		self.phi = constants_conversions.angle(math.atan2(self.y, self.x), 'radians')
		self.cylindrical = f"""({self.rho:.4}, {self.phi.radians:.4}, {self.z:.4})"""

		self.r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		self.theta = constants_conversions.angle(math.atan2(self.z, self.r), 'radians')
		self.spherical = f"""({self.r:.4}, {self.theta.radians:.4}, {self.phi.radians:.4})"""

		self.types = {'rectangular':self.rectangular, 'cylindrical':self.cylindrical, 'spherical':self.spherical, 'cartesian':self.rectangular}


class Line():
	def __init__(self):
		pass

	def init_two_points(self, point1, point2):
		try:
			self.general = (point2.x - point1.x) * y - (point2.y - point1.y) *x + point2.y * point1.x - point1.y * point2.x
			self.slope = (point2.y - point1.y) / (point2.x - point1.x)
			self.string = parse(f"""{self.general} = 0""")
			self.equation = sympy.Eq((point2.x - point1.x) * y - (point2.y - point1.y) *x + point2.y * point1.x - point1.y * point2.x, 0)
		except:
			self.general = x - point1.x
			self.string = parse(f"""{self.general} = 0""")
			self.slope = 'undefined'
			self.equation = sympy.Eq(x - point1.x, 0)

		return self


	def init_point_slope(self, point, slope):
		self.general = slope * x - y - slope * point.x + point.y
		self.slope = slope
		self.string = parse(f"""{self.general} = 0""")
		self.equation = sympy.Eq(slope * x - y - slope * point.x + point.y, 0)
		return self


	def init_slope_intercept(self, slope, yintercept):
		self.general = slope * x - y + yintercept 
		self.string = parse(f"""{self.general} = 0""")
		self.slope = slope
		self.equation = sympy.Eq(slope * x - y + yintercept , 0)
		return self

	def init_intercepts(self, a, b):
		self.general = b * x + a * y - a * b 
		self.slope = - b / a
		self.string = parse(f"""{self.general} = 0""")
		self.equation = sympy.Eq(b * x + a * y - a * b , 0)
		return self

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
		self.string = parse(f"""{self.general} = 0""")
		return self

	def inclination(self):

		return constants_conversions.angle(math.atan(self.slope), 'radians')

	def angle_to_line(self, line):
		m1 = self.slope
		m2 = line.slope

		if m2 > m1:
			m2, m1 = m1, m2


		tan_theta = (m1 - m2)/(1 + m1*m2)

		if tan_theta > 0:
			return constants_conversions.angle(math.atan(tan_theta))
		else:
			return constants_conversions.angle(math.pi - math.atan(tan_theta))


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
		print('equation: ', sympy.Eq(self.general.subs(x, x1), 0))
		y1 = sympy.solveset(sympy.Eq(self.general.subs(x, x1), 0), y).args[0]
		print('y1: ', y1)
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
		self.area = math.pi * self.radius**2

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
		self.area = math.pi * self.radius**2

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
		return {'A':self.A, 'B':self.B, 'C':self.C, 'D':self.D, 'E':self.E, 'F':self.F}

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
		tryagain = True
		while tryagain:
			try:
				point_1 = Point()
				point_2 = Point()
				point_1.init_random()
				point_2.init_random()
				self.point_1 = point_1
				self.point_2 = point_2
				self.distance = point_1.distance(point_2)
				tryagain = False
			except:
				tryagain = True

class Quadrant_identification():
	def __init__(self):
		point_1 = Point()
		point_1.init_random()
		self.point_1 = point_1
		self.quadrant = point_1.quadrant()

class Midpoint():
	def __init__(self):
		tryagain = True
		while tryagain:
			try:
				self.point_1 = Point()
				self.point_2 = Point()
				self.point_1.init_random()
				self.point_2.init_random()
				self.midpoint = self.point_1.midpoint(self.point_2)
				tryagain = False
			except:
				pass

class Extension_of_line_segment():
	def __init__(self):
		point_1 = Point()
		point_2 = Point()
		point_1.init_random()
		point_2.init_random()
		factor = random.randint(EXTEND_FACTOR_MIN, EXTEND_FACTOR_MAX)
		terminal_point = point_1.extend(point_2, factor)
		self.point_1 = point_1
		self.point_2 = point_2
		self.factor = factor
		self.terminal_point = terminal_point

class Division_of_line_segment():
	def __init__(self):
		point_1 = Point()
		point_2 = Point()

		point_1.init_random()
		point_2.init_random()
		
		factor = random.randint(1,99)/100
		terminal_point = point_1.extend(point_2, factor)
		
		self.point_1 = point_1
		self.point_2 = point_2
		self.factor = factor
		self.terminal_point = terminal_point


class Equation_of_a_line_two_points():
	def __init__(self):
		point_1 = Point()
		point_2 = Point()
		point_1.init_random()
		point_2.init_random()
		line = Line()
		line.init_two_points(point_1, point_2)
		self.point_1 = point_1
		self.point_2 = point_2
		self.line = line

class Equation_of_a_line_point_slope():
	def __init__(self):
		point = Point()
		point.init_random()
		slope = random.randint(-SLOPE_MAX, SLOPE_MAX)
		line = Line()
		line.init_point_slope(point, slope)
		self.point = point
		self.slope = slope
		self.line = line

class Equation_of_a_line_slope_intercept():
	def __init__(self):
		y_intercept = random.randint(-Y_RANGE, Y_RANGE)
		slope = random.randint(-SLOPE_MAX, SLOPE_MAX)
		line = Line()
		line.init_slope_intercept(slope, y_intercept)
		self.slope = slope
		self.y_intercept = y_intercept
		self.line = line

class Equation_of_a_line_intercepts():
	def __init__(self):
		tryagain = True
		while tryagain:
			try:
				x_intercept = random.randint(-X_RANGE, X_RANGE)
				y_intercept = random.randint(-Y_RANGE, Y_RANGE)
				line = Line()
				line.init_intercepts(x_intercept, y_intercept)
				self.x_intercept = x_intercept
				self.y_intercept = y_intercept
				self.line = line
				tryagain = False
			except:
				pass

class Line_parallel_to_line():
	def __init__(self):
		tryagain = True
		while tryagain:
			try:
				point_1 = Point()
				point_2 = Point()
				point_3 = Point()
				point_1.init_random()
				point_2.init_random()
				point_3.init_random()
				line_1 = Line()
				line_1.init_two_points(point_1, point_2)
				line_2 = Line()
				line_2.init_point_slope(point_3, line_1.parallel())
				self.point_1 = point_1
				self.point_2 = point_2
				self.point_3 = point_3
				self.line = line_2
				tryagain = False
			except:
				pass

class Line_perpendicular_to_line():
	def __init__(self):
		tryagain = True
		while tryagain:
			try:
				point_1 = Point()
				point_2 = Point()
				point_3 = Point()
				point_1.init_random()
				point_2.init_random()
				point_3.init_random()
				line_1 = Line()
				line_1.init_two_points(point_1, point_2)
				line_2 = Line()
				line_2.init_point_slope(point_3, line_1.perpendicular())
				self.point_1 = point_1
				self.point_2 = point_2
				self.point_3 = point_3
				self.line = line_2
				tryagain = False
			except:
				pass

class Angle_between_the_lines():
	def __init__(self):
		tryagain = True
		while tryagain:
			try:
				line_1 = Line()
				line_1.init_random()
				line_2 = Line()
				line_2.init_random()
				angle = line_1.angle_to_line(line_2)
				self.line_1 = line_1
				self.line_2 = line_2
				self.angle = angle
				tryagain = False
			except:
				pass

class Distance_from_point_to_line():
	def __init__(self):
		line = Line()
		line.init_random()
		point = Point()
		point.init_random()
		distance = line.distance(point)
		self.line = line
		self.point = point
		self.distance = distance

class Distance_from_line_to_line():
	def __init__(self):
		line_1 = Line()
		slope = random.randint(-SLOPE_MAX, SLOPE_MAX)
		y_intercept_1 = random.randint(-Y_RANGE, Y_RANGE)
		line_1.init_slope_intercept(slope, y_intercept_1)
		line_2 = Line()
		y_intercept_2 = random.randint(-Y_RANGE, Y_RANGE)
		line_2.init_slope_intercept(slope, y_intercept_2)
		distance = line_1.distance(line_2)
		self.line_1 = line_1
		self.line_2 = line_2
		self.distance = distance

class Area_of_three_points():
	def __init__(self):
		point_1 = Point()
		point_2 = Point()
		point_3 = Point()
		point_1.init_random()
		point_2.init_random()
		point_3.init_random()
		area = point_1.area_shoelace_3_points(point_2, point_3)
		self.point_1 = point_1
		self.point_2 = point_2
		self.point_3 = point_3
		self.area = area

class Conic_section_derivation():
	def __init__(self):
		conic = random.choice(CONIC_SECTIONS_LIST)
		self.description = conic[1]
		self.conic = conic[0]

class Circle_standard_to_general():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		self.circle = circle

class Circle_circumference_from_general():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		self.circle = circle

class Circle_general_from_three_points():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		points = circle.three_points()
		self.circle = circle
		self.points = points

class Circle_coefficient_from_general_and_radius():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		coeff = circle.general_coefficients()
		self.radius = circle.radius
		self.coefficients = coeff

class Circle_distance_from_point():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		point = Point()
		point.init_random()
		while circle.distance_to_center(point) <= circle.radius:
			point = Point()
			point.init_random()
		self.circle = circle
		self.point = point
		self.distance = circle.distance_to_center(point)

class Circle_center_from_general():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		self.circle = circle

class Circle_area_from_general():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		self.circle = circle

class Circle_area_from_center_and_tangent_line():
	def __init__(self):
		line = Line()
		line.init_random()
		point = Point()
		point.init_random()
		circle = Circle()
		circle.init_define(point, line.distance(point))
		self.area = circle.area()
		self.center = circle.center
		self.line = line

class Circle_center_to_line_distance():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		point_1 = circle.point()
		line_1 = Line()
		line_1.init_two_points(circle.center, point_1)
		point_2 = circle.center.extend(point_1, random.randint(EXTEND_FACTOR_MIN, EXTEND_FACTOR_MAX))
		line_2 = Line()
		line_2.init_point_slope(point_2, line_1.perpendicular())
		self.circle = circle
		self.line = line_2
		self.distance = point_1.distance(point_2)

class Circle_length_of_tangent_from_general_and_point():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		point_1 = circle.point()
		print('point_1 ', point_1.string)
		line_1 = Line()
		line_1.init_two_points(circle.center, point_1)
		line_2 = Line()
		line_2.init_point_slope(point_1, line_1.perpendicular())
		point_2 = line_2.point()
		print('point_2 ', point_2.string)
		self.distance = point_1.distance(point_2)
		self.point = point_2
		self.circle = circle

class Circle_ratio_of_circumference():
	def __init__(self):
		circle_1 = Circle()
		circle_2 = Circle()
		circle_1.init_random()
		circle_2.init_random()
		self.circle_1 = circle_1
		self.circle_2 = circle_2
		self.ratio = circle_1.circumference()/circle_2.circumference()

class Circle_diameter_from_general():
	def __init__(self):
		circle = Circle()
		circle.init_random()
		self.circle = circle
		self.diameter = circle.diameter

class Parabola_diameter_from_general():
	def __init__(self):
		parabola = Parabola()
		parabola.init_random()
		self.parabola = parabola

class Parabola_latus_rectum_from_general():
	def __init__(self):
		parabola = Parabola()
		parabola.init_random()
		self.parabola = parabola

class Parabola_generic():
	def __init__(self):
		parabola = Parabola()
		parabola.init_random()
		self.parabola = parabola

class Parabola_from_three_points():
	def __init__(self):
		parabola = Parabola()
		parabola.init_random()
		self.points = parabola.points(3)
		self.parabola = parabola

class Ellipse_generic():
	def __init__(self):
		ellipse = Ellipse()
		ellipse.init_random()
		self.ellipse = ellipse



























		




























































