import random
from mathsub import trigonometry_engine as engine
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

class median():
	def __init__(self):
		instance_list = [
		engine.median(),        
		engine.median(),
		engine.median(),
		engine.median()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class angular_bisector():
	def __init__(self):
		instance_list = [
		engine.angular_bisector(),        
		engine.angular_bisector(),
		engine.angular_bisector(),
		engine.angular_bisector()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class altitude():
	def __init__(self):
		instance_list = [
		engine.altitude(),        
		engine.altitude(),
		engine.altitude(),
		engine.altitude()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class inradius_SSS():
	def __init__(self):
		instance_list = [
		engine.inradius_SSS(),        
		engine.inradius_SSS(),
		engine.inradius_SSS(),
		engine.inradius_SSS()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class inradius_SAS():
	def __init__(self):
		instance_list = [
		engine.inradius_SAS(),        
		engine.inradius_SAS(),
		engine.inradius_SAS(),
		engine.inradius_SAS()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class inradius_ASA():
	def __init__(self):
		instance_list = [
		engine.inradius_ASA(),        
		engine.inradius_ASA(),
		engine.inradius_ASA(),
		engine.inradius_ASA()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class inradius():
	def __init__(self):
		instance_list = [
		engine.inradius(),        
		engine.inradius(),
		engine.inradius(),
		engine.inradius()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class circumradius():
	def __init__(self):
		instance_list = [
		engine.circumradius(),        
		engine.circumradius(),
		engine.circumradius(),
		engine.circumradius()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class exradius():
	def __init__(self):
		instance_list = [
		engine.exradius(),        
		engine.exradius(),
		engine.exradius(),
		engine.exradius()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class identity():
	def __init__(self):
		instance_list = [
		engine.identity(),        
		engine.identity(),
		engine.identity(),
		engine.identity()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class area():
	def __init__(self):
		instance_list = [
		engine.area(),        
		engine.area(),
		engine.area(),
		engine.area()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class airplane():
	def __init__(self):
		instance_list = [
		engine.airplane(),        
		engine.airplane(),
		engine.airplane(),
		engine.airplane()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class elevation_person_building():
	def __init__(self):
		instance_list = [
		engine.elevation_person_building(),        
		engine.elevation_person_building(),
		engine.elevation_person_building(),
		engine.elevation_person_building()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class elevation_two_person_building():
	def __init__(self):
		instance_list = [
		engine.elevation_two_person_building(),        
		engine.elevation_two_person_building(),
		engine.elevation_two_person_building(),
		engine.elevation_two_person_building()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class inclined_post():
	def __init__(self):
		instance_list = [
		engine.inclined_post(),        
		engine.inclined_post(),
		engine.inclined_post(),
		engine.inclined_post()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 
