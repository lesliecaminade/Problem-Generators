import sympy
import math
import random
from mathsub import discrete_math_engine as engine
from num2words import num2words

def ask():
    ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
    return random.choice(ask_words)

def parse(string_input):
    string_input = str(string_input)
    return string_input.replace('**', '^').replace('*', ' ')    

class Binomial_expansion():
    def __init__(self):
        BATTERIES = []
        CHOICES = []
        suffix = ''
        prefix = ''
        for i in range(4):
            #battery = engine.Some_class_from_engine
            battery = engine.Binomial_expansion()
            #data = battery.Some_attribute_from_battery         
            data =  parse(battery.expanded)
            BATTERIES.append(battery)
            CHOICES.append(prefix + str(data) + suffix) 
        main = BATTERIES[0]
        CHOICES[0] = str(CHOICES[0]) + ' #'
        random.shuffle(CHOICES)
        #edit below
        self.question = f"""{ask()} the binomial series expansion of {parse(main.factored)}."""

        self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Binomial_expansion_nth_term():
    def __init__(self):
        BATTERIES = []
        CHOICES = []
        suffix = ''
        prefix = ''
        for i in range(4):
            #battery = engine.Some_class_from_engine
            battery = engine.Binomial_expansion()
            #data = battery.Some_attribute_from_battery         
            data =  parse(battery.nth_term()[0])
            BATTERIES.append(battery)
            CHOICES.append(prefix + str(data) + suffix) 
        main = BATTERIES[0]
        CHOICES[0] = str(CHOICES[0]) + ' #'
        random.shuffle(CHOICES)
        #edit below
        self.question = f"""{ask()} the {num2words(main.nth_term()[1], to = 'ordinal')} term of the binomial series expansion of {parse(main.factored)}."""

        self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""     















 































































