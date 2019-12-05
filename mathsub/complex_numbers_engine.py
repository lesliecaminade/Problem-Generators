from generator import random_handler as ran
import math
import random
from generator import constants_conversions as c
import cmath

POW_MAX = 5
COE_MAX = 10

def coe():
	return random.randint(-COE_MAX, COE_MAX)
	
def random_complex():
	real = 0
	im = 0
	while real == 0 and im == 0:
		real = coe()
		im = coe()
	return complex(real, im)

def pow():
	return random.randint(2, POW_MAX)

def round_off(argument, **kwargs):
	places = 2
	for key, value in kwargs.items():
		if key == 'places':
			places = value

	return complex(round(argument.real,places), round(argument.imag,places))

class Complex_raised_to_positive_integer():
	def __init__(self):
		self.base = random_complex()
		self.power = pow()
		self.solution = self.base ** self.power
		self.solution = round_off(self.solution)

class Complex_root_to_positive_integer():
	def __init__(self):
		self.base = random_complex()
		self.power = 1/pow()
		self.solution = self.base ** self.power
		self.solution = round_off(self.solution)

class Complex_raised_to_complex():
	def __init__(self):
		self.base = random_complex()
		self.power = random_complex()
		self.solution = self.base ** self.power
		self.solution = round_off(self.solution)

class Natural_logarithm_of_complex():
	def __init__(self):
		self.antilogarithm = random_complex()
		self.logarithm = cmath.log(self.antilogarithm)
		self.base = math.exp
		self.logarithm = round_off(self.logarithm)

class Logarithm_to_the_positive_integer_base_of_complex():
	def __init__(self):
		self.antilogarithm = random_complex()
		self.base = random.randint(2,10)
		self.logarithm = cmath.log(self.antilogarithm, self.base)
		self.logarithm = round_off(self.logarithm)

class Logarithm_to_the_base_of_complex_number_complex():
	def __init__(self):
		self.antilogarithm = random_complex()
		self.base = random_complex()
		self.logarithm = cmath.log(self.antilogarithm, self.base)
		self.logarithm = round_off(self.logarithm)

class Sine_of_a_complex_number():
	def __init__(self):
		self.argument = random_complex()
		self.angle = cmath.sin(self.argument)
		self.angle = round_off(self.angle)

class Cosine_of_a_complex_number():
	def __init__(self):
		self.argument = random_complex()
		self.angle = cmath.cos(self.argument)
		self.angle = round_off(self.angle)

class Trigonometric_value_of_a_complex_number():
	def __init__(self):

		TRIGOS = ['tangent', 'cotangent', 'secant', 'cosecant']
		self.trigo = random.choice(TRIGOS)
		self.argument = random_complex()

		if self.trigo == TRIGOS[0]:
			self.angle = cmath.tan(self.argument)
		elif self.trigo == TRIGOS[1]:
			self.angle = 1/cmath.tan(self.argument)
		elif self.trigo == TRIGOS[2]:
			self.angle = 1/cmath.cos(self.argument)
		elif self.trigo == TRIGOS[3]:
			self.angle = 1/cmath.sin(self.argument)
		self.angle = round_off(self.angle, places = 8)	













































































































        




























































