input_list = [
'boylestad_4_1',
'boylestad_4_2',
'boylestad_4_3',
'boylestad_4_6',
'boylestad_4_8',
'boylestad_4_12',
'boylestad_4_14',
'boylestad_4_15',
'boylestad_4_16',
'boylestad_4_17',
'boylestad_4_18',
'boylestad_4_19',
'boylestad_4_20',
'boylestad_4_27',
'boylestad_4_28',
'boylestad_4_29',
'boylestad_4_30',
'boylestad_4_31',
'boylestad_4_32',
'boylestad_4_35',
'boylestad_4_36'
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