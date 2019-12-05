import random
import math

def toListSet(values,amount):
    list = []
    for i in range(0,amount):
        list.append(random.choice(values))
    
    return list


def toInt(num,variance):
    low = num - variance
    high = num + variance
    output = random.randint(low,high)
    return output

def toIntRange(low,high):

    output = random.randint(low,high)
        
    return output

def toFloat(num,variance):
    low = num - variance
    high = num + variance
    output = random.uniform(low,high)
    return output

def toFloatRange(low,high):
    output = random.uniform(low,high)
    return output

def toListFloat(num):
    list = [0,0,0,0]
    if num >= 0:
        low = num * 0.5
        high = num * 1.5
    else:
        high = num * 0.5
        low = num * 1.5
    for i in range(0,4):
        list[i] = random.uniform(low,high)
        #list[i] = round(list[i],2)
    return list

def toListInt(num):
    list = [0,0,0,0] 
    low = num - 10
    high = num + 10
    for i in range(0,4):
        list[i] = random.randint(int(low),int(high))       
    return list
    
def toListIntRange(low, high):
    list = [0,0,0,0]
    for i in range(0,4):
        list[i] = random.randint(int(low),int(high))
    return list

def toListFloatRange(low, high):
    list = [0,0,0,0]
    for i in range(0,4):
        list[i] = random.uniform(low,high)
    return list

def decimalFudger(input, i, k ):
    if i != k:
        output = input + random.uniform(-2,2)
    else:
        output = input
    return output
    
def choiceShuffle(ans, dist1, dist2, dist3):
    map = random.sample([0,1,2,3],4)
    mapping = [0,0,0,0]
    mapping[map[0]] = ans
    mapping[map[1]] = dist1
    mapping[map[2]] = dist2
    mapping[map[3]] = dist3
    choices = ["","","",""]
    choices[0]="A. " + mapping[0]
    choices[1]="B. " + mapping[1]
    choices[2]="C. " + mapping[2]
    choices[3]="D. " + mapping[3]
    
    return choices

    

    
