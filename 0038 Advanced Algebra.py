import random
from mathsub import algebra_2 as source

print('Generating...')
file_name = 'algebra'

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

question_list = [source.algebra_1(),
source.algebra_2(),
source.algebra_3(),
source.algebra_4(),
source.algebra_5(),
source.algebra_6(),
source.algebra_7(),
source.algebra_8(),
source.algebra_9(),
source.algebra_10(),
source.algebra_11(),
source.algebra_12(),
source.algebra_13(),
source.algebra_14(),
source.algebra_15(),
source.algebra_16(),
source.algebra_17(),
source.algebra_18(),
source.algebra_19(),
source.algebra_20(),
source.algebra_21(),
source.algebra_22(),
source.algebra_23(),
source.algebra_24(),
source.algebra_25(),
source.algebra_26(),
source.algebra_27(),
source.algebra_28(),
source.algebra_29(),
source.algebra_30(),
source.algebra_31(),
]

if TESTMODE:
	random.shuffle(question_list)


file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

for i in range (len(question_list)):
    print('-----------------------------------------------------------------------')
    item = question_list[i]
    print_tasks(item)
    write_to_file(item)

print()
file.close()
print('Finished.')
