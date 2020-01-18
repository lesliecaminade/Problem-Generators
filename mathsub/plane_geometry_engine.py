from generator import random_handler as ran
from generator import constants_conversions as c
from num2words import num2words
from mathsub import trigonometry_engine
from mathsub import analytic_geometry_engine
import sympy
import math
import random
import fractions

x, y, z = sympy.symbols('x y z', real = True)#generic variables

POLYGON_SIDE_MIN = 3
POLYGON_SIDE_MAX = 20

MIN_LENGTH = 1
MAX_LENGTH = 20

STAR_SIDE_MIN = 5
STAR_SIDE_MAX = 20

STAR_CIRCUMRADIUS_MIN = 1
STAR_CIRCUMRADIUS_MAX = 20

POLYGON_NAMES = [
None, 
None,
None,
'triangle',
'quadrilateral',
'pentagon',
'hexagon',
'heptagon',
'octagon',
'nonagon',
'decagon',
'undecagon',
'dodecagon',
'tridecagon',
'tetradecagon',
'pentadecagon',
'hexadecagon',
'heptadecagon',
'octadecagon',
'enneadecagon',
'icosagon']


def polygon_name(sides):
	return POLYGON_NAMES[sides]


class Regular_Polygon():
	def __init__(self):
		pass

	def init_random(self):
		sides = random.randint(POLYGON_SIDE_MIN, POLYGON_SIDE_MAX)
		name = polygon_name(sides)
		side_length = round(random.uniform(MIN_LENGTH, MAX_LENGTH),2)
		area = (1/4) * sides * side_length**2 * (1/math.tan(math.pi/sides))
		inradius = ( side_length / 2 ) / (math.tan(math.pi / sides))
		circumradius = ( side_length / 2 ) / (math.sin(math.pi / sides))

		diagonals = (sides / 2) * (sides - 3)
		triangles = (sides - 2)
		sum_of_interior_angles = c.angle(triangles * math.pi)
		interior_angle = c.angle(sum_of_interior_angles.radians / sides)
		sum_of_exterior_angles = c.angle(math.pi * 2)
		exterior_angle = c.angle( sum_of_exterior_angles.radians / sides)

		area_2 = sides * inradius**2 * math.tan(math.pi / sides)
		area_3 = (sides/2) * circumradius**2 * math.sin(2*math.pi / sides)
		print('check_1', round(area, 2) == round(area_2, 2))
		print('check_2', round(area, 2) == round(area_3, 2))

		self.sides = sides
		self.name = name
		self.side = side_length
		self.area = area
		self.inradius = inradius
		self.circumradius = circumradius
		self.diagonals = diagonals
		self.triangles = triangles
		self.sum_of_interior_angles = sum_of_interior_angles
		self.interior_angle = interior_angle
		self.sum_of_exterior_angles = sum_of_exterior_angles
		self.exterior_angle = exterior_angle

		self.central_angle = c.angle(math.pi * 2 / sides)

	def init_inradius(self, sides, inradius):
		circumradius = inradius / math.cos(math.pi / sides)
		side = 2 * inradius * math.tan(math.pi / sides)
		name = polygon_name(sides)
		diagonals = (sides / 2) * (sides - 3)
		triangles = (sides - 2)
		sum_of_interior_angles = c.angle(triangles * math.pi)
		interior_angle = c.angle(sum_of_interior_angles.radians / sides)
		sum_of_exterior_angles = c.angle(math.pi * 2)
		exterior_angle = c.angle( sum_of_exterior_angles.radians / sides)

		area = (1/4) * sides * side**2 * (1/math.tan(math.pi/sides))
		area_2 = sides * inradius**2 * math.tan(math.pi / sides)
		area_3 = (sides/2) * circumradius**2 * math.sin(2*math.pi / sides)
		print('check_1', round(area, 2) == round(area_2, 2))
		print('check_2', round(area, 2) == round(area_3, 2))

		self.sides = sides
		self.name = name
		self.side = side
		self.area = area
		self.inradius = inradius
		self.circumradius = circumradius
		self.diagonals = diagonals
		self.triangles = triangles
		self.sum_of_interior_angles = sum_of_interior_angles
		self.interior_angle = interior_angle
		self.sum_of_exterior_angles = sum_of_exterior_angles
		self.exterior_angle = exterior_angle
		self.central_angle = c.angle(math.pi * 2 / sides)

	def init_circumradius(self, sides, circumradius):
		inradius = circumradius * math.cos(math.pi / sides)
		side = 2 * circumradius * math.sin(math.pi / sides)
		name = polygon_name(sides)
		diagonals = (sides / 2) * (sides - 3)
		triangles = (sides - 2)
		sum_of_interior_angles = c.angle(triangles * math.pi)
		interior_angle = c.angle(sum_of_interior_angles.radians / sides)
		sum_of_exterior_angles = c.angle(math.pi * 2)
		exterior_angle = c.angle( sum_of_exterior_angles.radians / sides)

		area = (1/4) * sides * side**2 * (1/math.tan(math.pi/sides))
		area_2 = sides * inradius**2 * math.tan(math.pi / sides)
		area_3 = (sides/2) * circumradius**2 * math.sin(2*math.pi / sides)
		print('check_1', round(area, 2) == round(area_2, 2))
		print('check_2', round(area, 2) == round(area_3, 2))

		self.sides = sides
		self.name = name
		self.side = side
		self.area = area
		self.inradius = inradius
		self.circumradius = circumradius
		self.diagonals = diagonals
		self.triangles = triangles
		self.sum_of_interior_angles = sum_of_interior_angles
		self.interior_angle = interior_angle
		self.sum_of_exterior_angles = sum_of_exterior_angles
		self.exterior_angle = exterior_angle
		self.central_angle = c.angle(math.pi * 2 / sides)

	def init_side(self, sides, side):
		inradius = side / (2 * math.tan(math.pi / sides))
		circumradius = side / (2 * math.sin(math.pi / sides))
		name = polygon_name(sides)
		diagonals = (sides / 2) * (sides - 3)
		triangles = (sides - 2)
		sum_of_interior_angles = c.angle(triangles * math.pi)
		interior_angle = c.angle(sum_of_interior_angles.radians / sides)
		sum_of_exterior_angles = c.angle(math.pi * 2)
		exterior_angle = c.angle( sum_of_exterior_angles.radians / sides)

		area = (1/4) * sides * side**2 * (1/math.tan(math.pi/sides))
		area_2 = sides * inradius**2 * math.tan(math.pi / sides)
		area_3 = (sides/2) * circumradius**2 * math.sin(2*math.pi / sides)
		print('check_1', round(area, 2) == round(area_2, 2))
		print('check_2', round(area, 2) == round(area_3, 2))

		self.sides = sides
		self.name = name
		self.side = side
		self.area = area
		self.inradius = inradius
		self.circumradius = circumradius
		self.diagonals = diagonals
		self.triangles = triangles
		self.sum_of_interior_angles = sum_of_interior_angles
		self.interior_angle = interior_angle
		self.sum_of_exterior_angles = sum_of_exterior_angles
		self.exterior_angle = exterior_angle
		self.central_angle = c.angle(math.pi * 2 / sides)

