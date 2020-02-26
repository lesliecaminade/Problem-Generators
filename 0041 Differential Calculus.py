import random
from mathsub import differential_calculus_engine as source2
from mathsub import differential_calculus as source

print('Generating...')
file_name = 'differential calculus'

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
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source.first_derivative(),
source2.besavilla_1(),
source2.besavilla_2(),
source2.besavilla_3(),
source2.besavilla_4(),
source2.besavilla_5(),
source2.besavilla_6(),
source2.besavilla_7(),
source2.besavilla_8(),
source2.besavilla_9(),
source2.besavilla_10(),
source2.besavilla_37(),
source2.besavilla_38(),
source2.besavilla_39(),
source2.besavilla_40(),
source2.besavilla_41(),
source2.besavilla_42(),
source2.besavilla_43(),
source2.besavilla_44(),
source2.besavilla_45(),
source2.besavilla_46(),
source2.besavilla_47(),
source2.besavilla_48(),
source2.besavilla_49(),
source2.besavilla_50(),
source2.besavilla_51(),
source2.besavilla_52(),
source2.besavilla_53(),
source2.besavilla_54(),
source2.besavilla_55(),
source2.besavilla_56(),
source2.besavilla_57(),
source2.besavilla_58(),
source2.besavilla_59(),
source2.besavilla_60(),
source2.besavilla_61(),
source2.besavilla_62(),
source2.besavilla_63(),
source2.besavilla_64(),
source2.besavilla_65(),
source2.besavilla_66(),
source2.besavilla_67(),
source2.besavilla_68(),
source2.besavilla_69(),
source2.besavilla_70(),
source2.besavilla_71(),
source2.besavilla_72(),
source2.besavilla_73(),
source2.besavilla_74(),
source2.besavilla_75(),
source2.besavilla_76(),
source2.besavilla_77(),
source2.besavilla_78(),
source2.besavilla_79(),
source2.besavilla_80(),
source2.besavilla_81(),
source2.besavilla_82(),
source2.besavilla_83(),
source2.besavilla_84(),
source2.besavilla_85(),
source2.besavilla_86(),
source2.besavilla_87(),
source2.besavilla_88(),
source2.besavilla_89(),
source2.besavilla_90(),
source2.besavilla_91(),
source2.besavilla_92(),
source2.besavilla_93(),
source2.besavilla_94(),
source2.besavilla_95(),
source2.besavilla_96(),
source2.besavilla_97(),
source2.besavilla_98(),
source2.besavilla_99(),
source2.besavilla_100(),
source2.besavilla_101(),
source2.besavilla_102(),
source2.besavilla_103(),
source2.besavilla_104(),
source2.besavilla_105(),
source2.besavilla_106(),
source2.besavilla_107(),
source2.besavilla_108(),
source2.besavilla_109(),
source2.besavilla_110(),
source2.besavilla_111(),
source2.besavilla_112(),
source2.besavilla_113(),
source2.besavilla_114(),
source2.besavilla_115(),
source2.besavilla_116(),
source2.besavilla_117(),
source2.besavilla_118(),
source2.besavilla_119(),
source2.besavilla_120(),
source2.besavilla_121(),
source2.besavilla_122(),
source2.besavilla_123(),
source2.besavilla_124(),
source2.besavilla_125(),
]


concept_list = [
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
