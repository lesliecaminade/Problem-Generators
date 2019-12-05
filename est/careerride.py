import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

class careerride_1:
    def __init__(self, *args, **kwargs):
        choice_a = '0.0149 m2*'
        choice_b = '0.0475 m2'
        choice_c = '0.5521 m2'
        choice_d = '0.9732 m2'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A rectangular horn antenna operating at 4GHz has the wavelength of 0.075m and gain of about 13dBi. What will be its required capture area?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'Normal*'
        choice_b = 'Axial'
        choice_c = 'Circular'
        choice_d = 'Polar'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which mode of radiation occurs in an helical antenna due to smaller dimensions of helix as compared to a wavelength?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_3:
    def __init__(self, *args, **kwargs):
        choice_a = '2'
        choice_b = '3'
        choice_c = '4*'
        choice_d = '6'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""By how many times is an input impedance of a folded dipole at resonance greater than that of an isolated dipole with same length as one of its sides? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'Inductive'
        choice_b = 'Capacitive'
        choice_c = 'Resistive*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How do the elements of an active region behave? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'lambda/2'
        choice_b = 'lambda*'
        choice_c = 'lambda/10'
        choice_d = 'lambda/50'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an electrically large loop, an overall length of the loop is equal to ______ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'C & D'
        choice_c = 'A & D'
        choice_d = 'B & C'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is /are the advantages of using ferrite loops?
A. Increase in Magnetic field intensity
B. Increase in radiation resistance
C. Decrease in Magnetic field intensity
D. Decrease in radiation resistance """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'Field pattern estimation due to any length of antenna'
        choice_b = 'Improvement in radiation resistance by increasing dipole length'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is/are the major applications of an infinitesimal dipole that contribute/s to its analysis? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_8:
    def __init__(self, *args, **kwargs):
        choice_a = '90 kW'
        choice_b = '135 kW'
        choice_c = '180 kW*'
        choice_d = '200 kW'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A dipole carries r.m.s. current of about 300A across the radiation resistance 2 Ω. What would be the power radiated by an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reciprocity'
        choice_b = 'Superposition*'
        choice_c = 'Causality'
        choice_d = 'Relativity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" If J' & M' are active at the same time, which principle theorem is used for field estimation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'Real fields'
        choice_b = 'Imaginary fields'
        choice_c = 'Complex fields*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The concept of  magnetic vector potential finds its major application in deriving expression of magnetic field intensity especially for ______"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'B\'*'
        choice_b = 'H\''
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the below mentioned magnetic quantities is/are dependent on media/medium? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'e^(-jkr)*'
        choice_b = 'e^(jkr)'
        choice_c = 'e^(-jk/r)'
        choice_d = 'e^(jk+r)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In solution evaluation process of inhomogeneous vector potential wave equation, if points are completely removed from the source, then by which factor does the time varying field & static solution differ? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'Its input impedance during the removal of all other antennas*'
        choice_b = 'Its impedance by taking into consideration the consequences of other antennas'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Self impedance of an antenna is basically __________"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Equality of impedances'
        choice_b = 'Equality of directional patterns'
        choice_c = 'Equality of effective lengths'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which property/ies of antenna is/are likely to be evidenced in accordance to Reciprocity theorem? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Perpendicular'
        choice_b = 'Perfectly aligned*'
        choice_c = 'Angle of inclination'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Under which conditions of two unit vectors, the polarization loss factor (PLF) is equal to unity?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_16:
    def __init__(self, *args, **kwargs):
        choice_a = '22.22 ohms'
        choice_b = '27.77 ohms*'
        choice_c = '33.33 ohms'
        choice_d = '39.77 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an antenna draws 12 A current and radiates 4 kW, then what will be its radiation resistance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'B & C'
        choice_c = 'A & C'
        choice_d = 'B & D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following elucidate the generation of electromagnetic waves?
A. Ampere's law
B. Faraday's law
C. Gauss's law
D. Kirchoff's law """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spherical*'
        choice_b = 'Plane'
        choice_c = 'Triangular'
        choice_d = 'Square'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In radio communication link, what is the shape/nature of waves generated by transmitting antenna? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'Radiator'
        choice_b = 'Converter'
        choice_c = 'Sensor*'
        choice_d = 'Inverter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the functioning role of an antenna in receiving mode?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_20
    def __init__(self, *args, **kwargs):
        choice_a = 'Convergent'
        choice_b = 'Divergent*'
        choice_c = 'Contingent'
        choice_d = 'Congruent'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In lens antenna, what kind of wave energy is transformed into plane waves?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_21:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & C*'
        choice_b = 'B & D'
        choice_c = 'A & D'
        choice_d = 'B & C'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How is the effect of selective fading reduced?
A. By high carrier reception
B. By low carrier reception
C. By single side band system
D. By double side band system"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_22:
    def __init__(self, *args, **kwargs):
        choice_a = 'MUF*'
        choice_b = 'LUF'
        choice_c = 'OWF'
        choice_d = 'UHF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to Secant law, which frequency is greater than critical frequency by a factor of secθi? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_23:
    def __init__(self, *args, **kwargs):
        choice_a = '4 MHz'
        choice_b = '9 MHz'
        choice_c = '18 MHz*'
        choice_d = '25 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" If the maximum electron density for F-layer in ionosphere is 4 x 106 electrons/cm3, then what will be the critical frequency of EM wave for F-layer? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_24:
    def __init__(self, *args, **kwargs):
        choice_a = 'Depression layer'
        choice_b = 'Regression layer'
        choice_c = 'Inversion layer*'
        choice_d = 'Invasion layer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which layer has the atmospheric conditions exactly opposite to that of standard atmosphere?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_25:
    def __init__(self, *args, **kwargs):
        choice_a = 'Horizontal'
        choice_b = 'Vertical*'
        choice_c = 'Diagonal'
        choice_d = 'Opposite'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the direction of varying orientation of polarized surface wave at the earth surface in a wave tilt mechanism? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_26:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'C & D'
        choice_c = 'A & C'
        choice_d = 'B & D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On which factors of earth does the magnitude of tilt angle depend in surface wave?
