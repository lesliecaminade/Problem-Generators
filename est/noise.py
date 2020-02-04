import random
from est import noise_engine as engine
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

class jma_1_95():
	def __init__(self):
		instance_list = [
		engine.jma_1_95(),        
		engine.jma_1_95(),
		engine.jma_1_95(),
		engine.jma_1_95()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_98():
	def __init__(self):
		instance_list = [
		engine.jma_1_98(),        
		engine.jma_1_98(),
		engine.jma_1_98(),
		engine.jma_1_98()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_99_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_99_a(),        
		engine.jma_1_99_a(),
		engine.jma_1_99_a(),
		engine.jma_1_99_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_99_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_99_b(),        
		engine.jma_1_99_b(),
		engine.jma_1_99_b(),
		engine.jma_1_99_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_100():
	def __init__(self):
		instance_list = [
		engine.jma_1_100(),        
		engine.jma_1_100(),
		engine.jma_1_100(),
		engine.jma_1_100()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_102_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_102_a(),        
		engine.jma_1_102_a(),
		engine.jma_1_102_a(),
		engine.jma_1_102_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_102_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_102_b(),        
		engine.jma_1_102_b(),
		engine.jma_1_102_b(),
		engine.jma_1_102_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_104():
	def __init__(self):
		instance_list = [
		engine.jma_1_104(),        
		engine.jma_1_104(),
		engine.jma_1_104(),
		engine.jma_1_104()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_105():
	def __init__(self):
		instance_list = [
		engine.jma_1_105(),        
		engine.jma_1_105(),
		engine.jma_1_105(),
		engine.jma_1_105()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_108():
	def __init__(self):
		instance_list = [
		engine.jma_1_108(),        
		engine.jma_1_108(),
		engine.jma_1_108(),
		engine.jma_1_108()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_109_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_109_a(),        
		engine.jma_1_109_a(),
		engine.jma_1_109_a(),
		engine.jma_1_109_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_109_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_109_b(),        
		engine.jma_1_109_b(),
		engine.jma_1_109_b(),
		engine.jma_1_109_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_110():
	def __init__(self):
		instance_list = [
		engine.jma_1_110(),        
		engine.jma_1_110(),
		engine.jma_1_110(),
		engine.jma_1_110()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_112():
	def __init__(self):
		instance_list = [
		engine.jma_1_112(),        
		engine.jma_1_112(),
		engine.jma_1_112(),
		engine.jma_1_112()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_113():
	def __init__(self):
		instance_list = [
		engine.jma_1_113(),        
		engine.jma_1_113(),
		engine.jma_1_113(),
		engine.jma_1_113()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

