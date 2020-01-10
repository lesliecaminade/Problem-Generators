import random
from geas import strength_of_materials as source

print('Generating...')
file_name = 'strength_of_materials'

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
source.singer_104(),
source.singer_105(),
source.singer_106(),
source.singer_107(),
source.singer_108(),
source.singer_109(),
source.singer_110(),
source.singer_115(),
source.singer_116(),
source.singer_117(),
source.singer_125(),
source.singer_126(),
source.singer_127(),
source.singer_133(),
source.singer_134(),
source.singer_135(),
source.singer_136(),
source.singer_138(),
source.singer_141(),
source.singer_142(),
source.singer_206(),
source.singer_207(),
source.singer_208(),
source.singer_209(),
source.singer_211(),
source.singer_223(),
source.singer_225(),
source.singer_226(),
source.singer_227(),
source.singer_228(),
source.singer_233(),
source.singer_234(),
source.singer_235(),
source.singer_236(),
source.singer_238(),
source.singer_239(),
source.singer_240(),
source.singer_241(),
source.singer_244(),
source.singer_245(),
source.singer_247(),
source.singer_261(),
source.singer_262(),
source.singer_263(),
source.singer_264(),
source.singer_265(),
source.singer_266(),
source.singer_267(),
source.singer_304(),
source.singer_305(),
source.singer_306(),
source.singer_307(),
source.singer_308(),
source.singer_309(),
source.singer_311(),
source.singer_312(),
source.singer_313()
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