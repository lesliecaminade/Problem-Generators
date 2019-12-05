import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import cellular as cell

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """Cellular Communications
Coded by Leslie Caminade Aug 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (
cell.jma_5_121(),
cell.jma_5_122(),
cell.jma_5_123_a(),
cell.jma_5_123_b(),
cell.jma_5_132_a(),
cell.jma_5_132_b(),
cell.jma_5_133_a(),
cell.jma_5_133_b()
)



#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(0.25 * len(questionList)))


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
