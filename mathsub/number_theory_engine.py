from generator import random_handler as ran
import sympy
import math
import random
from generator import constants_conversions as c
from num2words import num2words
import fractions


from functools import reduce
from fractions import gcd
from mathsub import algebra_engine


COE_RANGE = 10
MAX_TERMS = 5

def lcm(a, b):
    return a * b / gcd(a, b)

def lcms(*numbers):
 	return reduce(lcm, numbers)

def gcds(*numbers):
 	return reduce(gcd, numbers)

def parse(expression):
	expression = str(expression)
	return expression.replace("**", "^").replace("*", "" "")

x, y, z = sympy.symbols('x y z', real = True)#generic variables

def find_sigfigs(x):
	'''Returns the number of significant digits in a number. This takes into account
	   strings formatted in 1.23e+3 format and even strings such as 123.450'''
	# change all the 'E' to 'e'
	x = x.lower()
	if ('e' in x):
		# return the length of the numbers before the 'e'
		myStr = x.split('e')
		return len( myStr[0] ) - 1 # to compenstate for the decimal point
	else:
		# put it in e format and return the result of that
		### NOTE: because of the 8 below, it may do crazy things when it parses 9 sigfigs
		
		n = ('%.*e' %(8, float(x))).split('e')
		# remove and count the number of removed user added zeroes. (these are sig figs)
		if '.' in x:
			s = x.replace('.', '')
			#number of zeroes to add back in
			l = len(s) - len(s.rstrip('0'))
			#strip off the python added zeroes and add back in the ones the user added
			n[0] = n[0].rstrip('0') + ''.join(['0' for num in xrange(l)])
		else:
			#the user had no trailing zeroes so just strip them all
			n[0] = n[0].rstrip('0')
		#pass it back to the beginning to be parsed
	return find_sigfigs('e'.join(n))

def pick_num():
	return random.randint(1, 100)

def pick_coe():
	return random.randint(-COE_RANGE, COE_RANGE)


class Remainder_Theorem():
	def __init__(self):
		dividend = algebra_engine.Polynomial()
		dividend.init_random()

		c = pick_coe()
		divisor = algebra_engine.Linear()
		divisor.init_random()

		remainder = dividend.expression.subs(x, divisor.root())

		self.dividend = parse(dividend.expression)
		self.divisor = parse(divisor.expression)
		self.remainder = fractions.Fraction(float(remainder)).limit_denominator(1000)
		self.c = fractions.Fraction(divisor.root()).limit_denominator(1000)

def sign_alternations(array):

		def pos(num):
			if num >= 0:
				return True
			else:
				return False

		alternations = 0
		previous_pos = pos(array[0])

		for i in range(1, len(array)):
			now_pos = pos(array[i])
			if not(previous_pos == now_pos):
				alternations = alternations + 1
			previous_pos = now_pos

		return alternations

class Descartes_Rule_Of_Signs():
	def __init__(self):
		polynomial = algebra_engine.Polynomial()
		polynomial.init_random()

		f_x = polynomial.expression
		f_nx = polynomial.expression.subs(x, -x)

		pfx = sympy.Poly(f_x)
		pfnx = sympy.Poly(f_nx)

		coeff_p = pfx.all_coeffs()
		coeff_n = pfnx.all_coeffs()
		# print(polynomial.expression)
		# print(coeff_p)
		# print(coeff_n)

		# print(sign_alternations(coeff_p))
		# print(sign_alternations(coeff_n))

		sp = sign_alternations(coeff_p)
		sn = sign_alternations(coeff_n)

		possible_proots = []
		possible_nroots = []

		while sp >= 0:
			possible_proots.append(sp)
			sp  = sp - 2 

		while sn >= 0:
			possible_nroots.append(sn)
			sn = sn - 2

		# print(possible_proots)
		# print(possible_nroots)

		def roots_to_string(roots):

			output = str(roots[0])

			if len(roots) > 1:
				for i in range(1, len(roots)):
					output = output + ' or ' + str(roots[i])

			return output 

		self.polynomial = parse(polynomial.expression) + ' = 0'
		self.positive_roots = roots_to_string(possible_proots)
		self.negative_roots = roots_to_string(possible_nroots)
		# print(self.positive_roots)
		# print(self.negative_roots)

