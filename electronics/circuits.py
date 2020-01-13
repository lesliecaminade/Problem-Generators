import random
from electronics import circuits_engine as engine
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
		
class sadiku_1_1():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_1(),        
		engine.sadiku_1_1(),
		engine.sadiku_1_1(),
		engine.sadiku_1_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_2():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_2(),        
		engine.sadiku_1_2(),
		engine.sadiku_1_2(),
		engine.sadiku_1_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_3():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_3(),        
		engine.sadiku_1_3(),
		engine.sadiku_1_3(),
		engine.sadiku_1_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_4():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_4(),        
		engine.sadiku_1_4(),
		engine.sadiku_1_4(),
		engine.sadiku_1_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_5():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_5(),        
		engine.sadiku_1_5(),
		engine.sadiku_1_5(),
		engine.sadiku_1_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_5():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_5(),        
		engine.sadiku_1_5(),
		engine.sadiku_1_5(),
		engine.sadiku_1_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_6():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_6(),        
		engine.sadiku_1_6(),
		engine.sadiku_1_6(),
		engine.sadiku_1_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_7():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_7(),        
		engine.sadiku_1_7(),
		engine.sadiku_1_7(),
		engine.sadiku_1_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_8():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_8(),        
		engine.sadiku_1_8(),
		engine.sadiku_1_8(),
		engine.sadiku_1_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_1_9():
	def __init__(self):
		instance_list = [
		engine.sadiku_1_9(),        
		engine.sadiku_1_9(),
		engine.sadiku_1_9(),
		engine.sadiku_1_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_1():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_1(),        
		engine.sadiku_2_1(),
		engine.sadiku_2_1(),
		engine.sadiku_2_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_2():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_2(),        
		engine.sadiku_2_2(),
		engine.sadiku_2_2(),
		engine.sadiku_2_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_3():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_3(),        
		engine.sadiku_2_3(),
		engine.sadiku_2_3(),
		engine.sadiku_2_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_5():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_5(),        
		engine.sadiku_2_5(),
		engine.sadiku_2_5(),
		engine.sadiku_2_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_6():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_6(),        
		engine.sadiku_2_6(),
		engine.sadiku_2_6(),
		engine.sadiku_2_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_7():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_7(),        
		engine.sadiku_2_7(),
		engine.sadiku_2_7(),
		engine.sadiku_2_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class sadiku_2_8():
	def __init__(self):
		instance_list = [
		engine.sadiku_2_8(),        
		engine.sadiku_2_8(),
		engine.sadiku_2_8(),
		engine.sadiku_2_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_1():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_1(),        
		engine.johnbird_2_1(),
		engine.johnbird_2_1(),
		engine.johnbird_2_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_2(),        
		engine.johnbird_2_2(),
		engine.johnbird_2_2(),
		engine.johnbird_2_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_3(),        
		engine.johnbird_2_3(),
		engine.johnbird_2_3(),
		engine.johnbird_2_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_4(),        
		engine.johnbird_2_4(),
		engine.johnbird_2_4(),
		engine.johnbird_2_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_5():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_5(),        
		engine.johnbird_2_5(),
		engine.johnbird_2_5(),
		engine.johnbird_2_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_6():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_6(),        
		engine.johnbird_2_6(),
		engine.johnbird_2_6(),
		engine.johnbird_2_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_7():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_7(),        
		engine.johnbird_2_7(),
		engine.johnbird_2_7(),
		engine.johnbird_2_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_9():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_9(),        
		engine.johnbird_2_9(),
		engine.johnbird_2_9(),
		engine.johnbird_2_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_10():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_10(),        
		engine.johnbird_2_10(),
		engine.johnbird_2_10(),
		engine.johnbird_2_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_11():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_11(),        
		engine.johnbird_2_11(),
		engine.johnbird_2_11(),
		engine.johnbird_2_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_12():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_12(),        
		engine.johnbird_2_12(),
		engine.johnbird_2_12(),
		engine.johnbird_2_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_13():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_13(),        
		engine.johnbird_2_13(),
		engine.johnbird_2_13(),
		engine.johnbird_2_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_14():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_14(),        
		engine.johnbird_2_14(),
		engine.johnbird_2_14(),
		engine.johnbird_2_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_15():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_15(),        
		engine.johnbird_2_15(),
		engine.johnbird_2_15(),
		engine.johnbird_2_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_16():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_16(),        
		engine.johnbird_2_16(),
		engine.johnbird_2_16(),
		engine.johnbird_2_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_17():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_17(),        
		engine.johnbird_2_17(),
		engine.johnbird_2_17(),
		engine.johnbird_2_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_18():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_18(),        
		engine.johnbird_2_18(),
		engine.johnbird_2_18(),
		engine.johnbird_2_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_2_19():
	def __init__(self):
		instance_list = [
		engine.johnbird_2_19(),        
		engine.johnbird_2_19(),
		engine.johnbird_2_19(),
		engine.johnbird_2_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_1():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_1(),        
		engine.johnbird_3_1(),
		engine.johnbird_3_1(),
		engine.johnbird_3_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_2(),        
		engine.johnbird_3_2(),
		engine.johnbird_3_2(),
		engine.johnbird_3_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_3(),        
		engine.johnbird_3_3(),
		engine.johnbird_3_3(),
		engine.johnbird_3_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_4(),        
		engine.johnbird_3_4(),
		engine.johnbird_3_4(),
		engine.johnbird_3_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_5():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_5(),        
		engine.johnbird_3_5(),
		engine.johnbird_3_5(),
		engine.johnbird_3_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_6():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_6(),        
		engine.johnbird_3_6(),
		engine.johnbird_3_6(),
		engine.johnbird_3_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_7():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_7(),        
		engine.johnbird_3_7(),
		engine.johnbird_3_7(),
		engine.johnbird_3_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_8():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_8(),        
		engine.johnbird_3_8(),
		engine.johnbird_3_8(),
		engine.johnbird_3_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_9():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_9(),        
		engine.johnbird_3_9(),
		engine.johnbird_3_9(),
		engine.johnbird_3_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_10():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_10(),        
		engine.johnbird_3_10(),
		engine.johnbird_3_10(),
		engine.johnbird_3_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_11():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_11(),        
		engine.johnbird_3_11(),
		engine.johnbird_3_11(),
		engine.johnbird_3_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_12():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_12(),        
		engine.johnbird_3_12(),
		engine.johnbird_3_12(),
		engine.johnbird_3_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_13():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_13(),        
		engine.johnbird_3_13(),
		engine.johnbird_3_13(),
		engine.johnbird_3_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_14():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_14(),        
		engine.johnbird_3_14(),
		engine.johnbird_3_14(),
		engine.johnbird_3_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_16():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_16(),        
		engine.johnbird_3_16(),
		engine.johnbird_3_16(),
		engine.johnbird_3_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_17():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_17(),        
		engine.johnbird_3_17(),
		engine.johnbird_3_17(),
		engine.johnbird_3_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_18():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_18(),        
		engine.johnbird_3_18(),
		engine.johnbird_3_18(),
		engine.johnbird_3_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_3_19():
	def __init__(self):
		instance_list = [
		engine.johnbird_3_19(),        
		engine.johnbird_3_19(),
		engine.johnbird_3_19(),
		engine.johnbird_3_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_1():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_1(),        
		engine.johnbird_5_1(),
		engine.johnbird_5_1(),
		engine.johnbird_5_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_2(),        
		engine.johnbird_5_2(),
		engine.johnbird_5_2(),
		engine.johnbird_5_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_3(),        
		engine.johnbird_5_3(),
		engine.johnbird_5_3(),
		engine.johnbird_5_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_5():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_5(),        
		engine.johnbird_5_5(),
		engine.johnbird_5_5(),
		engine.johnbird_5_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_7():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_7(),        
		engine.johnbird_5_7(),
		engine.johnbird_5_7(),
		engine.johnbird_5_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_13():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_13(),        
		engine.johnbird_5_13(),
		engine.johnbird_5_13(),
		engine.johnbird_5_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_16():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_16(),        
		engine.johnbird_5_16(),
		engine.johnbird_5_16(),
		engine.johnbird_5_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_5_17():
	def __init__(self):
		instance_list = [
		engine.johnbird_5_17(),        
		engine.johnbird_5_17(),
		engine.johnbird_5_17(),
		engine.johnbird_5_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_1_a():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_1_a(),        
		engine.johnbird_6_1_a(),
		engine.johnbird_6_1_a(),
		engine.johnbird_6_1_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_1_b():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_1_b(),        
		engine.johnbird_6_1_b(),
		engine.johnbird_6_1_b(),
		engine.johnbird_6_1_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_2(),        
		engine.johnbird_6_2(),
		engine.johnbird_6_2(),
		engine.johnbird_6_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_3(),        
		engine.johnbird_6_3(),
		engine.johnbird_6_3(),
		engine.johnbird_6_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_4(),        
		engine.johnbird_6_4(),
		engine.johnbird_6_4(),
		engine.johnbird_6_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_5():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_5(),        
		engine.johnbird_6_5(),
		engine.johnbird_6_5(),
		engine.johnbird_6_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_6():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_6(),        
		engine.johnbird_6_6(),
		engine.johnbird_6_6(),
		engine.johnbird_6_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_8():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_8(),        
		engine.johnbird_6_8(),
		engine.johnbird_6_8(),
		engine.johnbird_6_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_9():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_9(),        
		engine.johnbird_6_9(),
		engine.johnbird_6_9(),
		engine.johnbird_6_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_10():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_10(),        
		engine.johnbird_6_10(),
		engine.johnbird_6_10(),
		engine.johnbird_6_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_11():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_11(),        
		engine.johnbird_6_11(),
		engine.johnbird_6_11(),
		engine.johnbird_6_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_12():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_12(),        
		engine.johnbird_6_12(),
		engine.johnbird_6_12(),
		engine.johnbird_6_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_13():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_13(),        
		engine.johnbird_6_13(),
		engine.johnbird_6_13(),
		engine.johnbird_6_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_15():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_15(),        
		engine.johnbird_6_15(),
		engine.johnbird_6_15(),
		engine.johnbird_6_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_16():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_16(),        
		engine.johnbird_6_16(),
		engine.johnbird_6_16(),
		engine.johnbird_6_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_17():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_17(),        
		engine.johnbird_6_17(),
		engine.johnbird_6_17(),
		engine.johnbird_6_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_6_18():
	def __init__(self):
		instance_list = [
		engine.johnbird_6_18(),        
		engine.johnbird_6_18(),
		engine.johnbird_6_18(),
		engine.johnbird_6_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_1():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_1(),        
		engine.johnbird_7_1(),
		engine.johnbird_7_1(),
		engine.johnbird_7_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_2(),        
		engine.johnbird_7_2(),
		engine.johnbird_7_2(),
		engine.johnbird_7_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_3(),        
		engine.johnbird_7_3(),
		engine.johnbird_7_3(),
		engine.johnbird_7_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_4(),        
		engine.johnbird_7_4(),
		engine.johnbird_7_4(),
		engine.johnbird_7_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_5():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_5(),        
		engine.johnbird_7_5(),
		engine.johnbird_7_5(),
		engine.johnbird_7_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_6():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_6(),        
		engine.johnbird_7_6(),
		engine.johnbird_7_6(),
		engine.johnbird_7_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_7():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_7(),        
		engine.johnbird_7_7(),
		engine.johnbird_7_7(),
		engine.johnbird_7_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_8():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_8(),        
		engine.johnbird_7_8(),
		engine.johnbird_7_8(),
		engine.johnbird_7_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_9():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_9(),        
		engine.johnbird_7_9(),
		engine.johnbird_7_9(),
		engine.johnbird_7_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_10():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_10(),        
		engine.johnbird_7_10(),
		engine.johnbird_7_10(),
		engine.johnbird_7_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_11():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_11(),        
		engine.johnbird_7_11(),
		engine.johnbird_7_11(),
		engine.johnbird_7_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_7_12():
	def __init__(self):
		instance_list = [
		engine.johnbird_7_12(),        
		engine.johnbird_7_12(),
		engine.johnbird_7_12(),
		engine.johnbird_7_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_8_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_8_2(),        
		engine.johnbird_8_2(),
		engine.johnbird_8_2(),
		engine.johnbird_8_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_8_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_8_3(),        
		engine.johnbird_8_3(),
		engine.johnbird_8_3(),
		engine.johnbird_8_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_8_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_8_4(),        
		engine.johnbird_8_4(),
		engine.johnbird_8_4(),
		engine.johnbird_8_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_8_6():
	def __init__(self):
		instance_list = [
		engine.johnbird_8_6(),        
		engine.johnbird_8_6(),
		engine.johnbird_8_6(),
		engine.johnbird_8_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_8_7():
	def __init__(self):
		instance_list = [
		engine.johnbird_8_7(),        
		engine.johnbird_8_7(),
		engine.johnbird_8_7(),
		engine.johnbird_8_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_1():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_1(),        
		engine.johnbird_9_1(),
		engine.johnbird_9_1(),
		engine.johnbird_9_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_2(),        
		engine.johnbird_9_2(),
		engine.johnbird_9_2(),
		engine.johnbird_9_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_3():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_3(),        
		engine.johnbird_9_3(),
		engine.johnbird_9_3(),
		engine.johnbird_9_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_4(),        
		engine.johnbird_9_4(),
		engine.johnbird_9_4(),
		engine.johnbird_9_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_6():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_6(),        
		engine.johnbird_9_6(),
		engine.johnbird_9_6(),
		engine.johnbird_9_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_7():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_7(),        
		engine.johnbird_9_7(),
		engine.johnbird_9_7(),
		engine.johnbird_9_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_8():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_8(),        
		engine.johnbird_9_8(),
		engine.johnbird_9_8(),
		engine.johnbird_9_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_9():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_9(),        
		engine.johnbird_9_9(),
		engine.johnbird_9_9(),
		engine.johnbird_9_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_10():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_10(),        
		engine.johnbird_9_10(),
		engine.johnbird_9_10(),
		engine.johnbird_9_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_11():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_11(),        
		engine.johnbird_9_11(),
		engine.johnbird_9_11(),
		engine.johnbird_9_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_12():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_12(),        
		engine.johnbird_9_12(),
		engine.johnbird_9_12(),
		engine.johnbird_9_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_13():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_13(),        
		engine.johnbird_9_13(),
		engine.johnbird_9_13(),
		engine.johnbird_9_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_14():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_14(),        
		engine.johnbird_9_14(),
		engine.johnbird_9_14(),
		engine.johnbird_9_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_15():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_15(),        
		engine.johnbird_9_15(),
		engine.johnbird_9_15(),
		engine.johnbird_9_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_16():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_16(),        
		engine.johnbird_9_16(),
		engine.johnbird_9_16(),
		engine.johnbird_9_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_17():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_17(),        
		engine.johnbird_9_17(),
		engine.johnbird_9_17(),
		engine.johnbird_9_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_18():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_18(),        
		engine.johnbird_9_18(),
		engine.johnbird_9_18(),
		engine.johnbird_9_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_19():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_19(),        
		engine.johnbird_9_19(),
		engine.johnbird_9_19(),
		engine.johnbird_9_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_9_20():
	def __init__(self):
		instance_list = [
		engine.johnbird_9_20(),        
		engine.johnbird_9_20(),
		engine.johnbird_9_20(),
		engine.johnbird_9_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_1():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_1(),        
		engine.johnbird_10_1(),
		engine.johnbird_10_1(),
		engine.johnbird_10_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_2():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_2(),        
		engine.johnbird_10_2(),
		engine.johnbird_10_2(),
		engine.johnbird_10_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_4():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_4(),        
		engine.johnbird_10_4(),
		engine.johnbird_10_4(),
		engine.johnbird_10_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_18():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_18(),        
		engine.johnbird_10_18(),
		engine.johnbird_10_18(),
		engine.johnbird_10_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_19():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_19(),        
		engine.johnbird_10_19(),
		engine.johnbird_10_19(),
		engine.johnbird_10_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_20():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_20(),        
		engine.johnbird_10_20(),
		engine.johnbird_10_20(),
		engine.johnbird_10_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_21():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_21(),        
		engine.johnbird_10_21(),
		engine.johnbird_10_21(),
		engine.johnbird_10_21()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_22():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_22(),        
		engine.johnbird_10_22(),
		engine.johnbird_10_22(),
		engine.johnbird_10_22()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_23():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_23(),        
		engine.johnbird_10_23(),
		engine.johnbird_10_23(),
		engine.johnbird_10_23()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class johnbird_10_24():
	def __init__(self):
		instance_list = [
		engine.johnbird_10_24(),        
		engine.johnbird_10_24(),
		engine.johnbird_10_24(),
		engine.johnbird_10_24()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		


		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		