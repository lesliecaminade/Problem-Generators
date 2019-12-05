import random
from mathsub import transforms_engine as engine
from num2words import num2words

def ask():
	ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
	return random.choice(ask_words)

def parse(string_input):
	string_input = str(string_input)
	return string_input.replace('**', '^').replace('*', ' ')

class Taylor_series():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Taylor_series()
			#data = battery.Some_attribute_from_battery			
			data =  parse(battery.taylor.print(terms = 5))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the Taylor series expasion of the function f(x) = {parse(main.function)} about x = {main.center}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Laplace_transform():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_enginee:
			battery = engine.Laplace_transform(solve = True)
			#data = battery.Some_attribute_from_battery			
			data =  parse(battery.laplace)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the Laplace transform of the function f(t) = {parse(str(main.function))}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Inverse_laplace_transform():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			if i == 0:
				battery = engine.Laplace_transform(solve = True)
			else:
				battery = engine.Laplace_transform()
			#data = battery.Some_attribute_from_battery			
			data =  parse(battery.function)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the inverse Laplace transform of the function F(s) = {parse(str(main.laplace))}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	

class Fourier_series():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Fourier_series(solve = True)
			#data = battery.Some_attribute_from_battery			
			data =  parse(battery.fourier)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ' #'
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the Fourier series of the function f(t) = {main.function.replace('FourierSeries', '')}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""	