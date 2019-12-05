import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
#import algebra
#import analytic_geometry
#import constants_conversions as c

x, y, z = sym.symbols('x y z', real = True)
a, b, c, d, e, f = sym.symbols('a b c d e f')

class Gate:
    def __init__(self,*args,**kwargs): 
        
        operators = ['AND', 'OR', 'NAND', 'NOR', 'XOR']
        operation = random.choice(operators)
        operator_dict = {'AND':sym.And, 
                            'OR':sym.Or,
                            'NAND':sym.Nand,
                            'NOR':sym.Nor,
                            'XOR':sym.Xor}
        
        
        self.gate = operation
        
    def doit(self, *args, **kwargs):
        self.output  = operator_dict[self.gate](args[0], args[1])
        return self.output
        
        
class mano_4_1:
    def __init__(self,*args,**kwargs): 
        
        gate1 = Gate()
        gate2 = Gate()
        gate3 = Gate()
        gate4 = Gate()
        gate5 = Gate()
        gate6 = Gate()
        

        self.question = f"""Considering the combinational circuit ... gate 1 is {gate1.gate}, gate 2 is {gate2.gate}, gate 3 is {gate3.gate}, gate 4 is {gate4.gate} and gate 5 is {gate5.gate}."""
        
        
        t1 = gate1(c, ~b)
        t2 = gate2(~a, d)
        t3 = gate3(t1, a)
        t4 = gate4(t2, d)
        f2 = gate5(~d, t2)
        f1 = gate6(t3, t4)
        
        f1_simplified = sym.simplify_logic(f1)
        f2_simplified = sym.simplify_logic(f2)
        
        self.answer = f"""F1 simplified = {f1_simplified}
F2 simplified = {f2_simplified}"""
        
        
        
        


        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        