input_list = [
'boylestad_10_1',
'boylestad_10_2',
'boylestad_10_3',
'boylestad_10_4',
'boylestad_10_5',
'boylestad_10_6',
'boylestad_10_7',
'boylestad_10_8',
'boylestad_10_9',
'boylestad_10_10',
'boylestad_10_11',
'boylestad_10_12',
'boylestad_10_13',
'boylestad_10_14',
'boylestad_10_15',
'boylestad_10_16',
'boylestad_10_17',
'boylestad_10_18',
'boylestad_10_19',
'boylestad_10_20',
'boylestad_10_21',
'boylestad_10_22',
'boylestad_11_1',
'boylestad_11_2',
'boylestad_11_3',
'boylestad_11_4',
'boylestad_11_5',
'boylestad_11_6',
'boylestad_11_7',
'boylestad_11_8',
'boylestad_11_9',
'boylestad_11_10',
'boylestad_11_11',
'boylestad_11_12',
'boylestad_11_13',
'boylestad_11_14'
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