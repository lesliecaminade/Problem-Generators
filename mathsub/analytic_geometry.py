import math
import random
from mathsub import analytic_geometry_engine as engine
from num2words import num2words

ANSWER_FLAG = ' #'


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
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
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
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the quadrant in which the point {main.point_1.string} belongs."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Midpoint():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Midpoint()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.midpoint.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the midpoint of the points {main.point_1.string} and {main.point_2.string}"""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Extension_of_line_segment():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Extension_of_line_segment()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.terminal_point.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the terminal point of the line segment formed by extending the line segment from point {main.point_1.string} to {main.point_2.string} to {num2words(main.factor)} times its original length."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Extension_of_line_segment_by():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Extension_of_line_segment()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.terminal_point.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the terminal point of the line segment formed by extending the line segment from point {main.point_1.string} to {main.point_2.string} by {num2words(main.factor-1)} times its original length."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Division_of_line_segment():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Division_of_line_segment()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.terminal_point.round().string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the terminal point of the line segment formed by dividing the line segment from point {main.point_1.string} to {main.point_2.string} to {main.factor} times its original length."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Equation_of_a_line_two_points():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Equation_of_a_line_two_points()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.line.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the line which intersects with the points {main.point_1.string} and {main.point_2.string}."""

		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Equation_of_a_line_point_slope():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Equation_of_a_line_point_slope()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.line.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the line that intersects the point {main.point.string} and has a slope of {main.slope}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Equation_of_a_line_slope_intercept():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Equation_of_a_line_slope_intercept()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.line.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the line which has a slope of {main.slope} and a y-intercept of {main.y_intercept}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Equation_of_a_line_intercepts():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Equation_of_a_line_intercepts()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.line.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the line which has an x-intercept of {main.x_intercept} and a y-intercept of {main.y_intercept}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Line_parallel_to_line():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Line_parallel_to_line()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.line.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the line which intersects the point {main.point_3.string} and also parallel to the line that intersects both the points {main.point_1.string} and {main.point_2.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Line_perpendicular_to_line():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Line_perpendicular_to_line()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.line.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the line which intersects the point {main.point_3.string} and also perpendicular to the line that intersects both the points {main.point_1.string} and {main.point_2.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Angle_between_the_lines():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Angle_between_the_lines()
			#data = battery.Some_attribute_from_battery         
			data =  parse(round(battery.angle.degrees,2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the angle between the lines {main.line_1.string}, and {main.line_2.string} in degrees."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""  

class Distance_from_point_to_line():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Distance_from_point_to_line()
			#data = battery.Some_attribute_from_battery         
			data =  parse(round(battery.distance,2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the distance between the line {main.line.string} and the point {main.point.string}"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Distance_from_line_to_line():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Distance_from_line_to_line()
			#data = battery.Some_attribute_from_battery         
			data =  parse(round(battery.distance, 2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the distance between the lines {main.line_1.string} and {main.line_2.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Area_of_three_points():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Area_of_three_points()
			#data = battery.Some_attribute_from_battery         
			data =  parse(round(battery.area, 2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + {ANSWER_FLAG}
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the area enclosed by the polygon formed by connecting the points {main.point_1.string}, {main.point_2.string} and {main.point_3.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Conic_section_derivation():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Conic_section_derivation()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.conic)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""What is the conic section that is {main.description.lower()}?"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Circle_standard_to_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_standard_to_general()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.circle.general_string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the circle that has a center at {main.circle.center.string} and has a radius of {main.circle.radius}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Circle_circumference_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_circumference_from_general()
			#data = battery.Some_attribute_from_battery         
			data =  parse(round(battery.circle.circumference(), 2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the circumference of the circle whose equation is {main.circle.general_string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Circle_general_from_three_points():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_general_from_three_points()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.circle.general_string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the circle that intersects the points {main.points[0].string}, {main.points[1].string}, and {main.points[2].string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Circle_coefficient_from_general_and_radius():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_coefficient_from_general_and_radius()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.coefficients['E'])
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the coefficient E of the circle if its general equation is in the form ({main.coefficients['A']}) x^2 + ({main.coefficients['C']}) y^2 + ({main.coefficients['D']}) x + E y + ({main.coefficients['F']}) = 0 and its radius is {main.radius} units."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Circle_distance_from_point():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_distance_from_point()
			#data = battery.Some_attribute_from_battery         
			data =  parse(round(battery.distance, 2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the distance from the point {main.point.string} to the circle whose equation is {parse(main.circle.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}""" 

class Circle_center_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_center_from_general()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.circle.center.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the general equation {parse(main.circle.general_string)}"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Circle_area_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_area_from_general()
			#data = battery.Some_attribute_from_battery         
			data =  parse(str(round(battery.circle.area(), 2)) + ' units^2' )
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the area of the circle whose equation is {parse(main.circle.general_string)}"""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Circle_area_from_center_and_tangent_line():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_area_from_center_and_tangent_line()
			#data = battery.Some_attribute_from_battery         
			data =  parse(str(round(battery.area, 2)) + ' units^2' )
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the area of the circle if its center is at the point {main.center.string} and tangent to the line {main.line.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Circle_center_to_line_distance():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_center_to_line_distance()
			#data = battery.Some_attribute_from_battery         
			data =  parse(str(battery.distance) + ' units' )
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the shortest distance between the circle whose equation is {parse(main.circle.general_string)} and the line {parse(main.line.string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""


class Circle_length_of_tangent_from_general_and_point():
	def __init__(self):
		try_again = True
		while try_again:
			try:
				BATTERIES = []
				CHOICES = []
				suffix = ''
				prefix = ''
				for i in range(4):
					#battery = engine.Some_class_from_engine
					battery = engine.Circle_length_of_tangent_from_general_and_point()
					#data = battery.Some_attribute_from_battery         
					data =  parse(str(round(battery.distance,2)) + ' units' )
					BATTERIES.append(battery)
					CHOICES.append(prefix + str(data) + suffix) 
				main = BATTERIES[0]
				CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
				random.shuffle(CHOICES)
				#edit below
				self.question = f"""{ask()} the length of the tangent segment from the point {parse(main.point.string)} to the circle {parse(main.circle.general_string)}."""
				self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""
				try_again = False
			except:
				print('regenerating ', type(self)) 


class Circle_ratio_of_circumference():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_ratio_of_circumference()
			#data = battery.Some_attribute_from_battery         
			data =  parse(str(round(battery.ratio,2)))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the ratio of the circumferences of the circles {parse(main.circle_1.general_string)} and {parse(main.circle_2.general_string)} respectively."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Circle_diameter_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Circle_diameter_from_general()
			#data = battery.Some_attribute_from_battery         
			data =  battery.diameter
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the diameter of the circle whose equation is {parse(main.circle.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""


class Parabola_diameter_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_diameter_from_general()
			#data = battery.Some_attribute_from_battery         
			data =  abs(battery.parabola.focal_length)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the focal length of the parabola whose equation is {parse(main.parabola.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Parabola_latus_rectum_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_latus_rectum_from_general()
			#data = battery.Some_attribute_from_battery         
			data =  abs(round(battery.parabola.latus_rectum,2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the length of the latus rectum of the parabola whose equation is {parse(main.parabola.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Parabola_latus_rectum_from_directrix_and_focus():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_generic()
			#data = battery.Some_attribute_from_battery         
			data =  abs(round(battery.parabola.latus_rectum,2))
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the length of the latus rectum of the parabola whose directrix is {main.parabola.directrix_string} and focus is {main.parabola.focus.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Parabola_from_three_points():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_from_three_points()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.parabola.general_string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the parabola if the parabola contains the points {main.points[0].string}, {main.points[1].string}, and {main.points[2].string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Parabola_from_vertex_and_focus():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_generic()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.parabola.general_string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the parabola if its vertex is {main.parabola.vertex.string} and its focus is {main.parabola.focus.string}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""


class Parabola_focus_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_generic()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.parabola.focus.string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the focus of the parabola that has the equation {parse(main.parabola.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Parabola_directrix_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Parabola_generic()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.parabola.directrix_string)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the equation of the directrix of the patabola whose equation is {parse(main.parabola.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Ellipse_eccentricity_from_general():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Ellipse_generic()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.ellipse.eccentricity)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the eccentricity of the conic sections which has the equation {parse(main.ellipse.general_string)}."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""

class Ellipse_eccentricity_from_major_minor():
	def __init__(self):
		BATTERIES = []
		CHOICES = []
		suffix = ''
		prefix = ''
		for i in range(4):
			#battery = engine.Some_class_from_engine
			battery = engine.Ellipse_generic()
			#data = battery.Some_attribute_from_battery         
			data =  parse(battery.ellipse.eccentricity)
			BATTERIES.append(battery)
			CHOICES.append(prefix + str(data) + suffix) 
		main = BATTERIES[0]
		CHOICES[0] = str(CHOICES[0]) + ANSWER_FLAG
		random.shuffle(CHOICES)
		#edit below
		self.question = f"""{ask()} the eccentricity of the ellipse which has a major axis of length {main.ellipse.major_axis} units and minor axis of length {main.ellipse.minor_axis} units."""
		self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""


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






















































































































 
















		
















 































































