import randomizer
import math
import random
import stringHandling

class domainRangeSetClass:
    
    def __init__(self):
        #self.name = name    # instance variable unique to each instance
        rep = False
        #ask_pos/neg is a boolean variable that indicates whether numbers 0-9(-1 to -9) are included
        ask_pos = random.randint(0,1)
        ask_neg = random.randint(0,1)
        
        if ask_pos == 1 and ask_neg == 1:
            values = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
        elif ask_neg == 1:
            values = [-9,-8,-7,-6,-5,-4,-3,-2,-1]
        else:
            values = [0,1,2,3,4,5,6,7,8,9]
        

        domain = set(random.sample(values,random.randint(1,5)))
        range = set(random.sample(values,random.randint(1,5)))
        
        self.soln = 'Domain: ' + str(domain)
        self.soln2 = 'Range: ' + str(range)

            
        self.question ={(x,y) for x in domain for y in range}     
        
print('DOMAIN AND RANGE (SET): Find the domain and range.')
print()
        
for i in range (1,10):
    A = domainRangeSetClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    #print("""S1: {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    #print("""S2: {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln2)))))
    print("""S1: {a:s}""".format(a=stringHandling.cleanAst(str(A.soln))))
    print("""S2: {a:s}""".format(a=stringHandling.cleanAst(str(A.soln2))))
    print()



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
