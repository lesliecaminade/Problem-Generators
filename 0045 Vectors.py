import math
import random
from generator import constants_conversions as c
from mathsub import vectors as source
from generator import random_handler as ran

print('Generating...')

TESTMODE = True

questionList = [
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
source.Curl_of_a_vector()
]

tryagain = True
while tryagain:
    try:
        additional_questionlist = [
        #insert hard to generate questions here
        ]
        tryagain = False
    except:
        pass



questionList = questionList + additional_questionlist



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
if not TESTMODE:
    items_list = random.sample(total_items_list, round(1 * len(questionList)))
else:
    items_list = total_items_list

print(items_list)

for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print(item.question)
    print()
    print(item.answer + '        --------------------------------- answer')
    print()
    print()

    try:
        print(item.choices)
        print()
    except:
        pass

print()
print('Finished.')
stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