class Quadrilateral():
	def __init__(self):
		pass

	def init_random(self):
		#https://en.wikipedia.org/wiki/Quadrilateral
		triangle_1 = trigonometry_engine.Triangle()
		triangle_2 = trigonometry_engine.Triangle()

		diagonal_1 = round(random.randint(1,100), 2)

		repeat = True
		while repeat:
			angle_A_1 = c.angle(random.randint(10,80), 'degrees')
			angle_C_1 = c.angle(random.randint(10,80), 'degrees')
			angle_A_2 = c.angle(random.randint(10,80), 'degrees')
			angle_C_2 = c.angle(random.randint(10,80), 'degrees')



			triangle_1.init_define_ASA(angle_A_1.degrees, diagonal_1, angle_C_1.degrees)


			triangle_2.init_define_ASA(angle_A_2.degrees, diagonal_1, angle_C_2.degrees)

			angle_A = c.angle(angle_A_1.degrees + angle_A_2.degrees, 'degrees')
			angle_C = c.angle(angle_C_1.degrees + angle_C_2.degrees, 'degrees')

			angle_B = triangle_1.B
			angle_D = triangle_2.B

			side_a = triangle_1.c
			side_b = triangle_1.a
			side_c = triangle_2.a
			side_d = triangle_2.c

			print(side_a, side_b, side_c, side_d, angle_A.degrees, angle_B.degrees, angle_C.degrees, angle_D.degrees)

			print('check_1', side_a**2 + side_b**2 + side_c**2 > side_d**2 / 3)
			print('check_2', side_a**4 + side_b**4 + side_c**4 > side_d**4 / 27)
			print('check_3', round(angle_A.degrees + angle_B.degrees + angle_C.degrees + angle_D.degrees, 2) == 360)

			if round(angle_A.degrees + angle_B.degrees + angle_C.degrees + angle_D.degrees,1) == 360:
				repeat = False

		area = triangle_1.area + triangle_2.area
		perimeter = side_a + side_b + side_c + side_d
		
		diagonal_1_repeat = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_B.radians)
			)

		print('check_4', round(diagonal_1_repeat, 2) == round(diagonal_1, 2))

		diagonal_2 = math.sqrt(
			side_a**2 + side_d**2 - 2 * side_a * side_d * math.cos(angle_A.radians)
			)

		self.a = side_a
		self.b = side_b
		self.c = side_c
		self.d = side_d
		self.A = angle_A
		self.B = angle_B
		self.C = angle_C
		self.D = angle_D
		self.area = area
		self.perimeter = perimeter
		self.d1 = diagonal_1
		self.d2 = diagonal_2


