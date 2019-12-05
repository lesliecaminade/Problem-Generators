import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
import algebra
import analytic_geometry
import constants_conversions
# from sympy.vector import CoordSys3D
# from sympy.physics.vector import gradient
# from sympy.physics.vector import ReferenceFrame

x, y, z = sym.symbols('x y z', real = True)
i, j, k = sym.symbols('i j k', real = True)

#V = CoordSys3D('V')
#R = ReferenceFrame('R')


#Last Updated: June 26 2019

init_printing(use_unicode=False)

def randomMonomial():
    expression = ran.c(5)*x**random.randint(0,3)*y**random.randint(0,3)*z**random.randint(0,3)
    return expression
    
class vector: #custom vector
    def __init__(self, *args, **kwargs):
        try:
            a = args[0]
        except:
            a = ran.c(10)
            
        try:
            b = args[1]
        except:
            b = ran.c(10)
            
        try:
            c = args[2]
        except:
            c = ran.c(10)

        field = False
        for arg in args:
            if arg == 'field':
                field = True
                
                
        #standard 3 dimensional vector
        if not field:
            self.vector = a*i + b*j + c*k 
            self.x = a
            self.y = b
            self.z = c
            
        if field:
            a = randomMonomial()
            b = randomMonomial()
            c = randomMonomial()
            self.vector = a*i + b*j + c*k
            self.x = a
            self.y = b
            self.z = c
        
        #two dimensional vector
        for arg in args:
            if arg == '2dim':
                if not field:
                    self.vector = a*i + b*j 
                    self.x = a
                    self.y = b
                    #self.z = c
                    
                if field:
                    a = randomMonomial()
                    b = randomMonomial()
                    #c = randomMonomial()
                    self.vector = a*i + b*j
                    self.x = a
                    self.y = b
                    #self.z = c
            
    def magnitude(self):
        try:
            magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        except:
            magnitude = sym.sqrt(self.x**2 + self.y**2 + self.z**2)
        
        self.magnitude = magnitude
        return magnitude
        
    def normalize(self):
        magnitude = self.magnitude()
        normx = self.x / magnitude
        normy = self.y / magnitude
        normz = self.z / magnitude
        return vector(normx, normy, normz)
    
    def add(self,vector2):
        addx = self.x + vector2.x
        addy = self.y + vector2.y
        addz = self.z + vector2.z
        #add = addx*i + addy*j + addz*k
        return vector(addx, addy, addz)
        
    def scalar_multiplication(self,num):
        self.x = self.x * num
        self.y = self.y * num
        self.z = self.z * num
        self.vector = self.x*i + self.y*j + self.z*k
        return vector(self.x, self.y, self.z)

    def subtract(self,vector2):
        addx = self.x - vector2.x
        addy = self.y - vector2.y
        addz = self.z - vector2.z
        #add = addx*i + addy*j + addz*k
        return vector(addx, addy, addz)       
        
    def dot(self, vector2):
        dotx = self.x * vector2.x
        doty = self.y * vector2.y
        dotz = self.z * vector2.z
        return dotx + doty + dotz
        
    def cross(self,v2):
        crossx = self.y*v2.z - self.z*v2.y
        crossy = self.z*v2.x - self.x*v2.z
        crossz = self.x*v2.y - self.y*v2.x
        # print(crossx)
        # print(crossy)
        # print(crossz)
        return vector(crossx, crossy, crossz)
        
    def component(self,v2):
        return self.dot(v2.normalize())
        
    def projection(self,v2):
        unitb = v2.normalize()
        adotb = self.dot(unitb)
        adotb_x_unitb = unitb.scalar_multiplication(adotb)
        return adotb_x_unitb
        
    def scalar_triple_product(self,v2,v3):
        bcrossc = v2.cross(v3)
        adotbcrossc = self.dot(bcrossc)
        return adotbcrossc
        
    def vector_triple_product(self,v2,v3):
        bcrossc = v2.cross(v3)
        acrossbcrossc = self.cross(bcrossc)
        return acrossbcrossc
        
    def divergence(self):
        divx = sym.diff(self.x, x)
        divy = sym.diff(self.y, y)
        divz = sym.diff(self.z, z)
        div = divx + divy + divz
        return div
        
    def curl(self):
        curlx = sym.diff(self.z, y) - sym.diff(self.y, z)
        curly = sym.diff(self.x, z) - sym.diff(self.z, x)
        curlz = sym.diff(self.y, x) - sym.diff(self.x, y)
        return vector(curlx, curly, curlz)
        
       
