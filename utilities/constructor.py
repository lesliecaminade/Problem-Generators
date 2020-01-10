input_list = [
'johnbird_4_1',
'johnbird_4_2',
'johnbird_4_3',
'johnbird_4_4',
'johnbird_21_1',
'johnbird_21_2',
'johnbird_21_3',
'johnbird_21_4',
'johnbird_21_5',
'johnbird_21_6',
'johnbird_21_7',
'johnbird_21_8',
'johnbird_21_9',
'johnbird_21_10',
'johnbird_21_11',
'johnbird_21_12',
'johnbird_21_13',
'johnbird_22_1',
'johnbird_22_2',
'johnbird_22_3',
'johnbird_22_4',
'johnbird_22_5',
'johnbird_22_6',
'johnbird_22_7',
'johnbird_22_8',
'johnbird_22_9',
'johnbird_22_10',
'johnbird_22_11',
'johnbird_22_12',
'johnbird_22_13',
'johnbird_22_14',
'johnbird_22_15',
'johnbird_22_16',
'johnbird_22_17',
'johnbird_22_18',
'johnbird_22_19',
'johnbird_22_20',
'johnbird_22_21',
'johnbird_22_22',
'johnbird_22_23',
'johnbird_22_24',
'johnbird_22_25',
'johnbird_22_26',
'johnbird_22_27'
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