from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import analytic_geometry_engine as engine
from mathsub import algebra_engine

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

def ask():
    ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
    return random.choice(ask_words)

def parse(string_input):
    string_input = str(string_input)
    return string_input.replace('**', '^').replace('*', ' ')

class Distance_between_two_points():
    def __init__(self):
        BATTERIES = []
        CHOICES = []
        suffix = ''
        prefix = ''
        for i in range(4):
            #battery = engine.Some_class_from_engine
            battery = engine.Distance_between_two_points()
            #data = battery.Some_attribute_from_battery         
            data =  parse(round(battery.distance,2))
            BATTERIES.append(battery)
            CHOICES.append(prefix + str(data) + suffix) 
        main = BATTERIES[0]
        CHOICES[0] = str(CHOICES[0]) + ' #'
        random.shuffle(CHOICES)
        #edit below
        self.question = f"""{ask()} the distance between the two points {main.point_1.string} and {main.point_2.string}"""

        self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  


class Quadrant_identification():
    def __init__(self):
        BATTERIES = []
        CHOICES = []
        suffix = ''
        prefix = ''
        for i in range(4):
            #battery = engine.Some_class_from_engine
            battery = engine.Quadrant_identification()
            #data = battery.Some_attribute_from_battery         
            data =  parse(battery.quadrant)
            BATTERIES.append(battery)
            CHOICES.append(prefix + str(data) + suffix) 
        main = BATTERIES[0]
        CHOICES[0] = str(CHOICES[0]) + ' #'
        random.shuffle(CHOICES)
        #edit below
        self.question = f"""{ask()} the quadrant in which the point {main.point_1.string} belongs."""

        self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class midpoint_of_two_points():
    def __init__(self):

        point_1 = engine.Point()
        point_2 = engine.Point()
        point_1.init_random()
        point_2.init_random()

        midpoint = point_1.midpoint(point_2)

        self.question = f"""Determine the midpoint of the two points {point_1.string}  and {point_2.string}."""
        self.answer = f"""{midpoint.string}"""

class extension_of_line_segment():
    def __init__(self):

        point_1 = engine.Point()
        point_2 = engine.Point()
        point_1.init_random()
        point_2.init_random()

        factor = random.randint(engine.EXTEND_FACTOR_MIN, engine.EXTEND_FACTOR_MAX)
        terminal_point = point_1.extend(point_2, factor)

        form = random.randint(0,1)

        if form == 0:

            self.question = f"""The line segment from {point_1.string} to {point_2.string} is extended to {factor} times its own length. Find the terminal point."""
            self.answer = f"""{terminal_point.string}"""

        if form == 1:
            self.question = f"""If the line segment from {point_1.string} to {point_2.string} is extended by {factor - 1} times its own length. Find the terminal point."""

            self.answer = f"""{terminal_point.string}"""

class division_of_line_segment():
    def __init__(self):

        point_1 = engine.Point()
        point_2 = engine.Point()
        point_1.init_random()
        point_2.init_random()

        factor = random.randint(1,99) / 100
        terminal_point = point_1.extend(point_2, factor)

        self.question = f"""If the line segment from {point_1.string} to {point_2.string} is divided to {factor} times its own length, find the terminal point."""
        self.answer = f"""{terminal_point.string}"""


class equation_of_a_line_two_points():
    def __init__(self):

        point1 = engine.Point()
        point2 = engine.Point()

        point1.init_random()
        point2.init_random()


        line = engine.Line()
        line.init_two_points(point1, point2)

        self.question = f"""Determine the equation of the line that passes through the points {point1.string} to {point2.string}"""

        self.answer = f"""{line.general} = 0"""

class equation_of_a_line_point_slope():
    def __init__(self):

        point = engine.Point()
        point.init_random()

        slope = random.randint(-engine.SLOPE_MAX, engine.SLOPE_MAX)

        line = engine.Line()

        line.init_point_slope(point, slope)

        self.question = f"""Determine the equation of the line passes through the point {point.string} and has a slope of {slope}."""

        self.answer = f"""{line.general} = 0"""

