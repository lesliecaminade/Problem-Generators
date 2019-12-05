import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
import algebra
import analytic_geometry

x, y = sym.symbols('x y', real = True)
alpha, beta = sym.symbols('a b', real = True)

f = sym.Function('f')(x)
f_ = sym.Function('f')

fd = sym.Derivative(f, x)
fdd = sym.Derivative(f, x, x)
fddd = sym.Derivative(f, x, x, x)


init_printing(use_unicode=False)


class rainville_separable:
    def __init__(self, *args, **kwargs):
        equation_list = (
        sym.Eq(fd, -ran.cpos(5) * f * x ), 
        sym.Eq(ran.cpos(5)*x*f*fd, ran.cpos(5) + f**2),
        sym.Eq(x*f*fd, ran.cpos(5) + f**2),
        sym.Eq(ran.cpos(5) * f , ran.cpos(5) * x * fd),
        sym.Eq(fd, x * sym.exp( f - x**2)),
        sym.Eq(x * f**2 + sym.exp(x) * fd, 0),
        sym.Eq((ran.cpos(5) - f**2) *fd , f**3 * sym.sin(x)),
        sym.Eq(f * fd , ran.cpos(5)),
        sym.Eq(  (ran.cpos(5) - x)  * fd , f**2),
        sym.Eq(  sym.sin(x) * sym.sin(f) + sym.cos(x) * sym.cos(f) * fd, 0),
        sym.Eq( x * f**3 +  sym.exp(x**2) * fd, 0 ), #10
        sym.Eq( ran.cpos(5) * f , ran.cpos(5) * x * fd    ),
        sym.Eq( fd, x * f**2  ),
        sym.Eq( fd, - f/x),
        sym.Eq( y * sym.exp(ran.cpos(5) * x) , (ran.cpos(5) + sym.exp(ran.cpos(5) * x ) ) * fd),
        sym.Eq( fd , ran.cpos(5) * ( sym.cos(x) * fd + f * sym.sin(x)    )  ),
        sym.Eq( x * f  - (x + ran.cpos(5)) * fd , 0),
        sym.Eq( x**2 + f * (x - ran.cpos(5)) * fd, 0),
        sym.Eq( x * f + x , (x**2 * f**2 + x**2 + f**2 + 1)*fd), ####!
        sym.Eq( x * sym.cos(f)**2 + sym.tan(f) * fd, 0), 
        sym.Eq( x * f**3 + (f + ran.cpos(5)) * sym.exp(-x) * fd , 0), 
        sym.Eq( (ran.cpos(5) - f) * fd , x**2 ) ,
        sym.Eq( x**2 * f * fd , sym.exp(f)),
        sym.Eq( sym.tan(f)**2 * f * fd , sym.sin(x)**3 ), #####!
        #sym.Eq( fd , sym.cos(x)**2 * sym.cos(f)),#####!
        sym.Eq( fd , f * sym.sec(x)),
        sym.Eq( fd , x * (ran.cpos(5) + x**2) * sym.sec(x)**2 ),
        #sym.Eq( )
        sym.Eq( ran.cpos(5) + sym.log(x) + (ran.cpos(5) + sym.log(f) ) * fd , 0),
        sym.Eq( x - sym.sqrt(ran.cpos(5) - x**2) * fd, 0),
        sym.Eq( x + sym.sqrt(ran.cpos(5) - x**2) * fd, 0),
        sym.Eq( ran.cpos(5) * x , x * sym.sqrt(x**2 - ran.cpos(5)) * fd), 
        sym.Eq( f * sym.log(x) * sym.log(f) + fd, 0)
        )
        
        temp = random.randint(0,len(equation_list)-1)
        print(f"""TEMP {temp}""")
        equation = equation_list[temp]
        
        equation_pretty = sym.pretty(equation)
        solution = sym.dsolve(equation, f)
        solution_pretty = sym.pretty(solution)
        
        self.question = f"""Find the solution to the differential equation 
{equation_pretty}"""
        
        self.answer = f"""{solution_pretty}"""
        
# class rainville_homogeneous:
    # def __init__(self,*args,**kwargs): 
        # equation_list = (
        
        # )
        
        # temp = random.randint(0,len(equation_list)-1)
        # print(f"""TEMP {temp}""")
        # equation = equation_list[temp]
        
        # equation_pretty = sym.pretty(equation)
        # solution = sym.dsolve(equation, f)
        # solution_pretty = sym.pretty(solution)
        
        # self.question = f"""Find the solution to the differential equation 
