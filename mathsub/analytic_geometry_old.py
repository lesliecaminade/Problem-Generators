import random_handler as ran
import numpy_handler as num
import sympy as sym
import math
import random

x, y = sym.symbols('x y', real = True)

def point(*args, **kwargs):
    
    try:
        type = args[0]
    except:
        type = 'cartesian'
        
    try:
        input = kwargs['range']
    except:
        input = 10
    
    if type == 'cartesian':
        try:
            dimensions = kwargs['dimensions']
        except:
            dimensions = 2
            
        try:
            input = kwargs['range']
        except:
            input = 10
            
        if dimensions == 2:
            a = random.randint(-input,input)
            b = random.randint(-input,input)
            return a,b
            
        if dimensions == 3:
            a = random.randint(-input,input)
            b = random.randint(-input,input)
            c = random.randint(-input,input)
            return a,b,c

    if type == 'cylindrical':
        a = random.randint(0, input)
        b = random.randint(0, 360) #degrees
        c = random.randint(-input, input)
        return a,b,c
        
    if type == 'spherical':
        a = random.randint(0,input)
        b = random.randint(0,180) #degrees
        c = random.randint(0,360) #degrees
        
# class pointInstance: #later should be merged with point
    # def __init__(self, *args, **kwargs):
        # try:
            # type = kwargs['type']
        # except:
            # type = 'cartesian'
            
        # try:
            # input = kwargs['range']
        # except:
            # input = 10
        
        # if type == 'cartesian':
            # try:
                # dimensions = kwargs['dimensions']
            # except:
                # dimensions = 2
                
            # try:
                # input = kwargs['range']
            # except:
                # input = 10
                
            # if dimensions == 2:
                # a = random.randint(-input,input)
                # b = random.randint(-input,input)
                # return a,b
                
            # if dimensions == 3:
                # a = random.randint(-input,input)
                # b = random.randint(-input,input)
                # c = random.randint(-input,input)
                # return a,b,c

        # if type == 'cylindrical':
            # a = random.randint(0, input)
            # b = random.randint(0, 360) #degrees
            # c = random.randint(-input, input)
            # return a,b,c
            
        # if type == 'spherical':
            # a = random.randint(0,input)
            # b = random.randint(0,180) #degrees
            # c = random.randint(0,360) #degrees
            
    # def convert(*args,**kwargs):
        # try:
            # type = kwargs['type']
        # except:
            # type = 'cartesian'
            
        
def polar(*args):
    xcoord = args[0]
    ycoord = args[1]
    
    radius = math.sqrt(xcoord**2 + ycoord**2)
    
    if xcoord >= 0 and ycoord >=0:
        theta = math.atan(ycoord/xcoord)*constants_conversions.RADIANS
        

    
def point_quadrant(input, Q1=True,Q2=True,Q3=True,Q4=True):
    xpos, xneg, ypos, yneg = False, False, False, False
    #conditions for x
    if Q1 or Q4:
        xpos = True
    if Q2 or Q3:
        xneg = True
        
    #condition for y
    if Q1 or Q2:
        ypos = True
    if Q3 or Q4:
        yneg = True

    if xpos and xneg:
        x = ran.c(input)
    elif xpos and (not xneg):
        x = ran.cpos(input)
    elif (not xpos) and xneg:
        x = ran.cneg(input)
    else:
        x = 0
        
    if ypos and yneg:
        y = ran.c(input)
    elif ypos and (not yneg):
        y = ran.cpos(input)
    elif (not ypos) and yneg:
        y = ran.cneg(input)
    else:
        y = 0
    
    return x,y
        
    
def distancePointPoint(x1,y1,x2,y2):
    distance = math.sqrt((x1 -x2)**2 + (y1-y2)**2)
    return distance
    
def lineTwoPoint(x1,y1,x2,y2):
    #format y = function of x
    LHS = y
    RHS = ((y2 - y1)/(x2 - x1))*(x - x1) + y1
    return LHS, RHS
    
class line_slope_intercept:
    def __init__(self, slope, yintercept):
        #this is a line in the form y = mx +b
        expr = slope*x + yintercept - y
        try:
            self.yinx = sym.solveset(expr, y, domain = sym.Reals).args[0]   
            self.expression = sym.solveset(expr, y, domain = sym.Reals).args[0] 
        except:
            self.yinx = 'error in solving for y(x) in line'
            self.expression = 'error in solving for y(x) in line'
            
        try:
            self.xiny = sym.solveset(expr, x, domain = sym.Reals).args[0] 
        except:
            self.xiny = 'error in solving for x(y) in line'
        