class equation_of_a_line_slope_intercept():
    def __init__(self):

        yintercept = random.randint(-engine.Y_RANGE, engine.Y_RANGE)

        slope = random.randint(-engine.SLOPE_MAX, engine.SLOPE_MAX)

        line = engine.Line()

        line.init_slope_intercept(slope, yintercept)

        self.question = f"""Determine the equation of the line that has a slope of {slope} and has a y-intercept of {yintercept}."""

        self.answer = f"""{line.general} = 0"""

class equation_of_a_line_intercepts():
    def __init__(self):

        xintercept = random.randint(-engine.X_RANGE, engine.X_RANGE)
        yintercept = random.randint(-engine.Y_RANGE, engine.Y_RANGE)

        line = engine.Line()
        line.init_intercepts(xintercept, yintercept)

        self.question = f"""Determine the equation of the line that has x-intercept equal to {xintercept} and y-intercept equal to {yintercept}."""

        self.answer = f"""{line.general} = 0"""

class line_parallel_to_line():
    def __init__(self):

        point1 = engine.Point()
        point2 = engine.Point()

        point3 = engine.Point()

        point1.init_random()
        point2.init_random()
        point3.init_random()

        line1 = engine.Line()
        line1.init_two_points(point1, point2)

        line2 = engine.Line()
        line2.init_point_slope(point3, line1.parallel())

        self.question = f"""Determine the equation of a line that includes the point {point3.string} and is parallel to {line1.general} = 0."""

        self.answer = f"""{line2.general} = 0"""

class line_perpendicular_to_line():
    def __init__(self):

        point1 = engine.Point()
        point2 = engine.Point()

        point3 = engine.Point()

        point1.init_random()
        point2.init_random()
        point3.init_random()

        line1 = engine.Line()
        line1.init_two_points(point1, point2)

        line2 = engine.Line()
        line2.init_point_slope(point3, line1.perpendicular())

        self.question = f"""Determine the equation of a line that includes the point {point3.string} and is perpendicular to {line1.general} = 0."""
        self.answer = f"""{line2.general} = 0"""


class angle_between_two_lines():
    def __init__(self):

        line1 = engine.Line()
        line1.init_random()

        line2 = engine.Line()
        line2.init_random()

        angle_between_lines = line1.angle_to_line(line2)

        self.question = f"""Determine the smaller angle between the lines {line1.general} = 0 and {line2.general} = 0."""

        self.answer = f"""{angle_between_lines.degrees} degrees"""

class distance_from_point_to_line():
    def __init__(self):

        line = engine.Line()
        line.init_random()

        point = engine.Point()
        point.init_random()

        distance = line.distance(point)

        self.question = f"""Determine the shortest distance between the line {line.string} and the point {point.string}."""

        self.answer = f"""{distance}"""

class distance_from_line_to_line():
    def __init__(self):

        line1 = engine.Line()
        slope = random.randint(-engine.SLOPE_MAX, engine.SLOPE_MAX)
        b1 = random.randint(-engine.Y_RANGE, engine.Y_RANGE)
        line1.init_slope_intercept(slope, b1)


        line2 = engine.Line()
        b2 = random.randint(-engine.Y_RANGE, engine.Y_RANGE)
        line2.init_slope_intercept(slope, b2)

        distance = line1.distance(line2)

        self.question = f"""Determine the shortest distance between the lines {line1.string} and {line2.string}."""
        self.answer = f"""{distance}"""

class area_of_3_points():
    def __init__(self):

        point1 = engine.Point()
        point2 = engine.Point()
        point3 = engine.Point()

        point1.init_random()
        point2.init_random()
        point3.init_random()

        area = point1.area_shoelace_3_points(point2, point3)

        self.question = f"""Determine the area formed by the convex polygon by connecting the points {point1.string}, {point2.string}, and {point3.string}."""
        self.answer = f"""{area} square units"""

class derivation_of_conic_sections():
    def __init__(self):

        conic_sections = engine.CONIC_SECTIONS_LIST
        conic = random.choice(conic_sections)

        self.question = f"""What conic section is produced when {conic[1]}?"""
        self.answer = f"""{conic[0]}"""

