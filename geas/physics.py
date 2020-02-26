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

class example_2_1():
	def __init__(self):
		instance_list = [
		engine.example_2_1(),        
		engine.example_2_1(),
		engine.example_2_1(),
		engine.example_2_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_2():
	def __init__(self):
		instance_list = [
		engine.example_2_2(),        
		engine.example_2_2(),
		engine.example_2_2(),
		engine.example_2_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_3():
	def __init__(self):
		instance_list = [
		engine.example_2_3(),        
		engine.example_2_3(),
		engine.example_2_3(),
		engine.example_2_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_4():
	def __init__(self):
		instance_list = [
		engine.example_2_4(),        
		engine.example_2_4(),
		engine.example_2_4(),
		engine.example_2_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_8():
	def __init__(self):
		instance_list = [
		engine.example_2_8(),        
		engine.example_2_8(),
		engine.example_2_8(),
		engine.example_2_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_9():
	def __init__(self):
		instance_list = [
		engine.example_2_9(),        
		engine.example_2_9(),
		engine.example_2_9(),
		engine.example_2_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_10():
	def __init__(self):
		instance_list = [
		engine.example_2_10(),        
		engine.example_2_10(),
		engine.example_2_10(),
		engine.example_2_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_11():
	def __init__(self):
		instance_list = [
		engine.example_2_11(),        
		engine.example_2_11(),
		engine.example_2_11(),
		engine.example_2_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_12():
	def __init__(self):
		instance_list = [
		engine.example_2_12(),        
		engine.example_2_12(),
		engine.example_2_12(),
		engine.example_2_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_13():
	def __init__(self):
		instance_list = [
		engine.example_2_13(),        
		engine.example_2_13(),
		engine.example_2_13(),
		engine.example_2_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_14():
	def __init__(self):
		instance_list = [
		engine.example_2_14(),        
		engine.example_2_14(),
		engine.example_2_14(),
		engine.example_2_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_15():
	def __init__(self):
		instance_list = [
		engine.example_2_15(),        
		engine.example_2_15(),
		engine.example_2_15(),
		engine.example_2_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_16():
	def __init__(self):
		instance_list = [
		engine.example_2_16(),        
		engine.example_2_16(),
		engine.example_2_16(),
		engine.example_2_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_17():
	def __init__(self):
		instance_list = [
		engine.example_2_17(),        
		engine.example_2_17(),
		engine.example_2_17(),
		engine.example_2_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_18():
	def __init__(self):
		instance_list = [
		engine.example_2_18(),        
		engine.example_2_18(),
		engine.example_2_18(),
		engine.example_2_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_19():
	def __init__(self):
		instance_list = [
		engine.example_2_19(),        
		engine.example_2_19(),
		engine.example_2_19(),
		engine.example_2_19()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_20():
	def __init__(self):
		instance_list = [
		engine.example_2_20(),        
		engine.example_2_20(),
		engine.example_2_20(),
		engine.example_2_20()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class example_2_21():
	def __init__(self):
		instance_list = [
		engine.example_2_21(),        
		engine.example_2_21(),
		engine.example_2_21(),
		engine.example_2_21()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

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



class Schaums_15_1():
	def __init__(self):
		instance_list = [
		engine.schaums_15_1(),        
		engine.schaums_15_1(),
		engine.schaums_15_1(),
		engine.schaums_15_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_15_2():
	def __init__(self):
		instance_list = [
		engine.schaums_15_2(),        
		engine.schaums_15_2(),
		engine.schaums_15_2(),
		engine.schaums_15_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_15_3():
	def __init__(self):
		instance_list = [
		engine.schaums_15_3(),        
		engine.schaums_15_3(),
		engine.schaums_15_3(),
		engine.schaums_15_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_15_4():
	def __init__(self):
		instance_list = [
		engine.schaums_15_4(),        
		engine.schaums_15_4(),
		engine.schaums_15_4(),
		engine.schaums_15_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_15_5():
	def __init__(self):
		instance_list = [
		engine.schaums_15_5(),        
		engine.schaums_15_5(),
		engine.schaums_15_5(),
		engine.schaums_15_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_15_6():
	def __init__(self):
		instance_list = [
		engine.schaums_15_6(),        
		engine.schaums_15_6(),
		engine.schaums_15_6(),
		engine.schaums_15_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer       

class Schaums_15_7():
	def __init__(self):
		instance_list = [
		engine.schaums_15_7(),        
		engine.schaums_15_7(),
		engine.schaums_15_7(),
		engine.schaums_15_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer         

class Schaums_15_8():
	def __init__(self):
		instance_list = [
		engine.schaums_15_8(),        
		engine.schaums_15_8(),
		engine.schaums_15_8(),
		engine.schaums_15_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_15_9():
	def __init__(self):
		instance_list = [
		engine.schaums_15_9(),        
		engine.schaums_15_9(),
		engine.schaums_15_9(),
		engine.schaums_15_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_15_10():
	def __init__(self):
		instance_list = [
		engine.schaums_15_10(),        
		engine.schaums_15_10(),
		engine.schaums_15_10(),
		engine.schaums_15_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_16_1():
	def __init__(self):
		instance_list = [
		engine.schaums_16_1(),        
		engine.schaums_16_1(),
		engine.schaums_16_1(),
		engine.schaums_16_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_16_2():
	def __init__(self):
		instance_list = [
		engine.schaums_16_2(),        
		engine.schaums_16_2(),
		engine.schaums_16_2(),
		engine.schaums_16_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_16_3():
	def __init__(self):
		instance_list = [
		engine.schaums_16_3(),        
		engine.schaums_16_3(),
		engine.schaums_16_3(),
		engine.schaums_16_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_16_4():
	def __init__(self):
		instance_list = [
		engine.schaums_16_4(),        
		engine.schaums_16_4(),
		engine.schaums_16_4(),
		engine.schaums_16_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_16_5():
	def __init__(self):
		instance_list = [
		engine.schaums_16_5(),        
		engine.schaums_16_5(),
		engine.schaums_16_5(),
		engine.schaums_16_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_16_6():
	def __init__(self):
		instance_list = [
		engine.schaums_16_6(),        
		engine.schaums_16_6(),
		engine.schaums_16_6(),
		engine.schaums_16_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              

class Schaums_16_7():
	def __init__(self):
		instance_list = [
		engine.schaums_16_7(),        
		engine.schaums_16_7(),
		engine.schaums_16_7(),
		engine.schaums_16_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 

class Schaums_16_8():
	def __init__(self):
		instance_list = [
		engine.schaums_16_8(),        
		engine.schaums_16_8(),
		engine.schaums_16_8(),
		engine.schaums_16_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_16_9():
	def __init__(self):
		instance_list = [
		engine.schaums_16_9(),        
		engine.schaums_16_9(),
		engine.schaums_16_9(),
		engine.schaums_16_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_16_10():
	def __init__(self):
		instance_list = [
		engine.schaums_16_10(),        
		engine.schaums_16_10(),
		engine.schaums_16_10(),
		engine.schaums_16_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_16_11():
	def __init__(self):
		instance_list = [
		engine.schaums_16_11(),        
		engine.schaums_16_11(),
		engine.schaums_16_11(),
		engine.schaums_16_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_16_12():
	def __init__(self):
		instance_list = [
		engine.schaums_16_12(),        
		engine.schaums_16_12(),
		engine.schaums_16_12(),
		engine.schaums_16_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_16_13():
	def __init__(self):
		instance_list = [
		engine.schaums_16_13(),        
		engine.schaums_16_13(),
		engine.schaums_16_13(),
		engine.schaums_16_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_16_14():
	def __init__(self):
		instance_list = [
		engine.schaums_16_14(),        
		engine.schaums_16_14(),
		engine.schaums_16_14(),
		engine.schaums_16_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_16_15():
	def __init__(self):
		instance_list = [
		engine.schaums_16_15(),        
		engine.schaums_16_15(),
		engine.schaums_16_15(),
		engine.schaums_16_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_16_16():
	def __init__(self):
		instance_list = [
		engine.schaums_16_16(),        
		engine.schaums_16_16(),
		engine.schaums_16_16(),
		engine.schaums_16_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              

class Schaums_16_17():
	def __init__(self):
		instance_list = [
		engine.schaums_16_17(),        
		engine.schaums_16_17(),
		engine.schaums_16_17(),
		engine.schaums_16_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 

class Schaums_16_18():
	def __init__(self):
		instance_list = [
		engine.schaums_16_18(),        
		engine.schaums_16_18(),
		engine.schaums_16_18(),
		engine.schaums_16_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_17_1():
	def __init__(self):
		instance_list = [
		engine.schaums_17_1(),        
		engine.schaums_17_1(),
		engine.schaums_17_1(),
		engine.schaums_17_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_17_2():
	def __init__(self):
		instance_list = [
		engine.schaums_17_2(),        
		engine.schaums_17_2(),
		engine.schaums_17_2(),
		engine.schaums_17_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_17_3():
	def __init__(self):
		instance_list = [
		engine.schaums_17_3(),        
		engine.schaums_17_3(),
		engine.schaums_17_3(),
		engine.schaums_17_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_17_4():
	def __init__(self):
		instance_list = [
		engine.schaums_17_4(),        
		engine.schaums_17_4(),
		engine.schaums_17_4(),
		engine.schaums_17_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_17_5():
	def __init__(self):
		instance_list = [
		engine.schaums_17_5(),        
		engine.schaums_17_5(),
		engine.schaums_17_5(),
		engine.schaums_17_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_17_6():
	def __init__(self):
		instance_list = [
		engine.schaums_17_6(),        
		engine.schaums_17_6(),
		engine.schaums_17_6(),
		engine.schaums_17_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_17_7():
	def __init__(self):
		instance_list = [
		engine.schaums_17_7(),        
		engine.schaums_17_7(),
		engine.schaums_17_7(),
		engine.schaums_17_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer           

class Schaums_17_8():
	def __init__(self):
		instance_list = [
		engine.schaums_17_8(),        
		engine.schaums_17_8(),
		engine.schaums_17_8(),
		engine.schaums_17_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_17_9():
	def __init__(self):
		instance_list = [
		engine.schaums_17_9(),        
		engine.schaums_17_9(),
		engine.schaums_17_9(),
		engine.schaums_17_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_17_10():
	def __init__(self):
		instance_list = [
		engine.schaums_17_10(),        
		engine.schaums_17_10(),
		engine.schaums_17_10(),
		engine.schaums_17_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_17_11():
	def __init__(self):
		instance_list = [
		engine.schaums_17_11(),        
		engine.schaums_17_11(),
		engine.schaums_17_11(),
		engine.schaums_17_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_17_12():
	def __init__(self):
		instance_list = [
		engine.schaums_17_12(),        
		engine.schaums_17_12(),
		engine.schaums_17_12(),
		engine.schaums_17_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer

class Schaums_18_1():
	def __init__(self):
		instance_list = [
		engine.schaums_18_1(),        
		engine.schaums_18_1(),
		engine.schaums_18_1(),
		engine.schaums_18_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_18_2():
	def __init__(self):
		instance_list = [
		engine.schaums_18_2(),        
		engine.schaums_18_2(),
		engine.schaums_18_2(),
		engine.schaums_18_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_18_3():
	def __init__(self):
		instance_list = [
		engine.schaums_18_3(),        
		engine.schaums_18_3(),
		engine.schaums_18_3(),
		engine.schaums_18_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_18_4():
	def __init__(self):
		instance_list = [
		engine.schaums_18_4(),        
		engine.schaums_18_4(),
		engine.schaums_18_4(),
		engine.schaums_18_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_18_5():
	def __init__(self):
		instance_list = [
		engine.schaums_18_5(),        
		engine.schaums_18_5(),
		engine.schaums_18_5(),
		engine.schaums_18_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_18_6():
	def __init__(self):
		instance_list = [
		engine.schaums_18_6(),        
		engine.schaums_18_6(),
		engine.schaums_18_6(),
		engine.schaums_18_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer     

class Schaums_18_7():
	def __init__(self):
		instance_list = [
		engine.schaums_18_7(),        
		engine.schaums_18_7(),
		engine.schaums_18_7(),
		engine.schaums_18_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer          

class Schaums_18_8():
	def __init__(self):
		instance_list = [
		engine.schaums_18_8(),        
		engine.schaums_18_8(),
		engine.schaums_18_8(),
		engine.schaums_18_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_18_9():
	def __init__(self):
		instance_list = [
		engine.schaums_18_9(),        
		engine.schaums_18_9(),
		engine.schaums_18_9(),
		engine.schaums_18_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_18_10():
	def __init__(self):
		instance_list = [
		engine.schaums_18_10(),        
		engine.schaums_18_10(),
		engine.schaums_18_10(),
		engine.schaums_18_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_18_11():
	def __init__(self):
		instance_list = [
		engine.schaums_18_11(),        
		engine.schaums_18_11(),
		engine.schaums_18_11(),
		engine.schaums_18_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_18_12():
	def __init__(self):
		instance_list = [
		engine.schaums_18_12(),        
		engine.schaums_18_12(),
		engine.schaums_18_12(),
		engine.schaums_18_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_18_13():
	def __init__(self):
		instance_list = [
		engine.schaums_18_13(),        
		engine.schaums_18_13(),
		engine.schaums_18_13(),
		engine.schaums_18_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_18_14():
	def __init__(self):
		instance_list = [
		engine.schaums_18_14(),        
		engine.schaums_18_14(),
		engine.schaums_18_14(),
		engine.schaums_18_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_18_15():
	def __init__(self):
		instance_list = [
		engine.schaums_18_15(),        
		engine.schaums_18_15(),
		engine.schaums_18_15(),
		engine.schaums_18_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_18_16():
	def __init__(self):
		instance_list = [
		engine.schaums_18_16(),        
		engine.schaums_18_16(),
		engine.schaums_18_16(),
		engine.schaums_18_16()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              

class Schaums_18_17():
	def __init__(self):
		instance_list = [
		engine.schaums_18_17(),        
		engine.schaums_18_17(),
		engine.schaums_18_17(),
		engine.schaums_18_17()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 

class Schaums_18_18():
	def __init__(self):
		instance_list = [
		engine.schaums_18_18(),        
		engine.schaums_18_18(),
		engine.schaums_18_18(),
		engine.schaums_18_18()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_19_1():
	def __init__(self):
		instance_list = [
		engine.schaums_19_1(),        
		engine.schaums_19_1(),
		engine.schaums_19_1(),
		engine.schaums_19_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_19_2():
	def __init__(self):
		instance_list = [
		engine.schaums_19_2(),        
		engine.schaums_19_2(),
		engine.schaums_19_2(),
		engine.schaums_19_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_19_3():
	def __init__(self):
		instance_list = [
		engine.schaums_19_3(),        
		engine.schaums_19_3(),
		engine.schaums_19_3(),
		engine.schaums_19_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_19_4():
	def __init__(self):
		instance_list = [
		engine.schaums_19_4(),        
		engine.schaums_19_4(),
		engine.schaums_19_4(),
		engine.schaums_19_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_19_5():
	def __init__(self):
		instance_list = [
		engine.schaums_19_5(),        
		engine.schaums_19_5(),
		engine.schaums_19_5(),
		engine.schaums_19_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_19_6():
	def __init__(self):
		instance_list = [
		engine.schaums_19_6(),        
		engine.schaums_19_6(),
		engine.schaums_19_6(),
		engine.schaums_19_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              

class Schaums_19_7():
	def __init__(self):
		instance_list = [
		engine.schaums_19_7(),        
		engine.schaums_19_7(),
		engine.schaums_19_7(),
		engine.schaums_19_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 

class Schaums_19_8():
	def __init__(self):
		instance_list = [
		engine.schaums_19_8(),        
		engine.schaums_19_8(),
		engine.schaums_19_8(),
		engine.schaums_19_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   

class Schaums_20_1():
	def __init__(self):
		instance_list = [
		engine.schaums_20_1(),        
		engine.schaums_20_1(),
		engine.schaums_20_1(),
		engine.schaums_20_1()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_20_2():
	def __init__(self):
		instance_list = [
		engine.schaums_20_2(),        
		engine.schaums_20_2(),
		engine.schaums_20_2(),
		engine.schaums_20_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_20_3():
	def __init__(self):
		instance_list = [
		engine.schaums_20_3(),        
		engine.schaums_20_3(),
		engine.schaums_20_3(),
		engine.schaums_20_3()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_20_4():
	def __init__(self):
		instance_list = [
		engine.schaums_20_4(),        
		engine.schaums_20_4(),
		engine.schaums_20_4(),
		engine.schaums_20_4()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_20_5():
	def __init__(self):
		instance_list = [
		engine.schaums_20_5(),        
		engine.schaums_20_5(),
		engine.schaums_20_5(),
		engine.schaums_20_5()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_20_6():
	def __init__(self):
		instance_list = [
		engine.schaums_20_6(),        
		engine.schaums_20_6(),
		engine.schaums_20_6(),
		engine.schaums_20_6()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        

class Schaums_20_7():
	def __init__(self):
		instance_list = [
		engine.schaums_20_7(),        
		engine.schaums_20_7(),
		engine.schaums_20_7(),
		engine.schaums_20_7()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer       

class Schaums_20_8():
	def __init__(self):
		instance_list = [
		engine.schaums_20_8(),        
		engine.schaums_20_8(),
		engine.schaums_20_8(),
		engine.schaums_20_8()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer      
		
class Schaums_20_9():
	def __init__(self):
		instance_list = [
		engine.schaums_20_9(),        
		engine.schaums_20_9(),
		engine.schaums_20_9(),
		engine.schaums_20_9()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer   
		
class Schaums_20_10():
	def __init__(self):
		instance_list = [
		engine.schaums_20_10(),        
		engine.schaums_20_10(),
		engine.schaums_20_10(),
		engine.schaums_20_10()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  

class Schaums_20_11():
	def __init__(self):
		instance_list = [
		engine.schaums_20_11(),        
		engine.schaums_20_11(),
		engine.schaums_20_11(),
		engine.schaums_20_11()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_20_12():
	def __init__(self):
		instance_list = [
		engine.schaums_20_12(),        
		engine.schaums_20_12(),
		engine.schaums_20_12(),
		engine.schaums_20_12()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer
		
class Schaums_20_13():
	def __init__(self):
		instance_list = [
		engine.schaums_20_13(),        
		engine.schaums_20_13(),
		engine.schaums_20_13(),
		engine.schaums_20_13()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer        
		
class Schaums_20_14():
	def __init__(self):
		instance_list = [
		engine.schaums_20_14(),        
		engine.schaums_20_14(),
		engine.schaums_20_14(),
		engine.schaums_20_14()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class Schaums_20_15():
	def __init__(self):
		instance_list = [
		engine.schaums_20_15(),        
		engine.schaums_20_15(),
		engine.schaums_20_15(),
		engine.schaums_20_15()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer              
		
class Schaums_20_16():
	def __init__(self):
		instance_list = [
		engine.schaums_20_16(),        
		engine.schaums_20_16(),
		engine.schaums_20_16(),
		engine.schaums_20_16()        
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
		
		



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		