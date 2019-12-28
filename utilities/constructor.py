input_list = [
'singer_107', 'singer_108', 'singer_109', 'singer_110', 'singer_115', 'singer_116', 'singer_117', 'singer_125', 'singer_126', 'singer_127', 'singer_133', 'singer_134', 'singer_135', 'singer_136', 'singer_138', 'singer_141', 'singer_142', 'singer_206', 'singer_207', 'singer_208', 'singer_209', 'singer_211', 'singer_223', 'singer_225', 'singer_226', 'singer_227', 'singer_228','singer_233', 'singer_234', 'singer_235', 'singer_236', 'singer_238', 'singer_239', 'singer_240', 'singer_241', 'singer_244', 'singer_245', 'singer_247', 'singer_261', 'singer_262', 'singer_263', 'singer_264', 'singer_265', 'singer_266', 'singer_267', 'singer_304', 'singer_305', 'singer_306', 'singer_307', 'singer_308', 'singer_309', 'singer_311', 'singer_312', 'singer_313'
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