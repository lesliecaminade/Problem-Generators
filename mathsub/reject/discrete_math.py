from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import discrete_math_engine as de
from num2words import num2words

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables
            
#sanfoundry---
class sanfoundry_1:
    def __init__(self):
        choice_a = 'relation'
        choice_b = 'function'
        choice_c = 'set*'
        choice_d = 'proposition'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""A ____ is an ordered collection of objects."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_2:
    def __init__(self):
        choice_a = '{1, 2, 3}'
        choice_b = '{1, 3, 5, 7, 9}*'
        choice_c = '{1, 2, 5, 9}'
        choice_d = '{1, 5, 7, 9, 11}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""The set O of odd positice integers less than 10 can be expressed by ____."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""
        
class sanfoundry_3:
    def __init__(self):
        choice_a = 'One*'
        choice_b = 'Two'
        choice_c = 'Zero'
        choice_d = 'Three'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Power set of empty set has exactly _____ subset."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class sanfoundry_4:
    def __init__(self):
        choice_a = '{(1, a), (1, b), (2, a), (b, b)}'
        choice_b = '{(1, 1), (2, 2), (a, a), (b, b)}'
        choice_c = '{(1, a), (2, a), (1, b), (2, b)}*'
        choice_d = '{(1, 1), (a, a), (2, a), (1, b)}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""What is the cartesian product of A = {{1, 2}} and B = {{a, b}}?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_6:
    def __init__(self):
        choice_a = '10'
        choice_b = '5*'
        choice_c = '3'
        choice_d = '20'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""What is the cardinality of the set of odd positive integers less than 10?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_7:
    def __init__(self):
        choice_a = 'A = {1, 2} and B = {1}'
        choice_b = 'A = {1, 2} and B = {1, 2, 3}'
        choice_c = 'A = {1, 2, 3} and B = {2, 1, 3}*'
        choice_d = 'A = {1, 2, 4} and B = {1, 2, 3}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Which of the following two sets are equal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_8:
    def __init__(self):
        choice_a = 'infinite*'
        choice_b = 'finite'
        choice_c = 'subset'
        choice_d = 'empty'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""The set of positive integers is ______."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_9:
    def __init__(self):
        choice_a = '8*'
        choice_b = '6'
        choice_c = '7'
        choice_d = '9'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""What is the cardinality of the power set of the set {{0, 1, 2}}?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_10:
    def __init__(self):
        choice_a = '{0, 2, 4, 5, 9, 58, 49, 56, 99, 12}'
        choice_b = '{0, 1, 4, 9, 16, 25, 36, 49, 64, 81}*'
        choice_c = '{1, 4, 9, 16, 25, 36, 64, 81, 85, 99}'
        choice_d = '{0, 1, 4, 9, 16, 25, 36, 49, 64, 121}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""The members of the set S = {{x | x is a square of an integer and x < 100 }} is _______."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_11:
    def __init__(self):
        choice_a = 'empty set'
        choice_b = 'non - empty set'
        choice_c = 'finite set'
        choice_d = 'both B and C*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)
        self.question = f"""{{x: x is an integer neither positive nor negative }} is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class sanfoundry_12:
    def __init__(self):
        choice_a = 'infinite set*'
        choice_b = 'finite set'
        choice_c = 'empty set'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = '{x: x is a real number between 1 and 2} is an'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_13:
    def __init__(self):
        choice_a = '{x: either x=1 or x=5n, where n is a real number}'
        choice_b = '{x: either x=1 or x=5n, where n is a integer}'
        choice_c = '{x: either x=1 or x=5n, where n is an odd natural number}*'
        choice_d = '{x: x=5n, where n is a natural number}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'Write set {1, 5, 15, 25, ...} in set-builder form: '
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_14:
    def __init__(self):
        choice_a = '{1⁄2, 2⁄3, 4⁄5, 6⁄7}'
        choice_b = '{1⁄2, 2⁄3, 3⁄4, 4⁄5, 5⁄6, 6⁄7, 7⁄8}'
        choice_c = '{1⁄2, 2⁄3, 3⁄4, 4⁄5, 5⁄6, 6⁄7}*'
        choice_d = 'infinite'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'Express {x: x= n/(n+1), n is a natural number less than 7} in roster form:'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_15:
    def __init__(self):
        choice_a = '3'
        choice_b = '4*'
        choice_c = '2'
        choice_d = '5'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'Number of power set of {a, b}, where a and b are distinct elements.'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_16:
    def __init__(self):
        choice_a = '{1, 2}'
        choice_b = '{1, 2, 3}'
        choice_c = '{1}'
        choice_d = 'all of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'Which of the following is subset of set {1, 2, 3, 4}?'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_17:
    def __init__(self):
        choice_a = f'{{{{∅,{{∅}}}} ∈ A'
        choice_b = f'{{2}} ∈ A'
        choice_c = f'∅ ⊂ A*'
        choice_d = f'3 ⊂ A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""A = {{∅,{{∅}},2,{{2,∅}},3}} ,which of the following is true"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_18:
    def __init__(self):
        choice_a = f'A'
        choice_b = f'{{}}'
        choice_c = f'∅'
        choice_d = f'all of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Subset of the set A= {{ }} is:'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_19:
    def __init__(self):
        choice_a = 'infinite set*'
        choice_b = 'finite set'
        choice_c = 'empty set'
        choice_d = 'not a set'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'{{x: x ∈ N and x is prime}} then it is:'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_20:
    def __init__(self):
        choice_a = f'{{2, 3, 5}}'
        choice_b = f'{{2, 3, 6}}'
        choice_c = f'{{2, 3}}*'
        choice_d = f'{{∅}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Convert set {{x: x is a positive prime number which divides 72}} in roster form:'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_21:
    def __init__(self):
        choice_a = f'{{1, 2, 6, 1}}'
        choice_b = f'{{1, 2, 6, 1}}*'
        choice_c = f'{{1, 2, 1, 2}}'
        choice_d = f'{{1, 5, 6, 3}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'The union of the sets {{1, 2, 5}} and {{1, 2, 6}} is the set _______________'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_22:
    def __init__(self):
        choice_a = f'{{1, 2}}*'
        choice_b = f'{{5, 6}}'
        choice_c = f'{{2, 5}}'
        choice_d = f'{{1, 6}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'The intersection of the sets {{1, 2, 5}} and {{1, 2, 6}} is the set _____________'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_23:
    def __init__(self):
        choice_a = 'union'
        choice_b = 'difference'
        choice_c = 'intersection*'
        choice_d = 'complement' 

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Two sets are called disjoint if their _____ is the empty set' 
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_24:
    def __init__(self):
        choice_a = f'{{1, 3, 5}} and {{1, 3, 6}}'
        choice_b = f'{{1, 2, 3}} and {{1, 2, 3}}'
        choice_c = f'{{1, 3, 5}} and {{2, 3, 4}}'
        choice_d = f'{{1, 3, 5}} and {{2, 4, 6}}*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'Which of the following two sets are disjoint?'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_25:
    def __init__(self):
        choice_a = f'{{1}}'
        choice_b = f'{{5}}'
        choice_c = f'{{3}}*'
        choice_d = f'{{2}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'The difference of {{1, 2, 3}} and {{1, 2, 5}} is the set ____________'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_26:
    def __init__(self):
        choice_a = 'A - B'
        choice_b = 'U - A*'
        choice_c = 'A - U' 
        choice_d = 'B - A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'The complement of set A is _______'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_27:
    def __init__(self):
        choice_a = '0101010101*'
        choice_b = '1010101010'
        choice_c = '1010010101'
        choice_d = '0010010101'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'The bit string for the set {{2, 4, 6, 8, 10}} (with universal set of natural numbers less than or equal to 10) is ____________________'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_28:
    def __init__(self):
        choice_a = 'union'
        choice_b = 'intersection*'
        choice_c = 'set difference'
        choice_d = 'disjoint'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Let Ai = {{i, i+1, i+2, …..}}. Then set {{n, n+1, n+2, n+3, …..}} is the _________ of the set Ai.'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_29:
    def __init__(self):
        choice_a = '1010100000'
        choice_b = '1010101101'
        choice_c = '1111111100'
        choice_d = '1111101010*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'The bit strings for the sets are 1111100000 and 1010101010. The union of these sets is ___________'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_30:
    def __init__(self):
        choice_a = 'A*'
        choice_b = 'null'
        choice_c = 'U'
        choice_d = 'B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'The set difference of the set A with null set is __________'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_31:
    def __init__(self):
        choice_a = '4*'
        choice_b = '5'
        choice_c = '6'
        choice_d = '7'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Let the set A is {{1, 2, 3}} and B is {{2, 3, 4}}. Then number of elements in A U B is'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_32:
    def __init__(self):
        choice_a = '1'
        choice_b = '2*'
        choice_c = '3'
        choice_d = '4'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Let the set A is {{1, 2, 3}} and B is {{ 2, 3, 4}}. Then number of elements in A ∩ B is'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_33:
    def __init__(self):
        choice_a = f'{{1, -4}}'
        choice_b = f'{{1, 2, 3}}'
        choice_c = f'{{1}}*'
        choice_d = f'{{2, 3}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Let the set A is {{1, 2, 3}} and B is {{2, 3, 4}}. Then the set A – B is'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_34:
    def __init__(self):
        choice_a = f'A= {{1, 2, 3}}, B ={{2, 3, 4}}'
        choice_b = f'A= {{1, 2, 3}}, B ={{1, 2, 3, 4}}'
        choice_c = f'A={{1, 2, 3}}, B ={{2, 3, 1}}*'
        choice_d = f'A={{1, 2, 3, 4, 5, 6}}, B ={{2, 3, 4, 5, 1}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'In which of the following sets A- B is equal to B – A?'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_35:
    def __init__(self):
        choice_a = f'A ≡ B U C'
        choice_b = f'B is a singleton set.'
        choice_c = f'A ≡ C U {2}'
        choice_d = f'all of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'Let A be set of all prime numbers, B be the set of all even prime numbers, C be the set of all odd prime numbers, then which of the following is true?'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_36:
    def __init__(self):
        choice_a = f'4, 8'
        choice_b = f'8, 12*'
        choice_c = f'4, 12'
        choice_d = f'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'If A has 4 elements B has 8 elements then the minimum and maximum number of elements in A U B are respectively'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_37:
    def __init__(self):
        choice_a = '2'
        choice_b = '4*'
        choice_c = '6' 
        choice_d = '8'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'If A is {{{{Φ}}, {{Φ, {{Φ}}}}, then the power set of A has how many element?'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_38:
    def __init__(self):
        choice_a = '4, 5*'
        choice_b = '6, 7'
        choice_c = '2, 3'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Two sets A and B contains a and b elements respectively .If power set of A contains 16 more elements than that of B, value of ‘b’ and ‘a’ are respectively'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_39:
    def __init__(self):
        choice_a = f'{{1, 2, 3, 4, 5, 6, ….}}'
        choice_b = f'{{5, 6, 7, 8, 9, ……}}'
        choice_c = f'{{1, 2, 3, 4}}*'
        choice_d = f'all of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question =  f'Let A be {{1, 2, 3, 4}}, U be set of all natural numbers, then U-A’(complement of A) is given by set.'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_40:
    def __init__(self):
        choice_a = f'{{x: x is a even prime greater than 3}}'
        choice_b = f'{{x : x is a multiple of 2 and is odd}}'
        choice_c = f'{{x: x is an even number and x+3 is even}}'
        choice_d = f'{{ x: x is a prime number less than 5 and is odd}}*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f'Which set is not empty?'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_41:
    def __init__(self):
        choice_a = 'A ∩ B*'
        choice_b = 'A U B'
        choice_c = 'A'
        choice_d = 'B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'The shaded area in the figure is best described by: https://lesliecaminadecom.files.wordpress.com/2019/10/discrete-mathematics-questions-answers-venn-diagram-q1.png'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_42:
    def __init__(self):
        choice_a = 'A‘ (Complement of A)'
        choice_b = 'A U B -B*'
        choice_c = 'A ∩ B'
        choice_d = 'B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'The shaded area of the figure is best described by: https://lesliecaminadecom.files.wordpress.com/2019/10/discrete-mathematics-questions-answers-venn-diagram-q2.png'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_43:
    def __init__(self):
        choice_a = '20'
        choice_b = '30'
        choice_c = '40'
        choice_d = '10*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'If n(A)=20 and n(B)=30 and n(A U B) = 40 then n(A ∩ B) is'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_44:
    def __init__(self):
        choice_a = 'A‘ (Complement of A)'
        choice_b = 'B – (A ∩ B) – (C ∩ B)*'
        choice_c = 'A ∩ C ∩ B'
        choice_d = 'B’ (Complement of B)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'The shaded area in the figure is best described by: https://lesliecaminadecom.files.wordpress.com/2019/10/discrete-mathematics-questions-answers-venn-diagram-q4.png'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_45:
    def __init__(self):
        choice_a = 'A is subset of B and B is subset of C'
        choice_b = 'C is not a subset of A and A is subset of B'
        choice_c = 'C is subset of B and B is subset of A*'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = 'The relation between sets A,B,C as shown by venn diagram is'
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_46:
    def __init__(self):
        choice_a = 'Z contains both X and Y*'
        choice_b = 'Z contains X and Y is outside'
        choice_c = 'X contains Y and Z'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let A: All badminton players are good sportspersons.
Let B: All persons who play cricket are good sportspersons.
Let X denote the set of all badminton players, Y of all cricket players, Z of all good sportspersons. Then which of the following statements is correct?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_47:
    def __init__(self):
        choice_a = 'n(A U B)=0'
        choice_b = 'n( B U C)=0'
        choice_c = 'n( A U B U C)=90'
        choice_d = 'all of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If n(A)=10 , n(B)=30,n(C)=50 and if set A,B,C are pairwise disjoint then which of the following is correct?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_48:
    def __init__(self):
        choice_a = '35*'
        choice_b = '20'
        choice_c = '30'
        choice_d = '10'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""In the given figure the if n(A)=20,n(U)=50,n(C)=10 and n(A∩B)=5 then n(B)=?: https://lesliecaminadecom.files.wordpress.com/2019/10/discrete-mathematics-questions-answers-venn-diagram-q8.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_49:
    def __init__(self):
        choice_a = '16'
        choice_b = '8'
        choice_c = '4*'
        choice_d = '10'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let the students who likes table tennis be 12,the ones who like lawn tennis 10,those who like only table tennis are 6,then number of students who likes only lawn tennis are, assuming there are total of 16 students."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_50:
    def __init__(self):
        choice_a = 'A‘ (Complement of A)'
        choice_b = 'A U B – (A ∩ B)*'
        choice_c = 'A – B'
        choice_d = 'B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""The shaded area of figure is best described by: https://lesliecaminadecom.files.wordpress.com/2019/10/discrete-mathematics-questions-answers-venn-diagram-q10.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_51:
    def __init__(self):
        choice_a = 'Both of the statements*'
        choice_b = 'Only 1st statement'
        choice_c = 'Only 2nd statement'
        choice_d = 'None of the statements'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let C and D be two sets then which of the following statements are true?
1) C U D = D U C
2) C ∩ D = D ∩ C"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_52:
    def __init__(self):
        choice_a = f'{{1, 2, 4, 5}}'
        choice_b = f'{{1, 2, 3}}'
        choice_c = f'{{1, 2, 3, 4, 5}}*'
        choice_d = f'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If set C is {{1, 2, 3, 4}} and C – D = Φ then set D can be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_53:
    def __init__(self):
        choice_a = f'C’ ∩ D'
        choice_b = f'C‘∩ D’'
        choice_c = f'C ∩ D’*'
        choice_d = f'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let C and D be two sets then C – D is equivalent to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_54:
    def __init__(self):
        choice_a = 'C'
        choice_b = 'D'
        choice_c = 'Φ*'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""For two sets C and D the set (C – D) ∩ D will be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfroundry_55:
    def __init__(self):
        choice_a = f'A ∩ A = A'
        choice_b = f'A U A = A'
        choice_c = f'A – (B ∩ C) = (A – B) U (A –C)'
        choice_d = f'(A U B)’ =A’ U B’*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Which of the following statement regarding sets is false"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_56:
    def __init__(self):
        choice_a = f'C – D = D – C'
        choice_b = f'C U D = C ∩ D'
        choice_c = f'C ∩ D = C – D*'
        choice_d = f'C – D = Φ'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let C = {{1,2,3,4}} and D = {{1, 2, 3, 4}} then which of the following hold not true in this case"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_57:
    def __init__(self):
        choice_a = f'(C ∩ (D U E))’'
        choice_b = f'(C ∩( D∩ E’))’'
        choice_c = f'(C ∩( D’ U E))’*'
        choice_d = f'(C U ( D ∩ E’)’'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If C’ U (D ∩ E’) is equivalent to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_58:
    def __init__(self):
        choice_a = f'8*'
        choice_b = f'7'
        choice_c = f'1'
        choice_d = f'3'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let Universal set U is {{1, 2, 3, 4, 5, 6, 7, 8}} ,(Complement of A) A’ is {{2, 5, 6, 7}}, A ∩ B is {{1, 3, 4}} then the set B’ will surely have of which of the element"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_59:
    def __init__(self):
        choice_a = 'φ, φ'
        choice_b = 'φ, A*'
        choice_c = 'A, φ'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let a set be A then A ∩ φ and A U φ are respectively"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_60:
    def __init__(self):
        choice_a = '8*'
        choice_b = '14'
        choice_c = '22'
        choice_d = '15'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If in sets A, B, C, the set B ∩ C consists of 8 elements, set A ∩ B consists of 7 elements and set C ∩ A consists of 7 elements then the minimum element in set A U B U C will be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_61:
    def __init__(self):
        choice_a = f'{{1, 2, 3, 4}}'
        choice_b = f'{{(1, 3) ,(2, 4)}}'
        choice_c = f'{{(1, 3) , (2, 4), (1, 4) , (2, 3) }}*'
        choice_d = f'{{(3, 1), (4, 1)}}'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let set A ={{1, 2}} and C be {{3, 4}} then A X B (Cartesian product of set A and B) is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_62:
    def __init__(self):
        choice_a = '12*'
        choice_b = '14'
        choice_c = '24'
        choice_d = '7'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If set A has 4 elements and B has 3 elements then set n(A X B) is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_63:
    def __init__(self):
        choice_a = '9'
        choice_b = '27*'
        choice_c = '6'
        choice_d = '19'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If set A has 3 elements then number of elements in A X A X A are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_64:
    def __init__(self):
        choice_a = f'A X B = B X A*'
        choice_b = f'A X B ≠ B X A'
        choice_c = f'n(A X B) = n(A) * n(B)'
        choice_d = f'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Which of the following statements regarding sets is false ?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_65:
    def __init__(self):
        choice_a = f'n(A)=2, n(B)=18'
        choice_b = f'n(A)=9, n(B)=4'
        choice_c = f'n(A)=6, n(b)=6*'
        choice_d = f'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If n(A X B) = n(B X A) = 36 then which of the following may hold true?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_67:
    def __init__(self):
        choice_a = f'(A X C) ∩ (B X D)*'
        choice_b = f'(A X D) U (B X C)'
        choice_c = f'(A X C) U ( B X D)'
        choice_d = f'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let the sets be A, B, C, D then (A ∩ B) X (C ∩ D) is equivalent to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_69:
    def __init__(self):
        choice_a = '1024'
        choice_b = '2048'
        choice_c = '512'
        choice_d = '4096*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If set A and B have 3 and 4 elements respectively then the number of subsets of set (A X B) is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_70:
    def __init__(self):
        choice_a = f'A={{1, 2, 3}} , B={{1, 2, 3, 4}}'
        choice_b = f'A={{1, 2}} , B={{2, 1}}*'
        choice_c = f'A={{1, 2, 3}} , B={{2, 3, 4}}'
        choice_d = f'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If set A X B=B X A then which of the following sets may satisfy"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_71:
    def __init__(self):
        choice_a = '6'
        choice_b = '3'
        choice_c = '12'
        choice_d = '8*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If a set contains 3 elements then the number of subsets is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_72:
    def __init__(self):
        choice_a = 'subset'
        choice_b = 'power set*'
        choice_c = 'union set'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""The set containing all the collection of subsets is known as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_73:
    def __init__(self):
        choice_a = '1*'
        choice_b = '2'
        choice_c = '0'
        choice_d = '4'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If a set is empty then number of subsets will be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_74:
    def __init__(self):
        choice_a = '1'
        choice_b = '2*'
        choice_c = '3'
        choice_d = '4'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f""" If the number of subsets of a set are 4 then the number of elements in that sets are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_77:
    def __init__(self):
        choice_a = '4'
        choice_b = '3*'
        choice_c = '5'
        choice_d = '8'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let a set be A={{1, 2, 3}} then the number of subsets containing two elements will be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_78:
    def __init__(self):
        choice_a = f'{{a, b}} Є A'
        choice_b = f'a Є A'
        choice_c = f'{{a}} Є A*'
        choice_d = f'b, c ЄA'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let the set be A= {{a , b, c, {{a,b}}}} then which of the following is false"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_79:
    def __init__(self):
        choice_a = '16'
        choice_b = '4*'
        choice_c = '8'
        choice_d = '24'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If A={{1, 2, 3, 4}} ,then the number of the subsets of A that contain the element 2 but not 3, is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class sanfoundry_80:
    def __init__(self):
        choice_a = '99'
        choice_b = '100'
        choice_c = '101*'
        choice_d = '102'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Let A(1), A(2), A(3),……..,A(100) be 100 sets such that number of elements in A(i)=i+1 and A(1) is subset of A(2), A(2)is subset of A(3),…..,A(99) is subset of A(100). The the number of elements in union of the all the sets are: n(A(1) U A(2) U A(3) …..U A(100)):"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class binomial_1:
    def __init__(self):
        print('binomial_1')
        b = de.Binomial()
        nth_term = random.randint(1,b.number_of_terms)
        self.question = f"""Find the {num2words(nth_term, to = 'ordinal')} term of the expansion of {b.expression}"""
        self.answer = f"""{b.nth_term(nth_term)}"""