class Trapezoid():
	def __init__(self):
		pass

	def init_random(self):
		#https://en.wikipedia.org/wiki/Trapezoid

		repeat = True
		while repeat:
			#a and b are the supposedly parallel sides
			side_a = round(random.uniform(MIN_LENGTH, MAX_LENGTH),2)
			side_b = round(random.uniform(MIN_LENGTH, MAX_LENGTH),2)
			side_c = round(random.uniform(MIN_LENGTH, MAX_LENGTH),2)
			side_d = round(random.uniform(MIN_LENGTH, MAX_LENGTH),2)
			if side_a > side_b:
				#side_a is the shorter base
				#side_b is the longer base
				side_a, side_b = side_b, side_a

			if abs(side_d - side_c) < abs(side_b - side_a) < (side_d + side_c) and not(side_a == side_b):
				#the trapezoid exists
				repeat = False

		median = (side_a + side_b) / 2

		altitude = math.sqrt(
			(-side_a + side_b + side_c + side_d) *
			(side_a - side_b + side_c + side_d) *
			(side_a - side_b + side_c - side_d) *
			(side_a - side_b - side_c + side_d)

			) / (2 * abs(side_b - side_a))

		area = median * altitude

		diagonal_1 = math.sqrt(
			(side_a * side_b**2 - side_a**2 * side_b - side_a * side_c**2 + side_b*side_d**2) / 
			(side_b - side_a)
			)

		diagonal_2 = math.sqrt(
			(side_a * side_b**2 - side_a**2 * side_b - side_a * side_d**2 + side_b * side_c**2) / 
			(side_b - side_a)
			)

		self.a = side_a
		self.b = side_b
		self.c = side_c
		self.d = side_d
		self.d1 = diagonal_1
		self.d2 = diagonal_2
		self.area = area
		self.perimeter = side_a + side_b + side_c + side_d
		self.median = median

class Parallelogram():
	def __init__(self):
		pass

	def init_random(self):
		#https://en.wikipedia.org/wiki/Parallelogram
		side_a = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)
		side_b = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)

		if side_a > side_b:
			#side_a is the shorter side
			#side_b is the longer side
			side_a, side_b = side_b, side_a

		angle_1 = c.angle(random.randint(10, 170), 'degrees')
		angle_2 = angle_1.supplementary()

		area = (1/2) * side_a * side_b * math.sin(angle_1.radians)
		perimeter = 2* side_a + 2*side_b

		diagonal_1 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_1.radians)
			)

		diagonal_2 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_2.radians)
			)

		self.a = side_a
		self.b = side_b
		self.c = side_a
		self.d = side_b
		self.A = angle_1
		self.B = angle_2
		self.C = angle_1
		self.D = angle_2
		self.area = area
		self.perimeter = perimeter
		self.d1 = diagonal_1
		self.d2 = diagonal_2

class Rhombus():
	def __init__(self):
		pass

	def init_random(self):
		side_a = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)
		side_b = side_a
		angle_1 = c.angle(random.randint(10, 170), 'degrees')
		angle_2 = angle_1.supplementary()

		area = (1/2) * side_a * side_b * math.sin(angle_1.radians)
		perimeter = 2* side_a + 2*side_b

		diagonal_1 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_1.radians)
			)

		diagonal_2 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_2.radians)
			)

		self.a = side_a
		self.b = side_b
		self.c = side_a
		self.d = side_b
		self.side = side_a
		self.A = angle_1
		self.B = angle_2
		self.C = angle_1
		self.D = angle_2
		self.area = area
		self.perimeter = perimeter
		self.d1 = diagonal_1
		self.d2 = diagonal_2

class Square():
	def __init__(self):
		pass

	def init_random(self):
		side_a = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)
		side_b = side_a
		angle_1 = c.angle(math.pi/2)
		angle_2 = angle_1

		area = (1/2) * side_a * side_b * math.sin(angle_1.radians)
		perimeter = 2* side_a + 2*side_b

		diagonal_1 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_1.radians)
			)

		diagonal_2 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_2.radians)
			)

		self.a = side_a
		self.b = side_b
		self.c = side_a
		self.d = side_b
		self.A = angle_1
		self.B = angle_2
		self.C = angle_1
		self.D = angle_2
		self.area = area
		self.perimeter = perimeter
		self.d1 = diagonal_1
		self.d2 = diagonal_2   

class Rectangle():
	def __init__(self):
		pass

	def init_random(self):
		side_a = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)
		side_b = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)
		if side_a > side_b:
			#side_a is the shorter side
			#side_b is the longer side
			side_a, side_b = side_b, side_a

		angle_1 = c.angle(math.pi/2)
		angle_2 = angle_1

		area = (1/2) * side_a * side_b * math.sin(angle_1.radians)
		perimeter = 2* side_a + 2*side_b

		diagonal_1 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_1.radians)
			)

		diagonal_2 = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_2.radians)
			)

		self.a = side_a
		self.b = side_b
		self.c = side_a
		self.d = side_b
		self.A = angle_1
		self.B = angle_2
		self.C = angle_1
		self.D = angle_2
		self.area = area
		self.perimeter = perimeter
		self.d1 = diagonal_1
		self.d2 = diagonal_2

class Circle():
	def __init__(self):
		pass

	def init_diameter(self, diameter):
		radius = diameter / 2
		circumference = math.pi * 2 * radius
		area = math.pi * radius**2

		self.r = radius
		self.d = diameter
		self.C = circumference
		self.area = area        

	def init_random(self):
		radius = round(random.uniform(MIN_LENGTH, MAX_LENGTH), 2)
		circumference = math.pi * 2 * radius
		diameter = 2 * radius
		area = math.pi * radius**2

		self.r = radius
		self.d = diameter
		self.C = circumference
		self.area = area

