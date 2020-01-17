import random
from mathsub import probability as source

print('Generating...')
file_name = 'word_problems'

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

question_list = [source.rgs_sample_1(),
source.rgs_sample_2(),
source.rgs_sample_3(),
source.rgs_sample_4(),
source.rgs_sample_5(),
source.rgs_sample_6(),
source.rgs_sample_7(),
source.rgs_sample_8(),
source.rgs_sample_9(),
source.rgs_sample_11(),
source.rgs_sample_12(),
source.rgs_2(),
source.rgs_3(),
source.rgs_5(),
source.rgs_6(),
source.rgs_7(),
source.rgs_8(),
source.rgs_9(),
source.rgs_10(),
source.rgs_11(),
source.rgs_12(),
source.rgs_13(),
source.rgs_14(),
source.rgs_15(),
source.rgs_16(),
source.rgs_17(),
]


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

