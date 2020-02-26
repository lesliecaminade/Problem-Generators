from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import algebra_engine
from mathsub import analytic_geometry_engine

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

PIECEWISE_PARTS_MIN = 2
PIECEWISE_PARTS_MAX = 3

CONTINUOUS_PIECEWISE_TYPES_2_PARTS = ['line.line', 'parabola.line' ]

DISCONTINUOUS_PIECEWISE_TYPES = ['point', 'jump', 'removable', 'infinite', 'essential']

BIVARIATE_TYPES = ['random', 'conic section']

POS_INFINITY = 1e6
NEG_INFINITY = -1e6

X_RANGE = 10
Y_RANGE = 10

SLOPE_RANGE = 20

#product of two numbers
SUM_OF_NUMBERS_MAX = 500
SUM_OF_NUMBERS_MIN = 20

#paper with margins parameters
MARGIN_MAX = 50
MARGIN_MIN = 10
PAPER_AREA_MIN = 10000
PAPER_AREA_MAX = 20000

#ships moving at axis
SHIP_VELOCITY_MIN = 5
SHIP_VELOCITY_MAX = 20
B_DISTANCE_A_MIN = 40
B_DISTANCE_A_MAX = 80

#can minimum material
CAN_VOLUME_MAX = 300
CAN_VOLUME_MIN = 100

#car fuel consumption
CAR_FUEL_PHP_PER_HOUR_MIN = 10
CAR_FUEL_PHP_PER_HOUR_MAX = 40
CAR_OTHER_COST_MIN = 50
CAR_OTHER_COST_MAX = 200 
SPEED_MIN = 10
SPEED_MAX = 40

#man in rowboat
PA_DISTANCE_MIN = 4
PA_DISTANCE_MAX = 6
AB_DISTANCE_MIN = 5
AB_DISTANCE_MAX = 7
ROWSPEED_MIN = 1
ROWSPEED_MAX = 3
WALKPLUS = 2

#rectangular fencing
AREA_MIN = 20
AREA_MAX = 100

#wall and building and ladder
WALL_HEIGHT_MIN = 10
WALL_HEIGHT_MAX = 30
WALL_DISTANCE_MIN = 5
WALL_DISTANCE_MAX = 15

#choice creating function
def choice(number, *args, **kwargs):
    try:
        suffix = args[0]
    except:
        suffix = ''

    try:
        rounding_level = kwargs['round']
    except:
        rounding_level = 2

    new = round(random.gauss(number, 0.1 * number), rounding_level)
    if number%1 == 0:
        return f"""{int(new)} {suffix}"""
    else:
        return f"""{new} {suffix}"""


class ContinuousPiecewise():
    def __init__(self):
        pass

    def init_random(self, **kwargs):
        piecewise_type = None
        for key, value in kwargs.items():
            if key == 'parts':
                parts = value

            if key == 'type':
                piecewise_type = value

        if parts == 2:
            if piecewise_type == None:
                piecewise_type = random.choice(CONTINUOUS_PIECEWISE_TYPES_2_PARTS)


            if piecewise_type == 'line.line':
                slice_point = analytic_geometry_engine.Point()
                slice_point.init_random()

                part1 = analytic_geometry_engine.Line()
                part1.init_point_slope(slice_point, random.randint(-SLOPE_RANGE, SLOPE_RANGE))

                part2 = analytic_geometry_engine.Line()
                part2.init_point_slope(slice_point, random.randint(-SLOPE_RANGE, SLOPE_RANGE))

            if piecewise_type == 'parabola.line':
                part1 = analytic_geometry_engine.Parabola()

                part1.init_random(orientation = random.choice(['concave upward', 'concave downward']))

                slice_x = random.randint(-X_RANGE, X_RANGE)
                slice_point = analytic_geometry_engine.Point()
                slice_point.init_define(slice_x, part1.y_in_terms_of_x().subs(x, slice_x))

                part2 = analytic_geometry_engine.Line()
                part2.init_point_slope(slice_point, random.randint(-SLOPE_RANGE, SLOPE_RANGE))



            piecewise = sym.Piecewise(
                (part1.y_in_terms_of_x(), x < slice_point.x),
                (part2.y_in_terms_of_x(), x >= slice_point.x)
                )


        self.function = piecewise
        self.type = 'continuous'

class DiscontinuousPiecewise():
    def __init__(self, **kwargs):
        pass

class PointDiscontinuity(DiscontinuousPiecewise):
    def __init__(self):
        pass

    def init_random(self):
        root1 = random.randint(-X_RANGE, X_RANGE)
        root2 = random.randint(-X_RANGE, X_RANGE)

        numerator = sym.expand((x - root1) * (x - root2))
        denominator = (x - root1)

        self.function = sym.Mul(numerator, 1/denominator, evaluate = False)

        self.point_of_discontinuity = root1
        self.type = 'point discontinuity'

class JumpDiscontinuity(DiscontinuousPiecewise):
    def __init__(self):
        pass

    def init_random(self):
        tryagain = True
        while tryagain:
            try:
                slice_point_x = random.randint(-X_RANGE, X_RANGE)

                choices =[analytic_geometry_engine.Parabola(), analytic_geometry_engine.Line()]

                part1 = random.choice(choices)
                if type(part1) is analytic_geometry_engine.Line:
                    part1.init_random()
                if type(part1) is analytic_geometry_engine.Parabola:
                    part1.init_random(orientation = random.choice(['concave upward', 'concave downward']))

                choices = [analytic_geometry_engine.Parabola(), analytic_geometry_engine.Line()]

                part2 = random.choice(choices)
                
                if type(part2) is analytic_geometry_engine.Line:
                    part2.init_random()
                if type(part2) is analytic_geometry_engine.Parabola:
                    part2.init_random(orientation = random.choice(['concave upward', 'concave downward']))

                value_at_a_part1 = part1.y_in_terms_of_x().subs(x, slice_point_x)
                value_at_a_part2 = part2.y_in_terms_of_x().subs(x, slice_point_x)
                magnitude = abs(value_at_a_part1 - value_at_a_part2)

                self.function = sym.Piecewise(
                    (part1.y_in_terms_of_x(), x < slice_point_x),
                    (part2.y_in_terms_of_x(), x >= slice_point_x)
                    )

                self.point_of_discontinuity = slice_point_x
                self.type = 'jump discontinuity'
                self.magnitude = magnitude
                tryagain = False
            except:
                tryagain = True


class Derivative_explicit:
    def __init__(self):
        type1 = algebra_engine.Polynomial()
        type2 = algebra_engine.NegativePowerPolynomial()
        type3 = algebra_engine.PositiveFractionPowerPolynomial()
        type4 = algebra_engine.NegativeFractionPowerPolynomial()
        type5 = algebra_engine.MixedPowerPolynomial()
        type6 = algebra_engine.Rational()
        type7 = algebra_engine.Rational() #variation1


        type1.init_random()
        type2.init_random()
        type3.init_random()
        type4.init_random()
        type5.init_random()
        type6.init_random()
        type7.init_random()

        type8 = algebra_engine.ShortPolynomial().init_types('linear') * sym.sqrt(algebra_engine.ShortPolynomial().init_types('quadratic-constant'))

        choices = [type1.expression, type2.expression, type3.expression, type4.expression, type5.expression, type6.expression, type7.expression_variation_1, type8]

        self.function = random.choice(choices)
        self.function_string = f"""y = {self.function}"""

    def derivative(self, n = 1):
        self.derivative = sym.Derivative(self.function, x, n).doit()
        return self.derivative
    
    def derivative_unevaluated(self, n = 1):
        self.unevaluate_derivative = sym.Derivative(self.function, x, n)
        return self.unevaluate_derivative

