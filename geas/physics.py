import random
from geas import physics_engine as engine
from num2words import num2words


def ask():
	ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
	return random.choice(ask_words)

def parse(string_input):
	string_input = str(string_input)
	return string_input.replace('**', '^').replace('*', ' ')

class Constructor():
	def __init__(self, engine_class_instances):
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

class Schaums_6_1():
	def __init__(self):
		instance_list = [
		engine.schaums_6_1(),        
		engine.schaums_6_1(),
		engine.schaums_6_1(),
		engine.schaums_6_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_6_2():
	def __init__(self):
		instance_list = [
		engine.schaums_6_2(),        
		engine.schaums_6_2(),
		engine.schaums_6_2(),
		engine.schaums_6_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_6_3():
	def __init__(self):
		instance_list = [
		engine.schaums_6_3(),        
		engine.schaums_6_3(),
		engine.schaums_6_3(),
		engine.schaums_6_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_6_4():
	def __init__(self):
		instance_list = [
		engine.schaums_6_4(),        
		engine.schaums_6_4(),
		engine.schaums_6_4(),
		engine.schaums_6_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer                
		
class Schaums_6_6():
	def __init__(self):
		instance_list = [
		engine.schaums_6_6(),        
		engine.schaums_6_6(),
		engine.schaums_6_6(),
		engine.schaums_6_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          
		
class Schaums_6_7():
	def __init__(self):
		instance_list = [
		engine.schaums_6_7(),        
		engine.schaums_6_7(),
		engine.schaums_6_7(),
		engine.schaums_6_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        

class Schaums_6_8():
	def __init__(self):
		instance_list = [
		engine.schaums_6_8(),        
		engine.schaums_6_8(),
		engine.schaums_6_8(),
		engine.schaums_6_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_6_9():
	def __init__(self):
		instance_list = [
		engine.schaums_6_9(),        
		engine.schaums_6_9(),
		engine.schaums_6_9(),
		engine.schaums_6_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_6_10():
	def __init__(self):
		instance_list = [
		engine.schaums_6_10(),        
		engine.schaums_6_10(),
		engine.schaums_6_10(),
		engine.schaums_6_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          
		
class Schaums_6_11():
	def __init__(self):
		instance_list = [
		engine.schaums_6_11(),        
		engine.schaums_6_11(),
		engine.schaums_6_11(),
		engine.schaums_6_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_6_13():
	def __init__(self):
		instance_list = [
		engine.schaums_6_13(),        
		engine.schaums_6_13(),
		engine.schaums_6_13(),
		engine.schaums_6_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer             
		
class Schaums_6_16():
	def __init__(self):
		instance_list = [
		engine.schaums_6_16(),        
		engine.schaums_6_16(),
		engine.schaums_6_16(),
		engine.schaums_6_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          
		
class Schaums_6_17():
	def __init__(self):
		instance_list = [
		engine.schaums_6_17(),        
		engine.schaums_6_17(),
		engine.schaums_6_17(),
		engine.schaums_6_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        

class Schaums_6_18():
	def __init__(self):
		instance_list = [
		engine.schaums_6_18(),        
		engine.schaums_6_18(),
		engine.schaums_6_18(),
		engine.schaums_6_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_6_19():
	def __init__(self):
		instance_list = [
		engine.schaums_6_19(),        
		engine.schaums_6_19(),
		engine.schaums_6_19(),
		engine.schaums_6_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   

class Schaums_6_20():
	def __init__(self):
		instance_list = [
		engine.schaums_6_20(),        
		engine.schaums_6_20(),
		engine.schaums_6_20(),
		engine.schaums_6_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 
		
class Schaums_6_21():
	def __init__(self):
		instance_list = [
		engine.schaums_6_21(),        
		engine.schaums_6_21(),
		engine.schaums_6_21(),
		engine.schaums_6_21()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
# class Schaums_6_22():
#     def __init__(self):
#         instance_list = [
#         engine.schaums_6_22(),        
#         engine.schaums_6_22(),
#         engine.schaums_6_22(),
#         engine.schaums_6_22()        
#         ]
#         constructed = Constructor(instance_list)
#         self.question = constructed.question
#         self.answer = constructed.answer
		
class Schaums_6_23():
	def __init__(self):
		instance_list = [
		engine.schaums_6_23(),        
		engine.schaums_6_23(),
		engine.schaums_6_23(),
		engine.schaums_6_23()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   


class Schaums_8_1():
	def __init__(self):
		instance_list = [
		engine.schaums_8_1(),        
		engine.schaums_8_1(),
		engine.schaums_8_1(),
		engine.schaums_8_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_8_2():
	def __init__(self):
		instance_list = [
		engine.schaums_8_2(),        
		engine.schaums_8_2(),
		engine.schaums_8_2(),
		engine.schaums_8_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_8_3():
	def __init__(self):
		instance_list = [
		engine.schaums_8_3(),        
		engine.schaums_8_3(),
		engine.schaums_8_3(),
		engine.schaums_8_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_8_4():
	def __init__(self):
		instance_list = [
		engine.schaums_8_4(),        
		engine.schaums_8_4(),
		engine.schaums_8_4(),
		engine.schaums_8_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_8_5():
	def __init__(self):
		instance_list = [
		engine.schaums_8_5(),        
		engine.schaums_8_5(),
		engine.schaums_8_5(),
		engine.schaums_8_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_8_6():
	def __init__(self):
		instance_list = [
		engine.schaums_8_6(),        
		engine.schaums_8_6(),
		engine.schaums_8_6(),
		engine.schaums_8_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              

class Schaums_8_8():
	def __init__(self):
		instance_list = [
		engine.schaums_8_8(),        
		engine.schaums_8_8(),
		engine.schaums_8_8(),
		engine.schaums_8_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_8_9():
	def __init__(self):
		instance_list = [
		engine.schaums_8_9(),        
		engine.schaums_8_9(),
		engine.schaums_8_9(),
		engine.schaums_8_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_8_10():
	def __init__(self):
		instance_list = [
		engine.schaums_8_10(),        
		engine.schaums_8_10(),
		engine.schaums_8_10(),
		engine.schaums_8_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_8_11():
	def __init__(self):
		instance_list = [
		engine.schaums_8_11(),        
		engine.schaums_8_11(),
		engine.schaums_8_11(),
		engine.schaums_8_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_8_12():
	def __init__(self):
		instance_list = [
		engine.schaums_8_12(),        
		engine.schaums_8_12(),
		engine.schaums_8_12(),
		engine.schaums_8_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_8_13():
	def __init__(self):
		instance_list = [
		engine.schaums_8_13(),        
		engine.schaums_8_13(),
		engine.schaums_8_13(),
		engine.schaums_8_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_8_14():
	def __init__(self):
		instance_list = [
		engine.schaums_8_14(),        
		engine.schaums_8_14(),
		engine.schaums_8_14(),
		engine.schaums_8_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer     

class Schaums_8_15():
	def __init__(self):
		instance_list = [
		engine.schaums_8_15(),        
		engine.schaums_8_15(),
		engine.schaums_8_15(),
		engine.schaums_8_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer             
		
class Schaums_8_16():
	def __init__(self):
		instance_list = [
		engine.schaums_8_16(),        
		engine.schaums_8_16(),
		engine.schaums_8_16(),
		engine.schaums_8_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          
		

class Schaums_8_17():
	def __init__(self):
		instance_list = [
		engine.schaums_8_17(),        
		engine.schaums_8_17(),
		engine.schaums_8_17(),
		engine.schaums_8_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 










		
   
class Serway_7_1():
	def __init__(self):
		instance_list = [
		engine.serway_7_1(),        
		engine.serway_7_1(),
		engine.serway_7_1(),
		engine.serway_7_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Serway_7_3():
	def __init__(self):
		instance_list = [
		engine.serway_7_3(),        
		engine.serway_7_3(),
		engine.serway_7_3(),
		engine.serway_7_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer                 
	
class Serway_7_5():
	def __init__(self):
		instance_list = [
		engine.serway_7_5(),        
		engine.serway_7_5(),
		engine.serway_7_5(),
		engine.serway_7_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer       
		
class Serway_7_6():
	def __init__(self):
		instance_list = [
		engine.serway_7_6(),        
		engine.serway_7_6(),
		engine.serway_7_6(),
		engine.serway_7_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          
		
class Serway_8_3():
	def __init__(self):
		instance_list = [
		engine.serway_8_3(),        
		engine.serway_8_3(),
		engine.serway_8_3(),
		engine.serway_8_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer                       
		
class Serway_8_6():
	def __init__(self):
		instance_list = [
		engine.serway_8_6(),        
		engine.serway_8_6(),
		engine.serway_8_6(),
		engine.serway_8_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          
		
class Serway_8_7():
	def __init__(self):
		instance_list = [
		engine.serway_8_7(),        
		engine.serway_8_7(),
		engine.serway_8_7(),
		engine.serway_8_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        

class Serway_8_8():
	def __init__(self):
		instance_list = [
		engine.serway_8_8(),        
		engine.serway_8_8(),
		engine.serway_8_8(),
		engine.serway_8_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Serway_8_11():
	def __init__(self):
		instance_list = [
		engine.serway_8_11(),        
		engine.serway_8_11(),
		engine.serway_8_11(),
		engine.serway_8_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
		



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		