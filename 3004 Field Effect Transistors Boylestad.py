import random
from electronics import field_effect_transistors as source

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
TESTMODE = False

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
source.boylestad_8_12(),
]

if not TESTMODE:
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
