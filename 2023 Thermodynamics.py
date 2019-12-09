import random
from geas import physics as source

print('Generating...')
file_name = 'thermodynamics'

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
source.Schaums_15_1(),
source.Schaums_15_2(),
source.Schaums_15_3(),
source.Schaums_15_4(),
source.Schaums_15_5(),
source.Schaums_15_6(),
source.Schaums_15_7(),
source.Schaums_15_8(),
source.Schaums_15_9(),
source.Schaums_15_10(),
source.Schaums_16_1(),
source.Schaums_16_2(),
source.Schaums_16_3(),
source.Schaums_16_4(),
source.Schaums_16_5(),
source.Schaums_16_6(),
source.Schaums_16_7(),
source.Schaums_16_8(),
source.Schaums_16_9(),
source.Schaums_16_10(),
source.Schaums_16_11(),
source.Schaums_16_12(),
source.Schaums_16_13(),
source.Schaums_16_14(),
source.Schaums_16_15(),
source.Schaums_16_16(),
source.Schaums_16_17(),
source.Schaums_16_18(),
source.Schaums_17_1(),
source.Schaums_17_2(),
source.Schaums_17_3(),
source.Schaums_17_4(),
source.Schaums_17_5(),
source.Schaums_17_6(),
source.Schaums_17_7(),
source.Schaums_17_8(),
source.Schaums_17_9(),
source.Schaums_17_10(),
source.Schaums_17_11(),
source.Schaums_17_12(),
source.Schaums_18_1(),
source.Schaums_18_2(),
source.Schaums_18_3(),
source.Schaums_18_4(),
source.Schaums_18_5(),
source.Schaums_18_6(),
source.Schaums_18_7(),
source.Schaums_18_8(),
source.Schaums_18_9(),
source.Schaums_18_10(),
source.Schaums_18_11(),
source.Schaums_18_12(),
source.Schaums_18_13(),
source.Schaums_18_14(),
source.Schaums_18_15(),
source.Schaums_18_16(),
source.Schaums_18_17(),
source.Schaums_18_18(),
source.Schaums_19_1(),
source.Schaums_19_2(),
source.Schaums_19_3(),
source.Schaums_19_4(),
source.Schaums_19_5(),
source.Schaums_19_6(),
source.Schaums_19_7(),
source.Schaums_19_8(),
source.Schaums_20_1(),
source.Schaums_20_1(),
source.Schaums_20_2(),
source.Schaums_20_3(),
source.Schaums_20_4(),
source.Schaums_20_5(),
source.Schaums_20_6(),
source.Schaums_20_7(),
source.Schaums_20_8(),
source.Schaums_20_9(),
source.Schaums_20_10(),
source.Schaums_20_11(),
source.Schaums_20_12(),
source.Schaums_20_13(),
source.Schaums_20_14(),
source.Schaums_20_15(),
source.Schaums_20_16()
]


total_items_list = question_list
    
if not TESTMODE:
    items_list = random.sample(total_items_list, round(1 * len(question_list)))
else:
    items_list = total_items_list

print(items_list)
file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

for i in range (len(items_list)):

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
