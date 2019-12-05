from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import discrete_math_engine as de
from num2words import num2words
from mathsub import probability_engine as pe

x, y, z = sym.symbols('x y z', real = True)#generic variables


class probability_1:
    def __init__(self):
        girls = random.randint(3,8)
        boys = random.randint(2,8)
        children = boys + girls

        self.question = f"""What are the chances that no {boys} boys are sittings together for photograph if there are {girls} girls and boys {boys}?"""

        total_ways = math.factorial(children)
        boys_together_ways = math.factorial(boys) * math.factorial(girls + 1)
        no_boys_together_ways = total_ways - boys_together_ways

        probability = no_boys_together_ways/total_ways
        probability = round(probability, 4)

class probability_2:
    def __init__(self):
        cards = pe.Cards()
        suit = cards.random_suit()
        draws = random.randint(1, 4)
        self.question = f"""What is the probability of drawing {draws} {suit} from a well shuffled pack of {cards.total} cards?"""

        first_draw_probability = cards.query(suit = suit) / cards.query()
        cards.draw(suit = suit)
        second_draw_probability = cards.query(suit = suit) / cards.query()

        probability = first_draw_probability * second_draw_probability

        self.answer = f"""Probability: {probability}"""

class probability_3:
    def __init__(self):
        trials = random.randint(2, 9)
        coins = pe.Coins()

        self.question = f"""When {trials} coins are tossed simutaneously, what are the chances of getting at least one tail?"""

        probability_no_tail = coins.probability_in_any_order(trials, 0)
        probability = 1 - probability_no_tail

        self.answer = f"""Probability: {probability}"""

class probability_4:
    def __init__(self):
        white = random.randint(2,8)
        gray = random.randint(2,8)
        blue = random.randint(2,8)
        total = white + gray + blue
        draw = random.randint(2,min(white, gray, blue))


        self.question = f"""In a drawer there are {white} white socks, {blue} blue socks and {gray} gray socks. {num2words(draw)} socks are picked randomly. What is the possibility that all the socks are of the same color?"""

        probabilities = [white/total, gray/total, blue/total]
        p_white = pe.multinomial([trials, 0, 0], probabilities)
        p_gray = pe.multinomial([0, trials, 0], probabilities)
        p_blue = pe.multinomial([0, 0, trials], probabilities)
        probability = p_white + p_gray + p_blue

        self.answer = f"""Probability: {probability}"""

class probability_5:
    def __init__(self):
        black = random.randint(2, 9)
        green = random.randint(2, 9)
        total = black + green
        probability = pe.binomial(trials, trials, black/total, green/total)

        self.question = f"""In a drawer there are {black} black socks and {green} green socks. {trials} socks are picked randomly one after the other without replacement. What is the possibility that all the socks are black?"""

        self.answer = f"""Probability: {probability}"""

class probability_6:
    def __init__(self):
        leap = random.choice([True, False])
        number_of_days = random.choice([52,53])
        day = random.choice(['Sundays', 'Mondays', 'Tuesdays', 'Wednesdays', 'Thursdays', 'Fridays', 'Saturdays'])

        self.question = f"""What is the possibility of having {number_of_days} {day} in a {leap_status} year?"""

        if leap_status:
            probability = 2/7
        else:
            probability = 1/7

        self.answer = f"""Probability: {probability}"""

class probability_7:
    def __init__(self):
        black = random.randint(2,9)
        green = random.ranint(2,9)
        total = black + green

        black2 = random.ranint(2,9)
        green2 = random.randint(2,9)
        total2 = black2 + green2

        #case1
        probability_1 = (black / total)*((black2 + 1)/(total2 + 1))

        #case2
        probability_2 = (green / total)*((black2)/(total2 + 1))

        probability = probability_1 + probability_2

        self.question = f"""A box has {black} black and {green} green shirts. One shirt is picked randomly and put in another box. The second box has {black2} black and {green2} green shirts. Now a shirt is picked from second box. What is the probability of it being a black shirt?"""

        self.answer = f"""Probability: {probability}"""

class probability_8:
    def __init__(self):
        self.question = f"""On rolling a dice two times, the sum of the two numbers that appear on the uppermost face is {sum_of_dice}. What is the probability that the first throw of dice yields



















            
            
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        