class binomial_2:
    def __init__(self):
        print('binomial_2')
        regen = True
        while regen:
            b = de.Binomial(x_only = True)
            self.question = f"""Find the coefficient of x in the expansion of {b.expression}"""

            coefficient_of_x = b.expansion.coeff(x, 1)
            if coefficient_of_x > 0:
                regen = False

        self.answer = f"""Coefficient of x: {coefficient_of_x}"""

class binomial_3:
    def __init__(self):
        print('binomial_3')
        b = de.Binomial(x_only = True)
        power_of_x = random.randint(1,6)
        self.question = f"""Find the coefficient of x^{power_of_x} in the expansion of {b.expression}"""

        self.answer = f"""Coefficient of x^{power_of_x}: {b.expansion.coeff(x,power_of_x)}"""

class binomial_4:
    def __init__(self):
        print('binomial_4')
        regen = True
        while regen:
            b = de.Binomial(x_only = True)
            power_of_x = random.randint(1,6)
            self.question = f"""Find the coefficient of 1/(x^{power_of_x}) in the expansion of {b.expression}"""

            coe = b.expansion.coeff(x, -power_of_x)
            if coe > 0:
                regen = False

        self.answer = f"""Coefficient of 1/x^{power_of_x}: {coe}"""

class binomial_5:
    def __init__(self):

        choice_a = 'Pascal*'
        choice_b = 'Fermat'
        choice_c = 'Fibonacci'
        choice_d = 'Euler'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Who created the special triangle?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class binomial_6:
    def __init__(self):
        print('binomial_6')
        regen = True
        while regen:
            b = de.Binomial(x_only = True)

            x3_coefficient = b.expansion.coeff(x, 3)
            x4_coefficient = b.expansion.coeff(x, 4)
            ratio = sym.simplify(sym.Rational(x3_coefficient, x4_coefficient))

            if x4_coefficient > 0:
                regen = False

        self.question = f"""In the expansion of ({b.A} + {b.B})^N the ratio of the coefficients of x^3 and x^4 are {ratio}, Find the value of N."""

        self.answer = f"""Value of N: {b.N}"""

