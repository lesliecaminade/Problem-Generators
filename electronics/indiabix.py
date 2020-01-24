import random

class template():
	def __init__(self):
		
		choice_a = 'The number of neutrons'
		choice_b = 'The number of protons#'
		choice_c = 'The number of neutrons plus the number of protons'
		choice_d = 'The number of electrons'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The atomic number of an element is determined by:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