class remainder_1():
	def __init__(self):
		rt = Remainder_Theorem()
		self.question = f"""When {rt.dividend} is divided by x - k, the remainder is {int(rt.remainder)}. Find the value of k."""
		self.answer = f"""{rt.c}"""

class remainder_2():
	def __init__(self):
		rt = Remainder_Theorem()
		self.question = f"""Find the remainder when {rt.dividend} is divided by {rt.divisor}."""
		self.answer = f"""{rt.remainder}"""

class descartes_1():
	def __init__(self):
		dros = Descartes_Rule_Of_Signs()
		self.question = f"""How many positive roots are possible for the polynomial {dros.polynomial} by the Descartes' rule of signs?"""
		self.answer = f"""{dros.positive_roots}"""

class descartes_2():
	def __init__(self):
		dros = Descartes_Rule_Of_Signs()
		self.question = f"""How many negative roots are possible for the polynomial {dros.polynomial} by the Descartes' rule of signs?"""
		self.answer = f"""{dros.negative_roots}"""

class fibonacci_1:
	def __init__(self,*args,**kwargs): 
		n = random.randint(20,100)
		self.question = f"""Determine {num2words(n, to = 'ordinal_num')} term of the Fibonnaci sequence."""
		fn = (1 / math.sqrt(5)) * ( ((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5)) / 2)**n )
		self.answer = f"""{fn:4.4}"""
			
class lucas_1:
	def __init__(self,*args,**kwargs): 
		n = random.randint(20,100)
		self.question = f"""Determine {num2words(n, to = 'ordinal_num')} term of the Lucas sequence."""
		ln = ((1+math.sqrt(5))/2)**n + ((1-math.sqrt(5)) / 2)**n 
		self.answer = f"""{ln:4.4}"""
		
 
class digits_base_exponent:
	def __init__(self,*args,**kwargs): 
		base = random.randint(10, 100)
		exponent = random.randint(10, 100)
		self.question = f"""Determine the number of digits of the number {base}^{exponent}."""
		
		digits = 1 + math.floor( exponent * math.log( base, 10 )  )
		self.answer = f"""{digits}"""
		
class digits_factorial:
	def __init__(self,*args,**kwargs): 
		number = random.randint(50,300)
		self.question = f"""Determine the number of digits {number}!."""
		digits = 1 + math.floor(
		math.log(math.sqrt(2 * math.pi * 100), 10) + number * math.log(number/math.exp(1), 10))
		self.answer = f"""{digits}"""
		
class trailing_zeroes_1:
	def __init__(self,*args,**kwargs): 
		number = random.randint(50,300)
		self.question = f"""Determine the number of trailing zeroes of {number}!."""
		zeros = 0
		for i in range(10):
			zeros = zeros + math.floor(number/5**i)
		self.answer = f"""{zeros}"""

class gcd_1():
	def __init__(self):
		num_1 = pick_num()
		num_2 = pick_num()
		num_3 = pick_num()
		gcd = gcds(num_1, num_2, num_3)
		self.question = f"""Determine the greatest common divisor of the numbers {num_1}, {num_2}, and {num_3}."""
		self.answer = f"""{int(gcd)}"""

class lcm_1():
	def __init__(self):
		num_1 = pick_num()
		num_2 = pick_num()
		num_3 = pick_num()
		lcm = lcms(num_1, num_2, num_3)
		self.question = f"""Determine the least common multiple of the numbers {num_1}, {num_2}, and {num_3}."""
		self.answer = f"""{int(lcm)}"""



		
		
		
		
		
		
		
		
		
		
		
		
		
		