class binomial_7:
    def __init__(self):
        print('binomial_7')
        regen = True
        b = de.Binomial(x_only = True)
        c = de.Binomial(x_only = True)

        d = b.expression * c.expression
        e = d.expand()

        while regen:
            power_of_x = random.randint(2,20)
            coe = e.coeff(x, power_of_x)

            if coe > 0:
                regen = False

        self.question = f"""Find the term involving x^{power_of_x} in the expansion of {d}"""

        self.answer = f"""Term with x^{power_of_x}: {coe} x^{power_of_x}"""

class counting_1:
    def __init__(self):
        people = random.randint(10,50)
        handshakes = de.combination(people, 2)
        self.question = f"""There are {people} people in a group. If all shake hands with one another, how many handshakes are possible?"""
        self.answer = f"""Handshakes: {handshakes}"""

class counting_2:
    def __init__(self):
        word = de.Word()
        self.question = f"""In how many ways can we arrange the word {word.word} so that all the vowels come together?"""

        vowels = word.vowels()
        length = word.length()

        ways = math.factorial(vowels) * math.factorial(length - vowels + 1) / word.repetitions()

        self.answer = f"""Number of ways: {ways}"""

class counting_3:
    def __init__(self):
        teams = random.randint(5,20)
        self.question = f"""In Cricket League, in first round every team plays a match with every other team. {teams} teams participated in the Cricket League. How many matches were played in the first round?"""
        matches = de.combination(teams,2)
        self.answer = f"""Matches: {matches}"""

class counting_4:
    def __init__(self):
        choice_a = '41*'
        choice_b = '81'
        choice_c = '8! / 2!'
        choice_d = '3! / 2!'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""How many combinations are possible while selecting four letters from the word SMOKEJACK with the condition that J must appear in it?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class counting_5:
    def __init__(self):
        regen = True
        while regen:

            try:
                green = random.randint(2,10)
                yellow = random.randint(2,10)
                blue = random.randint(2,10)
                total = green + blue + yellow

                chairs = random.randint(3, total)
                self.question = f"""In a room there are {green} green chairs, {yellow} yellow chairs and {blue} blue chairs. In how many ways can Roy choose {chairs} chairs so that at least one yellow chair is included?"""

                total_ways = de.combination(total, chairs)
                no_yellow_chair = de.combination(blue + green, chairs)

                ways  = total_ways - no_yellow_chair

                self.answer = f"""Number of ways: {ways}"""
                regen = False
            except:
                pass

class counting_6:
    def __init__(self):
        circle_1 = random.randint(5,15)
        circle_2 = random.randint(5,15)
        total = circle_1 + circle_2

        self.question = f"""{total} students are present in class. In how many ways, can they be made to stand in two circles of {circle_1} and {circle_2} students?"""

        ways = de.combination(total, circle_1) * math.factorial(circle_1 - 1) * math.factorial(circle_2 - 1)

        self.answer = f"""Number of ways: {ways}"""

class counting_7:
    def __init__(self):
        total = random.randint(10, 30)
        self.question = f"""On a railway line there are {total} stops. A ticket is needed to travel between any 2 stops. How many different tickets would the government need to prepare to cater to all possibilities?"""
        ways = de.combination(total, 2)
        self.answer = f"""Number of ways: {ways}"""

class counting_8:
    def __init__(self):
        types = 3
        history = random.randint(2,10)
        science = random.randint(2,10)
        math_ = random.randint(2,10)

        ways = types * math.factorial(history) * math.factorial(science) * math.factorial(math_)

        self.question = f"""In Daya's bag there are {history} books of history, {science} books of science and {math_} books of math. In how many ways can Daya arrange the books so that all the books of the same subject are together?"""

        self.answer = f"""Number of ways: {ways}"""

class counting_9:
    def __init__(self):
        digits = random.randint(3,10)
        seconds_per_try = c.time(random.randint(4,8))

        self.question = f"""A locker in a bank has a {digits}-digit lock. Mary forgot her password and was trying all possible combinations. She took {seconds_per_try.s} seconds for each try. The problem was that each digit can be from 0 to 9. How much time will be needed by Mary to try all the combinations?"""

        ways = 10**digits
        total_time = c.time( seconds_per_try.s * ways)

        self.answer = f"""Time needed: {total_time.min} minutes"""

