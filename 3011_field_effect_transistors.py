import random
from electronics import field_effect_transistors as source
from electronics import gibilisco as source_2

print('Generating...')
file_name = 'field_effect_transistors'

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
TESTMODE = True

question_list = [source.boylestad_7_1(),
source.boylestad_7_2(),
source.boylestad_7_4(),
source.boylestad_7_5(),
source.boylestad_7_6(),
source.boylestad_7_8(),
source.boylestad_7_10(),
source.boylestad_7_11(),
source.boylestad_8_7(),
source.boylestad_8_8(),
source.boylestad_8_9(),
source.boylestad_8_10(),
source.boylestad_8_11(),
source.boylestad_8_12()
]

concept_list = [
source_2.gibilisco_23_1(),
source_2.gibilisco_23_2(),
source_2.gibilisco_23_3(),
source_2.gibilisco_23_4(),
source_2.gibilisco_23_5(),
source_2.gibilisco_23_6(),
source_2.gibilisco_23_7(),
source_2.gibilisco_23_8(),
source_2.gibilisco_23_9(),
source_2.gibilisco_23_10(),
source_2.gibilisco_23_11(),
source_2.gibilisco_23_12(),
source_2.gibilisco_23_13(),
source_2.gibilisco_23_14(),
source_2.gibilisco_23_15(),
source_2.gibilisco_23_16(),
source_2.gibilisco_23_17(),
source_2.gibilisco_23_18(),
source_2.gibilisco_23_19(),
source_2.gibilisco_23_20()
]

if not TESTMODE:
	random.shuffle(question_list)
	random.shuffle(concept_list)

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

for i in range (min(len(question_list), len(concept_list))):
	print('-----------------------------------------------------------------------')
	item = random.choice([question_list[i], concept_list[i]])
	print_tasks(item)
	write_to_file(item)

print()
file.close()
print('Finished.')
