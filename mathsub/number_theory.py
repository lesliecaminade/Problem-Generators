import random
from mathsub import number_theory_engine as engine
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
		
class remainder_1():
	def __init__(self):
		instance_list = [
		engine.remainder_1(),        
		engine.remainder_1(),
		engine.remainder_1(),
		engine.remainder_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class remainder_2():
	def __init__(self):
		instance_list = [
		engine.remainder_2(),        
		engine.remainder_2(),
		engine.remainder_2(),
		engine.remainder_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class descartes_1():
	def __init__(self):
		instance_list = [
		engine.descartes_1(),        
		engine.descartes_1(),
		engine.descartes_1(),
		engine.descartes_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class descartes_2():
	def __init__(self):
		instance_list = [
		engine.descartes_2(),        
		engine.descartes_2(),
		engine.descartes_2(),
		engine.descartes_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fibonacci_1():
	def __init__(self):
		instance_list = [
		engine.fibonacci_1(),        
		engine.fibonacci_1(),
		engine.fibonacci_1(),
		engine.fibonacci_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class lucas_1():
	def __init__(self):
		instance_list = [
		engine.lucas_1(),        
		engine.lucas_1(),
		engine.lucas_1(),
		engine.lucas_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class digits_base_exponent():
	def __init__(self):
		instance_list = [
		engine.digits_base_exponent(),        
		engine.digits_base_exponent(),
		engine.digits_base_exponent(),
		engine.digits_base_exponent()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class digits_factorial():
	def __init__(self):
		instance_list = [
		engine.digits_factorial(),        
		engine.digits_factorial(),
		engine.digits_factorial(),
		engine.digits_factorial()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class trailing_zeroes_1():
	def __init__(self):
		instance_list = [
		engine.trailing_zeroes_1(),        
		engine.trailing_zeroes_1(),
		engine.trailing_zeroes_1(),
		engine.trailing_zeroes_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class gcd_1():
	def __init__(self):
		instance_list = [
		engine.gcd_1(),        
		engine.gcd_1(),
		engine.gcd_1(),
		engine.gcd_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class lcm_1():
	def __init__(self):
		instance_list = [
		engine.lcm_1(),        
		engine.lcm_1(),
		engine.lcm_1(),
		engine.lcm_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  
		


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		