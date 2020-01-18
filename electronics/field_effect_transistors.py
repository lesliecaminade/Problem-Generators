import random
from electronics import field_effect_transistors_engine as engine
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
		
class boylestad_7_1():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_1(),        
		engine.boylestad_7_1(),
		engine.boylestad_7_1(),
		engine.boylestad_7_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_2():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_2(),        
		engine.boylestad_7_2(),
		engine.boylestad_7_2(),
		engine.boylestad_7_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_4():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_4(),        
		engine.boylestad_7_4(),
		engine.boylestad_7_4(),
		engine.boylestad_7_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_5():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_5(),        
		engine.boylestad_7_5(),
		engine.boylestad_7_5(),
		engine.boylestad_7_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_6():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_6(),        
		engine.boylestad_7_6(),
		engine.boylestad_7_6(),
		engine.boylestad_7_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_8():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_8(),        
		engine.boylestad_7_8(),
		engine.boylestad_7_8(),
		engine.boylestad_7_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_10():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_10(),        
		engine.boylestad_7_10(),
		engine.boylestad_7_10(),
		engine.boylestad_7_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_7_11():
	def __init__(self):
		instance_list = [
		engine.boylestad_7_11(),        
		engine.boylestad_7_11(),
		engine.boylestad_7_11(),
		engine.boylestad_7_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_8_7():
	def __init__(self):
		instance_list = [
		engine.boylestad_8_7(),        
		engine.boylestad_8_7(),
		engine.boylestad_8_7(),
		engine.boylestad_8_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_8_8():
	def __init__(self):
		instance_list = [
		engine.boylestad_8_8(),        
		engine.boylestad_8_8(),
		engine.boylestad_8_8(),
		engine.boylestad_8_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_8_9():
	def __init__(self):
		instance_list = [
		engine.boylestad_8_9(),        
		engine.boylestad_8_9(),
		engine.boylestad_8_9(),
		engine.boylestad_8_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_8_10():
	def __init__(self):
		instance_list = [
		engine.boylestad_8_10(),        
		engine.boylestad_8_10(),
		engine.boylestad_8_10(),
		engine.boylestad_8_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_8_11():
	def __init__(self):
		instance_list = [
		engine.boylestad_8_11(),        
		engine.boylestad_8_11(),
		engine.boylestad_8_11(),
		engine.boylestad_8_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_8_12():
	def __init__(self):
		instance_list = [
		engine.boylestad_8_12(),        
		engine.boylestad_8_12(),
		engine.boylestad_8_12(),
		engine.boylestad_8_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		