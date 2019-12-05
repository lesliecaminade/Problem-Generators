import math
import random

import pyperclip


title_string = """Choice Randomizer
Code by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""

def randomize(number):
    stringList = number.split(' ')
    number = float(stringList[0])
    try:
        unit = stringList[1]
    except:
        unit = ''
    temp = random.randint(0,3)
    numbers = []
    temp2 = random.randint(0,1)
    ast = ['','','','']
    ast[temp] = '*'
    
    for i in range(0,4):
        if temp2 == 0:
            numbers.append(random.gauss(number*1.2,number))
        if temp2 == 1:
            numbers.append(random.gauss(number*0.8,number))
    
    numbers[temp] = number
    
    for i in range(0,4):
        numbers[i] = round(numbers[i],num_after_point(number))
  
    choice_template = """A. {a:g} {unit:s}{aa:s}			C. {c:g} {unit:s}{cc:s}
B. {b:g} {unit:s}{bb:s}				D. {d:g} {unit:s}{dd:s}""".format(
a = numbers[0],
b = numbers[1],
c = numbers[2],
d = numbers[3],
aa = ast[0],
bb = ast[1],
cc = ast[2],
dd = ast[3],
unit = unit
)

    print(choice_template)
    print()
    pyperclip.copy(choice_template)
    
def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1
    
while True:
    command = input()
    
    randomize(command)
    


       
