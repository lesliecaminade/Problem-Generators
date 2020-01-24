import random_handler as ran
import math
import random
import constants_conversions as c


# class grobs_15_1:
#     def __init__(self):
#         choice_a = 
#         choice_b = 
#         choice_c = 
#         choice_d = 

#         choices = [choice_a, choice_b, choice_c, choice_d]
#         random.shuffle(choices)
#         self.questions = f""" """
#         self.answer = f"""A. {choices[0]}
# B. {choices[1]}
# C. {choices[2]}
# D. {choices[3]}""" - for template purposes


class grobs_1_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'coulomb'
		choice_b = 'electron*'
		choice_c = 'proton'
		choice_d = 'neutron'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The most basic particle of negative charge is the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'electric charge*'
		choice_b = 'potential difference'
		choice_c = 'current'
		choice_d = 'voltage'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The coulomb is a unit"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'copper'
		choice_b = 'silver'
		choice_c = 'glass*'
		choice_d = 'gold'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following is not a good conductor?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_4:
	def __init__(self, *args, **kwargs):
		choice_a = '+ 1*'
		choice_b = '0'
		choice_c = '(+/-) 4'
		choice_d = '- 1'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The electron valence of a neutral copper atom is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_5:
	def __init__(self, *args, **kwargs):
		choice_a = 'volt*'
		choice_b = 'ampere'
		choice_c = 'siemens'
		choice_d = 'coulomb'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The unit of potential difference is the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'unlike charges repel each other'
		choice_b = 'like charges repel each other'
		choice_c = 'unlike charges attract each other'
		choice_d = 'like charges repel each other, unlike charges attract each other*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following statements is true?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'positive ions are the moving charges that provide current'
		choice_b = 'free electrons are the moving charges that provide current*'
		choice_c = 'there are no free electrons'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In metal conductor, such as a copper wire,"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_8:
	def __init__(self, *args, **kwargs):
		choice_a = '0.01 S*'
		choice_b = '0.1 S'
		choice_c = '0.001 S'
		choice_d = '1 S'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 100-ohms resistor has a conductance, G, of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'coulomb'
		choice_b = 'electron'
		choice_c = 'proton*'
		choice_d = 'neutron'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The most basic particle of positive charge is the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'negative ion'
		choice_b = 'electrically charged atom'
		choice_c = 'positive ion'
		choice_d = 'electrically charged atom, positive ion*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If the neutral atom loses one of its valence electrons, it becomes a(n)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'volt'
		choice_b = 'ampere*'
		choice_c = 'coulomb'
		choice_d = 'siemens'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The unit of electric current is the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_12:
	def __init__(self, *args, **kwargs):
		choice_a = '(+/-) 4*'
		choice_b = '+ 1'
		choice_c = '- 7'
		choice_d = '0'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A semiconductor, such as silicon, has an electron valence of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'current can exist without voltage'
		choice_b = 'voltage can exist without current*'
		choice_c = 'current can flow through an open circuit'
		choice_d = 'voltage can exist without current and current can flow through an open circuit'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following statements is true?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_14:
	def __init__(self, *args, **kwargs):
		choice_a = 'volt'
		choice_b = 'coulomb'
		choice_c = 'siemens'
		choice_d = 'ohm*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The unit of resistance is the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_15:
	def __init__(self, *args, **kwargs):
		choice_a = '6'
		choice_b = '1'
		choice_c = '8*'
		choice_d = '4'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Except for hydrogen (H) and helium (He) the goal of valence for an atom"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_16:
	def __init__(self, *args, **kwargs):
		choice_a = '1C/1s*'
		choice_b = '1J/1C'
		choice_c = '6.25 e18 electrons'
		choice_d = '0.16 e-18 C/s'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""One ampere of current corresponds to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_17:
	def __init__(self, *args, **kwargs):
		choice_a = 'the motion of negative charges in the opposite direction of electron flow'
		choice_b = 'the motion of positive charges in the same direction as electron flow'
		choice_c = 'the motion of positive charges in the position of electron flow*'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Conventional current is considered"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_18:
	def __init__(self, *args, **kwargs):
		choice_a = 'make sure that the resistor is in a circuit where voltage is present'
		choice_b = 'make sure there is no voltage present across the resistor'
		choice_c = 'make sure there is no other component connected across the leads of the resistor'
		choice_d = 'both b and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""When using a DMM to measure the value of a resistor"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_19:
	def __init__(self, *args, **kwargs):
		choice_a = 'conductance'
		choice_b = 'resistance*'
		choice_c = 'voltage'
		choice_d = 'current'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In a circuit, the opposition to the flow of current is called"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_20:
	def __init__(self, *args, **kwargs):
		choice_a = '13 valence electrons'
		choice_b = '3 valence electrons'
		choice_c = '13 protons in its nucleus'
		choice_d = 'both b and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""Aluminum, with an atomic number of 13, has"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_21:
	def __init__(self, *args, **kwargs):
		choice_a = 'electrons and neutrons'
		choice_b = 'ions'
		choice_c = 'neutrons and protons*'
		choice_d = 'electrons only'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The nucleus of an atom is made up of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_22:
	def __init__(self, *args, **kwargs):
		choice_a = '16 C'
		choice_b = '20 C*'
		choice_c = '1.25 C'
		choice_d = '0.8 C'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much charge is accumulated in a dielectric that is charged by a 4A current for 5 seconds"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_23:
	def __init__(self, *args, **kwargs):
		choice_a = '24 A*'
		choice_b = '2.4 A'
		choice_c = '1.5 A'
		choice_d = '12 A'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A charge of 6 C moves past a given point every 0.25 second. How much is the current flow in amperes?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_24:
	def __init__(self, *args, **kwargs):
		choice_a = '18 V'
		choice_b = '6 V'
		choice_c = '125 mV'
		choice_d = '8 V*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is output voltage of a battery that expands 12 J of energy in moving 1.5 C of charge?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_1_25:
	def __init__(self, *args, **kwargs):
		choice_a = 'The resistance of an open circuit is practically zero*'
		choice_b = 'The resistance of a short circuit is practically zero'
		choice_c = 'The resistance of an open circuit is infinitely high'
		choice_d = 'There is no current in an open circuit'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following statements is false?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_1:
	def __init__(self, *args, **kwargs):
		choice_a = '+/- 5%'
		choice_b = '+/- 20%*'
		choice_c = '+/- 10%'
		choice_d = '+/- 100%'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A carbon composition resistor having only three color stripes has a tolerance of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'carbon-composition resistor'
		choice_b = 'metal-film resistor'
		choice_c = 'surface-mount resistor'
		choice_d = 'wire-wound resistor*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A resistor with a power rating of 25 W is most likely a"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'infinite resistance*'
		choice_b = 'its color-coded value'
		choice_c = 'zero resistance'
		choice_d = 'less than its color-coded value'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When checked with an ohmmeter, an open resistor measures"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'check high resistances on the lowest ohms range'
		choice_b = 'check low resistances on the highest ohms range'
		choice_c = 'disconnect all parallel paths*'
		choice_d = 'make sure your fingers are touching each test lead'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""One precaution to observe when checking resistors with an ohmmeter is to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_5:
	def __init__(self, *args, **kwargs):
		choice_a = '39.4 ohms'
		choice_b = '394 ohms'
		choice_c = '390,000 ohms*'
		choice_d = '39,000 ohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A chip resistor is marked 394. Its resistance value is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_6:
	def __init__(self, *args, **kwargs):
		choice_a = '27 ohms +/- 5%*'
		choice_b = '270 ohms +/- 5%'
		choice_c = '270 ohms +/- 10%'
		choice_d = '27 ohms +/- 10%'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A carbon-film resistor is color-coded with red, violet, black, and gold stripes. What are its resistance and tolerance?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'three-terminal device used to vary the voltage in a circuit*'
		choice_b = 'two-terminal device used to vary the current in a circuit'
		choice_c = 'fixed resistor'
		choice_d = 'two-terminal device used to vary the voltage in a circuit'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A potentiometer is a"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_8:
	def __init__(self, *args, **kwargs):
		choice_a = '1500 ohms +/- 1.25%'
		choice_b = '152 ohms +/- 1%'
		choice_c = '1521 ohms +/- 0.5%'
		choice_d = '1520 ohms +/- 0.25%*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A metal-film resistor is color-coded with brown, green, red, brown, and blue stripes. What are its resistance and tolerance?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'wire-wound resistors'
		choice_b = 'carbon-composition resistors'
		choice_c = 'surface-mount resistors*'
		choice_d = 'potentiometers'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following resistors has the smallest physical size?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'resistors always have axial leads'
		choice_b = 'resistors are always made from carbon'
		choice_c = 'there is no correlation between the physical size of a resistor and its resistance value*'
		choice_d = 'the shelf of a resistor is about 1 year'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following statements si true?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'increases with an increase in operating temperature'
		choice_b = 'decreases with a decrease in operating temperature'
		choice_c = 'decreases with an increase in operating temperature*'
		choice_d = 'is unaffected by its operating temperature'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If a thermistor has a negative temperature coefficient (NTC), its resistance"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'fractional multiplier of 0.01'
		choice_b = 'fractional multiplier of 0.1*'
		choice_c = 'decimal multiplier of 10'
		choice_d = 'resistor tolerance of +/- 10%'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With the four-band resistor color code, gold in the third stripe corresponds to a"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'wire-wound resistors'
		choice_b = 'carbon-composition resistors'
		choice_c = 'carbon-film resistors'
		choice_d = 'metal-film resistors*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following axial-lead resistor types usually has a blue, light green, or red body?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_14:
	def __init__(self, *args, **kwargs):
		choice_a = '4.7 ohms*'
		choice_b = '4.7 kohms'
		choice_c = '4.7 Mohms'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A surface-mound resistor has a coded value of 4R7. This indicates a resistance of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_2_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'well within tolerance'
		choice_b = 'out of tolerance*'
		choice_c = 'right on the money'
		choice_d = 'close enough to be considered within tolerance'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Reading from left to right, the colored bands on a resistor are yellow, voilet, brown and gold. If the resistor measures 513 ohm with an ohmmeter, it is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_1:
	def __init__(self, *args, **kwargs):
		choice_a = '0.24 A'
		choice_b = '2.4 mA'
		choice_c = '24 mA*'
		choice_d = '24 uA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With 24 V across a 1kohm resistor, the current I equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_2:
	def __init__(self, *args, **kwargs):
		choice_a = '360 mV'
		choice_b = '3.6 kV'
		choice_c = '0.036 V'
		choice_d = '3.6 V*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With 30 uA of current in a 120 kohm resistor, the voltage V equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""
		
