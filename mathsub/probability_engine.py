from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import discrete_math_engine as de
from num2words import num2words

x, y, z = sym.symbols('x y z', real = True)#generic variables

def binomial_probability(n, r, p, q):
    return de.combination(n, r) * p**(r) * q**(n-r)

def multinomial_probability(trials, instances, probabilities):
        reps = 1
        trials = 0
        for i in instances:
            reps = reps * math.factorial(i)
            trials = trials + i
        
        right = 1
        for i in range(len(probabilities)):
            right = right * probabilities[i]**instances[i]

        probability = (math.factorial(trials)/reps) * right

        return probability

class Container():
    def __init__(self, descriptions, instances, distinguishable = False):


class Coins():
    def __init__(self):
        self.p_heads = 1/2
        self.p_tails = 1/2

    def probability_exactly(heads, tails):
        return p_heads**heads * p_tails**tails

    def probability_in_any_order(heads, tails):
        return binomial_probability(heads + tails, heads, self.p_heads, self.p_tails)

class Dice():
    def __init__(self):
        self.p_one = 1/6
        self.p_two = 1/6
        self.p_three = 1/6
        self.p_four = 1/6
        self.p_five = 1/6
        self.p_six = 1/6

    def sum_of_ways(self, sum_):
        if sum_ == 2 or sum_ == 12:
            return 1
        elif sum_ == 3 or sum_ == 11:
            return 2
        elif sum_ == 4 or sum_ == 10:
            return 3
        elif sum_ == 5 or sum_ == 9:
            return 4
        elif sum_ == 6 or sum_ == 8:
            return 5
        elif sum_ == 7:
            return 6
        else:
            print('sum_of() argument out of range')









class Cards():
    def __init__(self):
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.ranks = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
        self.total = 52
        self.clubs = 13
        self.hearts = 13
        self.spades = 13
        self.diamonds = 13
        self.ace = 4
        self.two = 4
        self.three = 4
        self.four = 4
        self.five = 4
        self.six = 4
        self.seven = 4
        self.eight = 4
        self.nine = 4
        self.ten = 4
        self.jack = 4
        self.queen = 4
        self.king = 4

    def random_suit():
        return random.choice(self.suits)

    def random_rank():
        return random.choice(self.ranks)

    def draw(rank = None, suit = None):
        if rank == 'ace':
            self.ace = self.ace - 1 
        elif rank == 'two':
            self.two = self.two - 1
        elif rank == 'three':
            self.three = self.three - 1
        elif rank == 'four':
            self.four = self.four - 1
        elif rank == 'five':
            self.five = self.five - 1
        elif rank == 'six'
            self.six = self.six - 1
        elif rank == 'seven':
            self.seven = self.seven - 1
        elif rank == 'eight':
            self.eight = self.eight - 1
        elif rank == 'nine':
            self.nine = self.nine - 1
        elif rank == 'ten':
            self.ten = self.ten - 1
        elif rank == 'jack':
            self.jack = self.jack - 1
        elif rank == 'queen':
            self.queen = self.queen - 1
        elif rank == 'king':
            self.king = self.king - 1
        else:
            print('no rank indicated.')

        if suit == 'spades':
            self.spades = self.spades - 1
        elif suit == 'clubs':
            self.clubs = self.clubs - 1
        elif suit == 'hearts':
            self.hearts = self.hearts - 1
        elif suit == 'diamonds':
            self.diamonds = self.diamonds - 1
        else:
            print('no suit selected')

        self.total = self.total - 1

    def query(rank = None, suit = None):
        if rank == 'ace':
            return self.ace
        elif rank == 'two':
            return self.two
        elif rank == 'three':
            return self.three
        elif rank == 'four':
            return self.four
        elif rank == 'five':
            return self.five
        elif rank == 'six'
            return self.six
        elif rank == 'seven':
            return self.seven
        elif rank == 'eight':
            return self.eight
        elif rank == 'nine':
            return self.nine
        elif rank == 'ten':
            return self.ten
        elif rank == 'jack':
            return self.jack
        elif rank == 'queen':
            return self.queen
        elif rank == 'king':
            return self.king
        else:
            pass

        if suit == 'spades':
            return self.spades
        elif suit == 'clubs':
            return self.clubs
        elif suit == 'hearts':
            return self.hearts
        elif suit == 'diamonds':
            return self.diamonds
        else:
            pass

        if suit == None and rank == None:
            return self.total
            


        






            
            
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        