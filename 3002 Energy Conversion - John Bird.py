import random
from electronics import energy_conversion as source

print('Generating...')
file_name = 'energy_conversion'

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

question_list = [
source.johnbird_4_1(),
source.johnbird_4_2(),
source.johnbird_4_3(),
source.johnbird_4_4(),
source.johnbird_21_1(),
source.johnbird_21_2(),
source.johnbird_21_3(),
source.johnbird_21_4(),
source.johnbird_21_5(),
source.johnbird_21_6(),
source.johnbird_21_7(),
source.johnbird_21_8(),
source.johnbird_21_9(),
source.johnbird_21_10(),
source.johnbird_21_11(),
source.johnbird_21_12(),
source.johnbird_21_13(),
source.johnbird_22_1(),
source.johnbird_22_2(),
source.johnbird_22_3(),
source.johnbird_22_4(),
source.johnbird_22_5(),
source.johnbird_22_6(),
source.johnbird_22_7(),
source.johnbird_22_8(),
source.johnbird_22_9(),
source.johnbird_22_10(),
source.johnbird_22_11(),
source.johnbird_22_12(),
source.johnbird_22_13(),
source.johnbird_22_14(),
source.johnbird_22_15(),
source.johnbird_22_16(),
source.johnbird_22_17(),
source.johnbird_22_18(),
source.johnbird_22_19(),
source.johnbird_22_20(),
source.johnbird_22_21(),
source.johnbird_22_22(),
source.johnbird_22_23(),
source.johnbird_22_24(),
source.johnbird_22_25(),
source.johnbird_22_26(),
source.johnbird_22_27()
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

stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False