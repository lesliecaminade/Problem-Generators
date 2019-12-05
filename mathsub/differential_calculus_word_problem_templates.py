import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import div
import math
import random
import algebra

x, y = sym.symbols('x y', real = True)

init_printing(use_unicode=True)

class maxima_rectangle_inside_a_circle:
    def __init__(self):
        radius = ran.cpos(50)
        xmax = (sym.sqrt(2)/2)*radius
        Amax = 2*xmax*sym.sqrt(radius**2 - xmax**2)
        
        question = f"""What is the area of the largest rectangle that can be inscribed in a semicircle of radius {radius}"""
        answer = f"""{Amax}"""
        
        self.question = question
        self.answer = answer
        
class maxima_numbers_1:
    def __init__(self):
        sum = ran.cpos(50)
        num1 = sym.Rational(2,3)*sum
        num2 = sum - num1
        
        self.question = f"""The sum of two numbers is {sum}. The product of one of the numbers by the square of the other is to maximum, what are the numbers?"""
        self.answer = f"""{num1} and {num2}"""
        
class minima_two_posts:
    def __init__(self):
        lengthA = ran.cpos(50)
        lengthB = ran.cpos(50)
        distanceD = random.randint(40,100)
        distancex = (lengthA * distanceD) / (lengthA + lengthB)
        
        min_wire = sym.sqrt(distancex**2 + lengthA**2) + sym.sqrt(lengthB**2 + (distanceD - distancex)**2)
        
        version = random.randint(0,1)
        if version == 0:
        
            self.question = f"""Two posts, one {lengthA} m and the other {lengthB} m high are {distanceD} m apart. If the posts are supported by a cable running from the top of the first post to a stake on the ground and then back to the top of the second post, find the distance from the lower post to the stake to use the minimum amount of wire."""
            self.answer = f"""{distancex} m"""
        if version == 1:
            self.question = f"""Two posts, one {lengthA} m and the other {lengthB} m high are {distanceD} m apart. If the posts are supported by a cable running from the top of the first post to a stake on the ground and then back to the top of the second post, find the minimum amount of wire that can be used."""
            self.answer = f"""{min_wire} m"""
            
class minima_rowboat:
    def __init__(self):
        
        
        a = ran.cpos(30)
        b = ran.cpos(30)
        r = ran.cpos(30)
        s = ran.cpos(30)

        
        while b**2 * r**2 * s**2 - b**2 * r**4 <0  or r**2 - s**2 == 0:
            a = ran.cpos(30)
            b = ran.cpos(30)
            r = ran.cpos(30)
            s = ran.cpos(30)
        
        x1 = (a * r**2 - a * s**2  - math.sqrt(b**2 * r**2 * s**2 - b**2 * r**4) )/(r**2 - s**2)
        x2 = (a * r**2 - a * s**2  + math.sqrt(b**2 * r**2 * s**2 - b**2 * r**4) )/(r**2 - s**2)
        
        if x1 >= 0 and x1 <= a:        
            distx = x1
        elif x2 >= 0 and x2 <= a:
            distx = x2
        else: 
            distx = 'extrema on edge (direct to shore or direct to destination) case'
            
        
        self.question = f"""A person in a rowboat is {b} km from the shore from a point P on a straight shore while his destination is {a} km directly east of point P. If he is able to row {r} kph and walk {s} kph, how far from his destination must he land on the shore in order to reach his destination in the shortest possible time?"""
        self.answer = f"""{distx} km"""
        
class related_rates_kite:
    def __init__(self):
        Y = random.randint(40,80)
        dxdt = ran.cpos(10)
        dydt = 0
        X = random.randint(40,80)
        Z = math.sqrt(X**2 + Y**2)
        dzdt = (X * dxdt + Y * dydt)/Z
        
        self.question = f"""A kite, at a height of {Y} ft is moving horizontally at a rate of {dxdt} ft/s away from the boy who flies it. How fast is the cord being released when there are {Z} ft out?"""
        self.answer = f"""{dzdt} ft/s"""
        
class related_rates_conical_tank:
    def __init__ (self):
        dVdt = ran.cpos(30)
        H = random.randint(10,30)
        D = random.randint(5,15)
        R = D / 2
        h = random.randint(1,H-1)
        
        dhdt = dVdt / (math.pi * (R/H)**2 * h**2)
        
        self.question = f"""Water is flowing into a conical reservoir {H} ft deep and {D} feet across the top, at a rate of {dVdt} cubic feet per minute. Find how fast is the water rising when it is {h} feet deep?"""
        self.answer = f"""{dhdt} ft/min"""
        
class approx_error_sphere:
    def __init__(self):
        R = random.randint(5,15)
        dR = random.randint(1,10)/100
        dV = 4 * math.pi * R**2 * dR
        V = (4/3) * math.pi * R**3
        dVV = dV / V 
        dVV_percent = dVV * 100
        
        self.question = f"""If the radius of the sphere is measured as {R} in with a possible error of {dR} inch, find the approximate error and the percentage error in the computed value of the volume."""
        self.answer = f"""{dV} inch^3, {dVV_percent} %"""
        
class related_rates_speed_of_a_particle:
    def __init__(self):
        xtobject = algebra.polynomial()
        ytobject = algebra.polynomial()
        xt = xtobject.expression
        yt = ytobject.expression
        t_sym = sym.symbols('t')
        xt = xt.subs(x,t_sym)
        yt = yt.subs(x,t_sym)
        t = random.randint(1,10)
        xt_eval = xt.subs(t_sym,t)
        yt_eval = yt.subs(t_sym,t)
        speed = math.sqrt(xt_eval**2 + yt_eval**2)
        
        self.question = f"""The equation of motion of a particle moving in a plane are x = {xt} and y = {yt} when t is the time and x and y are rectangular coordinates. Find the speed of motion at the instant when t = {t}."""
        self.answer = f"""{speed}"""
        
class radius_of_curvature:
    def __init__(self):
        fobject = algebra.polynomial_quadratic()
        f = fobject.expression
        fd = sym.diff(f,x)
        fdd = sym.diff(f,x,x)
        x1 = ran.c(10)
        y1 = float(f.subs(x,x1))
        fd_eval = fd.subs(x,x1)
        fdd_eval = fdd.subs(x,x1)
        ROC = abs(((1 + fd_eval**2)**(3/2))/fdd_eval)
        
        self.question = f"""Find the approximate radius of curvature of the function y = {f} at the point ({x1},{y1})"""
        self.answer = f"""{ROC}"""
        
        
    

