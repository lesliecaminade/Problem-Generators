input_list = [
'example_2_1',
'example_2_2',
'example_2_3',
'example_2_4',
'example_2_8',
'example_2_9',
'example_2_10',
'example_2_11',
'example_2_12',
'example_2_13',
'example_2_14',
'example_2_15',
'example_2_16',
'example_2_17',
'example_2_18',
'example_2_19',
'example_2_20',
'example_2_21',
]

def construct(battery_string):

	code = f"""class {battery_string}():
	def __init__(self):
		instance_list = [
		engine.{battery_string}(),        
		engine.{battery_string}(),
		engine.{battery_string}(),
		engine.{battery_string}()        
		]
		constructed = Constructor(instance_list)
		self.question = constructed.question
		self.answer = constructed.answer    
		
"""

	return code

def distribute(batteries_list):
	code = ''
	for battery in batteries_list:
		code = code + 'source.' + battery + '(),\n'

	code = 'question_list = [' + code + ']'
	return code

def construct_2(batteries_list):
	code= ''
	for battery in batteries_list:
		code = code + construct(battery)

	return code




print(construct_2(input_list))
print(distribute(input_list))