class Secant_Theorem():
	def __init__(self):
		pass

	def init_random(self):
		origin = analytic_geometry_engine.Point()
		origin.init_define(0,0)
		radius = random.randint(1,5)
		circle = analytic_geometry_engine.Circle()
		circle.init_define(origin, radius)

		point_p = analytic_geometry_engine.Point()
		point_p.init_define(random.randint(radius + 1, 2*radius), 0)

		point_a = analytic_geometry_engine.Point()
		point_a.init_define(0, round(random.uniform(0, radius), 2))

		point_b = analytic_geometry_engine.Point()
		point_b.init_define(0, -round(random.randint(0, radius), 2))

		line_1 = analytic_geometry_engine.Line()
		line_1.init_two_points(point_p, point_a)

		line_2 = analytic_geometry_engine.Line()
		line_2.init_two_points(point_p, point_b)

		print('circle ', circle.equation)
		print('line_1 ', line_1.equation)
		print('line_2 ', line_2.equation)

		points_above = sympy.nonlinsolve([circle.equation, line_1.equation], [x, y])
		print('points_above', points_above)

		points_below = sympy.nonlinsolve([circle.equation, line_2.equation], [x, y])
		print('points_below ', points_below)

		PA = analytic_geometry_engine.Point()
		PA.init_define(points_above.args[0][0], points_above.args[0][1])

		PB = analytic_geometry_engine.Point()
		PB.init_define(points_above.args[1][0], points_above.args[1][1])

		PC = analytic_geometry_engine.Point()
		PC.init_define(points_below.args[0][0], points_below.args[0][1])

		PD = analytic_geometry_engine.Point()
		PD.init_define(points_below.args[1][0], points_below.args[1][1])

		self.points = [PA, PB, PC, PD, point_p]

		print('pa ', PA.string)
		print('pb ', PB.string)
		print('pc ', PC.string)
		print('pd ', PD.string)

		PA_dist = PA.distance(point_p)
		PB_dist = PB.distance(point_p)
		PC_dist = PC.distance(point_p)
		PD_dist = PD.distance(point_p)

		#keep PA > PB and PC > PD
		if PA_dist < PB_dist:
			PA_dist, PB_dist = PB_dist, PA_dist

		if PC_dist < PD_dist:
			PC_dist, PD_dist = PD_dist, PC_dist

		print('pa_distance', PA_dist)
		print('pb_distance', PB_dist)
		print('pc_distance', PC_dist)
		print('pd_distance', PD_dist)

		print('check_1' , round(PA_dist*PB_dist, 2) == round(PC_dist*PD_dist,2))

		angle = line_1.angle_to_line(line_2)
		print('angle ', angle.degrees)

		self.angle = angle

		self.PA = PA_dist
		self.PB = PB_dist
		self.PC = PC_dist
		self.PD = PD_dist



	def compute_quadrilateral(self):
		
		return trigonometry_engine.herons(self.points[0].distance(self.points[1]), self.points[1].distance(self.points[2]), self.points[2].distance(self.points[0])) + trigonometry_engine.herons(self.points[0].distance(self.points[2]), self.points[2].distance(self.points[3]), self.points[3].distance(self.points[0]))

class Cyclic_Quadrilateral():
	def __init__(self):
		pass

	def init_random(self):
		#https://en.wikipedia.org/wiki/Quadrilateral
		triangle_1 = trigonometry_engine.Triangle()
		triangle_2 = trigonometry_engine.Triangle()

		diagonal_1 = round(random.randint(1,100), 2)

		repeat = True

		while repeat:
			angle_A_1 = c.angle(random.randint(10,80), 'degrees')
			angle_C_1 = c.angle(random.randint(10,80), 'degrees')
			angle_A_2 = c.angle(random.randint(10,80), 'degrees')

			if angle_A_1.degrees + angle_A_2.degrees + angle_C_1.degrees < 180:
				repeat = False

		angle_C_2 = c.angle(180 - angle_A_1.degrees - angle_A_2.degrees - angle_C_1.degrees, 'degrees')

		triangle_1.init_define_ASA(angle_A_1.degrees, diagonal_1, angle_C_1.degrees)

		triangle_2.init_define_ASA(angle_A_2.degrees, diagonal_1, angle_C_2.degrees)

		angle_A = c.angle(angle_A_1.degrees + angle_A_2.degrees, 'degrees')
		angle_C = c.angle(angle_C_1.degrees + angle_C_2.degrees, 'degrees')

		angle_B = triangle_1.B
		angle_D = triangle_2.B

		side_a = triangle_1.c
		side_b = triangle_1.a
		side_c = triangle_2.a
		side_d = triangle_2.c

		print(side_a, side_b, side_c, side_d, angle_A.degrees, angle_B.degrees, angle_C.degrees, angle_D.degrees)

		print('check_1', side_a**2 + side_b**2 + side_c**2 > side_d**2 / 3)
		print('check_2', side_a**4 + side_b**4 + side_c**4 > side_d**4 / 27)
		print('check_3', round(angle_A.degrees + angle_B.degrees + angle_C.degrees + angle_D.degrees,2) == 360)

		area = triangle_1.area + triangle_2.area
		perimeter = side_a + side_b + side_c + side_d
		
		diagonal_1_repeat = math.sqrt(
			side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_B.radians)
			)

		print('check_4', round(diagonal_1_repeat, 2) == round(diagonal_1, 2))



		diagonal_2 = math.sqrt(
			side_a**2 + side_d**2 - 2 * side_a * side_d * math.cos(angle_A.radians)
			)

		print('check_5', round(diagonal_1 * diagonal_2,2) == round(side_a * side_c + side_b * side_d,2))

		radius = math.sqrt(
			(side_a * side_b + side_c * side_d)  * (side_a * side_c + side_b * side_d) * (side_a * side_d + side_b * side_c) 
			) / (4 * area)

		self.a = side_a
		self.b = side_b
		self.c = side_c
		self.d = side_d
		self.A = angle_A
		self.B = angle_B
		self.C = angle_C
		self.D = angle_D
		self.area = area
		self.perimeter = perimeter
		self.d1 = diagonal_1
		self.d2 = diagonal_2
		self.radius = radius


