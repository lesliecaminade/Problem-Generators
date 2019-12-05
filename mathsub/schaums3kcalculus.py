from generator import random_handler as ran
import math
import random
from generator import constants_conversions as c
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

class grobs_1_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'coulomb'
        choice_b = 'electron'
        choice_c = 'proton'
        choice_d = 'neutron'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The most basic particle of negative charge is the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'electric charge'
        choice_b = 'potential difference'
        choice_c = 'current'
        choice_d = 'voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The coulomb is a unit"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'copper'
        choice_b = 'silver'
        choice_c = 'glass'
        choice_d = 'gold'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not a good conductor?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_4:
    def __init__(self, *args, **kwargs):
        choice_a = '+ 1'
        choice_b = '0'
        choice_c = '(+/-) 4'
        choice_d = '- 1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The electron valence of a neutral copper atom is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'volt'
        choice_b = 'ampere'
        choice_c = 'siemens'
        choice_d = 'coulomb'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The unit of potential difference is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'unlike charges repel each other'
        choice_b = 'like charges repel each other'
        choice_c = 'unlike charges attract each other'
        choice_d = 'like charges repel each other, unlike charges attract each other'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following statements is true?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'positive ions are the moving charges that provide current'
        choice_b = 'free electrons are the moving charges that provide current'
        choice_c = 'there are no free electrons'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In metal conductor, such as a copper wire,"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_8:
    def __init__(self, *args, **kwargs):
        choice_a = '0.01 S'
        choice_b = '0.1 S'
        choice_c = '0.001 S'
        choice_d = '1 S'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A 100-ohms resistor has a conductance, G, of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'coulomb'
        choice_b = 'electron'
        choice_c = 'proton'
        choice_d = 'neutron'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The most basic particle of positive charge is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'negative ion'
        choice_b = 'electrically charged atom'
        choice_c = 'positive ion'
        choice_d = 'electrically charged atom, positive ion'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the neutral atom loses one of its valence electrons, it becomes a(n)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'volt'
        choice_b = 'ampere'
        choice_c = 'coulomb'
        choice_d = 'siemens'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The unit of electric current is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_12:
    def __init__(self, *args, **kwargs):
        choice_a = '(+/-) 4'
        choice_b = '+ 1'
        choice_c = '- 7'
        choice_d = '0'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A semiconductor, such as silicon, has an electron valence of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'current can exist without voltage'
        choice_b = 'voltage can exist without current'
        choice_c = 'current can flow through an open circuit'
        choice_d = 'voltage can exist without current and current can flow through an open circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following statements is true?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'volt'
        choice_b = 'coulomb'
        choice_c = 'siemens'
        choice_d = 'ohm'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The unit of resistance is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_15:
    def __init__(self, *args, **kwargs):
        choice_a = '6'
        choice_b = '1'
        choice_c = '8'
        choice_d = '4'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Except for hydrogen (H) and helium (He) the goal of valence for an atom"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_16:
    def __init__(self, *args, **kwargs):
        choice_a = '1C/1s'
        choice_b = '1J/1C'
        choice_c = '6.25 e18 electrons'
        choice_d = '0.16 e-18 C/s'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One ampere of current corresponds to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'the motion of negative charges in the opposite direction of electron flow'
        choice_b = 'the motion of positive charges in the same direction as electron flow'
        choice_c = 'the motion of positive charges in the position of electron flow'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Conventional current is considered"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'make sure that the resistor is in a circuit where voltage is present'
        choice_b = 'make sure there is no voltage present across the resistor'
        choice_c = 'make sure there is no other component connected across the leads of the resistor'
        choice_d = 'both b and c'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)

        self.question = f"""When using a DMM to measure the value of a resistor"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'conductance'
        choice_b = 'resistance'
        choice_c = 'voltage'
        choice_d = 'current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a circuit, the opposition to the flow of current is called"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_20:
    def __init__(self, *args, **kwargs):
        choice_a = '13 valence electrons'
        choice_b = '3 valence electrons'
        choice_c = '13 protons in its nucleus'
        choice_d = 'both b and c'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)

        self.question = f"""Aluminum, with an atomic number of 13, has"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_21:
    def __init__(self, *args, **kwargs):
        choice_a = 'electrons and neutrons'
        choice_b = 'ions'
        choice_c = 'neutrons and protons'
        choice_d = 'electrons only'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The nucleus of an atom is made up of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_22:
    def __init__(self, *args, **kwargs):
        choice_a = '16 C'
        choice_b = '20 C'
        choice_c = '1.25 C'
        choice_d = '0.8 C'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How much charge is accumulated in a dielectric that is charged by a 4A current for 5 seconds"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_23:
    def __init__(self, *args, **kwargs):
        choice_a = '24 A'
        choice_b = '2.4 A'
        choice_c = '1.5 A'
        choice_d = '12 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A charge of 6 C moves past a given point every 0.25 second. How much is the current flow in amperes?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_24:
    def __init__(self, *args, **kwargs):
        choice_a = '18 V'
        choice_b = '6 V'
        choice_c = '125 mV'
        choice_d = '8 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is output voltage of a battery that expands 12 J of energy in moving 1.5 C of charge?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_25:
    def __init__(self, *args, **kwargs):
        choice_a = ''
        choice_b = ''
        choice_c = ''
        choice_d = ''

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""