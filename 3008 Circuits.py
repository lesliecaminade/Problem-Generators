import math
import random

import circuits as ckt


import constants_conversions as c
from constants_conversions import *

title_string = """Electrical Circuits
Coded by Leslie Caminade Sep 25 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
ckt.sadiku_1_1(),
ckt.sadiku_1_2(),
ckt.sadiku_1_3(),
ckt.sadiku_1_4(),
ckt.sadiku_1_5(),
ckt.sadiku_1_6(),
ckt.sadiku_1_7(),
ckt.sadiku_1_8(),
ckt.sadiku_1_9(),
ckt.sadiku_2_1(),
ckt.sadiku_2_2(),
ckt.sadiku_2_3(),
ckt.sadiku_2_5(),
ckt.sadiku_2_6(),
ckt.sadiku_2_7(),
ckt.sadiku_2_8(),
ckt.johnbird_2_1(),
ckt.johnbird_2_2(),
ckt.johnbird_2_3(),
ckt.johnbird_2_4(),
ckt.johnbird_2_5(),
ckt.johnbird_2_6(),
ckt.johnbird_2_7(),
ckt.johnbird_2_9(),
ckt.johnbird_2_10(),
ckt.johnbird_2_11(),
ckt.johnbird_2_12(),
ckt.johnbird_2_13(),
ckt.johnbird_2_14(),
ckt.johnbird_2_15(),
ckt.johnbird_2_16(),
ckt.johnbird_2_17(),
ckt.johnbird_2_18(),
ckt.johnbird_2_19(),
ckt.johnbird_3_1(),
ckt.johnbird_3_2(),
ckt.johnbird_3_3(),
ckt.johnbird_3_4(),
ckt.johnbird_3_5(),
ckt.johnbird_3_6(),
ckt.johnbird_3_7(),
ckt.johnbird_3_9(),
ckt.johnbird_3_10(),
ckt.johnbird_3_11()
)


#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    

fraction = 0.25
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(fraction * len(questionList)))

#this next line shows all items in the database in the correct order


#items_list = total_items_list #for testing purposes - comment if needed


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
