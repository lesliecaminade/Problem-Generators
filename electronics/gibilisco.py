import random_handler as ran
import math
import random
import constants_conversions as c
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

class gibilisco_1_1:
    def __init__(self, *args, **kwargs):
        
        choice_a = 'The number of neutrons'
        choice_b = 'The number of protons*'
        choice_c = 'The number of neutrons plus the number of protons'
        choice_d = 'The number of electrons'
        
        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)
        
        
        self.question = f"""The atomic number of an element is determined by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_2:
    def __init__(self, *args, **kwargs):
        
        choice_a = 'The number of neutrons'
        choice_b = 'The number of protons'
        choice_c = 'The number of neutrons plus the number of protons*'
        choice_d = 'The number of electrons'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The atomic weight of an element is approximately determined by"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_3:
    def __init__(self, *args, **kwargs):
        choice_a = '8'
        choice_b = '10'
        choice_c = '16'
        choice_d = '18*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose there is an atom of oxygen, containing eight protons and eight neutrons in the nucleus, and two neutrons are added to the nucleus. The resulting atomic weight is about:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is electrical neutral'
        choice_b = 'Has positive electric charge'
        choice_c = 'Has negative electric charge'
        choice_d = 'Might have either a positive or negative charge*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An ion: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is electrical neutral'
        choice_b = 'Has positive electric charge'
        choice_c = 'Has negative electric charge'
        choice_d = 'Might have either a positive or negative charge*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An isotope: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Might consist of just a single atom of an element*'
        choice_b = 'Must always contain two or more elements'
        choice_c = 'Always has two or more atoms'
        choice_d = 'Is always electrically charged'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A molecule: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'There can be just a single atom of an element'
        choice_b = 'There must always be two or more elements*'
        choice_c = 'The atoms are mixed in with each other but not joined'
        choice_d = 'There is always a shortage of electrons'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a compound: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'By heating.'
        choice_b = 'By cooling.'
        choice_c = 'By ionizing.*'
        choice_d = 'By oxidizing.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An electrical insulator can be made a conductor: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Air*'
        choice_b = 'Copper'
        choice_c = 'Iron'
        choice_d = 'Salt water'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Of the following substances, the worst conductor is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Air'
        choice_b = 'Copper*'
        choice_c = 'Iron'
        choice_d = 'Salt water'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""OF the following substances, the best conductor is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is like a flow of electrons in the same direction.'
        choice_b = 'Is possible only if the current is high enough.'
        choice_c = 'Results in a certain amount of electric current.*'
        choice_d = 'Causes the material to stop conducting.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Movement of holes in a semiconductor: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is a good conductor.*'
        choice_b = 'It is a poor conductor.'
        choice_c = 'The current flows mainly in the form of holes.'
        choice_d = 'Current can flow only in one direction.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a material has low resistance: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Represents a current of one ampere.'
        choice_b = 'Flows through a 100-watt light bulb.'
        choice_c = 'Is one ampere per second.'
        choice_d = 'Is an extremely large number number of charge carriers.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coulomb: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is caused by a movement of holes in an insulator.'
        choice_b = 'Has a very low current.'
        choice_c = 'Is a discharge of static electricity.*'
        choice_d = 'Builds up between clouds.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A stroke of lightning: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current'
        choice_b = 'Charge'
        choice_c = 'Electromotive Force*'
        choice_d = 'Resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The volt is the standard unit of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_1_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'Half an ampere*'
        choice_b = 'One ampere'
        choice_c = 'Two ampere'
        choice_d = 'One ohm'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an EMF of one volt is placed across a resistance of two ohms, then the current is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'An inefficient, energy-wasting device.'
        choice_b = 'A motor with the voltage connected the wrong way.'
        choice_c = 'An electric generator.*'
        choice_d = 'A magnetic-field generator.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A backwards-working electric motor is best described as: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Connecting it to a light bulb'
        choice_b = 'Charging it*'
        choice_c = 'Discharging it'
        choice_d = 'No means known; when a battery is dead, you have to throw it away'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In some batteries, chemical energy can be replenished by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_1_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Produces an electric current in an insulator'
        choice_b = 'Magnetizing the earth'
        choice_c = 'Produces a fluctuating electric field*'
        choice_d = 'Results from a steady electric current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A changing magnetic field: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_1_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'In a dry cell'
        choice_b = 'In a wet cell'
        choice_c = 'In an incandescent bulb'
        choice_d = 'In a photovoltaic cell*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Light is converted into electricity: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has a deficiency of electrons'
        choice_b = 'Has fewer electrons than the negative pole*'
        choice_c = 'Has an excess of electrons'
        choice_d = 'Has more electrons that the negative pole'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A positive electric pole: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Cannot drive much current through a circuit.'
        choice_b = 'Represents a low resistance.'
        choice_c = 'Can sometimes produce a large current.*'
        choice_d = 'Drops to zero in a short time.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An EMF of one volt: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_3:
    def __init__(self, *args, **kwargs):
        choice_a = '0.01 mA'
        choice_b = '0.1 mA'
        choice_c = '1 mA'
        choice_d = '0.1 A*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A potentially lethal electric current is on the order of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'A flashlight bulb'
        choice_b = 'A typical household*'
        choice_c = 'A power plant'
        choice_d = 'A clock radio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A current of 25 A is most likely drawn by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_5:
    def __init__(self, *args, **kwargs):
        choice_a = '20 ohms'
        choice_b = '0.5 ohms'
        choice_c = '0.05 ohms*'
        choice_d = '0.02 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A piece of wire has a conductance of 20 siemens. Its resistance is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_6:
    def __init__(self, *args, **kwargs):
        choice_a = '3.33 mS*'
        choice_b = '33.3 mS'
        choice_c = '333 uS'
        choice_d = '0.333 S'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor has a value of 300 ohms. Its conductance is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_7:
    def __init__(self, *args, **kwargs):
        choice_a = '1.8 siemens'
        choice_b = '1.8 ohms'
        choice_c = '0.2 siemens*'
        choice_d = 'Not enough information has been given to answer this'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A mile of wire has a conductance of 0.6 siemens. Then three miles of the same wire has a conductance of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_8:
    def __init__(self, *args, **kwargs):
        choice_a = '17 mA'
        choice_b = '234 mA'
        choice_c = '17 A*'
        choice_d = '234 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A 2-kW generator will deliver approximately how much current, reliably, at 117 V?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_9:
    def __init__(self, *args, **kwargs):
        choice_a = '1.76*'
        choice_b = '1760'
        choice_c = '7.8'
        choice_d = '0.0078'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A circuit breaker is rated for 15 A at 117 V. This represents approximately how many kilowatts?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_10:
    def __init__(self, *args, **kwargs):
        choice_a = '147'
        choice_b = '14.7'
        choice_c = '1.47'
        choice_d = '0.147*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You are told that a certain air conditioner is rated at 500 BTU. What is this in kWh?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'The BTU'
        choice_b = 'The erg'
        choice_c = 'The foot pound'
        choice_d = 'The kilowatt hour*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Of the following energy units, the one most used to define electrical energy is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_12:
    def __init__(self, *args, **kwargs):
        choice_a = '60 Hz*'
        choice_b = '120 Hz'
        choice_c = '50 Hz'
        choice_d = '100 Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The frequency of common household ac in the US is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Half of the ac wave is inverted'
        choice_b = 'Half of the ac wace is chopped off*'
        choice_c = 'The whole wave is inverted'
        choice_d = 'The effective value is half the peak value'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Half-wave rectification means that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Half of the wave is inverted'
        choice_b = 'The effective value is less than that of the original wave*'
        choice_c = 'The effective value is the same as thjat of the original ac wave'
        choice_d = 'The effective value is more than that of the original wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the output of a half-wave rectifier: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'The whole wave is inverted'
        choice_b = 'The effective value is less than that of the original wave'
        choice_c = 'The effective value is the same as thjat of the original ac wave*'
        choice_d = 'The effective value is more than that of the original wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the output of a full-wave rectifier: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is never dangerous'
        choice_b = 'Is always dangerous'
        choice_c = 'Is dangerous if it is ac, but not if it is dc'
        choice_d = 'Can be dangerous under certain conditions*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A low voltage, such as 12 V: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'The volt-turn'
        choice_b = 'The ampere-turn*'
        choice_c = 'The gauss'
        choice_d = 'The gauss-turn'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these can represent a magnetomotive force?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'The volt-turn'
        choice_b = 'The ampere-turn'
        choice_c = 'The gauss*'
        choice_d = 'The gauss-turn'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following units can represent magnetic flux density?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Concentrates magnetic flux lines within itself*'
        choice_b = 'Increases the total magnetomotive force around a current-carrying wire'
        choice_c = 'Causes an increase in the current in a wire'
        choice_d = 'Increases the number of ampere-turns in a wire'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ferromagnetic material"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_2_20:
    def __init__(self, *args, **kwargs):
        choice_a = '37500 At'
        choice_b = '375 At'
        choice_c = '37.5 At*'
        choice_d = '3.75 At'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil has 500 turns and carries 75 mA of current. The magnetomotive force will be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Electromagnetic deflection'
        choice_b = 'Electrostatic force*'
        choice_c = 'Magnetic force'
        choice_d = 'Electroscopic force'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The force between two electrically charged objects is called: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Electromagnetic deflection*'
        choice_b = 'Electrostatic force'
        choice_c = 'Magnetic force'
        choice_d = 'Electroscopic force'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The change in the direction of a compass needle, when a current-carrying wire is brought near, is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Will decrease'
        choice_b = 'Will stay the same'
        choice_c = 'Will increase*'
        choice_d = 'Will reverse direction'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose a certain current in a galvanometer causes the needle to deflect 20 degrees, and then this current is doubled. The needle deflection:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'It measures very small currents'
        choice_b = 'It will handle large currents'
        choice_c = 'It can detect ac voltages*'
        choice_d = 'It draws a large current from the source'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One important advantage of an electrostatic meter is that:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'Gets warm when current flows through it*'
        choice_b = 'Is a thin, straight, special wire'
        choice_c = 'Generates dc when exposed to light'
        choice_d = 'Generates ac when heated'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A thermocouple: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'The electromagnet meter costs much less'
        choice_b = 'The electromagnet meter need not be aligned with the earth\'s magnetic field'
        choice_c = 'The permanent-magnet meter has a more sluggish coil.'
        choice_d = 'The electromagnet meter is more rugged*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One advantage of an electromagnet meter over a permanent-magnet meter is that:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'It increases meter sensitivity'
        choice_b = 'It makes a meter more physically rugged'
        choice_c = 'It allows for measurement of a wide range of currents*'
        choice_d = 'It prevents overheating of the meter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An ammeter shunt is useful because: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'Large internal resistance*'
        choice_b = 'Low internal resistance'
        choice_c = 'Maximum possible sensitivity'
        choice_d = 'Ability to withstand large currents'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Voltmeters should generally have: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is placed in series with circuit that works from the supply'
        choice_b = 'Is placed between the negative pole of the supply and the circuit working from the supply'
        choice_c = 'Is placed between the positive pole of the supply and the circuit working from the supply'
        choice_d = 'Is placed in parallel with the circuit that works from the supply*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To measure power-supply voltage being used by a circuit, a voltmeter"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'A small voltage between points under test'
        choice_b = 'A slight change in switchable internal resistance'
        choice_c = 'A small change in the resistance to be measured*'
        choice_d = 'A slight error in range switch selection'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following will NOT cause a major error in ohmmeter reading?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_11:
    def __init__(self, *args, **kwargs):
        choice_a = '33,000 ohms*'
        choice_b = '3.3 kohms'
        choice_c = '330 ohms'
        choice_d = '33 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The ohmmeter in the figure shows a reading of about
https://lesliecaminadecom.files.wordpress.com/2019/08/ei3okm9558koh1lrvcg7.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Can measure lower voltages'
        choice_b = 'Draws less current from the circuit under test*'
        choice_c = 'Can withstand higher voltages safely'
        choice_d = 'Is sensitive to ac as well as to dc'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The main advantage of a FETVM over a conventional voltmeter is the fact that the FETVM"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'To be sure there is enough current available for an appliance to work right.*'
        choice_b = 'To make it impossible to use appliances that are too large for a given circuit'
        choice_c = 'To limit the amount of power that a circuit can deliver.'
        choice_d = 'To make sure the current is within safe limits.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not a function of a fuse: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'The number of ampere hours being used at the time.'
        choice_b = 'The number of watt hours being used at the time.'
        choice_c = 'The number of watts being used at the time.*'
        choice_d = 'The number of kilowatt hours being used at the time.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A utility meter’s motor speed works directly from: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Voltage'
        choice_b = 'Power'
        choice_c = 'Current'
        choice_d = 'Energy*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A utility meter’s readout indicates: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has an analog readout.'
        choice_b = 'Is usually accurate to six digits or more.*'
        choice_c = 'Works by indirectly measuring current.'
        choice_d = 'Works by indirectly measuring voltage.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A typical frequency counter: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Sound'
        choice_b = 'Decibels'
        choice_c = 'Power'
        choice_d = 'Energy*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A VU meter is NEVER used for measurement of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current*'
        choice_b = 'Voltage'
        choice_c = 'Power'
        choice_d = 'Energy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The meter movement in an illumination meter measures: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequency'
        choice_b = 'Wave shape'
        choice_c = 'Energy*'
        choice_d = 'Peak signal voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An oscilloscope cannot be used to indicate: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_3_20:
    def __init__(self, *args, **kwargs):
        choice_a = '6 V'
        choice_b = '6.6 V*'
        choice_c = '7.0 V'
        choice_d = 'No way to tell; the meter is malfunctioning.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The display shown in the figure could be caused by a voltage of: 
https://lesliecaminadecom.files.wordpress.com/2019/08/xz33637jrxwlugo34z30.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Four times as great*'
        choice_b = 'Twice as great'
        choice_c = 'The same as it was before'
        choice_d = 'Half as great'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose you double the voltage in a simple circuit, and cut the resistance in half. The current will become"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'An engineer\'s general circuit idea notebook'
        choice_b = 'An advertisement for an electrical device'
        choice_c = 'The service/repair manual for a radio receiver*'
        choice_d = 'A procedural flowchart'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_4_3:
    def __init__(self, *args, **kwargs):
        choice_a = '0.73 A'
        choice_b = '138 A'
        choice_c = '138 mA'
        choice_d = '7.3 mA*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Given a dc voltage source delivering 24 V and a circuit resistance of 3.3 kohms, what is the current?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_4:
    def __init__(self, *args, **kwargs):
        choice_a = '413 V*'
        choice_b = '0.539 V'
        choice_c = '1.85 V'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose that a circuit has 472 ohms of resistance and the current is 875 mA. Then the source voltage is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_5:
    def __init__(self, *args, **kwargs):
        choice_a = '0.76 ohms'
        choice_b = '76 ohms*'
        choice_c = '0.0040 ohms'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The dc voltage in a circuit is 550 mV and the current is 7.2 mA. Then the resistance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_6:
    def __init__(self, *args, **kwargs):
        choice_a = '16 mA'
        choice_b = '6.3 mA'
        choice_c = '6.3 A'
        choice_d = 'None of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Given a dc voltage source of 3.5 kV and a circuit resistance of 220 ohms, what is
the current?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_7:
    def __init__(self, *args, **kwargs):
        choice_a = '2082 V'
        choice_b = '110 kV'
        choice_c = '2.1 kV*'
        choice_d = '2.08266 kV'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A circuit has a total resistance of 473,332  and draws 4.4 mA. The best expression for the voltage of the source is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_8:
    def __init__(self, *args, **kwargs):
        choice_a = '15 ohms*'
        choice_b = '15.4 ohms'
        choice_c = '9.3 ohms'
        choice_d = '9.32 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A source delivers 12 V and the current is 777 mA. Then the best expression for the resistance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_9:
    def __init__(self, *args, **kwargs):
        choice_a = '31 mW'
        choice_b = '31 W'
        choice_c = '2.0 W*'
        choice_d = '2.0 mW'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The voltage is 250 V and the current is 8.0 mA. The power dissipated by the potentiometer is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_10:
    def __init__(self, *args, **kwargs):
        choice_a = '310 mW*'
        choice_b = '25.5 mW'
        choice_c = '39.2 W'
        choice_d = '3.26 W'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The voltage from the source is 12 V and the potentiometer is set for 470 ohms. The power is about:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_11:
    def __init__(self, *args, **kwargs):
        choice_a = '0.24 uW'
        choice_b = '20.7 W'
        choice_c = '20.7 mW'
        choice_d = '350 mW*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The current through the potentiometer is 17 mA and its value is 1.22 kohms. The power is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_12:
    def __init__(self, *args, **kwargs):
        choice_a = '90 ohms'
        choice_b = '3.24 kohms*'
        choice_c = '540 ohms'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose six resistors are hooked up in series, and each of them has a value of 540 ohms. Then the total resistance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_13:
    def __init__(self, *args, **kwargs):
        choice_a = '1 kohms'
        choice_b = '4 kohms'
        choice_c = '8 kohms'
        choice_d = '16 kohms*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Four resistors are connected in series, each with a value of 4.0 kohms. The total resistance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_14:
    def __init__(self, *args, **kwargs):
        choice_a = '23 ohms'
        choice_b = '23 kohms*'
        choice_c = '204 kohms'
        choice_d = '0.2 Mohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose you have three resistors in parallel, each with a value of 68,000 ohms. Then the total resistance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_15:
    def __init__(self, *args, **kwargs):
        choice_a = '1.3 A*'
        choice_b = '15 mA'
        choice_c = '150 mA'
        choice_d = '1.5 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""There are three resistors in parallel, with values of 22 ohms, 27 ohms, and 33 ohms. A 12-V battery is connected across this combination. What is the current drawn from the battery by this resistance combination?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_16:
    def __init__(self, *args, **kwargs):
        choice_a = '250 mW'
        choice_b = '13 mW'
        choice_c = '13 W*'
        choice_d = 'Not determinable from the data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors, with values of 47 ohms, 68 ohms, and 82 ohms, are connected in series with a 50-V dc generator. The total power consumed by this network of resistors is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""
        
class gibilisco_4_17:
    def __init__(self, *args, **kwargs):
        choice_a = '3 x 3 resistors'
        choice_b = '4 x 3 resistors'
        choice_c = '4 x 4 resistors*'
        choice_d = '2 x 5 resistors'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You have an unlimited supply of 1-W, 100-ohm resistors. You need to get a 100-Ω, 10-W resistor. This can be done most cheaply by means of a series-parallel matrix of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Four sets of two 1000-ohm resistors in series, and connecting these four sets in parallel.*'
        choice_b = 'Four sets of two 1000-ohm resistors in parallel, and connecting these four sets in series.'
        choice_c = 'A 3 x 3 series-parallel matrix of 1000-ohm resistors.'
        choice_d = 'Something other than any of the above.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You have an unlimited supply of 1-W, 1000-ohm resistors, and you need a 500-ohm resistance rated at 7 W or more. This can be done by assembling:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Make a 2 x 2 series-parallel matrix.'
        choice_b = 'Connect three of the resistors in parallel.'
        choice_c = 'Make a 3 x 3 series-parallel matrix.'
        choice_d = 'Do something other than any of the above.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You have an unlimited supply of 1-W, 1000-ohm resistors, and you need to get a 3000-Ω, 5-W resistance. The best way is to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_4_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'From resistors that are all very rugged.'
        choice_b = 'From resistors that are all the same.*'
        choice_c = 'From a series combination of resistors in parallel.'
        choice_d = 'From a parallel combination of resistors in series.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Good engineering practice usually requires that a series-parallel resistive network be made: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'All the other bulbs will go out.'
        choice_b = 'The current in the string will go up.*'
        choice_c = 'The current in the string will go down.'
        choice_d = 'The current in the string will stay the same.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a series-connected string of holiday ornament bulbs, if one bulb gets shorted out, which of these is most likely?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_2:
    def __init__(self, *args, **kwargs):
        choice_a = '0.18 V'
        choice_b = '33 mV'
        choice_c = '5.6 mV'
        choice_d = '670 mV*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Four resistors are connected in series across a 6.0-V battery. The values are R1 = 10 Ω, R2 = 20 Ω, R3 = 50 Ω, and R4 = 100 Ω. The voltage across R2 is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_3:
    def __init__(self, *args, **kwargs):
        choice_a = '0.22 V'
        choice_b = '0.22 mV'
        choice_c = '5.0 V*'
        choice_d = '3.3 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Four resistors are connected in series across a 6.0-V battery. The values are R1 = 10 Ω, R2 = 20 Ω, R3 = 50 Ω, and R4 = 100 Ω. the voltage across the combination of R3 and R4 is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_5_4:
    def __init__(self, *args, **kwargs):
        choice_a = '4.4 V'
        choice_b = '5.0 V'
        choice_c = '15 V*'
        choice_d = 'Not determinable from the data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors are connected in parallel across a battery that delivers 15 V. The values are R1 = 470 Ω, R2 = 2.2 KΩ, R3 = 3.3 KΩ. The voltage across R2 is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_5:
    def __init__(self, *args, **kwargs):
        choice_a = '6.8 mA*'
        choice_b = '43 mA'
        choice_c = '150 mA'
        choice_d = '6.8 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors are connected in parallel across a battery that delivers 15 V. The values are R1 = 470 Ω, R2 = 2.2 KΩ, R3 = 3.3 KΩ. what is the current through R2:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_6:
    def __init__(self, *args, **kwargs):
        choice_a = '6.8 mA'
        choice_b = '43 mA*'
        choice_c = '150 mA'
        choice_d = '6.8 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors are connected in parallel across a battery that delivers 15 V. The values are R1 = 470 Ω, R2 = 2.2 KΩ, R3 = 3.3 KΩ. what is the total current drawn from the source?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_5_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increase'
        choice_b = 'Decrease'
        choice_c = 'Drop to zero'
        choice_d = 'No change*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors are connected in parallel across a battery that delivers 15 V. The values are R1 = 470 Ω, R2 = 2.2 KΩ, R3 = 3.3 KΩ. Suppose that resistor R2 opens up. The current through the other two resistors will?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_8:
    def __init__(self, *args, **kwargs):
        choice_a = '200 mW*'
        choice_b = '6.5 mW'
        choice_c = '200 W'
        choice_d = '6.5 W'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Four resistors are connected in series across a 6.0-V battery. The values are R1 = 10 Ω, R2 = 20 Ω, R3 = 50 Ω, and R4 = 100 Ω. What is the power dissipated by the whole combination:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_9:
    def __init__(self, *args, **kwargs):
        choice_a = '11 mW'
        choice_b = '0.11 W*'
        choice_c = '0.2 W'
        choice_d = '6.5 mW'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Four resistors are connected in series across a 6.0-V battery. The values are R1 = 10 Ω, R2 = 20 Ω, R3 = 50 Ω, and R4 = 100 Ω. What is the power dissipated by R4?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_10:
    def __init__(self, *args, **kwargs):
        choice_a = '5.4 W'
        choice_b = '5.4 uW'
        choice_c = '650 W'
        choice_d = '650 mW*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors are connected in parallel across a battery that delivers 15 V. The values are R1 = 470 Ω, R2 = 2.2 KΩ, R3 = 3.3 KΩ. What is the power dissipated by the whole set?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_11:
    def __init__(self, *args, **kwargs):
        choice_a = '32 mW'
        choice_b = '480 mW*'
        choice_c = '2.1 W'
        choice_d = '31 W'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three resistors are connected in parallel across a battery that delivers 15 V. The values are R1 = 470 Ω, R2 = 2.2 KΩ, R3 = 3.3 KΩ. The power dissipated by R1 is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current'
        choice_b = 'Voltage'
        choice_c = 'Wattage*'
        choice_d = 'Resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Fill in the blank in the following sentence. In either series or a parallel circuit,the sum of the ________s in each component is equal to the total provided by the supply."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_5_13:
    def __init__(self, *args, **kwargs):
        choice_a = '1.1 A'
        choice_b = '730 mA*'
        choice_c = '360 mA'
        choice_d = 'Not determinable from the information given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Refer to Fig. 5-5A. Suppose the resistors each have values of 33 Ω. The battery provides 24 V. The current I1 is:
https://lesliecaminadecom.files.wordpress.com/2019/08/wxx9788ytr127c794o6v.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_14:
    def __init__(self, *args, **kwargs):
        choice_a = '33 W'
        choice_b = '40 mW'
        choice_c = '1.3 W*'
        choice_d = 'It can\'t be found using the information given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Let each resistor have a value of 820 Ω. Suppose the top three resistors all lead to light bulbs of the exact same wattage. If I1 = 50 mA and I2 = 70 mA, what is the power dissipated in the resistor carrying current I4? 
https://lesliecaminadecom.files.wordpress.com/2019/08/1g2dogiqt65jxm07jnxj.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_5_15:
    def __init__(self, *args, **kwargs):
        choice_a = '4 V*'
        choice_b = '8 V'
        choice_c = '16 V'
        choice_d = 'Not determinable from the data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose the resistances R1, R2, R3, and R4 are in the ratio 1:2:4:8 from left to right, and the battery supplies 30 V. Then the voltage E2 is:
https://lesliecaminadecom.files.wordpress.com/2019/08/i3v4w2d9uugs2nu1p8c8.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_16:
    def __init__(self, *args, **kwargs):
        choice_a = '0 V'
        choice_b = '3 V'
        choice_c = '6 V*'
        choice_d = '12 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Let the resistances each be 3.3 KΩ and the battery 12 V. If the plus terminal of a dc voltmeter is placed between R1 and R2 (with voltages E1 and E2), and the minus terminal of the voltmeter is placed between R3 and R4 (with voltages E3 and E4), what will the meter register?
https://lesliecaminadecom.files.wordpress.com/2019/08/i3v4w2d9uugs2nu1p8c8.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Should be large to minimize current drain.'
        choice_b = 'Should be as small as the power supply will allow.*'
        choice_c = 'Is not important.'
        choice_d = 'Should be such that the current is kept to 100 mA.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a voltage divider network, the total resistance:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is a fraction of the power supply voltage.'
        choice_b = 'Depends on the total resistance.'
        choice_c = 'Is equal to the supply voltage.*'
        choice_d = 'Depends on the ratio of resistances.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The maximum voltage output from a voltage divider: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_19:
    def __init__(self, *args, **kwargs):
        choice_a = '4.19 V'
        choice_b = '13.8 V*'
        choice_c = '1.61 V'
        choice_d = '2.94 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The battery E is 18.0 V. Suppose there are four resistors in the network: R1 = 100 Ω, R2 = 22.0 Ω, R3 = 33.0 Ω, R4 = 47.0 Ω. The voltage E3 at P3 is:
https://lesliecaminadecom.files.wordpress.com/2019/08/wk7k972rfb0qm4anleb0.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_5_20:
    def __init__(self, *args, **kwargs):
        choice_a = '15 ohms, 30 ohms, 45 ohms, 60 ohms'
        choice_b = '60 ohms, 45 ohms, 30 ohms, 15 ohms'
        choice_c = '15 ohms, 15 ohms, 15 ohms, 15 ohms*'
        choice_d = 'There isn\'t enough information to design the circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The battery is 12 V; you want intermediate voltages of 3.0,6.0 and 9.0 V. Suppose that a maximum of 200 mA is allowed through the network. What values should the resistors, R1, R2, R3, and R4 have, respectively?
https://lesliecaminadecom.files.wordpress.com/2019/08/wk7k972rfb0qm4anleb0.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Keeps it from oscillating.'
        choice_b = 'Matches it to other amplifier stages in a chain.'
        choice_c = 'Can be done using voltage dividers.*'
        choice_d = 'Maximizes current flow.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Biasing in an amplifier circuit: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current-limiting resistors.*'
        choice_b = 'Bleeder resistors.'
        choice_c = 'Maximizing the driving power.'
        choice_d = 'Shorting out the power supply when the circuit is off.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transistor can be protected from needless overheating by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Are connected across the capacitor in a power supply.*'
        choice_b = 'Keep a transistor from drawing too much current.'
        choice_c = 'Prevent an amplifier from being overdriven.'
        choice_d = 'Optimize the efficiency of an amplifier.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Bleeder resistors: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Can handle lots of power.'
        choice_b = 'Have capacitance or inductance along with resistance.'
        choice_c = 'Are comparatively nonreactive.*'
        choice_d = 'Work better for ac than for dc.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Carbon-composition resistors: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""
        
class gibilisco_6_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'In a radio-frequency amplifier.'
        choice_b = 'When the resistor doesn’t dissipate much power.'
        choice_c = 'In a high-power, radio-frequency circuit.'
        choice_d = 'In a high-power, direct-current circuit.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The best place to use a wirewound resistor is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is made using solid carbon/phenolic paste.'
        choice_b = 'Has less reactance than a wirewound type.*'
        choice_c = 'Can dissipate large amounts of power.'
        choice_d = 'Has considerable inductance.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A metal-film resistor: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'A set of switchable, fixed resistors.'
        choice_b = 'A linear-taper potentiometer.*'
        choice_c = 'A logarithmic-taper potentiometer.'
        choice_d = 'A wirewound resistor.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A meter-sensitivity control in a test instrument would probably be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'A set of switchable, fixed resistors.'
        choice_b = 'A linear-taper potentiometer.'
        choice_c = 'A logarithmic-taper potentiometer.*'
        choice_d = 'A wirewound resistor.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A volume control in a stereo compact-disc player would probably be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_9:
    def __init__(self, *args, **kwargs):
        choice_a = '3 dB'
        choice_b = '5 dB*'
        choice_c = '6 dB'
        choice_d = '9 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a sound triples in actual power level, approximately what is the decibel increase? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_10:
    def __init__(self, *args, **kwargs):
        choice_a = '13 W'
        choice_b = '77 mW'
        choice_c = '50 mW*'
        choice_d = 'There is not enough information to tell.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose a sound changes in volume by 13 dB. If the original sound power is 1 W, what is the final sound power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_11:
    def __init__(self, *args, **kwargs):
        choice_a = '50'
        choice_b = '169'
        choice_c = '5,000'
        choice_d = '100,000*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The sound from a transistor radio is at a level of 50 dB. How many times the threshold of hearing is this, in terms of actual sound power? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'A rheostat can handle higher frequencies.'
        choice_b = 'A rheostat is more precise.'
        choice_c = 'A rheostat can handle more current.*'
        choice_d = 'A rheostat works better with dc.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of a rheostat over a potentiometer is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_13:
    def __init__(self, *args, **kwargs):
        choice_a = '7.4 percent*'
        choice_b = '7.9 percent'
        choice_c = '5 percent'
        choice_d = '10 percent'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor is specified as having a value of 68 Ω, but is measured with an ohmmeter as 63 Ω. The value is off by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_14:
    def __init__(self, *args, **kwargs):
        choice_a = '2,970 and 3,630 Ω.'
        choice_b = '3,295 and 3,305 Ω.'
        choice_c = '3,135 and 3,465 Ω.*'
        choice_d = '2.8 KΩ and 3.8 KΩ.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose a resistor is rated at 3.3 KΩ, plus or minus 5 percent. This means it can be expected to have a value between: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_15:
    def __init__(self, *args, **kwargs):
        choice_a = '50.0 ohms*'
        choice_b = '53.0 ohms'
        choice_c = '59.7 ohms'
        choice_d = '61.1 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A package of resistors is rated at 56 Ω, plus or minus 10 percent. You test them with an ohmmeter. Which of the following values indicates a reject?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_16:
    def __init__(self, *args, **kwargs):
        choice_a = '1/4 W*'
        choice_b = '1/2 W'
        choice_c = '1 W'
        choice_d = '2 W'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor has a value of 680 Ω, and you expect it will have to draw 1 mA maximum continuous current. What power rating is best for this application?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Four 1 KΩ, 1-W resistors in series-parallel.'
        choice_b = 'Two 2.2 KΩ, 1-W resistors in parallel.*'
        choice_c = 'Three 3.3 KΩ, 1-W resistors in parallel.'
        choice_d = 'One 1 KΩ, 1-W resistor, since manufacturers allow for a 10-percent margin of safety.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose a 1-KΩ resistor will dissipate 1.05 W, and you have many 1-W resistors of all common values. If there’s room for 20-percent resistance error, the cheapest solution is to use: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_18:
    def __init__(self, *args, **kwargs):
        choice_a = '22 ohms'
        choice_b = '220 ohms'
        choice_c = '2.2 kohms*'
        choice_d = '22 kohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Red, red, red, gold indicates a resistance of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_19:
    def __init__(self, *args, **kwargs):
        choice_a = '11 ohms'
        choice_b = '110 ohms*'
        choice_c = '22 ohms'
        choice_d = '220 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The actual resistance of the above unit can be expected to vary by how much above or below the specified value?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_6_20:
    def __init__(self, *args, **kwargs):
        choice_a = '660 KΩ to 980 KΩ.*'
        choice_b = '740 KΩ to 900 KΩ.'
        choice_c = '7.4 KΩ to 9.0 KΩ.'
        choice_d = 'The manufacturer does not make any claim.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor has three bands: gray, red, yellow. This unit can be expected to have a value within approximately what range?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is a form of kinetic energy.'
        choice_b = 'Cannot be replenished once it is gone.'
        choice_c = 'Changes to kinetic energy when the cell is used.*'
        choice_d = 'Is caused by electric current.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The chemical energy in a battery or cell: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'A dry cell'
        choice_b = 'A wet cell'
        choice_c = 'A primary cell*'
        choice_d = 'A secondary cell'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A cell that cannot be recharged is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'As a current reference source.'
        choice_b = 'As a voltage reference source.*'
        choice_c = 'As a power reference source.'
        choice_d = 'As an energy source.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Weston cell is generally used: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Less than the voltage in a cell of the same kind.'
        choice_b = 'The same as the voltage in a cell of the same kind.'
        choice_c = 'More than the voltage in a cell of the same kind.*'
        choice_d = 'Always a multiple of 1.018 V.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The voltage in a battery is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'An increase in its voltage.'
        choice_b = 'No harm other than a rapid discharge of its energy.'
        choice_c = 'The current to drop to zero.'
        choice_d = 'An explosion.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A direct short-circuit of a battery can cause: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_6:
    def __init__(self, *args, **kwargs):
        choice_a = '7.33 Ah'
        choice_b = '733 mAh*'
        choice_c = '7.33 Wh'
        choice_d = '733 mWh'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A cell of 1.5 V supplies 100 mA for seven hours and twenty minutes, and then it is replaced. It has supplied: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_7:
    def __init__(self, *args, **kwargs):
        choice_a = '4 hours and 20 minutes.*'
        choice_b = '432 hours.'
        choice_c = '3.6 hours.'
        choice_d = '21.6 minutes.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A 12-V auto battery is rated at 36 Ah. If a 100-W, 12-Vdc bulb is connected across this battery, about how long will the bulb stay lit, if the battery has been fully charged?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'Are cheaper than zinc-carbon cells.'
        choice_b = 'Are generally better in radios than zinc-carbon cells.*'
        choice_c = 'Have higher voltages than zinc-carbon cells.'
        choice_d = 'Have shorter shelf lives than zinc-carbon cells.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Alkaline cells: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_7_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Its physical size.*'
        choice_b = 'The current drawn from it.'
        choice_c = 'Its voltage.'
        choice_d = 'All of the above.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The energy in a cell or battery depends mainly on: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'A heart pacemaker.'
        choice_b = 'An electronic calculator.'
        choice_c = 'An LCD wall clock.'
        choice_d = 'A two-way portable radio.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which of the following places would a “lantern” battery most likely be found? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'A heart pacemaker.'
        choice_b = 'An electronic calculator.*'
        choice_c = 'An LCD wristwatch.'
        choice_d = 'A two-way portable radio.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which of the following places would a transistor battery be the best power-source choice?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'A microcomputer memory backup.*'
        choice_b = 'A two-way portable radio.'
        choice_c = 'A portable audio cassette player.'
        choice_d = 'A rechargeable flashlight.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which of the following places would you most likely choose a lithium battery? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'In a portable audio cassette player.'
        choice_b = 'In a portable video camera/recorder.*'
        choice_c = 'In an LCD wall clock.'
        choice_d = 'In a flashlight.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Where would you most likely find a lead-acid battery? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'A large ampere-hour rating.'
        choice_b = 'Excellent energy capacity.'
        choice_c = 'A flat discharge curve.*'
        choice_d = 'Good energy storage per unit volume.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A cell or battery that keeps up a constant current-delivering capability almost until it dies is said to have: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'In a satellite.'
        choice_b = 'In a portable cassette player.'
        choice_c = 'In a handheld radio transceiver.'
        choice_d = 'In more than one of the above.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Where might you find a NICAD battery? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'They don’t last as long as other types.'
        choice_b = 'They have a flat discharge curve.'
        choice_c = 'They pollute the environment.*'
        choice_d = 'They need to be recharged often.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A disadvantage of mercury cells and batteries is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Silver-oxide.'
        choice_b = 'Lead-acid.'
        choice_c = 'Nickel-cadmium.*'
        choice_d = 'Mercury.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which kind of battery should never be used until it “dies”? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Connecting solar cells in series.'
        choice_b = 'Using NICAD cells in series with the solar cells.'
        choice_c = 'Connecting solar cells in parallel.*'
        choice_d = 'Using lead-acid cells in series with the solar cells.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The current from a solar panel is increased by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Allows a homeowner to sell power to the utility.*'
        choice_b = 'Lets the batteries recharge at night.'
        choice_c = 'Powers lights but not electronic devices.'
        choice_d = 'Is totally independent from the utility.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An interactive solar power system: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_7_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'There’s a danger of electric shock.'
        choice_b = 'It is impossible to get more than 103.5 V with electrochemical cells.'
        choice_c = 'The battery would weigh to much.'
        choice_d = 'There isn’t any real need for such thing.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One reason why it is impractical to make an extrememly high-voltage battery of cells is that:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Makes the earth like a huge horseshoe magnet.'
        choice_b = 'Runs exactly through the geographic poles.'
        choice_c = 'Is what makes a compass work.*'
        choice_d = 'Is what makes an electromagnet work.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The geomagnetic field: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Are horizontal at the geomagnetic equator.*'
        choice_b = 'Are vertical at the geomagnetic equator.'
        choice_c = 'Are always slanted, no matter where you go.'
        choice_d = 'Are exactly symmetrical around the earth, even far out into space.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Geomagnetic lines of flux: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Magnetic.'
        choice_b = 'Electromagnetic.'
        choice_c = 'Permanently magnetic.'
        choice_d = 'Ferromagnetic.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A material that can be permanently magnetized is generally said to be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Can be either repulsive or attractive.'
        choice_b = 'Is never repulsive.*'
        choice_c = 'Gets smaller as the magnet gets closer to the metal.'
        choice_d = 'Depends on the geomagnetic field.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The force between a magnet and a piece of ferromagnetic metal that has not been magnetized: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ferromagnetic materials.'
        choice_b = 'Aligned atoms.'
        choice_c = 'Motion of charged particles.*'
        choice_d = 'The geomagnetic field.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Magnetic flux can always be attributed to: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'In atoms of ferromagnetic materials.'
        choice_b = 'At a north magnetic pole.*'
        choice_c = 'Where the lines converge to a point.'
        choice_d = 'In charge carriers.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Lines of magnetic flux are said to originate: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'Gets stronger with increasing distance from the wire.'
        choice_b = 'Is strongest near the wire.*'
        choice_c = 'Does not vary in strength with distance from the wire.'
        choice_d = 'Consists of straight lines parallel to the wire.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The magnetic flux around a straight, current-carrying wire: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'Overall magnetic field strength.'
        choice_b = 'Ampere-turns.'
        choice_c = 'Magnetic flux density.*'
        choice_d = 'Magnetic power.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The gauss is a unit of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Maxwell.*'
        choice_b = 'Gauss.'
        choice_c = 'Tesla.'
        choice_d = 'Ampere-turn.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A unit of overall magnetic field quantity is the: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_10:
    def __init__(self, *args, **kwargs):
        choice_a = '5000'
        choice_b = '50'
        choice_c = '5.0*'
        choice_d = '0.02'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a wire coil has 10 turns and carries 500 mA of current, what is the magnetomotive force in ampere-turns?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_11:
    def __init__(self, *args, **kwargs):
        choice_a = '130'
        choice_b = '76.9'
        choice_c = '164*'
        choice_d = '61.0'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a wire coil has 100 turns and carries 1.30 A of current, what is the magnetomotive force in gilberts?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Charged particles streaming out from the sun.'
        choice_b = 'Fluctuations in the earth’s magnetic field.'
        choice_c = 'Disruption of electrical power transmission.'
        choice_d = 'Disruption of microwave radio links.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not generally possible in a geomagnetic storm?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Will attract only other magnetized objects.'
        choice_b = 'Will attract pure, unmagnetized iron.*'
        choice_c = 'Will repel other magnetized objects.'
        choice_d = 'Will either attract or repel permanent magnets, depending on the polarity.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An ac electromagnet: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'An electromagnet can be switched on and off.*'
        choice_b = 'An electromagnet does not have specific polarity.'
        choice_c = 'An electromagnet requires no power source.'
        choice_d = 'Permanent magnets must always be cylindrical.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of an electromagnet over a permanent magnet is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'An ac electromagnet.'
        choice_b = 'A dc electromagnet.'
        choice_c = 'An electrostatic shield.'
        choice_d = 'A permanent magnet.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A substance with high retentivity is best suited for making: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'An ac relay.'
        choice_b = 'A dc relay.'
        choice_c = 'Normally closed.'
        choice_d = 'Normally open.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A relay is connected into a circuit so that a device gets a signal only when the relay coil carries current. The relay is probably: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'A solenoid.'
        choice_b = 'An armature coil.'
        choice_c = 'A commutator.*'
        choice_d = 'A field coil.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A device that reverses magnetic field polarity to keep a dc motor rotating is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Voices.'
        choice_b = 'Video.*'
        choice_c = 'Digital data.'
        choice_d = 'All of the above.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A high tape-recorder motor speed is generally used for: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'A disk lasts longer.'
        choice_b = 'Data can be stored and retrieved more quickly with disks than with tapes.*'
        choice_c = 'Disks look better.'
        choice_d = 'Disks are less susceptible to magnetic fields.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of a magnetic disk, as compared with magnetic tape, for data storage and retrieval is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_8_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'A large computer.*'
        choice_b = 'A home video entertainment system.'
        choice_c = 'A portable cassette player.'
        choice_d = 'A magnetic disk.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A bubble memory is best suited for: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Power'
        choice_b = 'Voltage'
        choice_c = 'Frequency*'
        choice_d = 'Magnitude'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following can vary with ac, but not with dc? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequency'
        choice_b = 'Magnitude'
        choice_c = 'Period*'
        choice_d = 'Polarity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The length of time between a point in one cycle and the same point in the next cycle of an ac wave is the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'A single pip*'
        choice_b = 'A perfect sine wave'
        choice_c = 'A square wave'
        choice_d = 'A sawtooth wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On a spectrum analyzer, a pure ac signal, having just one frequency component,would look like:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'The same as the frequency'
        choice_b = 'Not related to the frequency'
        choice_c = 'Equal to 1 divided by the frequency*'
        choice_d = 'Equal to the amplitude divided by the frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The period of an AC wave is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_5:
    def __init__(self, *args, **kwargs):
        choice_a = '0.006 Hz'
        choice_b = '167 Hz'
        choice_c = '7 kHz'
        choice_d = '6 kHz*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The sixth harmonic of an ac wave whose period is 0.001 second has a frequency of """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_6:
    def __init__(self, *args, **kwargs):
        choice_a = '6.28 cycles'
        choice_b = '57.3 cycles'
        choice_c = '1/6.28 cycles'
        choice_d = '1/360 cycles*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A degree of phase represents """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_7:
    def __init__(self, *args, **kwargs):
        choice_a = '18*'
        choice_b = '20'
        choice_c = '36'
        choice_d = '5.73'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two waves have the same frequency but differ in phase by 1/20 cycle. The phase difference in degrees is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_9_8:
    def __init__(self, *args, **kwargs):
        choice_a = '1770 radians per second'
        choice_b = '11,120 radians per second*'
        choice_c = '282 radians per second'
        choice_d = 'Impossible to determine from the data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A signal has a frequency of 1770 Hz. The angular frequency is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has a fast rise time and a slow decay time.'
        choice_b = 'Has a slow rise time and a fast decay time.'
        choice_c = 'Has equal rise and decay rates.*'
        choice_d = 'Rises and falls abruptly.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A triangular wave: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has waves that add up to three times the originals.'
        choice_b = 'Has three waves, all of the same magnitude.*'
        choice_c = 'Is what you get at a common wall outlet.'
        choice_d = 'Is of interest only to physicists.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three-phase ac: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Twice the amplitude of either wave alone.'
        choice_b = 'Half the amplitude of either wave alone.'
        choice_c = 'A complex waveform, but with the same frequency as the originals.'
        choice_d = 'Zero.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If two waves have the same frequency and the same amplitude, but opposite phase, the composite wave is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has a magnitude equal to the difference between the two originals.'
        choice_b = 'Has a magnitude equal to the sum of the two originals.*'
        choice_c = 'Is complex, with the same frequency as the originals.'
        choice_d = 'Is zero.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If two waves have the same frequency and the same phase, the composite
