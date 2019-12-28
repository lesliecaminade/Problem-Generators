import random
from geas import strength_of_materials_engine as engine
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
		
class singer_104():
	def __init__(self):
		instance_list = [
		engine.singer_104(),        
		engine.singer_104(),
		engine.singer_104(),
		engine.singer_104()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class singer_105():
	def __init__(self):
		instance_list = [
		engine.singer_105(),        
		engine.singer_105(),
		engine.singer_105(),
		engine.singer_105()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class singer_106():
	def __init__(self):
		instance_list = [
		engine.singer_106(),        
		engine.singer_106(),
		engine.singer_106(),
		engine.singer_106()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    

class singer_107():
	def __init__(self):
		instance_list = [
		engine.singer_107(),        
		engine.singer_107(),
		engine.singer_107(),
		engine.singer_107()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_108():
	def __init__(self):
		instance_list = [
		engine.singer_108(),        
		engine.singer_108(),
		engine.singer_108(),
		engine.singer_108()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_109():
	def __init__(self):
		instance_list = [
		engine.singer_109(),        
		engine.singer_109(),
		engine.singer_109(),
		engine.singer_109()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_110():
	def __init__(self):
		instance_list = [
		engine.singer_110(),        
		engine.singer_110(),
		engine.singer_110(),
		engine.singer_110()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_115():
	def __init__(self):
		instance_list = [
		engine.singer_115(),        
		engine.singer_115(),
		engine.singer_115(),
		engine.singer_115()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_116():
	def __init__(self):
		instance_list = [
		engine.singer_116(),        
		engine.singer_116(),
		engine.singer_116(),
		engine.singer_116()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_117():
	def __init__(self):
		instance_list = [
		engine.singer_117(),        
		engine.singer_117(),
		engine.singer_117(),
		engine.singer_117()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_125():
	def __init__(self):
		instance_list = [
		engine.singer_125(),        
		engine.singer_125(),
		engine.singer_125(),
		engine.singer_125()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_126():
	def __init__(self):
		instance_list = [
		engine.singer_126(),        
		engine.singer_126(),
		engine.singer_126(),
		engine.singer_126()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_127():
	def __init__(self):
		instance_list = [
		engine.singer_127(),        
		engine.singer_127(),
		engine.singer_127(),
		engine.singer_127()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_133():
	def __init__(self):
		instance_list = [
		engine.singer_133(),        
		engine.singer_133(),
		engine.singer_133(),
		engine.singer_133()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_134():
	def __init__(self):
		instance_list = [
		engine.singer_134(),        
		engine.singer_134(),
		engine.singer_134(),
		engine.singer_134()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_135():
	def __init__(self):
		instance_list = [
		engine.singer_135(),        
		engine.singer_135(),
		engine.singer_135(),
		engine.singer_135()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_136():
	def __init__(self):
		instance_list = [
		engine.singer_136(),        
		engine.singer_136(),
		engine.singer_136(),
		engine.singer_136()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_138():
	def __init__(self):
		instance_list = [
		engine.singer_138(),        
		engine.singer_138(),
		engine.singer_138(),
		engine.singer_138()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_141():
	def __init__(self):
		instance_list = [
		engine.singer_141(),        
		engine.singer_141(),
		engine.singer_141(),
		engine.singer_141()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_142():
	def __init__(self):
		instance_list = [
		engine.singer_142(),        
		engine.singer_142(),
		engine.singer_142(),
		engine.singer_142()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_206():
	def __init__(self):
		instance_list = [
		engine.singer_206(),        
		engine.singer_206(),
		engine.singer_206(),
		engine.singer_206()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_207():
	def __init__(self):
		instance_list = [
		engine.singer_207(),        
		engine.singer_207(),
		engine.singer_207(),
		engine.singer_207()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_208():
	def __init__(self):
		instance_list = [
		engine.singer_208(),        
		engine.singer_208(),
		engine.singer_208(),
		engine.singer_208()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_209():
	def __init__(self):
		instance_list = [
		engine.singer_209(),        
		engine.singer_209(),
		engine.singer_209(),
		engine.singer_209()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_211():
	def __init__(self):
		instance_list = [
		engine.singer_211(),        
		engine.singer_211(),
		engine.singer_211(),
		engine.singer_211()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_223():
	def __init__(self):
		instance_list = [
		engine.singer_223(),        
		engine.singer_223(),
		engine.singer_223(),
		engine.singer_223()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_225():
	def __init__(self):
		instance_list = [
		engine.singer_225(),        
		engine.singer_225(),
		engine.singer_225(),
		engine.singer_225()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_226():
	def __init__(self):
		instance_list = [
		engine.singer_226(),        
		engine.singer_226(),
		engine.singer_226(),
		engine.singer_226()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_227():
	def __init__(self):
		instance_list = [
		engine.singer_227(),        
		engine.singer_227(),
		engine.singer_227(),
		engine.singer_227()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_228():
	def __init__(self):
		instance_list = [
		engine.singer_228(),        
		engine.singer_228(),
		engine.singer_228(),
		engine.singer_228()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_233():
	def __init__(self):
		instance_list = [
		engine.singer_233(),        
		engine.singer_233(),
		engine.singer_233(),
		engine.singer_233()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_234():
	def __init__(self):
		instance_list = [
		engine.singer_234(),        
		engine.singer_234(),
		engine.singer_234(),
		engine.singer_234()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_235():
	def __init__(self):
		instance_list = [
		engine.singer_235(),        
		engine.singer_235(),
		engine.singer_235(),
		engine.singer_235()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_236():
	def __init__(self):
		instance_list = [
		engine.singer_236(),        
		engine.singer_236(),
		engine.singer_236(),
		engine.singer_236()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_238():
	def __init__(self):
		instance_list = [
		engine.singer_238(),        
		engine.singer_238(),
		engine.singer_238(),
		engine.singer_238()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_239():
	def __init__(self):
		instance_list = [
		engine.singer_239(),        
		engine.singer_239(),
		engine.singer_239(),
		engine.singer_239()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_240():
	def __init__(self):
		instance_list = [
		engine.singer_240(),        
		engine.singer_240(),
		engine.singer_240(),
		engine.singer_240()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_241():
	def __init__(self):
		instance_list = [
		engine.singer_241(),        
		engine.singer_241(),
		engine.singer_241(),
		engine.singer_241()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_244():
	def __init__(self):
		instance_list = [
		engine.singer_244(),        
		engine.singer_244(),
		engine.singer_244(),
		engine.singer_244()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_245():
	def __init__(self):
		instance_list = [
		engine.singer_245(),        
		engine.singer_245(),
		engine.singer_245(),
		engine.singer_245()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_247():
	def __init__(self):
		instance_list = [
		engine.singer_247(),        
		engine.singer_247(),
		engine.singer_247(),
		engine.singer_247()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_261():
	def __init__(self):
		instance_list = [
		engine.singer_261(),        
		engine.singer_261(),
		engine.singer_261(),
		engine.singer_261()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_262():
	def __init__(self):
		instance_list = [
		engine.singer_262(),        
		engine.singer_262(),
		engine.singer_262(),
		engine.singer_262()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_263():
	def __init__(self):
		instance_list = [
		engine.singer_263(),        
		engine.singer_263(),
		engine.singer_263(),
		engine.singer_263()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_264():
	def __init__(self):
		instance_list = [
		engine.singer_264(),        
		engine.singer_264(),
		engine.singer_264(),
		engine.singer_264()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_265():
	def __init__(self):
		instance_list = [
		engine.singer_265(),        
		engine.singer_265(),
		engine.singer_265(),
		engine.singer_265()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_266():
	def __init__(self):
		instance_list = [
		engine.singer_266(),        
		engine.singer_266(),
		engine.singer_266(),
		engine.singer_266()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_267():
	def __init__(self):
		instance_list = [
		engine.singer_267(),        
		engine.singer_267(),
		engine.singer_267(),
		engine.singer_267()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_304():
	def __init__(self):
		instance_list = [
		engine.singer_304(),        
		engine.singer_304(),
		engine.singer_304(),
		engine.singer_304()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_305():
	def __init__(self):
		instance_list = [
		engine.singer_305(),        
		engine.singer_305(),
		engine.singer_305(),
		engine.singer_305()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_306():
	def __init__(self):
		instance_list = [
		engine.singer_306(),        
		engine.singer_306(),
		engine.singer_306(),
		engine.singer_306()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_307():
	def __init__(self):
		instance_list = [
		engine.singer_307(),        
		engine.singer_307(),
		engine.singer_307(),
		engine.singer_307()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_308():
	def __init__(self):
		instance_list = [
		engine.singer_308(),        
		engine.singer_308(),
		engine.singer_308(),
		engine.singer_308()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_309():
	def __init__(self):
		instance_list = [
		engine.singer_309(),        
		engine.singer_309(),
		engine.singer_309(),
		engine.singer_309()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_311():
	def __init__(self):
		instance_list = [
		engine.singer_311(),        
		engine.singer_311(),
		engine.singer_311(),
		engine.singer_311()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_312():
	def __init__(self):
		instance_list = [
		engine.singer_312(),        
		engine.singer_312(),
		engine.singer_312(),
		engine.singer_312()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    


class singer_313():
	def __init__(self):
		instance_list = [
		engine.singer_313(),        
		engine.singer_313(),
		engine.singer_313(),
		engine.singer_313()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer  
		



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		