class grobs_3_3:
	def __init__(self, *args, **kwargs):
		choice_a = '30 kohms*'
		choice_b = '3 Mohms'
		choice_c = '300 kohms'
		choice_d = '3 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the resistance in a circuit if 15V of potential difference produces 500 uA of current?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class grobs_3_4:
	def __init__(self, *args, **kwargs):
		choice_a = '1 A'
		choice_b = '1 mA*'
		choice_c = '0.01 A'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A current of 1000 uA equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_5:
	def __init__(self, *args, **kwargs):
		choice_a = '746 W'
		choice_b = '550 ftlb/s'
		choice_c = 'approximately 3/4 kW'
		choice_d = 'all of the choices*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""One horsepower equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'I and P are inversely related'
		choice_b = 'V and I are directly proportional*'
		choice_c = 'V and I are inversely proportional'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With R constant"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_7:
	def __init__(self, *args, **kwargs):
		choice_a = '1 V x 1 A'
		choice_b = '1 J/s'
		choice_c = '1 C/s'
		choice_d = 'both a and b*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""One watt of power equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_8:
	def __init__(self, *args, **kwargs):
		choice_a = '1 W'
		choice_b = '2 W'
		choice_c = '4 W*'
		choice_d = '10 W'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 10 ohm resistor dissipates 1 W of power when connected to a dc voltage source. If the value of dc voltage is doubled, resistor will dissipate"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class grobs_3_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'inversely proportional to resistance*'
		choice_b = 'directly proportional to resistance'
		choice_c = 'the same for all values of resistance'
		choice_d = 'both a and b'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If the voltage across a variable resistance is held constant, the current, I, is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_10:
	def __init__(self, *args, **kwargs):
		choice_a = '2.7 kohms, 1/8 W'
		choice_b = '270 ohms, 1/2 W'
		choice_c = '2.7 kohms, 1/2 W*'
		choice_d = '2.7 kohms, 1/4 W'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A resistor must provide a voltage drop of 27 V when the current is 10 mA. Which of the following resistors will provide the required resistance and appropriate wattage rating?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'approximately 0 ohms'
		choice_b = 'infinitely high*'
		choice_c = 'very low'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The resistance of an open circuit is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'normally very high because the resistance of an open circuit is 0 ohms'
		choice_b = 'usually high enough to blow a circuit fuse'
		choice_c = 'zero*'
		choice_d = 'slightly'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The current in an open circuit is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'Keep yourself well insulated from earth ground'
		choice_b = 'When making measurements in a live circuit place one hand behind your back or in your pocket'
		choice_c = 'Make resistance measurements only in a live circuit'
		choice_d = 'both A and B*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""Which of the following safety rules should be observed while working on a live electric circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_14:
	def __init__(self, *args, **kwargs):
		choice_a = '625 mA*'
		choice_b = '1.6 A'
		choice_c = '160 mA'
		choice_d = '62.5 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much current does a 75-W lightbulb draw from the 120-V power line?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'infinitely high'
		choice_b = 'very high'
		choice_c = 'usually above 1 kohms'
		choice_d = 'approximately zero*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The resistance of a short circuit is """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_16:
	def __init__(self, *args, **kwargs):
		choice_a = 'lightbulb'
		choice_b = 'thermistor'
		choice_c = '1-kohms, 1/2-W carbon-film resistor*'
		choice_d = 'both a and b'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""Which of the following is considered a linear resistance?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_17:
	def __init__(self, *args, **kwargs):
		choice_a = '$3.36*'
		choice_b = '33 cents'
		choice_c = '$8.24'
		choice_d = '$4.80'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much will it cost to operate a 4-kW air conditioner for 12 hours if the cost of electricity is 7 cents/kWh?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_18:
	def __init__(self, *args, **kwargs):
		choice_a = '18.75 V'
		choice_b = '4.33 V*'
		choice_c = '6.1 V'
		choice_d = '150 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is the maximum voltage a 150-ohm, 1/8 W resistor can safely handle without exceeding its power rating? ( Assume no power rating safety factor)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_19:
	def __init__(self, *args, **kwargs):
		choice_a = '12 V'
		choice_b = '10,000 mV'
		choice_c = '120 V*'
		choice_d = '9 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following voltages provides the greatest danger in terms of electric shock"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_3_20:
	def __init__(self, *args, **kwargs):
		choice_a = 'zero*'
		choice_b = 'much higher'
		choice_c = 'the same as normal'
		choice_d = 'excessively high'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If short circuit is placed across the leads of a resistor, the current in the resistor itself would be"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_1:
	def __init__(self, *args, **kwargs):
		choice_a = '1.8 kohms'
		choice_b = '20 kohms'
		choice_c = '2 kohms*'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Three resistor in series have individual values of 120 ohms, 680 ohms, and 1.2 kohms. How much is the total resistance, R1"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'different in each resistor'
		choice_b = 'the same everywhere*'
		choice_c = 'the highest near the positive and negative terminals of the voltage source'
		choice_d = 'different at all points along the circuit'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In a series circuit, the current I, is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'the largest voltage drop*'
		choice_b = 'the smallest voltage drop'
		choice_c = 'more current than the other resistors'
		choice_d = 'both a and c'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""In a series circuit, the largest resistance has"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'the direction of current through the resistor*'
		choice_b = 'the large the resistance is'
		choice_c = 'how close the resistor is to the voltage source'
		choice_d = 'how far away the resistor is from the voltage source'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The polarity of a resistor's voltage drop is determined by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_5:
	def __init__(self, *args, **kwargs):
		choice_a = '18 V'
		choice_b = '12 V'
		choice_c = '30 V*'
		choice_d = 'It cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 10-ohm and 15-ohm resistor are in series across a dc voltage source. If the 10-ohm resistor has a voltage drop of 12 V, how much voltage is the applied voltage?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'the full applied voltage '
		choice_b = 'the voltage is slightly higher than normal'
		choice_c = '0 V*'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the voltage across a shorted component in a series circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'the full applied voltage*'
		choice_b = 'the voltage is slightly lower than normal'
		choice_c = '0 V'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the voltage across an open component in a series circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_8:
	def __init__(self, *args, **kwargs):
		choice_a = '90 V'
		choice_b = '30 V*'
		choice_c = '120 V'
		choice_d = 'It cannot be determined.'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A voltage of 120 V is applied across two resistors R1 and R2, in series. If the voltage across R2 equals 90 V, how much is the voltage acros R1?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_9:
	def __init__(self, *args, **kwargs):
		choice_a = '0 V*'
		choice_b = '18 V'
		choice_c = '9 V'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If two series-opposing voltages, each have a voltage of 9 V, the net or total voltage is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'hot spots on the chassis'
		choice_b = 'the locations in the circuit where electrons accumulate'
		choice_c = 'a common return path for current in one or more circuits*'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""On a schematic diagram, what does the chassis ground symbol represent?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage at point G with respect to B'
		choice_b = 'the voltage at point B with respect to point G*'
		choice_c = 'the battery (b) or the generator (g) voltage'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The notation V_BG means"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'decreases'
		choice_b = 'stays the same'
		choice_c = 'increases*'
		choice_d = 'drops to zero'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If a resistor in a series circuit is shorted, the series current, I,"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_13:
	def __init__(self, *args, **kwargs):
		choice_a = '- 3V'
		choice_b = '+ 3V'
		choice_c = '0 V'
		choice_d = '15 V*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 6-V and 9-V source are connected in a series-aiding configuration. How much is the net or total voltgae?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

		self.question = f"""A 6-V and 9-V source are connected in a series-aiding configuration. How much is the net or total voltage?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_14:
	def __init__(self, *args, **kwargs):
		choice_a = '138 ohms'
		choice_b = '62 ohms*'
		choice_c = '26 ohms'
		choice_d = 'It cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 56-ohm and 82-ohm resistor are in series with an unknown resistor. If the total resistance of the series combination is 200 ohm, what is the value of the unknown resistor?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'infinite ohms*'
		choice_b = 'zero ohms'
		choice_c = 'RT is much lower than normal'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the total resistance, RT, of a series circuit if one of the resistors is open?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_16:
	def __init__(self, *args, **kwargs):
		choice_a = 'each good resistor hs the full value of the applied voltage'
		choice_b = 'the applied voltage is split evenly among the good resistors'
		choice_c = '0 V*'
		choice_d = 'It cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If a resistor in a series circuit becomes open, how much is the voltage across each of the remaining resistors that are still good?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_17:
	def __init__(self, *args, **kwargs):
		choice_a = 'the 5-ohm resistor'
		choice_b = 'the 10-ohm resistor*'
		choice_c = 'it depends on how much the current is'
		choice_d = 'they will both dissipate the same amount of power'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 5-ohm and 10-ohm resistor are connected in series across a dc voltage source. Which resistor will dissipate more power?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_18:
	def __init__(self, *args, **kwargs):
		choice_a = 'PT = P1 + P2 + P3 + ... + etc'
		choice_b = 'PT = V_T x I'
		choice_c = 'PT = I^2 R_T'
		choice_d = 'all of the choices*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following equations can be used to determine the total power in a series circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_19:
	def __init__(self, *args, **kwargs):
		choice_a = 'positive on the side where electrons enter and negative on the side where they leave'
		choice_b = 'negative on the side were electrons enter and positive on the side where they leave*'
		choice_c = 'opposite to that obtained with conventional current flow'
		choice_d = 'both b and c'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""Using the electron flow, the polarity of a resistor's voltage drop is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_4_20:
	def __init__(self, *args, **kwargs):
		choice_a = 'the fork symbol'
		choice_b = 'the arrow down symbol'
		choice_c = 'the triple line symbol*'
		choice_d = 'the battery symbol'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The schematic symbol for earth ground is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_1:
	def __init__(self, *args, **kwargs):
		choice_a = '72 kohms*'
		choice_b = '300 kohms'
		choice_c = '360 kohms'
		choice_d = '90 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 120 - kohm resistor R1, and a 180-kohm resistor R2 are in parallel. How much is the equivalent resistance REQ?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'the 300-ohm resistor'
		choice_b = 'both resistors dissipate the same amount of power'
		choice_c = 'the 100-ohm resistor*'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 100-ohm resistor R1, and a 300-ohm resistor R2, are in parallel across a dc voltage source. Which resistor dissipates more power?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class grobs_5_3:
	def __init__(self, *args, **kwargs):
		choice_a = '54 ohms'
		choice_b = '6 ohms*'
		choice_c = '9 ohms'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Three 18-ohm resistors are in parallel. How much is the equivalent resistance REQ?"""

		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage is the same across all branches in a parallel circuit'
		choice_b = 'the equivalent resistance REQ, of a parallel circuit is always smaller than the smallest branch resistance'
		choice_c = 'in a parallel circuit the total current, IT, in the main line equals the sum of the individual branch currents'
		choice_d = 'the equivalent resistance REQ of a parallel circuit decreases when one or more parallel branches are removed from the circuit*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following statements about parallel circuits is false?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_5:
	def __init__(self, *args, **kwargs):
		choice_a = '6 A'
		choice_b = '2 A*'
		choice_c = '4 A'
		choice_d = 'it cannot be determined.'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Two resistors, R1 and R2, are in parallel with each other and a dc voltage source. If the total current, IT, in the main line equals 6 A and I2 through R2 is 4 A, how much is I1 through R1?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_6:
	def __init__(self, *args, **kwargs):
		choice_a = '360 ohm'
		choice_b = '480 ohm'
		choice_c = '1.8 kohms'
		choice_d = '180 ohm*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much resistance must be connected in parallel with a 360-ohm resistor to obtain an equivalent resistance, REQ, of 120 ohms"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'all remaining branch currents increase'
		choice_b = 'the voltage across the open branch will be 0V'
		choice_c = 'the remaining branch currents do not change in value*'
		choice_d = 'the equivalent resistance of the circuit decreases'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If on branch of a parallel circuit becomes open,"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_8:
	def __init__(self, *args, **kwargs):
		choice_a = '250 mS*'
		choice_b = '58 S'
		choice_c = '4 ohm'
		choice_d = '0.25 uS'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If 10-ohm R1, 40-ohm R2, and 8-ohm R3 are in parallel, calculate the total conductance, GT, of the circuit."""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'PT = VA x IT'
		choice_b = 'PT = P1 + P2 + P3 + ... + etc'
		choice_c = 'PT = VA^2 / REQ'
		choice_d = 'all of the choices*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following formulas can be used to determine the total power PT dissipated by a parallel circuit"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'approximately zero ohms*'
		choice_b = 'infinite ohms'
		choice_c = '12.5 ohms'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 20-ohm R1, 50-ohm R2, and 100-ohm R3 are connected in parallel. If R2 is short-circuited, what is the equivalent resistance REQ, of the circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage across each branch will be zero volts'
		choice_b = 'the current in each branch will be zero'
		choice_c = 'the current in each branch will increase to offset the decrease in total current'
		choice_d = 'both a and b*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""If the fuse in the main line of a parallel circuit opens"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_12:
	def __init__(self, *args, **kwargs):
		choice_a = '16 mA'
		choice_b = '40 mA*'
		choice_c = '9.6 mA'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 100-ohm R1, and a 150-ohm R2 are in parallel. If the current I1, through 1 is 24 mA, much is the total current, IT?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_13:
	def __init__(self, *args, **kwargs):
		choice_a = '16.5 V'
		choice_b = '24.75 V'
		choice_c = '9.9 V*'
		choice_d = '41.25 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 2.2-kohm R1 is in parallel with a 3.3-kohm R2. If these two resistors carry a total current of 7.5 mA, how much is the applied voltage, VA?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_14:
	def __init__(self, *args, **kwargs):
		choice_a = '15'
		choice_b = '8*'
		choice_c = '12'
		choice_d = '6'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How many 120-ohm resistors must be connected in parallel to obtained an equivalent resistance, REQ, of 15 ohms?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'REQ doubles'
		choice_b = 'REQ cuts in half'
		choice_c = 'REQ does not change*'
		choice_d = 'REQ increase but is not double its original value'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A 220-ohm R1, 2.2-kohms R2, and 200-ohms R3 are connected across 15 V of applied voltage. What happens to REQ is the applied voltage is doubled to 30 V?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_16:
	def __init__(self, *args, **kwargs):
		choice_a = 'does not change'
		choice_b = 'decreases*'
		choice_c = 'increases'
		choice_d = 'goes to zero'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If one branch of a parallel circuit opens, the total current IT"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_17:
	def __init__(self, *args, **kwargs):
		choice_a = 'independent of each other*'
		choice_b = 'not affected by the value of the applied voltage'
		choice_c = 'larger than the total current IT'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In a normally operating parallel circuit, the individually branch currents are"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_18:
	def __init__(self, *args, **kwargs):
		choice_a = '500 ohms'
		choice_b = '200 kohms'
		choice_c = '5 kohms*'
		choice_d = '500 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If the total conductance GT, of a parallel circuit is 200 uS, how much is REQ?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_19:
	def __init__(self, *args, **kwargs):
		choice_a = 'the fuse in the main line will blow'
		choice_b = 'the voltage across the short-circuited branch will measure the full value of applied voltage'
		choice_c = 'all the remaining branches are effectively short-circuited as well'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""If one branch of a parallel circuit is short-circuited,"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_5_20:
	def __init__(self, *args, **kwargs):
		choice_a = '144 ohms'
		choice_b = '90 ohm*'
		choice_c = '213.3 ohm'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Two lightbulbs in parallel with the 120-V power line are rated at 60W and 100W, respectively. What is the equivalent, REQ, of the bulbs when they are lit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'R1 and R2 are in series'
		choice_b = 'R3 and R4 are in series'
		choice_c = 'R1 and R4 are in series*'
		choice_d = 'R2 and R4 are in series'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'R2, R3 and VT are in parallel'
		choice_b = 'R2 and R3 are in parallel*'
		choice_c = 'R2 and R3 are in series'
		choice_d = 'R1 and R4 are in parallel'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_3:
	def __init__(self, *args, **kwargs):
		choice_a = '1.6 kohms*'
		choice_b = '3.88 kohms'
		choice_c = '10 kohms'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		
		The total resistance RT is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_4:
	def __init__(self, *args, **kwargs):
		choice_a = '6.19 mA'
		choice_b = '150 mA'
		choice_c = '15 mA*'
		choice_d = '25 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		
		The total current It equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_5:
	def __init__(self, *args, **kwargs):
		choice_a = '12 V'
		choice_b = '18 V'
		choice_c = '13.8 V'
		choice_d = '10.8 V*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		
		How much voltage is across points A and B?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_6:
	def __init__(self, *args, **kwargs):
		choice_a = '9 mA'
		choice_b = '15 mA'
		choice_c = '6 mA*'
		choice_d = '10.8 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		how much is I2 through R2?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_7:
	def __init__(self, *args, **kwargs):
		choice_a = '9 mA*'
		choice_b = '15 mA'
		choice_c = '6 mA'
		choice_d = '45 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		how much is I3 through R3?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_8:
	def __init__(self, *args, **kwargs):
		choice_a = 'increases*'
		choice_b = 'decreases'
		choice_c = 'stays the same'
		choice_d = 'increases to 24 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png
		If R4 shorts, the voltage VAB"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage across points A and B will decrease'
		choice_b = 'the resistors R1, R3 and R4 will be in series*'
		choice_c = 'the total resistance RT will decrease'
		choice_d = 'the voltage across points A and B will measure 24 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If R2 becomes open
		https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage across R1 will measure 0 V'
		choice_b = 'the voltage across R4 will measure 0 V'
		choice_c = 'the voltage across points A and B will measure 0 V'
		choice_d = 'both b and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""If R1 opens in
		https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'it decreases'
		choice_b = 'it increases*'
		choice_c = 'it stays the same'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""IF R3 becomes open, what happens to the voltage across points A and B?
		https://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage VAB decreases to 0 V'
		choice_b = 'the total current IT flows through R3'
		choice_c = 'the current I3 in R3 will be zero'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""If R2 shortshttps://lesliecaminadecom.files.wordpress.com/2019/09/tkjfsaybh7qz4jh7qs2k.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_13:
	def __init__(self, *args, **kwargs):
		choice_a = '0 V*'
		choice_b = '10.9 V'
		choice_c = '2.18 V'
		choice_d = '12 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much voltage exists between terminals C and D when the bridge is balanced?
		https://lesliecaminadecom.files.wordpress.com/2019/09/m635q80dv7wge95fw0f4.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_14:
	def __init__(self, *args, **kwargs):
		choice_a = '55 943 ohms'
		choice_b = '559.43 ohms'
		choice_c = '5594.3 ohms*'
		choice_d = '10 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Assume that the current in M1 is zero when RS is adjusted to 55,943 ohms. What is the value of the unknown resistor RX?
		https://lesliecaminadecom.files.wordpress.com/2019/09/m635q80dv7wge95fw0f4.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'zero'
		choice_b = 'approximately 727.27 uA'
		choice_c = 'approximately 1.09 mA'
		choice_d = 'approximately 1.82 mA*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Assume that the bridge is balanced when RS is adjusted to 15,000 ohms. How much is the total current I_T flowing to and from the terminals of the voltage source VT?
		https://lesliecaminadecom.files.wordpress.com/2019/09/m635q80dv7wge95fw0f4.png
		"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_16:
	def __init__(self, *args, **kwargs):
		choice_a = '99.99 ohms'
		choice_b = '9,999.9 ohms*'
		choice_c = '99,999 ohms'
		choice_d = '999,999 ohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is the maximum unknown resistor RX(max) that can be measured for the resistor values shown in the ratio arm?
		https://lesliecaminadecom.files.wordpress.com/2019/09/m635q80dv7wge95fw0f4.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_17:
	def __init__(self, *args, **kwargs):
		choice_a = 'the placement accuracy of the measurement of RX'
		choice_b = 'the maximum unknown resistor RX(max) that can be measured'
		choice_c = 'the amount of voltage available across the terminals A and B'
		choice_d = 'both a and b*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""the ratio R1/R2 determines
		https://lesliecaminadecom.files.wordpress.com/2019/09/m635q80dv7wge95fw0f4.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_18:
	def __init__(self, *args, **kwargs):
		choice_a = '1.1 V'
		choice_b = '0 V'
		choice_c = '10.9 V*'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Assume that the standard resistor RS has been adjusted so that the current in M1 is exactly 0 uA. How much voltage exists at terminal C with respect to B?
		https://lesliecaminadecom.files.wordpress.com/2019/09/m635q80dv7wge95fw0f4.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_19:
	def __init__(self, *args, **kwargs):
		choice_a = '339.5 kohms*'
		choice_b = '3.395 kohms'
		choice_c = '33,950 ohms'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Assume that the ratio arm resistors, R1 and R2, are interchanged. What is the value of the unknown resistor, RX, if RS equals 33,950 ohms when the bridge is balanced?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_6_20:
	def __init__(self, *args, **kwargs):
		choice_a = 'change the ratio arm fraction R1/R2 from 1/10 to 1/100 or something else'
		choice_b = 'change the ratio arm fraction, R1/R2 from 1/10 to 1/1, 10/1 or something greater*'
		choice_c = 'reverse the polarity of the applied voltage, VT'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Assume that the standard resistor RS cannot be adjusted high enough to provide a balanced condition. What modification must be made to the circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'inverse proportional to the series resistance values'
		choice_b = 'proportional to the series resistance values*'
		choice_c = 'unrelated to the series resistance values'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In a series circuit, the individual resistor voltage drops are"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'not related to the branch resistance values'
		choice_b = 'directly proportional to the branch resistance values'
		choice_c = 'inversely proportional to the branch resistance values*'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In a parallel circuit, the individual branch currents are """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_3:
	def __init__(self, *args, **kwargs):
		choice_a = '8 V*'
		choice_b = '16 V'
		choice_c = '4 V'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Three resistor R1, R2, and R3 are connected in series across an applied voltage, VT, of 24 V. If R2 is one-third the value of RT, how much is V2?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_4:
	def __init__(self, *args, **kwargs):
		choice_a = '1 A'
		choice_b = '2 A'
		choice_c = '3 A'
		choice_d = '4 A*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Two resistors R1 and R2 are in parallel. If R1 is twice the value of R2, how much is I2 in R2 if IT equals 6 A?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_5:
	def __init__(self, *args, **kwargs):
		choice_a = '1 A'
		choice_b = '2 A*'
		choice_c = '3 A'
		choice_d = '4 A'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Two resistors R1 and R2 are in parallel. If the conductance, G1, of R1 is twice the value of the conductance, G2 of R2, how much is I2 if IT = 6 A?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_6:
	def __init__(self, *args, **kwargs):
		choice_a = '400 mA*'
		choice_b = '300 mA'
		choice_c = '100 mA'
		choice_d = '500 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is I1 in R1?https://lesliecaminadecom.files.wordpress.com/2019/09/r6s2j3c9fz0ctiv91y6b.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_7:
	def __init__(self, *args, **kwargs):
		choice_a = '500 mA'
		choice_b = '400 mA'
		choice_c = '100 mA*'
		choice_d = '300 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the bleeder current IB?
		https://lesliecaminadecom.files.wordpress.com/2019/09/r6s2j3c9fz0ctiv91y6b.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_8:
	def __init__(self, *args, **kwargs):
		choice_a = '500 mA*'
		choice_b = '400 mA'
		choice_c = '100 mA'
		choice_d = '300 mA'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the total current IT?
		https://lesliecaminadecom.files.wordpress.com/2019/09/r6s2j3c9fz0ctiv91y6b.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_9:
	def __init__(self, *args, **kwargs):
		choice_a = '18 V'
		choice_b = '19.2 V'
		choice_c = '6 V'
		choice_d = '22.15 V*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is the voltage, VBG, if load B becomes open?
		https://lesliecaminadecom.files.wordpress.com/2019/09/r6s2j3c9fz0ctiv91y6b.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_7_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'it increases'
		choice_b = 'it decreases'
		choice_c = 'it remains the same*'
		choice_d = 'it cannot be determine'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What happens to the voltage VBG, if load A becomes open?
		https://lesliecaminadecom.files.wordpress.com/2019/09/r6s2j3c9fz0ctiv91y6b.png"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class grobs_8_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'the amount of current needed in the moving coil to produce full scale deflection of the meter\'s pointer*'
		choice_b = 'the value of current flowing in the moving-coil for any amount of pointer deflection'
		choice_c = 'the amount of current required in the moving-coil to produce half-scale deflection of the meter\'s pointer'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""For a moving-coil meter movement IM is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'the pointer deflection will be magnified by the mirror when measuring small values of voltage, current, and resistance'
		choice_b = 'the meter should always be read by looking at the meter from the side'
		choice_c = 'the meter is read when the pointer and its mirror reflection appear as one*'
		choice_d = 'both a and b'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""For an analog VOM with a mirror along the printed scale"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'very high internal resistance'
		choice_b = 'very low internal resistance*'
		choice_c = 'infinitely high internal resistance'
		choice_d = 'none of the above'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A current meter should have a"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'resistance of about 0 ohms'
		choice_b = 'very low resistance'
		choice_c = 'very high internal resistance*'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A voltmeter should have a """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_5:
	def __init__(self, *args, **kwargs):
		choice_a = 'parallel circuits'
		choice_b = 'low-resistance circuit'
		choice_c = 'a series circuit with low resistance values'
		choice_d = 'high resistance circuits*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Voltmeter loading is usually a problem when measuring voltages in """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_6:
	def __init__(self, *args, **kwargs):
		choice_a = '2 kohms*'
		choice_b = '1 kohm'
		choice_c = '18 kohms'
		choice_d = '50 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""To double the current range of a 50 uA, 2 kohm moving coil meter movement the shunt resistance, RS, should be"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_7:
	def __init__(self, *args, **kwargs):
		choice_a = '20 kohms/volt'
		choice_b = '50 kohms/volt*'
		choice_c = '1 kohm/volt'
		choice_d = '10 Mohm/volt'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A voltmeter using a 20 uA meter movement has an ohm/volt rating of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_8:
	def __init__(self, *args, **kwargs):
		choice_a = 'decreases*'
		choice_b = 'increases'
		choice_c = 'stays the same'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""As the current range of an analog meter is increased, the overall meter resistance, RM"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'decreases'
		choice_b = 'increases*'
		choice_c = 'stays the same'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""As the voltage range of an analog VOM is increased, the total voltmeter resistance RV"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_10:
	def __init__(self, *args, **kwargs):
		choice_a = '10 kohms'
		choice_b = '10 Mohms'
		choice_c = '25 kohms'
		choice_d = '250 kohms*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""An analog VOM has an ohm/volt rating of 10kohm/V. What is the voltmeter resistance, RV, if the voltmeter is set to the 25-V range?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_11:
	def __init__(self, *args, **kwargs):
		choice_a = '25 ohm'
		choice_b = '10.2 ohm'
		choice_c = '20.41 ohm*'
		choice_d = '1 kohm'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What shunt resistance, RS, is needed to make a 100 uA, 1kohm meter movement capable of measuring currents from 0 to 5 mA?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_12:
	def __init__(self, *args, **kwargs):
		choice_a = '58 kohms'
		choice_b = '598 kohms*'
		choice_c = '10 Mohms'
		choice_d = '600 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""For a 30-V range, a 50-uA, 2kohm meter movement needs a multiplier resistor of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'about zero ohms'
		choice_b = '20 kohms'
		choice_c = '10 MOhms*'
		choice_d = '1 kohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When set to any of the voltage ranges, a typical DMM has an input resistance of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_14:
	def __init__(self, *args, **kwargs):
		choice_a = 'the power in the circuit being tested must be off*'
		choice_b = 'the power in the circuit being tested must be on'
		choice_c = 'the power in the circuit being tested may be on or off'
		choice_d = 'the power in the circuit being tested should be turned on after the leads are connected'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When using an ohmmeter to measure resistance in a circuit"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_15:
	def __init__(self, *args, **kwargs):
		choice_a = '7.64 V'
		choice_b = '13.5 V'
		choice_c = '19.98 V'
		choice_d = '29.98 V*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following voltages cannot be displayed by a DMM with a 3 1/2 digit display"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_16:
	def __init__(self, *args, **kwargs):
		choice_a = 'An analog VOM'
		choice_b = 'An amp-clamp probe*'
		choice_c = 'A DMM'
		choice_d = 'There isn\'t such a meter'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What type of meter can be used to measure ac currents without breaking open the circuit?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_17:
	def __init__(self, *args, **kwargs):
		choice_a = 'resistance measurements'
		choice_b = 'dc voltage measurements'
		choice_c = 'current measurements*'
		choice_d = 'ac voltage measurements'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following measurements is usually the most inconvinient and time-consuming when troubleshooting?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_18:
	def __init__(self, *args, **kwargs):
		choice_a = '180 kohms*'
		choice_b = '18 kohms'
		choice_c = '18 ohms'
		choice_d = '180 ohms'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""An analog ohmmeter reads 18 on the R x 10k range. What is the value of the measured resistance?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_19:
	def __init__(self, *args, **kwargs):
		choice_a = 'the DMM'
		choice_b = 'the analog VOM*'
		choice_c = 'they both have the same resistance'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which meter has a higher resistance, A DMM with 10 Mohm of resistance on all dc voltage ranges or an analog VOm ith a 50 kohms/V rating set to the 250-V range?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_8_20:
	def __init__(self, *args, **kwargs):
		choice_a = 'about 0 ohms if the wire is good'
		choice_b = 'infinity if the wire is broken'
		choice_c = 'very high resistance if the wire is good'
		choice_d = 'both a and b*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""When using an ohmmeter to measure the continuity of a wire, the resistance should measure"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'the algebraic sum of the currents flowing into any point in a circuit must equal zero'
		choice_b = 'the algebraic sum of the currents entering and leaving any point in a circuit must equal zero*'
		choice_c = 'the algebraic sum of the currents flowing away from any point in a circuit must equal zero'
		choice_d = 'the algebraic sum of the currents around any closed path must equal zero'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Kirchoff's current law states that"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'consider all currents flowing into a branch point positive and all currents directed away from that point negative*'
		choice_b = 'consider all currents flowing into a branch point negative and all currents directed away from that point positive'
		choice_c = 'remember that the total of all the currents entering a branch point must always be greater than the sum of the currents leaving that point'
		choice_d = 'the algebraic sum of the currents entering and leaving a branch point does not necessarily have to be zero'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When applying Kirchoff's current law"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_3:
	def __init__(self, *args, **kwargs):
		choice_a = '7 A'
		choice_b = '30 A'
		choice_c = '13 A*'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If a 10-A I1 and a 3-A I2 flow into point X, how much current must flow away from point X?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_4:
	def __init__(self, *args, **kwargs):
		choice_a = '21.5 A'
		choice_b = '14.5 A'
		choice_c = '26.5 A'
		choice_d = '9.5 A*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Three currents I1, I2, and I3 flow into point X, whereas current I4 flows away from point X. If I1 = 2.5 A, I3 = 6 A, and I4 = 18 A, how much is current I2?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_5:
	def __init__(self, *args, **kwargs):
		choice_a = 'node'
		choice_b = 'principal node'
		choice_c = 'loop*'
		choice_d = 'branch point'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When applying Kirchoff's voltage law, a closed path is commonly referred to as a """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'the algebraic sum of the voltage sources and IR voltage drops in any closed path must total zero.*'
		choice_b = 'the algebraic sum of the voltage sources and IR voltage drops around any closed path can never equal zero.'
		choice_c = 'the algebraic sum of all the currents fl owing around any closed loop must equal zero.'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Kirchoff's voltage law states that"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'consider any voltage whose positive terminal is reached first as negative and any voltage whose negative terminal is reached fi rst as positive.'
		choice_b = 'consider any voltage whose positive terminal is reached first as negative and any voltage whose negative terminal is reached fi rst as positive.'
		choice_c = 'consider any voltage whose negative terminal is reached first as negative and any voltage whose positive terminal is reached fi rst as positive.*'
		choice_d = 'always consider all resistor voltage drops as positive and all voltage sources as negative.'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When applying Kirchoff's voltage law"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_8:
	def __init__(self, *args, **kwargs):
		choice_a = '- 10 V'
		choice_b = '+ 10 V*'
		choice_c = '+ 70 V'
		choice_d = '- 70 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The algebraic sum of + 40 V and - 30 V is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'a closed path or loop where the algebraic sum of the voltages must equal zero.'
		choice_b = 'the simplest possible closed path around a circuit.'
		choice_c = 'a junction where branch currents can combine or divide.*'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A principal node is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_10:
	def __init__(self, *args, **kwargs):
		choice_a = '3'
		choice_b = '2'
		choice_c = '4'
		choice_d = '1*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How many equations are necessary to solve a circuit with two principal nodes?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'a mesh current is an assumed current and a branch current is an actual current.'
		choice_b = 'the direction of the currents themselves.'
		choice_c = 'a mesh current does not divide at a branch point.'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The difference between a mesh current and a branch current is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'two opposing mesh currents*'
		choice_b = 'one common mesh current'
		choice_c = 'zero current'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Using the method of mesh currents, any resistance common to two meshes has"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'Kirchoff\'s current law'
		choice_b = 'node-voltage analysis'
		choice_c = 'Kirchoff\'s voltage law*'
		choice_d = 'the method of mesh currents'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The fact that the sum of the resistor voltage drops equals the applied voltage in a series circuit is the basis for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_14:
	def __init__(self, *args, **kwargs):
		choice_a = 'Kirchoff\'s current law*'
		choice_b = 'node-voltage analysis'
		choice_c = 'Kirchoff\'s voltage law'
		choice_d = 'the method of mesh currents'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The fact that the sum of the individual branch currents equals the total current in a parallel circuit is the basis for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_9_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'the algebraic sum of the voltages will always be positive'
		choice_b = 'the algebraic sum is the voltage between the start and finish points*'
		choice_c = 'the algebraic sum of the voltages will always be negative'
		choice_d = 'the algebraic sum of the voltages cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If you do not go completely around the loop when applying Kirchoff's voltage law, then"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'bilateral component'
		choice_b = 'active component'
		choice_c = 'passive component'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""A resistor is an example of a(n)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'the active type'
		choice_b = 'both linear and bilateral*'
		choice_c = 'grounded'
		choice_d = 'both nonlinear and unidirectional'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""To apply the superposition theorem, all the components must be"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'RN and RTH have the same value*'
		choice_b = 'RN will always be larger than RTH'
		choice_c = 'IN is short-circuited to find VTH'
		choice_d = 'VTH is short-circuited to find IN'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When converting from a Norton equivalent circuit to a Thevenin equivalent circuit or vice versa,"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'all voltage sources must be opened'
		choice_b = 'all voltage source must be short-circuited*'
		choice_c = 'all voltage sources must be converted to current sources'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When solving for the Thevenin equivalent resistance RTH"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_5:
	def __init__(self, *args, **kwargs):
		choice_a = 'a single current source in parallel with a single resistance'
		choice_b = 'a single voltage source in parallel with a single resistance'
		choice_c = 'a single voltage source in series with a single resistance*'
		choice_d = 'a single current source is series with a single resistance'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Using the method of mesh currents, any resistance common to two meshes has"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'a single current source in parallel with a single resistance*'
		choice_b = 'a single voltage source in parallel with a single resistance'
		choice_c = 'a single voltage source in series with a single resistance'
		choice_d = 'a single current source in series with a single resistance'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Norton’s theorem states that an entire network connected to a pair of terminals can be replaced with"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'the voltage across terminals A and B when they are short-circuited'
		choice_b = 'the open-circuit voltage across the terminals A and B*'
		choice_c = 'the same as the voltage applied to the complex network'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With respect to terminals A and B in a complex network, the Thevenin voltage VTH is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_8:
	def __init__(self, *args, **kwargs):
		choice_a = '1 kV'
		choice_b = '10 V'
		choice_c = '1 V*'
		choice_d = 'It cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A Norton equivalent circuit consists of a 100uA current source IN in parallel with a 10kohm resistance RN. If this circuit is converted into a Thevenin equivalent circuit, how much is VTH?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'the current flowing between terminals A and B when they are open'
		choice_b = 'the total current supplied by the applied voltage to the network'
		choice_c = 'zero when terminals A and B are short-circuited'
		choice_d = 'the current flowing between terminals A and B when they are short-circuited*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With respect to terminals A and B in a complex network, the Norton equivalent current IN is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_10_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'superposition theorem'
		choice_b = 'Thevenin\'s theorem'
		choice_c = 'Norton\'s theorem'
		choice_d = 'Millmann\'s theorem*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which theorem provides a shortcut for finding the common voltage across any number of parallel branches with different sources?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'infinity'
		choice_b = 'zero ohms*'
		choice_c = '1 Mohms'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A closed switch has a resistance of approximately"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'infinity*'
		choice_b = 'zero ohms'
		choice_c = '1 to 2 ohms'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""An open fuse has a resistance that approaches"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_3:
	def __init__(self, *args, **kwargs):
		choice_a = '2'
		choice_b = '6'
		choice_c = '3*'
		choice_d = '4'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How many connecting terminals does an SPDT switch have"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'the applied voltage'
		choice_b = 'zero volts*'
		choice_c = 'infinity'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The voltage deop across a closed switch equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_5:
	def __init__(self, *args, **kwargs):
		choice_a = 'the diameter and circular area increase'
		choice_b = 'the wire resistance decreases for a specific length and type'
		choice_c = 'the diameter increases but the circular area remains constant'
		choice_d = 'the diameter and circular area decrease*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""For round wire, as the gauge numbers increase from 1 to 40"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'every 2 gauge sizes'
		choice_b = 'every 3 gauge sizes*'
		choice_c = 'every sucesscive gauge size'
		choice_d = 'every 10 gauge sizes'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The circular area of round wire doubles for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'the 100-ft length of No. 12 gauge aluminum wire*'
		choice_b = 'the 100-ft length of No. 12 gauge copper wire'
		choice_c = 'They both have exactly the same resistance'
		choice_d = 'It cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which has more resistance, a 100-ft length of No.12 gauge copper wire or a 100-ft length of No.12 gauge aluminum wire?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_8:
	def __init__(self, *args, **kwargs):
		choice_a = 'negative temperature coefficient'
		choice_b = 'temperature coefficient of zero'
		choice_c = 'positive temperature coefficient*'
		choice_d = 'very high resistance'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""In their pure form, all metals have a"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'open'
		choice_b = 'either open or closed'
		choice_c = 'closed*'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The current rating of a switch corresponds to the maximum current the switch can safely handle when it is """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'less than 1 ohm'
		choice_b = '20.35 ohms'
		choice_c = '3.33 kohms'
		choice_d = '33.27 ohms*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the resistance of a 2000-ft length No.20 gauge aluminum wire"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_11:
	def __init__(self, *args, **kwargs):
		choice_a = '1'
		choice_b = '2*'
		choice_c = '3'
		choice_d = '4'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How many completely isolated circuits can be controlled by a DPST switch?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'steel'
		choice_b = 'aluminum'
		choice_c = 'silver*'
		choice_d = 'gold'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following metals is the best conductor of electricity?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_13:
	def __init__(self, *args, **kwargs):
		choice_a = '0.001 cmil'
		choice_b = '10 cmil'
		choice_c = '1 cmil'
		choice_d = '100 cmil*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is the area in circular mils (cmils) of a wire whose diameter is 0.01 inches?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_14:
	def __init__(self, *args, **kwargs):
		choice_a = 'the number of completely isolated circuits that can be controlled by the switch*'
		choice_b = 'the number of closed contact positions that the switch has'
		choice_c = 'the number of connecting terminals the switch has'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The term pole as it relates to switches is defined as"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_11_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'the corona effect'
		choice_b = 'hole flow'
		choice_c = 'superconductivity'
		choice_d = 'ionization current*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The motion of ion charges in a liquid or gas is called"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'carbon-zinc'
		choice_b = 'alkaline'
		choice_c = 'zinc chloride'
		choice_d = 'lead-acid*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following cells is not a primary cell?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_2:
	def __init__(self, *args, **kwargs):
		choice_a = '1.2 V'
		choice_b = '1.5 V*'
		choice_c = '2.1 V'
		choice_d = 'about 3 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The dc output voltage of a C-size alkaline cell is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'silver oxide'
		choice_b = 'lead-acid'
		choice_c = 'nickel-cadmium'
		choice_d = 'both b and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""Which of the following is a secondary cell?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'it increases*'
		choice_b = 'it decreases'
		choice_c = 'it stays the same'
		choice_d = 'it usually disappears'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What happens to the internal resistance of a voltaic cell as the cell deteriorates?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_5:
	def __init__(self, *args, **kwargs):
		choice_a = '1.35 V'
		choice_b = '1.5 V'
		choice_c = '2.1 V*'
		choice_d = 'about 12 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The dc output voltage of a lead-acid cell is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'increase the current capacity'
		choice_b = 'increase the voltage output*'
		choice_c = 'decrease the voltage output'
		choice_d = 'decrease the internal resistance'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Cells are connected in series to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'increase the current capacity*'
		choice_b = 'increase the voltage output'
		choice_c = 'decrease the voltage output'
		choice_d = 'decrease the current capacity'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Cells are connected in parallel to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_8:
	def __init__(self, *args, **kwargs):
		choice_a = '1.5 V'
		choice_b = '5.0 V'
		choice_c = '7.5 V*'
		choice_d = '11.0 V'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Five D-size alkaline cells in series have a combined voltage of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'a primary cell can be recharged and a secondary cell cannot'
		choice_b = 'a secondary cell can be recharged and a primary cell cannot*'
		choice_c = 'a primary cell has an unlimited shelf life and a secondary cell does not'
		choice_d = 'primary cells produce a dc voltage and secondary cells produce an ac voltage'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The main difference between a primary cell and a secondary cell is that"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'has very high internal resistance'
		choice_b = 'supplies constant current to any load resistance'
		choice_c = 'has very low internal resistance*'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A constant-voltage source"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'has very low internal resistance'
		choice_b = 'supplies constant current to a wide range of load resistances'
		choice_c = 'has very high internal resistance'
		choice_d = 'both b and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""A constant-current source"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_12:
	def __init__(self, *args, **kwargs):
		choice_a = '12 ohms*'
		choice_b = '108 ohms'
		choice_c = '120 ohms'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The output voltage of a battery drops from 6.0 V with no load to 5.4 V with a load current of 50 mA. How much is the internal resistance ri?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'RL = ri*'
		choice_b = 'RL is maximum'
		choice_c = 'RL is minimum'
		choice_d = 'RL is 10 or more times the value of ri'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Maximum power is transferred from a generator to a load when"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_14:
	def __init__(self, *args, **kwargs):
		choice_a = '100 %'
		choice_b = '0 %'
		choice_c = '50 %*'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is the efficiency of power transfer for the matched load condition?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_12_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'cannot be measured with an ohmmeter'
		choice_b = 'can be measured with an ohmmeter'
		choice_c = 'can be measured directly by determining how much the output voltage drops for a given load current'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""The internal resistance of a battery"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_1:
	def __init__(self, *args, **kwargs):
		choice_a = 'flux density'
		choice_b = 'permeability'
		choice_c = 'magnetic flux*'
		choice_d = 'field intensity'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The maxwell (Mx) is a unit of """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_2:
	def __init__(self, *args, **kwargs):
		choice_a = 'like poles attract each other and unlike poles repel each other'
		choice_b = 'unlike poles attract each other and like poles repel each other*'
		choice_c = 'ther are no north or south poles on the ends of the magnet'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""With bar magnets"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'flux density*'
		choice_b = 'magnetic flux'
		choice_c = 'permeability'
		choice_d = 'magnetomotive force'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The tesla(T) is a unit of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class grobs_13_4:
	def __init__(self, *args, **kwargs):
		choice_a = '1 e8 Wb'
		choice_b = '1 Wb/ m^2'
		choice_c = '1 e4 G'
		choice_d = 'one magnetic field line*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""1 maxwell (Mx) is equal to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_5:
	def __init__(self, *args, **kwargs):
		choice_a = '1 e8 Mx*'
		choice_b = 'one magnetic field line'
		choice_c = '1 Mx/cm2'
		choice_d = '1 e4 kG'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""1 Wb is equal to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'its permeability'
		choice_b = 'induction*'
		choice_c = 'the Hall effect'
		choice_d = 'hysteresis'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The electric or magnetic effect of one body on another without any physical contact between them is called"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'a strong demagnetizing field'
		choice_b = 'a physical shock'
		choice_c = 'high temperatures'
		choice_d = 'all of the choices*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A commercial permanent magnet will last indefinitely if it is not subjected to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_8:
	def __init__(self, *args, **kwargs):
		choice_a = 'lodestone'
		choice_b = 'toroid'
		choice_c = 'ferrite*'
		choice_d = 'solenoid'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""What is the name for a nonmetallic material that has the ferromagnetic properties of iron?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_9:
	def __init__(self, *args, **kwargs):
		choice_a = '1 Mx/m2'
		choice_b = '1 Mx/cm2'
		choice_c = '1 Wb/m2*'
		choice_d = '1 Wb/cm2'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""One tesla (T) is equal to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'induction'
		choice_b = 'permeability*'
		choice_c = 'Hall effect'
		choice_d = 'diamagnetism'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The ability of a material to concentrate magnetic flux is called its"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'south pole*'
		choice_b = 'north pole'
		choice_c = 'it could be either a north pole or a south pole'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""If the north pole of a permanent magnet is placed near a piece of soft iron, what is the polarity of the nearest induced pole?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'permanent magnet'
		choice_b = 'electromagnet'
		choice_c = 'solenoid'
		choice_d = 'both b and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""A magnet that requires current in a coil to create the magnetic field is called a(n)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'melting point'
		choice_b = 'freezing point'
		choice_c = 'Curie temperature*'
		choice_d = 'leakeage point'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The point at which a magnetic material loses its ferromagnetic properties is called the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_14:
	def __init__(self, *args, **kwargs):
		choice_a = 'diamagnetic'
		choice_b = 'ferromagnetic*'
		choice_c = 'paramagnetic'
		choice_d = 'toroidal'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A material that becomes strongly magnetized in the same direction as the magnetizing field is classified as"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'air'
		choice_b = 'wood'
		choice_c = 'glass'
		choice_d = 'all of the choices*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Which of the following materials are non-magnetic?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_16:
	def __init__(self, *args, **kwargs):
		choice_a = 'flux density*'
		choice_b = 'magnetic flux'
		choice_c = 'permeability'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The gauss (G) is a unit of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_17:
	def __init__(self, *args, **kwargs):
		choice_a = '1 Mx/m2'
		choice_b = '1 Wb/cm2'
		choice_c = '1 Mx/cm2*'
		choice_d = '1 Wb/m'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""One gauss(G) is equal to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_18:
	def __init__(self, *args, **kwargs):
		choice_a = '1e8 Mx'
		choice_b = '10,000 mX'
		choice_c = '1e-8 Mx'
		choice_d = '100 Mx*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""1 uWb equals"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_19:
	def __init__(self, *args, **kwargs):
		choice_a = 'is an electromagnet'
		choice_b = 'has no magnetic poles'
		choice_c = 'uses iron for the core around which the coil is wound'
		choice_d = 'all of the choices*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A toroid"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_20:
	def __init__(self, *args, **kwargs):
		choice_a = 'the Doppler effect'
		choice_b = 'the Miller effect'
		choice_c = 'the Hall effect*'
		choice_d = 'the Schultz effect'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""When a small voltage is generated across the width of a conductor carrying current in an external magnetic field, the effect is called"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_21:
	def __init__(self, *args, **kwargs):
		choice_a = 'magnetic flux*'
		choice_b = 'flux density'
		choice_c = 'permeability'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The weber (Wb) is a unit of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_22:
	def __init__(self, *args, **kwargs):
		choice_a = '4'
		choice_b = '250'
		choice_c = '4000*'
		choice_d = 'it cannot be determined'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The flux density in the iron core of an electromagnet is 0.25 T. When the iron core is removed, the flux density drops to 62.5e-6 T. What is the relative permeability of the iron core?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_23:
	def __init__(self, *args, **kwargs):
		choice_a = '50 e-3 T'
		choice_b = '50 G*'
		choice_c = '5000 G'
		choice_d = 'both a and b'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""What is the magnetic flux density B for a magnetic flux of 500 Mx through an area of 10 cm2?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_24:
	def __init__(self, *args, **kwargs):
		choice_a = 'no magnetic polarity'
		choice_b = 'south magnetic polarity*'
		choice_c = 'north magnetic polarity'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The geographic north pole of the earth has """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_13_25:
	def __init__(self, *args, **kwargs):
		choice_a = 'more current and more coil turns mean a stronger magnetic field'
		choice_b = 'less current and fewer coil turns mean a stronger magnetic field'
		choice_c = 'if there is no current in the coil there is no magnetic field'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""With an electromagnet"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_1:
	def __init__(self, *args, **kwargs):
		choice_a = '100 At'
		choice_b = '1 At'
		choice_c = '10 At*'
		choice_d = '7.93 At'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A current of 20mA flowing through a coil with 500 turns produces an mmf of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_2:
	def __init__(self, *args, **kwargs):
		choice_a = '5 mA'
		choice_b = '0.5 A'
		choice_c = '50 uA'
		choice_d = '50 mA*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A coil with 1000 turns must provide an mmf of 50 At. The required current is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_3:
	def __init__(self, *args, **kwargs):
		choice_a = 'if the fingers of the left hand encircle the coil in the same direction as the electron flow, the thumb points in the direction of the north pole*'
		choice_b = 'if the thumb of the left hand points in the direction of current flow, the fingers point toward the north pole'
		choice_c = 'if the fingers of the left hand encircle the coil in the same direction as electron flow, the thumb points in the direction of the south pole'
		choice_d = 'if the thumb of the right hand points in the direction of electron flow, the fingers points in the direction of the north pole'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The left-hand rule for solenoids states that"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_4:
	def __init__(self, *args, **kwargs):
		choice_a = 'Len\'z law'
		choice_b = 'motor action*'
		choice_c = 'the left-hand rule for coils'
		choice_d = 'integration'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The physical motion resulting from the forces of two magnetic fields is called"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class grobs_14_5:
	def __init__(self, *args, **kwargs):
		choice_a = 'a stronger field towards a weaker field*'
		choice_b = 'a weaker field towards a stronger field'
		choice_c = 'a north pole toward a south pole'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Motor action always tends to produce motion from """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_6:
	def __init__(self, *args, **kwargs):
		choice_a = 'a stationary magnetic field'
		choice_b = 'a stationary conductor'
		choice_c = 'a relative motion between the wire and magnetic field*'
		choice_d = 'both a and b'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""A conductor will have an induced current or voltage only when there is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_7:
	def __init__(self, *args, **kwargs):
		choice_a = 'motor action'
		choice_b = 'Lenz\'s law*'
		choice_c = 'the number of turns in the coil'
		choice_d = 'the amount of current in the coil'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The polarity of an induced voltage is determined by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_8:
	def __init__(self, *args, **kwargs):
		choice_a = 'the maximum current rating of the relay coil'
		choice_b = 'the minimum relay coil current required to keep a relay energized'
		choice_c = 'the minimum relay coil current required to energize a relay*'
		choice_d = 'the minimum current in the switching contacts'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""For a relay, the pickup current is defined as"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_9:
	def __init__(self, *args, **kwargs):
		choice_a = 'contacts'
		choice_b = 'relay coil'
		choice_c = 'terminal'
		choice_d = 'armature*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The movable arm of an attraction-type relay is called the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_10:
	def __init__(self, *args, **kwargs):
		choice_a = 'the rate at which the conductor cuts the magnetic flux'
		choice_b = 'the number of magnetic flux lines that are cut by the conductor'
		choice_c = 'the time of day during which the conductor is moved through the field'
		choice_d = 'both a and b*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""For a conductor being moved through a magnetic field, the amount of induced voltage is determined by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_11:
	def __init__(self, *args, **kwargs):
		choice_a = 'strong permanent magnets'
		choice_b = 'alternating current*'
		choice_c = 'static electricity'
		choice_d = 'direct current'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Degaussing is done with"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_12:
	def __init__(self, *args, **kwargs):
		choice_a = 'increase with higher frequencies*'
		choice_b = 'decrease with higher frequencies'
		choice_c = 'are greater with direct current'
		choice_d = 'increase with lower frequencies'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""Hysteresis losses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_13:
	def __init__(self, *args, **kwargs):
		choice_a = 'all of the molecular dipoles and magnetic domains are aligned by the magnetizing force'
		choice_b = 'the coil is way too long'
		choice_c = 'the flux density cannot be increased in the core when the field intensity is increased'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""The saturation of an iron core occurs when"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_14:
	def __init__(self, *args, **kwargs):
		choice_a = 'oersted'
		choice_b = 'gilbert'
		choice_c = 'At/m'
		choice_d = 'both a and c*'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)

		self.question = f"""The unit of field intensity is the"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_15:
	def __init__(self, *args, **kwargs):
		choice_a = 'only on the top side'
		choice_b = 'parallel to the direction of current'
		choice_c = 'at right angles to the direction of current*'
		choice_d = 'only on the bottom side'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""For a single conductor carrying an alternating current, the associated magnetic field"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_16:
	def __init__(self, *args, **kwargs):
		choice_a = '4000 turns'
		choice_b = '400 turns*'
		choice_c = '40 turns'
		choice_d = '16 turns'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A coil with 200mA of current has an mmf of 80At. How many turns does the coil have?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_17:
	def __init__(self, *args, **kwargs):
		choice_a = 'like that of a permanent magnet*'
		choice_b = 'unable to develop north and south poles'
		choice_c = 'one without magnetic flux lines'
		choice_d = 'unlike that of a permanent magnet'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""The magnetic field surrounding a solenoid is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_18:
	def __init__(self, *args, **kwargs):
		choice_a = 'the maximum current the relay contacts can handle '
		choice_b = 'the minimum amount of relay coil currrent required to keep a relay energized*'
		choice_c = 'the minimum amount of relay coil current required to energize a relay'
		choice_d = 'the maximum current required to operate a relay'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""For a relay, the holding current is defined as"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_19:
	def __init__(self, *args, **kwargs):
		choice_a = 'clockwise'
		choice_b = 'counterclockwise*'
		choice_c = 'parallel to the wire'
		choice_d = 'none of the choices'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""A vertical wire with electron flow into this page has an associated magnetic field"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_14_20:
	def __init__(self, *args, **kwargs):
		choice_a = '7.5 kV'
		choice_b = '75 V'
		choice_c = '750 V*'
		choice_d = '750 mV'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)

		self.question = f"""How much is the induced voltage when a magnetic flux cuts across 150 turns at the rate of 5 Wb/s?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""



class grobs_15_1:
	def __init__(self):
		choice_a = 'varies continuously in magnitude'
		choice_b = 'reverses periodically in polarity.'
		choice_c = 'never varies in amplitude'
		choice_d = 'both a and b'

		choices = [choice_a, choice_b, choice_c, choice_d]
		#random.shuffle(choices)
		self.questions = f"""An alternating voltage is one that"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_15_2:
	def __init__(self):
		choice_a = 'octave'
		choice_b = 'decade'
		choice_c = 'cycle'
		choice_d = 'alternation'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		self.question = f"""One complete revolution of a conductor loop through a magnetic fi eld is called a(n)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class grobs_15_3:
	def __init__(self):
		choice_a = 'alternation'
		choice_b = 'harmonic'
		choice_c = 'octave'
		choice_d = 'period'

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		self.question = f"""For a sine wave, one-half cycle is
often called a(n)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class name_15_4:
	def __init__(self):
		choice_a = 
		choice_b = 
		choice_c = 
		choice_d = 

		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		self.question = f"""One cycle includes"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""