class Star():
	def __init__(self):
		pass

	def init_random(self):
		sides = random.randint(STAR_SIDE_MIN, STAR_SIDE_MAX)
		circumradius = random.randint(STAR_CIRCUMRADIUS_MIN, STAR_CIRCUMRADIUS_MAX)

		angle_A = c.angle(math.pi / sides)
		angle_B = c.angle(math.pi / (2 * sides))
		angle_C = c.angle(math.pi - angle_A.radians - angle_B.radians)

		S = circumradius * math.sin(angle_A.radians) / math.sin(angle_C.radians)

		area_t = (1/2) * circumradius * S * math.sin(angle_B.radians)
		area = 2 * sides * area_t

		self.sides = sides
		self.circumradius = circumradius
		self.area = area



class rgs_1():
	def __init__(self):
		regpol = Regular_Polygon()
		regpol.init_random()

		self.question = f"""The central circle has a {regpol.circumradius:4.4}-cm radius. {num2words(regpol.sides).capitalize()} equal smaller circles are to be arranged so that they are externally tangent to each other and the centers lie in the circumference of the central circle. What should be the radius in cm, of the smaller circle?"""
		self.answer = f"""{regpol.side/2:4.4} cm"""

class rgs_2():
	def __init__(self):
		circle_1 = Circle()
		circle_2 = Circle()
		circle_3 = Circle()

		circle_1.init_random()
		circle_2.init_random()
		circle_3.init_random()

		self.question = f"""Three circles C1, C2, and C3 are externally tangent to each other. Center-to-center distances are {circle_1.r + circle_2.r:4.4} cm, between C1 and C2, {circle_2.r + circle_3.r:4.4} cm between C2 and C3, and {circle_1.r + circle_3.r:4.4} cm between C1 and C3. Determine the total areas of the circles."""
		self.answer = f"""{round(circle_1.area + circle_2.area + circle_3.area,2)} cm^2"""

class rgs_3():
	def __init__(self):
		cq = Cyclic_Quadrilateral()
		cq.init_random()

		side_list = [cq.a, cq.b, cq.c, cq.d]

		area = math.pi * cq.radius**2

		self.question = f"""A cyclic quadrilateral has the sides AB = {round(side_list[0],2)} cm, BC = {round(side_list[1],2)} cm, CD = {round(side_list[2],2)} cm, and DA = {round(side_list[3], 2)} cm. Find the area of the circle."""
		self.answer = f"""{round(area,2)} cm2"""

class rgs_4():
	def __init__(self):

		st = Secant_Theorem()
		st.init_random()

		self.question = f"""The vertices A and B of a quadrilateral line on a circle and are collinear with an external point P. A secant is drawn to the circle intersecting at C and D. Angle BPC = {round(st.angle.degrees, 2)} degrees. If secants PA and PD have lengths of {round(st.PA, 2)} m and {round(st.PD, 2)} m, respectively and the external segment PB is {round(st.PB, 2)} m, determine the area of the quadrilateral ABCD."""
		self.answer = f"""{round(st.compute_quadrilateral(), 2)} m2"""

class rgs_5():
	def __init__(self):

		circle_1 = analytic_geometry_engine.Circle()
		circle_1.init_define(analytic_geometry_engine.ORIGIN, random.randint(1,5))

		circle_2 = analytic_geometry_engine.Circle()
		circle_2.init_define(analytic_geometry_engine.ORIGIN, random.randint(circle_1.radius + 1, circle_1.radius*2))

		point_a = analytic_geometry_engine.Point()
		point_a.init_define(0, circle_1.radius)

		line = analytic_geometry_engine.Line()
		line.init_point_slope(point_a, 0)

		points = sympy.nonlinsolve([line.equation, circle_2.equation], [x, y])

		print('points ', points)

		point_1 = analytic_geometry_engine.Point()
		point_1.init_define(points.args[0][0], points.args[0][1])

		point_2 = analytic_geometry_engine.Point()
		point_2.init_define(points.args[1][0], points.args[1][1])		

		print('point 1 ', point_1.string)
		print('point 2 ', point_2.string)

		distance = point_1.distance(point_2)

		self.question = f"""A border is formed by two concentric circles of different radii. If the length of the chord of the larger circle that is tangent to the smaller circle is {round(distance,2)} , find the area of the border."""
		self.answer = f"""{round(circle_2.area - circle_1.area, 2)}"""

