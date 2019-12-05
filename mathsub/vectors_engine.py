import sympy
import math
import random
from mathsub import analytic_geometry_engine

x, y, z = sympy.symbols('x y z', real = True)
i, j, k = sympy.symbols('i j k', real = True)

COMP_MAX = 10
COE_MAX = 10
POW_MAX = 3
SCALAR_TERMS_MAX = 3
MAGNITUDE_MAX = 10

def coe():
    return random.randint(-COE_MAX, COE_MAX)

def pow():
    return random.randint(-POW_MAX, POW_MAX)

def random_monomial():
    return coe() * (x**pow()) * (y**pow()) * (z**pow())

class vector: #custom vector
    def __init__(self,**kwargs):

            for key, value in kwargs.items():
                if key == 'x_comp':
                    self.x = value
                if key == 'y_comp':
                    self.y = value
                if key == 'z_comp':
                    self.z = value
                    
            self.vector = self.x *i + self.y *j + self.z *k

    def print(self):
        return f"""[({self.x})i + ({self.y})j + ({self.z})k]""" 

    def round(self, **kwargs):
        places = 2
        for key, value in kwargs.items():
            if key == 'places':
                places = value
        return vector(x_comp = round(self.x, places), y_comp = round(self.y, places), z_comp = round(self.z, places))

    def magnitude(self):
        try:
            magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        except:
            magnitude = sympy.sqrt(self.x**2 + self.y**2 + self.z**2)
        
        self.magnitude = magnitude
        return magnitude
        
    def normalize(self):
        magnitude = self.magnitude()
        normx = self.x / magnitude
        normy = self.y / magnitude
        normz = self.z / magnitude
        return vector(x_comp = normx, y_comp = normy, z_comp = normz)

    def unit_vector(self):
        magnitude = self.magnitude()
        normx = self.x / magnitude
        normy = self.y / magnitude
        normz = self.z / magnitude
        return vector(x_comp = normx, y_comp = normy, z_comp = normz)
    
    def add(self,vector2):
        addx = self.x + vector2.x
        addy = self.y + vector2.y
        addz = self.z + vector2.z
        #add = addx*i + addy*j + addz*k
        return vector(x_comp = addx, y_comp = addy, z_comp = addz)
        
    def multiply(self,num):
        self.x = self.x * num
        self.y = self.y * num
        self.z = self.z * num
        self.vector = self.x*i + self.y*j + self.z*k
        return vector(x_comp = self.x, y_comp = self.y, z_comp = self.z)

    def subtract(self,vector2):
        addx = self.x - vector2.x
        addy = self.y - vector2.y
        addz = self.z - vector2.z
        #add = addx*i + addy*j + addz*k
        return vector(x_comp = addx, y_comp = addy, z_comp = addz)       
        
    def dot(self, vector2):
        dotx = self.x * vector2.x
        doty = self.y * vector2.y
        dotz = self.z * vector2.z
        return dotx + doty + dotz
        
    def cross(self,v2):
        #taking a cross product is not commutative
        #this method follows SELF X VECTOR2
        crossx = self.y*v2.z - self.z*v2.y
        crossy = self.z*v2.x - self.x*v2.z
        crossz = self.x*v2.y - self.y*v2.x
        return vector(x_comp = crossx, y_comp = crossy, z_comp = crossz)
        
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
        divx = sympy.diff(self.x, x)
        divy = sympy.diff(self.y, y)
        divz = sympy.diff(self.z, z)
        div = divx + divy + divz
        return div
        
    def curl(self):
        curlx = sympy.diff(self.z, y) - sympy.diff(self.y, z)
        curly = sympy.diff(self.x, z) - sympy.diff(self.z, x)
        curlz = sympy.diff(self.y, x) - sympy.diff(self.x, y)
        return vector(x_comp = curlx, y_comp = curly, z_comp = curlz)


