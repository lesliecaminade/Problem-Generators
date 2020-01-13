import random
from mathsub import number_theory as source

print('Generating...')
file_name = 'number_theory'

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

question_list = [source.remainder_1(),
source.remainder_2(),
source.descartes_1(),
source.descartes_2(),
source.fibonacci_1(),
source.lucas_1(),
source.digits_base_exponent(),
source.digits_factorial(),
source.trailing_zeroes_1(),
source.gcd_1(),
source.lcm_1()
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