class counting_10:
    def __init__(self):
        travel_ways = random.randint(5,15)

        self.question = f"""John travels from Manila to Davao in {travel_ways} different ways. But he is allowed to return to Manila by any way except the one he used earlier. In how many ways can he complete his journey?"""

        ways = travel_ways * (travel_ways - 1)

        self.answer = f"""Number of ways: {ways}"""

class counting_11:
    def __init__(self):
        choice_a = '90*'
        choice_b = '70'
        choice_c = '147'
        choice_d = '60'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""Without repetition, using the digits 2, 3, 4, 5, 6, 8, and 0, how many numbers can be made which lie between 500 and 1000?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class counting_12:
    def __init__(self):
        girls = random.randint(2,10)
        boys = random.randint(2,10)
        teachers = random.randint(2,10)
        members = random.randint(4, min(teachers + boys, teachers + girls))
        #group 1
        teachers_choose_1 = random.randint(1, teachers)
        boys_choose_1 = random.randint(1, boys)

        #group 2
        teachers_choose_2 = random.randint(1, teachers)
        girls_choose_2 = random.randint(1, girls)

        ways1 = de.combination(teachers, teachers_choose_1) * de.combination(boys, boys_choose_1)
        ways2 = de.combination(teachers, teachers_choose_2) * de.combination(girls, girls_choose_2)

        ways = ways1 * ways2




        self.question = f"""A trekking group is to be formed having {members} members. They are to be selected from {girls} girls, {boys} boys and {teachers} teachers. In how many ways can the group be formed so that there are {teachers_choose_1} teachers and {boys_choose_1} boys or {girls_choose_2} girls and {teachers_choose_2} teachers?"""

        self.answer = f"""Number of ways: {ways}"""

class counting_13:
    def __init__(self):
        choice_a = '500'
        choice_b = '720'
        choice_c = '240*'
        choice_d = '360'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""If Anne doesn't want three vowels together, then in how many ways can she arrange letters of the word MARKER?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class counting_14:
    def __init__(self):
        digits = random.randint(5, 10)
        current = 8

        #6 digits, 4 iterations
        #7 digits, 5 iterations
        #n digits, n-2 iteration
        ways = 1
        for i in range(0, digits - 2):
            ways = ways * current
            current = current - 1


        self.question = f"""A bank has {digits}-digit account number with no repetition of digits within an account number. The first and last digits of the account numbers is fixed to be 4 and 7. How many such account numbers are possible?"""

        self.answer = f"""Number of ways: {ways}"""

class counting_15:
    def __init__(self):
        students = random.randint(10, 30)
        handshakes = de.combination(students, 2)
        self.question = f"""In a class, there are {students} students. During a Christmas party all of them shook hands with each other only once. How many handshakes took place in the class?"""

        self.answer = f"""Number of handshakes: {handshakes}"""

class counting_16:
    def __init__(self):
        girls = random.randint(10,20)
        boys = random.randint(10,20)
        senior = random.randint(5,10)
        babies = random.randint(5,10)
        people = girls + boys + senior + babies


        self.question = f"""There are {people} people in the group. There are {girls} school girls, {boys} school boys, {senior} senior citizens and {babies} babies in the group. The organizer of the group wants to select a school girl or a school boy as leader of the group. In how many ways can he do so?"""

        ways = girls + boys

        self.answer = f"""Number of ways to select a leader: {ways}"""

class counting_17:
    def __init__(self):
        routes_1 = random.randint(5,15)
        routes_2 = random.randint(5,15)
        self.question = f"""There are {routes_1} routes from London to Delhi. And there are {routes_2} from Delhi to Tokyo. In how many different ways can John travel from London to Tokyo via Delhi?""" 
        ways = routes_1 * routes_2

        self.answer = f"""Number of ways: {ways}"""

class counting_18:
    def __init__(self):
        regen = True
        while regen:
            try:
                members = random.randint(8, 20)
                members_choose = random.randint(1, members - 4)
                self.question = f"""{members_choose} member form a group out of total {members} members. 
        i) In how many ways it is possible to make the group if two particular members must be included?
        ii) In how many ways it is possible to make the group if two particular members must not be included?"""

                ways1 = de.combination(members - 2, members_choose - 2)
                ways2 = de.combination(members - 2, members_choose)

                self.answer = f"""Number of ways: {ways1} and {ways2}"""
                regen = False
            except:
                pass