class circle_standard:
    def __init__(self):
        h = ran.c(10)
        k = ran.c(10)
        r = ran.cpos(10)
        standard_L = (x - h)**2 + (y - k)**2
        standard_R = r**2
        general = sym.expand(standard_L - standard_R)
        self.standard_L = standard_L
        self.standard_R = standard_R
        self.general = general
        self.r = r
        self.h = h
        self.k = k
        self.center = h,k
        self.diameter = 2*r
        self.area = math.pi * r**2
        

class ellipse_standard:
    def __init__(self):
        h = ran.c(10)
        k = ran.c(10)
        a = 1
        b = 1
        while a == b:
            a = ran.cpos(10)
            b = ran.cpos(10)
        
        if a < b:
            a,b = b,a
        
        c = math.sqrt(a**2 - b**2)
        orientation = random.randint(0,1)
        if orientation == 0: #horizontal
            standard_L = (x - h)**2/a**2 + (y - k)**2/b**2
            standard_R = 1
            A = b**2
            C = a**2
            D = -2 * b**2 * h
            E = -2 * a**2 * k
            F = b**2*h**2 + a**2*k**2 - a**2*b**2
            general = A*x**2 + C*y**2 + D*x + E*y + F 
            fx1, fy1, fx2, fy2 = h - c, k , h + c , k
            vx1, vy1, vx2, vy2 = h - a, k , h + a , k
            
        if orientation == 1: #vertical
            standard_L = (x - h)**2/b**2 + (y - k)**2/a**2
            standard_R = 1
            A = a**2
            C = b**2
            D = -2 * a**2 * h
            E = -2 * b**2 * k
            F = a**2*h**2 + b**2*k**2 - a**2*b**2
            general = A*x**2 + C*y**2 + D*x + E*y + F 
            fx1, fy1, fx2, fy2 = h, k - c , h , k + c
            vx1, vy1, vx2, vy2 = h, k - a , h , k + a
        
        
        e = c / a
        d = a / e
        latus_rectum = (2*b**2) / a
        circumference = math.pi * (3*(a+b) - math.sqrt(10*a*b + 3*(a**2 + b**2)))
        
        self.A = A
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.c = c
        self.focal_length = abs(c)
        self.focal_distance = abs(c)
        self.h = h
        self.k = k
        self.center = h, k
        self.foci = fx1, fy1, fx2, fy2
        self.vertices = vx1, vy1, vx2, vy2
        self.latus_rectum = latus_rectum
        self.general = general
        self.standard_L = standard_L
        self.standard_R = standard_R
        self.eccentricity = e
        self.e = e
        self.d = d
        self.a = a
        self.semi_major = a
        self.b = b
        self.semi_minor = b
        self.major = 2*a
        self.minor = 2*b
        self.orientation = orientation
        self.area = math.pi * a * b
        self.circumference = circumference
        
          
class ellipse_general:
    def __init__(self):
        discriminant = 1
        A = 1
        C = 1
        while (not(discriminant < 0)) or A == C:
            A = ran.cpos(10)
            B = 0
            C = ran.cpos(10)
            D = ran.c(100)
            E = ran.c(100)
            discriminant = B**2 - 4*A*C
            
        if C > A: #horizontal ellipse
            a = math.sqrt(C)
            b = math.sqrt(A)
            h = -D / (2*A)
            k = -E / (2*C)
            
        if A > C: #vertical ellipse
            a = math.sqrt(A)
            b = math.sqrt(C)
            h = -D / (2*A)
            k = -E / (2*C)
            
        F = b**2 * h**2 + a**2 * k**2 - a**2 * b**2
            
        c = math.sqrt(a**2 - b**2)
        e = c / a
            
        general = A*x**2 + C*y**2 + D*x + E*y + F  

        self.general = general
        self.e = e
        self.c = c
        self.a = a
        self.b = b
        self.center = h,k
        self.h = h
        self.k = k
        self.major = 2*a
        self.minor = 2*b
        self.latus_rectum = 2*b**2 / a
        self.d = a / e
    
class parabola_standard:
    def __init__(self, orientation = random.randint(0,3)):
        
        h,k = ran.point(10)
        focal_length = ran.cpos(10)
        
        if orientation == 0: #right
            xf = h + focal_length
            yf = k
        if orientation == 1: #left
            xf = h - focal_length
            yf = k
            focal_length  = -focal_length
        if orientation == 2: #up
            xf = h
            yf = k + focal_length
        if orientation == 3: #down
            xf = h
            yf = k - focal_length
            focal_length = -focal_length
            
        if orientation == 0 or orientation == 1:
            expr = (y - k)**2 - 4*focal_length*(x - h)
        if orientation == 2 or orientation == 3:
            expr = (x - h)**2 - 4*focal_length*(y - k)
       
        
        
        list = ['right', 'left', 'up', 'down']
        orientation_desc = list[orientation]
        general = sym.expand(expr)
        
        
        self.h = h
        self.k = k
        self.focal_length = focal_length
        self.focal_distance = focal_length
        self.orientation = orientation
        self.orientation_desc = orientation_desc
        self.general = general
        self.standard = expr

        
