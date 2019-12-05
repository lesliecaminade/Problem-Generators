import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import satellite as sat

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """Satellite Communications
Coded by Leslie Caminade Aug 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (
sat.jma_5_89(),
sat.jma_5_93(),
sat.jma_5_94(),
sat.jma_5_96(),
sat.jma_5_97(),
sat.jma_5_98(),
sat.jma_5_99_a(),
sat.jma_5_99_b(),
sat.jma_5_100(),
sat.jma_5_101()
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
