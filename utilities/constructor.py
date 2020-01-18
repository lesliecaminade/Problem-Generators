input_list = [
'boylestad_7_1',
'boylestad_7_2',
'boylestad_7_4',
'boylestad_7_5',
'boylestad_7_6',
'boylestad_7_8',
'boylestad_7_10',
'boylestad_7_11',
'boylestad_8_7',
'boylestad_8_8',
'boylestad_8_9',
'boylestad_8_10',
'boylestad_8_11',
'boylestad_8_12'
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