import random
from mathsub import vectors_engine as engine
from num2words import num2words

class Vector_add_Vector_add_Vector():
	def __init__(self):

		main = engine.Vector_add_vector_add_vector()
		distractor_1 = engine.Vector_add_vector_add_vector()
		distractor_2 = engine.Vector_add_vector_add_vector()
		distractor_3 = engine.Vector_add_vector_add_vector()


		choice_a = str(main.resultant.print()) + ' #'
		choice_b = str(distractor_1.resultant.print())
		choice_c = str(distractor_2.resultant.print())
		choice_d = str(distractor_3.resultant.print())

		CHOICES = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(CHOICES)

		self.question = f"""Determine the resultant of the vectors {main.vector_1.print()}, {main.vector_2.print()}, and {main.vector_3.print()}."""
	
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Dot_product():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Dot_product() #edit this
			BATTERIES.append(battery)
			if i == 0:
				
				CHOICES.append(str(battery.dot) + ' #') #edit this
			else:
				
				CHOICES.append(battery.dot) #edit this

		main = BATTERIES[0]
		random.shuffle(CHOICES)
		#edit this
		self.question = f"""Determine the dot product of the vectors {main.vector_1.print()} and {main.vector_2.print()}."""


		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Unit_vector_parallel_to_a_vector():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Unit_vector_parallel_to_a_vector() #edit this
			BATTERIES.append(battery)
			if i == 0:
				
				CHOICES.append(str(battery.unit_vector.round().print()) + ' #') #edit this
			else:
				
				CHOICES.append(battery.unit_vector.round().print()) #edit this

		main = BATTERIES[0]
		random.shuffle(CHOICES)
		#edit this
		self.question = f"""Find a unit vector parallel to the vector {main.vector_1.print()}."""


		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""


class Unit_vector_parallel_to_a_vector_with_magnitude():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Unit_vector_parallel_to_a_vector_with_magnitude() #edit this
			BATTERIES.append(battery)
			if i == 0:
				
				CHOICES.append(str(battery.resultant.round().print()) + ' #') #edit this
			else:
				
				CHOICES.append(battery.resultant.round().print()) #edit this

		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit this
		self.question = f"""Find a vector parallel to the vector {main.vector_1.print()} and has a length of {main.length}."""


		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Cross_product():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Cross_product()
				#edit above 
			BATTERIES.append(battery)
			CHOICES.append(battery.cross_product.round().print()) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Find the cross product of the vectors {main.vector_1.print()} and {main.vector_2.print()} respectively."""


		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Unit_vector_perpendicular_to_two_vectors():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Unit_vector_perpendicular_to_two_vectors()
				#edit above 
			BATTERIES.append(battery)
			CHOICES.append(battery.cross_product_unit_vector.round().print()) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Find a unit vector perpendicular to both vectors {main.vector_1.print()} and {main.vector_2.print()}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Unit_vector_perpendicular_to_two_vectors_with_magnitude():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Unit_vector_perpendicular_to_two_vectors_with_magnitude()
				#edit above 
			BATTERIES.append(battery)
			CHOICES.append(battery.vector_3.round().print()) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Find a unit vector perpendicular to both vectors {main.vector_1.print()} and {main.vector_2.print()} with a magnitude of {main.magnitude}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		