import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import microwave as micro

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """Microwave Communications
Coded by Leslie Caminade Aug 2019 www.lesliecaminadecom.wordpress.com"""

questionList = (
micro.jma_5_65(),
micro.jma_5_66(),
micro.jma_5_67(),
micro.jma_5_68(),
micro.jma_5_69(),
micro.jma_5_70(),
micro.jma_5_76(),
micro.jma_5_78(),
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
