import randomizer
import random_handler as ran
import sympy_handler as symh
import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import oo

import math
import math_common
import random
import stringHandling
import integral_calculus
import analytic_geometry
import differential_equations
import algebra
import physics
import vectors
x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Vectors - Standard
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""



class genericClass:

    def __init__(self):
        question = ""
        answer = ""
        
        solution = ""
       
        form = random.randint(1,13) #check
        #form = 13
        
        if form == 1: 
            vectorObject = vectors.adding()
            question = vectorObject.question
            answer = vectorObject.answer
        
        if form == 2: 
            vectorObject = vectors.dot_product()
            question = vectorObject.question
            answer = vectorObject.answer

        if form == 3: 
            vectorObject = vectors.cross_product()
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 4:
            vectorObject = vectors.angle_between_two_vectors()
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 5:
            vectorObject = vectors.orthogonal_vectors()
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 6:
            vectorObject = vectors.component_of_a_vector()
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 7:
            vectorObject = vectors.projection_of_a_vector()
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 8:
            vectorObject = vectors.cross_product(version = 1)
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 9:
            vectorObject = vectors.scalar_triple_product(version = random.randint(0,1))
            question = vectorObject.question
            answer = vectorObject.answer

        if form == 10:
            vectorObject = vectors.vector_triple_product()
            question = vectorObject.question
            answer = vectorObject.answer
            
        if form == 11:
            question_object = vectors.gradient_of_a_scalar(version = random.randint(0,4))
            question = question_object.question
            answer = question_object.answer
        
        if form == 12:
            questionObject = vectors.divergence_of_a_vector()
            question = questionObject.question
            answer = questionObject.answer
            
        if form == 13:
            questionObject = vectors.curl_of_a_vector()
            question = questionObject.question
            answer = questionObject.answer
            
            
            
            
        self.question = question
        self.answer = answer
        self.solution = solution

print(title_string)
print()

 
for i in range (1,1000):
    A = genericClass()
    #display(A.question)
    #display(A.answer)
    print('--------------------------------------------')
    print(A.question)
    print(' ')
    print(A.answer)
    print(' ')
    print(' ')
    if solutions_flag == True:
        print("""solution: {a:s}""".format(a=str(A.solution)))
    print()
    



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
