input_list = [
'sadiku_1_1',
'sadiku_1_2',
'sadiku_1_3',
'sadiku_1_4',
'sadiku_1_5',
'sadiku_1_5',
'sadiku_1_6',
'sadiku_1_7',
'sadiku_1_8',
'sadiku_1_9',
'sadiku_2_1',
'sadiku_2_2',
'sadiku_2_3',
'sadiku_2_5',
'sadiku_2_6',
'sadiku_2_7',
'sadiku_2_8',
'johnbird_2_1',
'johnbird_2_2',
'johnbird_2_3',
'johnbird_2_4',
'johnbird_2_5',
'johnbird_2_6',
'johnbird_2_7',
'johnbird_2_9',
'johnbird_2_10',
'johnbird_2_11',
'johnbird_2_12',
'johnbird_2_13',
'johnbird_2_14',
'johnbird_2_15',
'johnbird_2_16',
'johnbird_2_17',
'johnbird_2_18',
'johnbird_2_19',
'johnbird_3_1',
'johnbird_3_2',
'johnbird_3_3',
'johnbird_3_4',
'johnbird_3_5',
'johnbird_3_6',
'johnbird_3_7',
'johnbird_3_8',
'johnbird_3_9',
'johnbird_3_10',
'johnbird_3_11',
'johnbird_3_12',
'johnbird_3_13',
'johnbird_3_14',
'johnbird_3_16',
'johnbird_3_17',
'johnbird_3_18',
'johnbird_3_19',
'johnbird_5_1',
'johnbird_5_2',
'johnbird_5_3',
'johnbird_5_5',
'johnbird_5_7',
'johnbird_5_13',
'johnbird_5_16',
'johnbird_5_17',
'johnbird_6_1_a',
'johnbird_6_1_b',
'johnbird_6_2',
'johnbird_6_3',
'johnbird_6_4',
'johnbird_6_5',
'johnbird_6_6',
'johnbird_6_8',
'johnbird_6_9',
'johnbird_6_10',
'johnbird_6_11',
'johnbird_6_12',
'johnbird_6_13',
'johnbird_6_15',
'johnbird_6_16',
'johnbird_6_17',
'johnbird_6_18',
'johnbird_7_1',
'johnbird_7_2',
'johnbird_7_3',
'johnbird_7_4',
'johnbird_7_5',
'johnbird_7_6',
'johnbird_7_7',
'johnbird_7_8',
'johnbird_7_9',
'johnbird_7_10',
'johnbird_7_11',
'johnbird_7_12',
'johnbird_8_2',
'johnbird_8_3',
'johnbird_8_4',
'johnbird_8_6',
'johnbird_8_7',
'johnbird_9_1',
'johnbird_9_2',
'johnbird_9_3',
'johnbird_9_4',
'johnbird_9_6',
'johnbird_9_7',
'johnbird_9_8',
'johnbird_9_9',
'johnbird_9_10',
'johnbird_9_11',
'johnbird_9_12',
'johnbird_9_13',
'johnbird_9_14',
'johnbird_9_15',
'johnbird_9_16',
'johnbird_9_17',
'johnbird_9_18',
'johnbird_9_19',
'johnbird_9_20',
'johnbird_10_1',
'johnbird_10_2',
'johnbird_10_4',
'johnbird_10_18',
'johnbird_10_19',
'johnbird_10_20',
'johnbird_10_21',
'johnbird_10_22',
'johnbird_10_23',
'johnbird_10_24'
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