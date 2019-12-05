import random
import math

def choicesTemplate(input,units):
    correct_placement = random.randint(0,3)
    answers = []
    for i in range(0,4):
        answers.append(round(random.gauss(input,10*input),4))
    
    answers[correct_placement] = round(input,4)
    
    asterisk = ['','','','']
    asterisk[correct_placement] = '*'
    
    choice_template = """A. {a:g} {unit:s}{asta:s}         C. {c:g} {unit:s}{astc:s}
B. {b:g} {unit:s}{astb:s}           D. {d:g} {unit:s}{astd:s} """.format(
a = answers[0]
b = answers[1]
c = answers[2]
d = answers[3]
unit = units
asta = asterisk[0]
astb = asterisk[1]
astc = asterisk[2]
astd = asterisk[3]
    return choice_template
)
    