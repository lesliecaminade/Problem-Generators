import random
from electronics import power_electronics as source
from electronics import indiabix as source2
print('Generating...')
file_name = 'power_electronics'

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

question_list = [source.fewson_2_1(),
source.fewson_2_2(),
source.fewson_2_3(),
source.fewson_2_4(),
source.fewson_2_5(),
source.fewson_3_1(),
source.fewson_3_3(),
source.fewson_3_4(),
source.fewson_3_5(),
source.fewson_3_6(),
source.fewson_3_7(),
source.fewson_3_8(),
source.fewson_3_9(),
source.fewson_3_10()
]

concept_list = [
source2.engineering_electronics_thyristors_1(),
source2.engineering_electronics_thyristors_2(),
# source2.engineering_electronics_thyristors_3(),
# source2.engineering_electronics_thyristors_4(),
source2.engineering_electronics_thyristors_5(),
source2.engineering_electronics_thyristors_6(),
source2.engineering_electronics_thyristors_7(),
source2.engineering_electronics_thyristors_8(),
# source2.engineering_electronics_thyristors_9(),
# source2.engineering_electronics_thyristors_10(),
source2.engineering_electronics_thyristors_11(),
source2.engineering_electronics_thyristors_12(),
source2.engineering_electronics_thyristors_13(),
source2.engineering_electronics_thyristors_14(),
source2.engineering_electronics_thyristors_16(),
source2.engineering_electronics_thyristors_fill_in_the_blanks_1(),
source2.engineering_electronics_thyristors_true_or_false_3_5(),
source2.engineering_electronics_thyristors_true_or_false_6_7(),
source2.engineering_electronics_thyristors_true_or_false_10_11(),
source2.engineering_electronics_thyristors_true_or_false_12_13(),

source2.engineering_electronic_devices_thyristors_1(),
source2.engineering_electronic_devices_thyristors_2(),
source2.engineering_electronic_devices_thyristors_3(),
source2.engineering_electronic_devices_thyristors_4(),
source2.engineering_electronic_devices_thyristors_5(),
source2.engineering_electronic_devices_thyristors_6(),
source2.engineering_electronic_devices_thyristors_7(),
source2.engineering_electronic_devices_thyristors_8(),
source2.engineering_electronic_devices_thyristors_9(),
source2.engineering_electronic_devices_thyristors_10(),
source2.engineering_electronic_devices_thyristors_11(),
source2.engineering_electronic_devices_thyristors_12(),
source2.engineering_electronic_devices_thyristors_13(),
source2.engineering_electronic_devices_thyristors_14(),
source2.engineering_electronic_devices_thyristors_15(),
source2.engineering_electronic_devices_thyristors_16(),
source2.engineering_electronic_devices_thyristors_17(),
source2.engineering_electronic_devices_thyristors_18(),
source2.engineering_electronic_devices_thyristors_19(),
source2.engineering_electronic_devices_thyristors_20(),
source2.engineering_electronic_devices_thyristors_21(),
source2.engineering_electronic_devices_thyristors_22(),
source2.engineering_electronic_devices_thyristors_true_or_false_1_2(),
source2.engineering_electronic_devices_thyristors_true_or_false_3_4(),
source2.engineering_electronic_devices_thyristors_true_or_false_5_6(),
source2.engineering_electronic_devices_thyristors_true_or_false_7_8(),
source2.engineering_electronic_devices_thyristors_true_or_false_9_10()
]

if len(concept_list) == 0:
	CONCEPTS = False
else:
	CONCEPTS = True

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
