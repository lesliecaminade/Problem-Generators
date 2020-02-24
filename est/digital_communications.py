import random
from est import digital_communications_engine as engine
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


class jma_14_1():
	def __init__(self):
		instance_list = [
		engine.jma_14_1(),        
		engine.jma_14_1(),
		engine.jma_14_1(),
		engine.jma_14_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_2():
	def __init__(self):
		instance_list = [
		engine.jma_14_2(),        
		engine.jma_14_2(),
		engine.jma_14_2(),
		engine.jma_14_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_3():
	def __init__(self):
		instance_list = [
		engine.jma_14_3(),        
		engine.jma_14_3(),
		engine.jma_14_3(),
		engine.jma_14_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_4():
	def __init__(self):
		instance_list = [
		engine.jma_14_4(),        
		engine.jma_14_4(),
		engine.jma_14_4(),
		engine.jma_14_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_5():
	def __init__(self):
		instance_list = [
		engine.jma_14_5(),        
		engine.jma_14_5(),
		engine.jma_14_5(),
		engine.jma_14_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_6():
	def __init__(self):
		instance_list = [
		engine.jma_14_6(),        
		engine.jma_14_6(),
		engine.jma_14_6(),
		engine.jma_14_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_7():
	def __init__(self):
		instance_list = [
		engine.jma_14_7(),        
		engine.jma_14_7(),
		engine.jma_14_7(),
		engine.jma_14_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_14_8():
	def __init__(self):
		instance_list = [
		engine.jma_14_8(),        
		engine.jma_14_8(),
		engine.jma_14_8(),
		engine.jma_14_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class jma_15_1():
	def __init__(self):
		instance_list = [
		engine.jma_15_1(),        
		engine.jma_15_1(),
		engine.jma_15_1(),
		engine.jma_15_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_2():
	def __init__(self):
		instance_list = [
		engine.jma_15_2(),        
		engine.jma_15_2(),
		engine.jma_15_2(),
		engine.jma_15_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_3():
	def __init__(self):
		instance_list = [
		engine.jma_15_3(),        
		engine.jma_15_3(),
		engine.jma_15_3(),
		engine.jma_15_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_4():
	def __init__(self):
		instance_list = [
		engine.jma_15_4(),        
		engine.jma_15_4(),
		engine.jma_15_4(),
		engine.jma_15_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_5():
	def __init__(self):
		instance_list = [
		engine.jma_15_5(),        
		engine.jma_15_5(),
		engine.jma_15_5(),
		engine.jma_15_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_6():
	def __init__(self):
		instance_list = [
		engine.jma_15_6(),        
		engine.jma_15_6(),
		engine.jma_15_6(),
		engine.jma_15_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_7():
	def __init__(self):
		instance_list = [
		engine.jma_15_7(),        
		engine.jma_15_7(),
		engine.jma_15_7(),
		engine.jma_15_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_8():
	def __init__(self):
		instance_list = [
		engine.jma_15_8(),        
		engine.jma_15_8(),
		engine.jma_15_8(),
		engine.jma_15_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_15_9():
	def __init__(self):
		instance_list = [
		engine.jma_15_9(),        
		engine.jma_15_9(),
		engine.jma_15_9(),
		engine.jma_15_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer



