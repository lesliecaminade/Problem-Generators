import sympy
import math
import random
from mathsub import analytic_geometry_engine
from generator import constants_conversions

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

def parse(string_input):
    return string_input.replace('**', '^').replace('*', ' ')

class vector: #custom vector
    def __init__(self,**kwargs):

        self.x = 0
        self.y = 0
        self.z = 0
        for key, value in kwargs.items():
            if key == 'x_comp':
                self.x = value
            if key == 'y_comp':
                self.y = value
            if key == 'z_comp':
                self.z = value
                
        self.vector = self.x *i + self.y *j + self.z *k

    def print(self, **kwargs):
        hide = None
        for key, value in kwargs.items():
            if key == 'hide':
                hide = value

        if hide == 'x':
            return f"""[(x)i + ({self.y})j + ({self.z})k]""" 
        elif hide == 'y':
            return f"""[({self.x})i + (y)j + ({self.z})k]""" 
        elif hide == 'z':
            return f"""[({self.x})i + ({self.y})j + (z)k]"""
        else:
            return f"""[({self.x})i + ({self.y})j + ({self.z})k]""" 

    def round(self, **kwargs):
        places = 2
        for key, value in kwargs.items():
            if key == 'places':
                places = value
        return vector(x_comp = round(self.x, places), y_comp = round(self.y, places), z_comp = round(self.z, places))

    def magnitude(self):
        try:
            mag = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        except:
            mag = sympy.sqrt(self.x**2 + self.y**2 + self.z**2)
        return mag
        
    def normalize(self):
        mag = self.magnitude()
        normx = self.x / mag
        normy = self.y / mag
        normz = self.z / mag
        return vector(x_comp = normx, y_comp = normy, z_comp = normz)

    def unit_vector(self):
        mag = self.magnitude()
        normx = self.x / mag
        normy = self.y / mag
        normz = self.z / mag
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


def random_vector(**kwargs):
    instances = 1
    for key, value in kwargs.items():
        if key == 'count':
            instances = value
    vectors = []

    if instances == 1:
        x_component = random.randint(-COMP_MAX, COMP_MAX)
        y_component = random.randint(-COMP_MAX, COMP_MAX)
        z_component = random.randint(-COMP_MAX, COMP_MAX)
        return vector(x_comp = x_component, y_comp = y_component, z_comp = z_component)
    else:
        for i in range(instances):
            x_component = random.randint(-COMP_MAX, COMP_MAX)
            y_component = random.randint(-COMP_MAX, COMP_MAX)
            z_component = random.randint(-COMP_MAX, COMP_MAX)
            vectors.append(vector(x_comp = x_component, y_comp = y_component, z_comp = z_component))
    return vectors

def random_vector_field():
    x_component = random_monomial()
    y_component = random_monomial()
    z_component = random_monomial()
    return vector(x_comp = x_component, y_comp = y_component, z_comp = z_component)

    
class Scalar_field:
    def __init__(self, *args):
        self.scalar = args[0]

    def print(self):
        return parse(f"""{self.scalar}""")
            
    def gradient(self):
        dx = sympy.diff(self.scalar, x)
        dy = sympy.diff(self.scalar, y)
        dz = sympy.diff(self.scalar, z)
        return vector(x_comp = dx, y_comp = dy, z_comp = dz)

def random_scalar_field():
    scalar = 0 * x
    for i in range(SCALAR_TERMS_MAX):
        scalar = scalar + random_monomial()
    return Scalar_field(scalar)



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
        
class Cross_product():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.cross_product = self.vector_1.cross(self.vector_2)

class Unit_vector_perpendicular_to_two_vectors():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.cross_product = self.vector_1.cross(self.vector_2)
        self.cross_product_unit_vector = self.cross_product.unit_vector()
         
class Unit_vector_perpendicular_to_two_vectors_with_magnitude():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.cross_product = self.vector_1.cross(self.vector_2)
        self.cross_product_unit_vector = self.cross_product.unit_vector()
        self.magnitude = random.randint(1, MAGNITUDE_MAX)
        self.vector_3 = self.cross_product_unit_vector.multiply(self.magnitude)
        
class Angle_between_two_vectors():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.dot = self.vector_1.dot(self.vector_2)
        self.angle = constants_conversions.angle(
                math.acos((self.dot) / (self.vector_1.magnitude() * self.vector_2.magnitude()))
            , 'radians')

class Orthogonal_vectors():
    def __init__(self):
        z_comp = 0
        while z_comp == 0:
            self.vector_1 = random_vector()
            z_comp = self.vector_1.z

        b_1 = coe()
        b_2 = coe()
        b_3 = ( - self.vector_1.x * b_1  - self.vector_1.y * b_2 ) / (self.vector_1.z)

        self.vector_2 = vector(x_comp = b_1, y_comp = b_2, z_comp = b_3 )

        dot = self.vector_1.dot(self.vector_2)
        if not (dot == 0):
            raise TypeError('vectors generated are not orthogonal')

class Component_of_a_vector():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.component = self.vector_1.component(self.vector_2)
        
class Projection_of_a_vector():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.component = self.vector_1.component(self.vector_2)  
        self.projection = self.vector_2.unit_vector().multiply(self.component)

class Scalar_triple_product():
    def __init__(self):
        self.vector_1 = random_vector()
        self.vector_2 = random_vector()
        self.vector_3 = random_vector()
        self.scalar_triple_product = self.vector_1.dot(self.vector_2.cross(self.vector_3))
      
class Vector_triple_product():
    def __init__(self):
        self.vector_1, self.vector_2, self.vector_3 = random_vector(count = 3)
        #A x (B x C)
        self.vector_triple_product = self.vector_1.cross(self.vector_2.cross(self.vector_3))

        
class Gradient_of_a_scalar():
    def __init__(self):
        self.scalar_1 = random_scalar_field()
        self.gradient = self.scalar_1.gradient()

            
class Divergence_of_a_vector():
    def __init__(self):
        self.vector = random_vector_field()
        self.divergence = self.vector.divergence()

        
class Curl_of_a_vector():
    def __init__(self):
        self.vector = random_vector_field()
        self.curl = self.vector.curl()
        
        
class Point_Conversion():
    def __init__(self):
        point = analytic_geometry_engine.Point_3_Dimensions()
        point.init_random()

        from_types = ['rectangular', 'cylindrical', 'spherical']
        to_types = ['rectangular', 'cylindrical', 'spherical']
        again = True
        while again:
            from_type = random.choice(from_types)
            to_type = random.choice(to_types)

            if not(to_type == from_type):
                again = False

        self.question = f"""Convert the point {point.types[from_type]} which is in {from_type} coordinates into its equivalent in {to_type} coordinates"""
        self.answer = f"""{point.types[to_type]}"""
        
        
        
            
    

        
        
        