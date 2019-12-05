import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
import algebra
import analytic_geometry
import constants_conversions_chemistry as c
#import randomizer_2 as ran2

x, y, z = sym.symbols('x y z', real = True)#generic variables

class schaums_2_1:
    def __init__(self,*args,**kwargs): 
        
        
        self.question = f"""It has been found by mass spectrometric analysis that in nature the relative abundances of the various isotopic atoms of silicon are 92.23% 28Si, 4.67% 29Si, and 3.10% 30Si. Calculate the atomic mass of silicon from this information and from the nuclidic masses."""

        self.answer = f"""Atomic mass of silicon = 28.085 amu"""
        
class schaums_2_2:
    def __init__(self,*args,**kwargs): 
        
        
        self.question = f"""Naturally occurring carbon consists of two isotopes, 12C and 13C. What are the percentage abundances of the two isotopes in a sample of carbon whose atomic mass is 12.01112 amu?"""
        
        self.answer = f"""Percent 12C = 98.892 %
Percent 13C = 1.108 %"""

class schaums_2_3:
    def __init__(self,*args,**kwargs): 
        
        mcdcl = c.mass(ran.main(1.5276))
        mcd = c.mass(m_cdcl.g * (0.9367/1.5276))
        Mcl = c.molarMass(35.453)
        
        self.question = f"""A {mcdcl.g} g sample of Cd C1_2 was converted to metallic cadmium and cadmium-free products by an electrolytic process. The weight of the metallic cadmium was {m_cd.g} g. If the atomic mass of chlorine is taken as {Mcl.amu}, what must be the atomic mass of Cd from this experiment?"""
        
        mcl = c.mass( mcdcl.g - mcd.g )
        ncl = c.moles( mcl.g * Mcl.amu )
        ncd = c.moles( 0.5 * ncl.mol )
        Mcd = c.molarMass( mcd.g / ncd.mol )
        
        self.answer = f"""Atomic mass of Cd = {Mcd.gpermol} g/mol"""
        
class schaums_2_5:
    def __init__(self,*args,**kwargs): 
        
        self.question = f"""In a chemical determination
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        