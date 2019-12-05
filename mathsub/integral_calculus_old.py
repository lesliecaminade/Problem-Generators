import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
import algebra
import analytic_geometry

x, y = sym.symbols('x y', real = True)

init_printing(use_unicode=False)

class basic_1:
    def __init__(self):
        gobject = algebra.polynomial_linear()
        g = gobject.expression
        i = sym.Integral(ran.c(10)/g,x)
        i_eval = i.doit()
        
        self.expression = i
        self.answer = i_eval 

class basic_2:
    def __init__(self):
        f = ran.c(10)
        gobject = algebra.trigonometric()
        g = gobject.expression
        h = sym.sqrt(f + g)
        i = sym.Integral(h,x)
        i_eval = i.doit()
        
        self.expression = i
        self.answer = i_eval
        
class basic_3:
    def __init__ (self):
        fobject = algebra.polynomial_linear()
        f = fobject.expression
        gobject = algebra.polynomial_linear()
        g = gobject.expression
        hobject = algebra.polynomial_linear()
        h = hobject.expression
        i = sym.Integral(f / (g*h),x)
        i_eval = i.doit()
        
        self.expression = i
        self.answer = i_eval

class multiple_1:
    def __init__ (self):
        fobject = algebra.polynomial()
        f = fobject.expression
        x1, x2 = ran.low_high(10)
        y1, y2 = ran.low_high(10)
        i = sym.Integral(f,(y,y1,y2),(x,x1,x2))
        i_eval = i.doit()
        
        self.expression = i
        self.answer = i_eval
        
class multiple_2: 
    def __init__ (self):
        fobject = algebra.polynomial_quadratic_xy()
        f = fobject.expression
        x1, x2 = ran.low_high(10)
        #y1, y2 = ran.low_high(10)
        i = sym.Integral(f,(x,0,y),(y,x1,x2))
        i_eval = i.doit()
        
        self.expression = i
        self.answer = i_eval
        
class area_1: #parabola opening downward area
    def __init__ (self):
        y1, y2 = 0, 0
        x1, x2 = ran.low_high(10)
        x3 = (x1 + x2)/2
        y3 = ran.cpos(10)
        
        parabolaobject = analytic_geometry.parabola_3points_specific(x1,y1,x2,y2,x3,y3)
        g = parabolaobject.general
        gp = sym.pretty(g)
        
        i = sym.Integral(g,(x,x1,x2))
        i_eval = i.doit()
        
        self.problem = f"""Find the area of the curve y = ...
{gp} and the x - axis"""
        self.answer = f"""{i_eval}"""
        
        
class area_2: #parabola opening to the left
    def __init__(self):
        x1, x2 = 0, 0
        y1, y2 = ran.low_high(10)
        y3 = (y1 + y2)/2
        x3 = ran.cpos(10)
        
        parabolaobject = analytic_geometry.parabola_3points_specific_horizontal(x1,y1,x2,y2,x3,y3)
        g = parabolaobject.general
        gp = sym.pretty(g)
        
        i = sym.Integral(g,(y,y1,y2))
        i_eval = i.doit()
        
        self.problem = f"""Find the area of the curve x = ...
{gp} and the y - axis"""
        self.answer = f"""{i_eval}"""
        
class area_3: #down parabola and a line (Horizontal strip)
    def __init__ (self):
            paraObject = analytic_geometry.parabola_standard_orientation_vertex(3, ran.c(5), random.randint(5,10))
            
            lineObject = analytic_geometry.line_slope_intercept(ran.c(5), ran.cneg(10))
            
            p = paraObject.yinx  #this is in the form  y(x)
            l = lineObject.expression # y = mx + b
            
            #print(paraObject.standard)
            #print(l)
            
            pp = sym.pretty(p)
            lp = sym.pretty(l)
            
            #finding the intersection
            try:
                xintersections = sym.solveset(sym.Eq(p,l), x, domain = sym.Reals)
                print(xintersections)
                
                x1 = xintersections.args[0]
                x2 = xintersections.args[1]
                
                if x1 > x2:
                    x1, x2 = x2, x1
                
                area = sym.integrate((p-l),(x,x1,x2))
                xcentroid = sym.integrate(x*(p-l),(x,x1,x2)) / area
                ycentroid = sym.integrate(((p+l)/2)*(p-l),(x,x1,x2)) / area
                area = float(area)
                area = round(area,2)
                xcentroid = round(float(xcentroid),2)
                ycentroid = round(float(ycentroid),2)                
                
            except:
                #xintersections = 'error'
                area = 'error'
                xcentroid = 'error'
                ycentroid = 'error'
            
            self.problem = f"""ERROR: other problem_? attributes available"""
            self.problem_area = f"""Find the area bounded by the curve y =...
{pp} and the line y = ...
{lp}."""
            self.answer = f"""(ERROR: there are other answer_? parameters available)"""
            self.answer_area = f"""{area}"""
            
            self.problem_centroid = f"""Find the centroid of area bounded by the curve y =...
{pp} and the line y = ...
{lp}."""
            self.answer_xcentroid = f"""{xcentroid}"""
            self.answer_ycentroid = f"""{ycentroid}"""
            self.answer_centroid = f"""({xcentroid}, {ycentroid})"""
            
