import random
from electronics import indiabix as source2
print('Generating...')
file_name = 'digital_electronics'

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
COMPUTATIONS = False

question_list = [
]

concept_list = [
source2.digital_electronics_digital_concepts_1(),
source2.digital_electronics_digital_concepts_2(),
source2.digital_electronics_digital_concepts_3(),
source2.digital_electronics_digital_concepts_4(),
source2.digital_electronics_digital_concepts_5(),
source2.digital_electronics_digital_concepts_6(),
source2.digital_electronics_digital_concepts_7(),
source2.digital_electronics_digital_concepts_8(),
source2.digital_electronics_digital_concepts_9(),
source2.digital_electronics_digital_concepts_10(),
source2.digital_electronics_digital_concepts_11(),
source2.digital_electronics_digital_concepts_12(),
source2.digital_electronics_digital_concepts_13(),
source2.digital_electronics_digital_concepts_14(),
source2.digital_electronics_digital_concepts_15(),
source2.digital_electronics_digital_concepts_16(),
source2.digital_electronics_digital_concepts_17(),
source2.digital_electronics_digital_concepts_18(),
source2.digital_electronics_digital_concepts_19(),
source2.digital_electronics_digital_concepts_20(),
source2.digital_electronics_digital_concepts_21(),
source2.digital_electronics_digital_concepts_22(),
source2.digital_electronics_digital_concepts_23(),
source2.digital_electronics_digital_concepts_24(),
source2.digital_electronics_digital_concepts_25(),
source2.digital_electronics_digital_concepts_26(),
source2.digital_electronics_digital_concepts_27(),
#source2.digital_electronics_digital_concepts_28(),
source2.digital_electronics_digital_concepts_29(),
source2.digital_electronics_digital_concepts_30(),
source2.digital_electronics_digital_concepts_31(),
source2.digital_electronics_digital_concepts_32(),
source2.digital_electronics_digital_concepts_33(),
source2.digital_electronics_digital_concepts_34(),
source2.digital_electronics_digital_concepts_35(),
source2.digital_electronics_digital_concepts_36(),
source2.digital_electronics_digital_concepts_37(),
source2.digital_electronics_digital_concepts_38(),
source2.digital_electronics_digital_concepts_39(),
source2.digital_electronics_digital_concepts_40(),
source2.digital_electronics_digital_concepts_41(),
source2.digital_electronics_digital_concepts_42(),
source2.digital_electronics_digital_concepts_43(),
source2.digital_electronics_digital_concepts_44(),
source2.digital_electronics_digital_concepts_45(),
source2.digital_electronics_digital_concepts_46(),
source2.digital_electronics_digital_concepts_47(),
source2.digital_electronics_digital_concepts_48(),
source2.digital_electronics_digital_concepts_49(),
source2.digital_electronics_digital_concepts_50(),
source2.digital_electronics_digital_concepts_51(),
source2.digital_electronics_digital_concepts_52(),
source2.digital_electronics_digital_concepts_53(),
source2.digital_electronics_digital_concepts_54(),
source2.digital_electronics_digital_concepts_true_1_2(),
source2.digital_electronics_digital_concepts_true_3_4(),
source2.digital_electronics_digital_concepts_true_5_6(),
source2.digital_electronics_digital_concepts_true_7_8(),
source2.digital_electronics_digital_concepts_true_9_10(),
source2.digital_electronics_digital_concepts_true_11_12(),
source2.digital_electronics_digital_concepts_true_13_14(),
source2.digital_electronics_digital_concepts_true_15_16(),
source2.digital_electronics_digital_concepts_true_17_18(),
source2.digital_electronics_digital_concepts_true_19_20(),
source2.digital_electronics_digital_concepts_true_21_22(),
source2.digital_electronics_digital_concepts_true_23_24(),
source2.digital_electronics_digital_concepts_true_25_26(),
source2.digital_electronics_digital_concepts_true_27_28(),
source2.digital_electronics_digital_concepts_true_29_30(),
source2.digital_electronics_digital_concepts_true_31_32(),
source2.digital_electronics_digital_concepts_true_33_34(),
source2.digital_electronics_digital_concepts_true_35_36(),
source2.digital_electronics_digital_concepts_true_37_38(),
source2.digital_electronics_digital_concepts_true_39_40(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_1(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_2(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_3(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_4(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_5(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_6(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_7(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_8(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_9(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_10(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_11(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_12(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_13(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_14(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_15(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_16(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_17(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_18(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_19(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_20(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_21(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_22(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_23(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_24(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_25(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_26(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_27(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_28(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_29(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_30(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_31(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_32(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_33(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_34(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_35(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_36(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_37(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_38(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_39(),
source2.digital_electronics_digital_concepts_fill_in_the_blanks_40()
]



if len(concept_list) == 0:
	CONCEPTS = False
else:
	CONCEPTS = True

if not TESTMODE:
	random.shuffle(question_list)
	random.shuffle(concept_list)

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

if CONCEPTS and COMPUTATIONS:
	for i in range (min(len(question_list), len(concept_list))):
		print('-----------------------------------------------------------------------')
		item = random.choice([question_list[i], concept_list[i]])
		print_tasks(item)
		write_to_file(item)
elif COMPUTATIONS and (not CONCEPTS):
	for i in range (len(question_list)):
		print('-----------------------------------------------------------------------')
		item = question_list[i]
		print_tasks(item)
		write_to_file(item)

elif CONCEPTS and (not COMPUTATIONS):
	for i in range (len(concept_list)):
		print('-----------------------------------------------------------------------')
		item = concept_list[i]
		print_tasks(item)
		write_to_file(item)	

print()
file.close()
print('Finished.')
