import random
from electronics import bipolar_junction_transistors as source

print('Generating...')
file_name = 'bipolar_junction_transistors'

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

question_list = [source.boylestad_4_1(),
source.boylestad_4_2(),
source.boylestad_4_3(),
source.boylestad_4_6(),
source.boylestad_4_8(),
source.boylestad_4_12(),
source.boylestad_4_14(),
source.boylestad_4_16(),
source.boylestad_4_17(),
source.boylestad_4_18(),
source.boylestad_4_19(),
# source.boylestad_4_20(), - to be troubleshooted
source.boylestad_4_27(),
source.boylestad_4_28(),
source.boylestad_4_29(),
source.boylestad_4_30(),
source.boylestad_4_31(),
source.boylestad_4_32(),
source.boylestad_4_35(),
source.boylestad_4_36()
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