class rgs_6():
	def __init__(self):
		rp = Regular_Polygon()
		rp.init_random()

		self.question = f"""Find the area of a regular {rp.name} whose side is {round(rp.side,4)} cm and apothem {round(rp.inradius, 4)} cm."""
		self.answer = f"""{round(rp.area, 4)} cm"""

class rgs_8():
	def __init__(self):
		circle_1 = analytic_geometry_engine.Circle()
		radius = random.randint(1,10)
		circle_1.init_define(analytic_geometry_engine.ORIGIN, radius)
		circle_2 = analytic_geometry_engine.Circle()
		circle_2.init_define(analytic_geometry_engine.ORIGIN, random.randint(circle_1.radius + 1, circle_1.radius * 2))
		
		area_percentage = c.percentage((circle_2.area - circle_1.area) / circle_2.area, 'decimal')

		self.question = f"""A circle with radius {round(circle_1.radius, 4)} has {round(area_percentage.percent,2)} % of its area removed by cutting of a border of uniform width. Find the width of the border."""
		self.answer = f"""{round(circle_2.radius - circle_1.radius,4)}"""

class rgs_9():
	def __init__(self):
		rp = Regular_Polygon()
		rp.init_random()

		self.question = f"""What is the measure of each interior angle of a regular {rp.name}?"""
		self.answer = f"""{round(rp.interior_angle.degrees, 2)} degrees"""

class rgs_10():
	def __init__(self):
		rp = Regular_Polygon()
		rp.init_random()

		self.question = f"""For a regular {rp.name}, find the number of degrees contained in each central angle."""
		self.answer = f"""{round(rp.central_angle.degrees,4)}"""

class rgs_12():
	def __init__(self):
		rh = Rhombus()
		rh.init_random()

		self.question = f"""The area of a rhombus is {round(rh.area,4)} m2. If one of its diagonals is {round(rh.d1,4)} m, find the length of the sides of the rhombus."""
		self.answer = f"""{round(rh.side,4)} m"""

class rgs_13():
	def __init__(self):
		rp = Regular_Polygon()
		rp.init_random()

		self.question = f"""Find the length of the side of a regular pentagon inscribed in a circle of a radius {round(rp.inradius,4)} cm"""
		self.answer = f"""{round(rp.side,4)} cm"""

class rgs_15():
	def __init__(self):
		p = Parallelogram()
		p.init_random()

		self.question = f"""One side of a parallelogram is {round(p.a, 4)} cm and its diagonals is {round(p.d1, 4)} cm and {round(p.d2, 4)} cm respectively. Find its area."""
		self.answer = f"""{round(p.area,4)} cm2"""

class rgs_16():
	def __init__(self):
		rp = Regular_Polygon()
		rp.init_random()

		self.question = f"""The sum of the interior angles of a polygon is {round(rp.sum_of_interior_angles.degrees, 2)} degrees. Find the number of sides."""
		self.answer = f"""{rp.sides}"""

class rgs_17():
	def __init__(self):
		rh = Rhombus()
		rh.init_random()

		self.question = f"""The lengths of the diagonals of a rhombus are {round(rh.d1, 4)} cm and {round(rh.d2, 4)} cm, respectively. Find the perimeter of the rhombus."""
		self.answer = f"""{round(rh.perimeter, 4)} cm"""

class rgs_18():
	def __init__(self):
		sides = random.randint(POLYGON_SIDE_MIN, POLYGON_SIDE_MAX)
		circle = analytic_geometry_engine.Circle()
		circle.init_random()

		large_rp = Regular_Polygon()
		large_rp.init_inradius(sides, circle.radius)
		small_rp = Regular_Polygon()
		small_rp.init_circumradius(sides, circle.radius)

		ratio = fractions.Fraction(small_rp.area/ large_rp.area).limit_denominator(100_000)

		self.question = f"""The ratio of the area of regular polygon inscribed in a circle to the area of the circumscribing regular polygon of the same number of side is {ratio.numerator}:{ratio.denominator}. Find the number of the sides."""
		self.answer = f"""{small_rp.sides}"""

class rgs_19():
	def __init__(self):
		base = random.randint(5,15)
		height = random.randint(base + 1, base * 2)

		line_1 = analytic_geometry_engine.Line()
		line_2 = analytic_geometry_engine.Line()
		D = analytic_geometry_engine.Point()
		D.init_define(0, 0)
		A = analytic_geometry_engine.Point()
		A.init_define(0, height)
		B = analytic_geometry_engine.Point()
		B.init_define(base, height)
		C = analytic_geometry_engine.Point()
		C.init_define(base, 0)

		line_1.init_two_points(A, D)
		line_2.init_two_points(C, B)

		print('line1 ', line_1.equation)
		print('line2 ', line_2.equation)

		diagonal = analytic_geometry_engine.Line()
		diagonal.init_two_points(A, C)

		print('diagonal ', diagonal.equation)

		p_diagonal = analytic_geometry_engine.Line()
		p_diagonal.init_point_slope(A.midpoint(C), diagonal.perpendicular())

		e_point = sympy.linsolve([line_1.equation, p_diagonal.equation], [x, y])
		print('epoints ', e_point)
		E = analytic_geometry_engine.Point()
		E.init_define(e_point.args[0][0], e_point.args[0][1])
		print('point E ', E.string)

		f_point = sympy.linsolve([line_2.equation, p_diagonal.equation], [x, y])
		print('fpoints ', f_point)
		F = analytic_geometry_engine.Point()
		F.init_define(f_point.args[0][0], f_point.args[0][1])
		print('point F ', F.string)

		fold = E.distance(F)

		self.question = f"""A rectangular ABCD which measures {base} x {height} units is folded once, perpendicular to the diagonal AC, so that the opposite vertices A and C coincide. Find the length of the fold."""
		self.answer = f"""{round(fold, 2)} units"""

