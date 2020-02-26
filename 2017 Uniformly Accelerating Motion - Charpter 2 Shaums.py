import random
from geas import physics as source

print('Generating...')
file_name = 'uniformly_accelerating_motion'

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

question_list = [source.example_2_1(),
source.example_2_2(),
source.example_2_3(),
source.example_2_4(),
source.example_2_8(),
source.example_2_9(),
source.example_2_10(),
source.example_2_11(),
source.example_2_12(),
source.example_2_13(),
source.example_2_14(),
source.example_2_15(),
source.example_2_16(),
source.example_2_17(),
source.example_2_18(),
source.example_2_19(),
source.example_2_20(),
source.example_2_21(),
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

stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
