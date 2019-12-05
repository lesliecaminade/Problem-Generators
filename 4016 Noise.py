import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import noise

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """Noise
Coded by Leslie Caminade Aug 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (
noise.jma_1_95(),
noise.jma_1_98(),
noise.jma_1_99_a(),
noise.jma_1_99_b(),
noise.jma_1_100(),
noise.jma_1_102_a(),
noise.jma_1_102_b(),
noise.jma_1_104(),
noise.jma_1_105(),
noise.jma_1_108(),
noise.jma_1_109_a(),
noise.jma_1_109_b(),
noise.jma_1_110(),
noise.jma_1_112(),
noise.jma_1_113(),
)



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(1 * len(questionList)))


print(title_string)
print()
print(items_list)

for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print(item.question)
    print()
    print(item.answer)

stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