class DerivativeExplicit_yofx_xoft_dydt():
    def __init__(self):
        pass

    def init_random(self):
        self.y_of_x = algebra_engine.ShortPolynomial().init_random()
        
        X_OF_T_CHOICES = [
        algebra_engine.random_coeff() * t **algebra_engine.random_positive_fraction() + algebra_engine.random_coeff()
        ]

        self.x_of_t = random.choice(X_OF_T_CHOICES)


        self.dydx = sym.Derivative(self.y_of_x, x).doit()
        self.dxdt = sym.Derivative(self.x_of_t, t).doit()

        self.dydt = self.dydx * (1/self.dxdt) 

        self.t = random.randint(1,9)
        self.x = self.x_of_t.subs(t, self.t)

        self.dydt_at_t = self.dydt.subs(t, self.t).subs(x, self.x)

        return f"""y(x) = {self.y_of_x}, x(t) = {self.x_of_t}, dydx = {self.dydx}, dxdt = {self.dxdt},dydt = {self.dydt}. (dydt = {self.dydt_at_t}at t = {self.t})"""

class DerivativeExplicit_xoft_yoft_dydx():
    def __init__(self):
        pass

    def init_random(self):
        self.y_of_t = algebra_engine.Polynomial().init_random().subs(x, t)
        self.x_of_t = algebra_engine.Polynomial().init_random().subs(x, t)

        self.dydt = sym.Derivative(self.y_of_t, t).doit()
        self.dxdt = sym.Derivative(self.x_of_t, t).doit()

        self.dydx = self.dydt * (1/self.dxdt)

        self.t = random.randint(1,9)

        self.dydx_at_t = self.dydx.subs(t, self.t)

        return f"""y(t) = {self.y_of_t}, x(t) = {self.x_of_t}, dydt = {self.dydt}, dxdt = {self.dxdt}, dydx = {self.dydx}, dydx(t = {self.t}) = {self.dydx_at_t}"""

class DerivativeImplicit_Bivariable():
    def __init__(self):
        self.expression = 0 * x

    def init_random(self):

        bivariable = algebra_engine.Bivariable()
        bivariate_type = random.choice(BIVARIATE_TYPES)
        if bivariate_type == 'random':
            bivariable.init_random()
        elif bivariate_type == 'conic section':
            bivariable.init_random_conic_section()
        else:
            raise InternalError('invalid conic section')


        self.expression = bivariable.expression
        self.dydx = sym.idiff(self.expression, y, x)

        return self.expression

class SecondDerivativeImplicit_Bivariable():
    def __init__(self):
        self.expression = 0 * x

    def init_random(self):

        bivariable = algebra_engine.Bivariable()
        
        if bivariate_type == 'random':
            bivariable.init_random()
        elif bivariate_type == 'conic section':
            bivariable.init_random_conic_section()
        else:
            raise InternalError('invalid conic section')


        self.expression = bivariable.expression
        self.dydx = sym.idiff(self.expression, y, x, n = 2)

        return self.expression

class TangentLine_from_ConicSection():
    def __init__(self):
        pass

    def init_random(self):
        #create any random conic section
        CONIC_SECTIONS = ['circle', 'ellipse', 'parabola', 'hyperbola']
        conic_section = random.choice(CONIC_SECTIONS)
        if conic_section == 'circle':
            self.conic_section = analytic_geometry_engine.Circle()
        elif conic_section == 'ellipse':
            self.conic_section = analytic_geometry_engine.Ellipse()
        elif conic_section == 'parabola':
            self.conic_section = analytic_geometry_engine.Parabola()
        elif conic_section == 'hyperbola':
            self.conic_section = analytic_geometry_engine.Hyperbola()
        else:
            raise InternalError('invalid conic section')

        self.conic_section.init_random()

        point_of_tangency = self.conic_section.point()

        tangent_line_slope = sym.idiff(self.conic_section.general, y, x)

        tangent_line_slope_at_point = tangent_line_slope.subs(x, point_of_tangency.x).subs(y, point_of_tangency.y)

        tangent_line = analytic_geometry_engine.Line()
        tangent_line.init_point_slope(point_of_tangency, tangent_line_slope_at_point)

        self.general = self.conic_section.general
        self.general_string = self.conic_section.general_string
        self.point_of_tangency = point_of_tangency
        self.tangent_line = tangent_line

class NormalLine_from_ConicSection():
    def __init__(self):
        pass

    def init_random(self):
        #create any random conic section
        CONIC_SECTIONS = ['circle', 'ellipse', 'parabola', 'hyperbola']
        conic_section = random.choice(CONIC_SECTIONS)
        if conic_section == 'circle':
            self.conic_section = analytic_geometry_engine.Circle()
        elif conic_section == 'ellipse':
            self.conic_section = analytic_geometry_engine.Ellipse()
        elif conic_section == 'parabola':
            self.conic_section = analytic_geometry_engine.Parabola()
        elif conic_section == 'hyperbola':
            self.conic_section = analytic_geometry_engine.Hyperbola()
        else:
            raise InternalError('invalid conic section')

        self.conic_section.init_random()

        point_of_tangency = self.conic_section.point()

        normal_line_slope = -1/sym.idiff(self.conic_section.general, y, x)

        normal_line_slope_at_point = normal_line_slope.subs(x, point_of_tangency.x).subs(y, point_of_tangency.y)

        normal_line = analytic_geometry_engine.Line()
        normal_line.init_point_slope(point_of_tangency, normal_line_slope_at_point)

        self.general = self.conic_section.general
        self.general_string = self.conic_section.general_string
        self.point_of_tangency = point_of_tangency
        self.normal_line = normal_line

class RelativeExtrema_Polynomials():
    def __init__(self):
        pass

    def init_random(self):
        tryagain = True
        while tryagain:
            try:
                self.polynomial = algebra_engine.Polynomial()
                self.polynomial.init_random()
                self.first_derivative = sym.Derivative(self.polynomial.expression, x).doit()
                self.second_derivative = sym.Derivative(self.polynomial.expression, x, x).doit()
                
                expression = self.polynomial.expression

                self.critical_numbers_list = list(sym.solveset(sym.Eq(self.first_derivative), x, domain=sym.S.Reals))

                self.inflection_list = list(sym.solveset(sym.Eq(self.second_derivative,0), x, domain=sym.S.Reals))
          

                self.critical_points = []
                self.inflection_points = []
                self.relative_maxima = []
                self.relative_minima = []

                for x_value in self.critical_numbers_list:
                    point = analytic_geometry_engine.Point()
                    point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
                    point.round(2)
                    self.critical_points.append(point)

                for x_value in self.inflection_list:
                    point = analytic_geometry_engine.Point()
                    point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
                    point.round(2)
                    self.inflection_points.append(point)

                for x_value in self.critical_numbers_list:
                    point = analytic_geometry_engine.Point()
                    point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
                    point.round(2)
                    second_derivative_check = sym.Derivative(expression, x, x).doit().subs(x, x_value)
                    if second_derivative_check < 0:
                        self.relative_maxima.append(point)

                for x_value in self.critical_numbers_list:
                    point = analytic_geometry_engine.Point()
                    point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
                    point.round(2)
                    second_derivative_check = sym.Derivative(expression, x, x).doit().subs(x, x_value)
                    if second_derivative_check > 0:
                        self.relative_minima.append(point)

          

                #find the interval which the polynomial is increasing
                self.interval_increasing = sym.solveset(self.first_derivative > 0, x, domain = sym.S.Reals)

                #find the interval which the polynomial is decreasing
                self.interval_decreasing = sym.solveset(self.first_derivative < 0, x, domain = sym.S.Reals)
                tryagain = False
            except:
                pass

