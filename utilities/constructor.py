input_list = [
'jma_14_1',
'jma_14_2',
'jma_14_3',
'jma_14_4',
'jma_14_5',
'jma_14_6',
'jma_14_7',
'jma_14_8',
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