class scalar_field:
    def __init__(self,**kwargs):
        try:
            degree = kwargs['degree']
        except:
            degree = 2
            
        A = ran.c(3)
        B = ran.c(3)
        C = ran.c(3)
        D = ran.c(3)
        E = ran.c(3)
        F = ran.c(3)
        G = ran.c(3)
        H = ran.c(3)
        I = ran.c(3)
        J = ran.c(3)

        if degree == 2:
            self.scalar = A*x**2 + B*x*y + C*y**2 + D*y*z + E*z**2 + F*x*z
            
        if degree == 3:
            self.scalar = A*x**3 + B*x**2*y + C+x**2*z + D*y**3 + E*y**2*x + F*y**2*z + G*z**3 + H*z**2*x + I*z**2*y + J*x*y*z
            
    def gradient(self, **kwargs):
    
        try:
            components = kwargs['point']
            subsx, subsy, subsz = components[0],components[1],components[2]
            subs = True
        except:
            subs = False
    
        dx = sym.diff(self.scalar, x)
        dy = sym.diff(self.scalar, y)
        dz = sym.diff(self.scalar, z)
        
        if subs:
            dx = dx.subs(x, subsx)
            dx = dx.subs(y, subsy)
            dx = dx.subs(z, subsz)
            
            dy = dy.subs(x, subsx)
            dy = dy.subs(y, subsy)
            dy = dy.subs(z, subsz)
            
            dz = dz.subs(x, subsx)
            dz = dz.subs(y, subsy)
            dz = dz.subs(z, subsz)
        
        return vector(dx, dy, dz)
        
    def pointOnScalar(self):
        pointx = ran.c(10)
        pointy = ran.c(10)
        sc = self.scalar.subs(x, pointx)
        sc = sc.subs(y, pointy)
        
        try:
            pointz = sym.solveset(sc,z,domain = sym.Reals).args[0]
        except:
            pointz = 'z coordinate not found'
        
        return pointx, pointy, pointz

class plane:
    def __init__(self, **kwargs):
    
        try:
            n = kwargs['normal']
        except:
            n = vector()
            
        try:
            px, py, pz = kwargs['point']
        except:
            px, py, pz = analytic_geometry.point(dimensions = 3)
            
        try:
            equation_plane = n.x * (x - px) + n.y*(y - py) + n.z*(z - pz)
        except:
            equation_plane = 'unable to solve plane equation'
            
        self.equation = equation_plane
        self.normalvector = vector(n.x, n.y, n.z)
        
        
        
        
        
#-------------------------------------------------------------------
class adding:
    def __init__(self):
        vecObject1 = vector()
        vecObject2 = vector()
        v1 = vecObject1.vector
        v2 = vecObject2.vector
        
        vadd = vecObject1.add(vecObject2)
        vaddv = vadd.vector
        self.question = f"""Add the vectors {v1} and {v2}"""
        self.answer = f"""{vaddv}"""
        
class dot_product:
    def __init__ (self):
        vecObject1 = vector()
        vecObject2 = vector()
        v1 = vecObject1.vector
        v2 = vecObject2.vector
        
        dot = vecObject1.dot(vecObject2)
        
        self.question = f"""Find the dot product of the vectors {v1} and {v2}"""
        self.answer = f"""{dot}"""
        
