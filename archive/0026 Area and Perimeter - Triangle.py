import randomizer
import math
import random
import sympy as sp
import stringHandling

from common_names import *
from sympy import *


#symbols for sympy
a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)
n = symbols('n', real = True)



class areaAndPerimeterTriangleClass:

    def __init__(self):
        form = random.randint(1,4)
        
        self.generateSides()
        
        if form == 1:
            image = 'https://lesliecaminadecom.files.wordpress.com/2019/04/rj7xsithdou8945xw2j6.png'
            semiperimeter = (side_a + side_b + side_c)/2
            area = math.sqrt(semiperimeter*(semiperimeter-side_a)*(semiperimeter-side_b)*(semiperimeter-side_c))
            perimeter = side_a + side_b + side_c
            problem = """Find the area and perimeter of the following triangle: {im:s}, a = {a:g}, b = {b:g}, c = {c:g}""".format(im=image,a=side_a,b=side_b,c=side_c) 
            soln = area
            soln2 = perimeter
        
        if form == 2:
            image = 'https://lesliecaminadecom.files.wordpress.com/2019/04/7fx3a86lussjrl4pxk4i.png'

            semiperimeter = (side_a + side_b + side_c)/2
            area = math.sqrt(semiperimeter*(semiperimeter-side_a)*(semiperimeter-side_b)*(semiperimeter-side_c))
            perimeter = side_a + side_b + side_c
            problem = """Find the area and perimeter of the following triangle: {im:s}, a = {a:g}, b = {b:g}, c = {c:g}""".format(im=image,a=side_a,b=side_b,c=side_c) 
            soln = area
            soln2 = perimeter

        if form == 3:
            image = 'https://lesliecaminadecom.files.wordpress.com/2019/04/g11wapjmgjpz2t397ij2.png'

            side_c = side_b
            semiperimeter = (side_a + side_b + side_c)/2
            area = math.sqrt(semiperimeter*(semiperimeter-side_a)*(semiperimeter-side_b)*(semiperimeter-side_c))
            perimeter = side_a + side_b + side_c
            problem = """Find the area and perimeter of the following triangle: {im:s}, a = {a:g}, b = {b:g}""".format(im=image,a=side_a,b=side_b,c=side_c) 
            soln = area
            soln2 = perimeter        
            
        if form == 4:
            image = 'https://lesliecaminadecom.files.wordpress.com/2019/04/4ahtno51o24yeqp0c552.png'

            side_b = side_a
            side_c = side_b
            semiperimeter = (side_a + side_b + side_c)/2
            area = math.sqrt(semiperimeter*(semiperimeter-side_a)*(semiperimeter-side_b)*(semiperimeter-side_c))
            perimeter = side_a + side_b + side_c
            problem = """Find the area and perimeter of the following triangle: {im:s}, s = {a:g}""".format(im=image,a=side_a,b=side_b,c=side_c) 
            soln = area
            soln2 = perimeter                
            
           
        self.question = problem
        self.soln = 'area: '+str(soln) 
        self.soln2 = 'perimeter: '+str(soln2)
       
    def generateSides(self):
        side_a = random.uniform(1,10)
        side_b = random.uniform(1,10)
        side_c = random.uniform(1,10)
        
        a_and_b = side_a + side_b
        b_and_c = side_b + side_c
        c_and_a = side_c + side_a
        
        while not(side_a > b_and_c and side_b > c_and_a and side_c > a_and_b):
            side_a = random.uniform(1,10)
            side_b = random.uniform(1,10)
            side_c = random.uniform(1,10)
        
        return self
            
            


print('TRIANGLE AREAS 1 ')
print()


 
for i in range (1,10):
    A = areaAndPerimeterTriangleClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))

    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
