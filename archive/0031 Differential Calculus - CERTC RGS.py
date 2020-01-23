import randomizer
import random_handler as ran
import sympy_handler as symh
import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import oo
import math
import math_common
import random
import stringHandling
import differential_calculus as difcal
import differential_calculus_word_problem_templates as difprob
import algebra


x, y = sym.symbols('x y', real = True)
#n = s.symbols('n', real = True)

import constants_conversions as cc
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Differential Calculus - RGS CERTC
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com
note: log(x) refers to the natural logarithm"""



class genericClass:

    def __init__(self):
        question = ""
        answer = ""
        
        solution = ""
       
        form = random.randint(1,24) #check
        #form = 24
        
        if form == 1: 
            limit_obj = difcal.limits_rational_poly_poly()
            expression = limit_obj.expression
            expression = sym.pretty(expression)
            answer = limit_obj.limit
            answer = sym.pretty(answer)
            answer = f'{answer}'
            question = f"""Evaluate
{expression}"""

        if form == 2:
            limit_obj = difcal.limits_rational_poly_poly()
            expression = limit_obj.expression
            expression = sym.pretty(expression)
            answer = limit_obj.limit
            answer = sym.pretty(answer)
            answer = f'{answer}'
            question = f"""Evaluate
{expression}"""
            
        if form == 3:
            numerator_obj = algebra.trigonometric(3,True)
            numerator_expr = numerator_obj.expression
            denominator_obj = algebra.polynomial()
            denominator_expr = denominator_obj.expression
            limit_expr = sym.Limit(numerator_expr / denominator_expr, x, 0)
            expression = sym.pretty(limit_expr)
            answer = limit_expr.doit()
            answer = sym.pretty(answer)
            answer = f'{answer}'
            question = f"""Evaluate
{expression}"""

        if form == 4:
            deriv_obj = difcal.derivative_rational_poly_poly()
            deriv_expr = deriv_obj.expression
            deriv_expr = sym.pretty(deriv_expr)
            deriv_derivative = sym.pretty(deriv_obj.derivative)
            
            question = f"""Differentiate 
{deriv_expr}"""
            answer = f'{deriv_derivative}'
            
        if form == 5:
            deriv_obj = difcal.derivative_square_root_poly()
            deriv_expr = deriv_obj.expression
            deriv_expr = sym.pretty(deriv_expr)
            deriv_derivative = sym.pretty(deriv_obj.derivative)
            question = f"""Differentiate 
{deriv_expr}"""
            answer = f'{deriv_derivative}'
            
        if form == 6:
            poly_obj = algebra.polynomial_linear()
            poly_expr = poly_obj.expression
            sqr_expr = (poly_expr)**sym.Rational(1,2)
            deriv_expr = sym.Derivative(sqr_expr, x)
            deriv_expr_pretty = sym.pretty(deriv_expr)
            deriv_deriv = sym.pretty(deriv_expr.doit())
            question = f"""Differentiate
{deriv_expr_pretty}"""
            answer = f'{deriv_deriv}'
            
        if form == 7:
            poly_obj = algebra.polynomial_linear()
            poly_expr = poly_obj.expression
            exponential_expr = (ran.c(10))**(poly_expr)
            deriv_expr = sym.Derivative(exponential_expr, x)
            deriv_expr_pretty = sym.pretty(deriv_expr)
            deriv_deriv = deriv_expr.doit()
            deriv_deriv_pretty = sym.pretty(deriv_deriv)
            question = f"""Differentiate
{deriv_expr_pretty}"""
            answer = f'{deriv_deriv_pretty}'
            
        if form == 8:
            invtrig_obj = algebra.inverse_trigonometric(3,True)
            invtrig_expr = invtrig_obj.expression
            deriv_expr = sym.Derivative(invtrig_expr,x)
            deriv_expr_pretty = sym.pretty(deriv_expr)
            deriv_deriv = deriv_expr.doit()
            deriv_deriv_pretty = sym.pretty(deriv_deriv)
            
            question = f"""Differentiate
{deriv_expr_pretty}"""
            answer = f'{deriv_deriv_pretty}'
            
        if form == 9:
            invtrig_obj = algebra.inverse_trigonometric(3,True)
            invtrig_expr = invtrig_obj.expression
            exponential_expr = (invtrig_expr)**random.randint(2,3)
            deriv_expr = sym.Derivative(exponential_expr,x)
            deriv_expr_pretty = sym.pretty(deriv_expr)
            deriv_deriv = deriv_expr.doit()
            deriv_deriv_pretty = sym.pretty(deriv_deriv)
            
            question = f"""Differentiate
{deriv_expr_pretty}"""
            answer = f'{deriv_deriv_pretty}'
            
        if form == 10:
            invtrig_object = algebra.inverse_trigonometric(3, True)
            invtrig_expr = invtrig_object.expression
            exponential_expr = (invtrig_expr)**(random.randint(2,3))
            deriv_expr = sym.Derivative(exponential_expr,x)
            deriv_expr_pretty = sym.pretty(deriv_expr)
            deriv_deriv = deriv_expr.doit()
            deriv_deriv_pretty = sym.pretty(deriv_deriv)
            
            question = f"""Differentiate
{deriv_expr_pretty}"""
            answer = f'{deriv_deriv_pretty}'
            
        if form == 11:
            invtrig_object = algebra.inverse_trigonometric_hyperbolic(3,True)
            invtrig_expr = invtrig_object.expression
            deriv_expr = sym.Derivative(invtrig_expr,x)
            deriv_expr_pretty = sym.pretty(deriv_expr)
            deriv_deriv = deriv_expr.doit()
            deriv_deriv_pretty = sym.pretty(deriv_deriv)
            question = f"""Find the first derivative of 
{deriv_expr_pretty}"""
            answer = f'{deriv_deriv_pretty}'
            
        
        if form == 12:
            poly1_object = algebra.polynomial_linear()
            poly2_object = algebra.polynomial_cubic()
            poly1_expr = poly1_object.expression
            poly2_expr = poly2_object.expression
            gen_expr = (poly1_expr) * ((poly2_expr)**sym.Rational(1,2))
            gen_expr_pretty = sym.pretty(gen_expr)
            gen_deriv = sym.Derivative(gen_expr,domain = sym.Reals)
            gen_deriv_pretty = sym.pretty(gen_deriv)
            deriv_deriv = gen_deriv.doit()
            deriv_deriv_pretty = sym.pretty(deriv_deriv)
            val = ran.c(10)
            deriv_value = deriv_deriv.subs(x, val)
            question = f"""Differentiate 
{gen_expr_pretty}
at x = {val}"""
            answer = f'{deriv_value}'
            
        if form == 13:
            poly1_object = algebra.polynomial_quadratic()
            poly2_object = algebra.polynomial_quadratic()
            gen_expr = poly1_object.expression * poly2_object.expression
            gen_expr_deriv = sym.Derivative(gen_expr, x, x) 
            gen_expr_deriv_pretty = sym.pretty(gen_expr_deriv)
            deriv = gen_expr_deriv.doit()
            deriv_pretty = sym.pretty(deriv)
            question = f"""Find the second derivative of y with respect to x of the function y = ...
{gen_expr_deriv_pretty}"""
            answer = f'{deriv_pretty}'
        
        if form == 14:
            poly1_obj = algebra.polynomial_cubic_xy()
            poly1_expr = poly1_obj.expression
            given = sym.Derivative(poly1_expr,x)
            given_pretty = sym.pretty(given)
            deriv = given.doit()
            deriv_pretty = sym.pretty(deriv)
            question = f"""Find the partial derivative of...
{given_pretty}
with respect to x."""
            answer = f'{deriv_pretty}'
            
        if form == 15:
            poly_obj1 = algebra.polynomial_cubic()
            poly_expr1 = poly_obj1.expression
            given_pretty = sym.pretty(poly_expr1)
            deriv = sym.Derivative(poly_expr1,x)
            critical_points = sym.nroots(deriv.doit())
            critical_points_pretty = sym.pretty(critical_points)
            question = f"""Given the function y = ...
{given_pretty}
Determine the critical points"""
            answer = f'{critical_points_pretty}'
            
        if form == 16:
            prob_object = difprob.maxima_rectangle_inside_a_circle()
            question = prob_object.question
            answer = prob_object.answer
            
        if form == 17:
            prob_object = difprob.maxima_numbers_1()
            question = prob_object.question
            answer = prob_object.answer
            
        if form == 18:
            prob_object = difprob.minima_two_posts()
            question = prob_object.question
            answer = prob_object.answer
            
        if form == 19:
            prob_object = difprob.minima_rowboat()
            question = prob_object.question
            answer = prob_object.answer
        
        if form == 20:
            prob_object = difprob.related_rates_kite()
            question = prob_object.question
            answer = prob_object.answer
            
        if form == 21:
            prob_object = difprob.related_rates_conical_tank()
            question = prob_object.question
            answer = prob_object.answer
            
        if form == 22:
            prob_object = difprob.approx_error_sphere()
            question = prob_object.question
            answer = prob_object.answer

        if form == 23:
            prob_object = difprob.related_rates_speed_of_a_particle()
            question = prob_object.question
            answer = prob_object.answer        
        
        if form == 24:
            prob_object = difprob.radius_of_curvature()
            question = prob_object.question
            answer = prob_object.answer  
            
        self.question = question
        self.answer = answer
        self.solution = solution

print(title_string)
print()

 
for i in range (1,30):
    A = genericClass()
    #display(A.question)
    #display(A.answer)
    print('--------------------------------------------')
    print(A.question)
    print(' ')
    print(A.answer)
    print(' ')
    print(' ')
    if solutions_flag == True:
        print("""solution: {a:s}""".format(a=str(A.solution)))
    print()
    



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
