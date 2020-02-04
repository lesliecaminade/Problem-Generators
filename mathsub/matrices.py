import random
from mathsub import matrices_engine as engine
from num2words import num2words


def ask():
	ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
	return random.choice(ask_words)

def parse(string_input):
	string_input = str(string_input)
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
		
class Addition():
	def __init__(self):
		instance_list = [
		engine.Addition(),        
		engine.Addition(),
		engine.Addition(),
		engine.Addition()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Multiplication():
	def __init__(self):
		instance_list = [
		engine.Multiplication(),        
		engine.Multiplication(),
		engine.Multiplication(),
		engine.Multiplication()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Transpose():
	def __init__(self):
		instance_list = [
		engine.Transpose(),        
		engine.Transpose(),
		engine.Transpose(),
		engine.Transpose()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Submatrix():
	def __init__(self):
		instance_list = [
		engine.Submatrix(),        
		engine.Submatrix(),
		engine.Submatrix(),
		engine.Submatrix()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Minor():
	def __init__(self):
		instance_list = [
		engine.Minor(),        
		engine.Minor(),
		engine.Minor(),
		engine.Minor()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Cofactor():
	def __init__(self):
		instance_list = [
		engine.Cofactor(),        
		engine.Cofactor(),
		engine.Cofactor(),
		engine.Cofactor()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Cofactor_Matrix():
	def __init__(self):
		instance_list = [
		engine.Cofactor_Matrix(),        
		engine.Cofactor_Matrix(),
		engine.Cofactor_Matrix(),
		engine.Cofactor_Matrix()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Adjugate():
	def __init__(self):
		instance_list = [
		engine.Adjugate(),        
		engine.Adjugate(),
		engine.Adjugate(),
		engine.Adjugate()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Determinant():
	def __init__(self):
		instance_list = [
		engine.Determinant(),        
		engine.Determinant(),
		engine.Determinant(),
		engine.Determinant()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Inverse():
	def __init__(self):
		instance_list = [
		engine.Inverse(),        
		engine.Inverse(),
		engine.Inverse(),
		engine.Inverse()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class Row_Echelon_Form():
	def __init__(self):
		instance_list = [
		engine.Row_Echelon_Form(),        
		engine.Row_Echelon_Form(),
		engine.Row_Echelon_Form(),
		engine.Row_Echelon_Form()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		