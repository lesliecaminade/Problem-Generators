import random
from electronics import feedback as source
from electronics import floyd as source2

print('Generating...')
file_name = 'feedback'

import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
folderpath = os.path.dirname(os.path.realpath(__file__))

def write_to_file(some_object):   
	if FILEMODE: 
		file.write(some_object.question)
		file.write('\n')
		file.write(some_object.answer)
		file.write('\n\n')

def print_tasks(some_object):
	print(some_object.question)
	print()
	print(some_object.answer)
	print()
	print()

FILEMODE = True
TESTMODE = False
CONCEPTS = True

question_list = [source.floyd_16_1(),
source.floyd_16_2(),
source.floyd_16_2_b(),
# source.floyd_16_3(),
source.floyd_16_4(),
# source.floyd_16_6(),
source.no_reference_1(),
source.no_reference_2(),
source.no_reference_3(),
]

concept_list = [
source2.floyd_16_2(),
source2.floyd_16_3(),
source2.floyd_16_4(),
source2.floyd_16_5(),
source2.floyd_16_6(),
source2.floyd_16_7(),
source2.floyd_16_8(),
source2.floyd_16_9(),
source2.floyd_16_10(),
source2.floyd_16_11(),
source2.floyd_16_12(),
source2.floyd_16_13(),
source2.floyd_16_14()
]

if not TESTMODE:
	random.shuffle(question_list)
	random.shuffle(concept_list)

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

if CONCEPTS:
	for i in range (min(len(question_list), len(concept_list))):
		print('-----------------------------------------------------------------------')
		item = random.choice([question_list[i], concept_list[i]])
		print_tasks(item)
		write_to_file(item)
else:
	for i in range (len(question_list)):
		print('-----------------------------------------------------------------------')
		item = question_list[i]
		print_tasks(item)
		write_to_file(item)

print()
file.close()
print('Finished.')