class parabola_standard_orientation_vertex:
    def __init__(self, orientation, h, k, focal_length = ran.cpos(10)):
        
        focal_length = ran.cpos(10)
        
        if orientation == 0: #right
            xf = h + focal_length
            yf = k
        if orientation == 1: #left
            xf = h - focal_length
            yf = k
            focal_length = -focal_length
        if orientation == 2: #up
            xf = h
            yf = k + focal_length
        if orientation == 3: #down
            xf = h
            yf = k - focal_length
            focal_length = -focal_length
            
            
        if orientation == 0 or orientation == 1:
            expr = (y - k)**2 - 4*focal_length*(x - h)
        if orientation == 2 or orientation == 3:
            expr = (x - h)**2 - 4*focal_length*(y - k)
       
        list = ['right', 'left', 'up', 'down']
        orientation_desc = list[orientation]
        general = sym.expand(expr)
        
        try:
            yinx = sym.solveset(expr, y)
        except:
            yinx = 'error in solving for y'
        
        try: 
            xiny = sym.solveset(expr, x)
        except:
            xiny = 'error in solving for x'
        
        self.h = h
        self.k = k
        self.focal_length = focal_length
        self.focal_distance = focal_length
        self.orientation = orientation
        self.orientation_desc = orientation_desc
        self.general = general
        self.standard = expr
        self.yinx = yinx.args[0]
        self.xiny = xiny.args[0]

class parabola_general:
    def __init__(self):

        A = ran.cnz(10)
        C = ran.cnz(10)
        D = ran.cnz(10)
        E = ran.cnz(10)
        F = ran.c(10)
        
        i = random.randint(0,1)
        if i == 0: #vertical
            expr = A*x**2 + D*x + E*y + F
            h = -D / (2*A)
            k = - ((F/E) - (D**2 / (4*A*E)))
            focal_length = -E / (4*A)
 
            standard_L = (x - h)**2
            standard_R = 4*focal_length*(y - k)
            
            if focal_length > 0: #upward
                fy = k + abs(focal_length)
            if focal_length < 0: #downward
                fy = k - abs(focal_length)
            fx = h
            


        if i == 1: #horizontal
            expr = C*y**2 + D*x + E*y + F
            k = -E / (2*C)
            h = - ((F/D) - (E**2 / (4*C*D)))
            focal_length = -D / (4*C)
            standard_L = (y - k)**2
            standard_R = 4*focal_length*(x - h)
            
            if focal_length > 0: #rightward
                fx = h + abs(focal_length)
            if focal_length < 0: #leftward
                fx = h - abs(focal_length)
            fy = k
            
        latus_rectum = 4*abs(focal_length)
        general = sym.expand(expr)
        
        
        self.A = A
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.focal_length = abs(focal_length)
        self.focal_distance = abs(focal_length)
        self.h = h
        self.k = k
        self.center = h, k
        self.focus = fx, fy
        self.latus_rectum = latus_rectum
        self.general = general
        self.standard_L = standard_L
        self.standard_R = standard_R

class parabola_3points_specific:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        a, b, c = sym.symbols('a b c', real = True)
        eqns = [a*x1**2 + b*x1 + c - y1, a*x2**2 + b*x2 + c - y2,a*x3**2 +b*x3 + c - y3]
        #print(sym.linsolve(eqns, a, b, c))
        try:
            A = sym.linsolve(eqns, a, b, c).args[0][0]
            B = sym.linsolve(eqns, a, b, c).args[0][1]
            C = sym.linsolve(eqns, a, b, c).args[0][2]
            general = A*x**2 + B*x + C
        except:
            general = 'error'       
        self.general = general

class parabola_3points_specific_horizontal:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        a, b, c = sym.symbols('a b c', real = True)
        eqns = [a*y1**2 + b*y1 + c - x1, a*y2**2 + b*y2 + c - x2,a*y3**2 +b*y3 + c - x3]
        #print(sym.linsolve(eqns, a, b, c))
        try:
            A = sym.linsolve(eqns, a, b, c).args[0][0]
            B = sym.linsolve(eqns, a, b, c).args[0][1]
            C = sym.linsolve(eqns, a, b, c).args[0][2]
            general = A*y**2 + B*y + C
        except:
            general = 'error'       
        self.general = general    
        
