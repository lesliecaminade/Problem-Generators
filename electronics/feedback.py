import random
from electronics import feedback_engine as engine
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
		
class floyd_16_1():
	def __init__(self):
		instance_list = [
		engine.floyd_16_1(),        
		engine.floyd_16_1(),
		engine.floyd_16_1(),
		engine.floyd_16_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_16_2():
	def __init__(self):
		instance_list = [
		engine.floyd_16_2(),        
		engine.floyd_16_2(),
		engine.floyd_16_2(),
		engine.floyd_16_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_16_2_b():
	def __init__(self):
		instance_list = [
		engine.floyd_16_2_b(),        
		engine.floyd_16_2_b(),
		engine.floyd_16_2_b(),
		engine.floyd_16_2_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_16_3():
	def __init__(self):
		instance_list = [
		engine.floyd_16_3(),        
		engine.floyd_16_3(),
		engine.floyd_16_3(),
		engine.floyd_16_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_16_4():
	def __init__(self):
		instance_list = [
		engine.floyd_16_4(),        
		engine.floyd_16_4(),
		engine.floyd_16_4(),
		engine.floyd_16_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_16_6():
	def __init__(self):
		instance_list = [
		engine.floyd_16_6(),        
		engine.floyd_16_6(),
		engine.floyd_16_6(),
		engine.floyd_16_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class no_reference_1():
	def __init__(self):
		instance_list = [
		engine.no_reference_1(),        
		engine.no_reference_1(),
		engine.no_reference_1(),
		engine.no_reference_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class no_reference_2():
	def __init__(self):
		instance_list = [
		engine.no_reference_2(),        
		engine.no_reference_2(),
		engine.no_reference_2(),
		engine.no_reference_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class no_reference_3():
	def __init__(self):
		instance_list = [
		engine.no_reference_3(),        
		engine.no_reference_3(),
		engine.no_reference_3(),
		engine.no_reference_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		