class cross_product:
    def __init__(self,**kwargs):
        try:
            version = kwargs['version']
        except:
            version = 0
        vObj1 = vector()
        vObj2 = vector()
        v1 = vObj1.vector
        v2 = vObj2.vector    
            
        crossObj = vObj1.cross(vObj2)
        cross = crossObj.vector
        self.question = f"""Find the cross product of the vectors {v1} and {v2}"""
        self.answer = f"""{cross}"""
        
        if version == 1:
            self.question = f"""Find the unit vector perpendicular to both vectors {v1} and {v2}"""
            unitObject = crossObj.normalize()
            unit = unitObject.vector
            unitObject2 = unitObject.scalar_multiplication(-1)
            unit2 = unitObject2.vector
            self.answer = f"""{unit} or {unit2}"""
        
class angle_between_two_vectors:
    def __init__(self):
        vObj1 = vector()
        vObj2 = vector()
        v1 = vObj1.vector
        v2 = vObj2.vector 
        angle = math.acos(vObj1.dot(vObj2) / (vObj1.magnitude()*vObj2.magnitude()))*constants_conversions.RADIANS
        
        self.question = f"""Find the angle between the vectors {v1} and {v2}"""
        self.answer = f"""{angle} degrees"""
        
class orthogonal_vectors:
    def __init__(self):
        u = random.randint(1,3)
        
        if u == 1:
            vctObj1 = vector(x, ran.c(10), ran.c(10))
        if u == 2:
            vctObj1 = vector(ran.c(10), x, ran.c(10))
        if u == 3:
            vctObj1 = vector(ran.c(10), ran.c(10), x)
            
        vctObj2 = vector()
        v1 = vctObj1.vector
        v2 = vctObj2.vector
        
        dotexpr = vctObj1.dot(vctObj2)
        try:
            unknown = sym.solveset(dotexpr, x, domain = sym.Reals).args[0]
        except:
            unknown = 'solveset error'
        
        self.question = f"""Find the value of x that will make the vectors {v1} and {v2} orthogonal"""
        self.answer = f"""{unknown}"""
        
class component_of_a_vector:
    def __init__(self):
        vctObj1 = vector()
        vctObj2 = vector()
        v1 = vctObj1.vector
        v2 = vctObj2.vector
        comp = vctObj1.component(vctObj2)
        
        self.question = f"""Find the component of {v1} onto {v2}"""
        self.answer = f"""{comp}"""
        
class projection_of_a_vector:
    def __init__(self):
        vctObj1 = vector()
        vctObj2 = vector()
        v1 = vctObj1.vector
        v2 = vctObj2.vector
        projObj = vctObj1.projection(vctObj2)
        proj = projObj.vector
        self.question = f"""Find the projection of {v1} onto {v2}"""
        self.answer = f"""{proj}"""   

class scalar_triple_product:
    def __init__(self, **kwargs):
        try:
            version = kwargs['version']
        except:
            version = 0
            
        ovcta = vector()
        ovctb = vector()
        ovctc = vector()
        vcta = ovcta.vector
        vctb = ovctb.vector
        vctc = ovctc.vector
        scalar_triple_product = ovcta.scalar_triple_product(ovctb,ovctc)
        
        self.question = f"""Find the scalar triple product of {vcta}, {vctb}, and {vctc}"""
        self.answer = f"""{scalar_triple_product}"""
        
        if version == 1:
            self.question = f"""Find the volume of the parallelipiped formed by the three vectors {vcta}, {vctb}, and {vctc}"""
            volume = abs(scalar_triple_product)
            self.answer = f"""{volume}"""
        
class vector_triple_product:
    def __init__(self,**kwargs):
        try:
            version = kwargs['version']
        except:
            version = 0
            
        ovcta = vector()
        ovctb = vector()
        ovctc = vector()
        vcta = ovcta.vector
        vctb = ovctb.vector
        vctc = ovctc.vector
        vector_triple_product = ovcta.vector_triple_product(ovctb,ovctc).vector
        
        
        self.question = f"""Find the vector triple product of {vcta}, {vctb}, and {vctc}"""
        self.answer = f"""{vector_triple_product}"""
        
