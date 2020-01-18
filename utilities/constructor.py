input_list = [
'rgs_1',
'rgs_2',
'rgs_3',
'rgs_4',
'rgs_5',
'rgs_6',
'rgs_7',
'rgs_8',
'rgs_9',
'rgs_10',
'rgs_11',
'rgs_12',
'rgs_13',
'rgs_14',
'rgs_15',
'rgs_16',
'rgs_17',
'rgs_18',
'rgs_19',
'rgs_20',
'rgs_21',
'rgs_22',
'rgs_23',
'rgs_24',
'rgs_25',
'rgs_26',
'rgs_27',
'rgs_28',
'rgs_29',
'rgs_30',
'rgs_31',
'rgs_32',
'rgs_33',
'rgs_34',
'rgs_35',
'rgs_36',
'rgs_37',
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