# {equation_pretty}"""
        
        # self.answer = f"""{solution_pretty}"""
        

class solde_homo:
    def __init__(self):
        a = ran.c(10)
        b = ran.c(10)
        c = ran.c(10)
        
        eq = a*fdd + b*fd + c*f
        eqp = sym.pretty(eq)
        try:
            solution = sym.dsolve(eq,f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'
        
        self.question = f"""Find the solution to the differential equation
{eqp} = 0."""
        self.answer = f"""{solutionp}"""
        self.lhs = eq
        self.rhs = 0
        
class solde_nonhomo_exp:
    def __init__ (self):
        lhs = solde_homo().lhs
        rhs = algebra.exponential().expression
        lhsp = sym.pretty(lhs)
        rhsp = sym.pretty(rhs)
        
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs), f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'
        
        self.question = f"""Find the solution to the differential equation
{lhsp} = ...
{rhsp}"""
        self.answer = f"""{solutionp}"""
        
class solde_nonhomo_trig_solo:
    def __init__ (self):
        lhs = solde_homo().lhs
        rhs = algebra.trigonometric(2).expression
        lhsp = sym.pretty(lhs)
        rhsp = sym.pretty(rhs)
        
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs), f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'
        
        self.question = f"""Find the solution to the differential equation
{lhsp} = ...
{rhsp}"""
        self.answer = f"""{solutionp}"""

class solde_nonhomo_trig_duo:
    def __init__ (self):
        lhs = solde_homo().lhs
        rhs = algebra.trigonometric_sin_cos_pair().expression
        lhsp = sym.pretty(lhs)
        rhsp = sym.pretty(rhs)
        
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs), f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'
        
        self.question = f"""Find the solution to the differential equation
{lhsp} = ...
{rhsp}"""
        self.answer = f"""{solutionp}"""
        
class solde_nonhomo_polynomial:
    def __init__ (self):
        lhs = solde_homo().lhs
        rhs = algebra.polynomial().expression
        lhsp = sym.pretty(lhs)
        rhsp = sym.pretty(rhs)
        
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs), f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'
        
        self.question = f"""Find the solution to the differential equation
{lhsp} = ...
{rhsp}"""
        self.answer = f"""{solutionp}"""

class solde_nonhomo_vop1:
    def __init__ (self):
        lhs = solde_homo().lhs
        rhs = (algebra.exponential().expression) / (ran.c(10)*x)
        lhsp = sym.pretty(lhs)
        rhsp = sym.pretty(rhs)
        
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs), f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'
        
        self.question = f"""Find the solution to the differential equation
{lhsp} = ...
{rhsp}"""
        self.answer = f"""{solutionp}"""
        
class sonlde_homo_euler_cauchy:
    def __init__(self):
        a = ran.c(10)
        b = ran.c(10)
        c = ran.c(10)
        lhs = a*x**2*fdd + b*x*fd + c*f
        rhs = 0
        lhsp = sym.pretty(lhs)
        rhsp = sym.pretty(rhs)
        
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs), f)
            solutionp = sym.pretty(solution)
        except:
            solution = 'error'
            solutionp = 'error'

        self.question = f"""Find the solution to the differential equation
{lhsp} = ...
{rhsp}"""
        self.answer = f"""{solutionp}"""
        
class RLC_circuits:
    def __init__(self):
        R = random.randint(100,500)
        C = sym.Rational(1,(random.randint(100,500)))
        L = random.randint(5,50)
        
        Epeak = ran.cpos(10)
        Iinit = random.randint(0,2)
        Qinit = random.randint(0,2)
        
        lhs = fdd + (R/L)*fd + (1/(L*C))*f
        rhs = Epeak*sym.sin(x)
        rhsp = sym.pretty(rhs)
        try:
            solution = sym.dsolve(sym.Eq(lhs,rhs),f,ics = {f_(0):Iinit, sym.diff(f_(x),x).subs(x,0): Qinit})
            solutionp = sym.pretty(solution)
            solution2 = sym.diff(solution.args[1],x)
            solution2p = sym.pretty(solution2)
        except:
            solution = 'error'
            solutionp = 'error'
            solution2 = 'error'
            solution2p = 'error'
            
        self.question = f"""An RLC circuit with R = {R} ohms, C = {C} F, and L = {L} H, and an applied voltage of ...
{rhsp}
Assume the initial charge is {Qinit} C and the initial current is {Iinit} A. Find the charge in the capacitor at any time t."""
        self.answer = f"""
-------I(t)----------------
{solutionp}
-------Q(t)---------------
{solution2p}"""
            
        
        
        
        