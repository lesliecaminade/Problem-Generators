import random
from mathsub import vectors as source

print('Generating...')
file_name = 'vectors'

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
CONCEPTS = False

question_list = [
source.Vector_add_Vector_add_Vector(),
source.Dot_product(),
source.Unit_vector_parallel_to_a_vector(),
source.Unit_vector_parallel_to_a_vector_with_magnitude(),
source.Cross_product(),
source.Unit_vector_perpendicular_to_two_vectors(),
source.Unit_vector_perpendicular_to_two_vectors_with_magnitude(),
source.Angle_between_two_vectors(),
source.Orthogonal_vectors(),
source.Component_of_a_vector(),
source.Projection_of_a_vector(),
source.Scalar_triple_product(),
source.Volume_of_parallelipiped(),
source.Vector_triple_product(),
source.Gradient_of_a_scalar(),
source.Divergence_of_a_vector(),
source.Curl_of_a_vector(),
source.Point_Conversion()
]


concept_list = []

if not TESTMODE:
    random.shuffle(question_list)
    random.shuffle(concept_list)

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

if CONCEPTS:
    for i in range (min(len(question_list), len(concept_list))):
        print('-----------------------------------------------------------------------')
        item = random.choice([question_list[i], concept_list[i]])
        print_tasks(item)
        write_to_file(item)
else:
    for i in range (len(question_list)):
        print('-----------------------------------------------------------------------')
        item = question_list[i]
        print_tasks(item)
        write_to_file(item)

print()
file.close()
print('Finished.')
