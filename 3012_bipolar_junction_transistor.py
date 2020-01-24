import random
from electronics import bipolar_junction_transistors as source
from electronics import gibilisco as source_2

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
source.boylestad_4_36(),
source_2.gibilisco_22_1(),
source_2.gibilisco_22_2(),
source_2.gibilisco_22_3(),
source_2.gibilisco_22_4(),
source_2.gibilisco_22_5(),
source_2.gibilisco_22_6(),
source_2.gibilisco_22_7(),
source_2.gibilisco_22_8(),
source_2.gibilisco_22_9(),
source_2.gibilisco_22_10(),
source_2.gibilisco_22_11(),
source_2.gibilisco_22_12(),
source_2.gibilisco_22_13(),
source_2.gibilisco_22_14(),
source_2.gibilisco_22_15(),
source_2.gibilisco_22_16(),
source_2.gibilisco_22_17(),
source_2.gibilisco_22_18(),
source_2.gibilisco_22_19(),
source_2.gibilisco_22_20()
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