class counting_19:
    def __init__(self):
        people = random.randint(10,50)

        self.question = f"""There are {people} people in a party. If everyone is to shake hands with one another, how many handshakes are possible?"""
        handshakes = de.combination(people, 2)
        self.answer = f"""Number of handshakes: {handshakes}"""

class counting_20:
    def __init__(self):

        white = random.randint(3,10)
        black = random.randint(3,10)
        red = random.randint(3,10)
        total = white + black + red
        choose = random.randint(2,white + red - 2)

        self.question = f"""A box contains {white} white, {black} black and {red} red balls. In how many ways can {choose} balls be drawn from the box if at least one black ball is to be included in the draw?"""

        #choose balls from all balls
        random_ways = de.combination(total, choose)

        #not black choose
        no_black = de.combination(red + white, choose)

        #at least one black
        ways = random_ways - no_black

        self.answer = f"""Number of ways: {ways}"""

class counting_21:
    def __init__(self):
        geology = random.randint(2, 6)
        sociology = random.randint(2, 6)
        economics = random.randint(2, 6)
        types = 3


        self.question = f"""On a shelf, {geology} books of Geology, {sociology} books of Sociology, and {economics} books of Economics are to be arranged in such a way that the books of any subject are to be together. Find how many ways can this be done?"""

        ways = math.factorial(types) * math.factorial(geology) * math.factorial(sociology) * math.factorial(economics)

        self.answer = f"""Number of ways: {ways} """

class counting_22:
    def __init__(self):

        digits = random.randint(3,9)
        time = c.time(random.randint(3,6))

        self.question = f"""A briefcase has a number-lock system containing a combination of {digits} digits (Each digit can be of numbers 0 to 8). If the correct combination is unknown, how much maximum time would be required to open the bag if each trial of combination takes {time.s} seconds?"""

        trials = 9**digits
        total_time = c.time(trials * time.s)

        self.answer = f"""Time required: {total_time.min} minutes"""

class counting_23:
    def __init__(self):
        routes = random.randint(5,15)

        self.question = f"""A person can go from place P to Q by {routes} different modes of transport,but is allowed to return back to P by any mode other than the one used earlier. In how many different ways can he complete the entire journey?"""

        ways = routes * (routes - 1)

        self.answer = f"""Number of ways: {ways} """

class counting_24:
    def __init__(self):
        word = de.Word()

        self.question = f"""How many words can be formed by using all the letters of the word {word.word}?"""

        ways = math.factorial(word.length()) / word.repetitions()

        self.answer = f"""Number of ways: {ways}"""

class counting_25:
    def __init__(self):
        regen = True
        while regen:
            try:
                word = de.Word()

                choose = random.randint(3, word.length())

                self.question = f"""How many {choose}-letter wordds can be formed out of the letters of the word {word.word}, if repetition is now allowed?"""

                ways = de.combination(word.unique_letters(), choose)

                self.answer = f"""Number of ways: {ways}"""
                regen = False
            except:
                pass

class counting_26:
    def __init__(self):
        word = de.Word()
        self.question = f"""In how many different ways can the letters of the word {word.word} be arranged so that the vowels always come together?"""

        ways = math.factorial(word.vowels()) * math.factorial(word.consonants() + 1)

        self.answer = f"""Number of ways: {ways}"""

class counting_27:
    def __init__(self):
        cows = random.randint(3, 10)
        buffalos = random.randint(3, 10)
        total = cows + buffalos
        choose = random.randint(2, buffalos - 1)


        self.question = f"""In a group containing {cows} cows and {buffalos} buffalos, {choose} livestock are to be selected in such a way that at least 1 cow should always be present. How many ways of doing that are possible?"""

        ways = de.combination(total, choose) - de.combination(buffalos, choose)
        #ways = choose_any - choose_no_cow = choose_at_least_1_cow

        self.answer = f"""Number of ways: {ways}"""

class counting_28:
    def __init__(self):
        choice_a = '453600*'
        choice_b = '128000'
        choice_c = '478200'
        choice_d = '635630'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        self.question = f"""In how many ways can the letters of the word ENCYCLOPAEDIA be arranged such that vowels only occupy the even positions?""" 
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class counting_29:
    def __init__(self):
        word = de.Word()
        self.question = f"""In how many ways can the letters of the word {word.word} be arranged, such that all the vowels are never together?"""

        total_ways = math.factorial(word.length())  / word.repetitions()

        ways_vowels_together = math.factorial(word.vowels()) * math.factorial( 1 + word.consonants()) / word.repetitions()

        ways = total_ways - ways_vowels_together

        self.answer=  f"""Number of ways: {ways}"""











 































































