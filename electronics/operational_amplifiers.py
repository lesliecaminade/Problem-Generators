import random
from electronics import bipolar_junction_transistors_engine as engine
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
		
class boylestad_4_1():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_1(),        
		engine.boylestad_4_1(),
		engine.boylestad_4_1(),
		engine.boylestad_4_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_2():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_2(),        
		engine.boylestad_4_2(),
		engine.boylestad_4_2(),
		engine.boylestad_4_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_3():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_3(),        
		engine.boylestad_4_3(),
		engine.boylestad_4_3(),
		engine.boylestad_4_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_6():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_6(),        
		engine.boylestad_4_6(),
		engine.boylestad_4_6(),
		engine.boylestad_4_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_8():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_8(),        
		engine.boylestad_4_8(),
		engine.boylestad_4_8(),
		engine.boylestad_4_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_12():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_12(),        
		engine.boylestad_4_12(),
		engine.boylestad_4_12(),
		engine.boylestad_4_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_14():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_14(),        
		engine.boylestad_4_14(),
		engine.boylestad_4_14(),
		engine.boylestad_4_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer     
		
class boylestad_4_16():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_16(),        
		engine.boylestad_4_16(),
		engine.boylestad_4_16(),
		engine.boylestad_4_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_17():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_17(),        
		engine.boylestad_4_17(),
		engine.boylestad_4_17(),
		engine.boylestad_4_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_18():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_18(),        
		engine.boylestad_4_18(),
		engine.boylestad_4_18(),
		engine.boylestad_4_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_19():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_19(),        
		engine.boylestad_4_19(),
		engine.boylestad_4_19(),
		engine.boylestad_4_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_20():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_20(),        
		engine.boylestad_4_20(),
		engine.boylestad_4_20(),
		engine.boylestad_4_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_27():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_27(),        
		engine.boylestad_4_27(),
		engine.boylestad_4_27(),
		engine.boylestad_4_27()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_28():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_28(),        
		engine.boylestad_4_28(),
		engine.boylestad_4_28(),
		engine.boylestad_4_28()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_29():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_29(),        
		engine.boylestad_4_29(),
		engine.boylestad_4_29(),
		engine.boylestad_4_29()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_30():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_30(),        
		engine.boylestad_4_30(),
		engine.boylestad_4_30(),
		engine.boylestad_4_30()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_31():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_31(),        
		engine.boylestad_4_31(),
		engine.boylestad_4_31(),
		engine.boylestad_4_31()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_32():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_32(),        
		engine.boylestad_4_32(),
		engine.boylestad_4_32(),
		engine.boylestad_4_32()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_35():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_35(),        
		engine.boylestad_4_35(),
		engine.boylestad_4_35(),
		engine.boylestad_4_35()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_4_36():
	def __init__(self):
		instance_list = [
		engine.boylestad_4_36(),        
		engine.boylestad_4_36(),
		engine.boylestad_4_36(),
		engine.boylestad_4_36()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		