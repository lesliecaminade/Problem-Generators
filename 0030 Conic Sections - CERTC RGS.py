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
import analytic_geometry as analytic_geometry

x, y = sym.symbols('x y', real = True)
#n = sym.symbols('n', real = True)

import constants_conversions as cc
from constants_conversions import *
from common_names import *

solutions_flag = False
init_printing(use_unicode = False)
title_string = """Conic Sections - RGS CERTC
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""



class genericClass:

    def __init__(self):
        x, y = sym.symbols('x y', real = True)
        question = ""
        soln = ""
        
        solution = ""
       
        form = random.randint(1,25) #check
        #form = 25
        
        if form == 1: #identifying a general formula
            
            conic_number = random.randint(0,3)
            
            if conic_number == 0:
                expr = (x - ran.c(10))**2 + (y - ran.c(10))**2 - ran.cpos(10)**2
                expr2 = sym.expand(expr)
                expr2_str = str(expr2)
                soln = '(circle)  / parabola  / hyperbola /  ellipse'
            
            if conic_number == 1:
                orient = random.randint(0,1)
                if orient == 0:
                    expr = (x - ran.c(10))**2 - ran.c(10)*(y - ran.c(10))
                if orient == 1:
                    expr = (y - ran.c(10))**2 - ran.c(10)*(x - ran.c(10))
                expr2 = sym.expand(expr)
                expr2_str = str(expr2)
                soln = 'circle  / (parabola)  / hyperbola /  ellipse'
            
            if conic_number == 2:
                ma = ran.c(10)
                mb = ran.c(10)
                mab = ma*mb
                expr = (((x - ran.c(10))**2)/ma + ((y - ran.c(10))**2)/mb - 1)*mab
                expr2 = sym.expand(expr)
                expr2_str = str(expr2)
                soln = 'circle  / parabola  / hyperbola /  (ellipse)'

            if conic_number == 3:
                ma = ran.c(10)
                mb = ran.c(10)
                mab = ma*mb
                expr = (((x - ran.c(10))**2)/ma - ((y - ran.c(10))**2)/mb - 1)*mab
                expr2 = sym.expand(expr)
                expr2_str = str(expr2)
                soln = 'circle  / parabola  / (hyperbola) /  ellipse'
                
                
            question = f"""What conic section is represented by the equation {expr2_str} = 0?"""
            
        if form == 2: #circumference of a circle
            radius = ran.cpos(10)
            circumference = 2 * math.pi * radius
            expr = (x - ran.c(10))**2 + (y - ran.c(10))**2 - radius**2
            expr2 = sym.expand(expr)
            expr2_str = str(expr2)
            soln = f'{circumference}'
            
            question = f"""Determine the circumference of a circle whose equation is {expr2_str} = 0"""
                
        
        if form == 3: #equation of a circle given 3 points
            x1,y1 = ran.point(10)
            x2,y2 = ran.point(10)
            x3,y3 = ran.point(10)
            
            D,E,F = num.sysLin3(x1,y1,1,-(x1**2 + y1**2), x2,y2,1,-(x2**2 + y2**2), x3,y3,1,-(x3**2 + y3**2),)
            
            expr = x**2 + y**2 + D*x + E*y + F 
            expr = sym.expand(expr)
            expr_str = str(expr)
            
            soln = f'{expr_str} = 0'
            question = f"""Find the equation of the circle circumscribing a triangle whose vertices are at ({x1},{y1}), ({x2},{y2}), ({x3},{y3})."""
            
        if form == 4:
            retry = True
            while retry == True:
                D = ran.c(10)
                E = ran.c(10)
                F = ran.c(10)
                if (-F + (D**2)/4 + (E**2)/4) >= 0:
                    radius = math.sqrt(-F + (D**2)/4 + (E**2)/4 )
                    retry = False
                else:
                    retry = True

                    
            expr = x**2 + y**2 + D*x + E*y + F
            expr_show = x**2 + y**2 + D*x + E*y
            expr_show_str = str(expr_show)
            expr_str = str(expr)
            soln = f'k = {F}'
            
            question = f"""Determine the value of k so that {expr_show_str} + k = 0  is the equation of a circle with radius {radius}."""
        
        if form == 5:
            radius = 1
            distance = 0
            while radius >= distance:
                x1, y1 = ran.point(10)
                radius = ran.r(10)
                h, k = ran.point(10)
                distance = math.sqrt((x1 - h)**2 + (y1 - k)**2)
            
            expr = sym.expand((x - h)**2  + (y - k)**2 - radius**2)
            expr = str(expr)
            short_distance = distance - radius
            soln = f'{short_distance} units'
            question = f"""Find the shortest distance from A({x1},{y1}) to the circle {expr}  = 0."""
            
        if form == 6:
            orientation = random.randint(0,3)
            h,k = ran.point(10)
            focal_distance = ran.cpos(10)
            if orientation == 0: #right
                xf = h + focal_distance
                yf = k
            if orientation == 1: #left
                xf = h - focal_distance
                yf = k
            if orientation == 2: #up
                xf = h
                yf = k + focal_distance
            if orientation == 3: #down
                xf = h
                yf = k + focal_distance
                
            if orientation == 0 or orientation == 1:
                expr = (y - k)**2 - 4*focal_distance*(x - h)
            if orientation == 2 or orientation == 3:
                expr = (x - h)**2 - 4*focal_distance*(y - k)
                
            expr = sym.expand(expr)
            soln = f'{expr} = 0'
            question = f"""Find the equation of the parabola with vertex at ({h},{k}) and focus at ({xf},{yf})"""
            
        if form == 7:
            parabola_1 = analytic_geometry.parabola_general()
            focal_length = parabola_1.focal_length
            latus_rectum = parabola_1.latus_rectum
            expr = parabola_1.general
            
            soln = f'{focal_length}, {latus_rectum}'
            question = f"""Compute the focal length and the length of the latus rectum of parabola {expr} = 0"""
            
        if form == 8:
            ellipse_1 = analytic_geometry.ellipse_general()
            expr = ellipse_1.general
            ecc = ellipse_1.e
            area = math.pi * ellipse_1.a * ellipse_1.b
            question = f"""Given the equation {expr} = 0. a) Determine the eccentricity of the curve. b) Find the area enclosed by the curve."""
            soln = f'{ecc}, {area}'
            
        if form == 9:
            major_axis = 186000000
            eccentricity = random.uniform(0.15, 0.2)
            a = major_axis /2
            e = eccentricity
            c = e* a
            max_distance = c + a
            soln = f'{max_distance} miles'
            
            question = f"""The major axis of the elliptical path in which the satellite moves around the earth is approximately {major_axis} miles and the eccentricity of the ellipse is {eccentricity}. Find the maximum altitude of the satellite."""
            
        if form == 10:
            
            ellipse1 = analytic_geometry.ellipse_standard()
            while ellipse1.orientation == 1:
                ellipse1 = analytic_geometry.ellipse_standard()
            
            h, k = ellipse1.center
            eccentricity = ellipse1.e
            vertex_to_vertex_distance = ellipse1.a * 2
            general = ellipse1.general
            vx1, vy1, vx2, vy2 = ellipse1.vertices
            #pick a random point in x
            x1 = random.randint(vx1, vx2)
            general_for_y1 = general.subs(x, x1)
            y1 = sym.solveset(general_for_y1, y, domain = sym.Reals).args[0]
            
            
            dist1 = analytic_geometry.distancePointPoint(vx1,vy1,x1,y1)
            dist2 = analytic_geometry.distancePointPoint(vx2,vy2,x1,y1)
            dist = max(dist1, dist2)
            soln = f'{dist}'
            question = f"""An ellipse has its center at ({h}, {k}) with its axis horizontal. The distance between the vertices is {vertex_to_vertex_distance} and its eccentricity is {eccentricity}. Compute the length of the longest focal radius from point ({x1}, {y1}) on the curve."""
            
        if form == 11:
            hyperbola = analytic_geometry.hyperbola_general()
            general = sym.expand(hyperbola.general)
            h, k = hyperbola.center
            soln = f'({h}, {k})'
            
            question = f"""From the given equation of the hyperbola {general} = 0, find the center of the hyperbola."""
            
        if form == 12:
            hyperbola = analytic_geometry.hyperbola_general()
            e = hyperbola.e
            general = sym.expand(hyperbola.general)
            soln = f'{e}'
            question = f"""Find the eccentricity of the hyperbola whose equation is {general} = 0."""
            
        if form == 13:
            hyperbola = analytic_geometry.hyperbola_standard()
            standard_onelineL = hyperbola.standard_onelineL
            standard_onelineR = hyperbola.standard_onelineR
            asymptote_1_LHS, asymptote_1_RHS = hyperbola.asymptote_1
            asymptote_2_LHS, asymptote_2_RHS = hyperbola.asymptote_2
            soln = f'{asymptote_1_LHS} = {asymptote_1_RHS} and {asymptote_2_LHS} = {asymptote_2_RHS}'
            question = f"""Find the equation of the asysmptotes for a hyperbola {standard_onelineL} = {standard_onelineR}."""
            
        if form == 14:
            ellipseObject = analytic_geometry.ellipse_general()
            expression = sym.pretty(sym.expand(ellipseObject.general))
            area = math.pi * ellipseObject.a * ellipseObject.b
            soln = f'{area}'
            question = f"""Find the area bounded by the curve 
{expression} = 0"""

        if form == 15:
            ellipseObject = analytic_geometry.ellipse_standard()
            circumference = ellipseObject.circumference
            major = ellipseObject.a * 2
            minor = ellipseObject.b * 2
            soln = f'{circumference} meters'
            question = f"""What is the circumference of an ellipse whose diameters are {major} and {minor} meters."""
            
        if form == 16:
            ellipseObject = analytic_geometry.ellipse_standard()
            fx1, fy1, fx2, fy2 = ellipseObject.foci
            major = ellipseObject.major
            expression = sym.expand(ellipseObject.general)
            expression_pretty = sym.pretty(expression)
            question = f"""Determine the equation of the curve such that the sum of the distances of any point on the curve from two points whose coordinates are ({fx1}, {fy1}) and ({fx2}, {fy2}) is always equal to {major} """
            soln = f'{expression_pretty}'
            
        if form == 17:
            parabolaObject = analytic_geometry.parabola_general()
            expression = parabolaObject.general
            expression = sym.expand(expression)
            expression_pretty = sym.pretty(expression)
            fx, fy = parabolaObject.focus
            question = f"""Find the focus of the parabola 
{expression_pretty} = 0."""
            soln = f'({fx} , {fy})'
            
        if form == 18:
            circleObject = analytic_geometry.circle_standard()
            general_expr = circleObject.general
            general_expr_pretty = sym.pretty(general_expr)
            h, k = circleObject.center
            question = f"""What is the center of the curve
{general_expr_pretty} = 0"""
            soln = f'({h},{k})' 
            
        if form == 19:
            ellipseObject = analytic_geometry.ellipse_standard()
            e = ellipseObject.e
            a = ellipseObject.a
            focus_to_focus = ellipseObject.c * 2
            soln = f'{a}'
            question = f"""An ellipse has an eccentricity of {e}. What is the length of the semi-major axis if the distance between the foci is {focus_to_focus}?"""
            
        if form == 20:
            circleObject = analytic_geometry.circle_standard()
            general = circleObject.general
            general_pretty = sym.pretty(general)
            area = circleObject.area
            question = f"""Find the area of the circle whose equation is 
{general_pretty} = 0."""
            soln = f'{area}'
            
        if form == 21:
            hyperbolaObject = analytic_geometry.hyperbola_general()
            general = hyperbolaObject.general
            general_pretty = sym.pretty(general)
            lr = hyperbolaObject.latus_rectum
            question = f"""Compute the length of the latus rectum of the hyperbola
{general_pretty} = 0"""
            soln = f'{lr}'
            
        if form == 22:
            hyperbolaObject = analytic_geometry.hyperbola_standard()
            asl1, asr1 = hyperbolaObject.asymptote_1
            asl2, asr2 = hyperbolaObject.asymptote_2
            x, y = hyperbolaObject.point
            general = hyperbolaObject.general
            general_pretty = sym.pretty(general)
            
            question = f"""Determine the equation of the hyperbola whose asymptotes are, {asl1} = {asr1}, {asl2} = {asr2}, and which passes through ({x}, {y})"""
            soln = f'({general_pretty} = 0)'
            
        if form == 23:
            ellipseObject = analytic_geometry.ellipse_standard()
            fx1, fy1, fx2, fy2 = ellipseObject.foci
            major = ellipseObject.major
            general = ellipseObject.general
            general_pretty = sym.pretty(general)
            question = f"""Determine the equation of the curve such that the sum of the distances of any point on the curve from two points whose coordinates are ({fx1}, {fy1}) and ({fx2},{fy2}) is always equal to {major}."""
            soln = f'{general_pretty} = 0'
            
        if form == 24:
            hyperbolaObject = analytic_geometry.hyperbola_standard()
            general = hyperbolaObject.general
            general_pretty = sym.pretty(general)
            fx1, fy1, fx2, fy2 = hyperbolaObject.foci
            distance_x_axis = min(abs(fy1), abs(fy2))
            question = f"""How far from the x - axis is the nearer focus of the curve 
{general_pretty} = 0"""
            soln = f'{distance_x_axis}'
            
        if form == 25:
            hyperbolaObject = analytic_geometry.hyperbola_standard()
            fx1, fy1, fx2, fy2 = hyperbolaObject.foci
            major = hyperbolaObject.major
            general = hyperbolaObject.general
            general_pretty = sym.pretty(general)
            question = f"""A point moves so that the difference between its distance from ({fx1},{fy1}) and ({fx2},{fy2}) is {major}. Find the equation of the locus."""
            soln = f'{general_pretty}'
            
        self.question = question
        self.soln = soln
        self.solution = solution

print(title_string)
print()

 
for i in range (1,100):
    A = genericClass()
    print(str(stringHandling.cleanAst(A.question))) 
    print("""{a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    if solutions_flag == True:
        print("""solution: {a:s}""".format(a=str(A.solution)))
    print()
    



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
