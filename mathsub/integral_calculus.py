import random
from mathsub import integral_calculus_engine as engine
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
		
class besavilla_470_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_470_a(),        
		engine.besavilla_470_a(),
		engine.besavilla_470_a(),
		engine.besavilla_470_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_470_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_470_b(),        
		engine.besavilla_470_b(),
		engine.besavilla_470_b(),
		engine.besavilla_470_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_471_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_471_a(),        
		engine.besavilla_471_a(),
		engine.besavilla_471_a(),
		engine.besavilla_471_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_471_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_471_b(),        
		engine.besavilla_471_b(),
		engine.besavilla_471_b(),
		engine.besavilla_471_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_472_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_472_b(),        
		engine.besavilla_472_b(),
		engine.besavilla_472_b(),
		engine.besavilla_472_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_472_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_472_c(),        
		engine.besavilla_472_c(),
		engine.besavilla_472_c(),
		engine.besavilla_472_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_473_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_473_b(),        
		engine.besavilla_473_b(),
		engine.besavilla_473_b(),
		engine.besavilla_473_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_473_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_473_c(),        
		engine.besavilla_473_c(),
		engine.besavilla_473_c(),
		engine.besavilla_473_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_474_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_474_b(),        
		engine.besavilla_474_b(),
		engine.besavilla_474_b(),
		engine.besavilla_474_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_474_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_474_c(),        
		engine.besavilla_474_c(),
		engine.besavilla_474_c(),
		engine.besavilla_474_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_475():
	def __init__(self):
		instance_list = [
		engine.besavilla_475(),        
		engine.besavilla_475(),
		engine.besavilla_475(),
		engine.besavilla_475()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_476():
	def __init__(self):
		instance_list = [
		engine.besavilla_476(),        
		engine.besavilla_476(),
		engine.besavilla_476(),
		engine.besavilla_476()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_479():
	def __init__(self):
		instance_list = [
		engine.besavilla_479(),        
		engine.besavilla_479(),
		engine.besavilla_479(),
		engine.besavilla_479()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_480_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_480_a(),        
		engine.besavilla_480_a(),
		engine.besavilla_480_a(),
		engine.besavilla_480_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_480_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_480_b(),        
		engine.besavilla_480_b(),
		engine.besavilla_480_b(),
		engine.besavilla_480_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_481():
	def __init__(self):
		instance_list = [
		engine.besavilla_481(),        
		engine.besavilla_481(),
		engine.besavilla_481(),
		engine.besavilla_481()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_482():
	def __init__(self):
		instance_list = [
		engine.besavilla_482(),        
		engine.besavilla_482(),
		engine.besavilla_482(),
		engine.besavilla_482()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_483():
	def __init__(self):
		instance_list = [
		engine.besavilla_483(),        
		engine.besavilla_483(),
		engine.besavilla_483(),
		engine.besavilla_483()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_484():
	def __init__(self):
		instance_list = [
		engine.besavilla_484(),        
		engine.besavilla_484(),
		engine.besavilla_484(),
		engine.besavilla_484()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_485():
	def __init__(self):
		instance_list = [
		engine.besavilla_485(),        
		engine.besavilla_485(),
		engine.besavilla_485(),
		engine.besavilla_485()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_486():
	def __init__(self):
		instance_list = [
		engine.besavilla_486(),        
		engine.besavilla_486(),
		engine.besavilla_486(),
		engine.besavilla_486()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_487():
	def __init__(self):
		instance_list = [
		engine.besavilla_487(),        
		engine.besavilla_487(),
		engine.besavilla_487(),
		engine.besavilla_487()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_488():
	def __init__(self):
		instance_list = [
		engine.besavilla_488(),        
		engine.besavilla_488(),
		engine.besavilla_488(),
		engine.besavilla_488()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_489():
	def __init__(self):
		instance_list = [
		engine.besavilla_489(),        
		engine.besavilla_489(),
		engine.besavilla_489(),
		engine.besavilla_489()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_490():
	def __init__(self):
		instance_list = [
		engine.besavilla_490(),        
		engine.besavilla_490(),
		engine.besavilla_490(),
		engine.besavilla_490()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_491():
	def __init__(self):
		instance_list = [
		engine.besavilla_491(),        
		engine.besavilla_491(),
		engine.besavilla_491(),
		engine.besavilla_491()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_493():
	def __init__(self):
		instance_list = [
		engine.besavilla_493(),        
		engine.besavilla_493(),
		engine.besavilla_493(),
		engine.besavilla_493()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_494():
	def __init__(self):
		instance_list = [
		engine.besavilla_494(),        
		engine.besavilla_494(),
		engine.besavilla_494(),
		engine.besavilla_494()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_495():
	def __init__(self):
		instance_list = [
		engine.besavilla_495(),        
		engine.besavilla_495(),
		engine.besavilla_495(),
		engine.besavilla_495()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_496():
	def __init__(self):
		instance_list = [
		engine.besavilla_496(),        
		engine.besavilla_496(),
		engine.besavilla_496(),
		engine.besavilla_496()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_497():
	def __init__(self):
		instance_list = [
		engine.besavilla_497(),        
		engine.besavilla_497(),
		engine.besavilla_497(),
		engine.besavilla_497()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_498_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_498_a(),        
		engine.besavilla_498_a(),
		engine.besavilla_498_a(),
		engine.besavilla_498_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_498_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_498_b(),        
		engine.besavilla_498_b(),
		engine.besavilla_498_b(),
		engine.besavilla_498_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_499():
	def __init__(self):
		instance_list = [
		engine.besavilla_499(),        
		engine.besavilla_499(),
		engine.besavilla_499(),
		engine.besavilla_499()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_499_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_499_a(),        
		engine.besavilla_499_a(),
		engine.besavilla_499_a(),
		engine.besavilla_499_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_499_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_499_b(),        
		engine.besavilla_499_b(),
		engine.besavilla_499_b(),
		engine.besavilla_499_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_499_b_2():
	def __init__(self):
		instance_list = [
		engine.besavilla_499_b_2(),        
		engine.besavilla_499_b_2(),
		engine.besavilla_499_b_2(),
		engine.besavilla_499_b_2()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_500():
	def __init__(self):
		instance_list = [
		engine.besavilla_500(),        
		engine.besavilla_500(),
		engine.besavilla_500(),
		engine.besavilla_500()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_501():
	def __init__(self):
		instance_list = [
		engine.besavilla_501(),        
		engine.besavilla_501(),
		engine.besavilla_501(),
		engine.besavilla_501()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_502_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_502_b(),        
		engine.besavilla_502_b(),
		engine.besavilla_502_b(),
		engine.besavilla_502_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_502_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_502_c(),        
		engine.besavilla_502_c(),
		engine.besavilla_502_c(),
		engine.besavilla_502_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_503_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_503_a(),        
		engine.besavilla_503_a(),
		engine.besavilla_503_a(),
		engine.besavilla_503_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_503_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_503_b(),        
		engine.besavilla_503_b(),
		engine.besavilla_503_b(),
		engine.besavilla_503_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_503_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_503_c(),        
		engine.besavilla_503_c(),
		engine.besavilla_503_c(),
		engine.besavilla_503_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_504_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_504_a(),        
		engine.besavilla_504_a(),
		engine.besavilla_504_a(),
		engine.besavilla_504_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_504_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_504_b(),        
		engine.besavilla_504_b(),
		engine.besavilla_504_b(),
		engine.besavilla_504_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_504_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_504_c(),        
		engine.besavilla_504_c(),
		engine.besavilla_504_c(),
		engine.besavilla_504_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_505_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_505_a(),        
		engine.besavilla_505_a(),
		engine.besavilla_505_a(),
		engine.besavilla_505_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_505_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_505_b(),        
		engine.besavilla_505_b(),
		engine.besavilla_505_b(),
		engine.besavilla_505_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_506_a():
	def __init__(self):
		instance_list = [
		engine.besavilla_506_a(),        
		engine.besavilla_506_a(),
		engine.besavilla_506_a(),
		engine.besavilla_506_a()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_506_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_506_b(),        
		engine.besavilla_506_b(),
		engine.besavilla_506_b(),
		engine.besavilla_506_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_506_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_506_c(),        
		engine.besavilla_506_c(),
		engine.besavilla_506_c(),
		engine.besavilla_506_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_507():
	def __init__(self):
		instance_list = [
		engine.besavilla_507(),        
		engine.besavilla_507(),
		engine.besavilla_507(),
		engine.besavilla_507()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_508():
	def __init__(self):
		instance_list = [
		engine.besavilla_508(),        
		engine.besavilla_508(),
		engine.besavilla_508(),
		engine.besavilla_508()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_509():
	def __init__(self):
		instance_list = [
		engine.besavilla_509(),        
		engine.besavilla_509(),
		engine.besavilla_509(),
		engine.besavilla_509()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_510():
	def __init__(self):
		instance_list = [
		engine.besavilla_510(),        
		engine.besavilla_510(),
		engine.besavilla_510(),
		engine.besavilla_510()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_511_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_511_b(),        
		engine.besavilla_511_b(),
		engine.besavilla_511_b(),
		engine.besavilla_511_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_511_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_511_c(),        
		engine.besavilla_511_c(),
		engine.besavilla_511_c(),
		engine.besavilla_511_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_512_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_512_b(),        
		engine.besavilla_512_b(),
		engine.besavilla_512_b(),
		engine.besavilla_512_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_512_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_512_c(),        
		engine.besavilla_512_c(),
		engine.besavilla_512_c(),
		engine.besavilla_512_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_513_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_513_b(),        
		engine.besavilla_513_b(),
		engine.besavilla_513_b(),
		engine.besavilla_513_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_513_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_513_c(),        
		engine.besavilla_513_c(),
		engine.besavilla_513_c(),
		engine.besavilla_513_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_514_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_514_b(),        
		engine.besavilla_514_b(),
		engine.besavilla_514_b(),
		engine.besavilla_514_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_514_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_514_c(),        
		engine.besavilla_514_c(),
		engine.besavilla_514_c(),
		engine.besavilla_514_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_515_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_515_c(),        
		engine.besavilla_515_c(),
		engine.besavilla_515_c(),
		engine.besavilla_515_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_515_A_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_515_A_b(),        
		engine.besavilla_515_A_b(),
		engine.besavilla_515_A_b(),
		engine.besavilla_515_A_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_515_A_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_515_A_c(),        
		engine.besavilla_515_A_c(),
		engine.besavilla_515_A_c(),
		engine.besavilla_515_A_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_516_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_516_b(),        
		engine.besavilla_516_b(),
		engine.besavilla_516_b(),
		engine.besavilla_516_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_516_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_516_c(),        
		engine.besavilla_516_c(),
		engine.besavilla_516_c(),
		engine.besavilla_516_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_517_b():
	def __init__(self):
		instance_list = [
		engine.besavilla_517_b(),        
		engine.besavilla_517_b(),
		engine.besavilla_517_b(),
		engine.besavilla_517_b()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
class besavilla_517_c():
	def __init__(self):
		instance_list = [
		engine.besavilla_517_c(),        
		engine.besavilla_517_c(),
		engine.besavilla_517_c(),
		engine.besavilla_517_c()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer 