input_list = [
'boylestad_2_4',
'boylestad_2_6',
'boylestad_2_9',
'boylestad_2_10',
'boylestad_2_11',
'boylestad_2_12',
'boylestad_2_13',
'boylestad_2_14',
'boylestad_2_15',
'boylestad_2_16',
'boylestad_2_17'
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