class rgs_20():
	def __init__(self):
		circle_1 = analytic_geometry_engine.Circle()
		circle_2 = analytic_geometry_engine.Circle()
		diameter_1 = random.randint(5,15)
		diameter_2 = random.randint(diameter_1 * 2 + 1, 3*diameter_1)
		center_2 = analytic_geometry_engine.Point()
		center_2.init_define((diameter_2/ 2) - (diameter_1/2), 0)
		circle_1.init_define(analytic_geometry_engine.ORIGIN, diameter_1 / 2)
		circle_2.init_define(center_2, diameter_2 / 2)

		tangent_length = math.sqrt(
			(circle_2.radius - circle_1.radius)**2 - circle_1.radius**2)

		self.question = f"""The diameters of two circles are {round(circle_2.diameter,4)} and {round(circle_1.diameter, 4)}, respectively. What is the length of the tangent segment from the center of the larger circle to the smaller circle?"""
		self.answer = f"""{round(tangent_length, 4)}"""

class rgs_21():
	def __init__(self):
		radius_1 = ran.main(2500)
		radius_2 = radius_1 + ran.main(500)

		angle_1 = c.angle(ran.main(20), 'degrees')
		angle_2 = c.angle(angle_1.degrees + ran.main(5), 'degrees')

		arc_1 = radius_1 * angle_1.radians 
		arc_2 = radius_2 * angle_2.radians

		arc_total = arc_1 + arc_2

		self.question = f"""A reverse curve on a railroad track consists of two circular arcs. The central angle of one side is {round(angle_1.degrees, 2)} degrees with radius of {round(radius_1, 2)} feet, while the central angle of the other is {round(angle_2.degrees, 2)} degrees with radius {round(radius_2, 2)} feet. Find the total lengths of the two arcs."""
		self.answer = f"""{round(arc_total, 2)} feet"""

class rgs_22():
	def __init__(self):
		star = Star()
		star.init_random()


		self.question = f"""A regular {star.sides}-pointed star is inscribed in a circle with a diameter of {round(star.circumradius * 2, 4)} m. What is the area of the region inside the circle not covered by the star?"""
		self.answer = f"""{round(star.circumradius**2 * math.pi - star.area, 4)} m2"""

class rgs_23():
	def __init__(self):
		rp_small = Regular_Polygon()
		rp_large = Regular_Polygon()

		side_length = int(ran.main(10))
		sides = random.randint(4, 10)
		rp_small.init_side(sides, side_length)
		rp_large.init_side(sides, side_length + int(ran.main(10)))

		self.question = f"""A regular {rp_small.name} has sides of {round(rp_large.side, 4)} cm. An inner {rp_small.name} with sides {round(rp_small.side, 4)} cm is inside and concentric to the larger {rp_small.name}. Determine the area inside the larger {rp_small.name} but outside of the smaller pentagon."""
		self.answer = f"""{round(rp_large.area - rp_small.area, 4)} cm2"""

class rgs_24():
	def __init__(self):
		cq = Cyclic_Quadrilateral()
		cq.init_random()

		self.question = f"""A quadrilateral is inscribed in a circle having a radius of {round(cq.radius, 2)} cm. Three other sides are {round(cq.a, 2)} cm, {round(cq.b, 2)} cm, and {round(cq.c, 2)} cm respectively. Determine the length of the fourth side."""
		self.answer = f"""{round(cq.d, 2)} cm"""


class rgs_26():
	def __init__(self):
		repeat= True
		while repeat:
			base = random.randint(5,10)
			height = random.randint(base + 1, base*2)
			rope = random.randint(height + 1, max(2* height, 2*base))

			if rope > base and rope > height and (rope - base) < height and (rope - height) < base:
				repeat = False

		area = math.pi * rope**2 * (3/4) + math.pi * (rope - base)**2 /4 + math.pi * (rope - height)**2 / 4
		animal = random.choice(['goat', 'chicken', 'dog', 'pig', 'horse', 'sheep'])
		self.question = f"""A {animal} is tethered to a corner of a {base} m by {height} m shed by a {rope} m rope. What is the maximum area the {animal} can cover?"""
		self.answer = f"""{round(area, 2)} m^2"""


