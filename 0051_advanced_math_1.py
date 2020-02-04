import random
from mathsub import complex_numbers as source
from mathsub import matrices as source2
print('Generating...')
file_name = 'advanced math 1'

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
source.Complex_number_raised_to_positive_integer(),
source.Complex_number_root_to_positive_integer(),
source.Complex_number_raised_to_complex_number(),
source.Natural_logarithm_of_complex(),
source.Logarithm_to_the_positive_integer_base_of_complex(),
source.Logarithm_to_the_base_of_complex_number_complex(),
source.Sine_of_a_complex_number(),
source.Cosine_of_a_complex_number(),
source.Trigonometric_value_of_a_complex_number(),

source2.Multiplication(),
source2.Transpose(),
source2.Submatrix(),
source2.Minor(),
source2.Cofactor(),
source2.Cofactor_Matrix(),
source2.Adjugate(),
source2.Determinant(),
source2.Inverse(),
source2.Row_Echelon_Form(),
]

concept_list = [

]

if len(concept_list) == 0:
	CONCEPTS = False

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
