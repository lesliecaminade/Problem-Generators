import random
from est import digital_communications as source
from est import fcarc as source2
from est import blake_mcq_1 as source3

print('Generating...')
file_name = 'digital_communications'

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


question_list = [
source.jma_14_1(),
source.jma_14_2(),
source.jma_14_3(),
source.jma_14_4(),
source.jma_14_5(),
source.jma_14_6(),
source.jma_14_7(),
source.jma_14_8(),
source.jma_15_1(),
source.jma_15_2(),
source.jma_15_3(),
source.jma_15_4(),
source.jma_15_5(),
source.jma_15_6(),
source.jma_15_7(),
source.jma_15_8(),
source.jma_15_9(),
]

concept_list = [
source2.f_1_366(),
source2.f_1_367(),
source2.f_1_368(),
source2.f_1_369(),
source2.f_1_370(),
source2.f_1_375(),
source3.chapter_7_1(),
source3.chapter_7_2(),
source3.chapter_7_3(),
source3.chapter_7_4(),
source3.chapter_7_5(),
source3.chapter_7_6(),
source3.chapter_7_7(),
source3.chapter_7_8(),
source3.chapter_7_9(),
source3.chapter_7_10(),
source3.chapter_7_11(),
source3.chapter_7_12(),
source3.chapter_7_13(),
source3.chapter_7_14(),
source3.chapter_7_15(),
source3.chapter_7_16(),
source3.chapter_7_17(),
source3.chapter_7_20(),
source3.chapter_7_21(),
source3.chapter_7_22()
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
