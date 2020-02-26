import random
from mathsub import algebra as engine
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
		self.question = parse(main.question)
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""       

class algebra_1():
	def __init__(self):
		instance_list = [
		engine.algebra_1(),        
		engine.algebra_1(),
		engine.algebra_1(),
		engine.algebra_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_2():
	def __init__(self):
		instance_list = [
		engine.algebra_2(),        
		engine.algebra_2(),
		engine.algebra_2(),
		engine.algebra_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_3():
	def __init__(self):
		instance_list = [
		engine.algebra_3(),        
		engine.algebra_3(),
		engine.algebra_3(),
		engine.algebra_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_4():
	def __init__(self):
		instance_list = [
		engine.algebra_4(),        
		engine.algebra_4(),
		engine.algebra_4(),
		engine.algebra_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_5():
	def __init__(self):
		instance_list = [
		engine.algebra_5(),        
		engine.algebra_5(),
		engine.algebra_5(),
		engine.algebra_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_6():
	def __init__(self):
		instance_list = [
		engine.algebra_6(),        
		engine.algebra_6(),
		engine.algebra_6(),
		engine.algebra_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_7():
	def __init__(self):
		instance_list = [
		engine.algebra_7(),        
		engine.algebra_7(),
		engine.algebra_7(),
		engine.algebra_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_8():
	def __init__(self):
		instance_list = [
		engine.algebra_8(),        
		engine.algebra_8(),
		engine.algebra_8(),
		engine.algebra_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_9():
	def __init__(self):
		instance_list = [
		engine.algebra_9(),        
		engine.algebra_9(),
		engine.algebra_9(),
		engine.algebra_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_10():
	def __init__(self):
		instance_list = [
		engine.algebra_10(),        
		engine.algebra_10(),
		engine.algebra_10(),
		engine.algebra_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_11():
	def __init__(self):
		instance_list = [
		engine.algebra_11(),        
		engine.algebra_11(),
		engine.algebra_11(),
		engine.algebra_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_12():
	def __init__(self):
		instance_list = [
		engine.algebra_12(),        
		engine.algebra_12(),
		engine.algebra_12(),
		engine.algebra_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_13():
	def __init__(self):
		instance_list = [
		engine.algebra_13(),        
		engine.algebra_13(),
		engine.algebra_13(),
		engine.algebra_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_14():
	def __init__(self):
		instance_list = [
		engine.algebra_14(),        
		engine.algebra_14(),
		engine.algebra_14(),
		engine.algebra_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_15():
	def __init__(self):
		instance_list = [
		engine.algebra_15(),        
		engine.algebra_15(),
		engine.algebra_15(),
		engine.algebra_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_16():
	def __init__(self):
		instance_list = [
		engine.algebra_16(),        
		engine.algebra_16(),
		engine.algebra_16(),
		engine.algebra_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_17():
	def __init__(self):
		instance_list = [
		engine.algebra_17(),        
		engine.algebra_17(),
		engine.algebra_17(),
		engine.algebra_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_18():
	def __init__(self):
		instance_list = [
		engine.algebra_18(),        
		engine.algebra_18(),
		engine.algebra_18(),
		engine.algebra_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_19():
	def __init__(self):
		instance_list = [
		engine.algebra_19(),        
		engine.algebra_19(),
		engine.algebra_19(),
		engine.algebra_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_20():
	def __init__(self):
		instance_list = [
		engine.algebra_20(),        
		engine.algebra_20(),
		engine.algebra_20(),
		engine.algebra_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_21():
	def __init__(self):
		instance_list = [
		engine.algebra_21(),        
		engine.algebra_21(),
		engine.algebra_21(),
		engine.algebra_21()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_22():
	def __init__(self):
		instance_list = [
		engine.algebra_22(),        
		engine.algebra_22(),
		engine.algebra_22(),
		engine.algebra_22()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_23():
	def __init__(self):
		instance_list = [
		engine.algebra_23(),        
		engine.algebra_23(),
		engine.algebra_23(),
		engine.algebra_23()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_24():
	def __init__(self):
		instance_list = [
		engine.algebra_24(),        
		engine.algebra_24(),
		engine.algebra_24(),
		engine.algebra_24()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_25():
	def __init__(self):
		instance_list = [
		engine.algebra_25(),        
		engine.algebra_25(),
		engine.algebra_25(),
		engine.algebra_25()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_26():
	def __init__(self):
		instance_list = [
		engine.algebra_26(),        
		engine.algebra_26(),
		engine.algebra_26(),
		engine.algebra_26()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_27():
	def __init__(self):
		instance_list = [
		engine.algebra_27(),        
		engine.algebra_27(),
		engine.algebra_27(),
		engine.algebra_27()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_28():
	def __init__(self):
		instance_list = [
		engine.algebra_28(),        
		engine.algebra_28(),
		engine.algebra_28(),
		engine.algebra_28()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_29():
	def __init__(self):
		instance_list = [
		engine.algebra_29(),        
		engine.algebra_29(),
		engine.algebra_29(),
		engine.algebra_29()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_30():
	def __init__(self):
		instance_list = [
		engine.algebra_30(),        
		engine.algebra_30(),
		engine.algebra_30(),
		engine.algebra_30()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class algebra_31():
	def __init__(self):
		instance_list = [
		engine.algebra_31(),        
		engine.algebra_31(),
		engine.algebra_31(),
		engine.algebra_31()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
