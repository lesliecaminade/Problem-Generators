import random
from mathsub import vectors_engine as engine
from num2words import num2words

def ask():
	ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
	return random.choice(ask_words)

def parse(string_input):
	return string_input.replace('**', '^').replace('*', ' ')


class Constructor():
	def __init__(self, engine_class_instances):
		#Battery - a single instance of a set of givens, and an answer for a certain problem

		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):

			#battery = engine.Some_class_from_engine
			battery = engine_class_instances[i]

			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.answer)

			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = main.question
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 


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

class Angle_between_two_vectors():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Angle_between_two_vectors()
				#edit above 
			BATTERIES.append(battery)
			CHOICES.append(str(round(battery.angle.degrees, 2)) + ' degrees') 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Find the angle between the vectors {main.vector_1.print()} and {main.vector_2.print()}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Orthogonal_vectors():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Orthogonal_vectors()
				#edit above 
			BATTERIES.append(battery)
			CHOICES.append(round(battery.vector_2.z,2)) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""If the two vectors {main.vector_1.print()} and {main.vector_2.print(hide = 'z')} are orthogonal, determine the value of z."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""			

class Component_of_a_vector():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Component_of_a_vector()			
			#edit above 
			BATTERIES.append(battery)
			CHOICES.append(round(battery.component,2)) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Determine the component of the vector {main.vector_1.print()} onto {main.vector_2.print()}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Projection_of_a_vector():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Projection_of_a_vector()			
			#edit above 
			BATTERIES.append(battery)
			CHOICES.append(battery.projection.round().print()) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Determine the projection of the vector {main.vector_1.print()} onto {main.vector_2.print()}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Scalar_triple_product():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Scalar_triple_product()			
			#edit above 
			BATTERIES.append(battery)
			CHOICES.append(round(battery.scalar_triple_product,2)) 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the scalar triple product of the vectors {main.vector_1.print()}, {main.vector_2.print()}, and {main.vector_3.print()}"""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Volume_of_parallelipiped():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		for i in range(4):
			battery = engine.Scalar_triple_product()			
			#edit above 
			BATTERIES.append(battery)
			CHOICES.append(str(abs(round(battery.scalar_triple_product,2))) + ' units^3') 
			#edit above
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the volume of the parallelipiped formed by the three vectors {main.vector_1.print()}, {main.vector_2.print()}, and {main.vector_3.print()}"""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Vector_triple_product():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Vector_triple_product()
			#data = battery.Some_attribute_from_battery			
			data =  battery.vector_triple_product.round().print()
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Find the vector triple product (A x ( B x C )) if vectors A, B, and C are {main.vector_1.print()}, {main.vector_2.print()}, and {main.vector_3.print()} respectively."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Gradient_of_a_scalar():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Gradient_of_a_scalar()
			#data = battery.Some_attribute_from_battery			
			data =  parse(battery.gradient.print())
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Determine the gradient of the scalar field {main.scalar_1.print()} """

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Divergence_of_a_vector():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Divergence_of_a_vector()
			#data = battery.Some_attribute_from_battery			
			data =  parse(str(battery.divergence))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Determine the divergence of the vector field {parse(main.vector.print())} """

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""		

class Curl_of_a_vector():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Curl_of_a_vector()
			#data = battery.Some_attribute_from_battery			
			data =  parse(str(battery.curl.print()))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""Determine the curl of the vector field {parse(main.vector.print())} """

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Point_Conversion():
	def __init__(self):
		instance_list = [
		engine.Point_Conversion(),        
		engine.Point_Conversion(),
		engine.Point_Conversion(),
		engine.Point_Conversion()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  