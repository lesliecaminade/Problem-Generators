import random
from electronics import diode as source
from electronics import gibilisco as source_2

print('Generating...')
file_name = 'diode'

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

question_list = [source.floyd_2_1_a(),
source.floyd_2_1_b(),
source.floyd_2_2(),
source.floyd_2_3(),
source.floyd_2_4(),
source.floyd_2_5(),
source.floyd_2_6(),
source.floyd_2_7(),
source.floyd_2_8(),
source.floyd_2_9(),
source.floyd_2_10(),
source.floyd_2_11(),
source.floyd_2_12(),
source.floyd_2_13(),
source.floyd_3_5(),
source.floyd_3_6(),
source.floyd_3_7(),
source.floyd_3_8_a(),
source.boylestad_2_4(),
source.boylestad_2_6(),
source.boylestad_2_9(),
source.boylestad_2_10(),
source.boylestad_2_11(),
source.boylestad_2_12(),
source.boylestad_2_13(),
source.boylestad_2_14(),
source.boylestad_2_15(),
source.boylestad_2_16(),
source.boylestad_2_17()
]

concept_list = [
source_2.gibilisco_19_1(),
source_2.gibilisco_19_2(),
source_2.gibilisco_19_3(),
source_2.gibilisco_19_4(),
source_2.gibilisco_19_5(),
source_2.gibilisco_19_6(),
source_2.gibilisco_19_7(),
source_2.gibilisco_19_8(),
source_2.gibilisco_19_9(),
source_2.gibilisco_19_10(),
source_2.gibilisco_19_11(),
source_2.gibilisco_19_12(),
source_2.gibilisco_19_13(),
source_2.gibilisco_19_14(),
source_2.gibilisco_19_15(),
source_2.gibilisco_19_16(),
source_2.gibilisco_19_17(),
source_2.gibilisco_19_18(),
source_2.gibilisco_19_19(),
source_2.gibilisco_19_20(),
source_2.gibilisco_20_1(),
source_2.gibilisco_20_8(),
source_2.gibilisco_20_9(),
source_2.gibilisco_20_10(),
source_2.gibilisco_20_11(),
source_2.gibilisco_20_12(),
source_2.gibilisco_20_13(),
source_2.gibilisco_20_14(),
source_2.gibilisco_20_15(),
source_2.gibilisco_20_16(),
source_2.gibilisco_20_17(),
source_2.gibilisco_20_18(),
source_2.gibilisco_20_19(),
source_2.gibilisco_20_20(),
source_2.gibilisco_21_1(),
source_2.gibilisco_21_2(),
source_2.gibilisco_21_3(),
source_2.gibilisco_21_4(),
source_2.gibilisco_21_5(),
source_2.gibilisco_21_6(),
source_2.gibilisco_21_7(),
source_2.gibilisco_21_8(),
source_2.gibilisco_21_9(),
source_2.gibilisco_21_10(),
source_2.gibilisco_21_11(),
source_2.gibilisco_21_12(),
source_2.gibilisco_21_13(),
source_2.gibilisco_21_14(),
source_2.gibilisco_21_15(),
source_2.gibilisco_21_16(),
source_2.gibilisco_21_17(),
source_2.gibilisco_21_18(),
source_2.gibilisco_21_19(),
source_2.gibilisco_21_20()
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