class standard_to_general_circle():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        self.question = f"""Determine the equation of a circle whose center is located at the point {circle.center.string} and has a radius of {circle.radius}."""
        self.answer = f"""{circle.general_string}"""

class circumference_from_general():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        self.question = f"""Calculate the circumference of the circle whose equation is {circle.general_string}."""

        self.answer = f"""{round(circle.circumference(),2)}"""

class general_from_three_points():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        points = circle.three_points()

        self.question = f"""Determine the equation of the circle that contains the points {points[0].string}, {points[1].string},  and {points[2].string}."""
        self.answer = f"""{circle.general_string}"""

class coefficient_from_general_and_radius():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        coeff = circle.general_coefficients()

        self.question = f"""If the equation of a circle is in the form Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 and the coefficients are A = {coeff[0]}, B = {coeff[1]}, C = {coeff[2]}, D = {coeff[3]}, and F = {coeff[5]}, and the radius of the circle is {circle.radius}, determine the value of E."""
        self.answer = f"""{circle.E} , check: {circle.general_string}"""

class distance_from_circle_and_point():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        point = engine.Point()

        point.init_random()

        while circle.distance_to_center(point) <= circle.radius:
            #making sure the random point is outside the circle
            point = engine.Point()
            point.init_random()

        self.question = f"""Find the shortest distance from the circle {circle.general_string} to the point {point.string}."""
        self.answer = f"""{round(circle.distance_to_center(point),2)}"""

class center_from_general():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        self.question = f"""Find the center of the circle whose equation is given by {circle.general_string}."""
        self.answer = f"""{circle.center.string}"""

class area_from_general():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        self.question = f"""Calculate the area of the circle whose equation is {circle.general_string}"""
        self.answer = f"""{round(circle.area(), 2)} units^2"""

class area_from_center_and_tangent_line():
    def __init__(self):

        line = engine.Line()
        line.init_random()

        point = engine.Point()
        point.init_random()

        circle = engine.Circle()
        circle.init_define(point, line.distance(point))

        self.question = f"""If the center of a circle is located at {point.string} and is tangent to the line {line.string}, determine the area of the circle."""
        self.answer = f"""{round(circle.area(), 2)} units^2"""

class center_to_line_distance():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        point1 = circle.point()
        line1 = engine.Line()

        line1.init_two_points(circle.center, point1)

        point2 = circle.center.extend(point1, random.randint(engine.EXTEND_FACTOR_MIN, engine.EXTEND_FACTOR_MAX))

        line2 = engine.Line()
        line2.init_point_slope(point2, line1.perpendicular())

        self.question =f"""Calculate the shortest distance between the circle whose equation is {circle.general_string} and the line {line2.string}."""
        self.answer = f"""{round(point1.distance(point2))}"""

class length_of_tangent_from_general_and_point():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        point1 = circle.point()

        line1 = engine.Line()
        line1.init_two_points(circle.center, point1)
        line2 = engine.Line()
        line2.init_point_slope(point1, line1.perpendicular())
        point2 = line2.point()

        self.question = f"""Calculate the length of the tangent segment from the point {point2.string} to the circle {circle.general_string}."""
        self.answer = f"""{round(point1.distance(point2), 2)}"""

class ratio_of_circumferences():
    def __init__(self):

        circle1 = engine.Circle()
        circle2 = engine.Circle()
        circle1.init_random()
        circle2.init_random()

        self.question = f"""Determine the ratio of the circumferences of the circles {circle1.general_string} and {circle2.general_string}."""

        self.answer = f"""{round(circle1.circumference()/circle2.circumference(), 2)}"""

class diameter_from_general():
    def __init__(self):

        circle = engine.Circle()
        circle.init_random()

        self.question = f"""Calculate the diameter of the circle whose equation is given by {circle.general_string}"""
        self.answer = f"""{circle.diameter}"""

