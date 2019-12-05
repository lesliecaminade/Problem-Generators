from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import algebra_engine as ae
import num2words

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

SET_MAX = 50
SET_MIN = 0
            
def combination(n, r):
    combinations = math.factorial(n) / ( math.factorial(n - r) * math.factorial(r))
    return int(combinations)

def permutation(n, r):
    permutations = math.factorial(n) / math.factorial(n - r)
    return int(permutations)

def random_size():
    return random.randint(SET_MIN, SET_MAX)

class Word:
    def __init__(self, word = False):
        if word == False:
            wordlist = ('FUZZTONE', 'ENGINEERING', 'TOMORROW', 'COMMITTEE', 'SMOKEJACK', 'ALIVE', 'CORPORATION', 'GEOMETRY', 'PHILIPPINES')
            self.word = random.choice(wordlist).upper()
        else:
            self.word = word.upper()
        print(self.word)
    
    def length(self):
        return len(self.word)

    def vowels(self):
        vowels = 0
        for i in self.word:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels=vowels+1
        return vowels

    def consonants(self):
        consonants = 0
        for i in self.word:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                pass
            else:
                consonants = consonants + 1
        return consonants

    def repetitions(self):
        divisor = 1

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in alphabet:
            count = self.word.count(i)
            divisor = divisor * math.factorial(count)

        return divisor

    def unique_letters(self):
        uniques = len(set(self.word))
        return uniques

class Binomial:
    def __init__(self):
        pass

    def init_random(self, x_only = False):

        if x_only:
            self.A = ae.random_coeff() * x**ae.random_power()
            self.B = ae.random_coeff() * x**-ae.random_power()

            self.N = random.randint(3,10)


        else:
            self.A = ae.random_coeff() * x**ae.random_power()
            self.B = ae.random_coeff() * y**ae.random_power()

            self.N = random.randint(3,10)

    def init_define(self, A, B, N):
        self.A = A
        self.B = B
        self.N = N

    def compressed(self):
        return (self.A + self.B)**self.N

    def expand(self):
        return sym.expand((self.A + self.B)**self.N)

    def nth_term(self, term):
        if term > self.N + 1:
            print('ERROR: term out of range')
            return None
        expression = combination(self.N, term - 1) * self.A**(self.N - term + 1) * self.B**(term - 1)
        return expression

    def term_involving(self, n):
        expansion = sym.expand((self.A + self.B)**self.N)
        expansion = sym.Poly(expansion)
        terms = expansion.all_terms()
        print(terms)
        return None


    def nth_coefficient(self, term):
        if term > self.N + 1:
            print('ERROR: term out of range')
            return None
        expression = combination(self.N, term - 1) * self.A**(self.N - term + 1) * self.B**(term - 1)
        coefficient = sym.Poly(expression).coeffs()
        return coefficient[0]

    def sum_of_the_coefficients(self):
        expansion = sym.expand((self.A + self.B)**self.N)
        expansion = expansion.subs(x, 1)
        expansion = expansion.subs(y, 1)
        return expansion

    def term_independent_of_x(self):
        if self.x_only == False:
            print('ERROR: binomial not purely of x variable')
            return None
        else:
            term_independent_of_x = self.expansion.coeff(x, 0)

        return term_independent_of_x


class VennDiagrams:
    def __init__(self):
        pass

    def init_random(self, sets, outside = False):
        if sets == 2:
            self.Aonly = random_size()
            self.AIB = random_size()
            self.Bonly = random_size()

            self.A = self.Aonly + self.AIB
            self.B = self.Bonly + self.AIB

            if outside:
                self.outside = random_size()
                self.universe = self.Aonly + self.Bonly + self.AIB + self.outside
            else:
                self.universe = self.Aonlt + self.Bonly + self.AIB

        if sets == 3:
            self.Aonly = random_size()
            self.AIBonly = random_size()
            self.Bonly = random_size()
            self.BIConly = random_size()
            self.Conly = random_size()
            self.AIConly = random_size()
            self.AIBIC = random_size()

            self.A = self.Aonly + self.AIBonly + self.AIConly + self.AIBIC
            self.B = self.Bonly + self.AIBonly + self.BIConly + self.AIBIC
            self.C = self.Conly + self.AIConly + self.BIConly + self.AIBIC

            if outside:
                self.outside = random_size()
                self.universe = self.Aonly + self.AIBonly + self.Bonly + self.BIConly + self.Conly + self.AIConly + self.AIBIC + self.outside

            else:
                self.universe = self.Aonly + self.AIBonly + self.Bonly + self.BIConly + self.Conly + self.AIConly + self.AIBIC

class ArithmeticSeries:
    def __init__(self):
        pass

    def init_random(self):
        self.a1 = ae.random_coeff()
        self.d = ae.random_coeff()

    def init_define(self, a1, d):
        self.a1 = a1
        self.d = d

    def nth_term(self, n):
        return self.a1 + (n - 1) * self.d

    def sum_of_n_terms(self, n):
        return (n/2) * (2 * self.a1 + (n - 1)*self.d)

    def terms(self, n):
        terms = []
        for i in range(1, n + 1):
            term = self.a1 + (i - 1) * self.d
            terms.append(term)

        return terms

class GeometricSeries:
    def __init__(self):
        pass

    def init_random(self):
        self.a1 = ae.random_coeff()
        self.r = ae.random_coeff()

    def init_define(self, a1, r):
        self.a1 = a1
        self.r = r

    def nth_term(self, n):
        return self.a1 * self.r**(n - 1)

    def sum_of_n_terms(self, n):
        if r >= 1:
            return self.a1 * ((self.r**n - 1)/(self.r - 1))

        elif 0 > r > 1:
            return self.a1 * ((1 - self.r**n)/(1 - self.r))

        else:
            print('error')

    def terms(self, n):
        terms = []
        for i in range(1, n + 1):
            term = self.a1 * self.r**(n - 1)
            terms.append(term)

        return terms













































