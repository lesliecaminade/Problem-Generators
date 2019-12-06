import random
from mathsub import complex_numbers_engine as engine
from num2words import num2words

class Complex_number_raised_to_positive_integer():
	def __init__(self):

		main = engine.Complex_raised_to_positive_integer()
		distractor_1 = engine.Complex_raised_to_positive_integer()
		distractor_2 = engine.Complex_raised_to_positive_integer()
		distractor_3 = engine.Complex_raised_to_positive_integer()


		choice_a = str(main.solution) + ' #'
		choice_b = str(distractor_1.solution)
		choice_c = str(distractor_2.solution)
		choice_d = str(distractor_3.solution)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(CHOICES)

		self.question = f"""Calculate the value of the complex number {main.base} when it is raised to the power of {main.power}."""
	
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""


class Complex_number_root_to_positive_integer():
	def __init__(self):

		main = engine.Complex_root_to_positive_integer()
		distractor_1 = engine.Complex_root_to_positive_integer()
		distractor_2 = engine.Complex_root_to_positive_integer()
		distractor_3 = engine.Complex_root_to_positive_integer()


		choice_a = str(main.solution) + ' #'
		choice_b = str(distractor_1.solution)
		choice_c = str(distractor_2.solution)
		choice_d = str(distractor_3.solution)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the value of the complex number {main.base} when its principal {num2words(int(1/main.power), to='ordinal')} root is taken."""
	
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Complex_number_raised_to_complex_number():
	def __init__(self):

		main = engine.Complex_raised_to_complex()
		distractor_1 = engine.Complex_raised_to_complex()
		distractor_2 = engine.Complex_raised_to_complex()
		distractor_3 = engine.Complex_raised_to_complex()


		choice_a = str(main.solution) + ' #'
		choice_b = str(distractor_1.solution)
		choice_c = str(distractor_2.solution)
		choice_d = str(distractor_3.solution)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the value of the complex number {main.base} when raised to the power of {main.power}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Natural_logarithm_of_complex():
	def __init__(self):

		main = engine.Natural_logarithm_of_complex()
		distractor_1 = engine.Natural_logarithm_of_complex()
		distractor_2 = engine.Natural_logarithm_of_complex()
		distractor_3 = engine.Natural_logarithm_of_complex()


		choice_a = str(main.logarithm) + ' #'
		choice_b = str(distractor_1.logarithm)
		choice_c = str(distractor_2.logarithm)
		choice_d = str(distractor_3.logarithm)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the natural logarithm of the complex number {main.antilogarithm}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Logarithm_to_the_positive_integer_base_of_complex():
	def __init__(self):

		main = engine.Logarithm_to_the_positive_integer_base_of_complex()
		distractor_1 = engine.Logarithm_to_the_positive_integer_base_of_complex()
		distractor_2 = engine.Logarithm_to_the_positive_integer_base_of_complex()
		distractor_3 = engine.Logarithm_to_the_positive_integer_base_of_complex()


		choice_a = str(main.logarithm) + ' #'
		choice_b = str(distractor_1.logarithm)
		choice_c = str(distractor_2.logarithm)
		choice_d = str(distractor_3.logarithm)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the logarithm of the complex number {main.antilogarithm} to the base of {main.base}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		


class Logarithm_to_the_base_of_complex_number_complex():
	def __init__(self):

		main = engine.Logarithm_to_the_base_of_complex_number_complex()
		distractor_1 = engine.Logarithm_to_the_base_of_complex_number_complex()
		distractor_2 = engine.Logarithm_to_the_base_of_complex_number_complex()
		distractor_3 = engine.Logarithm_to_the_base_of_complex_number_complex()


		choice_a = str(main.logarithm) + ' #'
		choice_b = str(distractor_1.logarithm)
		choice_c = str(distractor_2.logarithm)
		choice_d = str(distractor_3.logarithm)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the logarithm of the complex number {main.antilogarithm} to the base of {main.base}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Sine_of_a_complex_number():
	def __init__(self):

		main = engine.Sine_of_a_complex_number()
		distractor_1 = engine.Sine_of_a_complex_number()
		distractor_2 = engine.Sine_of_a_complex_number()
		distractor_3 = engine.Sine_of_a_complex_number()


		choice_a = str(main.angle) + ' #'
		choice_b = str(distractor_1.angle)
		choice_c = str(distractor_2.angle)
		choice_d = str(distractor_3.angle)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the sine of the complex number {main.argument}"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Cosine_of_a_complex_number():
	def __init__(self):

		main = engine.Cosine_of_a_complex_number()
		distractor_1 = engine.Cosine_of_a_complex_number()
		distractor_2 = engine.Cosine_of_a_complex_number()
		distractor_3 = engine.Cosine_of_a_complex_number()


		choice_a = str(main.angle) + ' #'
		choice_b = str(distractor_1.angle)
		choice_c = str(distractor_2.angle)
		choice_d = str(distractor_3.angle)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the cosine of the complex number {main.argument}"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Trigonometric_value_of_a_complex_number():
	def __init__(self):

		main = engine.Trigonometric_value_of_a_complex_number()
		distractor_1 = engine.Trigonometric_value_of_a_complex_number()
		distractor_2 = engine.Trigonometric_value_of_a_complex_number()
		distractor_3 = engine.Trigonometric_value_of_a_complex_number()


		choice_a = str(main.angle) + ' #'
		choice_b = str(distractor_1.angle)
		choice_c = str(distractor_2.angle)
		choice_d = str(distractor_3.angle)

		CHOICES = [choice_a, choice_b, choice_c, choice_d]

		
		self.question = f"""Calculate the {main.trigo} of the complex number {main.argument}"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	





























































































        




























