wave:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_13:
    def __init__(self, *args, **kwargs):
        choice_a = '82.7 V'
        choice_b = '165 V*'
        choice_c = '234 V'
        choice_d = '331 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a 117-V utility circuit, the peak voltage is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_14:
    def __init__(self, *args, **kwargs):
        choice_a = '82.7 V'
        choice_b = '165 V'
        choice_c = '234 V'
        choice_d = '331 V*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a 117-V utility circuit, the pk-pk voltage is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Half the peak value'
        choice_b = 'The same as the peak value'
        choice_c = '1.414 times the peak value'
        choice_d = 'Twice the peak value*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a perfect sine wave, the pk-pk value is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_16:
    def __init__(self, *args, **kwargs):
        choice_a = '+ 210 V and - 120 V*'
        choice_b = '+ 162 V and - 72 V'
        choice_c = '+ 396 V and - 286 V'
        choice_d = 'Both equal to 117 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a 45-Vdc battery is connected in series with the 117-V utility mains, the peak voltages will be: https://lesliecaminadecom.files.wordpress.com/2019/08/1khsf0r754v7sxg9aug6.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_17:
    def __init__(self, *args, **kwargs):
        choice_a = '117 V'
        choice_b = '210 V'
        choice_c = '331 V*'
        choice_d = '396 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a 45-Vdc battery is connected in series with the 117-V utility mains, the pk-pk voltage will be: https://lesliecaminadecom.files.wordpress.com/2019/08/1khsf0r754v7sxg9aug6.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'The strength of the magnet.'
        choice_b = 'The number of turns in the coil'
        choice_c = 'The type of natural energy source used*'
        choice_d = 'The speed of rotation of the coil or magnet'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which one of the following does NOT affect the power output available from a particular ac generator?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Smooth dc'
        choice_b = 'Smooth ac'
        choice_c = 'Ac with one peak greater than the other'
        choice_d = 'Pulsating dc*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a 175-V dc source were connected in series with the utility mains from a standard wall outlet, the result would be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_9_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ac is easier to transform from one voltage to another*'
        choice_b = 'Ac is transmitted with lower loss in wires'
        choice_c = 'Ac can be easily gotten from dc generators'
        choice_d = 'Ac can be generated with less dangerous by-products'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of ac over dc in utility applications is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Charging a piece of wire.'
        choice_b = 'Storing energy as magnetic field*'
        choice_c = 'Choking-off high frequency ac'
        choice_d = 'Introducing resistance into a circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" =An inductor works by """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'The diameter of the wire.*'
        choice_b = 'The number of turns.'
        choice_c = 'The type of core material.'
        choice_d = 'The length of the coil.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following does NOT affect the inductance of the coil? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Energy is stored and released slowly'
        choice_b = 'The current flow is always large'
        choice_c = 'The current flow is always small'
        choice_d = 'Energy is stored and released quickly*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a small inductance """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increase the current carrying capacity'
        choice_b = 'Increase the inductance*'
        choice_c = 'Limit the current'
        choice_d = 'Reduce the inductance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ferromagnetic core is placed in an inductor mainly to """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'Like resistors in parallel'
        choice_b = 'Like resistors in series*'
        choice_c = 'Like batteries in series with opposite polarities'
        choice_d = 'In a way unlike any other type of component'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Inductors in series, assuming there is no mutual inductance, combine: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_6:
    def __init__(self, *args, **kwargs):
        choice_a = '1.8 H'
        choice_b = '22 mH'
        choice_c = '88 mH*'
        choice_d = '21 mH'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two inductors are connected in series, without mutual inductance. Their values are 33 mH and 55 mH. The net inductance of the combination is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_7:
    def __init__(self, *args, **kwargs):
        choice_a = '1.8 H'
        choice_b = '22 mH'
        choice_c = '88 mH'
        choice_d = '21 mH*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two inductors are connected in parallel, without mutual inductance. Their values are 33 mH and 55 mH. The net inductance of the combination is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_8:
    def __init__(self, *args, **kwargs):
        choice_a = '4 nH'
        choice_b = '140 uH'
        choice_c = '5 H*'
        choice_d = 'None of these'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three inductors are connected in series without mutual inductance. Their values are 4 nH, 140 μH, and 5 H. For practical purposes, the net inductance will be very close to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_9:
    def __init__(self, *args, **kwargs):
        choice_a = '4 nH*'
        choice_b = '140 uH'
        choice_c = '5 H'
        choice_d = 'None of these'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Suppose the three inductors mentioned above are connected in parallel without mutual inductance. The net inductance will be close to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_10:
    def __init__(self, *args, **kwargs):
        choice_a = '50 uH'
        choice_b = '120 uH'
        choice_c = '200 uH'
        choice_d = '280 uH*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two inductors, each of 100 μH, are in series. The coefficient of coupling is 0.40. The net inductance, if the coil fields reinforce each other, is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_11:
    def __init__(self, *args, **kwargs):
        choice_a = '50 uH'
        choice_b = '120 uH*'
        choice_c = '200 uH'
        choice_d = '280 uH'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the coil fields oppose in the foregoing series-connected arrangement, the net inductance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_12:
    def __init__(self, *args, **kwargs):
        choice_a = '7.5 mH'
        choice_b = '132 mH'
        choice_c = '190 mH'
        choice_d = '260 mH*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two inductors, having values of 44 mH and 88 mH, are connected in series with a coefficient of coupling equal to 1.0 (maximum possible mutual inductance). If their fields reinforce, the net inductance (to two significant digits) is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_13:
    def __init__(self, *args, **kwargs):
        choice_a = '7.5 mH*'
        choice_b = '132 mH'
        choice_c = '190 mH'
        choice_d = '260 mH'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the fields in the previous situation oppose, the net inductance will be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increases the inductance.*'
        choice_b = 'Reduces the inductance'
        choice_c = 'Has no effect on the inductance, but increases the current-carrying capacity of the coil.'
        choice_d = 'Raises the frequency.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""With permeability tuning, moving the core further into a solenoidal coil:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'The toroid is easier to wind'
        choice_b = 'The solenoid cannot carry as much current'
        choice_c = 'The toroid is easier to tune'
        choice_d = 'The magnetic flux in a toroid is practically all within the core*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A significant advantage, in some situations, of a toroidal coil over a solenoid is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'High current capacity'
        choice_b = 'Large inductance in small volume*'
        choice_c = 'Efficiency at very high frequencies'
        choice_d = 'Ease of inductance adjustment'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A major feature of a pot-core winding"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has excellent efficiency*'
        choice_b = 'Has high permeability'
        choice_c = 'Allows large inductance in a small volume'
        choice_d = 'Has a permeability that can vary over a wide range'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As an inductor core material, air: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Air-core'
        choice_b = 'Solenoidal'
        choice_c = 'Toroidal*'
        choice_d = 'Transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At a frequency of 400 Hz, the most likely from for an inductor would be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Air-core*'
        choice_b = 'Pot-core'
        choice_c = 'Either of the two valid choices'
        choice_d = 'None of the two valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At a frequency of 95 MHz, the most likely form for an inductor would be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_10_20:
    def __init__(self, *args, **kwargs):
        choice_a = '16.7 m'
        choice_b = '11 m'
        choice_c = '16.7 m'
        choice_d = '11 cm*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmission line inductor made from coaxial cable, having velocity factor of 0.66, and working at 450 MHz, would be shorter than"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current'
        choice_b = 'Voltage'
        choice_c = 'A magnetic field'
        choice_d = 'An electric field*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Capacitance acts to store electrical energy as: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'The capacitance increases*'
        choice_b = 'The capacitance decreases'
        choice_c = 'The capacitance does not change'
        choice_d = 'The voltage-handling ability increases'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As capacitor plate area, all other things being equal: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'The capacitance increases.*'
        choice_b = 'The capacitance decreases.'
        choice_c = 'The capacitance does not change.'
        choice_d = 'The voltage-handling ability increases.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the spacing between plates in a capacitor is made smaller, all other things being equal:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Acts to increase capacitance per unit volume.*'
        choice_b = 'Acts to decrease capacitance per unit volume.'
        choice_c = 'Has no effect on capacitance.'
        choice_d = 'Causes a capacitor to become polarized.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A material with a high dielectric constant: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_5:
    def __init__(self, *args, **kwargs):
        choice_a = '0.01 uF'
        choice_b = '0.001 uF'
        choice_c = '0.0001 uF*'
        choice_d = '0.00001 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitance of 100 pF is the same as: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_6:
    def __init__(self, *args, **kwargs):
        choice_a = '33 pF'
        choice_b = '330 pF'
        choice_c = '3300 pF'
        choice_d = '33,000 pF*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitance of 0.033 μF is the same as: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_7:
    def __init__(self, *args, **kwargs):
        choice_a = '0.010 μF.'
        choice_b = '0.25 uF*'
        choice_c = '0.50 uF'
        choice_d = '0.025 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Five 0.050-μF capacitors are connected in parallel. The total capacitance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_8:
    def __init__(self, *args, **kwargs):
        choice_a = '0.010 μF*'
        choice_b = '0.25 uF'
        choice_c = '0.50 uF'
        choice_d = '0.025 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Five 0.050-μF capacitors are connected in series. The total capacitance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_9:
    def __init__(self, *args, **kwargs):
        choice_a = '80 pF'
        choice_b = '47 pF'
        choice_c = '33 pF'
        choice_d = '19 pF*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two capacitors are in series. Their values are 47 pF and 33 pF. The composite value is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_10:
    def __init__(self, *args, **kwargs):
        choice_a = '47 pF'
        choice_b = '517 pF'
        choice_c = '517 uF'
        choice_d = '470 uF*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two capacitors are in parallel. Their values are 47 pF and 470 μF. The combination capacitance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_11:
    def __init__(self, *args, **kwargs):
        choice_a = '0.0125 uF'
        choice_b = '0.170 uF*'
        choice_c = '0.1 uF'
        choice_d = '0.125 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three capacitors are in parallel. Their values are 0.0200 μF, 0.0500 μF and 0.10000 μF. The total capacitance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has a high dielectric constant.'
        choice_b = 'Is not physically dense'
        choice_c = 'Has low loss*'
        choice_d = 'Allows for large capacitance in a small volume'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Air works well as a dielectric mainly because it:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'High efficiency'
        choice_b = 'Small size*'
        choice_c = 'Capability to handle high voltages'
        choice_d = 'Low loss'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is NOT a characteristic of mica capacitors?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_14:
    def __init__(self, *args, **kwargs):
        choice_a = '100 pF*'
        choice_b = '33 uF'
        choice_c = '470 uF'
        choice_d = '10,000 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A disk ceramic capacitor might have a value of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_15:
    def __init__(self, *args, **kwargs):
        choice_a = '0.001 pF'
        choice_b = '0.01 uF*'
        choice_c = '100 uF'
        choice_d = '3300 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A paper capacitor might have a value of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_16:
    def __init__(self, *args, **kwargs):
        choice_a = '0.01 uF to 1 uF'
        choice_b = '1 uF to 100 uF'
        choice_c = '1 pF to 100 pF*'
        choice_d = '0.001 pF to 0.1 pF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An air-variable capacitor might have a range of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Paper'
        choice_b = 'Mica'
        choice_c = 'Interelectrode'
        choice_d = 'Electrolytic*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following types of capacitors is polarized? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_11_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Its value decreases as the temperature rises.*'
        choice_b = 'Its value increases as the temperature rises.'
        choice_c = 'Its value does not change with temperature.'
        choice_d = 'It must be connected with the correct polarity.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a capacitor has a negative temperature coefficient:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_19:
    def __init__(self, *args, **kwargs):
        choice_a = '30 pF'
        choice_b = '37 pF*'
        choice_c = '35 pF'
        choice_d = '31 pF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor is rated at 33 pF, plus or minus 10 percent. Which of the following capacitances is outside the acceptable range?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_11_20:
    def __init__(self, *args, **kwargs):
        choice_a = '0.039'
        choice_b = '3.9*'
        choice_c = '0.041'
        choice_d = '4.1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor, rated at 330 pF, shows an actual value of 317 pF. How many percent off is its value?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'The wave shape is identical for each cycle'
        choice_b = 'The polarity reverses periodically'
        choice_c = 'The electrons always flow in the same direction.*'
        choice_d = 'There is a definite frequency.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not a general characteristic of an ac wave?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Always has the same general appearance.*'
        choice_b = 'Has instantaneous rise and fall times.'
        choice_c = 'Is in the same phase as a cosine wave.'
        choice_d = 'Rises very fast, but decays slowly.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A sine wave: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is shifted in phase by 1⁄2 cycle from the sine wave.'
        choice_b = 'Is a representation of the rate of change.*'
        choice_c = 'Has instantaneous rise and fall times.'
        choice_d = 'Rises very fast, but decays slowly.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The derivative of a sine wave:  """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_4:
    def __init__(self, *args, **kwargs):
        choice_a = '1/4 revolution'
        choice_b = '1/2 revolution*'
        choice_c = 'A full revolution'
        choice_d = 'Two full revolutions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A phase difference of 180 degrees in the circular model represents: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_5:
    def __init__(self, *args, **kwargs):
        choice_a = '90'
        choice_b = '180'
        choice_c = '270'
        choice_d = '360*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You can add or subtract a certain number of degrees of phase to or from a wave, and end up with exactly the same wave again. This number is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_6:
    def __init__(self, *args, **kwargs):
        choice_a = '90'
        choice_b = '180*'
        choice_c = '270'
        choice_d = '360'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You can add or subtract a certain number of degrees of phase to or from a sine wave, and end up with an inverted (upside-down) representation of the original. This number is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_7:
    def __init__(self, *args, **kwargs):
        choice_a = '1/300 second'
        choice_b = '0.00333 second'
        choice_c = '1/3000 second'
        choice_d = '0.00000333 second*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A wave has a frequency of 300 kHz. One complete cycle takes: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_8:
    def __init__(self, *args, **kwargs):
        choice_a = '0.00273 second'
        choice_b = '0.000273 second'
        choice_c = '0.0000631 second*'
        choice_d = '0.00000631 second'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a wave has a frequency of 440 Hz, how long does it take for 10 degrees of phase?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_9:
    def __init__(self, *args, **kwargs):
        choice_a = '8 V peak, in phase with the composites.*'
        choice_b = '2 V peak, in phase with the composites.'
        choice_c = '8 V peak, in phase opposition with respect to the composites.'
        choice_d = '2 V peak, in phase opposition with respect to the composites.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two waves are in phase coincidence. One has a peak value of 3 V and the other a peak value of 5 V. The resultant will be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Moving it to the right or left by a full cycle.'
        choice_b = 'Moving it to the right or left by 1⁄4 cycle.*'
        choice_c = 'Turning it upside-down.'
        choice_d = 'Leaving it alone.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Shifting the phase of an ac sine wave by 90 degrees is the same thing as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'An offset of more than one cycle.'
        choice_b = 'Phase opposition.*'
        choice_c = 'A cycle and a half.'
        choice_d = '1.5 Hz.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A phase difference of 540 degrees would more often be spoken of as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_12:
    def __init__(self, *args, **kwargs):
        choice_a = '4 V, in phase with the composites.'
        choice_b = '4 V, out of phase with the composites.'
        choice_c = '4 V, in phase with wave X.'
        choice_d = '4 V, in phase with wave Y.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two sine waves are in phase opposition. Wave X has a peak amplitude of 4 V and wave Y has a peak amplitude of 8 V. The resultant has a peak amplitude of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Wave Y is 1⁄4 cycle ahead of wave X.'
        choice_b = 'Wave Y is 1⁄4 cycle behind wave X.'
        choice_c = 'Wave Y is 1⁄8 cycle behind wave X.*'
        choice_d = 'Wave Y is 1⁄16 cycle ahead of wave X.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If wave X leads wave Y by 45 degrees of phase, then: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Y is 120 degrees earlier than X.*'
        choice_b = 'Y is 90 degrees earlier than X.'
        choice_c = 'Y is 60 degrees earlier than X.'
        choice_d = 'Y is 30 degrees earlier than X.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If wave X lags wave Y by 1⁄3 cycle, then: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'X lags Y by 45 degrees.'
        choice_b = 'X leads Y by 45 degrees.'
        choice_c = 'X lags Y by 135 degrees.*'
        choice_d = 'X leads Y by 135 degrees.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the drawing 
        https://lesliecaminadecom.files.wordpress.com/2019/08/brkeotspx6mh5t7rilhi.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'A'
        choice_b = 'B*'
        choice_c = 'C'
        choice_d = 'D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)

        self.question = f"""Which of the following corresponds to the situation in the figure https://lesliecaminadecom.files.wordpress.com/2019/08/brkeotspx6mh5t7rilhi.png
        
        Choices
        https://lesliecaminadecom.files.wordpress.com/2019/08/sdwhz93z2rqno24lmru5.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Average amplitude'
        choice_b = 'Frequency'
        choice_c = 'Phase difference'
        choice_d = 'Peak amplitude*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In vector diagrams, length of the vector represents"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Average amplitude'
        choice_b = 'Frequency'
        choice_c = 'Phase difference*'
        choice_d = 'Peak amplitude'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In vector diagrams, the angle between the two vectors represents"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Average amplitude'
        choice_b = 'Frequency'
        choice_c = 'Phase difference'
        choice_d = 'Peak amplitude*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In vector diagrams, the distance from the center of the graph represents """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_12_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Movement to the right'
        choice_b = 'Movement to the left'
        choice_c = 'Rotation counterclockwise*'
        choice_d = 'Rotation clockwise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In vector diagrams, the progression of time is depicted as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Become very large'
        choice_b = 'Stay the same'
        choice_c = 'Decrease to near zero*'
        choice_d = 'Be stored in the core material'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the number of turns in a coil increases, the current in the coil will eventually"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increases*'
        choice_b = 'Decreases'
        choice_c = 'Stays the same'
        choice_d = 'Is stored in the core material'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the number of turns increases, the reactance"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increases'
        choice_b = 'Decreases*'
        choice_c = 'Stays the same'
        choice_d = 'Depends on the voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the frequency of an ac wave gets lower, the value of XL for a particular coil: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_4:
    def __init__(self, *args, **kwargs):
        choice_a = '0.628 ohms'
        choice_b = '6.28 ohms'
        choice_c = '62.8 ohms'
        choice_d = '628 ohms*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil has an inductance of 100 mH. What is the reactance at a frequency of 1000 Hz."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_13_5:
    def __init__(self, *args, **kwargs):
        choice_a = '0.637 H'
        choice_b = '628 H'
        choice_c = '63.7 mH*'
        choice_d = '628 mH'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil shows an inductive reactance of 200 ohms at 500 Hz. What is its inductance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_6:
    def __init__(self, *args, **kwargs):
        choice_a = '13 kHz*'
        choice_b = '0.013 kHz'
        choice_c = '83 kHz'
        choice_d = '83 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil has an inductance of 400 uH. Its reactance is 33 ohms. What is the frequency? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_7:
    def __init__(self, *args, **kwargs):
        choice_a = '670 mH'
        choice_b = '670 uH*'
        choice_c = '460 mH'
        choice_d = '460 uH'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An inductor has XL = 555 ohms at f = 132 kHz. What is L?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_8:
    def __init__(self, *args, **kwargs):
        choice_a = '682 ohms'
        choice_b = '4.28 ohms'
        choice_c = '4.28 kohms*'
        choice_d = '4.28 Mohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil has L = 689 uH at f = 990 Hz. What is XL = ?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_9:
    def __init__(self, *args, **kwargs):
        choice_a = '55.3 kHz'
        choice_b = '55.3 Hz'
        choice_c = '181 kHz'
        choice_d = '181 Hz*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An inductor has 88 mH with XL = 100 ohms. What is f?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Corresponds to a unique resistance'
        choice_b = 'Corresponds to a unique inductance'
        choice_c = 'Corresponds ro a unique combination of resistance and inductive reactance*'
        choice_d = 'Corresponds to a unique combination of resistance and inductance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Each point in the RL plane"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'A vector pointing straight up'
        choice_b = 'A vector pointing east'
        choice_c = 'A circle'
        choice_d = 'A ray of unlimited length*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the resistance R and the inductive reactance XL both vary from zero to unlimited values, but are always in the ration 3:1, the points in the RL plane from all the resulting impedances will fall along"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_13_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Corresponds to a unique point in the RL plane'
        choice_b = 'Corresponds to a unique inductive reactance'
        choice_c = 'Corresponds to a unique resistance'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Each impedance R + j XL"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Magnitude and direction*'
        choice_b = 'Resistance and inductance'
        choice_c = 'Resistance and reactance'
        choice_d = 'Inductance and reactance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A vector is a quantity that has: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increases'
        choice_b = 'Decreases*'
        choice_c = 'Stays the same'
        choice_d = 'Cannot be found'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an RL circuit, as the ratio of inductive reactance to resistance, XL/R, decreases, the phase angle: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increasing'
        choice_b = 'Decreasing'
        choice_c = '0 degrees'
        choice_d = '90 degrees*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a purely reactive circuit, the phase angle is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_16:
    def __init__(self, *args, **kwargs):
        choice_a = '0 degrees'
        choice_b = '45 degrees*'
        choice_c = '90 degrees'
        choice_d = 'Impossible to find, there\'s not enough data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the inductive reactance is the same as the resistance in an RL circuit, the phase angle is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_17:
    def __init__(self, *args, **kwargs):
        choice_a = '8.0'
        choice_b = '90'
        choice_c = '90 + j 8.0'
        choice_d = '8.0 + j 90*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the figure, the impedance shown is
        https://lesliecaminadecom.files.wordpress.com/2019/08/cuxrvccff3b41u742kh5.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'About 50 degrees, from the looks of it.'
        choice_b = '48 degrees, as measured with a protractor.'
        choice_c = '85 degrees, as calculated trigonometrically.*'
        choice_d = '6.5 degrees, as calculated trigonometrically.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the figure, note that the R and XL scale divisions are of different sizes. The phase angle is is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_19:
    def __init__(self, *args, **kwargs):
        choice_a = '45.0 degrees'
        choice_b = '51.5 degrees*'
        choice_c = '38.5 degrees'
        choice_d = 'There is not enough data to know'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An RL circuit consists of a 100 uH inductor and a 100 ohms resistor. What is the phase angle at a frequency of 200 kHz? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_13_20:
    def __init__(self, *args, **kwargs):
        choice_a = '78 degrees*'
        choice_b = '12 degrees'
        choice_c = '43 degrees'
        choice_d = '47 degrees'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An RL circuit has an inductance of 88 mH. The resistance is 95 ohms. What is the phase angle at 800 Hz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'The value of XC increases negatively.'
        choice_b = 'The value of XC decreases negatively.*'
        choice_c = 'The value of XC does not change.'
        choice_d = 'You can’t say what happens to XC without more data.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the size of the plates in a capacitor increases, all other things being equal: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'The value of XC increases negatively.'
        choice_b = 'The value of XC decreases negatively.'
        choice_c = 'The value of XC does not change.'
        choice_d = 'You can’t say what happens to XC without more data.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the dielectric material between the plates of a capacitor is changed, all other things being equal: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increases negatively.*'
        choice_b = 'Decreases negatively.'
        choice_c = 'Does not change.'
        choice_d = 'Depends on the current.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the frequency of a wave gets lower, all other things being equal, the value of XC for a capacitor:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_4:
    def __init__(self, *args, **kwargs):
        choice_a = '- 1.66 ohms'
        choice_b = '- 0.00166 ohms'
        choice_c = '- 603 ohms*'
        choice_d = '- 603 kohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has a value of 330 pF. What is its capacitive reactance at a frequency of 800 kHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_5:
    def __init__(self, *args, **kwargs):
        choice_a = '9.39 uF'
        choice_b = '93.9 uF*'
        choice_c = '7.42 uF'
        choice_d = '74.2 uF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has a reactance of -4.50 Ω at 377 Hz. What is its capacitance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_6:
    def __init__(self, *args, **kwargs):
        choice_a = '72 Hz*'
        choice_b = '7.2 MHz'
        choice_c = '0.000072 Hz'
        choice_d = '7.2 Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has a value of 47 μF. Its reactance is - 47 Ω. What is the frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_7:
    def __init__(self, *args, **kwargs):
        choice_a = '2.18 uF'
        choice_b = '21.8 pF*'
        choice_c = '0.00218 uF'
        choice_d = '2.18 pF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has XC = - 8800 Ω at f = 830 kHz. What is C?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_8:
    def __init__(self, *args, **kwargs):
        choice_a = '- 2.4 kohms*'
        choice_b = '- 2.4 ohms'
        choice_c = '- 2.4 e-06 ohms'
        choice_d = '- 2.4 Mohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has C = 166 pF at f = 400 kHz. What is XC?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_9:
    def __init__(self, *args, **kwargs):
        choice_a = '1.0 Hz*'
        choice_b = '10 Hz'
        choice_c = '1.0 kHz'
        choice_d = '10 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has C = 4700 μF and XC = - 33 Ω. What is f?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Corresponds to a unique inductance.'
        choice_b = 'Corresponds to a unique capacitance.'
        choice_c = 'Corresponds to a unique combination of resistance and capacitance.'
        choice_d = 'Corresponds to a unique combination of resistance and reactance.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Each point in the RC plane: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Rotate clockwise.'
        choice_b = 'Rotate counterclockwise.'
        choice_c = 'Always point straight towards the right.*'
        choice_d = 'Always point straight down.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If R increases in an RC circuit, but XC is always zero, then the vector in the RC plane will:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Get longer and rotate clockwise.'
        choice_b = 'Get longer and rotate counterclockwise.*'
        choice_c = 'Get shorter and rotate clockwise.'
        choice_d = 'Get shorter and rotate counterclockwise.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the resistance R increases in an RC circuit, but the capacitance and the frequency are nonzero and constant, then the vector in the RC plane will:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Represents a unique combination of resistance and capacitance.'
        choice_b = 'Represents a unique combination of resistance and reactance.*'
        choice_c = 'Represents a unique combination of resistance and frequency.'
        choice_d = 'All of the above.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Each impedance R - jXC:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Gets closer to - 90 degrees.'
        choice_b = 'Gets closer to 0 degrees.*'
        choice_c = 'Stays the same.'
        choice_d = 'Cannot be found.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an RC circuit, as the ratio of capacitive reactance to resistance, - XC/R, gets closer to zero, the phase angle:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increasing.'
        choice_b = 'Decreasing.'
        choice_c = '0 degrees.*'
        choice_d = '- 90 degrees.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a purely resistive circuit, the phase angle is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_16:
    def __init__(self, *args, **kwargs):
        choice_a = '0 degrees.'
        choice_b = '- 45 degrees.*'
        choice_c = '- 90 degrees.'
        choice_d = 'Impossible to find; there’s not enough data given.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the ratio of XC/R is 1, the phase angle is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_14_17:
    def __init__(self, *args, **kwargs):
        choice_a = '8.02 + j323.'
        choice_b = '323 + j8.02'
        choice_c = '8.02 - j323*'
        choice_d = '323 - j8.02'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The impedance shown in the figure https://lesliecaminadecom.files.wordpress.com/2019/08/xj0ddyeapjiqxg6mz5co.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_18:
    def __init__(self, *args, **kwargs):
        choice_a = '1.42 degrees'
        choice_b = 'About - 60 degrees, from the looks of it'
        choice_c = '-58.9 degrees'
        choice_d = '-88.6 degrees*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the figure, note that the R and XC scale divisions are not the same size. The phase angle is
        https://lesliecaminadecom.files.wordpress.com/2019/08/xj0ddyeapjiqxg6mz5co.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_19:
    def __init__(self, *args, **kwargs):
        choice_a = '-67.4 degrees*'
        choice_b = '-22.6 degrees'
        choice_c = '-24.4 degrees'
        choice_d = '-65.6 degrees'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An RC circuit consists of a 150-pF capacitor and a 330 Ω resisitor in series. What is the phase angle at a frequency of 1.34 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_14_20:
    def __init__(self, *args, **kwargs):
        choice_a = '-24 degrees'
        choice_b = '-0.017 degrees'
        choice_c = '-66 degrees*'
        choice_d = 'None of the above'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An RC circuit has a capitance of 0.015 μF. The resistance is 52 Ω. What is the phase angle at 90 kHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Can never be negative'
        choice_b = 'Can never be positive*'
        choice_c = 'Might be either negative or positive'
        choice_d = 'Is equal to j'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The square of an imaginary number: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is the same thing as an imaginary number.'
        choice_b = 'Has a real part and an imaginary part.*'
        choice_c = 'Is one-dimensional.'
        choice_d = 'Is a concept reserved for elite imaginations.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A complex number"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_3:
    def __init__(self, *args, **kwargs):
        choice_a = '0 + j0*'
        choice_b = '6 + j14'
        choice_c = '- 6 - j14'
        choice_d = '0 - j14'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the sum of 3 + j7 and -3 - j7? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_4:
    def __init__(self, *args, **kwargs):
        choice_a = '- 1 + j2'
        choice_b = '- 9 - j2'
        choice_c = '- 1 - j2'
        choice_d = '- 9 + j12*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is (-5 + j7) - (4 - j5)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_5:
    def __init__(self, *args, **kwargs):
        choice_a = '24 - j14'
        choice_b = '-38 - j34*'
        choice_c = '-24 - j14'
        choice_d = '-24 + j14'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the product (- 4 - j7)(6 - j2)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_6:
    def __init__(self, *args, **kwargs):
        choice_a = '42'
        choice_b = '-42'
        choice_c = '30*'
        choice_d = '-30'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the magnitude of the vector 18 - j24?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'A pure resistance*'
        choice_b = 'A pure inductance'
        choice_c = 'A pure capacitance'
        choice_d = 'An inductance combined with a capacitance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The impedance vector 5 + j0 represents: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'A pure resistance'
        choice_b = 'A pure inductance'
        choice_c = 'A pure capacitance*'
        choice_d = 'An inductance combined with a resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The impedance vector 0 - j22 represents:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Z = 9 ohms'
        choice_b = 'Z = 3 ohms'
        choice_c = 'Z = 45 ohms'
        choice_d = 'Z = 6.7 ohms*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the absolute-value impedance of 3.0 - j6.0?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Z = 240 ohms*'
        choice_b = 'Z = 58,000 ohms'
        choice_c = 'Z = 285 ohms'
        choice_d = 'Z = - 185 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the absolute value impedance of 50 - j235?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'It will increase*'
        choice_b = 'It will decrease'
        choice_c = 'It will stay the same'
        choice_d = 'There is no way to know'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the center conductor of a coaxial cable is made to have smaller diameter, all other things being equal, what will happen to the Zo of the transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'R + jX = 100 + j 0*'
        choice_b = 'R + jX = 0 + j100'
        choice_c = 'R + jX = 0 - j100'
        choice_d = 'You need to know more specific information'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a device is said to have an impedance of Z = 100 Ω, this would most often mean that:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'j4.79'
        choice_b = '-j4.79'
        choice_c = 'j0.209*'
        choice_d = '-j0.209'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A capacitor has a value of 0.050 μF at 665 kHz. What is the capacitive susceptance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_14:
    def __init__(self, *args, **kwargs):
        choice_a = '-j0.060*'
        choice_b = 'j0.060'
        choice_c = '-j17'
        choice_d = 'j17'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An inductor has a value of 44 mH at 60 Hz. What is the inductive susceptance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Impedance'
        choice_b = 'Inductance'
        choice_c = 'Reactance'
        choice_d = 'Admittance*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Susceptance and conductance add to form: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_15_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'G^2  + B^2'
        choice_b = 'R^2 + X^2*'
        choice_c = 'Zo'
        choice_d = 'Y'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Absolute value impedance is equal to the square root of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ohms'
        choice_b = 'Henrys'
        choice_c = 'Farads'
        choice_d = 'Siemens*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Inductive susceptance is measured in: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Positive and real valued'
        choice_b = 'Negative and real valued'
        choice_c = 'Positive and imaginary'
        choice_d = 'Negative and imaginary*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Capacitive susceptance is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Bc = 1 / Xc'
        choice_b = 'Complex impedance can be depicted as a vector'
        choice_c = 'Characteristic impedance is complex*'
        choice_d = 'G = 1/R'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is false?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_15_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'The greater the flow of alternating current.'
        choice_b = 'The less the flow of alternating current.*'
        choice_c = 'The larger the reactance.'
        choice_d = 'The larger the resistance.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In general, the greater the absolute value of the impedance in a circuit: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_1:
    def __init__(self, *args, **kwargs):
        choice_a = '0 + j550'
        choice_b = '0 - j50*'
        choice_c = '250 - j300'
        choice_d = '-300 + j250'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil and capacitor are connected in series. The inductive reactance is 250 Ω, and the capacitive reactance is -300 Ω. What is the net impedance vector, R + jX?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_2:
    def __init__(self, *args, **kwargs):
        choice_a = '0 + j467*'
        choice_b = '25 + j100'
        choice_c = '0 - j467'
        choice_d = '25 - j100'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil of 25.0 μH and capacitor of 100 pF are connected in series. The frequency is 5.00 MHz. What is the impedance vector, R + jX?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Always points straight up'
        choice_b = 'Always points straight down'
        choice_c = 'Always points straight towards the right'
        choice_d = 'None of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When R = 0 in a series RLC circuit, but the net reactance is not zero, the impedance vector:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_4:
    def __init__(self, *args, **kwargs):
        choice_a = '150 + j100'
        choice_b = '150 - j200'
        choice_c = '100 - j200'
        choice_d = '150 - j100*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor of 150 Ω, a coil with reactance 100 Ω and a capacitor with reactance –200 Ω are connected in series. What is the complex impedance R + jX?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_5:
    def __init__(self, *args, **kwargs):
        choice_a = '330 - j199'
        choice_b = '300 + j201'
        choice_c = '300 + j142'
        choice_d = '330 - j16.8*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor of 330 Ω, a coil of 1.00 μH and a capacitor of 200 pF are in series. What is R + jX at 10.0 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_6:
    def __init__(self, *args, **kwargs):
        choice_a = '10 + j3.00'
        choice_b = '10 + j29.2*'
        choice_c = '10 - j97'
        choice_d = '10 + j348'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil has an inductance of 3.00 μH and a resistance of 10.0 Ω in its winding. A capacitor of 100 pF is in series with this coil. What is R + jX at 10.0 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_7:
    def __init__(self, *args, **kwargs):
        choice_a = '0 + j0.25'
        choice_b = '0 + j4.00'
        choice_c = '0 - j0.25*'
        choice_d = '0 - j4.00'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil has a reactance of 4.00 Ω. What is the admittance vector, G + jB, assuming nothing else is in the circuit?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'It will decrease to half its former value.'
        choice_b = 'It will not change.'
        choice_c = 'It will double.*'
        choice_d = 'It will quadruple.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What will happen to the susceptance of a capacitor if the frequency is doubled, all other things being equal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_9:
    def __init__(self, *args, **kwargs):
        choice_a = '0 - j0.02*'
        choice_b = '0 - j0.07'
        choice_c = '0 + j0.02'
        choice_d = '-0.05 + j0.03'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil and capacitor are in parallel, with jBL = - j0.05 and jBC = j0.03. What is the admittance vector, assuming that nothing is in series or parallel with these components?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_10:
    def __init__(self, *args, **kwargs):
        choice_a = '1 + j0'
        choice_b = '1 + j1.5'
        choice_c = '1 - j1.5*'
        choice_d = '1 - j2'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil, resistor, and capacitor are in parallel. The resistance is 1 Ω ; the capacitive susceptance is 1.0 siemens; the inductive susceptance is - 1.0 siemens. Then the frequency is cut to half its former value. What will be the admittance vector, G + jB, at the new frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_11:
    def __init__(self, *args, **kwargs):
        choice_a = '0 + j0.00282'
        choice_b = '0 - j0.00194*'
        choice_c = '0 + j0.00194'
        choice_d = '0 - j0.00758'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil of 3.50 μH and a capacitor of 47.0 pF are in parallel. The frequency is 9.55 MHz. There is nothing else in series or parallel with these components. What is the admittance vector?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Pure conductance, zero susceptance.'
        choice_b = 'Conductance and inductive susceptance.*'
        choice_c = 'Conductance and capacitive susceptance.'
        choice_d = 'Pure susceptance, zero conductance.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A vector pointing “southeast” in the GB plane would indicate the following:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_13:
    def __init__(self, *args, **kwargs):
        choice_a = '0.0044 + j0.024*'
        choice_b = '0.035 - j0.011'
        choice_c = '-0.011 + j0.035'
        choice_d = '0.0044 + j0.046'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor of 0.0044 siemens, a capacitor whose susceptance is 0.035 siemens, and a coil whose susceptance is -0.011 siemens are all connected in parallel. The admittance vector is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_14:
    def __init__(self, *args, **kwargs):
        choice_a = '100 + j0.00354'
        choice_b = '0.010 + j0.00354*'
        choice_c = '100 - j0.0144'
        choice_d = '0.010 + j0.0144'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor of 100 Ω, a coil of 4.50 μH, and a capacitor of 220 pF are in parallel. What is the admittance vector at 6.50 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_15:
    def __init__(self, *args, **kwargs):
        choice_a = '50 + j5.0'
        choice_b = '0.495 - j4.95*'
        choice_c = '50 - j5.0'
        choice_d = '0.495 + j4.95'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The admittance for a circuit, G + jB, is 0.02 + j0.20. What is the impedance, R + jX?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_16:
    def __init__(self, *args, **kwargs):
        choice_a = '51.0 - j14.9'
        choice_b = '51.0 + j14.9'
        choice_c = '46.2 - j14.9'
        choice_d = '46.2 + j14.9*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor of 51.0 Ω, an inductor of 22.0 μH and a capacitor of 150 pF are in parallel. The frequency is 1.00 MHz. What is the complex impedance, R + jX?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_17:
    def __init__(self, *args, **kwargs):
        choice_a = '1.18 A'
        choice_b = '1.13 A'
        choice_c = '0.886 A*'
        choice_d = '0.846 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A series circuit has 99.0 Ω of resistance and 88.0 Ω of inductive reactance. An ac rms voltage of 117 V is applied to this series network. What is the current?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_18:
    def __init__(self, *args, **kwargs):
        choice_a = '78.0 V*'
        choice_b = '55.1 V'
        choice_c = '99.4 V'
        choice_d = '74.4 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A series circuit has 99.0 Ω of resistance and 88.0 Ω of inductive reactance. An ac rms voltage of 117 V is applied to this series network. What is the the voltage across the reactance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_19:
    def __init__(self, *args, **kwargs):
        choice_a = '2.00 A'
        choice_b = '2.40 A*'
        choice_c = '1.33 A'
        choice_d = '0.80 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parallel circuit has 10 ohms of resistance and 15 Ω of reactance. An ac rms voltage of 20 V is applied across it. What is the total current?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_16_20:
    def __init__(self, *args, **kwargs):
        choice_a = '2.00 A*'
        choice_b = '2.40 A'
        choice_c = '1.33 A'
        choice_d = '0.800 A'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parallel circuit has 10 ohms of resistance and 15 Ω of reactance. An ac rms voltage of 20 V is applied across it. What is the current through the resistance in the above example?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Radiated power'
        choice_b = 'True power'
        choice_c = 'Imaginary power*'
        choice_d = 'Apparent power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The power in a reactance is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Power that heats a resistor'
        choice_b = 'Power radiated from an antenna'
        choice_c = 'Power in a capacitor*'
        choice_d = 'Heat loss in a feed line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not an example of true power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_3:
    def __init__(self, *args, **kwargs):
        choice_a = '92 watts*'
        choice_b = '100 watts'
        choice_c = '140 watts'
        choice_d = 'Not determinable from this information'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The apparent power in a circuit is 100 watts, and the imaginary power is 40 watts. The true power is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Apparent power divided by true power'
        choice_b = 'Imaginary power divided by apparent power'
        choice_c = 'Imaginary power divided by true power'
        choice_d = 'True power divided by apparent power*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Power factor is equal to: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_5:
    def __init__(self, *args, **kwargs):
        choice_a = '0.334*'
        choice_b = '0.999'
        choice_c = '0.595'
        choice_d = 'It can\'t be found from the data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A circuit has a resistance of 300 W and an inductance of 13.5 μH in series at 10.0 MHz. What is the power factor?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_6:
    def __init__(self, *args, **kwargs):
        choice_a = '99.9 percent'
        choice_b = '56.6 percent*'
        choice_c = '60.5 percent'
        choice_d = '29.5 percent'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A series circuit has Z = 88.4 ohms with R = 50.0 ohms. What is PF? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_7:
    def __init__(self, *args, **kwargs):
        choice_a = '70.9 percent'
        choice_b = '81.6 percent'
        choice_c = '57.8 percent*'
        choice_d = '63.2 percent'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A series circuit has R = 53.5 ohms and X = 75.5 ohms. What is PF? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'arctan Z/R'
        choice_b = 'arctan R/Z'
        choice_c = 'arctan R/X'
        choice_d = 'arctan X/R*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Phase angle is equal to: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_9:
    def __init__(self, *args, **kwargs):
        choice_a = '237 watts'
        choice_b = '204 watts*'
        choice_c = '88.0 watts'
        choice_d = '81.6 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A wattmeter shows 220 watts of VA power in a circuit. There is a resistance of 50 Ω in series with a capacitive reactance of −20 Ω. What is the true power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_10:
    def __init__(self, *args, **kwargs):
        choice_a = '50 ohms'
        choice_b = '57 ohms'
        choice_c = '71 ohms*'
        choice_d = 'It can\'t be calculated from this data'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A wattmeter shows 57 watts of VA power in a circuit. The resistance is known to be 50 Ω, and the true power is known to be 40 watts. What is the absolute-value impedance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'The characteristic impedance'
        choice_b = 'The resistance'
        choice_c = 'Minimizing the loss*'
        choice_d = 'The VA power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is the most important consideration in a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reducing the power output of the source*'
        choice_b = 'Increasing the degree of mismatch between the line and the load'
        choice_c = 'Reducing the diameter of the line conductors'
        choice_d = 'Raising the frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following does not increase the loss in a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Feed line overheating'
        choice_b = 'Excessive power loss'
        choice_c = 'Inaccuracy of the power measurement'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A problem that standing waves can cause is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_14:
    def __init__(self, *args, **kwargs):
        choice_a = '17 kHz*'
        choice_b = '540 Hz'
        choice_c = '17 MHz'
        choice_d = '540 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil and capacitor are in series. The inductance is 88 mH and the capacitance is 1000 pF. What is the resonant frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_15:
    def __init__(self, *args, **kwargs):
        choice_a = '15.9 kHz'
        choice_b = '5.04 MHz'
        choice_c = '15.9 MHz*'
        choice_d = '50.4 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A coil and a capacitor are in parallel, with L = 10 uH and C = 10 pF. What is the resonant frequency? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_16:
    def __init__(self, *args, **kwargs):
        choice_a = '0.945 uF'
        choice_b = '9.45 pF*'
        choice_c = '94.5 pF'
        choice_d = '945 pF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A series-resonant circuit is to be made for 14.1 MHz. A coil of 13.5 μH is available. What size capacitor is needed?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_17:
    def __init__(self, *args, **kwargs):
        choice_a = '2.54 mH'
        choice_b = '254 uH'
        choice_c = '25.4 uH'
        choice_d = '2.54 uH*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parallel-resonant circuit is to be made for 21.3 MHz. A capacitor of 22.0 pF is available. What size coil is needed?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_18:
    def __init__(self, *args, **kwargs):
        choice_a = '11.1 m'
        choice_b = '3.55 m'
        choice_c = '8.87 m'
        choice_d = '2.84 m*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A 1/4-wave line section is made for 21.1 MHz, using cable with a velocity factor of 0.800. How many meters long is it?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_19:
    def __init__(self, *args, **kwargs):
        choice_a = '200 kHz'
        choice_b = '400 kHz'
        choice_c = '3.20 MHz*'
        choice_d = '4.00 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The fourth harmonic of 800 kHz is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_17_20:
    def __init__(self, *args, **kwargs):
        choice_a = '130 feet*'
        choice_b = '1680 feet'
        choice_c = '39.7 feet'
        choice_d = '515 feet'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How long is a 1/2-wave dipole for 3.60 MHz"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'The primary impedance is greater than the secondary impedance.'
        choice_b = 'The secondary winding is right on top of the primary.'
        choice_c = 'The primary voltage is less than the secondary voltage.*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a step up transformer"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Placing the windings on opposite sides of a toroidal core.*'
        choice_b = 'Winding the secondary right on top of the primary.'
        choice_c = 'Using the highest possible frequency.'
        choice_d = 'Using a center tap on the balanced winding.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The capacitance between the primary and the secondary windings of a transformer can be minimized by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_3:
    def __init__(self, *args, **kwargs):
        choice_a = '1:380'
        choice_b = '380:1*'
        choice_c = '1:19.5'
        choice_d = '19.5:1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transformer steps a voltage down from 117 V to 6.00 V. What is its primary-to-secondary turns ratio?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_4:
    def __init__(self, *args, **kwargs):
        choice_a = '23.4 V'
        choice_b = '585 V*'
        choice_c = '117 V'
        choice_d = '2.93 kV'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A step-up transformer has a primary-to-secondary turns ratio of 1:5.00. If 117 V rms appears at the primary, what is the rms voltage across the secondary?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'A step-up unit'
        choice_b = 'A step-down unit*'
        choice_c = 'Neither step-up or step-down'
        choice_d = 'A reversible unit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transformer has a secondary-to-primary turns ratio of 0.167. This transformer is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Air concentrates the magnetic lines of flux.*'
        choice_b = 'Air works at higher frequencies than ferromagnetics.'
        choice_c = 'Ferromagnetics are lossier than air.'
        choice_d = 'A ferromagnetic-core unit needs fewer turns of wire than an equivalent air-core unit.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is false, concerning air cores versus ferromagnetic cores?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'An increase in efficiency.'
        choice_b = 'An increase in coupling between windings.'
        choice_c = 'An increase in core loss.*'
        choice_d = 'An increase in usable frequency range.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Eddy currents cause"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_8:
    def __init__(self, *args, **kwargs):
        choice_a = '234 V'
        choice_b = '468 V'
        choice_c = '117 V'
        choice_d = '58.5 V*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transformer has 117 V rms across its primary and 234 V rms across its secondary. If this unit is reversed, assuming it can be done without damaging the windings, what will be the voltage at the output?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Provides maximum coupling*'
        choice_b = 'Minimizes capacitance between windings'
        choice_c = 'Withstands more voltage than other winding methods'
        choice_d = 'Has windings far apart but along a common axis'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The shell method of transformer winding: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Air core'
        choice_b = 'Ferrormagnetic solenoid core'
        choice_c = 'Ferromagnetic toroid core'
        choice_d = 'Ferromagnetic pot core*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these core types, in general, is best if you need a winding inductance of 1.5 H?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'The toroid works at higher frequencies'
        choice_b = 'The toroid confines the magnetic flux*'
        choice_c = 'The toroid can work for dc as well as for ac'
        choice_d = 'It\'s easier to wind the turns on a toroid'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of a toroid core over a solenoid core is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is easier to regulate than low voltage'
        choice_b = 'The I2R losses are lower*'
        choice_c = 'The electromagnetic fields are stronger'
        choice_d = 'Smaller transformers can be used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""High voltage is used in long-distance power transmission because: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'One phase'
        choice_b = 'Two phases'
        choice_c = 'Three phases*'
        choice_d = 'Four phases'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a household circuit, the 234-V power has: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'The primary winding'
        choice_b = 'The secondary winding'
        choice_c = 'The unbalanced winding'
        choice_d = 'The balanced winding*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a transformer, a center tap would probably be found in: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_18_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Works automatically'
        choice_b = 'Has a center-tapped secondary'
        choice_c = 'Has one tapped winding*'
        choice_d = 'Is useful only for impedance matching'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An autotransformer: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_16:
    def __init__(self, *args, **kwargs):
        choice_a = '75 ohms*'
        choice_b = '150 ohms'
        choice_c = '600 ohms'
        choice_d = '1200 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transformer has a primary-to-secondary turns ratio of 2.00:1. The input impedance is 300 Ω resistive. What is the output impedance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_17:
    def __init__(self, *args, **kwargs):
        choice_a = '9.00 : 1'
        choice_b = '3.00 : 1'
        choice_c = '1 : 3.00*'
        choice_d = '1 : 9.00'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistive input impedance of 50 Ω must be matched to a resistive output impedance of 450 Ω. The primary-to-secondary turns ratio of the transformer must be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_18:
    def __init__(self, *args, **kwargs):
        choice_a = '150 ohms'
        choice_b = '125 ohms'
        choice_c = '100 ohms'
        choice_d = '113 ohms*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A quarter-wave matching section has a characteristic impedance of 75.0 Ω. The input impedance is 50.0 Ω resistive. What is the resistive output impedance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_19:
    def __init__(self, *args, **kwargs):
        choice_a = '188 ohms'
        choice_b = '150 ohms*'
        choice_c = '225 ohms'
        choice_d = '375 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistive impedance of 75 Ω must be matched to a resistive impedance of 300 Ω. A quarter-wave section would need:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_18_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'The circuit will not work.'
        choice_b = 'There will be an impedance mismatch, no matter what the turns ratio of the transformer.*'
        choice_c = 'A center tap must be used at the secondary.'
        choice_d = 'The turns ratio must be changed to obtain a match'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If there is reactance at the output of an impedance transformer:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_19_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Resistor-like properties of metal oxides.'
        choice_b = 'Variable conductive properties of some materials.*'
        choice_c = 'The fact that there’s nothing better to call silicon.'
        choice_d = 'Insulating properties of silicon and GaAs.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The term "semiconductor" arises from: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Smaller size'
        choice_b = 'Lower working voltage'
        choice_c = 'Lighter weight'
        choice_d = 'Ability to withstand high voltages*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not an advantage of semiconductor devices over vacuum tubes?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Germanium'
        choice_b = 'Galena'
        choice_c = 'Silicon*'
        choice_d = 'Copper'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The most common semiconductor among the following substances is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class gibilisco_19_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Compound*'
        choice_b = 'Element'
        choice_c = 'Conductor'
        choice_d = 'Gas'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""GaAs is a/an """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'The charge carriers move fast'
        choice_b = 'The material does not react to ionizing radiation'
        choice_c = 'It is expensive to produce*'
        choice_d = 'It must be used at high frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A disadvantage of gallium-arsenide devices is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Photocells*'
        choice_b = 'High frequency detectors'
        choice_c = 'Radio frequency power amplifiers'
        choice_d = 'Voltage regulators'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Selenium works especially well in """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'Selenium'
        choice_b = 'Silicon'
        choice_c = 'Copper'
        choice_d = 'Germanium*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Of the following, which material allows the lowest forward voltage drop in a diode?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'Can only work at low frequencies'
        choice_b = 'Is susceptible to damage by static*'
        choice_c = 'Requires considerable power to function'
        choice_d = 'Needs very high voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A CMOS integrated circuit: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Make the charge carriers move faster'
        choice_b = 'Cause holes to flow'
        choice_c = 'Give the semiconductor material certain properties*'
        choice_d = 'Protect devices from damage in case of transients'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The purpose of doping is to: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Adding an acceptor impurity'
        choice_b = 'Adding a donor impurity*'
        choice_c = 'Injecting electrons'
        choice_d = 'Taking electrons away'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A semiconductor material is made into N type by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'The material becomes P-type'
        choice_b = 'Current flows mainly in the form of holes'
        choice_c = 'Most of the charge carriers have positive electric charge'
        choice_d = 'The substance has an electron surplus*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following does not result from adding an acceptor impurity?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Majority carriers'
        choice_b = 'Minority carriers*'
        choice_c = 'Positively charged'
        choice_d = 'Negatively charged'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a P-type material, electrons are:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Minus to plus'
        choice_b = 'Plus to minus*'
        choice_c = 'P-type to N-type material'
        choice_d = 'N-type to P-type material'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Holes flow from: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reverse biased*'
        choice_b = 'Forward biased'
        choice_c = 'Biased past the breaker voltage'
        choice_d = 'In a state of avalanche effect'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a PN junction does not conduct, it is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Charge carriers flow continuously'
        choice_b = 'Charge carriers are passed from atom to atom.*'
        choice_c = 'They have the same polarity'
        choice_d = 'No! Holes flow in the same direction as electrons'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Holes flow the opposite way from electrons because: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'A charge of -1 unit'
        choice_b = 'No charge'
        choice_c = 'A charge of +1 unit*'
        choice_d = 'A charge that depends on the semiconductor type'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an electron has a charge of -1 unit, a hole has:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'The frequency*'
        choice_b = 'The width of the depletion region'
        choice_c = 'The cross sectional area of the junction'
        choice_d = 'The type of semiconductor material'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a P-N junction is reverse-biased, the capacitance depends on all of the following except:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'The junction will be destroyed'
        choice_b = 'The junction will insulate, no current will flow'
        choice_c = 'The junction will conduct current*'
        choice_d = 'The capacitance will become extremely high'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the reverse bias exceeds the avalanche voltage in a P-N junction: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current rectifier'
        choice_b = 'Variable resistor'
        choice_c = 'Variable capacitor'
        choice_d = 'Voltage regulator*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Avalanche voltage is routinely exceeded when a P-N junction acts as a: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_19_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'The type of semiconductor material'
        choice_b = 'The cross sectional area of the junction'
        choice_c = 'The reverse current*'
        choice_d = 'The capacitance with reverse bias'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An unimportant factor concerning the frequency at which a P-N junction will work effectively is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is negative relative to the cathode.'
        choice_b = 'Is positive relative to the cathode.*'
        choice_c = 'Is at the same voltage as the cathode.'
        choice_d = 'Alternates between positive and negative relative to the cathode.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a diode is forward-biased, the anode: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ac with half the frequency of the input'
        choice_b = 'Ac with the same frequency as the input'
        choice_c = 'Ac with twice the frequency as the input'
        choice_d = 'None of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If ac is applied to a diode, and the peak ac voltage never exceeds the avalanche voltage, then the output is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Can be used to transmit radio signals'
        choice_b = 'Requires a battery with long life'
        choice_c = 'Requires no battery*'
        choice_d = 'Is useful for rectifying 60 Hz ac'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A crystal set """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is used in power supplies'
        choice_b = 'Is employed in some radio receivers*'
        choice_c = 'Is used commonly in high power radio transmitters'
        choice_d = 'Changes dc into ac'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A diode detector: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'The circuit is linear*'
        choice_b = 'The circuit is said to be detecting'
        choice_c = 'The circuit is a mixer'
        choice_d = 'The circuit is a rectifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the output wave in a circuit has the same shape as the input wave, then: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_6:
    def __init__(self, *args, **kwargs):
        choice_a = '455 kHz*'
        choice_b = '866 kHz'
        choice_c = '14.00 MHz'
        choice_d = '1.129 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The two input frequencies of a mixer circuit are 3.522 MHz and 3.977 MHz. Which of the following frequencies might be used at the output?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'An ammeter'
        choice_b = 'A spectrum analyzer'
        choice_c = 'A digital voltmeter'
        choice_d = 'An oscilloscope*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A time-domain display might be found in: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'Forward breakover voltage'
        choice_b = 'Peak forward voltage'
        choice_c = 'Avalanche voltage*'
        choice_d = 'Reverse bias'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Zener voltage is also known as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'About 0.3 V'
        choice_b = 'About 0.6 V*'
        choice_c = 'About 1.0 V'
        choice_d = 'Dependent on the method of manufacture'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The forward breakover voltage of a silicon diode is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is useful for voltage regulation'
        choice_b = 'Always uses Zener diode'
        choice_c = 'Rectifies the audio to reduce distortion'
        choice_d = 'Can cause objectionable signal distortion*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A diode audio limiter circuit: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Forward voltage'
        choice_b = 'Reverse voltage*'
        choice_c = 'Avalanche voltage'
        choice_d = 'Forward breakover voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The capacitance of a varactor varies with: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Minimize the diode capacitance*'
        choice_b = 'Optimize the avalanche voltage'
        choice_c = 'Reduce the forward breakover voltage'
        choice_d = 'Increase the current through the diode'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The purpose of the I layer in a PIN diode is to: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'A rectifier diode'
        choice_b = 'A cat whisker'
        choice_c = 'An IMPATT diode*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these diode types might be found in the oscillator circuit of a microwave radio transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Communications device*'
        choice_b = 'Radio detector'
        choice_c = 'Rectifier'
        choice_d = 'Signal mixer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Gunnplexer can be used as a: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'In a rectifier circuit'
        choice_b = 'In a mixer circuit'
        choice_c = 'In a digital frequency display*'
        choice_d = 'In an oscillator circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The most likely place you would find an LED would be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'Gunn diode'
        choice_b = 'Varactor diode'
        choice_c = 'Rectifier diode'
        choice_d = 'Laser diode*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Coherent radiation is produced by a"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'A Gunn diode'
        choice_b = 'An optoisolator*'
        choice_c = 'A photovoltaic cell'
        choice_d = 'A laser diode'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You want a circuit to be stable with a variety of amplifier impedance conditions. You might consider a coupler using:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'The operating frequency of the panel*'
        choice_b = 'The total surface area of the panel'
        choice_c = 'The number of cells in the panel'
        choice_d = 'The intensity of the light'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The power from a solar panel depends on all of the following except: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'High-frequency radio waves'
        choice_b = 'Rectification'
        choice_c = 'Electron energy-level changes*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Emission of energy in an IRED is caused by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_20_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reverse bias*'
        choice_b = 'No bias'
        choice_c = 'Forward bias'
        choice_d = 'Negative resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A photodiode, when not used as a photovoltaic cell, has: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_1:
    def __init__(self, *args, **kwargs):
        choice_a = '60 Hz ac'
        choice_b = 'Smooth dc'
        choice_c = 'Pulsating dc*'
        choice_d = '120 Hz ac'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The output of a rectifier is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'The transformer'
        choice_b = 'The filter'
        choice_c = 'The rectifier'
        choice_d = 'All of the choices are needed*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following might not be needed in a power supply? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'A clock radio'
        choice_b = 'A TV broadcast transmitter*'
        choice_c = 'A shortwave radio receiver'
        choice_d = 'A home TV set'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Of the following appliances, which would need the biggest transformer? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'It uses the whole transformer secondary for the entire ac input cycle*'
        choice_b = 'It costs less than other rectifier types'
        choice_c = 'It cuts off half of the ac wave cycle'
        choice_d = 'It never needs a regulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of full wave bridge rectification is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'Half wave'
        choice_b = 'Full wave center tapped*'
        choice_c = 'Bridge'
        choice_d = 'Voltage multiplier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a supply designed to provide high power at low voltage, the best rectifier design would probably be """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'The transformer'
        choice_b = 'The rectifier'
        choice_c = 'The filter*'
        choice_d = 'The ac input'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The part of a power supply immediately preceding the regulator is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_7:
    def __init__(self, *args, **kwargs):
        choice_a = '52.7 V*'
        choice_b = '105 V'
        choice_c = '117 V'
        choice_d = '328 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a half-wave rectifier is used with 117-V rms ac (house mains), the average dc output voltage is about:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_8:
    def __init__(self, *args, **kwargs):
        choice_a = '50 V'
        choice_b = '70 V*'
        choice_c = '100 V'
        choice_d = '140 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a full-wave bridge circuit is used with a transformer whose secondary provides 50 V rms, the PIV across the diodes is about:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Excessive current'
        choice_b = 'Excessive voltage'
        choice_c = 'Insufficient rectification'
        choice_d = 'Poor regulation*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The principal disadvantage of a voltage multiplier is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_10:
    def __init__(self, *args, **kwargs):
        choice_a = '14 V'
        choice_b = '20 V'
        choice_c = '28 V*'
        choice_d = '36 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transformer secondary provides 10 V rms to a voltage-doubler circuit. The dc output voltage is about:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Twice that from a half-wave circuit*'
        choice_b = 'The same as that from a half-wave circuit'
        choice_c = 'Half that from a half-wave circuit'
        choice_d = 'One-fourth that from a half wave circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The ripple frequency from a full-wave rectifier is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'A capacitor in series'
        choice_b = 'A choke in series'
        choice_c = 'A capacitor in series and a choke in parallel'
        choice_d = 'A capacitor in parallel and a choke in series*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following would make the best filter for a power supply? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Connect several capacitors in parallel'
        choice_b = 'Use a choke input filter'
        choice_c = 'Connect several chokes in series'
        choice_d = 'Use two capacitor/choke sections one after the other*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you needed exceptionally good ripple filtering for a power supply, the best approach would be to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Parallel with the filter output, forward biased'
        choice_b = 'Parallel with the filter output, reverse biased*'
        choice_c = 'Series with the filter output, forward biased'
        choice_d = 'Series with the filter output, reverse biased'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Voltage regulation can be accomplished by a Zener diode connected in"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'The transformer core is suddenly magnetized'
        choice_b = 'The diodes suddenly start to conduct'
        choice_c = 'The filter capacitor(s) must be initially charged*'
        choice_d = 'Arcing takes place in the power switch'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" A current surge takes place when a power supply is first turned on because: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'Diode failure*'
        choice_b = 'Transformer failure'
        choice_c = 'Filter capacitor failure'
        choice_d = 'Poor voltage regulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Transient suppression minimizes the chance of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'The power supply will be severely damaged'
        choice_b = 'The diodes will not rectify'
        choice_c = 'The fuse will blow out right away*'
        choice_d = 'Transient suppressors won\'t work'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a fuse blows, and it is replaced with one having a lower current rating, there’s a good chance that:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'A slow blow type'
        choice_b = 'A quick break type*'
        choice_c = 'Of a low current rating'
        choice_d = 'Of a high current rating'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A fuse with nothing but a straight wire inside is probably: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Connected in parallel with filter capacitors*'
        choice_b = 'Of low ohmic value'
        choice_c = 'Effective for transient suppression'
        choice_d = 'Effective for surge suppression'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Bleeder resistors are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_21_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Install bleeder resistors'
        choice_b = 'Use proper biasing'
        choice_c = 'Leave it alone and have a professional work on it*'
        choice_d = 'Use a voltage regulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To service a power supply with which you are not completely familiar, you should: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has an arrow pointing inward*'
        choice_b = 'Is positive with respect to the emitter'
        choice_c = 'Is biased at a small fraction of the base bias'
        choice_d = 'Is negative with respect to the emitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a PNP circuit, the collector"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'The supply polarity is reversed'
        choice_b = 'The collector and emitter leads are interchanged'
        choice_c = 'The arrow is pointing inward'
        choice_d = 'No! A PNP device cannot be replaced with an NPN*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In many cases, a PNP transistor can be replaced with an NPN device and the circuit will do the same thing, provided that:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Three PN junctions*'
        choice_b = 'Three semiconductor layers'
        choice_c = 'Two N-type layers around a P-type layer'
        choice_d = 'A low avalanche voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A bipolar transistor has: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'The point where the cathodes are connected together'
        choice_b = 'The point where the cathode of one diode is connected to the anode of the other*'
        choice_c = 'The point where the anodes are connected together'
        choice_d = 'Either of the two choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the dual-diode model of an NPN transistor, the emitter corresponds to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'EC'
        choice_b = 'EB relative to EC'
        choice_c = 'IB'
        choice_d = 'More than one of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The current through a transistor depends on"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'The emitter is grounded'
        choice_b = 'The E-B junction is forward biased'
        choice_c = 'The E-B junction is reverse biased*'
        choice_d = 'THe E-B current is high'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" With no signal input, a bipolar transistor would have the least IC when: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'In cutoff'
        choice_b = 'In saturation*'
        choice_c = 'Forward biased'
        choice_d = 'In avalanche'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a transistor is conducting as much as it possibly can, it is said to be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'A'
        choice_b = 'B'
        choice_c = 'C*'
        choice_d = 'D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)

        self.question = f"""The best point to operated a transistor as a small-signal amplifier is: 
        https://lesliecaminadecom.files.wordpress.com/2019/08/efjhl8jyl68bw5prx520.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'No point on this graph'
        choice_b = 'B*'
        choice_c = 'C'
        choice_d = 'D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)

        self.question = f"""The forward breakover point for the BE junction is nearest to: 
        https://lesliecaminadecom.files.wordpress.com/2019/08/efjhl8jyl68bw5prx520.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'A'
        choice_b = 'B'
        choice_c = 'C'
        choice_d = 'D*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        #random.shuffle(choices)

        self.question = f"""The saturation is nearest to point
        https://lesliecaminadecom.files.wordpress.com/2019/08/efjhl8jyl68bw5prx520.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'A'
        choice_b = 'B'
        choice_c = 'C*'
        choice_d = 'D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The greatest gain occurs at point
        https://lesliecaminadecom.files.wordpress.com/2019/08/efjhl8jyl68bw5prx520.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'The frequency at which the gain is 1*'
        choice_b = 'The frequency at which the gain is 0.707 times its value at 1 MHz'
        choice_c = 'The frequency at which the gain is greatest'
        choice_d = 'The difference between the frequency at which the gain is the greatest, and the frequency at which the gain is 1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a common emitter circuit, the gain-bandwidth product is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'The emitter'
        choice_b = 'The base'
        choice_c = 'The collector*'
        choice_d = 'Any point, it doesn\'t matter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The configuration most used for matching a high input impedance to a low output impedance puts signal ground at"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Common emitter circuit'
        choice_b = 'Common base circuit'
        choice_c = 'Common collector circuit'
        choice_d = 'More than one of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The output is in phase with the input in a: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'A common-emitter circuit*'
        choice_b = 'A common-base circuit'
        choice_c = 'A common-collector circuit'
        choice_d = 'More than one of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The greatest possible amplification is obtained in: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'A common-emitter circuit'
        choice_b = 'A common-base circuit'
        choice_c = 'A common-collector circuit'
        choice_d = 'None of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The input is applied to the collector in:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Common-emitter circuit'
        choice_b = 'Common-base circuit*'
        choice_c = 'Common-collector circuit'
        choice_d = 'Emitter-follower circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The configuration noted for its stability in radio-frequency power amplifiers is the: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Emitter '
        choice_b = 'Base '
        choice_c = 'Collector*'
        choice_d = 'More than one of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a common-base circuit, the output is taken from the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'The greatest possible amplification'
        choice_b = 'Reduced efficiency*'
        choice_c = 'Avalanche effect'
        choice_d = 'Nonlinear output impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The input signal to a transistor amplifier results in saturation during part of the cycle. This produces: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_22_20:
    def __init__(self, *args, **kwargs):
        choice_a = '1 kHz'
        choice_b = '335 kHz*'
        choice_c = '210 MHz'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The gain of a transistor in a common-emitter circuit is 100 at a frequency of 1000 Hz. The gain is 70.7 at 335 kHz. The gain drops to 1 at 210 MHz. The alpha cutoff is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Drain voltage'
        choice_b = 'Transconductance*'
        choice_c = 'Gate voltage'
        choice_d = 'Gate bias'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The current through the channel of a JFET is directly affected by all of the following except:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Slightly positive'
        choice_b = 'Zero'
        choice_c = 'Slightly negative'
        choice_d = 'Very negative*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an N-channel JFET, pinchoff occurs when the gate bias is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has a P-type channel*'
        choice_b = 'Is forward biased'
        choice_c = 'Is zero biased'
        choice_d = 'Is reversed biased'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The current consists mainly of holes when a JFET: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'A rectifier'
        choice_b = 'A radio receiver* '
        choice_c = 'A filter'
        choice_d = 'A transformer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A JFET might work better than a bipolar transistor in: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'The drain is forward biased'
        choice_b = 'The gate-source junction is forward biased'
        choice_c = 'The drain is negative relative to the source*'
        choice_d = 'The gate must be at dc ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a P-channel JFET"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'A power amplifier*'
        choice_b = 'A rectifier'
        choice_c = 'An oscillator'
        choice_d = 'A weak-signal amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A JFET is sometimes biased at or beyond pinchoff in: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'Forward bias'
        choice_b = 'High impedance*'
        choice_c = 'Low reverse resistance'
        choice_d = 'Low avalanche voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The gate of a JFET has"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'A pinched-off channel'
        choice_b = 'Holes as the majority carriers'
        choice_c = 'A forward-biased PN junction*'
        choice_d = 'A high input impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A JFET circuit essentially never has:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'dID / dEG is very large with no signal'
        choice_b = 'dID / dEG might vary considerably with no signal'
        choice_c = 'dID / dEG is negative with no signal'
        choice_d = 'dID / dEG is zero with no signal*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a JFET is pinched-off: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'A change in drain voltage to a change in source voltage.'
        choice_b = 'A change in drain current to a change in gate voltage.*'
        choice_c = 'A change in gate current to a change in source voltage.'
        choice_d = 'A change in drain current to a change in drain voltage.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Transconductance is the ratio of """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Drain voltage as a function of source current.'
        choice_b = 'Drain current as a function of gate current.'
        choice_c = 'Drain current as a function of drain voltage.*'
        choice_d = 'Drain voltage as a function of gate current.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Characteristic curves for JFETs generally show: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is easily damaged by static electricity.*'
        choice_b = 'It needs a high input voltage.'
        choice_c = 'It draws a large amount of current.'
        choice_d = 'It produces a great deal of electrical noise.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A disadvantage of a MOS component is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is lower than that of a JFET'
        choice_b = 'Is lower than that of a bipolar transistor'
        choice_c = 'Is between that of a bipolar transistor and a JFET'
        choice_d = 'Is extremely high*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The input impedance of a MOSFET: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'MOSFETs can handle a wider range of gate voltages.*'
        choice_b = 'MOSFETs deliver greater output power.'
        choice_c = 'MOSFETs are more rugged.'
        choice_d = 'MOSFETs last longer.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of MOSFETs over JFETs is that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Pinched-off'
        choice_b = 'Somewhat open'
        choice_c = 'All the way open*'
        choice_d = 'Of P-type semiconductor material'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The channel in a zero-biased JFET is normally: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'The drain current is high with no signal.'
        choice_b = 'The drain current fluctuates with no signal.'
        choice_c = 'The drain current is low with no signal.'
        choice_d = 'The drain current is zero with no signal.*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When an enhancement-mode MOSFET is at zero bias:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'An arrow pointing inward'
        choice_b = 'A broken vertical line inside the circle*'
        choice_c = 'An arrow pointing outward'
        choice_d = 'A solid vertical line inside the circle'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An enhancement-mode MOSFET can be recognized in schematic diagrams by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'None of them'
        choice_b = 'The source'
        choice_c = 'The gate*'
        choice_d = 'The drain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a source follower, which of the electrodes of the FET receives the input signal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Common source*'
        choice_b = 'Common gate'
        choice_c = 'Common drain'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following circuits has its output 180 degrees out of phase with its input?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_23_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Common source*'
        choice_b = 'Common gate'
        choice_c = 'Common drain'
        choice_d = 'It depends only on the bias, not on which electrode is grounded'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following circuits generally has the greatest gain?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Relative signal strength*'
        choice_b = 'Voltage'
        choice_c = 'Power'
        choice_d = 'Current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The decibel is a unit of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_2:
    def __init__(self, *args, **kwargs):
        choice_a = '13 dB'
        choice_b = '20 dB'
        choice_c = '26 dB*'
        choice_d = '40 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a circuit has a voltage amplification factor of 20, then the voltage gain is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'The output signal is stronger than the input'
        choice_b = 'The input signal is stronger than the output*'
        choice_c = 'The input signal is 15 times as strong as the output'
        choice_d = 'The output signal is 15 times as strong as the input'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A gain of -15 dB in a circuit means that: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_4:
    def __init__(self, *args, **kwargs):
        choice_a = '76 V'
        choice_b = '47 V*'
        choice_c = '660 V'
        choice_d = 'Not determinable from the data given'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A device has a voltage gain of 23 dB. The input voltage is 3.3 V. The output voltage is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_5:
    def __init__(self, *args, **kwargs):
        choice_a = '44'
        choice_b = '160'
        choice_c = '440'
        choice_d = '25,000*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A power gain of 44 dB is equivalent to an output/input power ratio of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Provide proper bias*'
        choice_b = 'Provide a path for the input signal'
        choice_c = 'Provide a path for the output signal'
        choice_d = 'Limit the collector current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resistor between the base of an NPN bipolar transistor and the positive supply voltage is used to: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'The supply voltage'
        choice_b = 'The polarity'
        choice_c = 'The signal strength'
        choice_d = 'The signal frequency*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The capacitance values in an amplifier circuit depend on"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'A stereo hi-fi amplifier'
        choice_b = 'A television transmitter PA*'
        choice_c = 'A low-level microphone preamplifier'
        choice_d = 'The first stage in a radio receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A class-A circuit would not work well as: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Class A'
        choice_b = 'Class AB1'
        choice_c = 'Class AB2'
        choice_d = 'Class B*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which of the following FEt amplifier types does drain current flow for 50 percent of the signal cycle?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Class A*'
        choice_b = 'Class AB1'
        choice_c = 'Class AB2'
        choice_d = 'Class B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following amplifier types produces the least distortion of the signal waveform?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Class A'
        choice_b = 'Class AB1'
        choice_c = 'Class AB2*'
        choice_d = 'Class B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which bipolar amplifier type has some distortion in the signal wave, with collector current during most, but not all, of the cycle? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'By increasing the bias'
        choice_b = 'By using two transistors in push-pull*'
        choice_c = 'By using tuned circuits in the output'
        choice_d = 'A class-B amplifier cannot work well for hi-fi audio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can a class-B amplifier be made suitable for hi-fi audio applications?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'By reducing the bias'
        choice_b = 'By increasing the drive'
        choice_c = 'By using two transistors in push-pull'
        choice_d = 'A class-C amplifier cannot be made linear*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can a class-C amplifier be made linear?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Class A'
        choice_b = 'Class AB1'
        choice_c = 'Class AB2'
        choice_d = 'Class B*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following amplifier classes generally needs the most driving power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Bias control'
        choice_b = 'Gain control'
        choice_c = 'Tone control*'
        choice_d = 'Frequency control'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A graphic equalizer is a form of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'Transformers can\'t match impedances'
        choice_b = 'Transformers can\'t work above audio frequencies'
        choice_c = 'Transformers cost more*'
        choice_d = 'Transformers reduce the gain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A disadvantage of transformer coupling, as opposed to capacitive coupling, is that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_17:
    def __init__(self, *args, **kwargs):
        choice_a = '22 W'
        choice_b = '50 W*'
        choice_c = '2.2 W'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A certain bipolar-transistor PA is 66 percent efficient. The output power is 33 W. The DC collector power input is: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Generally easy to use*'
        choice_b = 'More efficient than a tuned PA'
        choice_c = 'Less likely than a tuned PA to amplify unwanted signals'
        choice_d = 'Usable only at audio frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A broadband PA is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Set to work over a wide range of frequencies'
        choice_b = 'Adjusted for maximum power output*'
        choice_c = 'Made as efficient as possible'
        choice_d = 'Operated in class C'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A tuned PA must always be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_24_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Provides an impedance match between the bipolar transistor or FET and the load*'
        choice_b = 'Allows broadband operation'
        choice_c = 'Adjusts the resonant frequency'
        choice_d = 'Controls the input impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A loading control in a tuned PA"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'Causes oscillation'
        choice_b = 'Increases sensitivity'
        choice_c = 'Reduces the gain*'
        choice_d = 'Is used in an Armstrong oscilltor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Negative feedback in an amplifier: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'A common-drain or common-collector circuit'
        choice_b = 'A stage with gain*'
        choice_c = 'A tapped coil'
        choice_d = 'Negative feedback'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Oscillation requires"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'A split capacitance in tuned circuit*'
        choice_b = 'A tapped coil in the tuned circuit'
        choice_c = 'A transformer for the feedback'
        choice_d = 'A common-base or common-gate arrangement'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Colpitts oscillator can be recognized by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'As great as possible.'
        choice_b = 'Kept to a minimum.'
        choice_c = 'Just enough to sustain oscillation.*'
        choice_d = 'Done through a transformer whose wires can be switched easily.'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an oscillator circuit, the feedback should be: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'Hartley oscillator*'
        choice_b = 'Colpitts oscillator'
        choice_c = 'Armstrong oscillator'
        choice_d = 'Clapp oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A tapped coil is used in a(n)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Passes RF but not dc'
        choice_b = 'Passes both RF and dc'
        choice_c = 'Pasees dc but not RF*'
        choice_d = 'Blocks both dc and RF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An RF choke: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'The inductances are too large'
        choice_b = 'It\'s hard to vary the inductance of such a coil'
        choice_c = 'Such coils are too bulky'
        choice_d = 'Air-core coils have better thermal stability*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Ferromagnetic coil cores are not generally good for use in RF oscillator because"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'Low-power-supply voltage'
        choice_b = 'Low stage gain'
        choice_c = 'In-phase feedback*'
        choice_d = 'Very low output impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An oscillator might fail to start for any of the following reasons EXCEPT"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Single-frequency operation'
        choice_b = 'Ease of frequency adjustment '
        choice_c = 'High output power'
        choice_d = 'Low drift*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An advantage of a crystal-controlled oscillator over a VFO"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'The values of the inductor and capacitor'
        choice_b = 'The thickness of the crystal*'
        choice_c = 'The amount of capacitance across the crystal'
        choice_d = 'The power-supply voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The frequency at which a crystal oscillator functions is determined mainly by: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'Differences in the waveshape*'
        choice_b = 'Differences in frequency'
        choice_c = 'Differences in amplitude'
        choice_d = 'Differences in phase'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The different sounds of musical instruments are primarily the result of: """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'Has an irregular waveshape'
        choice_b = 'Has most or all of its energy at a single frequency*'
        choice_c = 'Produces a sound that depends on its waveform'
        choice_d = 'Uses RC tuning'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A radio frequency oscillator usually"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is mechanically flexible'
        choice_b = 'Has high power output'
        choice_c = 'Can produce different waveforms'
        choice_d = 'Is good for use in frequency synthesizers*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A varactor diode"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'High power output'
        choice_b = 'High drift rate'
        choice_c = 'Exceptional stability*'
        choice_d = 'Adjustable waveshape'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A frequency synthesizer has"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'That must have the best possible stability'
        choice_b = 'That must have high power output'
        choice_c = 'That must work at microwave frequencies'
        choice_d = 'No! Air-core coils work better in RF oscillators*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ferromagnetic-core coil is preferred for use in the tuned circuit of an RF oscillator"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'The frequency might drift'
        choice_b = 'The power output might be reduced'
        choice_c = 'The oscillator might fail to start'
        choice_d = 'It\'s not a cause for worry; it can\'t be too high*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the load impedance for an oscillator is too high"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'Class B'
        choice_b = 'A common-emitter or common-source arrangement*'
        choice_c = 'Class C'
        choice_d = 'A common-collector or common-drain arrangement'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The bipolar transistors or JFETs in a multivibrator are usually connected in :"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'A waveform analyzer*'
        choice_b = 'An audio oscillator'
        choice_c = 'An RF oscillator'
        choice_d = 'A sine-wave generator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The arrangement in the block diagram represents https://lesliecaminadecom.files.wordpress.com/2019/08/2298jasy68alhxfw6zjw.png"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Is useful for generating RF sine waves'
        choice_b = 'Is useful for waveform analysis'
        choice_c = 'Can be used to increase the amplifier gain'
        choice_d = 'Serves no useful purpose*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Acoustic feedback in a public-address system"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class gibilisco_25_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'Makes a good audio oscillator'
        choice_b = 'Can be used for waveform analysis'
        choice_c = 'Is used as a microwave oscillator*'
        choice_d = 'Allows for frequency adjustment of a VCO'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An IMPATT diode"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""