class hyperbola_standard:
    def __init__(self):

        h, k = ran.point(10)
        a = ran.cpos(10)
        b = ran.cpos(10)
        
        orient = random.randint(0,1)
        c = math.sqrt(a**2 + b**2)
        if orient == 0:
            standard_L = (x - h)**2/a**2 - (y - k)**2/b**2
            standard_R = 1
            standard_onelineL = b**2*(x - h)**2 - a**2*(y - k)**2
            standard_onelineR = a**2*b**2
            general = b**2*x**2 - a**2*y**2 - 2*b**2*h*x + 2*a**2*k*y + b**2*h**2 - a**2*k**2 - a**2*b**2 
            asymptote_1_LHS, asymptote_1_RHS = lineTwoPoint(h,k,h+a,k+b)
            asymptote_2_LHS, asymptote_2_RHS = lineTwoPoint(h,k,h-a,k+b)
            vx1 = h + a
            vy1 = k
            vx2 = h - a
            vy2 = k
            fx1 = h + c
            fy1 = k
            fx2 = h - c
            fy2 = k
            temp = random.randint(0,1)
            if temp == 0:
                random_point_x = random.randint(vx1,vx1+50)
            if temp == 1:
                random_point_x = random.randint(vx2-50,vx2)
                    
            random_point_y = sym.solveset(general.subs(x,random_point_x),y,domain=sym.Reals)
            
        if orient == 1:
            standard_L = (y - k)**2/a**2 - (x - h)**2/b**2
            standard_R = 1
            standard_onelineL = b**2*(y - k)**2 - a**2*(x - h)**2
            standard_onelineR = a**2*b**2
            general = - a**2*x**2 + b**2*y**2 + 2*a**2*h*x -2*b**2*k*y +  b**2*k**2 - a**2*h**2 - a**2*b**2
            asymptote_1_LHS, asymptote_1_RHS = lineTwoPoint(h,k,h+b,k+a)
            asymptote_2_LHS, asymptote_2_RHS = lineTwoPoint(h,k,h+b,k-a)
            vx1 = h
            vy1 = k + a
            vx2 = h
            vy2 = k - a 
            fx1 = h
            fy1 = k + c
            fx2 = h
            fy2 = k - c
            
            temp = random.randint(0,1)
            if temp == 0:
                random_point_y = random.randint(vy1,vy1+50)
            if temp == 1:
                random_point_y = random.randint(vy2-50,vy2)
                    
            random_point_x = sym.solveset(general.subs(y,random_point_y),x,domain=sym.Reals)
            
        
        e = c / a
        d = a / e
        


        
        self.general = general
        
        self.standard_L = standard_L
        self.standard_R = standard_R
        self.standard_onelineL = standard_L
        self.standard_onelineR = standard_R
        
        self.e = e
        self.c = c
        self.a = a
        self.b = b
        
        self.major = 2*a
        self.minor = 2*b
        
        self.latus_rectum = 2*b**2 / a
        
        self.d = d
        self.center = h, k
        self.h = h
        self.k = k
        self.asymptote_1 = asymptote_1_LHS, asymptote_1_RHS
        self.asymptote_2 = asymptote_2_LHS, asymptote_2_RHS
        self.point = random_point_x, random_point_y
        self.foci = fx1, fy1, fx2, fy2
        self.vertices = vx1, vy1, vx2, vy2
        

        
class hyperbola_general:
    def __init__(self):
        discriminant = 0
        A = 1
        C = 1
        while (not(discriminant > 0)):
            
            select = random.randint(0,1)
            if select == 0:
                A = ran.cpos(10)
                C = ran.cneg(10)
                
            if select == 1:
                A = ran.cneg(10)
                C = ran.cpos(10)
                
            B = 0
            C = ran.c(10)
            D = ran.c(100)
            E = ran.c(100)
            F = ran.c(100)

            discriminant = B**2 - 4*A*C
            
        if C > A: #vertical hyperbola
            a = math.sqrt(C)
            b = math.sqrt(-A)
            
        if A > C: #horizontal hyperbola
            a = math.sqrt(A)
            b = math.sqrt(-C)
            
        
        h = -D / (2 * A)
        k = -E / (2 * C)
        
        c = math.sqrt(a**2 + b**2)
        e = c / a
        d = a / e
        general = A*x**2 + C*y**2 + D*x + E*y + F  
        
        self.general = general
        self.e = e
        self.c = c
        self.a = a
        self.b = b
        self.major = 2*a
        self.minor = 2*b
        self.latus_rectum = 2*b**2 / a
        self.d = d
        self.center = h, k
        self.h = h
        self.k = k
        
