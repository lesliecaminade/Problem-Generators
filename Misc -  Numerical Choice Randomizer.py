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
    temp2 = random.randint(0,3)
    ast = ['','','','']
    ast[temp] = '*'
    
    for i in range(0,4):
        if temp2 == 0:
            numbers.append(random.gauss(number*0.3,number*2))
        if temp2 == 1:
            numbers.append(random.gauss(number*0.5,number*2))
        if temp2 == 2:
            numbers.append(random.gauss(number*1.5,number*2))
        if temp2 == 3:
            numbers.append(random.gauss(number*2,number*2))
            
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
    
    
def fraction(number):    
    numerator_denominator = number.split('/')
    numerator = int(numerator_denominator[0])
    denominator = int(numerator_denominator[1])
    
    a = str(numerator) + '/' + str(denominator) + '*'
    
    bn = random.randint(1,numerator*2)
    bd = random.randint(1,denominator*2)
    if bn % bd == 0:
        b = str(bn/bd)
    else:
        b = str(random.randint(1, numerator*2)) + '/' + str(random.randint(1, denominator*2))

    cn = random.randint(1,numerator*2)
    cd = random.randint(1,denominator*2)
    if cn % cd == 0:
        c = str(cn/cd)
    else:
        c = str(random.randint(1, numerator*2)) + '/' + str(random.randint(1, denominator*2))
        
    dn = random.randint(1,numerator*2)
    dd = random.randint(1,denominator*2)
    if dn % dd == 0:
        d = str(dn/dd)
    else:
        d = str(random.randint(1, numerator*2)) + '/' + str(random.randint(1, denominator*2))
    
    choices = [a,b,c,d]
    random.shuffle(choices)
    
    choice_template = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""



    print(choice_template)
    print()
    pyperclip.copy(choice_template)
    
    
def multiple(input):
    number_list = input.split(' ')
    
    string = ''
    
    
    for i in range(len(number_list)):
        string = string + ' ' + str(random.randint(1, 2*int(number_list[i])))  
    print(string)
    
    string = ''
    
    
    for i in range(len(number_list)):
        string = string + ' ' + str(random.randint(1, 2*int(number_list[i]))) 
    print(string)
    
    
    string = ''
    
    
    for i in range(len(number_list)):
        string = string + ' ' + str(random.randint(1, 2*int(number_list[i]))) 
    print(string)
    
    

        
    
    
def randomize2(number):
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

    # print(choice_template)
    # print()
    # pyperclip.copy(choice_template)
    return choice_template
    
def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1
    
while True:
    command = input()
    if command == 'fraction':
        print('input fraction n/d')
        command = input()
        fraction(command)
        
    elif command == 'multiple':
        print('input multiple numbers')
        command = input()
        multiple(command)
    else:
        randomize(command)
    
    


       