class RelativeExtrema():
    def __init__(self):
        pass

    def init_define(self, expression, a, b):
        #a - lower interval for absolute extrema
        #b - upper interval for absolute extrema

        self.first_derivative = sym.Derivative(expression, x).doit()
        self.second_derivative = sym.Derivative(expression, x, x).doit()
        

        self.critical_numbers_list = list(sym.solveset(sym.Eq(self.first_derivative, 0), x, domain = sym.S.Reals))

        self.inflection_list = list(sym.solveset(sym.Eq(self.second_derivative), x, domain = sym.S.Reals))
  

        self.critical_points = []
        self.inflection_points = []
        self.relative_maxima = []
        self.relative_minima = []

        self.critical_numbers_interval = []
        self.critical_points_interval = []
        self.relative_maxima_interval = []
        self.relative_minima_interval = []


        for x_value in self.critical_numbers_list:
            point = analytic_geometry_engine.Point()
            point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
            point.round(2)
            self.critical_points.append(point)

        for x_value in self.inflection_list:
            point = analytic_geometry_engine.Point()
            point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
            point.round(2)
            self.inflection_points.append(point)

        for x_value in self.critical_numbers_list:
            point = analytic_geometry_engine.Point()
            point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
            point.round(2)
            second_derivative_check = sym.Derivative(expression, x, x).doit().subs(x, x_value)
            if second_derivative_check < 0:
                self.relative_maxima.append(point)

        for x_value in self.critical_numbers_list:
            point = analytic_geometry_engine.Point()
            point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
            point.round(2)
            second_derivative_check = sym.Derivative(expression, x, x).doit().subs(x, x_value)
            if second_derivative_check > 0:
                self.relative_minima.append(point)

        for x_value in self.critical_numbers_list:
           if a < x_value < b:
                self.critical_numbers_interval.append(x_value)
                point = analytic_geometry_engine.Point()
                point.init_define(x_value, self.first_derivative.subs(x, x_value))
                self.critical_points_interval.append(point)


        for x_value in self.critical_numbers_interval:
            point = analytic_geometry_engine.Point()
            point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
            point.round(2)
            second_derivative_check = self.second_derivative.subs(x, x_value)
            if second_derivative_check < 0:
                self.relative_maxima_interval.append(point)

        for x_value in self.critical_numbers_interval:
            point = analytic_geometry_engine.Point()
            point.init_define(x_value.evalf(), expression.subs(x, x_value).evalf())
            point.round(2)
            second_derivative_check = self.second_derivative.subs(x, x_value)
            if second_derivative_check > 0:
                self.relative_minima_interval.append(point)


        #find the interval which the polynomial is increasing
        self.interval_increasing = sym.solveset(self.first_derivative > 0, x, domain = sym.S.Reals)

        #find the interval which the polynomial is decreasing
        self.interval_decreasing = sym.solveset(self.first_derivative < 0, x, domain = sym.S.Reals)


class AbsoluteExtrema():
    def __init__(self):
        pass

    def init_define(self, expression, a, b):
        #a - lower interval for absolute extrema
        #b - upper interval for absolute extrema

        first_derivative = sym.Derivative(expression, x).doit()

        critical_numbers = sym.solveset(first_derivative, x, domain = sym.S.Reals)

        print(critical_numbers)
        
        f_of_a = expression.subs(x, a)
        f_of_b = expression.subs(x, b)

        points = []

        points.append((a, f_of_a))
        points.append((b, f_of_b))

        for i in range(len(critical_numbers)):
            if a < critical_numbers.args[i] < b:
                points.append((critical_numbers.args[i], expression.subs(x, critical_numbers.args[i])))

        y_values = []
        x_values = []

        for i in range(len(points)):
            if sym.sympify(points[i][0]).is_real and sym.sympify(points[i][1]).is_real:
                x_values.append(points[i][0])
                y_values.append(points[i][1])

        # print(points)
        # print(x_values)
        # print(y_values)

        max_y = max(y_values)

        for i in range(len(points)):
            if points[i][1] == max_y:
                x_of_max_y = points[i][0]

        self.absolute_maxima = analytic_geometry_engine.Point()
        self.absolute_maxima.init_define(x_of_max_y, max_y)

        y_values = []
        x_values = []

        for i in range(len(points)):
            if sym.sympify(points[i][0]).is_real and sym.sympify(points[i][1]).is_real:
                x_values.append(points[i][0])
                y_values.append(points[i][1])

        min_y = min(y_values)

        for i in range(len(points)):
            if points[i][1] == min_y:
                x_of_min_y = points[i][0]

        self.absolute_minima = analytic_geometry_engine.Point()
        self.absolute_minima.init_define(x_of_min_y, min_y)

class ProductOfTwoNumbers_x_y():
    def __init__(self):
        pass

    def init_random(self):

        self.sum_of_numbers = random.randint(SUM_OF_NUMBERS_MIN, SUM_OF_NUMBERS_MAX)

        maxima_expression = x * ( self.sum_of_numbers - x )

        relative_extrema = AbsoluteExtrema()
        relative_extrema.init_define(maxima_expression, 0, self.sum_of_numbers)

        self.maxima = relative_extrema.absolute_maxima
        self.number1 = self.maxima.x
        self.number2 = self.sum_of_numbers - self.number1

class ProductOfTwoNumbers_xsquared_y():
    def __init__(self):
        pass

    def init_random(self):

        self.sum_of_numbers = random.randint(SUM_OF_NUMBERS_MIN, SUM_OF_NUMBERS_MAX)

        maxima_expression = x**2 * ( self.sum_of_numbers - x )

        relative_extrema = AbsoluteExtrema()
        relative_extrema.init_define(maxima_expression, 0, self.sum_of_numbers)

        self.maxima = relative_extrema.absolute_maxima
        self.number1 = self.maxima.x
        self.number2 = self.sum_of_numbers - self.number1

class PaperWithMargins():
    def __init__(self):
        pass
    def init_random(self):
        self.area = random.randint(PAPER_AREA_MIN, PAPER_AREA_MAX)
        area = PAPER_AREA_MAX + 1

        while area > self.area:
            self.margin_length_one_side = random.randint(MARGIN_MIN, MARGIN_MAX)
            self.margin_width_one_side = random.randint(MARGIN_MIN, MARGIN_MAX)
            area = self.margin_length_one_side * self.margin_width_one_side



        maxima_expression = (x - 2 * self.margin_length_one_side) * ((self.area/x) -  2 * self.margin_width_one_side)

        relative_extrema = AbsoluteExtrema()
        relative_extrema.init_define(maxima_expression, 0, PAPER_AREA_MAX)

        self.maxima = relative_extrema.absolute_maxima
        self.length = self.maxima.x
        self.width = self.area / self.length

