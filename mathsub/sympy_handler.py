#sympy handler
import sympy as sympy


#symbols for sympy
a, b, c, d, x, y, z = sympy.symbols('a b c d x y z', real = True)
n = sympy.symbols('n', real = True)

def solvex(input):
    try:
        result = sympy.solveset(input,x).args[0]
        output = N(result)
    except:
        output = - 999999999