A. Permittivity
B. Conductivity
C. Resistivity
D. Reflectivity"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_27:
    def __init__(self, *args, **kwargs):
        choice_a = 'Attenuation*'
        choice_b = 'Phase velocity'
        choice_c = 'Propagation constant'
        choice_d = 'Tilt angle'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For avoiding ground losses, better is the surface conductivity, less is the __________"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_28:
    def __init__(self, *args, **kwargs):
        choice_a = 'Curvature of the earth'
        choice_b = 'Roughness of the earth'
        choice_c = 'Magnetic field of the earth'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When an electromagnetic wave travels from transmitter to receiver, which factor/s affect/s the propagation level?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_29:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ex'
        choice_b = 'Ey'
        choice_c = 'Both Ex and Ey in phase*'
        choice_d = 'Both EX and Ey out of phase'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Linear polarization can be obtained only if the wave consists of  ________ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_30:
    def __init__(self, *args, **kwargs):
        choice_a = '17 %'
        choice_b = '27 %'
        choice_c = '37 %*'
        choice_d = '57 %'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to depth of penetration, what is the percentage proportion of attenuated wave w.r.t its original value? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_31:
    def __init__(self, *args, **kwargs):
        choice_a = 'Plane'
        choice_b = 'Elliptical'
        choice_c = 'Circular*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of polarization is provided by helical antennas? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_32:
    def __init__(self, *args, **kwargs):
        choice_a = 'Low radiation resistance'
        choice_b = 'Low radiation efficiency'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why are beverage antennas not used as transmitting antenna? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_33:
    def __init__(self, *args, **kwargs):
        choice_a = 'Requirement of a large space'
        choice_b = 'Reduced transmission effieciency'
        choice_c = 'Maximum radiated power along main axis*'
        choice_d = 'Wastage of power in terminating resistor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following is not a disadvantage of rhombic antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_34:
    def __init__(self, *args, **kwargs):
        choice_a = 'Apex angle'
        choice_b = 'Tilt angle*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which angle of rhombic antenna represents one half of included angle of two legs of one wire?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_35:
    def __init__(self, *args, **kwargs):
        choice_a = 'Transmission line region'
        choice_b = 'Active region'
        choice_c = 'Reflective region*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the length of elements of an array is greater than λ/2, which will be the operating region of an array?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_36:
    def __init__(self, *args, **kwargs):
        choice_a = 'Widest'
        choice_b = 'Narrowest*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" What kind of beamwidth is/are produced by Chebyshev arrays for given side lobe level (SLL)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_37:
    def __init__(self, *args, **kwargs):
        choice_a = '2'
        choice_b = '4'
        choice_c = '8*'
        choice_d = '16'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the elements of a binomial array are separated by λ/4, how many shape patterns are generated with no minor lobes?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_38:
    def __init__(self, *args, **kwargs):
        choice_a = '6.53 dB*'
        choice_b = '7.99 dB'
        choice_c = '8.55 dB'
        choice_d = '9.02 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a linear uniform array consists of 9 isotropic elements separated by λ/4, what would be the directivity of a broadside array in dB? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_39:
    def __init__(self, *args, **kwargs):
        choice_a = 'Wave is incident in direction of plane of the loop with induced maximum voltage'
        choice_b = 'Wave is incident normal to plane of the loop with no induced voltage*'
        choice_c = 'Wave is incident in opposite direction of plane of the loop with minimum voltage'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What would happen if the rms value of induced emf in loop acquires an angle θ = 90°? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_40:
    def __init__(self, *args, **kwargs):
        choice_a = 'Along x-axis'
        choice_b = 'Along y-axis'
        choice_c = 'Along z-axis*'
        choice_d = 'Along the xy plane'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the far-field position of an electric short dipole?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_41:
    def __init__(self, *args, **kwargs):
        choice_a = '0.7883 ohms'
        choice_b = '50.45 ohms'
        choice_c = '123.17 ohms*'
        choice_d = '190.01 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the radius of loop is λ/ 20 in a free space medium,what will be the radiation resistance of 8-turn small circular loop? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_42:
    def __init__(self, *args, **kwargs):
        choice_a = 'Capacitor*'
        choice_b = 'Inductor'
        choice_c = 'Resistor'
        choice_d = 'Gyrator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For receiving a particular frequency signal, which tuning component must be used by the loop to form a resonant circuit for tuning to that frequency? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_43:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spherical'
        choice_b = 'Rectangular'
        choice_c = 'Triangular*'
        choice_d = 'Square'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the nature of current distribution over the small dipoles? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_44:
    def __init__(self, *args, **kwargs):
        choice_a = '1/r'
        choice_b = '1/r^2*'
        choice_c = '1/r^3'
        choice_d = '1/r^4'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which term is regarded as an inductive field as it is predictable from Biot Savart law & considered to be of prime importance at near field or the distance close to current element?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_45:
    def __init__(self, *args, **kwargs):
        choice_a = 'Initial'
        choice_b = 'Eventual'
        choice_c = 'Mid*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Dipole antenna is symmetrical in nature where the two ends are at equal potentials with respect to _____point """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_46:
    def __init__(self, *args, **kwargs):
        choice_a = '0.032 m^2*'
        choice_b = '0.047 m^2'
        choice_c = '0.65 m^2'
        choice_d = '0.99 m^2'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a half-wave dipole operates at 300 MHz with λ = 0.5m & D0 = 1.643, what will be its effective area? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_47:
    def __init__(self, *args, **kwargs):
        choice_a = 'Inward'
        choice_b = 'Outward*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the solutions of inhomogeneous vector potential wave equation, which component exists if the source is at origin and the points are removed from the source (Jz = 0)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_48:
    def __init__(self, *args, **kwargs):
        choice_a = 'R + c'
        choice_b = 'R - c'
        choice_c = 'R/c*'
        choice_d = 'Rc'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In retarded potentials, what factor of time delay is generally introduced in A' & V' equations? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_49:
    def __init__(self, *args, **kwargs):
        choice_a = 'Source'
        choice_b = 'Distance of point from the source'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The vector magnetic potential shows the inverse relationship with its ____ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_50:
    def __init__(self, *args, **kwargs):
        choice_a = 'pi/2'
        choice_b = 'pi'
        choice_c = '2pi'
        choice_d = '4pi*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to the geometry, how many sterdians are present in a full sphere?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_51:
    def __init__(self, *args, **kwargs):
        choice_a = 'Point angle'
        choice_b = 'Linear angle'
        choice_c = 'Plane angle'
        choice_d = 'Solid angle*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Steradian is a measurement unit of __________ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_52:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reactive near-field region'
        choice_b = 'Fresnel region'
        choice_c = 'Fraunhoffer region*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which antenna radiating region/s has/have independent nature of angular field distribution over the distance from the antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_53:
    def __init__(self, *args, **kwargs):
        choice_a = 'Plane to spherical wave'
        choice_b = 'Spherical to plane wave*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which conversion mechanism is performed by parabolic reflector antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_54:
    def __init__(self, *args, **kwargs):
        choice_a = 'Aperture'
        choice_b = 'Microstrip*'
        choice_c = 'Array'
        choice_d = 'Lens'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which antennas are renowned as patch antennas especially adopted for space craft applications?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class careerride_55:
    def __init__(self, *args, **kwargs):
        choice_a = 'Linear*'
        choice_b = 'Loop '
        choice_c = 'Helical'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of wire antennas are also known as dipoles?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_56:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ions'
        choice_b = 'Motion of electrons*'
        choice_c = 'Neutral molecules'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following plays a primary role in generation of conduction current in an ionosphere due to presence of electric field? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_57:
    def __init__(self, *args, **kwargs):
        choice_a = 'Only reflection'
        choice_b = 'Only refraction'
        choice_c = 'Partial reflection and refraction*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which mechanism/s is/are likely to occur in mid-frequency operation corresponding to ionospheric region?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_58:
    def __init__(self, *args, **kwargs):
        choice_a = 'Towards'
        choice_b = 'Away*'
        choice_c = 'Across'
        choice_d = 'Beside'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to Snell's law in optics, if a ray travels from dense media to rarer media, what would be its direction w.r.t the normal? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_59:
    def __init__(self, *args, **kwargs):
        choice_a = 'Sea wave propagation'
        choice_b = 'Ground wave propagation'
        choice_c = 'Sky wave propagation*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""By which name/s is an ionospheric propagation, also known as? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_60:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reflection or scattering'
        choice_b = 'Refraction'
        choice_c = 'Defraction'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""After which phenomenon/phenomena do the waves arrive at the receiving antenna in ionospheric propagation? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_61:
    def __init__(self, *args, **kwargs):
        choice_a = 'Surface wave'
        choice_b = 'Space wave*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of ground wave travels over the earth surface by acquiring direct path  through air from transmitting to receiving antennas?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_62:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reactive'
        choice_b = 'Resistive*'
        choice_c = 'Capacitive'
        choice_d = 'Inductive'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an electrical circuit,which nature of impedance causes the current & voltages in phase? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_63:
    def __init__(self, *args, **kwargs):
        choice_a = '1.047e6 m/s*'
        choice_b = '1.257e6 m/s'
        choice_c = '2.50e6 m/s'
        choice_d = '3e6 m/s'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the magnetic field component of a plane wave in a lossless dielectric is H = 50 sin (2π x 106 t – 6x) az  mA/m , what will be the wave velocity?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_64:
    def __init__(self, *args, **kwargs):
        choice_a = 'Maxwell\'s'
        choice_b = 'Lorentz'
        choice_c = 'Helmholtz'
        choice_d = 'Poisson\'s'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which equations are regarded as wave equations in frequency domain for lossless media?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_65:
    def __init__(self, *args, **kwargs):
        choice_a = 'Electric field'
        choice_b = 'Magnetic field'
        choice_c = 'Direction of propagation'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following exhibits perpendicular nature in TEM wave?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_66:
    def __init__(self, *args, **kwargs):
        choice_a = 'Power delivered to antenna'
        choice_b = 'Power factor of impedance'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In ungrounded antennas, if an excitation is applied directly across the base insulator, then on which factor/s would the voltage across the insulator depend? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_67:
    def __init__(self, *args, **kwargs):
        choice_a = 'Series*'
        choice_b = 'Shunt'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the tower antenna is not grounded, which method of excitation is/are applicable for it? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_68:
    def __init__(self, *args, **kwargs):
        choice_a = 'VHF'
        choice_b = 'SHF'
        choice_c = 'UHF'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For which band/s is the space wave propagation suitable over 30 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_69:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ionospheric*'
        choice_b = 'Ground wave'
        choice_c = 'Tropospheric'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which mode of propagation is adopted in HF antennas? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_70:
    def __init__(self, *args, **kwargs):
        choice_a = 'alpha < beta x d'
        choice_b = 'alpha > beta x d'
        choice_c = 'alpha = (+/-) beta x d*'
        choice_d = 'alpha =/= (+/-) beta x d'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following is regarded as a condition of an ordinary endfire array? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_71:
    def __init__(self, *args, **kwargs):
        choice_a = 'Phase*'
        choice_b = 'Frequency'
        choice_c = 'Current'
        choice_d = 'Voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In broadside array, all the elements in the array should have similar _______excitation along with similar amplitude excitation for maximum radiation."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_72:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spherical*'
        choice_b = 'Doughnut'
        choice_c = 'Elliptical'
        choice_d = 'Hyperbolic'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the nature of radiation pattern of an isotropic antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_73:
    def __init__(self, *args, **kwargs):
        choice_a = 'Linear'
        choice_b = 'Plane'
        choice_c = 'Conformal*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which kind of array configuration, the element locations must deviate or adjust to some nonplaner surface like an aircraft or missile?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_74:
    def __init__(self, *args, **kwargs):
        choice_a = '0 degrees'
        choice_b = '90 degrees*'
        choice_c = '180 degrees'
        choice_d = '270 degrees'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to the directivity of a small loop, which value of 'θ' contributes to achieve the maximum value of radiation intensity (Umax)? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_75:
    def __init__(self, *args, **kwargs):
        choice_a = 'Poor*'
        choice_b = 'Good'
        choice_c = 'Better'
        choice_d = 'Excellent'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" From the radiation point of view, small loops are _________radiators"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_76:
    def __init__(self, *args, **kwargs):
        choice_a = 'Shape'
        choice_b = 'Area*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" On which factor/s do/does the radiation field of a small loop depend? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_77:
    def __init__(self, *args, **kwargs):
        choice_a = 'Less than*'
        choice_b = 'Equal to'
        choice_c = 'Greater than'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an electrically small loops, the overall length of the loop is ______ one-tenth of a wavelength."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_78:
    def __init__(self, *args, **kwargs):
        choice_a = 'Field pattern'
        choice_b = 'Voltage pattern'
        choice_c = 'Power pattern*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" Which pattern is generated due to plotting of square of amplitude of an electric field? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_79:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increase*'
        choice_b = 'Decrease'
        choice_c = 'Stability'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In flared transmission line, the radiation phenomenon increases due to ________ in flaring"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_80:
    def __init__(self, *args, **kwargs):
        choice_a = 'length <= (lambda/50)*'
        choice_b = '(lambda/50) < length <= (lambda/10)'
        choice_c = 'length = lambda/2'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How are the infinitesimal dipoles represented in terms of antenna length and signal wavelength? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_81:
    def __init__(self, *args, **kwargs):
        choice_a = 'Current*'
        choice_b = 'Voltage'
        choice_c = 'Frequency'
        choice_d = 'Phase'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which waveform plays a crucial role in determining the radiation pattern of the dipole/wire antennas?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_82:
    def __init__(self, *args, **kwargs):
        choice_a = 'Addition'
        choice_b = 'Subtraction'
        choice_c = 'Differentiation*'
        choice_d = 'Integration'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which operations are performed by vector potentials (A, F) over the radiated fields  (E & H)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_83:
    def __init__(self, *args, **kwargs):
        choice_a = 'Scalar potentials'
        choice_b = 'Vector potentials*'
        choice_c = 'Gradient potentials'
        choice_d = 'Divergence potentials'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which auxiliary functions assist in solving the radiation problem by evaluation of E & H using sources J & M?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_84:
    def __init__(self, *args, **kwargs):
        choice_a = 'Induced*'
        choice_b = 'Radiated'
        choice_c = 'Reflected'
        choice_d = 'Far-field'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an observation point is closely located to the source, then the field is termed as ________ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_85:
    def __init__(self, *args, **kwargs):
        choice_a = 'Half power beamwidth'
        choice_b = 'First null beamwidth*'
        choice_c = 'Side lobe level'
        choice_d = 'Front to back ratio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following defines the angular distance between two points on each side of major lobe especially when the radiation drops to zero?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_86:
    def __init__(self, *args, **kwargs):
        choice_a = '0 and 180 degrees*'
        choice_b = '90 and 180 degrees'
        choice_c = '180 and 270 degrees'
        choice_d = '180 and 360 degrees'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At which angles does the front to back ratio specify an antenna gain? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_87:
    def __init__(self, *args, **kwargs):
        choice_a = 'Minor lobe'
        choice_b = 'Side lobe'
        choice_c = 'Back lobe*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a non-isotropic directional antenna, which radiating lobe axis makes an angle of 180° w.r.t. major beam of an antenna? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_88:
    def __init__(self, *args, **kwargs):
        choice_a = 'For a charge with no motion'
        choice_b = 'For a charge moving with uniform velocity with straight and infinite wire'
        choice_c = 'For a charge oscillating in time motion*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" Under which conditions of charge does the radiation occur through wire antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_89:
    def __init__(self, *args, **kwargs):
        choice_a = 'Impedance matching device'
        choice_b = 'Sensor of electromagnetic waves'
        choice_c = 'Transducer between guided wave and free space wave'
        choice_d = 'Metallic device for radiating of receiving radio waves*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" According to Webster's dictionary, what is an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_90:
    def __init__(self, *args, **kwargs):
        choice_a = 'Electric field intensity'
        choice_b = 'Magnetic field intensity'
        choice_c = 'Current density*'
        choice_d = 'Power density'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The knowledge of which parameter is sufficient for deriving the time varying electromagnetic field?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_91:
    def __init__(self, *args, **kwargs):
        choice_a = 'Low'
        choice_b = 'Moderate'
        choice_c = 'High*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""F2 layer of appleton region acts as a significant reflecting medium for _____ frequency radio waves """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_92:
    def __init__(self, *args, **kwargs):
        choice_a = '20 km to 50 km'
        choice_b = '45 km to 85 km'
        choice_c = '90 km to 130 km*'
        choice_d = '140 km to 200 km'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the possible range of height for the occurrence of sporadic E-region with respect to normal E-region?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_93:
    def __init__(self, *args, **kwargs):
        choice_a = 'D-region*'
        choice_b = 'Normal E-region'
        choice_c = 'Sporadic E-region'
        choice_d = 'Appleton region'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which ionization layer exists during day time & usually vanishes at night due to highest recombination rate? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_94:
    def __init__(self, *args, **kwargs):
        choice_a = 'beta x (lambda/2)*'
        choice_b = 'beta / (lambda/2)'
        choice_c = 'beta + (lambda/2)'
        choice_d = 'beta - (lambda/2)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the path difference of two waves with single source traveling by different paths to arrive at the same point, is λ/2, what would be the phase difference between them?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_95:
    def __init__(self, *args, **kwargs):
        choice_a = 'Reflected'
        choice_b = 'Refracted'
        choice_c = 'Radiated*'
        choice_d = 'Diffracted'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Power density is basically termed as ________ power per unit are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_96:
    def __init__(self, *args, **kwargs):
        choice_a = 'Solid bodies'
        choice_b = 'Ionized particles'
        choice_c = 'Interference of normal radiation and radio wave propagation'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following is/are not present in free space?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_97:
    def __init__(self, *args, **kwargs):
        choice_a = 'Sinusoidal*'
        choice_b = 'Rectangular'
        choice_c = 'Square'
        choice_d = 'Triangular'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which kind of waveform is the phase velocity defined?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_98:
    def __init__(self, *args, **kwargs):
        choice_a = 'Phase*'
        choice_b = 'Frequency'
        choice_c = 'Amplitude'
        choice_d = 'Wave equation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Wavefront is basically a locus of points acquiring similar _______ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_99:
    def __init__(self, *args, **kwargs):
        choice_a = 'SONAR'
        choice_b = 'Subsurface communication'
        choice_c = 'Radio navigation'
        choice_d = 'Facsimile*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following is an application of high frequency? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_100:
    def __init__(self, *args, **kwargs):
        choice_a = '1 m to 10 m'
        choice_b = '1 cm to 10 cm*'
        choice_c = '10 cm to 1 m'
        choice_d = '0.1 cm to 1 cm'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the wavelength of Super high frequency (SHF) especially used in Radar & satellite communication? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_101:
    def __init__(self, *args, **kwargs):
        choice_a = 'Power efficiency'
        choice_b = 'Spectral efficiency*'
        choice_c = 'Transmission efficiency'
        choice_d = 'Modulation efficiency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For fixed symbol rate, increase in bits/symbol ultimately improves rb/B bits/s/Hz & hence, regarded as _____. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_102:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'C & D'
        choice_c = 'A & C'
        choice_d = 'B & D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For designing a communication system, which among the following parameters should be maximum?
