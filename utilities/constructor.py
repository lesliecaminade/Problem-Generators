input_list = [
'jma_1_95',
'jma_1_98',
'jma_1_99_a',
'jma_1_99_b',
'jma_1_100',
'jma_1_102_a',
'jma_1_102_b',
'jma_1_104',
'jma_1_105',
'jma_1_108',
'jma_1_109_a',
'jma_1_109_b',
'jma_1_110',
'jma_1_112',
'jma_1_113'
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