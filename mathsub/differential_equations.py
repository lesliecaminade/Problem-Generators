from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import differential_equation_engine as engine
from mathsub import algebra_engine

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

class separable():
    def __init__(self):
        de = engine.Separable()
        de.init_random()

        self.question = f"""Solve the differential equation {de.de}"""
        self.answer = f"""{de.results}"""

class exact():
    def __init__(self):
        de = engine.Exact()
        de.init_random()

        self.question = f"""Solve the differential equation {de.de}"""
        self.answer = f"""{de.results}"""

class homogeneous():
    def __init__(self):
        de = engine.Homogeneous()
        de.init_random()

        self.question = f"""Solve the differential equation {de.de}"""
        self.answer = f"""{de.results}"""

class linear():
    def __init__(self):
        de = engine.Linear()
        de.init_random()

        self.question = f"""Solve the differential equation {de.de}"""
        self.answer = f"""{de.results}"""

























































































































 
















        
















 































































