import randomizer
import math
import random
import sympy as sp
import stringHandling
import math_common

from common_names import *
#from sympy import *

#symbols for sympy
spa, spb, spc, spd, spx, spy, spz = sp.symbols('a b c d x y z', real = True)
spn = sp.symbols('n', real = True)


title_string = """Permutations and Combinations
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""


class permutationsCombinationsClass:

    def __init__(self):
        form = random.randint(1,1) #check
        if form == 1:
            word = random.sample(commonPermutationWords,1)[0].lower()
            
            denominator = 1
            for character in letters_of_the_alphabet:
                denominator = denominator * math.factorial(word.count(character))
                
            take_n_at_a_time = random.randint(3,len(word))
            word_length = len(word)
            
            permutations = math_common.npr(word_length,take_n_at_a_time)/denominator
            word = word.upper()
            question = """How many permutations can be made out of the letters in the word {word:s} taking {take:g} letters at a time?""".format(
            word = word,
            take = take_n_at_a_time
            )
            
            soln = int(permutations)
        
        self.question = question
        self.soln = soln
        
            
    


print(title_string)
print()




for i in range (1,10):
    A = permutationsCombinationsClass()
    print(str(stringHandling.cleanAst(A.question))) 
    print("""{a:s}*""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