A. Transmission rate
B. Received signal-to-noise ratio
C. Error probability
D. Bandwidth requirement """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_103:
    def __init__(self, *args, **kwargs):
        choice_a = 'Euclidean distance between code vectors*'
        choice_b = 'Hamming distance of error correcting codes'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For designing trellis code, the emphasis must be on maximizing __________ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_104:
    def __init__(self, *args, **kwargs):
        choice_a = 'smallest*'
        choice_b = 'largest'
        choice_c = 'average'
        choice_d = 'constant'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""d_free is defined as the Euclidean distance of coded signal in terms of _________ possible distance between all allowed sequences."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_105:
    def __init__(self, *args, **kwargs):
        choice_a = 'Euclidean distance'
        choice_b = 'Distance between sequences*'
        choice_c = 'Manmattan distance'
        choice_d = 'Hamming distance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The distance between each symbol in given sequence and reference sequence is known as _______."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_106:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'B & C'
        choice_c = 'A & C'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To obtain the transfer function of a convolutional code, the splitting of all-zero state takes place into ___
A. starting state
B. first return to all-zero state
C. in-between state"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_107:
    def __init__(self, *args, **kwargs):
        choice_a = 'Soft decision decoding*'
        choice_b = 'Hard decision decoding'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a received sequence of 6 bits, which decoding mechanism deals with the selection of best correlated sequence especially by correlating the received sequence and all permissible sequences?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_108:
    def __init__(self, *args, **kwargs):
        choice_a = 'Maximum likelihood decoding'
        choice_b = 'Sequential decoding*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which decoding method involves the evaluation by means of Fano Algorithm?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_109:
    def __init__(self, *args, **kwargs):
        choice_a = '0 input*'
        choice_b = '1 input'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For the 4 states of an encoder on vertical axis of Trellis diagram, what do/does the solid line indicate/s?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_110:
    def __init__(self, *args, **kwargs):
        choice_a = 'Continuous time'
        choice_b = 'Discrete time*'
        choice_c = 'Sampled time'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Trellis diagram, what do/does the horizontal axis represent/s? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_111:
    def __init__(self, *args, **kwargs):
        choice_a = 'Information bits'
        choice_b = 'Symbol bits'
        choice_c = 'Parity check bits*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Minimum Distance Separable (MDS) codes, the minimum distance is one more than the number of _________. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_112:
    def __init__(self, *args, **kwargs):
        choice_a = 'One*'
        choice_b = 'Two'
        choice_c = 'Three'
        choice_d = 'Infinite'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" In RS code, the length is ____less than number of symbols in symbol set (q)."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_113:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'C & D'
        choice_c = 'A & C'
        choice_d = 'B & D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Decoding of RS code comprises the determination of error _______
A. position
B. magnitude
C. angle
D. frequency"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_114:
    def __init__(self, *args, **kwargs):
        choice_a = 'CRC-12*'
        choice_b = 'CRC-16'
        choice_c = 'CRC-32'
        choice_d = 'CRC-CCITT'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Frame Check Sequence (FCS), which code is used if character length is 6 bit and generates 12 bit parity check bits? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_115:
    def __init__(self, *args, **kwargs):
        choice_a = 'Transmitter'
        choice_b = 'Receiver*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the errors are corrected at _______end/s, it is known as 'Forward Error Correction' (FEC). """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_116:
    def __init__(self, *args, **kwargs):
        choice_a = 'Input*'
        choice_b = 'Output'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In register contents at decoder, the syndrome register consists of syndrome after all bits of received vector are clocked into the decoder ________. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_117:
    def __init__(self, *args, **kwargs):
        choice_a = 'LRC'
        choice_b = 'VRC*'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following error detecting technique is supposed to be parity bit associated with character code? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_118:
    def __init__(self, *args, **kwargs):
        choice_a = 'A & B*'
        choice_b = 'C & D'
        choice_c = 'A & C'
        choice_d = 'B & D'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the below stated logical circuits are present in encoder and decoder used for the implementation of cyclic codes?