class rgs_27():
	def __init__(self):
		st = Secant_Theorem()
		st.init_random()

		self.question = f"""Two secants are to a circle from the same external point. If the external and internal segments of one secant is {round(st.PB, 2)} inches and {round(st.PA - st.PB, 2)} inches and the external segment of the other secant is {round(st.PD, 2)} inches, compute the length of the second secant."""
		self.answer = f"""{round(st.PC, 2)} inches"""

class rgs_28():
	def __init__(self):
		circle_1 = analytic_geometry_engine.Circle()
		circle_2 = analytic_geometry_engine.Circle()
		diameter_2 = random.randint(5,15)
		diameter_1 = random.randint(diameter_2 + 1, 2*diameter_2)

		center_2 = analytic_geometry_engine.Point()
		center_2.init_define((diameter_1/ 2) + (diameter_1/2), 0)
		circle_1.init_define(analytic_geometry_engine.ORIGIN, diameter_1 / 2)
		circle_2.init_define(center_2, diameter_2 / 2)

		length_tangent_segment = math.sqrt(
			(circle_1.radius + circle_2.radius)**2 - (circle_1.radius - circle_2.radius)**2
			)

		self.question = f"""Two circles with radii {circle_1.radius} m and {circle_2.radius} m are tangent to each other externally. What is the distance between the points of tangency of one of their common external tangents?"""
		self.answer = f"""{round(length_tangent_segment,2)} m"""

class rgs_29():
	def __init__(self):
		p = Parallelogram()
		p.init_random()

		self.question = f"""If the sides of a parallelogram and an included angle area {round(p.a, 2)}, {round(p.b, 2)} and {round(p.A.degrees, 2)} degrees respectively, find the length of the shorter diagonal."""
		self.answer = f"""{round(min(p.d1, p.d2),2)}"""

class rgs_30():
	def __init__(self):
		p = Parallelogram()
		p.init_random()

		self.question = f"""The sides of a parallelogram are {round(p.a, 2)} cm and {round(p.b, 2)} cm respectively. If one of its diagonals is {round(p.d1,2)} cm long, compute the smallest interior angle of the parallelogram."""
		self.answer = f"""{round(min(p.A.degrees, p.B.degrees),2)} degrees"""

class rgs_31():
	def __init__(self):
		rp_1 = Regular_Polygon()
		rp_2 = Regular_Polygon()

		rp_1.init_random()
		rp_2.init_random()

		sum_of_sides = rp_1.sides + rp_2.sides
		sum_of_diagonals = rp_1.diagonals + rp_2.diagonals

		self.question = f"""The sum of the sides of two polygons is {sum_of_sides} and the sum of their diagonals is {sum_of_diagonals}. Find the number of sides of the polygon with smaller number of sides."""
		self.answer = f"""{min(rp_1.sides, rp_2.sides)}"""

class rgs_32():
	def __init__(self):
		radius = random.randint(5,15)
		distance = random.randint(radius + 1, 2 * radius)
		tangent = math.sqrt(
			distance**2 - radius**2
			)
		self.question = f"""Tangents are drawn to a circle of radius {radius} cm from a point {distance} cm from its center. Find the length of each tangent."""
		self.answer = f"""{round(tangent, 2)} cm"""

class rgs_33():
	def __init__(self):
		tr = trigonometry_engine.Triangle()
		tr.init_random()
		radius_circumscribing = tr.circumradius()

		self.question = f"""Find the radius of the circle circumscribing a triangle with side lengths {round(tr.a, 2)} cm, {round(tr.b, 2)} cm, and {round(tr.c, 2)} cm."""

		self.answer = f"""{round(radius_circumscribing, 2)} cm"""

class rgs_34():
	def __init__(self):
		tr = trigonometry_engine.Triangle()
		tr.init_random()
		radius_circumscribing = tr.circumradius()

		self.question = f"""The sides of the triangle are {round(tr.a, 2)} cm, {round(tr.b, 2)} cm, and {round(tr.c, 2)} cm. How far is the point of intersection of the perpendicular bisectors of the sides of the triangle to any of its vertices?"""
		self.answer = f"""{round(tr.circumradius(), 2)} cm"""

class rgs_35():
	def __init__(self):
		tr = trigonometry_engine.Triangle()
		tr.init_random()

		self.question = f"""A triangle has sides equal to {round(tr.a, 2)} cm, {round(tr.b, 2)} cm, and {round(tr.c, 2)} cm, respectively. Find the area of the escribed circle tangent to the shortest side of the triangle."""
		self.answer = f"""{round(tr.exradius('smallest')**2 * math.pi, 2)} cm^2"""

class rgs_36():
	def __init__(self):
		q = Quadrilateral()
		q.init_random()

		self.question = f"""A quadrilateral has sides equal to {round(q.a, 2)} cm, {round(q.b, 2)} cm, {round(q.c, 2)} cm and {round(q.d, 2)} cm respectively. If the sum of the two opposite angles is {round(q.A.degrees + q.C.degrees, 2)} degrees, find the area of the quadrilateral."""
		self.answer= f"""{round(q.area, 2)} cm^2"""

class rgs_37():
	def __init__(self):
		rp = Regular_Polygon()
		rp.init_random()

		self.question = f"""How many diagonals can be drawn from a {rp.sides}-sided polygon?"""
		self.answer = f"""{rp.diagonals}"""


































