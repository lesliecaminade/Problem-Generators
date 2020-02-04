import random
from est import amplitude_modulation_engine as engine
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

class schaums_ec_3_1():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_1(),        
		engine.schaums_ec_3_1(),
		engine.schaums_ec_3_1(),
		engine.schaums_ec_3_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_2():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_2(),        
		engine.schaums_ec_3_2(),
		engine.schaums_ec_3_2(),
		engine.schaums_ec_3_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_3():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_3(),        
		engine.schaums_ec_3_3(),
		engine.schaums_ec_3_3(),
		engine.schaums_ec_3_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_4():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_4(),        
		engine.schaums_ec_3_4(),
		engine.schaums_ec_3_4(),
		engine.schaums_ec_3_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_5():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_5(),        
		engine.schaums_ec_3_5(),
		engine.schaums_ec_3_5(),
		engine.schaums_ec_3_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_6():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_6(),        
		engine.schaums_ec_3_6(),
		engine.schaums_ec_3_6(),
		engine.schaums_ec_3_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_7():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_7(),        
		engine.schaums_ec_3_7(),
		engine.schaums_ec_3_7(),
		engine.schaums_ec_3_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_8():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_8(),        
		engine.schaums_ec_3_8(),
		engine.schaums_ec_3_8(),
		engine.schaums_ec_3_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_9():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_9(),        
		engine.schaums_ec_3_9(),
		engine.schaums_ec_3_9(),
		engine.schaums_ec_3_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_10():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_10(),        
		engine.schaums_ec_3_10(),
		engine.schaums_ec_3_10(),
		engine.schaums_ec_3_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_11():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_11(),        
		engine.schaums_ec_3_11(),
		engine.schaums_ec_3_11(),
		engine.schaums_ec_3_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_12():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_12(),        
		engine.schaums_ec_3_12(),
		engine.schaums_ec_3_12(),
		engine.schaums_ec_3_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_13():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_13(),        
		engine.schaums_ec_3_13(),
		engine.schaums_ec_3_13(),
		engine.schaums_ec_3_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_14():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_14(),        
		engine.schaums_ec_3_14(),
		engine.schaums_ec_3_14(),
		engine.schaums_ec_3_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_15():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_15(),        
		engine.schaums_ec_3_15(),
		engine.schaums_ec_3_15(),
		engine.schaums_ec_3_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_16():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_16(),        
		engine.schaums_ec_3_16(),
		engine.schaums_ec_3_16(),
		engine.schaums_ec_3_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_17():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_17(),        
		engine.schaums_ec_3_17(),
		engine.schaums_ec_3_17(),
		engine.schaums_ec_3_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_19():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_19(),        
		engine.schaums_ec_3_19(),
		engine.schaums_ec_3_19(),
		engine.schaums_ec_3_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_20():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_20(),        
		engine.schaums_ec_3_20(),
		engine.schaums_ec_3_20(),
		engine.schaums_ec_3_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class schaums_ec_3_21():
	def __init__(self):
		instance_list = [
		engine.schaums_ec_3_21(),        
		engine.schaums_ec_3_21(),
		engine.schaums_ec_3_21(),
		engine.schaums_ec_3_21()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_40_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_40_a(),        
		engine.jma_1_40_a(),
		engine.jma_1_40_a(),
		engine.jma_1_40_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_40_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_40_b(),        
		engine.jma_1_40_b(),
		engine.jma_1_40_b(),
		engine.jma_1_40_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_42():
	def __init__(self):
		instance_list = [
		engine.jma_1_42(),        
		engine.jma_1_42(),
		engine.jma_1_42(),
		engine.jma_1_42()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_43_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_43_a(),        
		engine.jma_1_43_a(),
		engine.jma_1_43_a(),
		engine.jma_1_43_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_43_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_43_b(),        
		engine.jma_1_43_b(),
		engine.jma_1_43_b(),
		engine.jma_1_43_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_46_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_46_a(),        
		engine.jma_1_46_a(),
		engine.jma_1_46_a(),
		engine.jma_1_46_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_46_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_46_b(),        
		engine.jma_1_46_b(),
		engine.jma_1_46_b(),
		engine.jma_1_46_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_46_c():
	def __init__(self):
		instance_list = [
		engine.jma_1_46_c(),        
		engine.jma_1_46_c(),
		engine.jma_1_46_c(),
		engine.jma_1_46_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_47_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_47_a(),        
		engine.jma_1_47_a(),
		engine.jma_1_47_a(),
		engine.jma_1_47_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_47_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_47_b(),        
		engine.jma_1_47_b(),
		engine.jma_1_47_b(),
		engine.jma_1_47_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_49():
	def __init__(self):
		instance_list = [
		engine.jma_1_49(),        
		engine.jma_1_49(),
		engine.jma_1_49(),
		engine.jma_1_49()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_50():
	def __init__(self):
		instance_list = [
		engine.jma_1_50(),        
		engine.jma_1_50(),
		engine.jma_1_50(),
		engine.jma_1_50()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_52_a():
	def __init__(self):
		instance_list = [
		engine.jma_1_52_a(),        
		engine.jma_1_52_a(),
		engine.jma_1_52_a(),
		engine.jma_1_52_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class jma_1_52_b():
	def __init__(self):
		instance_list = [
		engine.jma_1_52_b(),        
		engine.jma_1_52_b(),
		engine.jma_1_52_b(),
		engine.jma_1_52_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   

