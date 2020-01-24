import random
from electronics import operational_amplifiers_engine as engine
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
		
class boylestad_10_1():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_1(),        
		engine.boylestad_10_1(),
		engine.boylestad_10_1(),
		engine.boylestad_10_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_2():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_2(),        
		engine.boylestad_10_2(),
		engine.boylestad_10_2(),
		engine.boylestad_10_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_3():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_3(),        
		engine.boylestad_10_3(),
		engine.boylestad_10_3(),
		engine.boylestad_10_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_4():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_4(),        
		engine.boylestad_10_4(),
		engine.boylestad_10_4(),
		engine.boylestad_10_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_5():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_5(),        
		engine.boylestad_10_5(),
		engine.boylestad_10_5(),
		engine.boylestad_10_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_6():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_6(),        
		engine.boylestad_10_6(),
		engine.boylestad_10_6(),
		engine.boylestad_10_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_7():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_7(),        
		engine.boylestad_10_7(),
		engine.boylestad_10_7(),
		engine.boylestad_10_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_8():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_8(),        
		engine.boylestad_10_8(),
		engine.boylestad_10_8(),
		engine.boylestad_10_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_9():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_9(),        
		engine.boylestad_10_9(),
		engine.boylestad_10_9(),
		engine.boylestad_10_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_10():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_10(),        
		engine.boylestad_10_10(),
		engine.boylestad_10_10(),
		engine.boylestad_10_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_11():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_11(),        
		engine.boylestad_10_11(),
		engine.boylestad_10_11(),
		engine.boylestad_10_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_12():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_12(),        
		engine.boylestad_10_12(),
		engine.boylestad_10_12(),
		engine.boylestad_10_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_13():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_13(),        
		engine.boylestad_10_13(),
		engine.boylestad_10_13(),
		engine.boylestad_10_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_14():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_14(),        
		engine.boylestad_10_14(),
		engine.boylestad_10_14(),
		engine.boylestad_10_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_10_15():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_15(),        
		engine.boylestad_10_15(),
		engine.boylestad_10_15(),
		engine.boylestad_10_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer     
		
class boylestad_10_17():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_17(),        
		engine.boylestad_10_17(),
		engine.boylestad_10_17(),
		engine.boylestad_10_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer         
		
class boylestad_10_22():
	def __init__(self):
		instance_list = [
		engine.boylestad_10_22(),        
		engine.boylestad_10_22(),
		engine.boylestad_10_22(),
		engine.boylestad_10_22()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_1():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_1(),        
		engine.boylestad_11_1(),
		engine.boylestad_11_1(),
		engine.boylestad_11_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_2():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_2(),        
		engine.boylestad_11_2(),
		engine.boylestad_11_2(),
		engine.boylestad_11_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_3():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_3(),        
		engine.boylestad_11_3(),
		engine.boylestad_11_3(),
		engine.boylestad_11_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer       
		
class boylestad_11_6():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_6(),        
		engine.boylestad_11_6(),
		engine.boylestad_11_6(),
		engine.boylestad_11_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_7():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_7(),        
		engine.boylestad_11_7(),
		engine.boylestad_11_7(),
		engine.boylestad_11_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_8():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_8(),        
		engine.boylestad_11_8(),
		engine.boylestad_11_8(),
		engine.boylestad_11_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class boylestad_11_10():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_10(),        
		engine.boylestad_11_10(),
		engine.boylestad_11_10(),
		engine.boylestad_11_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_11():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_11(),        
		engine.boylestad_11_11(),
		engine.boylestad_11_11(),
		engine.boylestad_11_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_12():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_12(),        
		engine.boylestad_11_12(),
		engine.boylestad_11_12(),
		engine.boylestad_11_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_13():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_13(),        
		engine.boylestad_11_13(),
		engine.boylestad_11_13(),
		engine.boylestad_11_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class boylestad_11_14():
	def __init__(self):
		instance_list = [
		engine.boylestad_11_14(),        
		engine.boylestad_11_14(),
		engine.boylestad_11_14(),
		engine.boylestad_11_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		