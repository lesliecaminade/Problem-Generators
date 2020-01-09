import random
from geas import engineering_economy_engine as engine
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
		
class hipolito_2_1():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_1(),        
		engine.hipolito_2_1(),
		engine.hipolito_2_1(),
		engine.hipolito_2_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_2():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_2(),        
		engine.hipolito_2_2(),
		engine.hipolito_2_2(),
		engine.hipolito_2_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_3():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_3(),        
		engine.hipolito_2_3(),
		engine.hipolito_2_3(),
		engine.hipolito_2_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_4():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_4(),        
		engine.hipolito_2_4(),
		engine.hipolito_2_4(),
		engine.hipolito_2_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_5():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_5(),        
		engine.hipolito_2_5(),
		engine.hipolito_2_5(),
		engine.hipolito_2_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_6():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_6(),        
		engine.hipolito_2_6(),
		engine.hipolito_2_6(),
		engine.hipolito_2_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_7():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_7(),        
		engine.hipolito_2_7(),
		engine.hipolito_2_7(),
		engine.hipolito_2_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_8():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_8(),        
		engine.hipolito_2_8(),
		engine.hipolito_2_8(),
		engine.hipolito_2_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_9():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_9(),        
		engine.hipolito_2_9(),
		engine.hipolito_2_9(),
		engine.hipolito_2_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_10():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_10(),        
		engine.hipolito_2_10(),
		engine.hipolito_2_10(),
		engine.hipolito_2_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_11():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_11(),        
		engine.hipolito_2_11(),
		engine.hipolito_2_11(),
		engine.hipolito_2_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_12():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_12(),        
		engine.hipolito_2_12(),
		engine.hipolito_2_12(),
		engine.hipolito_2_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_14():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_14(),        
		engine.hipolito_2_14(),
		engine.hipolito_2_14(),
		engine.hipolito_2_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_15():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_15(),        
		engine.hipolito_2_15(),
		engine.hipolito_2_15(),
		engine.hipolito_2_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_18():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_18(),        
		engine.hipolito_2_18(),
		engine.hipolito_2_18(),
		engine.hipolito_2_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_19():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_19(),        
		engine.hipolito_2_19(),
		engine.hipolito_2_19(),
		engine.hipolito_2_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_21():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_21(),        
		engine.hipolito_2_21(),
		engine.hipolito_2_21(),
		engine.hipolito_2_21()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_22():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_22(),        
		engine.hipolito_2_22(),
		engine.hipolito_2_22(),
		engine.hipolito_2_22()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_2_23():
	def __init__(self):
		instance_list = [
		engine.hipolito_2_23(),        
		engine.hipolito_2_23(),
		engine.hipolito_2_23(),
		engine.hipolito_2_23()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_3_1():
	def __init__(self):
		instance_list = [
		engine.hipolito_3_1(),        
		engine.hipolito_3_1(),
		engine.hipolito_3_1(),
		engine.hipolito_3_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_3_2():
	def __init__(self):
		instance_list = [
		engine.hipolito_3_2(),        
		engine.hipolito_3_2(),
		engine.hipolito_3_2(),
		engine.hipolito_3_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_3_3():
	def __init__(self):
		instance_list = [
		engine.hipolito_3_3(),        
		engine.hipolito_3_3(),
		engine.hipolito_3_3(),
		engine.hipolito_3_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class hipolito_3_5():
	def __init__(self):
		instance_list = [
		engine.hipolito_3_5(),        
		engine.hipolito_3_5(),
		engine.hipolito_3_5(),
		engine.hipolito_3_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		