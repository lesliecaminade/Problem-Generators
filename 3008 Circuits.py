import random
from electronics import circuits as source

print('Generating...')
file_name = 'circuits'

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

question_list = [source.sadiku_1_1(),
source.sadiku_1_2(),
source.sadiku_1_3(),
source.sadiku_1_4(),
source.sadiku_1_5(),
source.sadiku_1_5(),
source.sadiku_1_6(),
source.sadiku_1_7(),
source.sadiku_1_8(),
source.sadiku_1_9(),
source.sadiku_2_1(),
source.sadiku_2_2(),
source.sadiku_2_3(),
source.sadiku_2_5(),
source.sadiku_2_6(),
source.sadiku_2_7(),
source.sadiku_2_8(),
source.johnbird_2_1(),
source.johnbird_2_2(),
source.johnbird_2_3(),
source.johnbird_2_4(),
source.johnbird_2_5(),
source.johnbird_2_6(),
source.johnbird_2_7(),
source.johnbird_2_9(),
source.johnbird_2_10(),
source.johnbird_2_11(),
source.johnbird_2_12(),
source.johnbird_2_13(),
source.johnbird_2_14(),
source.johnbird_2_15(),
source.johnbird_2_16(),
source.johnbird_2_17(),
source.johnbird_2_18(),
source.johnbird_2_19(),
source.johnbird_3_1(),
source.johnbird_3_2(),
source.johnbird_3_3(),
source.johnbird_3_4(),
source.johnbird_3_5(),
source.johnbird_3_6(),
source.johnbird_3_7(),
source.johnbird_3_8(),
source.johnbird_3_9(),
source.johnbird_3_10(),
source.johnbird_3_11(),
source.johnbird_3_12(),
source.johnbird_3_13(),
source.johnbird_3_14(),
source.johnbird_3_16(),
source.johnbird_3_17(),
source.johnbird_3_18(),
source.johnbird_3_19(),
source.johnbird_5_1(),
source.johnbird_5_2(),
source.johnbird_5_3(),
source.johnbird_5_5(),
source.johnbird_5_7(),
source.johnbird_5_13(),
source.johnbird_5_16(),
source.johnbird_5_17(),
source.johnbird_6_1_a(),
source.johnbird_6_1_b(),
source.johnbird_6_2(),
source.johnbird_6_3(),
source.johnbird_6_4(),
source.johnbird_6_5(),
source.johnbird_6_6(),
source.johnbird_6_8(),
source.johnbird_6_9(),
source.johnbird_6_10(),
source.johnbird_6_11(),
source.johnbird_6_12(),
source.johnbird_6_13(),
source.johnbird_6_15(),
source.johnbird_6_16(),
source.johnbird_6_17(),
source.johnbird_6_18(),
source.johnbird_7_1(),
source.johnbird_7_2(),
source.johnbird_7_3(),
source.johnbird_7_4(),
source.johnbird_7_5(),
source.johnbird_7_6(),
source.johnbird_7_7(),
source.johnbird_7_8(),
source.johnbird_7_9(),
source.johnbird_7_10(),
source.johnbird_7_11(),
source.johnbird_7_12(),
source.johnbird_8_2(),
source.johnbird_8_3(),
source.johnbird_8_4(),
source.johnbird_8_6(),
source.johnbird_8_7(),
source.johnbird_9_1(),
source.johnbird_9_2(),
source.johnbird_9_3(),
source.johnbird_9_4(),
source.johnbird_9_6(),
source.johnbird_9_7(),
source.johnbird_9_8(),
source.johnbird_9_9(),
source.johnbird_9_10(),
source.johnbird_9_11(),
source.johnbird_9_12(),
source.johnbird_9_13(),
source.johnbird_9_14(),
source.johnbird_9_15(),
source.johnbird_9_16(),
source.johnbird_9_17(),
source.johnbird_9_18(),
source.johnbird_9_19(),
source.johnbird_9_20(),
source.johnbird_10_1(),
source.johnbird_10_2(),
source.johnbird_10_4(),
source.johnbird_10_18(),
source.johnbird_10_19(),
source.johnbird_10_20(),
source.johnbird_10_21(),
source.johnbird_10_22(),
source.johnbird_10_23(),
source.johnbird_10_24(),
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
