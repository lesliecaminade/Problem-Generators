import random
from mathsub import integral_calculus_engine as source

print('Generating...')
file_name = 'integral calculus 2'

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


question_list = [source.besavilla_470_a(),
source.besavilla_470_b(),
source.besavilla_471_a(),
source.besavilla_471_b(),
source.besavilla_472_b(),
source.besavilla_472_c(),
source.besavilla_473_b(),
source.besavilla_473_c(),
source.besavilla_474_b(),
source.besavilla_474_c(),
source.besavilla_475(),
source.besavilla_476(),
source.besavilla_479(),
source.besavilla_480_a(),
source.besavilla_480_b(),
source.besavilla_481(),
source.besavilla_482(),
source.besavilla_483(),
source.besavilla_484(),
source.besavilla_485(),
source.besavilla_486(),
source.besavilla_487(),
source.besavilla_488(),
source.besavilla_489(),
source.besavilla_490(),
source.besavilla_491(),
source.besavilla_493(),
source.besavilla_494(),
source.besavilla_495(),
source.besavilla_496(),
source.besavilla_497(),
source.besavilla_498_a(),
source.besavilla_498_b(),
source.besavilla_499(),
source.besavilla_499_a(),
source.besavilla_499_b(),
source.besavilla_499_b_2(),
source.besavilla_500(),
source.besavilla_501(),
source.besavilla_502_b(),
source.besavilla_502_c(),
source.besavilla_503_a(),
source.besavilla_503_b(),
source.besavilla_503_c(),
source.besavilla_504_a(),
source.besavilla_504_b(),
source.besavilla_504_c(),
source.besavilla_505_a(),
source.besavilla_505_b(),
source.besavilla_506_a(),
source.besavilla_506_b(),
source.besavilla_506_c(),
source.besavilla_507(),
source.besavilla_508(),
source.besavilla_509(),
source.besavilla_510(),
source.besavilla_511_b(),
source.besavilla_511_c(),
source.besavilla_512_b(),
source.besavilla_512_c(),
source.besavilla_513_b(),
source.besavilla_513_c(),
source.besavilla_514_b(),
source.besavilla_514_c(),
source.besavilla_515_c(),
source.besavilla_515_A_b(),
source.besavilla_515_A_c(),
source.besavilla_516_b(),
source.besavilla_516_c(),
source.besavilla_517_b(),
source.besavilla_517_c()
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
