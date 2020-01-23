import randomizer
import math
import random
import sympy as sp
import stringHandling

from common_names import *
#from sympy import *

#symbols for sympy
spa, spb, spc, spd, spx, spy, spz = sp.symbols('a b c d x y z', real = True)
spn = sp.symbols('n', real = True)


title_string = """Set (Venn Diagrams)
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""
SPEED_OF_LIGHT = 299792458

class setVennDiagramClass:

    def __init__(self):
        form = random.randint(1,4) #check
        if form == 1:
            a_only = random.randint(10,50)
            b_only = random.randint(10,50)
            a_int_b = random.randint(1,min(a_only,b_only))
            complement_of_a_union_b = random.randint(1,9)
            universe = a_only + b_only + a_int_b + complement_of_a_union_b
            subjects_temp = ['','']
            subjects_temp = random.sample(subjects,2)
            a_standard = a_only + a_int_b
            b_standard = b_only + a_int_b
            
        
            question = """A class of {U:g} took examination in {subject1:s} and {subject2:s}. If {subject1_passers:g} passed {subject1:s}, {subject2_passers:g} passed {subject2:s}, and {failed_both:g} failed in both subjects, the number of students who passed the two subjects is:""".format(
            U = universe,
            subject1 = subjects_temp[0],
            subject2 = subjects_temp[1],
            subject1_passers = a_standard,
            subject2_passers = b_standard,
            failed_both = complement_of_a_union_b,
            )
            
            soln = a_int_b
            
        if form == 2:
            a_only = random.randint(10,50)
            b_only = random.randint(10,50)
            a_int_b = random.randint(1,min(a_only,b_only))
            complement_of_a_union_b = 0
            universe = a_only + b_only + a_int_b + complement_of_a_union_b
            subjects_temp = ['','']
            subjects_temp = random.sample(subjects,2)
            a_standard = a_only + a_int_b
            b_standard = b_only + a_int_b
            
            question = """In a class of {universe:g} students, {a:g} students like {sub1:s} and {b:g} like {sub2:s}. How many students liked both {sub1:s} and {sub2:s}?""".format(
            universe = universe,
            a = a_standard,
            b = b_standard,
            sub1 = subjects_temp[0],
            sub2 = subjects_temp[1]
            )
            
            soln = a_int_b
            
        if form == 3:
            a_only = random.randint(20,100)
            b_only = random.randint(20,100)
            c_only = random.randint(20,100)
            
            
            a_int_b_minus_c = random.randint(1,min(a_only,b_only,c_only))
            b_int_c_minus_a = random.randint(1,min(a_only,b_only,c_only))
            c_int_a_minus_b = random.randint(1,min(a_only,b_only,c_only)) 
            
            a_int_b_int_c = 0
            
            complement_of_a_union_b_union_c = random.randint(1,min(a_only,b_only,c_only))
            
            universe = a_only + b_only + c_only + a_int_b_minus_c + b_int_c_minus_a + c_int_a_minus_b + a_int_b_int_c + complement_of_a_union_b_union_c
            

            a = a_only + a_int_b_minus_c + c_int_a_minus_b + a_int_b_int_c
            b = b_only + b_int_c_minus_a + a_int_b_minus_c + a_int_b_int_c
            c = c_only + c_int_a_minus_b + b_int_c_minus_a + a_int_b_int_c
            
            question = """In a commercial survey involving {u:g} persons on brand preferences, {x_only:g} were found to prefer brand x only, {y_only:g} persons prefer brand y only, {z_only:g} persons prefer brand z only, {x_union_y_minus_z:g} prefer either brand x or y but not z, {y_union_z_minus_x:g} prefer either brand y or z but not x, {z_union_x_minus_y:g} prefer either brand z or x but not y, and none prefer all three brands at the same time. How many persons have no brand preference with any of the three brands?""".format(
            u = universe,
            x_only = a_only,
            y_only = b_only,
            z_only = c_only,
            x_union_y_minus_z = a_only + a_int_b_minus_c + b_only,
            y_union_z_minus_x = b_only + b_int_c_minus_a + c_only,
            z_union_x_minus_y = c_only + c_int_a_minus_b + a_only,
            )
            
            soln = complement_of_a_union_b_union_c
        
        if form == 4:
            a_only = random.randint(1,50)
            b_only = random.randint(1,50)
            a_int_b = random.randint(1,min(a_only,b_only))
            complement_of_a_union_b = 0
            universe = a_only + b_only + a_int_b + complement_of_a_union_b
            subjects_temp = ['','']
            subjects_temp = random.sample(subjects,2)
            a = a_only + a_int_b
            b = b_only + a_int_b
            if sp.ntheory.primetest.isprime(universe):
                frac_a = a/universe
                frac_b = b/universe
                frac_a = str(frac_a)
                frac_b = str(frac_b)
            else:
                frac_a = sp.Rational(a,universe)
                frac_b = sp.Rational(b,universe)
                frac_a = str(frac_a)
                frac_b = str(frac_b)
            
            question = """The probability for the examinees from a certain school to pass the {subject1:s} subject is {prob_a:s} and that for the {subject2:s} is {prob_b:s}. If none of the examinees failed in both subjects and there are {pass_both:g} examinees who pass both subjects, how many examinees from the school took the examination?""".format(
            subject1 = subjects_temp[0],
            subject2 = subjects_temp[1],
            prob_a = frac_a,
            prob_b = frac_b,
            pass_both = a_int_b
            
            )
            
            soln = universe        
        self.question = question
        self.soln = soln
        
            
            


print(title_string)
print()


 
for i in range (1,10):
    A = setVennDiagramClass()
    print(str(stringHandling.cleanAst(A.question))) 
    print("""{a:s}*""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
