import random
from mathsub import transforms as source

print('Generating...')
file_name = 'transforms'

def write_to_file(some_object):   
	if FILEMODE: 
		file.write(some_object.question)
		file.write('\n')
		file.write(some_object.answer)
		file.write('\n\n')

def print_taks(some_object):
	print(some_object.question)
	print()
	print(some_object.answer)
	print()
	print()

FILEMODE = True
TESTMODE = True

questionList = [
source.Taylor_series(),
source.Laplace_transform(),
source.Inverse_laplace_transform(),
source.Fourier_series()
]

tryagain = True
while tryagain:
	try:
		additional_questionlist = [
		#insert hard to generate questions here
		]
		tryagain = False
	except:
		pass



questionList = questionList + additional_questionlist



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
	total_items_list.append(i)
	
	
#choose a smaller subset from these questions
if not TESTMODE:
	items_list = random.sample(total_items_list, round(1 * len(questionList)))
else:
	items_list = total_items_list

print(items_list)
file = open(f"{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

for i in range (len(items_list)):
	print('-----------------------------------------------------------------------')
	item = questionList[items_list[i]]
	print_taks(item)
	write_to_file(item)


print()
file.close()
print('Finished.')

stay = True
while stay:
	command = input()
	if command == 'exit':
		stay = False
