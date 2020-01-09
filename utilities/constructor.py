input_list = [
'hipolito_2_1',
'hipolito_2_2',
'hipolito_2_3',
'hipolito_2_4',
'hipolito_2_5',
'hipolito_2_6',
'hipolito_2_7',
'hipolito_2_8',
'hipolito_2_9',
'hipolito_2_10',
'hipolito_2_11',
'hipolito_2_12',
'hipolito_2_14',
'hipolito_2_15',
'hipolito_2_18',
'hipolito_2_19',
'hipolito_2_21',
'hipolito_2_22',
'hipolito_2_23',
'hipolito_3_1',
'hipolito_3_2',
'hipolito_3_3',
'hipolito_3_5'
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