class area_4: # a cubic equation versus the x - axis (vertical strip)
    def __init__ (self):
        curveObject = algebra.polynomial_cubic_roots(ran.c(10), ran.c(10), ran.c(10))
        
        c = curveObject.expression
        cp = sym.pretty(c)
        
        x1, x2, x3 = curveObject.roots
        area1 = sym.integrate(c, (x, x1, x2))
        area2 = sym.integrate(c, (x, x2, x3))
        
        area = abs(area1) + abs(area2)
        
        self.problem = f"""Determine the area of the region bounded by the curve y = ...
{cp}, and the x - axis?"""
        self.answer = f"""{area}"""
        
class area_5: #right parabola and line (horizontal strip)
    def __init__ (self):
        paraObject = analytic_geometry.parabola_standard_orientation_vertex(0, ran.c(5), ran.c(5))
            
        lineObject = analytic_geometry.line_slope_intercept(ran.c(5), ran.cneg(10))
        p = paraObject.xiny  #this is in the form  y(x)
        l = lineObject.xiny # x = (y - b)/m
        
        #print(paraObject.standard)
        #print(l)
        
        pp = sym.pretty(p)
        lp = sym.pretty(l)
        
        #finding the intersection
        try:
            xintersections = sym.solveset(sym.Eq(p,l), y, domain = sym.Reals)
            #print(xintersections)
            
            y1 = xintersections.args[0]
            y2 = xintersections.args[1]
            
            if y1 > y2:
                y1, y2 = y2, y1
            
            area = sym.integrate((l-p),(y,y1,y2))
            xcentroid = sym.integrate(((l+p)/2)*(l-p),(y,y1,y2))/ area
            ycentroid = sym.integrate(y*(l-p),(y,y1,y2))/ area
            area = float(area)
            area = round(area,2)
            xcentroid = round(float(xcentroid),2)
            ycentroid = round(float(ycentroid),2)
            
        except:
            #xintersections = 'error'
            area = 'error'
            xcentroid = 'error'
            ycentroid = 'error'
        
        self.problem = f"""ERROR: there are other problem_? attributes available"""
        self.problem_area = f"""Find the area bounded by the curve x =...
{pp} and the line x = ...
{lp}."""
        self.answer = f"""(ERROR: there are other answer_? atributes available)"""
        self.answer_area = f"""{area}"""
        
        self.problem_centroid = f"""Find the centroid of area bounded by the curve x =...
{pp} and the line x = ...
{lp}."""
        self.answer_xcentroid = f"""{xcentroid}"""
        self.answer_ycentroid = f"""{ycentroid}"""
        self.answer_centroid = f"""({xcentroid}, {ycentroid})"""
        
class length_of_arc_1: #legnth of arc y(x) dy/dx version
    def __init__ (self):
        
        curveObject = algebra.polynomial()
        c = curveObject.expression
        cd = sym.diff(c,x)
        x1, x2 = ran.low_high(10)
        
        length = sym.integrate(sym.sqrt(1 + (cd)**2 ), (x, x1,x2))
        cp = sym.pretty(c)
        
        self.problem = f"""Find the length of arc of the curve y = ...
{cp} 
from x = {x1} to x = {x2}"""
        self.answer = f"""{length}"""
        
        
        
        
        
        