def random_vector():
    x_component = random.randint(-COMP_MAX, COMP_MAX)
    y_component = random.randint(-COMP_MAX, COMP_MAX)
    z_component = random.randint(-COMP_MAX, COMP_MAX)
    return vector(x_comp = x_component, y_comp = y_component, z_comp = z_component)

def random_vector_field():
    x_component = random_monomial()
    y_component = random_monomial()
    z_component = random_monomial()
    return vector(x_comp = x_component, y_comp = y_component, z_comp = z_component)

    
class scalar_field:
    def __init__(self, *args):
        self.scalar = args[0]
            
    def gradient(self):
        dx = sympy.diff(self.scalar, x)
        dy = sympy.diff(self.scalar, y)
        dz = sympy.diff(self.scalar, z)
        return vector(x_comp = dx, y_comp = dy, z_comp = dz)
        
    def point(self):
        pointx = coe()
        pointy = coe()
        sc = self.scalar.subs(x, pointx)
        sc = sc.subs(y, pointy)
        
        pointz = sympy.solveset(sc , z, domain = sympy.Reals).args[0]

        point = analytic_geometry_engine.Point_3D()
        point.init_define(pointx, pointy, pointz)

class plane:
    def __init__(self, **kwargs):
    
        point = Point_3D()

        for key, value in kwargs.items():
            if key == 'normal_vector':
                normal_vector = value
            if key == 'point':
                point.init_define(value.x, value.y, value.z)
            
        equation_plane = normal_vector.x * (x - point.x) + normal_vector.y*(y - point.y) + normal_vector.z*(z - point.z)
            
        self.equation = equation_plane
        self.normalvector = vector(x_comp = normal_vector.x, y_comp = normal_vector.y, z_comp = normal_vector.z)
           
        
#-------------------------------------------------------------------

class Vector_add_vector_add_vector():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.vector_3 = random_vector()
        self.resultant = self.vector_1.add(self.vector_2.add(self.vector_3))

class Dot_product():
    def __init__ (self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.dot = self.vector_1.dot(self.vector_2)

#unit vector parallel to a vector 
class Unit_vector_parallel_to_a_vector():
    def __init__(self):
        self.vector_1 = random_vector()
        self.unit_vector = self.vector_1.unit_vector()
        self.unit_vector = self.unit_vector.round()

class Unit_vector_parallel_to_a_vector_with_magnitude():
    def __init__(self):
        self.vector_1 = random_vector()
        self.unit_vector = self.vector_1.unit_vector()
        self.length = random.randint(1, MAGNITUDE_MAX)
        self.resultant = self.unit_vector.multiply(self.length)
        
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

#unit vector perpendicular to two vectors
        
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
            unknown = sympy.solveset(dotexpr, x, domain = sympy.Reals).args[0]
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
            unit_vector_p = sympy.pretty(unit_vector)
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
            plane_equation_p = sympy.pretty(plane_equation)
            
            
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
        vp = sympy.pretty(v)
        divergence = vectorObject.divergence()
        divergencep = sympy.pretty(divergence)
        
        self.question = f"""Find the divergence of the vector field 
{vp}"""
        self.answer = f"""{divergencep}"""
        
class curl_of_a_vector:
    def __init__(self):
        vectorObject = vector(field = True)
        v = vectorObject.vector
        vp = sympy.pretty(v)
        curlObject = vectorObject.curl()
        curl = curlObject.vector
        curlp = sympy.pretty(curl)
        
        self.question = f"""Find the curl of the vector field
{vp}"""
        self.answer = f"""{curlp}"""
        
        
# class point_conversion:
    # def __init__(self, *args):
        # typeFrom = random.randint(1,3)
        # typeList = ('','cartesian','cylindrical','spherical')
        # point1 = analytic_geometry.pointInstance(type = typeList[typeFrom], dimensions = 3)
        # typeTo = random.randint(1,3)
        
        
        
            
    

        
        
        