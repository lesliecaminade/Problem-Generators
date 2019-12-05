import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c
import grobs

x, y = sym.symbols('x y', real = True)



solutions_flag = False

title_string = """
Coded by Leslie Caminade Sep 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (
#grobs.grobs_1_0(),
grobs.grobs_1_1(),
grobs.grobs_1_2(),
grobs.grobs_1_3(),
grobs.grobs_1_4(),
grobs.grobs_1_5(),
grobs.grobs_1_6(),
grobs.grobs_1_7(),
grobs.grobs_1_8(),
grobs.grobs_1_9(),

grobs.grobs_1_10(),
grobs.grobs_1_11(),
grobs.grobs_1_12(),
grobs.grobs_1_13(),
grobs.grobs_1_14(),
grobs.grobs_1_15(),
grobs.grobs_1_16(),
grobs.grobs_1_17(),
grobs.grobs_1_18(),
grobs.grobs_1_19(),

grobs.grobs_1_20(),
grobs.grobs_1_21(),
grobs.grobs_1_22(),
grobs.grobs_1_23(),
grobs.grobs_1_24(),
grobs.grobs_1_25(),

#---
grobs.grobs_2_1(),
grobs.grobs_2_2(),
grobs.grobs_2_3(),
grobs.grobs_2_4(),
grobs.grobs_2_5(),
grobs.grobs_2_6(),
grobs.grobs_2_7(),
grobs.grobs_2_8(),
grobs.grobs_2_9(),

grobs.grobs_2_10(),
grobs.grobs_2_11(),
grobs.grobs_2_12(),
grobs.grobs_2_13(),
grobs.grobs_2_14(),
grobs.grobs_2_15(),

#----
grobs.grobs_3_1(),
grobs.grobs_3_2(),
grobs.grobs_3_3(),
grobs.grobs_3_4(),
grobs.grobs_3_5(),
grobs.grobs_3_6(),
grobs.grobs_3_7(),
grobs.grobs_3_8(),
grobs.grobs_3_9(),

grobs.grobs_3_10(),
grobs.grobs_3_11(),
grobs.grobs_3_12(),
grobs.grobs_3_13(),
grobs.grobs_3_14(),
grobs.grobs_3_15(),
grobs.grobs_3_16(),
grobs.grobs_3_17(),
grobs.grobs_3_18(),
grobs.grobs_3_19(),

grobs.grobs_3_20(),

#---
grobs.grobs_4_1(),
grobs.grobs_4_2(),
grobs.grobs_4_3(),
grobs.grobs_4_4(),
grobs.grobs_4_5(),
grobs.grobs_4_6(),
grobs.grobs_4_7(),
grobs.grobs_4_8(),
grobs.grobs_4_9(),

grobs.grobs_4_10(),
grobs.grobs_4_11(),
grobs.grobs_4_12(),
grobs.grobs_4_13(),
grobs.grobs_4_14(),
grobs.grobs_4_15(),
grobs.grobs_4_16(),
grobs.grobs_4_17(),
grobs.grobs_4_18(),
grobs.grobs_4_19(),

grobs.grobs_4_20(),
#------
grobs.grobs_5_1(),
grobs.grobs_5_2(),
grobs.grobs_5_3(),
grobs.grobs_5_4(),
grobs.grobs_5_5(),
grobs.grobs_5_6(),
grobs.grobs_5_7(),
grobs.grobs_5_8(),
grobs.grobs_5_9(),

grobs.grobs_5_10(),
grobs.grobs_5_11(),
grobs.grobs_5_12(),
grobs.grobs_5_13(),
grobs.grobs_5_14(),
grobs.grobs_5_15(),
grobs.grobs_5_16(),
grobs.grobs_5_17(),
grobs.grobs_5_18(),
grobs.grobs_5_19(),

grobs.grobs_5_20(),
#-----
grobs.grobs_6_1(),
grobs.grobs_6_2(),
grobs.grobs_6_3(),
grobs.grobs_6_4(),
grobs.grobs_6_5(),
grobs.grobs_6_6(),
grobs.grobs_6_7(),
grobs.grobs_6_8(),
grobs.grobs_6_9(),

grobs.grobs_6_10(),
grobs.grobs_6_11(),
grobs.grobs_6_12(),
grobs.grobs_6_13(),
grobs.grobs_6_14(),
grobs.grobs_6_15(),
grobs.grobs_6_16(),
grobs.grobs_6_17(),
grobs.grobs_6_18(),
grobs.grobs_6_19(),

grobs.grobs_6_20(),
#----
grobs.grobs_7_1(),
grobs.grobs_7_2(),
grobs.grobs_7_3(),
grobs.grobs_7_4(),
grobs.grobs_7_5(),
grobs.grobs_7_6(),
grobs.grobs_7_7(),
grobs.grobs_7_8(),
grobs.grobs_7_9(),

grobs.grobs_7_10(),
#---
grobs.grobs_8_1(),
grobs.grobs_8_2(),
grobs.grobs_8_3(),
grobs.grobs_8_4(),
grobs.grobs_8_5(),
grobs.grobs_8_6(),
grobs.grobs_8_7(),
grobs.grobs_8_8(),
grobs.grobs_8_9(),

grobs.grobs_8_10(),
grobs.grobs_8_11(),
grobs.grobs_8_12(),
grobs.grobs_8_13(),
grobs.grobs_8_14(),
grobs.grobs_8_15(),
grobs.grobs_8_16(),
grobs.grobs_8_17(),
grobs.grobs_8_18(),
grobs.grobs_8_19(),

grobs.grobs_8_20(),
#----
grobs.grobs_9_1(),
grobs.grobs_9_2(),
grobs.grobs_9_3(),
grobs.grobs_9_4(),
grobs.grobs_9_5(),
grobs.grobs_9_6(),
grobs.grobs_9_7(),
grobs.grobs_9_8(),
grobs.grobs_9_9(),

grobs.grobs_9_10(),
grobs.grobs_9_11(),
grobs.grobs_9_12(),
grobs.grobs_9_13(),
grobs.grobs_9_14(),
grobs.grobs_9_15(),
#----
grobs.grobs_10_1(),
grobs.grobs_10_2(),
grobs.grobs_10_3(),
grobs.grobs_10_4(),
grobs.grobs_10_5(),
grobs.grobs_10_6(),
grobs.grobs_10_7(),
grobs.grobs_10_8(),
grobs.grobs_10_9(),

grobs.grobs_10_10(),
#----
grobs.grobs_11_1(),
grobs.grobs_11_2(),
grobs.grobs_11_3(),
grobs.grobs_11_4(),
grobs.grobs_11_5(),
grobs.grobs_11_6(),
grobs.grobs_11_7(),
grobs.grobs_11_8(),
grobs.grobs_11_9(),

grobs.grobs_11_10(),
grobs.grobs_11_11(),
grobs.grobs_11_12(),
grobs.grobs_11_13(),
grobs.grobs_11_14(),
grobs.grobs_11_15(),
#----
grobs.grobs_12_1(),
grobs.grobs_12_2(),
grobs.grobs_12_3(),
grobs.grobs_12_4(),
grobs.grobs_12_5(),
grobs.grobs_12_6(),
grobs.grobs_12_7(),
grobs.grobs_12_8(),
grobs.grobs_12_9(),

grobs.grobs_12_10(),
grobs.grobs_12_11(),
grobs.grobs_12_12(),
grobs.grobs_12_13(),
grobs.grobs_12_14(),
grobs.grobs_12_15(),
#---
grobs.grobs_13_1(),
grobs.grobs_13_2(),
grobs.grobs_13_3(),
grobs.grobs_13_4(),
grobs.grobs_13_5(),
grobs.grobs_13_6(),
grobs.grobs_13_7(),
grobs.grobs_13_8(),
grobs.grobs_13_9(),

grobs.grobs_13_10(),
grobs.grobs_13_11(),
grobs.grobs_13_12(),
grobs.grobs_13_13(),
grobs.grobs_13_14(),
grobs.grobs_13_15(),
grobs.grobs_13_16(),
grobs.grobs_13_17(),
grobs.grobs_13_18(),
grobs.grobs_13_19(),

grobs.grobs_13_20(),
grobs.grobs_13_21(),
grobs.grobs_13_22(),
grobs.grobs_13_23(),
grobs.grobs_13_24(),
grobs.grobs_13_25(),
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