class MovingAtAxis():
    def __init__(self):
        pass

    def init_random(self):
        #A is initially at origin moving south
        #B is at east at a certain distance moving towards the origin

        A_velocity = random.randint(SHIP_VELOCITY_MIN, SHIP_VELOCITY_MAX)
        B_velocity = random.randint(SHIP_VELOCITY_MIN, SHIP_VELOCITY_MAX)

        B_initial_distance_from_A = random.randint(B_DISTANCE_A_MIN, B_DISTANCE_A_MAX)

        distance = (A_velocity*x)**2 + (B_initial_distance_from_A - B_velocity*x)**2

        maxima_minima = AbsoluteExtrema()
        maxima_minima.init_define(distance, 0, POS_INFINITY)

        minima = maxima_minima.absolute_minima
        time_nearest = minima.x
        distance_nearest = math.sqrt(minima.y)

        self.A_velocity = A_velocity
        self.B_velocity = B_velocity
        self.B_initial_distance_from_A = B_initial_distance_from_A
        self.time_nearest = time_nearest
        self.distance_nearest = distance_nearest

class CanWithMinimumArea_Open():
    def __init__(self):
        pass

    def init_random(self):

        volume = random.randint(CAN_VOLUME_MIN, CAN_VOLUME_MAX)

        area_equation = 2 * sym.pi * x  * (volume/(sym.pi * x**2)) + sym.pi * x**2

        minima_maxima = AbsoluteExtrema()
        minima_maxima.init_define(area_equation, 0, POS_INFINITY)

        minima = minima_maxima.absolute_minima
        area_smallest = minima.y
        radius = minima.x
        height = volume / (math.pi * radius**2 )

        self.volume = volume
        self.area_smallest = area_smallest
        self.radius = radius
        self.height = height


class CanWithMinimumArea_Closed():
    def __init__(self):
        pass

    def init_random(self):

        volume = random.randint(CAN_VOLUME_MIN, CAN_VOLUME_MAX)

        area_equation = 2 * sym.pi * x  * (volume/(sym.pi * x**2)) + 2 * sym.pi * x**2

        minima_maxima = AbsoluteExtrema()
        minima_maxima.init_define(area_equation, 0, POS_INFINITY)

        minima = minima_maxima.absolute_minima
        area_smallest = minima.y
        radius = minima.x
        height = volume / (math.pi * radius**2 )

        self.volume = volume
        self.area_smallest = area_smallest
        self.radius = radius
        self.height = height


class Manufacturing():

    def __init__(self):
        pass

    def init_random(self):

        cost_function = sym.Rational(1,random.randint(5,20)) * x**2 + algebra_engine.random_positive_coeff() * x + algebra_engine.random_coeff()

        price_function = random.randint(1,9) - (sym.Rational(1, random.randint(20,50))) * x

        profit_function = cost_function * price_function

        maxima_minima = AbsoluteExtrema()
        maxima_minima.init_define(profit_function, 0, POS_INFINITY)

        maxima = maxima_minima.absolute_maxima
        profit_max = maxima.y
        items_at_profit_max = maxima.x

        self.cost_function = cost_function
        self.price_function = price_function
        self.items_at_profit_max = math.floor(items_at_profit_max)
        self.profit_max = profit_function.subs(x, self.items_at_profit_max)


class ManInRowBoat():

    def __init__(self):
        pass

    def init_random(self):

        #P is the point in the middle of the sea
        #A is the point where a line drawn from P to A is perpendicular to the shore
        #B is the destination along the shoreline 

        PA_distance = random.randint(PA_DISTANCE_MIN, PA_DISTANCE_MAX)
        AB_distance = random.randint(AB_DISTANCE_MIN, AB_DISTANCE_MAX)

        row_speed = random.randint(ROWSPEED_MIN, ROWSPEED_MAX)
        walk_speed = row_speed + WALKPLUS

        time_equation = sym.sqrt(PA_distance**2 + x**2)/row_speed + (AB_distance - x)/walk_speed

        difcal = AbsoluteExtrema()
        difcal.init_define(time_equation, 0, AB_distance)

        minima = difcal.absolute_minima

        time_smallest = minima.y
        distance_for_smallest_time = minima.x

        self.PA_distance = PA_distance
        self.AB_distance = AB_distance
        self.row_speed = row_speed
        self.walk_speed = walk_speed
        self.time_smallest = time_smallest
        self.distance_at_time_smallest = distance_for_smallest_time


class RectangularFence():
    def __init__(self):
        pass

    def init_random(self):

        self.area = random.randint(AREA_MIN, AREA_MAX)

        fencing_equation = x + 2*(self.area/x)

        difcal = AbsoluteExtrema()
        difcal.init_define(fencing_equation, 0, POS_INFINITY)

        minima = difcal.absolute_minima
        self.perimeter = minima.y
        self.width = minima.x

class WallAndBuilding():
    def __init__(self):
        pass

    def init_random(self):

        wall_height = random.randint(WALL_HEIGHT_MIN, WALL_HEIGHT_MAX)
        wall_distance = random.randint(WALL_DISTANCE_MIN, WALL_DISTANCE_MAX)

        length_function = ( x + wall_distance)**2 + ((wall_height*(x + wall_distance))/(x))

        dif = AbsoluteExtrema()
        dif.init_define(length_function, 0, POS_INFINITY)

        minima = dif.absolute_minima

        self.beam_length = math.sqrt(minima.y)
        self.beam_distance_from_wall = minima.x
        self.wall_height = wall_height
        self.wall_distance = wall_distance


#direct copy questions


