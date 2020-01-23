import random
from electronics import diode as source

print('Generating...')
file_name = 'diode'

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

question_list = [source.floyd_2_1_a(),
source.floyd_2_1_b(),
source.floyd_2_2(),
source.floyd_2_3(),
source.floyd_2_4(),
source.floyd_2_5(),
source.floyd_2_6(),
source.floyd_2_7(),
source.floyd_2_8(),
source.floyd_2_9(),
source.floyd_2_10(),
source.floyd_2_11(),
source.floyd_2_12(),
source.floyd_2_13(),
source.floyd_3_5(),
source.floyd_3_6(),
source.floyd_3_7(),
source.floyd_3_8_a(),
source.boylestad_2_4(),
source.boylestad_2_6(),
source.boylestad_2_9(),
source.boylestad_2_10(),
source.boylestad_2_11(),
source.boylestad_2_12(),
source.boylestad_2_13(),
source.boylestad_2_14(),
source.boylestad_2_15(),
source.boylestad_2_16(),
source.boylestad_2_17()
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
