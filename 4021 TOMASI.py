import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import tomasi

x, y = sym.symbols('x y', real = True)

title_string = """TOMASI
Coded by Leslie Caminade Sep 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = [
tomasi.tomasi_14_1(),
tomasi.tomasi_14_2(),
tomasi.tomasi_14_3(),
tomasi.tomasi_14_3_b(),
tomasi.tomasi_14_3_c(),
tomasi.tomasi_14_3_d(),
tomasi.tomasi_15_1(),
tomasi.tomasi_15_2(),
tomasi.tomasi_15_3(),
tomasi.tomasi_15_4(),
tomasi.tomasi_15_5(),
tomasi.tomasi_15_6()
]

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