A. Shift Registers
B. Modulo-2 Adders
C. Counters
D. Multiplexers"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_119:
    def __init__(self, *args, **kwargs):
        choice_a = 'ABCD'
        choice_b = 'BADC'
        choice_c = 'CBDA'
        choice_d = 'DACB*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Consider the assertions related to decoding process of cyclic code. Which among the following is a correct sequence of steps necessary for the correction of errors?
A. Syndrome determination after the division of r(x) & g(x) 
B. Addition of error pattern to received code word
C. Selection of error pattern corresponding to the syndrome
D. Preparation of table comprising error patterns and syndromes """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_120:
    def __init__(self, *args, **kwargs):
        choice_a = 'x^n + 1'
        choice_b = 'x^n - 1'
        choice_c = 'x^n / 2'
        choice_d = 'x^(2n/3)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For the generation of a cyclic code, the generator polynomial should be the factor of _____ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_121:
    def __init__(self, *args, **kwargs):
        choice_a = 'Small'
        choice_b = 'Medium'
        choice_c = 'Large*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which buffer size is required by the interleaved codes at the transmitter for the accumulation of λ code words?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_122:
    def __init__(self, *args, **kwargs):
        choice_a = 'Number of error vectors'
        choice_b = 'Error probability of symbol transmission'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On which factor/s do/does the error probability depend/s after decoding?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_123:
    def __init__(self, *args, **kwargs):
        choice_a = 'One*'
        choice_b = 'Two'
        choice_c = 'Four'
        choice_d = 'Eight'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Repetition Code, how many information bit/s is/are present in addition to n-1 parity bits?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_124:
    def __init__(self, *args, **kwargs):
        choice_a = '0'
        choice_b = '1*'
        choice_c = '2'
        choice_d = '3'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a (6,4) block code where n = 6, k = 4 and dmin = 3, how many errors can be corrected by this code? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_125:
    def __init__(self, *args, **kwargs):
        choice_a = 'Hamming codes'
        choice_b = 'Interleaved code'
        choice_c = 'Repetition codes'
        choice_d = 'Golay code*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which amount the following is capable of correcting any combination of three or fewer errors random errors in a block of 23 bits?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_126:
    def __init__(self, *args, **kwargs):
        choice_a = 'Bandwidth'
        choice_b = 'Signal to noise ratio'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On which factor/s do/does the channel capacity depend/s in the communication system? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_127:
    def __init__(self, *args, **kwargs):
        choice_a = '16 Mbps'
        choice_b = '24 Mbps'
        choice_c = '48 Mbps*'
        choice_d = '64 Mbps'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Assuming that the channel is noiseless, if TV channels are 8 kHz wide with the bits/sample = 3Hz and signalling rate = 16 x 106 samples/second, then what would be the value of data rate?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_128:
    def __init__(self, *args, **kwargs):
        choice_a = '250 samples/second'
        choice_b = '500 samples/second'
        choice_c = '800 samples/second'
        choice_d = '1000 samples/seconde'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a noiseless channel bandlimited to 5 kHz is sampled every 1msec, what will be the value of sampling frequency? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_129:
    def __init__(self, *args, **kwargs):
        choice_a = 'Inside the sphere*'
        choice_b = 'Outside the sphere'
        choice_c = 'On the boundary (circumference) of the sphere'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In sphere packing, where is the received code vector with added noise located? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_130:
    def __init__(self, *args, **kwargs):
        choice_a = 'Line packing'
        choice_b = 'Volume packing'
        choice_c = 'Sphere packing*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which approach plays a cardinal role in supporting the results obtained regarding the information capacity theorem?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_131:
    def __init__(self, *args, **kwargs):
        choice_a = 'Second*'
        choice_b = 'Minute'
        choice_c = 'Hour'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Information rate basically gives an idea about the generated information per _____ by source."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_132:
    def __init__(self, *args, **kwargs):
        choice_a = 'Information rate'
        choice_b = 'Noiseless channel'
        choice_c = 'Channel coding theorem'
        choice_d = 'Kraft inequality*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following is used to construct the binary code that satisfies the prefix condition?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_133:
    def __init__(self, *args, **kwargs):
        choice_a = 'Lempel Ziv*'
        choice_b = 'Huffman'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which coding technique/s exhibit/s the usability of fixed length codes?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_134:
    def __init__(self, *args, **kwargs):
        choice_a = 'Silence compression'
        choice_b = 'Linear Predictive Coding'
        choice_c = 'Adaptive Differential Pulse Code Modulation*'
        choice_d = 'Code Excite Linear Predictor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which lossy method for audio compression is responsible for encoding the difference between two consecutive samples? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_135:
    def __init__(self, *args, **kwargs):
        choice_a = 'JPEG*'
        choice_b = 'H.263'
        choice_c = 'MPEG'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following compression techniques is/are intended for still images?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_136:
    def __init__(self, *args, **kwargs):
        choice_a = 'Expansion*'
        choice_b = 'Compression'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In coding gain & bandwidth of TCM, if the signal energy is kept constant, the ________of constellation reduces the noise margin and results into the degradation of performance. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_137:
    def __init__(self, *args, **kwargs):
        choice_a = 'Power efficient modulation'
        choice_b = 'Bandwidth efficient modulation'
        choice_c = 'Error control coding*'
        choice_d = 'Trellis coded modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In digital communication system, if both power and bandwidth are limited, then which mechanism/choice is preferred?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_138:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increased*'
        choice_b = 'Constant'
        choice_c = 'Decreased'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""With respect to power-bandwidth trade-off, for reducing the transmit power requirement, the bandwidth needs to be ________. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_139:
    def __init__(self, *args, **kwargs):
        choice_a = '12000 bits/sec'
        choice_b = '14400 bits/sec*'
        choice_c = '28000 bits/sec'
        choice_d = '32500 bits/sec'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a Gaussian channel of 1 MHz bandwidth with the signal power to noise spectral density ratio of about 104 Hz, what would be the maximum information rate?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_140:
    def __init__(self, *args, **kwargs):
        choice_a = 'rs/2Hz'
        choice_b = 'rs/4Hz*'
        choice_c = 'rs/8Hz'
        choice_d = 'rs/16Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a baseband system with transmission rate 'rs' symbols/sec, what would be the required bandwidth?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_141:
    def __init__(self, *args, **kwargs):
        choice_a = 'survivors*'
        choice_b = 'defenders'
        choice_c = 'destroyers'
        choice_d = 'carriers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Viterbi's algorithm, the selected paths are regarded as __________ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_142:
    def __init__(self, *args, **kwargs):
        choice_a = 'Hamming distance*'
        choice_b = 'Galois field'
        choice_c = 'Hamming bound'
        choice_d = 'Parity-check'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Viterbi's algorithm, which metric is adopted for decision making? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_143:
    def __init__(self, *args, **kwargs):
        choice_a = 'By lines*'
        choice_b = 'By circles'
        choice_c = 'By summers'
        choice_d = 'By squares'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""During the shifting of bits in an encoder, how are the transitions in the states represented?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_144:
    def __init__(self, *args, **kwargs):
        choice_a = 'Coded bits'
        choice_b = 'Message bits'
        choice_c = 'Memory order*'
        choice_d = 'All of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""While representing the convolutional code by (n,k,m), what does 'm' signify or represent in it?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_145:
    def __init__(self, *args, **kwargs):
        choice_a = 'Past input'
        choice_b = 'Present input'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At any given time, the output of an encoder depends on ______ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_146:
    def __init__(self, *args, **kwargs):
        choice_a = 'Go-back-N ARQ'
        choice_b = 'Selective repeat ARQ'
        choice_c = 'Stop-and-wait ARQ*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of ARQ system introduces the transmission delay between the transmitter and receiver before the reception of frame at receiver for the purpose of error detection?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_147:
    def __init__(self, *args, **kwargs):
        choice_a = 'largest'
        choice_b = 'constant'
        choice_c = 'smallest*'
        choice_d = 'unpredictable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In minimal polynomial, _______degree polynomial is present with coefficients in the basefield along with the zeros in extension field. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_148:
    def __init__(self, *args, **kwargs):
        choice_a = '2^m - 1*'
        choice_b = 'm/n - 1'
        choice_c = '(m+1) / 2'
        choice_d = 'm - n - 1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Generally, a primitive polynomial of degree 'm' is an irreducible polynomial in such a way that it is a factor of xn + 1, where 'n' = ______ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_149:
    def __init__(self, *args, **kwargs):
        choice_a = 'Alphabet size'
        choice_b = 'Block length'
        choice_c = 'Code rates'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""BCH codes exhibit the multiple error correcting capability with the provision of selecting _________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_150:
    def __init__(self, *args, **kwargs):
        choice_a = 'm + tc'
        choice_b = 'm - tc'
        choice_c = 'mtc'
        choice_d = 'm/tc'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For (n,k) binary BCH code, how are the parity check bits (n – k) specified?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_151:
    def __init__(self, *args, **kwargs):
        choice_a = '1'
        choice_b = '3*'
        choice_c = '4'
        choice_d = '5'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For designing of (4,1) cyclic repetition code, what would be the order of the generator polynomial g(x)? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_152:
    def __init__(self, *args, **kwargs):
        choice_a = 'Generator Polynomial'
        choice_b = 'Received code word polynomial'
        choice_c = 'Quotient polynomial'
        choice_d = 'Remainder polynomial*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In decoding of cyclic code, which among the following is also regarded as 'Syndrome Polynomial'? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_153:
    def __init__(self, *args, **kwargs):
        choice_a = 'Zero*'
        choice_b = 'Unity'
        choice_c = 'Infinity'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""While decoding the cyclic code, if the received code word is similar as transmitted code word, then r(x) mod g(x) is equal to _________ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_154:
    def __init__(self, *args, **kwargs):
        choice_a = '0.5'
        choice_b = '1*'
        choice_c = '4'
        choice_d = '16'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the value of leading coefficient of a monic polynomial?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_155:
    def __init__(self, *args, **kwargs):
        choice_a = 'sum*'
        choice_b = 'difference'
        choice_c = 'product'
        choice_d = 'division'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to linearity property, the ________ of two code words in a cyclic code is also a valid code word. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_156:
    def __init__(self, *args, **kwargs):
        choice_a = 'sum*'
        choice_b = 'difference'
        choice_c = 'product'
        choice_d = 'division'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The minimum distance of linear block code (dmin) is equal to minimum number of rows or columns of HT, whose  _____ is equal to zero vector."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_157:
    def __init__(self, *args, **kwargs):
        choice_a = 'Finite*'
        choice_b = 'Infinite'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Basically, Galois field consists of ______ number of elements"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_158:
    def __init__(self, *args, **kwargs):
        choice_a = 'Less than'
        choice_b = 'Greater than'
        choice_c = 'Equal to*'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a linear code, the minimum Hamming distance between any two code words is ______minimum weight of any non-zero code word. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_159:
    def __init__(self, *args, **kwargs):
        choice_a = 'Block Codes'
        choice_b = 'Systematic Codes*'
        choice_c = 'Code rate'
        choice_d = 'Hamming distance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following represents the code in which codewords consists of message bits and parity bits separately?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_160:
    def __init__(self, *args, **kwargs):
        choice_a = 'Faster coding and decoding methods'
        choice_b = 'Better error correcting capability'
        choice_c = 'Maximum transfer of information in bits/sec'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which among the following is/are the essential condition/s for a good error control coding technique?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerrider_161:
    def __init__(self, *args, **kwargs):
        choice_a = 'small*'
        choice_b = 'large'
        choice_c = 'stable'
        choice_d = 'unpredictable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""According to Shannon's second theorem, it is not feasible to transmit information over the channel with ______error probability, although by using any coding technique. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_162:
    def __init__(self, *args, **kwargs):
        choice_a = '15.15 kbps'
        choice_b = '24.74 kbps'
        choice_c = '30.12 kbps'
        choice_d = '52.18 kbps'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the channel is bandlimited to 6 kHz & signal to noise ratio is 16, what would be the capacity of channel? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_163:
    def __init__(self, *args, **kwargs):
        choice_a = 'Maximum*'
        choice_b = 'Minimum'
        choice_c = 'Constant'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In channel coding theorem, channel capacity decides the _________permissible rate at which error free transmission is possible. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_164:
    def __init__(self, *args, **kwargs):
        choice_a = 'less'
        choice_b = 'more*'
        choice_c = 'equal'
        choice_d = 'unpredictable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In digital communication system, smaller the code rate, _________are the redundant bits."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_165:
    def __init__(self, *args, **kwargs):
        choice_a = 'noiseless channel'
        choice_b = 'lossless channel'
        choice_c = 'useless channel*'
        choice_d = 'deterministic channel'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of channel does not represent any correlation between input and output symbols? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_166:
    def __init__(self, *args, **kwargs):
        choice_a = 'Static dictionary*'
        choice_b = 'Adaptive dictionary'
        choice_c = 'Both of the valid choices'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In dictionary techniques for data compaction, which approach of building dictionary is used for the prior knowledge of probability of the frequently occurring patterns?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_167:
    def __init__(self, *args, **kwargs):
        choice_a = 'TIFF'
        choice_b = 'BMP'
        choice_c = 'PCX'
        choice_d = 'All of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which bitmap file format/s support/s the Run Length Encoding (RLE)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_168:
    def __init__(self, *args, **kwargs):
        choice_a = 'Maximum'
        choice_b = 'Constant'
        choice_c = 'Minimum*'
        choice_d = 'Unpredictable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Huffman coding technique is adopted for constructing the source code with ________ redundancy. """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_169:
    def __init__(self, *args, **kwargs):
        choice_a = 'Enciphering'
        choice_b = 'Deciphering*'
        choice_c = 'Codeword'
        choice_d = 'Codebook'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which coding terminology deals with the inverse operation of assigned words of second language corresponding to the words in the first language?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class careerride_170:
    def __init__(self, *args, **kwargs):
        choice_a = 'Past output'
        choice_b = 'Future output'
        choice_c = 'Both of the valid choices*'
        choice_d = 'None of the valid choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In discrete memoryless source, the current letter produced by a source is statistically independent of _____ """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

