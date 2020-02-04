import random
from est import frequency_and_phase_modulation_engine as engine
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

class jma_1_73_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_73_a(),        
		engine.jma_1_73_a(),
		engine.jma_1_73_a(),
		engine.jma_1_73_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_73_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_73_b(),        
		engine.jma_1_73_b(),
		engine.jma_1_73_b(),
		engine.jma_1_73_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_74_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_74_a(),        
		engine.jma_1_74_a(),
		engine.jma_1_74_a(),
		engine.jma_1_74_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_74_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_74_b(),        
		engine.jma_1_74_b(),
		engine.jma_1_74_b(),
		engine.jma_1_74_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_75():
	def __init__(self):
		instance_list = [
		engine.jma_1_75(),        
		engine.jma_1_75(),
		engine.jma_1_75(),
		engine.jma_1_75()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_76_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_76_a(),        
		engine.jma_1_76_a(),
		engine.jma_1_76_a(),
		engine.jma_1_76_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_77_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_77_a(),        
		engine.jma_1_77_a(),
		engine.jma_1_77_a(),
		engine.jma_1_77_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_77_c():
	def __init__(self):
		instance_list = [
		engine.jma_1_77_c(),        
		engine.jma_1_77_c(),
		engine.jma_1_77_c(),
		engine.jma_1_77_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_1():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_1(),        
		engine.schaums_ec_4_1(),
		engine.schaums_ec_4_1(),
		engine.schaums_ec_4_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_2():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_2(),        
		engine.schaums_ec_4_2(),
		engine.schaums_ec_4_2(),
		engine.schaums_ec_4_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_3():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_3(),        
		engine.schaums_ec_4_3(),
		engine.schaums_ec_4_3(),
		engine.schaums_ec_4_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_4():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_4(),        
		engine.schaums_ec_4_4(),
		engine.schaums_ec_4_4(),
		engine.schaums_ec_4_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_5():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_5(),        
		engine.schaums_ec_4_5(),
		engine.schaums_ec_4_5(),
		engine.schaums_ec_4_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_6():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_6(),        
		engine.schaums_ec_4_6(),
		engine.schaums_ec_4_6(),
		engine.schaums_ec_4_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_7():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_7(),        
		engine.schaums_ec_4_7(),
		engine.schaums_ec_4_7(),
		engine.schaums_ec_4_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_8():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_8(),        
		engine.schaums_ec_4_8(),
		engine.schaums_ec_4_8(),
		engine.schaums_ec_4_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_9():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_9(),        
		engine.schaums_ec_4_9(),
		engine.schaums_ec_4_9(),
		engine.schaums_ec_4_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_12():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_12(),        
		engine.schaums_ec_4_12(),
		engine.schaums_ec_4_12(),
		engine.schaums_ec_4_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_13():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_13(),        
		engine.schaums_ec_4_13(),
		engine.schaums_ec_4_13(),
		engine.schaums_ec_4_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_14():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_14(),        
		engine.schaums_ec_4_14(),
		engine.schaums_ec_4_14(),
		engine.schaums_ec_4_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_15():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_15(),        
		engine.schaums_ec_4_15(),
		engine.schaums_ec_4_15(),
		engine.schaums_ec_4_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_16():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_16(),        
		engine.schaums_ec_4_16(),
		engine.schaums_ec_4_16(),
		engine.schaums_ec_4_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_4_17():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_4_17(),        
		engine.schaums_ec_4_17(),
		engine.schaums_ec_4_17(),
		engine.schaums_ec_4_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