class focal_length_from_general():
    def __init__(self):

        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""Calculate the focal length of the parabola whose equation is {parabola.general_string} = 0"""
        self.answer = f"""{abs(parabola.focal_length)}"""

class latus_rectum_from_general():
    def __init__(self):
         parabola = engine.Parabola()
         parabola.init_random()

         self.question = f"""Determine the length of the latus rectum of the parabola whose equation is {parabola.general_string}."""
         self.answer = f"""{parabola.latus_rectum}"""

class latus_rectum_from_directrix_and_focus():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""Determine the length of the latus rectum of the parabola whose directrix is {parabola.directrix_string} and focus is {parabola.focus.string}."""
        self.answer = f"""{parabola.latus_rectum}"""

class parabola_from_three_points():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        points = parabola.points(3)
        self.question = f"""Determine the equation of the parabola if the parabola contains the points {points[0].string}, {points[1].string}, and {points[2].string}."""
        self.answer= f"""{parabola.general_string}"""

class parabola_from_vertex_and_focus():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""Determine the equation of the parabola if its vertex is {parabola.vertex.string} and its focus is {parabola.focus.string}"""
        self.answer = f"""{parabola.general_string}"""

class parabola_from_directrix_and_point():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""Determine the equation of the parabola if its directrix is {parabola.directrix_string} and one of its points is {parabola.point().string}"""

        self.answer = f"""{parabola.general_string}"""

class focus_from_general_parabola():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""A parabola has the equation {parabola.general_string}. Find the location of the focus of such parabola."""
        self.answer = f"""{parabola.focus.string}"""

class directrix_from_general_parabola():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""A parabola has the equation {parabola.general_string}. Determine the equation of its directrix."""
        self.answer = f"""{parabola.directrix_string}"""

class concavity_from_general_parabola():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""A parabola has the equation {parabola.general_string}. Determine the direction of its concavity."""
        self.answer = f"""{parabola.concavity}"""

class area_bounded_by_parabola_and_latus_rectum():
    def __init__(self):
        parabola = engine.Parabola()
        parabola.init_random()

        self.question = f"""Calculate the area bounded by the parabola {parabola.general_string} and its latus rectum."""
        self.answer = f"""{round(parabola.area_parabola_and_latus_rectum(),2)}"""

class eccentricity_from_general_ellipse():
    def __init__(self):
        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Determine the eccentricity of the conic section by the equation {ellipse.general_string}."""
        self.answer = f"""{ellipse.eccentricity}"""

class eccentricity_from_major_axis_minor_axis():
    def __init__(self):
        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Determine the eccentricity of the conic section that has a major axis of length {ellipse.major_axis} and has a minor axis of length {ellipse.minor_axis}."""
        self.answer = f"""{ellipse.eccentricity}"""

class area_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""For an conic section with a general equation {ellipse.general_string}, calculate the area of the ellipse."""
        self.answer = f"""{round(ellipse.area,2)} units^2"""

class longest_focal_radius_ellipse_from_point_center_orientation():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""What is the longest possible focal radius for an ellipse with that contains the point {ellipse.point().string}, and its center at {ellipse.center.string}, with its orientation {ellipse.orientation}?"""
        self.answer = f"""{ellipse.semi_major_axis + ellipse.focal_length}"""

class longest_focal_radius_ellipse_from_distance_between_vertices_eccentricity():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Calculate the longest focal radius for an ellipse whose distance between vertices is {ellipse.major_axis} and eccentricity of {ellipse.eccentricity}."""
        self.answer = f"""{ellipse.focal_length + ellipse.semi_major_axis}"""

class circumference_from_general_equation_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Calculate the circumference of the ellipse whose general equation is {ellipse.general_string}"""
        self.answer = f"""{round(ellipse.circumference,2)}"""

class general_from_sum_of_distances_two_foci__eccentricity_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Find the general equation of the conic section where the sum of the distances from any point (x, y) to the two points {ellipse.focus1.string} and {ellipse.focus2.string}, and also, its eccentricity is {ellipse.eccentricity}."""
        self.answer = f"""{ellipse.general_string}"""

