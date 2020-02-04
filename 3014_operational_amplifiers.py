import random
from electronics import operational_amplifiers as source
from electronics import gibilisco as source_2
from electronics import floyd as source_3

print('Generating...')
file_name = 'opamp'

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

question_list = [source.boylestad_10_1(),
source.boylestad_10_2(),
source.boylestad_10_3(),
source.boylestad_10_4(),
source.boylestad_10_5(),
source.boylestad_10_6(),
source.boylestad_10_7(),
source.boylestad_10_8(),
source.boylestad_10_9(),
source.boylestad_10_10(),
source.boylestad_10_11(),
source.boylestad_10_12(),
source.boylestad_10_13(),
source.boylestad_10_14(),
source.boylestad_10_15(),
source.boylestad_10_17(),
source.boylestad_10_22(),
source.boylestad_11_1(),
source.boylestad_11_2(),
source.boylestad_11_3(),
source.boylestad_11_6(),
source.boylestad_11_7(),
source.boylestad_11_8(),
source.boylestad_11_10(),
source.boylestad_11_11(),
source.boylestad_11_12(),
source.boylestad_11_13(),
source.boylestad_11_14()
]

concept_list = [
source_3.floyd_12_1(),
source_3.floyd_12_2(),
source_3.floyd_12_3(),
source_3.floyd_12_4(),
source_3.floyd_12_5(),
source_3.floyd_12_6(),
source_3.floyd_12_7(),
source_3.floyd_12_8(),
source_3.floyd_12_9(),
source_3.floyd_12_10(),
source_3.floyd_12_11(),
source_3.floyd_12_12(),
source_3.floyd_12_13(),
source_3.floyd_12_14(),
source_3.floyd_12_15(),
source_3.floyd_12_16(),
source_3.floyd_12_18(),
source_3.floyd_12_19(),
source_3.floyd_12_21(),
source_3.floyd_12_22(),
source_3.floyd_12_23(),
source_3.floyd_12_24(),
source_3.floyd_12_25(),
source_3.floyd_12_26(),
source_3.floyd_12_28(),
source_3.floyd_12_29(),
source_3.floyd_12_30()
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
