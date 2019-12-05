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


class DerivativeExplicit:
    def __init__(self):
        pass

    def init_random(self):
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




































































































        




























































