import random
from mathsub import plane_geometry as source

print('Generating...')
file_name = 'plane_geometry'

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

question_list = [source.rgs_1(),
source.rgs_2(),
source.rgs_3(),
source.rgs_4(),
source.rgs_5(),
source.rgs_6(),
source.rgs_8(),
source.rgs_9(),
source.rgs_10(),
source.rgs_12(),
source.rgs_13(),
source.rgs_15(),
source.rgs_16(),
source.rgs_17(),
source.rgs_18(),
source.rgs_19(),
source.rgs_20(),
source.rgs_21(),
source.rgs_22(),
source.rgs_23(),
source.rgs_24(),
source.rgs_26(),
source.rgs_27(),
source.rgs_28(),
source.rgs_29(),
source.rgs_30(),
source.rgs_31(),
source.rgs_32(),
source.rgs_33(),
source.rgs_34(),
source.rgs_35(),
source.rgs_36(),
source.rgs_37(),
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