class besavilla_1():
    def __init__(self):
        
        choice_a = '15.7 cm3 #' 
        choice_b = choice(15.7, 'cm2', round = 1)
        choice_c = choice(15.7, 'cm2', round = 1)
        choice_d = choice(15.7, 'cm2', round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Using differentials, determine the appropriate increase in the volume of a sphere if the radius increases from 5 cm to 5.05 cm."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_2():
    def __init__(self):
        
        choice_a = '5.03 cm2 #'
        choice_b = choice(5.03, 'cm2')
        choice_c = choice(5.03, 'cm2')
        choice_d = choice(5.03, 'cm2')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Using differentials, determine the appropriate increase in the surface area of a sphere if the radius increases from  4 cm to 4.05 cm"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_3():
    def __init__(self):
        
        choice_a = '0.20 #'
        choice_b = choice(0.20)
        choice_c = choice(0.20)
        choice_d = choice(0.20)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""If y = x^(5/2), what is the approximate change in y when x changes from 4 to 4.01?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_4():
    def __init__(self):
        
        choice_a = '0.027 #'
        choice_b = choice(0.027, round = 3 )
        choice_c = choice(0.027, round = 3 )
        choice_d = choice(0.027, round = 3 )
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""If y = x^(4/3), what is the approximate change in y when x changes from 8 to 8.01?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_5():
    def __init__(self):
        
        choice_a = '0.227 #'
        choice_b = choice(0.227)
        choice_c = choice(0.227)
        choice_d = choice(0.227)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""If h = 65 tan(theta), what is the approximate change in h when theta changes from 60 degrees to 60 degrees and 3 minutes?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_6():
    def __init__(self):
        
        choice_a = '2545 cm3 #'
        choice_b = choice(2545, 'cm3', round = 0)
        choice_c = choice(2545, 'cm3', round = 0)
        choice_d = choice(2545, 'cm3', round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A diameter of a spere can be measured with a max.error of 0.2 cm. Find the corresponding error in the volume of a sphere whose diameter is 90 cm."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_7():
    def __init__(self):
        
        choice_a = '2.36 cm2 #'
        choice_b = choice(2.36, 'cm2')
        choice_c = choice(2.36, 'cm2')
        choice_d = choice(2.36, 'cm2')
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The radius of a circle can be measured with an allowable error of 0.01 cm. Determine the corresponding error in the area of a circle with a diameter of 75 cm."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_8():
    def __init__(self):
        
        choice_a = '2430 cm3 #'
        choice_b = choice(2430, 'cm3', round = 0)
        choice_c = choice(2430, 'cm3', round = 0)
        choice_d = choice(2430, 'cm3', round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The allowable error in the measurement of the edge of a cubical box is 1 mm. What is the corresponding error in the volume of a cubical box whose edge is 90 cm?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_9():
    def __init__(self):
        
        choice_a = '151 cm2 #'
        choice_b = choice(151, 'cm2', round = 0)
        choice_c = choice(151, 'cm2', round = 0)
        choice_d = choice(151, 'cm2', round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The allowable error in the measurement of the radius of a sphere is 1 mm. Find the corresponding error in the surface area of a sphere whose radius is 60 cm."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_10():
    def __init__(self):
        
        choice_a = '240 cm2 #'
        choice_b = choice(240, 'cm2', round = 0)
        choice_c = choice(240, 'cm2', round = 0)
        choice_d = choice(240, 'cm2', round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The edge of a cubical box can be measured with an allowable error of 2 mm. What is the corresponding error in the total surface area of the cubical box whose edge is 1 meter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class first_derivative():
    def __init__(self):

        question_answer = {
        """y = 3^(3x)""":"""y' = 3 ln(3) (3x)""",
        """y = 2 x^(x)""":"""y' = 4 x^(x) ( 1 + ln(x))""",
        """y = ln e^(2x)""":"""y' = 1/x""",
        """y = 5^x""":"""y' = ln(5) 5^x""",
        """y = 3^(2x)""":"""y' = 2 ln(3) 3^(2x)""",
        """y = 2 e^(x^3)""":"""y' = 6 x^2 e^(x^3)""",
        """y = 1.76 e^(x^4)""":"""y' = 7.04 x^3 e^(x^4)""",
        """y = 2.16 e^(sin (2x))""":"""y' = 4.32 cos(2x) e^(sin(2x))""",
        """y = 3^x e^x""":"""y' = 2.10 e^x 3^x""",
        """y = 5^x e^x""":"""y' = 2.61 e^x 5^x""",
        """y = 2e^x 8^x""":"""y' = 6.16 e^x 8^x""",
        """y = 2 cos(2 + x^3)""":"""y' = - 6x^2 sin (2 + x^3)""",
        """y = 2 sin^2(x^2 + 1)""":"""y' = 8x sin(x^2 + 1) cos(x^2 + 1)""",
        """y = 2 tan(1 + x^3)""":"""y' = 6x^2 sec^2(1 + x^3)""",
        """y = 2 sec(x^2 + 1)""":"""y' = 4x sec(x^2 + 1) tan(x^2 + 1)""",
        """y = tan^2(x^2 + 1)""":"""y' = 4x tan(x^2 + 1) sec^2(x^2 + 1)""",
        """y = arccsc(4x)""":"""y' = -1 / (x sqrt(16 x^2 - 1))""",
        """y = arcsec(2x)""":"""y' = 1 / (x sqrt(4x^2 - 1))""",
        """y = arcsin(x/2)""":"""y' = 1 / sqrt(4 - x^2)""",
        """y = arcsin(3x)""":"""y' = 3 / sqrt(1 - 9x^2)""",
        """y = arccos(4x)""":"""y' = -4 / sqrt(1 - 16x^2)""",
        """y = arctan(5x)""":"""y' = 5 / (1 + 25x^2)""",
        """y = arccot(3x)""":"""y' = -3 / (1 + 9x^2)""",
        """y = arccos(x/3)""":"""y' = -1 / sqrt(9 - x^2)""",
        """y = arctan(x/4)""":"""y' = 4 / (16 + x^2)""",
        """y = arccot(x/2)""":"""y' = -2 / (4 + x^2)"""
        }

        zeroth_derivative = random.choice(list(question_answer.keys()))
        self.question = f"""What is the first derivative of {zeroth_derivative}?"""
        self.answer = f"""{question_answer[zeroth_derivative]}"""

class besavilla_37():
    def __init__(self):
        
        choice_a = '1.75 #'
        choice_b = choice(1.75)
        choice_c = choice(1.75)
        choice_d = choice(1.75)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = (t + 1)^2 + sqrt(t) when t = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_38():
    def __init__(self):
        
        choice_a = '5 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = (t + 1)^2 sqrt(t) when t = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_39():
    def __init__(self):
        
        choice_a = '2.25 #'
        choice_b = choice(2.25)
        choice_c = choice(2.25)
        choice_d = choice(2.25)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = (t + 1)^2 - sqrt(t) when t = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_40():
    def __init__(self):
        
        choice_a = '18 #'
        choice_b = choice(18, round = 0)
        choice_c = choice(18, round = 0)
        choice_d = choice(18, round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = x + (x + 2)^3 when x = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_41():
    def __init__(self):
        
        choice_a = '- 0.125 #'
        choice_b = choice(-0.125, round = 3)
        choice_c = choice(-0.125, round = 3)
        choice_d = choice(-0.125, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = x / (x + 1)^2 when x = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_42():
    def __init__(self):
        
        choice_a = '36 #'
        choice_b = choice(36, round = 0)
        choice_c = choice(36, round = 0)
        choice_d = choice(36, round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = x(x + 1)^3 when x = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_43():
    def __init__(self):
        
        choice_a = '0.375 #'
        choice_b = choice(0.375, round = 3)
        choice_c = choice(0.375, round = 3)
        choice_d = choice(0.375, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = x-2 when x = 2"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_44():
    def __init__(self):
        
        choice_a = '0.088 #'
        choice_b = choice(0.088, round = 3)
        choice_c = choice(0.088, round = 3)
        choice_d = choice(0.088, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the second derivative of y = x^(-1/3) when x = 2"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_45():
    def __init__(self):
        
        choice_a = '-6 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the slope of the curve y = (1 - 2x)^3 at (1, -1)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_46():
    def __init__(self):
        
        choice_a = '-10 #'
        choice_b = random.randint(-10, 10)
        choice_c = random.randint(-10, 10)
        choice_d = random.randint(-10, 10)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the slope of the curve y = (1 - 5x)^6 / 3   at (3, 1/3)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_47():
    def __init__(self):
        
        choice_a = '1.5 #'
        choice_b = choice(1.5, round = 1)
        choice_c = choice(1.5, round = 1)
        choice_d = choice(1.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the slope of the curve y = 6(4 + x)^(1/2) at (0, 12)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_48():
    def __init__(self):
        
        choice_a = '28 #'
        choice_b = random.randint(-30, 30)
        choice_c = random.randint(-30, 30)
        choice_d = random.randint(-30, 30)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the slope of the curve y = x^2 (x + 1)^3 at (1, 8)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_49():
    def __init__(self):
        
        choice_a = '3 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the slope of the curve y = ( 1 - 2x)^2 / x  at (1, 1)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_50():
    def __init__(self):
        
        choice_a = '(2, 3) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""At what point does the curve x^2 - 2x + y - 3 = 0 have a slope of 2?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_51():
    def __init__(self):
        
        choice_a = '(1, 4) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""At what point does the curve 3x^2 - 7x + y = 0 have a slope of 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_52():
    def __init__(self):
        
        choice_a = '(3, 0) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""At what point does the curve x^3 - 9x - y = 0 have a slope of 18?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_53():
    def __init__(self):
        
        choice_a = '(0, 0) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""At what point does the curve x^2 - 2x + y = 0 have a slope of 2?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_54():
    def __init__(self):
        
        choice_a = '(2, 2/3) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""At what point does the curve x^3 - 3x - 3y = 0 have a slope of 3?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_55():
    def __init__(self):
        
        choice_a = '2 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the slope of the tangent to the curve y = 2 ln(x) at the point where x = 1"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_56():
    def __init__(self):
        
        choice_a = '4 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the slope of the tangent to the curve y = 4 e^x at (0, 4)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_57():
    def __init__(self):
        
        choice_a = '0.5 #'
        choice_b = choice(0.5, round = 1)
        choice_c = choice(0.5, round = 1)
        choice_d = choice(0.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the slope of the tangent to the curve y = ln(2x) at the point where x = 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_58():
    def __init__(self):
        
        choice_a = '6 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the slope of the tangent line to the curve y = 3 e^(2x) at (0, 3)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_59():
    def __init__(self):
        
        choice_a = '3 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the slope of the tangent to the curve y = 3 ln(3x) at the point where abcissa is 1?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_60():
    def __init__(self):
        
        choice_a = '4 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the slope of the tangent to the curve y = e^(4x) at the point where x = 0?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_61():
    def __init__(self):
        
        choice_a = '(2, -6) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the point of inflection of the curve y = x^3 - 6x^2 - x + 12."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_62():
    def __init__(self):
        
        choice_a = '(2, 3) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the point of inflection of the curve y = (6x^2 - x^3 + 5) / 7  """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_63():
    def __init__(self):
        
        choice_a = '3 #'
        choice_b = random.randint(-9,9)
        choice_c = random.randint(-9,9)
        choice_d = random.randint(-9,9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""If y = ax^3 + bx^2 and its point of inflection is at (2, 8), what is the value of b?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_64():
    def __init__(self):
        
        choice_a = '-0.25 #'
        choice_b = choice(-0.25, round = 2)
        choice_c = choice(-0.25, round = 2)
        choice_d = choice(-0.25, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""If y = ax^3 + bx^2 and its point of inflection is at (2, 4), what is the value of a?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_65():
    def __init__(self):
        
        choice_a = '(2, -3) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Locate the point of inflection of the curve y = 2x^3 - 12 x^2 - 3x + 35"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_66():
    def __init__(self):
        
        choice_a = '1 #'
        choice_b = '- 1'
        choice_c = '0'
        choice_d = 'infinity'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of sin(theta) / theta as theta approaches 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_67():
    def __init__(self):
        
        choice_a = '0.67 #'
        choice_b = round(random.randint(-99, 99)/100,2)
        choice_c = round(random.randint(-99, 99)/100,2)
        choice_d = round(random.randint(-99, 99)/100,2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (4x - 1) / 6x as x approaches 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_68():
    def __init__(self):
        
        choice_a = '0.5 #'
        choice_b = round(random.randint(-9, 9)/10,1)
        choice_c = round(random.randint(-9, 9)/10,1)
        choice_d = round(random.randint(-9, 9)/10,1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (cos(x) - 1) / (1 - sec^2(x)) as x approaches zero."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_69():
    def __init__(self):
        
        choice_a = '0.5 #'
        choice_b = round(random.randint(-9, 9)/10,1)
        choice_c = round(random.randint(-9, 9)/10,1)
        choice_d = round(random.randint(-9, 9)/10,1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x + tan(x)) / (sin(4x)) as x approaches zero."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_70():
    def __init__(self):
        
        choice_a = '0.4 #'
        choice_b = round(random.randint(-9, 9)/10,1)
        choice_c = round(random.randint(-9, 9)/10,1)
        choice_d = round(random.randint(-9, 9)/10,1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 - 1) / (x^2 + 3x - 9 ) as x approaches 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_71():
    def __init__(self):
        
        choice_a = 'inifinity #'
        choice_b = '1'
        choice_c = '0'
        choice_d = '-1'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 + 4) / (x - 4) as x approaches infinity."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_72():
    def __init__(self):
        
        choice_a = '0.1429 #'
        choice_b = choice(0.1429, round = 4)
        choice_c = choice(0.1429, round = 4)
        choice_d = choice(0.1429, round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x - 4) / (x^2 - x - 12)  as x approaches 4."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_73():
    def __init__(self):
        
        choice_a = '0.67 #'
        choice_b = choice(0.67, round= 2)
        choice_c = choice(0.67, round= 2)
        choice_d = choice(0.67, round= 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 + 4) / (x^2 + 2x - 8) as x approaches 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_74():
    def __init__(self):
        
        choice_a = '0.5 #'
        choice_b = random.randint(-9, 9) / 10
        choice_c = random.randint(-9, 9) / 10
        choice_d = random.randint(-9, 9) / 10
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (1 - cos(x)) / x^2 as x approaches zero."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_75():
    def __init__(self):
        
        choice_a = 'infinity #'
        choice_b = '1'
        choice_c = '0'
        choice_d = '-1'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the limit of sin(2x) / x^2 as x approaches zero?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_76():
    def __init__(self):
        
        choice_a = '0 #'
        choice_b = '1'
        choice_c = '-1'
        choice_d = 'infinity'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the limit of (1 - cos(2x)) / x as x approaches zero?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_77():
    def __init__(self):
        
        choice_a = 'infinity #'
        choice_b = '0'
        choice_c = '1'
        choice_d = '-1'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the limit of (1 - cos(x))/x^3 as x approaches zero?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_78():
    def __init__(self):
        
        choice_a = '0 #'
        choice_b = 'infinity'
        choice_c = '1'
        choice_d = '- 1'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the limit of (x - sin(x)) / x^2 as x approaches zero?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_79():
    def __init__(self):
        
        choice_a = '-5 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the limit of (x^3 + 2x^2 - 3) / (1 - x^2) as x approaches 1?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_80():
    def __init__(self):
        
        choice_a = '0.67 #'
        choice_b = choice(0.67, round = 2)
        choice_c = choice(0.67, round = 2)
        choice_d = choice(0.67, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit (2x^2 - x) / (3x^2 + 4) as x approaches infinity."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_81():
    def __init__(self):
        
        choice_a = '0.5833 #'
        choice_b = choice(0.5833, round = 4)
        choice_c = choice(0.5833, round = 4)
        choice_d = choice(0.5833, round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (4x - 1) / 6x as x approaches 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_82():
    def __init__(self):
        
        choice_a = '0 #'
        choice_b = '1'
        choice_c = '-1 '
        choice_d = 'infinity'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (sin(x) - x) / (x - tan(x)) as x approaches zero."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_83():
    def __init__(self):
        
        choice_a = '0 #'
        choice_b = '1'
        choice_c = '-1 '
        choice_d = 'infinity'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (sin(x) - x) / tan^3(x) as x approaches 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_84():
    def __init__(self):
        
        choice_a = '-0.75 #'
        choice_b = choice(-0.75, round = 2)
        choice_c = choice(-0.75, round = 2)
        choice_d = choice(-0.75, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^3 - 9x + 10) / (x^2 - 4) as x approaches 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_85():
    def __init__(self):
        
        choice_a = '3 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^3 - 9x + 10) / (x - 2) as x approaches 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_86():
    def __init__(self):
        
        choice_a = '0.4 #'
        choice_b = choice(0.4, round = 1)
        choice_c = choice(0.4, round = 1)
        choice_d = choice(0.4, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 - 1) / (x^2 + 3x + 9) as x approaches 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_87():
    def __init__(self):
        
        choice_a = '0.5 #'
        choice_b = choice(0.5, round= 1)
        choice_c = choice(0.5, round= 1)
        choice_d = choice(0.5, round= 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x - 2)^(0.5) / (x^2 - 4)^(0.5) as x approaches 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_88():
    def __init__(self):
        
        choice_a = '-3 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 + 4x - 5) / (x^2 - 4x + 3) as x approaches 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_89():
    def __init__(self):
        
        choice_a = '1.5 #'
        choice_b = choice(1.5, round = 1)
        choice_c = choice(1.5, round = 1)
        choice_d = choice(1.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit (1 - x^3) / (1 - x^2) as x approaches 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_90():
    def __init__(self):
        
        choice_a = '2.5 #'
        choice_b = choice(2.5, round = 1)
        choice_c = choice(2.5, round = 1)
        choice_d = choice(2.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 + 3x - 4) / (x^2 - 1) as x approaches 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_91():
    def __init__(self):
        
        choice_a = '1.33 #'
        choice_b = choice(1.33, round = 2)
        choice_c = choice(1.33, round = 2)
        choice_d = choice(1.33, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (x^2 - 4) / (x^3 - 9x + 10) as x approaches 2."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_92():
    def __init__(self):
        
        choice_a = '0.67 #'
        choice_b = choice(0.67, round = 2)
        choice_c = choice(0.67, round = 2)
        choice_d = choice(0.67, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Evaluate the limit of (1 - x^2) / (1- x^3) as x approaches 1."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_93():
    def __init__(self):
        
        choice_a = '0 #'
        choice_b = '-1'
        choice_c = '1'
        choice_d = 'infinity'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the limit of (x - 3) / (x^2 - 9)^(1/2) as x approaches 3"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_94():
    def __init__(self):
        
        choice_a = 'x + 4y - 18 = 0 #'
        point = analytic_geometry_engine.Point()
        point.init_define(2,4)
        choice_b = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9,9)).string
        choice_c = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9,9)).string
        choice_d = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9,9)).string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the equation of the normal to y = x^3 - 2x^2 + 4 at (2,4)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_95():
    def __init__(self):
        
        choice_a = '(3, 6) and (-3, -6) #'
        choice_b = analytic_geometry_engine.Point().init_random().string + ' and ' + analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string + ' and ' + analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string + ' and ' + analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the points of tangency of horizontal tangents to the curve x^2 - xy + y^2 = 27"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_96():
    def __init__(self):
        
        choice_a = '(6, 3) and (-6, -3) #'
        choice_b = analytic_geometry_engine.Point().init_random().string + ' and ' + analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string + ' and ' + analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string + ' and ' + analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the points of tangency of vertical tangents to the curve x^2 - xy + y^2 = 27"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_97():
    def __init__(self):
        
        choice_a = '5x - 3y - 16 = 0 #'
        point = analytic_geometry_engine.Point()
        point.init_define(2, -2)
        choice_b = analytic_geometry_engine.Line().init_point_slope(point,  random.randint(-9, 9)).string
        choice_c = analytic_geometry_engine.Line().init_point_slope(point,  random.randint(-9, 9)).string
        choice_d = analytic_geometry_engine.Line().init_point_slope(point,  random.randint(-9, 9)).string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the equation of the tangent through the point (2, -2) to the hyperbola x^2 - y^2 = 16 """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_98():
    def __init__(self):
        
        choice_a = '2x + 9y + 20 = 0 #'
        point_1 = analytic_geometry_engine.Point()
        point_1.init_random()
        point_2 = analytic_geometry_engine.Point()
        point_2.init_random()
        point_3 = analytic_geometry_engine.Point()
        point_3.init_random()

        choice_b = analytic_geometry_engine.Line().init_point_slope(point_1,  - 2/9).string
        choice_c = analytic_geometry_engine.Line().init_point_slope(point_2, - 2/9).string
        choice_d = analytic_geometry_engine.Line().init_point_slope(point_3, - 2/9).string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the equation of the tangent with slope m = -2 / 9 to the ellipse 4x^2 + 9y^2 = 40"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_99():
    def __init__(self):
        point = analytic_geometry_engine.Point()
        point.init_define(1, 1)

        choice_a = 'x - y = 0 #'
        choice_b = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9, 9)).string
        choice_c = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9, 9)).string
        choice_d = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9, 9)).string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the equations of the normal to x^2 + 3xy + y^2 = 5 at (1, 1)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_100():
    def __init__(self):
        point = analytic_geometry_engine.Point()
        point.init_define(2, 4)
        choice_a = 'x + 4y - 18 = 0 #'
        choice_b = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9, 9)).string
        choice_c = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9, 9)).string
        choice_d = analytic_geometry_engine.Line().init_point_slope(point, random.randint(-9, 9)).string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the equation of the normal to y = x^3 - 2x^2 + 4 at (2, 4)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_101():
    def __init__(self):
        
        choice_a = '(1, 6) and (-1, 4) #'
        random_x_1 = random.randint(-5, 5)
        random_x_2 = random.randint(-5, 5)
        choice_b = f"""({random_x_1}, {random_x_1**3 + 5}) and ({random_x_2}, {random_x_2**3 + 5})"""
        random_x_1 = random.randint(-5, 5)
        random_x_2 = random.randint(-5, 5)
        choice_c = f"""({random_x_1}, {random_x_1**3 + 5}) and ({random_x_2}, {random_x_2**3 + 5})"""
        random_x_1 = random.randint(-5, 5)
        random_x_2 = random.randint(-5, 5)
        choice_d = f"""({random_x_1}, {random_x_1**3 + 5}) and ({random_x_2}, {random_x_2**3 + 5})"""
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""At what point on the curve y = x^3 + 5 is its tangent perpendicular to the line x + 3y = 2?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_102():
    def __init__(self):
        
        choice_a = '83 deg 49 min and 46 deg 05 min #'
        choice_b = f"""{choice(83, round = 0)} deg {choice(49, round = 0)} min and {choice(46, round = 0)} deg and {choice(5, round = 0)} min"""
        choice_c = f"""{choice(83, round = 0)} deg {choice(49, round = 0)} min and {choice(46, round = 0)} deg and {choice(5, round = 0)} min"""
        choice_d = f"""{choice(83, round = 0)} deg {choice(49, round = 0)} min and {choice(46, round = 0)} deg and {choice(5, round = 0)} min"""
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the acute angles of intersection of the curves y^2 = 4x and 2x^2 = 12 - 5y."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_103():
    def __init__(self):
        
        choice_a = '51 deg 20 min #'
        choice_b = f"""{choice(51, round = 0)} deg and {choice(20, round = 0)} min"""
        choice_c = f"""{choice(51, round = 0)} deg and {choice(20, round = 0)} min"""
        choice_d = f"""{choice(51, round = 0)} deg and {choice(20, round = 0)} min"""
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""A cable of a certain suspension bridge is attached to supporting pillars 250 feet apart. If it hangs in the form of a parabola with the lowest point 50 feet below the point of suspension, find the angle between the cable and the pillar."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_104():
    def __init__(self):
        
        choice_a = '45 degrees #'
        choice_b = choice(45, 'degrees', round = 0)
        choice_c = choice(45, 'degrees', round = 0)
        choice_d = choice(45, 'degrees', round = 0)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the acute angles of the intersection of the circles x^2 - 4x + y^2 = 0 and x^2 + y^2 = 8."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_105():
    def __init__(self):
        
        choice_a = '40.6 degrees #'
        choice_b = choice(40.6, 'degrees', round = 1)
        choice_c = choice(40.6, 'degrees', round = 1)
        choice_d = choice(40.6, 'degrees', round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the angle of intersection between the curve y = x^3 + x - 8 and y = x."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_106():
    def __init__(self):
        
        choice_a = '-11.18 #'
        choice_b = choice(-11.18, round = 2)
        choice_c = choice(-11.18, round = 2)
        choice_d = choice(-11.18, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the radius of curvature at point (4,4) of the curve y^2 - 4x = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_107():
    def __init__(self):
        
        choice_a = '5.66 #'
        choice_b = choice(5.66, round = 2)
        choice_c = choice(5.66, round = 2)
        choice_d = choice(5.66, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the radius of curvature at point (1, -2) of the curve 4x - y^2  = 0."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_108():
    def __init__(self):
        
        choice_a = '11.3 #'
        choice_b = choice(11.3, round = 1)
        choice_c = choice(11.3, round = 1)
        choice_d = choice(11.3, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the radius of curvature at the point (4, 2) of the curve x^2 - 8y = 0"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_109():
    def __init__(self):
        
        choice_a = '8.2 #'
        choice_b = choice(8.2, round = 1)
        choice_c = choice(8.2, round = 1)
        choice_d = choice(8.2, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the radius of curvature at point (1, 4) of the curve 16y - x^2 = 0"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_110():
    def __init__(self):
        
        choice_a = '2 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the radius of curvature at point (0,0) of the curve 4y - x^2 = 0?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_111():
    def __init__(self):
        
        choice_a = '-5.27 #'
        choice_b = choice(-5.27, round = 2)
        choice_c = choice(-5.27, round = 2)
        choice_d = choice(-5.27, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the radius of curvature of the curve x = y^3 at (1, 1)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_112():
    def __init__(self):
        
        choice_a = '-145.5 #'
        choice_b = choice(-145.5, round = 1)
        choice_c = choice(-145.5, round = 1)
        choice_d = choice(-145.5, round = 1)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Determine the radius of curvature of the curve x - y^3 = 0 at (8, 2)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class besavilla_113():
    def __init__(self):
        
        choice_a = '145.50 #'
        choice_b = choice(145.50, round = 2)
        choice_c = choice(145.50, round = 2)
        choice_d = choice(145.50, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the radius of curvature of the curve x^3 = y at (2, 8)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_114():
    def __init__(self):
        
        choice_a = '5.27 #'
        choice_b = choice(5.27, round = 2)
        choice_c = choice(5.27, round = 2)
        choice_d = choice(5.27, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the radius of curvature of the curve x^3 - y = 0 at (1, 1)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_115():
    def __init__(self):
        
        choice_a = '0.707 #'
        choice_b = choice(0.707, round = 3)
        choice_c = choice(0.707, round = 3)
        choice_d = choice(0.707, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the radius of curvature of the curve y = x^3 - x^2 at (1, 0)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_116():
    def __init__(self):
        
        choice_a = '0.088 #'
        choice_b = choice(0.088, round = 3)
        choice_c = choice(0.088, round = 3)
        choice_d = choice(0.088, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the curvature of the curve x^2 = 8y at the point (4, 2)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_117():
    def __init__(self):
        
        choice_a = '0.0589 #'
        choice_b = choice(0.0589, round = 4)
        choice_c = choice(0.0589, round = 4)
        choice_d = choice(0.0589, round = 4)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the curvature of the curve x^2 = 12y at point (6, 3)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_118():
    def __init__(self):
        
        choice_a = '-0.044 #'
        choice_b = choice(-0.044,round = 3)
        choice_c = choice(-0.044,round = 3)
        choice_d = choice(-0.044,round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the curvature of the curve y^2 = 16x at the point (4, 8)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_119():
    def __init__(self):
        
        choice_a = '-0.128 #'
        choice_b = choice(-0.128, round = 3)
        choice_c = choice(-0.128, round = 3)
        choice_d = choice(-0.128, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the curvature of the curve y^2 = 9x at the point (1, 3)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_120():
    def __init__(self):
        
        choice_a = '0.177 #'
        choice_b = choice(0.177, round = 3)
        choice_c = choice(0.177, round = 3)
        choice_d = choice(0.177, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the curvature of the curve x^2 = 4y at the point (2, 1)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_121():
    def __init__(self):
        
        choice_a = '(-2, 6) #'
        choice_b = analytic_geometry_engine.Point().init_random().string
        choice_c = analytic_geometry_engine.Point().init_random().string
        choice_d = analytic_geometry_engine.Point().init_random().string
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Locate the center of curvature of the parabola x^2 = 4y at the point (2, 2)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_122():
    def __init__(self):
        
        choice_a = '-6 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the ordinate of the center of curvature of the curve y^2 = 4x at point (2, 4) from the x - axis."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_123():
    def __init__(self):
        
        choice_a = '5 #'
        choice_b = random.randint(-9, 9)
        choice_c = random.randint(-9, 9)
        choice_d = random.randint(-9, 9)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""Find the abcissa of the center of curvature of the parabola y^2 = 4x at (1,2)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_124():
    def __init__(self):
        
        choice_a = '0.385 #'
        choice_b = choice(0.385, round = 3)
        choice_c = choice(0.385, round = 3)
        choice_d = choice(0.385, round = 3)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the maximum value of y if y = x^3 - x?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class besavilla_125():
    def __init__(self):
        
        choice_a = '-7.56 #'
        choice_b = choice(-7.56, round = 2)
        choice_c = choice(-7.56, round = 2)
        choice_d = choice(-7.56, round = 2)
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""What is the maximum of value of y if y = x^4 - 8x?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

























































































        




























































