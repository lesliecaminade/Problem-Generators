import random
from electronics import diode_engine as engine
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
		
class floyd_2_1_a():
	def __init__(self):
		instance_list = [
		engine.floyd_2_1_a(),        
		engine.floyd_2_1_a(),
		engine.floyd_2_1_a(),
		engine.floyd_2_1_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_1_b():
	def __init__(self):
		instance_list = [
		engine.floyd_2_1_b(),        
		engine.floyd_2_1_b(),
		engine.floyd_2_1_b(),
		engine.floyd_2_1_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_2():
	def __init__(self):
		instance_list = [
		engine.floyd_2_2(),        
		engine.floyd_2_2(),
		engine.floyd_2_2(),
		engine.floyd_2_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_3():
	def __init__(self):
		instance_list = [
		engine.floyd_2_3(),        
		engine.floyd_2_3(),
		engine.floyd_2_3(),
		engine.floyd_2_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_4():
	def __init__(self):
		instance_list = [
		engine.floyd_2_4(),        
		engine.floyd_2_4(),
		engine.floyd_2_4(),
		engine.floyd_2_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_5():
	def __init__(self):
		instance_list = [
		engine.floyd_2_5(),        
		engine.floyd_2_5(),
		engine.floyd_2_5(),
		engine.floyd_2_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_6():
	def __init__(self):
		instance_list = [
		engine.floyd_2_6(),        
		engine.floyd_2_6(),
		engine.floyd_2_6(),
		engine.floyd_2_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_7():
	def __init__(self):
		instance_list = [
		engine.floyd_2_7(),        
		engine.floyd_2_7(),
		engine.floyd_2_7(),
		engine.floyd_2_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_8():
	def __init__(self):
		instance_list = [
		engine.floyd_2_8(),        
		engine.floyd_2_8(),
		engine.floyd_2_8(),
		engine.floyd_2_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_9():
	def __init__(self):
		instance_list = [
		engine.floyd_2_9(),        
		engine.floyd_2_9(),
		engine.floyd_2_9(),
		engine.floyd_2_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_10():
	def __init__(self):
		instance_list = [
		engine.floyd_2_10(),        
		engine.floyd_2_10(),
		engine.floyd_2_10(),
		engine.floyd_2_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_11():
	def __init__(self):
		instance_list = [
		engine.floyd_2_11(),        
		engine.floyd_2_11(),
		engine.floyd_2_11(),
		engine.floyd_2_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_12():
	def __init__(self):
		instance_list = [
		engine.floyd_2_12(),        
		engine.floyd_2_12(),
		engine.floyd_2_12(),
		engine.floyd_2_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_2_13():
	def __init__(self):
		instance_list = [
		engine.floyd_2_13(),        
		engine.floyd_2_13(),
		engine.floyd_2_13(),
		engine.floyd_2_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_3_5():
	def __init__(self):
		instance_list = [
		engine.floyd_3_5(),        
		engine.floyd_3_5(),
		engine.floyd_3_5(),
		engine.floyd_3_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_3_6():
	def __init__(self):
		instance_list = [
		engine.floyd_3_6(),        
		engine.floyd_3_6(),
		engine.floyd_3_6(),
		engine.floyd_3_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_3_7():
	def __init__(self):
		instance_list = [
		engine.floyd_3_7(),        
		engine.floyd_3_7(),
		engine.floyd_3_7(),
		engine.floyd_3_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class floyd_3_8_a():
	def __init__(self):
		instance_list = [
		engine.floyd_3_8_a(),        
		engine.floyd_3_8_a(),
		engine.floyd_3_8_a(),
		engine.floyd_3_8_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class boylestad_2_4():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_4(),        
		engine.boylestad_2_4(),
		engine.boylestad_2_4(),
		engine.boylestad_2_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_6():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_6(),        
		engine.boylestad_2_6(),
		engine.boylestad_2_6(),
		engine.boylestad_2_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_9():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_9(),        
		engine.boylestad_2_9(),
		engine.boylestad_2_9(),
		engine.boylestad_2_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_10():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_10(),        
		engine.boylestad_2_10(),
		engine.boylestad_2_10(),
		engine.boylestad_2_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_11():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_11(),        
		engine.boylestad_2_11(),
		engine.boylestad_2_11(),
		engine.boylestad_2_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_12():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_12(),        
		engine.boylestad_2_12(),
		engine.boylestad_2_12(),
		engine.boylestad_2_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_13():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_13(),        
		engine.boylestad_2_13(),
		engine.boylestad_2_13(),
		engine.boylestad_2_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_14():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_14(),        
		engine.boylestad_2_14(),
		engine.boylestad_2_14(),
		engine.boylestad_2_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_15():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_15(),        
		engine.boylestad_2_15(),
		engine.boylestad_2_15(),
		engine.boylestad_2_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_16():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_16(),        
		engine.boylestad_2_16(),
		engine.boylestad_2_16(),
		engine.boylestad_2_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_2_17():
	def __init__(self):
		instance_list = [
		engine.boylestad_2_17(),        
		engine.boylestad_2_17(),
		engine.boylestad_2_17(),
		engine.boylestad_2_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		