class semi_major_axis_from_distance_between_foci_and_eccentricity_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""For an ellipse, if the distance between its foci is {ellipse.focal_length*2}, and has an eccentricity of {ellipse.eccentricity}, determine the length of its semi-major axis."""
        self.answer = f"""{ellipse.semi_major_axis}"""

class major_axis_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()
        
        self.question = f"""Calculate the length of the major axis of an ellipse whose general equation is given by {ellipse.general_string}"""

        self.answer = f"""{ellipse.major_axis}"""

class distance_from_y_axis_to_focus_ellipse_vertical():
    def __init__(self):
        center = engine.Point()
        center.init_random()
        b = random.randint(engine.ELLIPSE_MINOR_AXIS_MIN, engine.ELLIPSE_MINOR_AXIS_MAX)
        a = random.randint(b + 1, engine.ELLIPSE_MAJOR_AXIS_MAX)

        ellipse = engine.Ellipse()
        ellipse.init_define(center, a, b, 'vertical')

        self.question = f"""If the equation of an ellipse is {ellipse.general_string}, compute for the the distance between its foci and the y - axis."""
        self.answer = f"""{abs(ellipse.center.x)}"""

class center_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Find the center of the ellipse whose equation is {ellipse.general_string}"""
        self.answer = f"""{ellipse.center.string}"""


class distance_between_directrices_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Find the distance between the directrices of the ellipse {ellipse.general_string}"""
        self.answer = f"""{2 * ellipse.directrix_distance}"""

class distance_between_foci_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""An ellipse has the equation {ellipse.general_string}. Determine the distance between its foci."""
        self.answer = f"""{ellipse.focal_length * 2}"""

class directrix_equation_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Find the equation of the directrices of the ellipse {ellipse.general_string}"""
        self.answer = f"""{ellipse.directrix1_string} and {ellipse.directrix2_string}"""

class latus_rectum_length_from_general_ellipse():
    def __init__(self):

        ellipse = engine.Ellipse()
        ellipse.init_random()

        self.question = f"""Calculate the length of the latus rectum of an ellipse whose equation is {ellipse.general_string}"""
        self.answer = f"""{ellipse.latus_rectum}"""

class center_from_general_hyperbola():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""Find the center of the hyperbola whose general equation is {hyperbola.general_string}"""
        self.answer = f"""{hyperbola.center.string}"""

class eccentricity_from_general_hyperbola():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""Find the eccentricity of the hyperbola whose general equation is {hyperbola.general_string}"""
        self.answer = f"""{hyperbola.eccentricity}"""

class equation_of_asymptotes_from_general_hyperbola():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""Determine the equation of the asymptotes of the hyperbola whose general equation is in the form {hyperbola.general_string}"""

        self.answer = f"""{hyperbola.asymptote1.string} and {hyperbola.asymptote2.string}"""

class latus_rectum_from_general_hyperbola():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""The length of the latus rectum of a hyperbola whose general equation is {hyperbola.general_string} is """
        self.answer = f"""{hyperbola.latus_rectum}"""

class general_hyperbola_from_asymptotes_and_point():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""If the hyperbola has asymptotes {hyperbola.asymptote1.string} and {hyperbola.asymptote2.string}, and also contains the point {hyperbola.point().string}, determine the equation of the hyperbola."""
        self.answer = f"""{hyperbola.general_string}"""

class general_hyperbola_difference_between_distance_foci():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""If the hyperbola contains the foci {hyperbola.focus1.string} and {hyperbola.focus2.string}, and the magnitude of the difference of the distances from the point (x, y) to each focus is {hyperbola.semi_transverse_axis * 2}, determine the equation of the hyperbola."""
        self.answer = f"""{hyperbola.general_string}"""

class semi_conjugate_axis_from_general_hyperbola():
    def __init__(self):

        hyperbola = engine.Hyperbola()
        hyperbola.init_random()

        self.question = f"""If the hyperbola has an equation {hyperbola.general_string}, determine the length of its semi-conjugate axis."""
        self.answer = f"""{hyperbola.semi_conjugate_axis}"""






















































































































 
















        
















 































































