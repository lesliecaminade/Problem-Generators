import random
from electronics import power_electronics_engine as engine
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
		

class fewson_2_1():
	def __init__(self):
		instance_list = [
		engine.fewson_2_1(),        
		engine.fewson_2_1(),
		engine.fewson_2_1(),
		engine.fewson_2_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_2_2():
	def __init__(self):
		instance_list = [
		engine.fewson_2_2(),        
		engine.fewson_2_2(),
		engine.fewson_2_2(),
		engine.fewson_2_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_2_3():
	def __init__(self):
		instance_list = [
		engine.fewson_2_3(),        
		engine.fewson_2_3(),
		engine.fewson_2_3(),
		engine.fewson_2_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_2_4():
	def __init__(self):
		instance_list = [
		engine.fewson_2_4(),        
		engine.fewson_2_4(),
		engine.fewson_2_4(),
		engine.fewson_2_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_2_5():
	def __init__(self):
		instance_list = [
		engine.fewson_2_5(),        
		engine.fewson_2_5(),
		engine.fewson_2_5(),
		engine.fewson_2_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_1():
	def __init__(self):
		instance_list = [
		engine.fewson_3_1(),        
		engine.fewson_3_1(),
		engine.fewson_3_1(),
		engine.fewson_3_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_3():
	def __init__(self):
		instance_list = [
		engine.fewson_3_3(),        
		engine.fewson_3_3(),
		engine.fewson_3_3(),
		engine.fewson_3_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_4():
	def __init__(self):
		instance_list = [
		engine.fewson_3_4(),        
		engine.fewson_3_4(),
		engine.fewson_3_4(),
		engine.fewson_3_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_5():
	def __init__(self):
		instance_list = [
		engine.fewson_3_5(),        
		engine.fewson_3_5(),
		engine.fewson_3_5(),
		engine.fewson_3_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_6():
	def __init__(self):
		instance_list = [
		engine.fewson_3_6(),        
		engine.fewson_3_6(),
		engine.fewson_3_6(),
		engine.fewson_3_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_7():
	def __init__(self):
		instance_list = [
		engine.fewson_3_7(),        
		engine.fewson_3_7(),
		engine.fewson_3_7(),
		engine.fewson_3_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_8():
	def __init__(self):
		instance_list = [
		engine.fewson_3_8(),        
		engine.fewson_3_8(),
		engine.fewson_3_8(),
		engine.fewson_3_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_9():
	def __init__(self):
		instance_list = [
		engine.fewson_3_9(),        
		engine.fewson_3_9(),
		engine.fewson_3_9(),
		engine.fewson_3_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class fewson_3_10():
	def __init__(self):
		instance_list = [
		engine.fewson_3_10(),        
		engine.fewson_3_10(),
		engine.fewson_3_10(),
		engine.fewson_3_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		