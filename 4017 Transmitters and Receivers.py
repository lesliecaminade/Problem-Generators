import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import transmitters_and_receivers as txrx

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """Transmitters and Receivers
Coded by Leslie Caminade Aug 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (
txrx.jma_1_127_a(),
txrx.jma_1_127_b(),
txrx.jma_1_128(),
txrx.jma_1_129(),
txrx.jma_1_130(),
txrx.jma_1_131(),
txrx.jma_1_132(),
txrx.jma_1_133(),
txrx.jma_1_135(),
txrx.jma_1_137_a(),
txrx.jma_1_137_b()
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