class gradient_of_a_scalar:
    def __init__(self,**kwargs):
        try:
            version = kwargs['version']
        except:
            version = 0
            
        scalar_object = scalar_field()
        gradient_vector_object = scalar_object.gradient()
        gradient_vector = gradient_vector_object.vector
        scalar = scalar_object.scalar
        
        self.question = f"""Find the gradient of the scalar field {scalar} = 0"""
        self.answer = f"""{gradient_vector}"""
        
        if version == 1:
            scalar_object = scalar_field()
            px, py, pz = scalar_object.pointOnScalar()
            scalar_gradient_vector_object = scalar_object.gradient(point=(px,py,pz))
            #print('gradient'+str(scalar_gradient_vector_object.vector))
            
            unit_vector_object = scalar_gradient_vector_object.normalize()
            
            unit_vector = unit_vector_object.vector
            unit_vector_p = sym.pretty(unit_vector)
            #print('unit vector'+str(unit_vector))
            
            self.question = f"""Find the unit vector normal to the surface {scalar} = 0 at the point ({px}, {py}, {pz})."""
            self.answer = f"""{unit_vector_p}"""
            
        if version == 2:
            scalar_object = scalar_field()
            px, py, pz = scalar_object.pointOnScalar()
            scalar_gradient_vector_object = scalar_object.gradient(point = (px,py,pz))
            normal_vector_object =  scalar_gradient_vector_object
            
            plane_object = plane(normal = normal_vector_object, point = (px,py,pz))
            plane_equation = plane_object.equation
            plane_equation_p = sym.pretty(plane_equation)
            
            
            self.question = f"""Find the equation of the plane tangent to the surface {scalar} = 0 at the point ({px}, {py}, {pz})."""
            self.answer = f"""{plane_equation_p}
... = 0"""   

        if version == 3:
            plane_object_1 = plane()
            plane_object_2 = plane()
            p1 = plane_object_1.equation
            p2 = plane_object_2.equation
            object_gradient1 = plane_object_1.normalvector
            object_gradient2 = plane_object_2.normalvector
            
            angle = math.acos((object_gradient1.dot(object_gradient2))/(object_gradient1.magnitude()*object_gradient2.magnitude()))*constants_conversions.RADIANS
            
            self.question = f"""Find the angle between the planes {p1} = 0 and {p2} = 0"""
            self.answer = f"""{angle} degrees"""

        if version == 4:
            scalarObject1 = scalar_field()
            s = scalarObject1.scalar
            px, py, pz = scalarObject1.pointOnScalar()
            gradientObject1 = scalarObject1.gradient(point = (px,py,pz))
            vectorObject = vector()
            v = vectorObject.vector
            unitVectorObject = vectorObject.normalize()
            directionalDerivative = gradientObject1.dot(unitVectorObject)
            
            self.question = f"""Find the directional derivative of {s} on the direction of {v} at the point ({px}, {py}, {pz})"""
            self.answer = f"""{directionalDerivative}"""
            
class divergence_of_a_vector:
    def __init__(self, **kwargs):
        
        vectorObject = vector(field = True)
        v = vectorObject.vector
        vp = sym.pretty(v)
        divergence = vectorObject.divergence()
        divergencep = sym.pretty(divergence)
        
        self.question = f"""Find the divergence of the vector field 
{vp}"""
        self.answer = f"""{divergencep}"""
        
class curl_of_a_vector:
    def __init__(self):
        vectorObject = vector(field = True)
        v = vectorObject.vector
        vp = sym.pretty(v)
        curlObject = vectorObject.curl()
        curl = curlObject.vector
        curlp = sym.pretty(curl)
        
        self.question = f"""Find the curl of the vector field
{vp}"""
        self.answer = f"""{curlp}"""
        
        
# class point_conversion:
    # def __init__(self, *args):
        # typeFrom = random.randint(1,3)
        # typeList = ('','cartesian','cylindrical','spherical')
        # point1 = analytic_geometry.pointInstance(type = typeList[typeFrom], dimensions = 3)
        # typeTo = random.randint(1,3)
        
        
        
            
    

        
        
        