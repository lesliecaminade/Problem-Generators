import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import schaums3kcalculus as sch
from generator import random_handler as ran

x, y = sym.symbols('x y', real = True)


title_string = """Schaums 3000 Calculus
Coded by Leslie Caminade Aug 2019 
www.lesliecaminadecom.wordpress.com"""

questionList = (

# sch.schaums_6_2(),
# sch.schaums_6_3(),
# sch.schaums_6_4(),
# sch.schaums_6_5(),
# sch.schaums_6_6(),
# sch.schaums_6_7(),
# sch.schaums_6_8(),
# sch.schaums_6_9(),

# sch.schaums_6_14(),
# sch.schaums_6_15(),
# sch.schaums_6_16(),
# sch.schaums_6_17(),
# sch.schaums_6_18(),
# sch.schaums_6_19(),

# sch.schaums_6_20(),
# sch.schaums_6_21(),
# sch.schaums_6_22(),
# sch.schaums_6_23(),
# sch.schaums_6_24(),
# sch.schaums_6_25(),
# sch.schaums_6_26(),
# sch.schaums_6_27(),
# sch.schaums_6_28(),
# sch.schaums_6_29(),

# sch.schaums_6_30(),
# sch.schaums_6_31(),
# sch.schaums_6_32(),
# sch.schaums_6_33(),
# sch.schaums_6_34(),
# sch.schaums_6_35(),
# sch.schaums_6_36(),
# sch.schaums_6_37(),
# sch.schaums_6_38(),
# sch.schaums_6_39(),

# sch.schaums_6_40(),
# sch.schaums_6_41(),

# sch.schaums_6_46(),
# sch.schaums_6_47(),
# sch.schaums_6_48(),
# sch.schaums_6_49(),

# sch.schaums_6_50(),
# sch.schaums_6_51(),
# sch.schaums_6_52(),


#sch.schaums_7_2(),
sch.schaums_7_3(),
sch.schaums_7_4(),
sch.schaums_7_5(),
sch.schaums_7_6(),
sch.schaums_7_7(),
sch.schaums_7_8(),
sch.schaums_7_9(),

sch.schaums_7_10(),

sch.schaums_7_12(),
sch.schaums_7_13(),
sch.schaums_7_14(),

sch.schaums_7_28(),



# sch.schaums_8_1(),

# sch.schaums_8_3(),
# sch.schaums_8_4(),
# sch.schaums_8_5(),

# sch.schaums_8_8(),
# sch.schaums_8_9(),

# sch.schaums_8_10(),
# sch.schaums_8_11(),
# sch.schaums_8_12a(),
# sch.schaums_8_12b(),
# sch.schaums_8_13(),
# sch.schaums_8_14(),
# sch.schaums_8_15(),
# sch.schaums_8_16(),
# sch.schaums_8_17(),
# sch.schaums_8_18(),
# sch.schaums_8_19(),

# sch.schaums_8_20(),
# sch.schaums_8_21(),

# sch.schaums_8_23(),
# sch.schaums_8_24(),

# sch.schaums_8_27(),
# sch.schaums_8_28(),

# sch.schaums_8_32(),
# sch.schaums_8_33(),
# sch.schaums_8_34(),
# sch.schaums_8_35(),
# sch.schaums_8_36(),
# sch.schaums_8_37(),
# sch.schaums_8_38(),
# sch.schaums_8_39(),

# sch.schaums_8_40(),
# sch.schaums_8_41(),

# sch.schaums_8_48(),
# sch.schaums_8_49(),

# sch.schaums_8_50(),
# sch.schaums_8_51(),


# sch.schaums_9_3(),

# sch.schaums_9_6(),
# sch.schaums_9_7(),
# sch.schaums_9_8(),
# sch.schaums_9_9(),

# sch.schaums_9_10(),
# sch.schaums_9_11(),
# sch.schaums_9_12(),
# sch.schaums_9_13(),
# sch.schaums_9_14(),
# sch.schaums_9_15(),
# sch.schaums_9_16(),

# sch.schaums_9_18(),
# sch.schaums_9_19(),

# sch.schaums_9_20(),
# sch.schaums_9_21(),
# sch.schaums_9_22(),
# sch.schaums_9_23(),
# sch.schaums_9_24(),

# sch.schaums_9_35(),
# sch.schaums_9_36(),
# sch.schaums_9_37(),
# sch.schaums_9_38(),
# sch.schaums_9_39(),

# sch.schaums_9_40(),
# sch.schaums_9_41(),
# sch.schaums_9_42(),
# sch.schaums_9_43(),
# sch.schaums_9_44(),
# sch.schaums_9_45(),

# sch.schaums_10_14(),
# sch.schaums_10_15(),
# sch.schaums_10_16(),
# sch.schaums_10_17(),
# sch.schaums_10_18(),
# sch.schaums_10_19(),

# sch.schaums_10_20(),
# sch.schaums_10_21(),
# sch.schaums_10_22(),
# sch.schaums_10_23(),
# sch.schaums_10_24(),
# sch.schaums_10_25(),
# sch.schaums_10_26(),
# sch.schaums_10_27(),
# sch.schaums_10_28(),
# sch.schaums_10_29(),

# sch.schaums_10_30(),
# sch.schaums_10_31(),

# sch.schaums_10_33(),
# sch.schaums_10_34(),
# sch.schaums_10_35(),
# sch.schaums_10_36(),
# sch.schaums_10_37(),
# sch.schaums_10_38(),
# sch.schaums_10_39(),

# sch.schaums_10_40(),
# sch.schaums_10_41(),
# sch.schaums_10_42(),
# sch.schaums_10_43(),
# sch.schaums_10_44(),
# sch.schaums_10_45(),
# sch.schaums_10_46(),
# sch.schaums_10_47(),
# sch.schaums_10_48(),

sch.schaums_11_30(),

sch.schaums_11_44(),
sch.schaums_11_45(),

sch.schaums_12_9(),

sch.schaums_12_10(),
sch.schaums_12_11(),
sch.schaums_12_12(),
sch.schaums_12_13(),
sch.schaums_12_14(),
sch.schaums_12_15(),
sch.schaums_12_16(),
sch.schaums_12_17(),
sch.schaums_12_18(),
sch.schaums_12_19(),

sch.schaums_12_20(),
sch.schaums_12_21(),
sch.schaums_12_22(),
sch.schaums_12_23(),
sch.schaums_12_24(),
sch.schaums_12_25(),

sch.schaums_12_27(),

sch.schaums_12_29(),

sch.schaums_12_30(),
sch.schaums_12_31(),
sch.schaums_12_32(),
sch.schaums_12_33(),
sch.schaums_12_34(),
sch.schaums_12_35(),
sch.schaums_12_36(),
sch.schaums_12_37(),
sch.schaums_12_38(),
sch.schaums_12_39(),

sch.schaums_12_40(),
sch.schaums_12_41(),
sch.schaums_12_42(),

sch.schaums_12_44(),

sch.schaums_12_47(),

sch.schaums_13_3(),
sch.schaums_13_4(),
sch.schaums_13_5(),
sch.schaums_13_6(),
sch.schaums_13_7(),
sch.schaums_13_8(),


sch.schaums_13_10(),
sch.schaums_13_11(),
sch.schaums_13_12(),
sch.schaums_13_13(),
sch.schaums_13_14(),
sch.schaums_13_15(),
sch.schaums_13_16(),
sch.schaums_13_17(),
sch.schaums_13_18(),

sch.schaums_13_22(),
sch.schaums_13_23(),
sch.schaums_13_24(),
sch.schaums_13_25(),
sch.schaums_13_26(),
sch.schaums_13_27(),
sch.schaums_13_28(),
sch.schaums_13_29(),

sch.schaums_13_30(),
sch.schaums_13_31(),
sch.schaums_13_32(),
sch.schaums_13_33(),
sch.schaums_13_34(),
sch.schaums_13_35(),
sch.schaums_13_36(),

sch.schaums_14_1(),
sch.schaums_14_2(),
sch.schaums_14_3(),
sch.schaums_14_4(),
sch.schaums_14_5(),
sch.schaums_14_6(),
sch.schaums_14_7(),
sch.schaums_14_8(),
sch.schaums_14_9(),

sch.schaums_14_10(),
sch.schaums_14_11(),
sch.schaums_14_12(),
sch.schaums_14_13(),
sch.schaums_14_14(),
sch.schaums_14_15(),
sch.schaums_14_16(),
sch.schaums_14_17(),
sch.schaums_14_18(),
sch.schaums_14_19(),

sch.schaums_14_20(),
sch.schaums_14_21(),
sch.schaums_14_22(),
sch.schaums_14_23(),
sch.schaums_14_24(),
sch.schaums_14_25(),
sch.schaums_14_26(),
sch.schaums_14_27(),
sch.schaums_14_28(),
sch.schaums_14_29(),

sch.schaums_14_30(),
sch.schaums_14_31(),
sch.schaums_14_32(),
sch.schaums_14_33(),
sch.schaums_14_34(),
sch.schaums_14_35(),
sch.schaums_14_36(),

sch.schaums_14_38(),
sch.schaums_14_39(),

sch.schaums_14_40(),
sch.schaums_14_41(),
sch.schaums_14_42(),
sch.schaums_14_43(),
sch.schaums_14_44(),
sch.schaums_14_45(),
sch.schaums_14_46(),
sch.schaums_14_47(),
sch.schaums_14_48(),
sch.schaums_14_49(),

sch.schaums_14_50(),
sch.schaums_14_51(),
sch.schaums_14_52(),
sch.schaums_14_53(),
sch.schaums_14_54(),
sch.schaums_14_55(),
sch.schaums_14_56(),

sch.schaums_16_2(),
sch.schaums_16_3(),
sch.schaums_16_4(),
sch.schaums_16_5(),
sch.schaums_16_6(),
sch.schaums_16_7(),
sch.schaums_16_8(),
sch.schaums_16_9(),

sch.schaums_16_10(),
sch.schaums_16_11(),
sch.schaums_16_12(),
sch.schaums_16_13(),
sch.schaums_16_14(),
sch.schaums_16_15(),
sch.schaums_16_16(),
sch.schaums_16_17(),
sch.schaums_16_18(),
sch.schaums_16_19(),

sch.schaums_16_21(),
sch.schaums_16_22(),
sch.schaums_16_23(),
sch.schaums_16_24(),
sch.schaums_16_25(),
sch.schaums_16_26(),
sch.schaums_16_27(),
sch.schaums_16_28(),
sch.schaums_16_29(),

sch.schaums_16_30(),
sch.schaums_16_31(),
sch.schaums_16_32(),
sch.schaums_16_33(),
sch.schaums_16_34(),
sch.schaums_16_35(),
sch.schaums_16_36(),
sch.schaums_16_37(),
sch.schaums_16_38(),
sch.schaums_16_39(),

sch.schaums_16_40(),
sch.schaums_16_41(),
sch.schaums_16_42(),
sch.schaums_16_43(),
sch.schaums_16_44(),
sch.schaums_16_45(),
sch.schaums_16_46(),
sch.schaums_16_47(),
sch.schaums_16_48(),
sch.schaums_16_49(),

sch.schaums_16_50(),
sch.schaums_16_51(),

sch.schaums_16_53(),
sch.schaums_16_54(),

sch.schaums_16_56(),
sch.schaums_16_57(),
sch.schaums_16_58(),
sch.schaums_16_59(),
sch.schaums_16_60(),
sch.schaums_16_61(),

sch.schaums_21_1(),
sch.schaums_21_2(),
sch.schaums_21_3(),
sch.schaums_21_4(),
sch.schaums_21_5(),
sch.schaums_21_6(),
sch.schaums_21_7(),
sch.schaums_21_8(),
sch.schaums_21_9(),

sch.schaums_21_10(),
sch.schaums_21_11(),
sch.schaums_21_12(),
sch.schaums_21_13(),
sch.schaums_21_14(),
sch.schaums_21_15(),
sch.schaums_21_16(),
sch.schaums_21_17(),
sch.schaums_21_18(),
sch.schaums_21_19(),

sch.schaums_21_20(),
sch.schaums_21_21(),
sch.schaums_21_22(),
sch.schaums_21_23(),
sch.schaums_21_24(),
sch.schaums_21_25(),
sch.schaums_21_26(),
sch.schaums_21_27(),
sch.schaums_21_28(),
sch.schaums_21_29(),

sch.schaums_21_30(),
sch.schaums_21_31(),
sch.schaums_21_32(),
sch.schaums_21_33(),
sch.schaums_21_34(),
sch.schaums_21_35(),
sch.schaums_21_36(),
sch.schaums_21_37(),
sch.schaums_21_38(),
sch.schaums_21_39(),

sch.schaums_21_40(),
sch.schaums_21_41(),
sch.schaums_21_42(),

sch.schaums_21_44(),
sch.schaums_21_45(),
sch.schaums_21_46(),
sch.schaums_21_47(),

sch.schaums_22_3(),
sch.schaums_22_4(),
sch.schaums_22_5(),
sch.schaums_22_6(),
sch.schaums_22_7(),

sch.schaums_22_10(),

sch.schaums_22_13(),

sch.schaums_22_15(),
sch.schaums_22_16(),
sch.schaums_22_17(),
sch.schaums_22_18(),
sch.schaums_22_19(),


sch.schaums_22_24(),
sch.schaums_22_25(),

sch.schaums_22_27(),
sch.schaums_22_28(),
sch.schaums_22_29(),

sch.schaums_22_30(),
sch.schaums_22_31(),
sch.schaums_22_32(),
sch.schaums_22_33(),
sch.schaums_22_34(),
sch.schaums_22_35(),
sch.schaums_22_36(),

sch.schaums_22_38(),
sch.schaums_22_39(),

sch.schaums_22_40(),
sch.schaums_22_41(),
sch.schaums_22_42(),
sch.schaums_22_43(),

sch.schaums_22_53(),
sch.schaums_22_54(),
sch.schaums_22_55(),

sch.schaums_22_58()
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
