import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

class kennedy_1:
    def __init__(self, *args, **kwargs):
        choice_a = 'at the transmitter'
        choice_b = 'at the channel*'
        choice_c = 'at the information source'
        choice_d = 'at the destination'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a communications system, noise is most likely to affect the signal"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_2:
    def __init__(self, *args, **kwargs):
        choice_a = 'fundamental and subharmonic sine waves*'
        choice_b = 'a fundamental sine wave and an infinite number of harmonics'
        choice_c = 'fundamental and harmonic sine waves whose amplitude decreases with the harmonic number'
        choice_d = 'sinusoidal voltages, some of which are small enough to ignore in practice'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: Fourier analysis shows that a sawtooth wave consists of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_3:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduce the bandwidth used*'
        choice_b = 'separate differing transmissions'
        choice_c = 'ensure that intelligence may be transmitted over long distances'
        choice_d = 'allow the use of practicable antennas'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: Modulation is used to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_4:
    def __init__(self, *args, **kwargs):
        choice_a = 'unwanted energy'
        choice_b = 'predictable in character*'
        choice_c = 'present in the transmitter'
        choice_d = 'due to any cause'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: From the transmitter the signal deterioration because of noise is usually"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_5:
    def __init__(self, *args, **kwargs):
        choice_a = 'amplitude-modulated group'
        choice_b = 'frequency-modulated group'
        choice_c = 'superheterodyne group*'
        choice_d = 'tuned radio frequency receiver group'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the true statement: Most receivers conforms to the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_6:
    def __init__(self, *args, **kwargs):
        choice_a = 'Antenna heights will be approximately lambda/4 long*'
        choice_b = 'An antenna in the standard broadcast AM band is 16,000 feet'
        choice_c = 'All sound is concentrated from 20 Hz to 20 kHz'
        choice_d = 'A message is composed of unpredictable variations in both amplitude and frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: The need for modulation can be best exemplified by the following."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_7:
    def __init__(self, *args, **kwargs):
        choice_a = 'the middle 1930s'
        choice_b = '1850'
        choice_c = 'the beginning of the twetienth century'
        choice_d = 'the 1840s*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the true statement. The process of sending and receiving started as early as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_8:
    def __init__(self, *args, **kwargs):
        choice_a = 'decoding'
        choice_b = 'encoding*'
        choice_c = 'storage'
        choice_d = 'interpretation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the steps is not included in the process of reception"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_9:
    def __init__(self, *args, **kwargs):
        choice_a = 'UHF communications'
        choice_b = 'single-sideband communications'
        choice_c = 'television communications'
        choice_d = 'person-to-person voice communications*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The acoustic channel is used for which of the following?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_10:
    def __init__(self, *args, **kwargs):
        choice_a = 'superimosing a low frequency on a high frequency*'
        choice_b = 'superimposing a high frequency on a low frequency'
        choice_c = 'carrier interruption'
        choice_d = 'frequency shift and phase shift'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Amplitude modulation is the process of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_11:
    def __init__(self, *args, **kwargs):
        choice_a = 'shot noise'
        choice_b = 'random noise'
        choice_c = 'impulse noise'
        choice_d = 'transit-time noise*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following types of noise becomes of great importance at high frequencies. It is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_12:
    def __init__(self, *args, **kwargs):
        choice_a = 'HF mixers are generally noisier than HF amplifiers'
        choice_b = 'Impulse noise voltage is independent of bandwidth*'
        choice_c = 'Thermal noise is independent of the frequency at which it is measured'
        choice_d = 'Industrial noise is usually of the impulse type'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_13:
    def __init__(self, *args, **kwargs):
        choice_a = 'halved'
        choice_b = 'quadrupled'
        choice_c = 'doubled'
        choice_d = 'unchanged*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The value of a resistor creating thermal noise is doubled. The noise power generator is therefore"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_14:
    def __init__(self, *args, **kwargs):
        choice_a = 'Input noise voltage*'
        choice_b = 'Equivalent noise resistance'
        choice_c = 'Noise temperature'
        choice_d = 'Noise figure'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is not a useful quantity for comparing the noise performance of receivers"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_15:
    def __init__(self, *args, **kwargs):
        choice_a = 'Solar noise'
        choice_b = 'Cosmic noise'
        choice_c = 'Atmospheric noise*'
        choice_d = 'Galactic noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the noise whose source is in a category different from that of the other three."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_16:
    def __init__(self, *args, **kwargs):
        choice_a = 'its resistance'
        choice_b = 'its temperature'
        choice_c = 'Boltzmann\'s constant*'
        choice_d = 'the bandwidth over which it is measured'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: The square of the thermal noise voltage generated by a resistor is proportional to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_17:
    def __init__(self, *args, **kwargs):
        choice_a = 'noise generated in the receiver*'
        choice_b = 'noise generated in the transmitter'
        choice_c = 'externally generated noise'
        choice_d = 'internally generated noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the broad classifications of noise are most difficult to treat?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_18:
    def __init__(self, *args, **kwargs):
        choice_a = 'between 8 MHz and 1.43 GHz'
        choice_b = 'below 20 MHz'
        choice_c = 'between 20 to 120 MHz*'
        choice_d = 'above 1.5 GHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Space noise generally covers a wide frequency spectrum, but the strongest interference occurs"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_19:
    def __init__(self, *args, **kwargs):
        choice_a = 'call calculations are based on peak to peak values'
        choice_b = 'calculations are based on peak values'
        choice_c = 'calculations are based on average values'
        choice_d = 'calculations are based on RMS values*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When dealing with random noise calculations it must be remembered that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_20:
    def __init__(self, *args, **kwargs):
        choice_a = 'signal-to-noise ratio'
        choice_b = 'noise factor*'
        choice_c = 'shot noise'
        choice_d = 'thermal noise agitation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is the most reliable measurement of comparing amplifier noise characteristics"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_21:
    def __init__(self, *args, **kwargs):
        choice_a = 'Random noie power is inversely proportional to bandwidth'
        choice_b = 'Flicker is sometimes called demodulation noise'
        choice_c = 'Noise in mixers is caused by by inadequate image frequency rejection*'
        choice_d = 'A random voltage across a resistance cannot be calculated'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following statements is true?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_22:
    def __init__(self, *args, **kwargs):
        choice_a = '4 V*'
        choice_b = '3 V'
        choice_c = '2 V'
        choice_d = '1 V'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the plate supply voltage for a plate-modulated class C amplifier is V, the maximum plate-cathode voltage could be almost as high as """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_23:
    def __init__(self, *args, **kwargs):
        choice_a = 'linear devices*'
        choice_b = 'harmonic devices'
        choice_c = 'class C amplifiers'
        choice_d = 'nonlinear devices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a low-level AM system, amplifiers following the modulated stage must be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_24:
    def __init__(self, *args, **kwargs):
        choice_a = '50'
        choice_b = '150'
        choice_c = '100'
        choice_d = '66.66*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the carrier of a 100 percent modulated AM wave is suppressed, the percentage power saveing will be"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_25:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent tuned circuit dampling'
        choice_b = 'prevent excessive grid current*'
        choice_c = 'screen-modulated class C amplifier '
        choice_d = 'grid-modulated class A amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Leak-type bias is used in a plate-modulated class C amplifier to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_26:
    def __init__(self, *args, **kwargs):
        choice_a = 'plate-modulated class C amplifier'
        choice_b = 'grid-modulated class C amplifier*'
        choice_c = 'screen-modulated class C amplifier'
        choice_d = 'grid-modulated class A amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The output stage of a television transmitter is most likely to be a"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_27:
    def __init__(self, *args, **kwargs):
        choice_a = 'unchanged'
        choice_b = 'halved'
        choice_c = 'doubled'
        choice_d = 'increased by 50 percent*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The modulation index of an AM wave is changed from 0 to 1. The transmitted power is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_28:
    def __init__(self, *args, **kwargs):
        choice_a = 'the lower modulating power required*'
        choice_b = 'higher power output per transistor'
        choice_c = 'better efficiency'
        choice_d = 'better linearity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the advantages of the base modulation over collector modulation of a transistor class C amplifier is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_29:
    def __init__(self, *args, **kwargs):
        choice_a = 'is 1'
        choice_b = 'cannot be calculated unless the phase relations are known'
        choice_c = 'is 0.5*'
        choice_d = 'is 0.7'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A carrier is simultaneously modulated by two sine waves with modulation indices 0.3 and 0.4; the total modulation index """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_30:
    def __init__(self, *args, **kwargs):
        choice_a = 'it is more noise immune than other modulation systems'
        choice_b = 'compared with other systems it requires less transmitting power'
        choice_c = 'its use avoids receiver complexity*'
        choice_d = 'no other modulation system can provide the necessary bandwidth for high fidelity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Amplitude modulation is used for broadcasting because """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_31:
    def __init__(self, *args, **kwargs):
        choice_a = '1:3*'
        choice_b = '1:2'
        choice_c = '2:3'
        choice_d = 'None of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the ratio of modulating power to total power at 100 percent modulation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_32:
    def __init__(self, *args, **kwargs):
        choice_a = 'More channel space is available'
        choice_b = 'Transmitter circuits must be more stable, giving better reception*'
        choice_c = 'The signal is more noise-resistant'
        choice_d = 'Much less power is required for the same signal strength'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement regarding the advantages of SSB over double sideband, full-carrier AM"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_33:
    def __init__(self, *args, **kwargs):
        choice_a = 'Single sideband, full carrier (H3E)'
        choice_b = 'Vestigial sideband (C3F)'
        choice_c = 'Single sideband, suppressed carrier (J3E)*'
        choice_d = 'Double sideband, full carrier (A3E)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When the modulation index of an AM wave is soubles, the antenna current is also doubled. The AM system being used is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_34:
    def __init__(self, *args, **kwargs):
        choice_a = 'Switching from one sideband to the other is simpler.'
        choice_b = 'It is possible to generate SSb at any frequency '
        choice_c = 'SSB with lower audio frequencies present can be generated'
        choice_d = 'There are more balanced modulators, therefore the carrier is suppressed better*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which on of the following advantages of the phase cancellation method of """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_35:
    def __init__(self, *args, **kwargs):
        choice_a = 'mechanical*'
        choice_b = 'RC'
        choice_c = 'LC'
        choice_d = 'low-pass'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The most commonly used filters in SSB generation are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_36:
    def __init__(self, *args, **kwargs):
        choice_a = 'class C audio amplifier'
        choice_b = 'tuned modulator'
        choice_c = 'class B RF amplifier*'
        choice_d = 'class A RF output amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an SSB transmitter, one is most likely to find a """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_37:
    def __init__(self, *args, **kwargs):
        choice_a = 'H3E*'
        choice_b = 'A3E'
        choice_c = 'B8E'
        choice_d = 'C3F'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate in which one of the following only one sideband is transmitted"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_38:
    def __init__(self, *args, **kwargs):
        choice_a = 'filter system'
        choice_b = 'phase-shift method'
        choice_c = 'third method'
        choice_d = 'balanced modulator*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following cannot be used to remove the unwanted sideband in SSB. This is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_39:
    def __init__(self, *args, **kwargs):
        choice_a = 'allow the receiver to have a frequency synthesizer'
        choice_b = 'simplify the frequency stability problem in reception*'
        choice_c = 'reduce the power that must be transmitted'
        choice_d = 'reduce the bandwidth required for transmission'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""R3E modulation is sometimes used to """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_40:
    def __init__(self, *args, **kwargs):
        choice_a = 'ISB*'
        choice_b = 'carrier insertion'
        choice_c = 'SSB with pilot carrier'
        choice_d = 'lincompex'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To provide two or more voice circuits with the same carrier, it is necessary to use"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_41:
    def __init__(self, *args, **kwargs):
        choice_a = 'HF point-to-point communication'
        choice_b = 'monoaural broadcasting'
        choice_c = 'TV broadcasting*'
        choice_d = 'stereo broadcasting'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Vestigial sideband modulation (C3F) is normally used for"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_42:
    def __init__(self, *args, **kwargs):
        choice_a = 'the discriminator must have a fast time constant to prevent demodulation'
        choice_b = 'the higher the discriminator frequency, the better the oscillator frequency stability'
        choice_c = 'the discriminator frequency must be too low, or the system will fail*'
        choice_d = 'phase modulation is converted into FM by the equalizer circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the stabilized reactance modulator AFC system"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_43:
    def __init__(self, *args, **kwargs):
        choice_a = 'the carrier frequency disappears when the modulation index is large'
        choice_b = 'the amplitude of any sideband depends on the modulation index*'
        choice_c = 'the total number of sidebands depends on the modulation index'
        choice_d = 'the carrier frequency cannot disappear'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the spectrum of a frequency-modulated wave"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_44:
    def __init__(self, *args, **kwargs):
        choice_a = 'is purely theoretical because they are the same in practice'
        choice_b = 'is too great to make the two systems compatible'
        choice_c = 'lies in the poorer audio response of phase modulation'
        choice_d = 'lies in the different definitions of the modulation index*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The difference between phase and frequency modulation"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_45:
    def __init__(self, *args, **kwargs):
        choice_a = 'The system is basically phase, not frequency modulation'
        choice_b = 'AFC is not needed, as crystal oscillator is used'
        choice_c = 'Frequency multiplication must be used'
        choice_d = 'Equalization is unnecessary*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement regarding the Armstrong modulation system."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_46:
    def __init__(self, *args, **kwargs):
        choice_a = 'mf/3'
        choice_b = 'mf'
        choice_c = '3mf*'
        choice_d = '9mf'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An Fm signal with a modulation index "mf" is passed through a frequency tripler. The wave in the output of the tripler will have a modulation index of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_47:
    def __init__(self, *args, **kwargs):
        choice_a = '5'
        choice_b = 'indeterminate'
        choice_c = 'delta/5'
        choice_d = 'delta*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An Fm signal with a deviation "delta" is passed through a mixer, and has its frequency reduced fivefold. The deviation in the output of the mixer is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_48:
    def __init__(self, *args, **kwargs):
        choice_a = 'boosting the bass frequencies'
        choice_b = 'amplifying the higher audio frequencies*'
        choice_c = 'preamplifying the whole audio band'
        choice_d = 'converting the phase modulation to FM'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A pre-emphasis circuit provides extra noise immunity by"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_49:
    def __init__(self, *args, **kwargs):
        choice_a = 'remains constant'
        choice_b = 'is decreased*'
        choice_c = 'is increased'
        choice_d = 'is equalized'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Since noise phase-modulates the FM wave, as the noise sideband frequency approaches the carrier frequency, the noise amplitude"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_50:
    def __init__(self, *args, **kwargs):
        choice_a = 'amplitude modulation'
        choice_b = 'phase modulation'
        choice_c = 'frequency modulation*'
        choice_d = 'any of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""when the modulating frequency is doubled, the modulation index is halved, and the modulating voltage remains constant. The modulation system is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_51:
    def __init__(self, *args, **kwargs):
        choice_a = 'better noise immunity is provided'
        choice_b = 'lower bandwidth is required*'
        choice_c = 'the transmitted power is more useful'
        choice_d = 'less modulating power is required'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which one of the following is not an advantage of FM over AM"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_52:
    def __init__(self, *args, **kwargs):
        choice_a = 'reactance FET modulator'
        choice_b = 'varactor diode modulator'
        choice_c = 'Armstrong modulator*'
        choice_d = 'reactance bipolar transistor modulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is an indirect way of generating FM. This is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_53:
    def __init__(self, *args, **kwargs):
        choice_a = 'sum signal modulates 19 kHz subcarrier'
        choice_b = 'difference signal modulates the 19kHz subcarrier'
        choice_c = 'difference signal modulates the 38 kHz subcarrier*'
        choice_d = 'difference signal modulates the 67 kHz subcarrier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an FM stereo multiplex transmission, the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_54:
    def __init__(self, *args, **kwargs):
        choice_a = 'much easier alignment'
        choice_b = 'better linearity'
        choice_c = 'greater limiting*'
        choice_d = 'fewer tuned circuits'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following statements about the advantages of the phase discriminator over the slope detector is false:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_55:
    def __init__(self, *args, **kwargs):
        choice_a = 'the circuit is always biased in class C, by virtue of the leak-type bias*'
        choice_b = 'When the input increases past the threshold of the limiting, the gain decreases to keep the output constant'
        choice_c = 'the output must be tuned'
        choice_d = 'leak-type bias must be used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Show which of the following statements about the amplitude limiter is untrue"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_56:
    def __init__(self, *args, **kwargs):
        choice_a = 'an increase in signal strength produces more AGC*'
        choice_b = 'the audio stage gain is normally controlled by the AGC'
        choice_c = 'the faster the AGC time constant the more accurate the output'
        choice_d = 'the highest AGC voltage is produced'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a radio receiver with AGC"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_57:
    def __init__(self, *args, **kwargs):
        choice_a = 'local oscillator operates below the signal frequency'
        choice_b = 'mixer input myst be tuned to the signal frequency*'
        choice_c = 'local oscillator frequency is normally double the IF'
        choice_d = 'RF amplifier normally works at 455 kHz above the carrier frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a broadcast superheterodyne receiver"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_58:
    def __init__(self, *args, **kwargs):
        choice_a = 'squelch'
        choice_b = 'variable sensitivity*'
        choice_c = 'variable selectiivity'
        choice_d = 'double conversion'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To prevent loading of the IF amplifier in  a receiver, one should use"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_59:
    def __init__(self, *args, **kwargs):
        choice_a = '750 kHz'
        choice_b = '900 kHz'
        choice_c = '1650 kHz'
        choice_d = '2100 kHz*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A superheterodyne receiver with an IF of 450 kHz is tuned to a signal at 1200 kHz. THe image frequency is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_60:
    def __init__(self, *args, **kwargs):
        choice_a = 'the linearity is worse than in phase discriminator*'
        choice_b = 'stabilization against signal strength variations is provided'
        choice_c = 'the output is twice that obtainable from a similar phase discriminator '
        choice_d = 'the circuit is the same as in a discriminator, except that the diode are reversed'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a ratio detector"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_61:
    def __init__(self, *args, **kwargs):
        choice_a = 'an audio amplifier when the carrier is absent*'
        choice_b = 'RF interference when the signal is weak'
        choice_c = 'An IF amplifier when the AGC is maximum'
        choice_d = 'An IF amplifier when the AGC is minimum'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""THe typical squelch circuit cuts off"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_62:
    def __init__(self, *args, **kwargs):
        choice_a = 'The noise limiter cuts off the receiver\'s output during a noise pulse'
        choice_b = 'A product demodulator could be used for the reception of Morse code'
        choice_c = 'Double conversion is used to improve image rejection'
        choice_d = 'Variable sensitivity is used to eliminate selective fading*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement in connection with communications receivers"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_63:
    def __init__(self, *args, **kwargs):
        choice_a = 'it is a simpler piece of equipment'
        choice_b = 'its frequency stability is better'
        choice_c = 'it does not require crystal oscillator'
        choice_d = 'it is relatively free of spurious frequencies*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The controlled oscillator synthesizer is sometimes preferred over the direct one because"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_64:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduce the spurious frequency problem*'
        choice_b = 'increase the frequency stability of the synthesizer'
        choice_c = 'reduce the number of decades'
        choice_d = 'reduce the number of crystals used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The frequency generated by each decade in a direct frequency synthesizer is much higher than the frequency shown; this is done to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_65:
    def __init__(self, *args, **kwargs):
        choice_a = 'balanced modulator'
        choice_b = 'product modulator'
        choice_c = 'BFO'
        choice_d = 'phase discriminator*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following circuits could not demodulate SSB"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_66:
    def __init__(self, *args, **kwargs):
        choice_a = 'improving the effectiveness of the AGC'
        choice_b = 'reducing the effect of negative-peak clipping*'
        choice_c = 'reducing the effect of noise at low modulation depths'
        choice_d = 'improving the selectivity of the receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a FET is used as the first Af amplifier in a transistor receiver, this will have the effect of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_67:
    def __init__(self, *args, **kwargs):
        choice_a = 'gain variation over the frequency coverage range'
        choice_b = 'insufficient gain and sensitivity*'
        choice_c = 'inadequate selectivity at high frequencies'
        choice_d = 'instability'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: The superheterodyne receiver replaced the TRF receiver because the latter suffered from"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_68:
    def __init__(self, *args, **kwargs):
        choice_a = 'is created within the receiver itself'
        choice_b = 'is due to insufficient adjacent channel rejection'
        choice_c = 'is not rejected by the IF tunes circuits*'
        choice_d = 'is independent of the frequency to which the receiver is tuned'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The image frequency of a superheterodyne receiver """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_69:
    def __init__(self, *args, **kwargs):
        choice_a = 'provide improved tracking'
        choice_b = 'permit better adjacent-channel rejection'
        choice_c = 'increase the tuning range of the receiver'
        choice_d = 'improve the rejection of the image frequency*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the main functions of the RF amplifier in a superheterodyne receiver is to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_70:
    def __init__(self, *args, **kwargs):
        choice_a = 'blocking*'
        choice_b = 'double-spotting'
        choice_c = 'diversion reception'
        choice_d = 'sensitivity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A receiver has poor IF selectivity. It will therefore have poor"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_71:
    def __init__(self, *args, **kwargs):
        choice_a = 'variable selectivity'
        choice_b = 'padding capacitors*'
        choice_c = 'double spotting'
        choice_d = 'double conversion'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three-point tracking is achieved with"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_72:
    def __init__(self, *args, **kwargs):
        choice_a = 'to help the image frequency rejection'
        choice_b = 'to permit easier tracking'
        choice_c = 'because otherwise an intermediate frequency could not be produced'
        choice_d = 'to allow adequate frequency coverage without switching*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The local oscillator of a broadcast receiver is tuned to a frequency higher than the incoming frequency"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_73:
    def __init__(self, *args, **kwargs):
        choice_a = 'image frequency rejection is very good'
        choice_b = 'the local oscillator need not be extremely stable'
        choice_c = 'the selectivity will be poor'
        choice_d = 'tracking will be improved*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the intermediate frequency is very high (indicate the false statement )"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_74:
    def __init__(self, *args, **kwargs):
        choice_a = 'diagonal clipping'
        choice_b = 'poor AGC operation'
        choice_c = 'negative-peak clipping*'
        choice_d = 'poor AF response'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A low ratio of the ac to the dc load impedance of a diode detector results in """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_75:
    def __init__(self, *args, **kwargs):
        choice_a = 'product detector'
        choice_b = 'diode balanced modulator'
        choice_c = 'bipolar transistor balanced modulator*'
        choice_d = 'complete phase-shift generator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following cannot be used to demodulate SSB"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_76:
    def __init__(self, *args, **kwargs):
        choice_a = 'the receiver cannot use a phase comparator for AFC'
        choice_b = 'adjacent-channel rejection is more difficult*'
        choice_c = 'production of AGC is a rather a complicated process'
        choice_d = 'the transmission is not compatible with A3E'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: Noting that no carrier is transmitted with J3E, we see that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_77:
    def __init__(self, *args, **kwargs):
        choice_a = 'it does not suffer from double-spotting'
        choice_b = 'its image frequency rejection is poor'
        choice_c = 'it is unaffected by AGC derived from nearby transmissions*'
        choice_d = 'its detector suffers from burnout'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a receiver has good blocking performance, this means that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_78:
    def __init__(self, *args, **kwargs):
        choice_a = 'single-sideband, suppressed carrier'
        choice_b = 'single-sideband, reduced carrier'
        choice_c = 'ISB'
        choice_d = 'single-sideband, full carrier*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An AM receiver uses a diode detector for demodulation. This enables it satisfactorily to receive"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_79:
    def __init__(self, *args, **kwargs):
        choice_a = 'a short circuit'
        choice_b = 'a complex impedance*'
        choice_c = 'an open circuit'
        choice_d = 'a pure reactance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: The SWR on a transmission line is infinity, the line is terminated in """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_80:
    def __init__(self, *args, **kwargs):
        choice_a = 'a short-circuited stub at the load'
        choice_b = 'an inductance at the load'
        choice_c = 'a capacitance at some specific distance'
        choice_d = 'a short-circuited stub at some specific distance from the load*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ( 75 - j50 ) ohm is connected to a coaxial transmission line of Zo = 75 ohms, at 10 GHz. The best method of matching consists of connecting"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_81:
    def __init__(self, *args, **kwargs):
        choice_a = 'depends on the dielectric constant of the material used*'
        choice_b = 'increases the velocity along the transmission line'
        choice_c = 'is governed by the skin effect'
        choice_d = 'is higher for a solid dielectric than for air'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The velocity factor of a transmission line"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_82:
    def __init__(self, *args, **kwargs):
        choice_a = 'a short-circuited stub'
        choice_b = 'an open-circuited stub'
        choice_c = 'a quarter-wave line*'
        choice_d = 'a half-wave line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Impedance inversion may be obtained with"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_83:
    def __init__(self, *args, **kwargs):
        choice_a = 'more difficult to make an connect'
        choice_b = 'made of a transmission line with a different characteristic impedance'
        choice_c = 'liable to radiate*'
        choice_d = 'incapable of giving a full range of reactances'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Short-circuited stubs are preferred to open-circuited stubs because the latter are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_84:
    def __init__(self, *args, **kwargs):
        choice_a = 'balun'
        choice_b = 'broadband directional coupler'
        choice_c = 'double stub*'
        choice_d = 'single stub of adjustable position'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For transmission-line load matching over a range of frequencies, it is best to use a """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_85:
    def __init__(self, *args, **kwargs):
        choice_a = 'low directional coupling'
        choice_b = 'poor directivity'
        choice_c = 'high SWR'
        choice_d = 'narrow bandwidth*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The main disadvantage of the two-hole directional coupler is """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_86:
    def __init__(self, *args, **kwargs):
        choice_a = 'slotted line'
        choice_b = 'balun*'
        choice_c = 'directional coupler'
        choice_d = 'quarter-wave transformer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To couple a coaxial line to a parallel-wire line, it is best to use a"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_87:
    def __init__(self, *args, **kwargs):
        choice_a = 'I^2 R, R, and temperature L'
        choice_b = 'Radiation, I^2 R, and dielectric heating*'
        choice_c = 'Dielectric separation, insulation breakdown, and radiation'
        choice_d = 'Conductor heating, dielectric heating, and radiation resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the three types of transmission line energy losses"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_88:
    def __init__(self, *args, **kwargs):
        choice_a = 'a device used to connect a transmitter to a directional antenna'
        choice_b = 'a coupling device for matching impedance*'
        choice_c = 'a device used to measure transmission line power'
        choice_d = 'an SWr measuring instrument'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the true statement below. The directional coupler is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_89:
    def __init__(self, *args, **kwargs):
        choice_a = 'SIDs'
        choice_b = 'fading*'
        choice_c = 'atmospheric storms'
        choice_d = 'faraday rotation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which one of the following terms applies to troposcatter propagation"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_90:
    def __init__(self, *args, **kwargs):
        choice_a = 'of the low powers required'
        choice_b = 'the transmitting antennas are of convienient size'
        choice_c = 'they are very reliable*'
        choice_d = 'they penetrate the ionosphere easily'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""VLF waves are used for some type of services because"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_91:
    def __init__(self, *args, **kwargs):
        choice_a = '20 kHz'
        choice_b = '15 MHz'
        choice_c = '900 MHz'
        choice_d = '12 GHz*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following frequencies cannot be used for reliable beyond-the-horizon terrestrial communications without repeaters"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_92:
    def __init__(self, *args, **kwargs):
        choice_a = 'absorbed by the F2 layer'
        choice_b = 'reflected by the D layer'
        choice_c = 'capable of use for long distance communications on the moon'
        choice_d = 'affected by the solar cycle*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""High frequency waves are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_93:
    def __init__(self, *args, **kwargs):
        choice_a = 'to avoid tilting'
        choice_b = 'to prevent sky-wave and upper ray interference*'
        choice_c = 'to avoid the Faraday effect'
        choice_d = 'so as not to exceed the critical frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Distance near the skip distance should be used for the sky-wave propagation"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_94:
    def __init__(self, *args, **kwargs):
        choice_a = 'a more directional antenna'
        choice_b = 'a broadband antenna'
        choice_c = 'frequency diversity*'
        choice_d = 'space diversity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ship-to-ship communications system is plagued by fading. The best solution seems to be use of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_95:
    def __init__(self, *args, **kwargs):
        choice_a = 'window*'
        choice_b = 'critical frequency'
        choice_c = 'gyro frequency range'
        choice_d = 'resonance in the atmosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A range of microwave frequencies more easily passed by the atmosphere than are the others is called a """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_96:
    def __init__(self, *args, **kwargs):
        choice_a = 'ground waves'
        choice_b = 'sky waves'
        choice_c = 'surface waves'
        choice_d = 'space waves*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Frequencies in the UHF range normally propagate by means of """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_97:
    def __init__(self, *args, **kwargs):
        choice_a = 'HF'
        choice_b = 'VHF'
        choice_c = 'UHF*'
        choice_d = 'VLF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Tropospheric scatter is used with frequencies in the following range"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_98:
    def __init__(self, *args, **kwargs):
        choice_a = 'interference from the sky wave'
        choice_b = 'loss of line-of-sight conditions'
        choice_c = 'maximum single-hop distance limitation'
        choice_d = 'tilting*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The ground wave eventually disappears, as one moves away from the transmitter, because of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_99:
    def __init__(self, *args, **kwargs):
        choice_a = 'is caused by reflection'
        choice_b = 'is due to the transverse nature of the waves*'
        choice_c = 'results from the longitudinal nature of the waves'
        choice_d = 'is always vertical in an isotropic medium'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In electromagnetic waves, polarization"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_100:
    def __init__(self, *args, **kwargs):
        choice_a = 'absorption'
        choice_b = 'attenuation*'
        choice_c = 'refraction'
        choice_d = 'reflection'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As electromagnetic waves travel in space, only one of the following can happen to them"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_101:
    def __init__(self, *args, **kwargs):
        choice_a = 'their frequency*'
        choice_b = 'their distance from the transmitter'
        choice_c = 'the polarization of the waves'
        choice_d = 'the polarization of the atmosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The absorption of radio waves by the atmosphere depends on"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_102:
    def __init__(self, *args, **kwargs):
        choice_a = 'pass into a medium of different dielectric constant*'
        choice_b = 'are polarized at right angles to the direction of propagation'
        choice_c = 'encounter a perfectly conducting plane'
        choice_d = 'pass through a small slot in a conducting plane'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Electromagnetic waves are refracted when they"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_103:
    def __init__(self, *args, **kwargs):
        choice_a = 'is caused by reflections from the ground'
        choice_b = 'arises only with spherical wavefronts'
        choice_c = 'will occur when the waves pass through a large slot'
        choice_d = 'may occur around the edge of a sharp obstacle*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Diffraction of electromagnetic waves"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_104:
    def __init__(self, *args, **kwargs):
        choice_a = 'the Faraday effect'
        choice_b = 'ducting*'
        choice_c = 'tropospheric scatter'
        choice_d = 'ionosperic reflection'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When microwave signals follow the curvature of the earth, this is known as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_105:
    def __init__(self, *args, **kwargs):
        choice_a = 'troposcatter'
        choice_b = 'superrefraction'
        choice_c = 'ionospheric effect'
        choice_d = 'the Faraday effect*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Helical antennas are often used for satellite tracking at VHF because of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_106:
    def __init__(self, *args, **kwargs):
        choice_a = 'acts like a single antenna of twice the height'
        choice_b = 'is unlikely to need a ground screen'
        choice_c = 'acts as an antenna array*'
        choice_d = 'must be horizontally polarized'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An ungrounded antenna near the ground"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_107:
    def __init__(self, *args, **kwargs):
        choice_a = 'The rhombic antenna*'
        choice_b = 'The folded dipole'
        choice_c = 'The end-fire array'
        choice_d = 'The broadside array'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following consists of non-resonant antennas:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_108:
    def __init__(self, *args, **kwargs):
        choice_a = 'conical horn'
        choice_b = 'folded dipole'
        choice_c = 'log periodic*'
        choice_d = 'square loop'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is very usegul as a multiband HF receiving antenna. This is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_109:
    def __init__(self, *args, **kwargs):
        choice_a = 'biconical'
        choice_b = 'horn*'
        choice_c = 'helical'
        choice_d = 'discone'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following antennas is best excited from a waveguide?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_110:
    def __init__(self, *args, **kwargs):
        choice_a = 'impossibility of a good ground connection'
        choice_b = 'protection of personnel working underground*'
        choice_c = 'provision of an earth for the antenna'
        choice_d = 'rockiness of the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following reasons for using a counterpoise with antenna is false"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_111:
    def __init__(self, *args, **kwargs):
        choice_a = 'to make the antenna look resistive'
        choice_b = 'to provide the output amplifier with the correct load impedance'
        choice_c = 'to discriminate against harmonics'
        choice_d = 'to prevent reradiation of the local oscillator*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is not a reason for the use of an antenna coupler"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_112:
    def __init__(self, *args, **kwargs):
        choice_a = 'discone'
        choice_b = 'folded dipole'
        choice_c = 'helical'
        choice_d = 'marconi*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the antenna that is not wideband"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_113:
    def __init__(self, *args, **kwargs):
        choice_a = 'impossibility of a good ground connection'
        choice_b = 'provision of an earth for the antenna'
        choice_c = 'protection of personnel working undernearth*'
        choice_d = 'improvement of the radiation pattern of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which one of the following reasons for the use of a ground screen with antennas is false"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_114:
    def __init__(self, *args, **kwargs):
        choice_a = 'Good bandwidth'
        choice_b = 'Parasitic elements'
        choice_c = 'Folded Dipole'
        choice_d = 'High Gain*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which one of the following terms does not apply to the Yagi-Uda array? """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_115:
    def __init__(self, *args, **kwargs):
        choice_a = 'helical*'
        choice_b = 'small circular loop'
        choice_c = 'parabolic reflector'
        choice_d = 'Yagi-Uda'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An antenna that is circularly polarized is the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_116:
    def __init__(self, *args, **kwargs):
        choice_a = 'infinitesimal dipole'
        choice_b = 'isotropic antenna*'
        choice_c = 'elementary doublet'
        choice_d = 'half-wave dipole'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The standard reference antenna for the directive gain is the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_117:
    def __init__(self, *args, **kwargs):
        choice_a = 'effective height*'
        choice_b = 'bandwidth'
        choice_c = 'beamwidth'
        choice_d = 'input capacitance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Top loading is sometimes used with an antenna in order to increase its """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_118:
    def __init__(self, *args, **kwargs):
        choice_a = 'increase the gain of the system'
        choice_b = 'increase the beamwidth of the system'
        choice_c = 'reduce the size of the main reflector'
        choice_d = 'allow the feed to be placed at a convinient point*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Cassegrain feed is used with a parabolic reflector to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_119:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduce the bulk of the lens'
        choice_b = 'increase the bandwidth of the lens'
        choice_c = 'increase the pin-point focusing'
        choice_d = 'correct the curvature of the wavefront from a horn that is too short'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Zoning is used with a dielectric antenna in order to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_120:
    def __init__(self, *args, **kwargs):
        choice_a = 'circular polarization*'
        choice_b = 'maneuverability'
        choice_c = 'broad bandwidth'
        choice_d = 'good front-to-back ratio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A helical antenna is used for satellite tracking because of its"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_121:
    def __init__(self, *args, **kwargs):
        choice_a = 'useful direction-finding antenna'
        choice_b = 'used as a radar receiving antenna'
        choice_c = 'circularly polarized like other circular antennas'
        choice_d = 'useful as UHF receiving antennas*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The discone antenna is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_122:
    def __init__(self, *args, **kwargs):
        choice_a = 'half-wave dipole'
        choice_b = 'log-periodic*'
        choice_c = 'discone'
        choice_d = 'marconi'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is not an omnidirectional antenna"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_123:
    def __init__(self, *args, **kwargs):
        choice_a = 'they travel along the broader walls of the guide'
        choice_b = 'they are reflected from the walls but do not travel along them*'
        choice_c = 'they travel through the dielectric without touching the walls'
        choice_d = 'they travel along all four walls of the waveguide'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When electromagnetic waves are propagated in a waveguide"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_124:
    def __init__(self, *args, **kwargs):
        choice_a = 'they depend on straight-line propagation which applies to microwaves only'
        choice_b = 'losses would be too heave at lower frequencies'
        choice_c = 'there are no generators powerful enough to excite them at lower frequencies'
        choice_d = 'they would be too bulky at lower frequencies*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Waveguides are used mainly for microwave signals because"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_125:
    def __init__(self, *args, **kwargs):
        choice_a = 'is greater than of free space*'
        choice_b = 'depends only on the waveguide dimensions and the free space length'
        choice_c = 'is inversely proportional to the phase velocity'
        choice_d = 'is directly proportional to the group velocity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The wavelength of a wave in a waveguide"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_126:
    def __init__(self, *args, **kwargs):
        choice_a = 'the latter are not distributed, like transmission lines'
        choice_b = 'the former can use stubs and quarter-wave transformers, unlike the latter'
        choice_c = 'transmission lines use the principal mode of propagation, and therefore do not suffer from low-frequency cutoff*'
        choice_d = 'terms such as impedance matching and standing-wave ratio cannot be applied to waveguides'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The main difference between the operation of transmission lines and waveguides is that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_127:
    def __init__(self, *args, **kwargs):
        choice_a = 'are less lossy'
        choice_b = 'can carry higher powers'
        choice_c = 'are less bulky*'
        choice_d = 'have lower attenuation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Compared with equivalent transmission lines, 3-GHz waveguides (indicate the false statement) """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_128:
    def __init__(self, *args, **kwargs):
        choice_a = 'transverse-electric'
        choice_b = 'transverse-magnetic*'
        choice_c = 'longitudinal'
        choice_d = 'transverse-electromagnetic'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a particular mode is excited in a waveguide, there appears an extra electric component, in the direction of propagation. The resulting mode is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_129:
    def __init__(self, *args, **kwargs):
        choice_a = 'the same as in free space'
        choice_b = 'the same as the wavelength perpendicular to the wall'
        choice_c = 'shortened because of the Doppler effect'
        choice_d = 'greater than in the actual direction of propagation*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When electromagnetic waves are reflected at an angle from a wall, their wavelength along the wall is """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_130:
    def __init__(self, *args, **kwargs):
        choice_a = 'velocity of propagation'
        choice_b = 'normal velocity'
        choice_c = 'group velocity'
        choice_d = 'phase velocity*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As a result of reflections from a plane conducting wall, electromagnetic waves acquired an apparent velocity greater than the velocity of light in free space. This is called the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_131:
    def __init__(self, *args, **kwargs):
        choice_a = 'the group velocity of the signal becomes zero'
        choice_b = 'the phase velocity of the signal becomes infinite'
        choice_c = 'the characteristic impedance of the guide becomes infinite*'
        choice_d = 'the wavelength within the waveguide becomes infinite'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: When the free space wavelength of a signal equals the cutoff wavelength of the guide"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_132:
    def __init__(self, *args, **kwargs):
        choice_a = 'TE11'
        choice_b = 'TE10'
        choice_c = 'TM22'
        choice_d = 'TE20*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A signal propagation in a waveguide has full wave of electric intensity change between the two further walls, and no component of the electric field in the direction of propagation. The mode is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_133:
    def __init__(self, *args, **kwargs):
        choice_a = 'it leads to the smallest waveguide dimensions'
        choice_b = 'the resulting impedance can be matched directly to coaxial lines*'
        choice_c = 'it is easier than the other modes'
        choice_d = 'propagation of it without any spurious generation can be ensured'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The dominant mode of propagation is preferred with rectangular waveguides because (indicate false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_134:
    def __init__(self, *args, **kwargs):
        choice_a = 'to help in the alignment of the waveguides'
        choice_b = 'because it is simpler than any join'
        choice_c = 'to compensate for discontinuities at the join*'
        choice_d = 'to increase the bandwidth of the system'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A choke flange may be used to couple two waveguides"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_135:
    def __init__(self, *args, **kwargs):
        choice_a = 'rat-race'
        choice_b = 'E-plane T*'
        choice_c = 'hybrid ring'
        choice_d = 'magic T'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In order to couple two generators to a waveguide system without coupling them to each other, one could NOT use a"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_136:
    def __init__(self, *args, **kwargs):
        choice_a = 'screw'
        choice_b = 'stub'
        choice_c = 'iris*'
        choice_d = 'plunger'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following waveguides tuning components is not easily adjustable?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_137:
    def __init__(self, *args, **kwargs):
        
        choice_a = 'vane attenuator'
        choice_b = 'waveguide below cutoff*'
        choice_c = 'mode filter'
        choice_d = 'flap attenuator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A piston attenuator is a """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_138:
    def __init__(self, *args, **kwargs):
        choice_a = 'a Q that is too low'
        choice_b = 'a shpae whose resonant frequency is too difficult to calculate'
        choice_c = 'harmonically related resonant frequencies*'
        choice_d = 'too heavy losses'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Cylindrical cavity resonators are not used with klystrons because they have"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_139:
    def __init__(self, *args, **kwargs):
        choice_a = 'because it is more efficient'
        choice_b = 'to increase coupling of the signal'
        choice_c = 'to reduce spurious mode generation'
        choice_d = 'to increase the bandwidth of the system*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A directional coupler with three or more holes is sometimes used in preference to the two-hole coupler """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_140:
    def __init__(self, *args, **kwargs):
        choice_a = 'A nonconductive with magnetic properties*'
        choice_b = 'An intermetallic compound with particularly good conductivity'
        choice_c = 'An insulator which heavily attenuates magnetic fields'
        choice_d = 'A microwave semiconductor invented by Faraday'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ferrite is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_141:
    def __init__(self, *args, **kwargs):
        choice_a = 'circulator'
        choice_b = 'isolator'
        choice_c = 'garnet*'
        choice_d = 'phase shifter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Manganese ferrite may be used as a (indicate false answer) """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_142:
    def __init__(self, *args, **kwargs):
        choice_a = 'Curie temperature*'
        choice_b = 'Saturation magnetization'
        choice_c = 'line width'
        choice_d = 'gyromagnetic resonance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The maximum power that may be handled by a ferrite component is limited by the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_143:
    def __init__(self, *args, **kwargs):
        choice_a = 'a metal semiconductor point-contact diode'
        choice_b = 'a microwave mixer diode'
        choice_c = 'often used as a microwave detector'
        choice_d = 'suitable for use as a microwave switch*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A PIN diode is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_144:
    def __init__(self, *args, **kwargs):
        choice_a = 'to couple two different antennas to a transmitter without mutual interference'
        choice_b = 'to allow the one antenna to be used for reception or retransmission without mutual interference'
        choice_c = 'to prevent interference between two antennas when they are connected to a receiver'
        choice_d = 'to increase the speed of the pulses in pulsed radar'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A duplexer is used"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_145:
    def __init__(self, *args, **kwargs):
        choice_a = 'the smaller cross section needed'
        choice_b = 'lower attenuation at any frequency*'
        choice_c = 'freedom from spurious modes'
        choice_d = 'rotation of polarization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        
        random.shuffle(choices)

        self.question = f"""For some applications, circular waveguides may be preferred to rectangular ones because of """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_146:
    def __init__(self, *args, **kwargs):
        choice_a = 'elliptical'
        choice_b = 'flexible'
        choice_c = 'coaxial*'
        choice_d = 'ridged'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following cannot be followed by the word 'waveguide'"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_147:
    def __init__(self, *args, **kwargs):
        choice_a = 'circular'
        choice_b = 'ridged*'
        choice_c = 'rectangular'
        choice_d = 'flexible'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In order to reduce cross-sectional dimensions, the waveguide to use is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_148:
    def __init__(self, *args, **kwargs):
        choice_a = 'flexible waveguide'
        choice_b = 'ridged waveguide'
        choice_c = 'rectangular waveguide*'            
        choice_d = 'coaxial line' 

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For low  attenuation, the best transmission medium is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_149:
    def __init__(self, *args, **kwargs):
        choice_a = 'reflex klystron'
        choice_b = 'coaxial magnetron'
        choice_c = 'travelling-wave magnetron'
        choice_d = 'CFA*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A microwave tube amplifier uses an axial magnetic field and a radial electric field. This is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_150:
    def __init__(self, *args, **kwargs):
        choice_a = 'multicavity klystron'
        choice_b = 'BWO*'
        choice_c = 'CFA'
        choice_d = 'TWT'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is unlikely to be used as a pulsed device. It is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_151:
    def __init__(self, *args, **kwargs):
        choice_a = 'noise figure increases*'
        choice_b = 'transit time becomes too short'
        choice_c = 'shunt capacitive reactances become too large'
        choice_d = 'series inductive reactances become too small'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the reasons why vacuum tubes eventually fail at microwave frequencies is that their """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_152:
    def __init__(self, *args, **kwargs):
        choice_a = 'the electrodes are brought closer together'
        choice_b = 'a higher anode current is used'
        choice_c = 'multiple or coaxial leads are used*'
        choice_d = 'the anode voltage is made larger'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement. Transit time in microwave tubes will be reduced if"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_153:
    def __init__(self, *args, **kwargs):
        choice_a = 'is not a good low-level amplifier because of noise*'
        choice_b = 'has a higher repeller voltage to ensure a rapid transit time'
        choice_c = 'is not suitable for pulsed operation'
        choice_d = 'needs a long transit time through the buncher cavity to ensure current modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The multicavity klystron"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_154:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent the oscillations that occur in two-cavity klystrons*'
        choice_b = 'increase the bandwidth of the device'
        choice_c = 'improve the power gain'
        choice_d = 'increase the efficiency of the klystron'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement. Klystron amplifiers may use intermediate cavities to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_155:
    def __init__(self, *args, **kwargs):
        choice_a = 'is more efficient'
        choice_b = 'has a greater bandwidth*'
        choice_c = 'has a higher number of modes'
        choice_d = 'produces a higher output power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The TWT is sometimes preferred to the multicavity klystron amplifier, because it"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_156:
    def __init__(self, *args, **kwargs):
        choice_a = 'electrons are accelerated by the gap voltage on their return'
        choice_b = 'returning electrons give energy to the gap oscillations*'
        choice_c = 'it is equal to the period of the cavity oscillations'
        choice_d = 'the repeller is not damaged by striking electrons'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The transit time in the repeller space of a reflex klystron must be ( n + 3/4 ) cycles to ensure that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_157:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent mode jumping*'
        choice_b = 'prevent cathode back-heating'
        choice_c = 'ensure bunching'
        choice_d = 'improve the phase-focusing effect'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The cavity magnetron uses strapping to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_158:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent anode current in the absence of oscillation'
        choice_b = 'ensure that the oscillations are pulsed'
        choice_c = 'help in focusing the electron beam, thus preventing spreading'
        choice_d = 'ensure that the electrons will orbit around the cathode*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A magnetic field is used in the cavity magnetron to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_159:
    def __init__(self, *args, **kwargs):
        choice_a = 'hole and slot'
        choice_b = 'slot'
        choice_c = 'vane'
        choice_d = 'rising sun*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To avoid difficulties with strapping at high frequencies, the type of cavity structure used in the magnetron is the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_160:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent the electron beam from spreading in the long tube'
        choice_b = 'reduce the axial velocity of the RF field*'
        choice_c = 'ensure broadband operation'
        choice_d = 'reduce the noise figure'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The primary purpose of the helix in a traveling wave tube is to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_161:
    def __init__(self, *args, **kwargs):
        choice_a = 'help bunching'
        choice_b = 'prevent oscillations*'
        choice_c = 'prevent saturation'
        choice_d = 'increase gain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The attenuator is used in the traveling wave tube to """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_162:
    def __init__(self, *args, **kwargs):
        choice_a = 'allow pulsed operation'
        choice_b = 'improve electron bunching'
        choice_c = 'avoid the bulk of an electromagnet*'
        choice_d = 'allow coupled-cavity opeartion at the highest frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Periodic permanent-magnet focusing is used with TWTs to """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_163:
    def __init__(self, *args, **kwargs):
        choice_a = 'capable of a longer duty cycle*'
        choice_b = 'a more efficient bandwidth'
        choice_c = 'more broadband'
        choice_d = 'less noisy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The TWT is sometimes preferred to the magnetron as a radar transmitter output tube because it is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_164:
    def __init__(self, *args, **kwargs):
        choice_a = 'coaxial magnetron'
        choice_b = 'dither-tuned magnetron'
        choice_c = 'frequency-agile magnetron'
        choice_d = 'VTM*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A magnetron whose oscillating frequency is electronically adjustable over a wide range is called a """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_165:
    def __init__(self, *args, **kwargs):
        choice_a = 'periodic-permanent magnet'
        choice_b = 'coupled cavity'
        choice_c = 'helix'
        choice_d = 'ring-bar'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following is not a TWT slow-wave structure"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_166:
    def __init__(self, *args, **kwargs):
        choice_a = 'help focusing'
        choice_b = 'provide attenuation*'
        choice_c = 'improve bunching'
        choice_d = 'increase gain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The glass tube of a TWT may be coated with aquadag to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_167:
    def __init__(self, *args, **kwargs):
        choice_a = 'rising-sun magnetron'
        choice_b = 'crossed-field amplifier'
        choice_c = 'coaxial magnetron'
        choice_d = 'traveling-wave tube*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A backward-wave oscillator is based on the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_168:
    def __init__(self, *args, **kwargs):
        choice_a = 'because parametric amplification generates a lot of heat'
        choice_b = 'to increase bandwidth'
        choice_c = 'because it cannot operate at room temperature'
        choice_d = 'to improve the noise performance*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parametric amplifier must be cooled"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_169:
    def __init__(self, *args, **kwargs):
        choice_a = 'because maser amplification generates a lot of heat'
        choice_b = 'to increase bandwidth'
        choice_c = 'because it cannot operate at room temperature*'
        choice_d = 'to improve the noise performance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A ruby maser amplifier must be cooled"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_170:
    def __init__(self, *args, **kwargs):
        choice_a = 'does not readily lend itself to printed circuit techniques'
        choice_b = 'is more likely to radiate*'
        choice_c = 'is bulkier'
        choice_d = 'is more expensive and complex to manufacture'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The disadvantage of microstrip compared with stripline is that microstrip"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_171:
    def __init__(self, *args, **kwargs):
        choice_a = 'microstrip'
        choice_b = 'elliptical waveguide'
        choice_c = 'parallel wire line'
        choice_d = 'stripline*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The transmission system using two ground planes is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_173:
    def __init__(self, *args, **kwargs):
        choice_a = 'easier integration with semiconductor devices*'
        choice_b = 'lower tendency to radiate'
        choice_c = 'higher isolation between adjacent circuits'
        choice_d = 'higher Q'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement. An advantage of stripline over microstrip is its"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_172:
    def __init__(self, *args, **kwargs):
        choice_a = 'smaller bulk'
        choice_b = 'greater bandwidth'
        choice_c = 'higher power-handling capability*'
        choice_d = 'greater compatibility with solid state devices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: An advantage of stripline over waveguide is its"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_174:
    def __init__(self, *args, **kwargs):
        choice_a = 'gallium arsenide'
        choice_b = 'indium phosphide'
        choice_c = 'stripline'
        choice_d = 'quartz crystal*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Surface acoustic waves propagate in"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_176:
    def __init__(self, *args, **kwargs):
        choice_a = 'are less noisy'
        choice_b = 'lend themselves more easily to integration*'
        choice_c = 'are capable of higher efficiencies'
        choice_d = 'can provide higher gains'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement: FETs are preferred to bipolar transistors at the highest frequencies because they"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_175:
    def __init__(self, *args, **kwargs):
        choice_a = 'transmission media like stripline*'
        choice_b = 'filters'
        choice_c = 'UHF amplifiers'
        choice_d = 'oscillators at millimeter frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""SAW devices may be used as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_177:
    def __init__(self, *args, **kwargs):
        choice_a = 'a bipolar transistor'
        choice_b = 'a Gunn diode'
        choice_c = 'a step-recovery diode*'
        choice_d = 'an IMPATT diode'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For best low-level performance in the X-band, an amplifier should use"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_178:
    def __init__(self, *args, **kwargs):
        choice_a = 'lower noise'
        choice_b = 'higher efficiency*'
        choice_c = 'ability to operate at higher frequencies'
        choice_d = 'lesser sensitivity to harmonics'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The biggest advantage of the TRAPATT diode over the IMPATT diode is its"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_179:
    def __init__(self, *args, **kwargs):
        choice_a = 'varactor'
        choice_b = 'gunn'
        choice_c = 'schottky barrier'
        choice_d = 'RIMPATT*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following diodes will produce the highest pulsed power output"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_180:
    def __init__(self, *args, **kwargs):
        choice_a = 'backward*'
        choice_b = 'gunn'
        choice_c = 'IMPATT'
        choice_d = 'tunnel'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following diodes does not use negative resistance in its operation"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_181:
    def __init__(self, *args, **kwargs):
        choice_a = 'crystal diode'
        choice_b = 'schottky barrier diode'
        choice_c = 'backward diode'
        choice_d = 'PIN diode*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following is not used as a microwave mixer or detector"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_182:
    def __init__(self, *args, **kwargs):
        choice_a = 'tunnel*'
        choice_b = 'avalanche'
        choice_c = 'gunn'
        choice_d = 'IMPATT'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the following microwave diodes is suitable for very low-power oscillators only"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_183:
    def __init__(self, *args, **kwargs):
        choice_a = 'germanium'
        choice_b = 'gallium arsenide*'
        choice_c = 'silicon'
        choice_d = 'metal semiconductor junctions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The transferred-electron bulk effect occurs in"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_184:
    def __init__(self, *args, **kwargs):
        choice_a = 'alpha of the transistor falls by 3dB'
        choice_b = 'beta of the transistor falls by 3dB'
        choice_c = 'power gain of the transistor falls to unity'
        choice_d = 'beta of the transistor falls to unity*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The gain-bandwidth frequency of a microwave transistor, is the frequency at which the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_185:
    def __init__(self, *args, **kwargs):
        choice_a = 'collector voltage must be large'
        choice_b = 'collector current must be high'
        choice_c = 'base should be thin'
        choice_d = 'emitter area must be large*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a microwave transistor to operate at the highest frequencies, the (indicate the false answer)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_187:
    def __init__(self, *args, **kwargs):
        choice_a = 'traveling wave amplifier'
        choice_b = 'degenerative amplifier*'
        choice_c = 'lower sideband up-converter'
        choice_d = 'upper sideband down-converter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parametric amplifier has an input and output frequency of 2.25 GHz, and is pumped at 4.5 GHz. It is """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_186:
    def __init__(self, *args, **kwargs):
        choice_a = 'the resistive cutoff frequency must be high'
        choice_b = 'a small value of the base resistance is required'
        choice_c = 'a step-recovery diode must be used*'
        choice_d = 'a large range of capacitance variation is needed'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If higher-order frequency multiplication is required from a diode multiplier"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_188:
    def __init__(self, *args, **kwargs):
        choice_a = 'fi '
        choice_b = '2 fi'
        choice_c = 'fi - fp'
        choice_d = 'fp - fi*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A non-degenerate parametric amplifier has an input frequency "fi" and a pump frequency "fp". Then idler frequency is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_189:
    def __init__(self, *args, **kwargs):
        choice_a = 'provide a greater gain'
        choice_b = 'reduce the number of varactor diodes required'
        choice_c = 'avoid the need for cooling'
        choice_d = 'provide greater bandwidth*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Traveling-wave parametric amplifiers are used to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_190:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent noise feedback*'
        choice_b = 'allow the antenna to be used simultaneously for transmission and reception'
        choice_c = 'separated the signal and idler frequencies'
        choice_d = 'permit more efficient pumping'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parametric amplifier sometimes uses a circulator to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_191:
    def __init__(self, *args, **kwargs):
        choice_a = 'permit satisfactory high frequency operation'
        choice_b = 'yields a low noise figure*'
        choice_c = 'reduce the pump power required'
        choice_d = 'permits satisfactory'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The degenerate one-port parametric amplifier should"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_192:
    def __init__(self, *args, **kwargs):
        choice_a = 'has a tiny hole through its center to facilitate tunneling'
        choice_b = 'is a point-contact diode with very high reverse resistance'
        choice_c = 'uses a high doping level to provide a narrow junction*'
        choice_d = 'works by quantum tunneling exhibited by gallium arsenide only'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The tunnel diode"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_193:
    def __init__(self, *args, **kwargs):
        choice_a = 'increase the frequency stability*'
        choice_b = 'increase the available negative resistance'
        choice_c = 'facilitate tuning'
        choice_d = 'allow operation at the highest frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A tunnel diode is loosely coupled to its cavity in order to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_194:
    def __init__(self, *args, **kwargs):
        choice_a = 'is maximum at the peak point of the characteristic curve'
        choice_b = 'is available between the peak and valley points*'
        choice_c = 'is maximum at the valley point'
        choice_d = 'may be improved by the use of reverse bias'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The negative resistance in a tunnel diode"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_195:
    def __init__(self, *args, **kwargs):
        choice_a = 'lower noise'
        choice_b = 'higher ion mobility'
        choice_c = 'larger voltage swing*'
        choice_d = 'simpler fabrication process'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The biggest advantage of gallium antimonide over germanium for tunnel diode use is that the former has a """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_196:
    def __init__(self, *args, **kwargs):
        choice_a = 'electron transfer to a less mobile energy level*'
        choice_b = 'avalanche breakdown with the high voltag gradient'
        choice_c = 'tunneling across the junction'
        choice_d = 'electron domains forming at the junction'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Negative resistance is obtained with a Gunn diode because of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_197:
    def __init__(self, *args, **kwargs):
        choice_a = 'has a suitable empty energy band, which silicon does not have*'
        choice_b = 'has a higher ion mobility'
        choice_c = 'has a lower noise at the highest frequencies'
        choice_d = 'is capable of handling higher power densities'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For Gunn diodes, gallium arsenide is preferred to silicon because the former"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_198:
    def __init__(self, *args, **kwargs):
        choice_a = 'lower efficiency that that of the other microwave diodes'
        choice_b = 'high noise*'
        choice_c = 'inability to provide pulsed operation'
        choice_d = 'lower power-handling ability'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The biggest disadvantage of the IMPATT diode is its"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_199:
    def __init__(self, *args, **kwargs):
        choice_a = 'provide sharp focusing for the electron beam'
        choice_b = 'increase the population inversion'
        choice_c = 'allow room-temperature operation'
        choice_d = 'provide frequency adjustments*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The magnetic field is used with a ruby maser to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_200:
    def __init__(self, *args, **kwargs):
        choice_a = 'a much greater bandwidth*'
        choice_b = 'a better frequency stability'
        choice_c = 'a lower noise figure'
        choice_d = 'no need for a circulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The ruby maser has been preferred to the ammonia maser for microwave amplification, because the former has"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_201:
    def __init__(self, *args, **kwargs):
        choice_a = 'must have pumping'
        choice_b = 'are extremely low-noise amplifiers'
        choice_c = 'must be cooled down to a few kelvins*'
        choice_d = 'generally required circulators, since they are one-port devices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Parametric amplifiers and masers are similar to each other in that both (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_202:
    def __init__(self, *args, **kwargs):
        choice_a = 'radio astronomy'
        choice_b = 'satellite communications'
        choice_c = 'radar*'
        choice_d = 'troposcatter receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A maser RF amplifier is not really suitable for """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_203:
    def __init__(self, *args, **kwargs):
        choice_a = 'does not require pumping'
        choice_b = 'needs no resonator'
        choice_c = 'is not an oscillator*'
        choice_d = 'produces much lower powers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The ruby laser differs from the ruby maser in that the former"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_204:
    def __init__(self, *args, **kwargs):
        choice_a = 'infrared'
        choice_b = 'polarized'
        choice_c = 'narrow-beam'
        choice_d = 'single-frequency*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The output from a laser is monochromaticl this means that it is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_205:
    def __init__(self, *args, **kwargs):
        choice_a = 'using cooling'
        choice_b = 'using Q spoiling*'
        choice_c = 'increasing the magnetic field'
        choice_d = 'dispensing with the Fabry-Perot resonator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a given average power, the peak output power of a ruby laser may be increased by"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_206:
    def __init__(self, *args, **kwargs):
        choice_a = 'ensure that the beam does not spread'
        choice_b = 'prevent atmospheric interference*'
        choice_c = 'prevent interference by other laser'
        choice_d = 'ensure that people are not blinded by them'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Communications lasers are used with optical fiber, rather than in open links, to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_207:
    def __init__(self, *args, **kwargs):
        choice_a = 'monochromatic ouput'
        choice_b = 'higher power output'
        choice_c = 'lower cost*'
        choice_d = 'ability to be pulsed at higher rates'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement. The advantages of semiconductor lasers over LEDs include"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_208:
    def __init__(self, *args, **kwargs):
        choice_a = 'Morse*'
        choice_b = 'Baudot'
        choice_c = 'CCITT-2'
        choice_d = 'ARQ'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following is not a binary code"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_209:
    def __init__(self, *args, **kwargs):
        choice_a = '2'
        choice_b = 'log_10 (16)'
        choice_c = '8'
        choice_d = '4*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To permit the selection of 1 out of 16 equi-probable events, the number of bits required is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_210:
    def __init__(self, *args, **kwargs):
        choice_a = 'it would be too difficult for an operator to memorize'
        choice_b = 'it is redundant'
        choice_c = 'noise would introduce too many errors*'
        choice_d = 'too many pulses per letter are required'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A signaling system in which each letter of the alphabet is represented by a different symbol is not used because """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_211:
    def __init__(self, *args, **kwargs):
        choice_a = 'the maximum rate of information transmission depends on the channel bandwidth*'
        choice_b = 'the maximum rate of information transmission depends on the depth of modulation'
        choice_c = 'redundancy is essential'
        choice_d = 'only binary codes may be used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)


        self.question = f"""The Hartley states that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_212:
    def __init__(self, *args, **kwargs):
        choice_a = 'the channel bandwidth may be increased*'
        choice_b = 'redundancy may be used'
        choice_c = 'the transmitted power may be increased'
        choice_d = 'the signaling rate may be reduced'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the false statement. In order to combat noise"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_213:
    def __init__(self, *args, **kwargs):
        choice_a = 'frequency-shift keying*'
        choice_b = 'two-tone modulation'
        choice_c = 'pulse-code modulation'
        choice_d = 'single-tone modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The most common modulation system used for telegraphy is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_214:
    def __init__(self, *args, **kwargs):
        choice_a = 'by differentiating pulse-position modulation'
        choice_b = 'with a monostable*'
        choice_c = 'by integrating the signal'
        choice_d = 'with a free-running multivibrator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Pulse-width modulation system used for telegraphy"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_215:
    def __init__(self, *args, **kwargs):
        choice_a = 'pulse-position modulation'
        choice_b = 'pulse-code modulation*'
        choice_c = 'pulse-width modulation'
        choice_d = 'pulse-frequency modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following system is digital"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_216:
    def __init__(self, *args, **kwargs):
        choice_a = 'time-division multiplex'
        choice_b = 'frequency-division multiplex'
        choice_c = 'pulse-code modulation*'
        choice_d = 'pulse-width modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Quantizing noise occurs in"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_217:
    def __init__(self, *args, **kwargs):
        choice_a = 'SSB, suppressed-carrier'
        choice_b = 'frequency modulation'
        choice_c = 'pulse-position modulation'
        choice_d = 'pulse-code modulation*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The modulation system inherently most noise resistant is """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_218:
    def __init__(self, *args, **kwargs):
        choice_a = 'increase the number of standard amplitudes*'
        choice_b = 'send pulses whose sides are more nearly vertical'
        choice_c = 'use an RF amplifier in the receiver'
        choice_d = 'increase the number of samples per second'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In order to reduce quantizing noise, one must"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_219:
    def __init__(self, *args, **kwargs):
        choice_a = 'highest frequency that may be sent over a given channel'
        choice_b = 'maximum capacity of a channel with a given noise level*'
        choice_c = 'maximum number of coding levels in a channel with a given noise level'
        choice_d = 'maximum number of quantizing levels in a channel of a given bandwidth'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The Hartley-Shannon theorem sets a limit on the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_220:
    def __init__(self, *args, **kwargs):
        choice_a = 'PCM'
        choice_b = 'differential PCM'
        choice_c = 'PWM*'
        choice_d = 'delta modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following pulse modulation systems is analog"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_221:
    def __init__(self, *args, **kwargs):
        choice_a = 'to overcome quantizing noise in PCM'
        choice_b = 'in PCM transmitters, to allow amplitude limiting in the receivers'
        choice_c = 'to protect small signals in PCM from quantizing distortion*'
        choice_d = 'in PCM receivers, to overcome impulse noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Companding is used"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_222:
    def __init__(self, *args, **kwargs):
        choice_a = 'its inability to handle analog signals'
        choice_b = 'the high error rate which its quantizing noise introduces'
        choice_c = 'its incompatibility with TDM'
        choice_d = 'the large bandwidths that are required for it*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The biggest disadvantage of PCM"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_223:
    def __init__(self, *args, **kwargs):
        choice_a = 'do not provide a continuous set of values'
        choice_b = 'represent values as discrete steps'
        choice_c = 'can utilize decimal or binary systems'
        choice_d = 'all of the choices*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Digital signals"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_224:
    def __init__(self, *args, **kwargs):
        choice_a = 'design of the ENIAC computer'
        choice_b = 'development of the Hollerith code'
        choice_c = 'development of the transistor*'
        choice_d = 'development of disk drives for data storage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The event which marked the start of the modern computer age was"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_225:
    def __init__(self, *args, **kwargs):
        choice_a = 'is always equal to the bit transfer rate'
        choice_b = 'is equal to twice the bandwidth of an ideal channel*'
        choice_c = 'is not equal to the signaling rate'
        choice_d = 'is equal to one-half the bandwidth of an ideal channel'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The baud rate"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_226:
    def __init__(self, *args, **kwargs):
        choice_a = 'refers to distortion'
        choice_b = 'defines bandwidth'
        choice_c = 'describes signaling rates'
        choice_d = 'refers to noise*'
        

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The Shannon-Hartley law """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_227:
    def __init__(self, *args, **kwargs):
        choice_a = 'Baudot'
        choice_b = 'ASCII*'
        choice_c = 'EBCDIC'
        choice_d = 'CCITT-2'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The code which provides for parity checks is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_228:
    def __init__(self, *args, **kwargs):
        choice_a = 'requiring partial retransmission of the signal'
        choice_b = 'requiring retransmission of the entire signal'
        choice_c = 'requiring no part of the signal to be retransmitted*'
        choice_d = 'using parity to correct the errors in all cases'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A forward error correcting code corrects errors by"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_229:
    def __init__(self, *args, **kwargs):
        choice_a = 'requires two pairs'
        choice_b = 'can transfer data in both directions at once'
        choice_c = 'requires modems at both ends of the circuit'
        choice_d = 'all of the above*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Full duplex operation"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_230:
    def __init__(self, *args, **kwargs):
        choice_a = 'interconnects data sets and transmission circuit*'
        choice_b = 'uses several different connectors'
        choice_c = 'permits custom wiring of signal lines to the connector pins as desired'
        choice_d = 'all of the above'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The RS-232 interface"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_231:
    def __init__(self, *args, **kwargs):
        choice_a = 'improve the efficiency of data transfer'
        choice_b = 'are not used in data systems'
        choice_c = 'required additional lines'
        choice_d = 'are limited to small data networks*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Switching systems"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_232:
    def __init__(self, *args, **kwargs):
        choice_a = 'bytes per second'
        choice_b = 'baud rate'
        choice_c = 'bits per second*'
        choice_d = 'megahertz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The data transmission rate of a modem is measured in """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_233:
    def __init__(self, *args, **kwargs):
        choice_a = 'telegraph cables'
        choice_b = 'repeater amplifiers*'
        choice_c = 'HF radi'
        choice_d = 'geostationary satellites'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Broadband long distance communications were made possible by the advent of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_234:
    def __init__(self, *args, **kwargs):
        choice_a = 'frequency-division multiplex*'
        choice_b = 'time-division multiplex'
        choice_c = 'a group'
        choice_d = 'a supergroup'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A scheme in which several channels are interleaved and then transmitted together is known as """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_235:
    def __init__(self, *args, **kwargs):
        choice_a = 'occupies the frequency range from 60 to 108 kHz*'
        choice_b = 'consists of erect channels only'
        choice_c = 'is formed at the group translating equipment'
        choice_d = 'consists of five supergroups'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A basic group B"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_236:
    def __init__(self, *args, **kwargs):
        choice_a = 'can be used with PCM only'
        choice_b = 'combines five groups into a supergroup'
        choice_c = 'stacks 24 channels in adjacent frequency slots'
        choice_d = 'interleaves pulses belonging to different transmissions*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Time-division multiplex"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_237:
    def __init__(self, *args, **kwargs):
        choice_a = 'whether separate tubes are used for the two directions of transmission'
        choice_b = 'the bandwidth of the system*'
        choice_c = 'the number of coaxial cables in the tube'
        choice_d = 'the separation of the equalizers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The number of repeaters along a coaxial cable link depends on"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_238:
    def __init__(self, *args, **kwargs):
        choice_a = 'applied at each multiplexing bay'
        choice_b = 'used to regulate the gain of individual repeaters'
        choice_c = 'applied at each adjustable equalizer'
        choice_d = 'fed in at the GTE*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A supergroup pilot"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_239:
    def __init__(self, *args, **kwargs):
        choice_a = 'because of atmospheric attenuation'
        choice_b = 'because of output tube power limitations'
        choice_c = 'because of the Earth\'s curvature*'
        choice_d = 'to ensure that the applied dc voltage is not excessive'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Microwave link repeaters are typically 50 km apart"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_240:
    def __init__(self, *args, **kwargs):
        choice_a = 'they have less overall phase distortion*'
        choice_b = 'they are cheaper'
        choice_c = 'of the greater bandwidths'
        choice_d = 'of their relative immunity to impulse noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Microwave links are generally preferred to coaxial cable for television transmission because"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_241:
    def __init__(self, *args, **kwargs):
        choice_a = 'to protect the cable at greate depths'
        choice_b = 'to prevent inadvertent ploughing-in of the cable'
        choice_c = 'for the shallow shore ends of the cable*'
        choice_d = 'to prevent insulation breakdown from the high feed voltages'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Armored submarine cable is used"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_242:
    def __init__(self, *args, **kwargs):
        choice_a = 'a dc power supply and a regulator'
        choice_b = 'filters for the two directions of transmission*'
        choice_c = 'multiplexing and demultiplexing equipement'
        choice_d = 'pilot injection pilot extraction equipment'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A submarine cable repeater contains, among other equipment"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_243:
    def __init__(self, *args, **kwargs):
        choice_a = 'is motionless in space (except for its spin)'
        choice_b = 'is not really stationary at all, but orbits the Earth within a 24 - hr period*'
        choice_c = 'appears stationary over the Earth\'s magnetic pole'
        choice_d = 'is located at a height of 35,800 km to ensure global coverage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A geostationary satellite"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_244:
    def __init__(self, *args, **kwargs):
        choice_a = 'If two earth stations do not face a common satellite, they should communicate via a double-satellite hop.'
        choice_b = 'Satellites are allocated so that it is impossible for two earth stations not to face the same satellite'
        choice_c = 'collocated earth stations are used for frequency diversity'
        choice_d = 'A satellite earth station must have as many receive chains as there are carriers transmitted to it*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate the correct statement regarding satellite communications"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_245:
    def __init__(self, *args, **kwargs):
        choice_a = 'Comsat'
        choice_b = 'Domsat'
        choice_c = 'Marisat'
        choice_d = 'Intelsat*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Satellite used for intercontiniental communications are known as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_246:
    def __init__(self, *args, **kwargs):
        choice_a = 'language digits'
        choice_b = 'access digits'
        choice_c = 'area codes*'
        choice_d = 'central office codes'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Identical telephone numbers in different parts of a country are distinguished by their"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_247:
    def __init__(self, *args, **kwargs):
        choice_a = 'with echo cancellers'
        choice_b = 'by the relative congestion'
        choice_c = 'in terms of grade of service'
        choice_d = 'in erlangs*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Telephone traffic is measured"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_248:
    def __init__(self, *args, **kwargs):
        choice_a = 'AND gates*'
        choice_b = 'bandpass filters'
        choice_c = 'differentiation'
        choice_d = 'integration'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In order to separate channels in a TDM receiver, it is necessary to use"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_249:
    def __init__(self, *args, **kwargs):
        choice_a = 'AND gates'
        choice_b = 'bandpass filters*'
        choice_c = 'differentiation'
        choice_d = 'integration'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To separate channels in an FDM receiver, it is necessary to use"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_250:
    def __init__(self, *args, **kwargs):
        choice_a = 'dividing pulse widths*'
        choice_b = 'using the A-law'
        choice_c = 'using the mu-law'
        choice_d = 'forming supermastergroups'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Higher order TDM level are obtained by"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_251:
    def __init__(self, *args, **kwargs):
        choice_a = 'impurities'
        choice_b = 'microbending'
        choice_c = 'attenuation in the glass'
        choice_d = 'stepped index operation*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Losses in optical fibers can be caused by (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_252:
    def __init__(self, *args, **kwargs):
        choice_a = 'the attenuation is higher than that at 0.85 um'
        choice_b = 'the attenuation is higher than that at 1.3 um'
        choice_c = 'suitable laser devices have not yet been developed'
        choice_d = 'it does not lend itself to wave*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The 1.55 um window is not hyet in use in fiber optic systems because"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_253:
    def __init__(self, *args, **kwargs):
        choice_a = 'TAT-7'
        choice_b = 'INTELSAT V*'
        choice_c = 'ATLANTIS'
        choice_d = 'CANTAT 2'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following is not a submarine cable"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_254:
    def __init__(self, *args, **kwargs):
        choice_a = 'INTELSAT'
        choice_b = 'COMSAT'
        choice_c = 'TELSTAR'
        choice_d = 'INMARSAT'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following is an American domsat system"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_255:
    def __init__(self, *args, **kwargs):
        choice_a = '2*'
        choice_b = '4'
        choice_c = '8'
        choice_d = '16'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the peak transmitted power in a radar system is increased by a factor of 16, the maximum range will be increased by a factor """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_256:
    def __init__(self, *args, **kwargs):
        choice_a = 'sqrt(2)'
        choice_b = '2'
        choice_c = '4*'
        choice_d = '8'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the antenna diameter in a radar system is increased by a factor of 4, the maximum range will be increased by a factor of """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_257:
    def __init__(self, *args, **kwargs):
        choice_a = 'large maximum range'
        choice_b = 'good target discrimination'
        choice_c = 'difficult target acquisition'
        choice_d = 'increased capture area*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the ratio of the antenna diameter to the wavelength in a radar system is high this will reslut in (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_258:
    def __init__(self, *args, **kwargs):
        choice_a = 'depends on the frequency used'
        choice_b = 'may be reduced by special coating of the target'
        choice_c = 'depends on the aspect of a traget, if this is non-spherical'
        choice_d = 'is equal to the actual cross-sectional area for small targets*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The radar cross section of a target (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class kennedy_259:
    def __init__(self, *args, **kwargs):
        choice_a = 'allow a good minimum range'
        choice_b = 'make the returned echoes easier to distinguish from noise*'
        choice_c = 'prevent frequency changes in the magnetron'
        choice_d = 'allow accurate range measurements'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Flat-topped rectangular pulses must be transmitted in radar to (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_260:
    def __init__(self, *args, **kwargs):
        choice_a = 'make the returned eachoes easier to distinguish from noise'
        choice_b = 'make the target tracking easier with conical scanning'
        choice_c = 'increase the maximum range*'
        choice_d = 'have no effect on the range resolution'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A high PRF will (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_261:
    def __init__(self, *args, **kwargs):
        choice_a = 'pulse width*'
        choice_b = 'pulse repetition frequency'
        choice_c = 'pulse interval'
        choice_d = 'square root of the peak transmitted power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The IF bandwidth of a radar receiver is inversely proportional to the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_262:
    def __init__(self, *args, **kwargs):
        choice_a = 'it will interfere with the operation of the transmitter'
        choice_b = 'the receiver might be overloaded'
        choice_c = 'it will not be received'
        choice_d = 'the target will appear closer than it really is*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the reuturn echo arrives after the allocated pulse interval"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_263:
    def __init__(self, *args, **kwargs):
        choice_a = 'nodding'
        choice_b = 'spiral'
        choice_c = 'conical*'
        choice_d = 'helical'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""After a target has been acquired, the best scanning system for tracking is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_264:
    def __init__(self, *args, **kwargs):
        choice_a = 'lobe switching '
        choice_b = 'sequential lobing'
        choice_c = 'conical scanning'
        choice_d = 'monopulse*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the target cross section is changing, the best system for accurate tracking is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_265:
    def __init__(self, *args, **kwargs):
        choice_a = 'it does not gice the target velocity'
        choice_b = 'it does not give the target range*'
        choice_c = 'a transponder is required at the target'
        choice_d = 'it does not give the target position'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The biggest disadvantage of CW Doppler radar is that"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_266:
    def __init__(self, *args, **kwargs):
        choice_a = 'the target position and range'
        choice_b = 'the target range, but not position*'
        choice_c = 'the target position, but not range'
        choice_d = 'neither range nor position, but not only velocity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The A scope displays"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_267:
    def __init__(self, *args, **kwargs):
        choice_a = 'moving target plotting in the PPI*'
        choice_b = 'the MTI system'
        choice_c = 'FM radar'
        choice_d = 'CW radar'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The Doppler effect is used in (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_268:
    def __init__(self, *args, **kwargs):
        choice_a = 'intermediate frequency*'
        choice_b = 'transmitted frequency'
        choice_c = 'received frequency'
        choice_d = 'pulse repetition frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""THe coho in MTI radar operates at the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_269:
    def __init__(self, *args, **kwargs):
        choice_a = 'help in subtracting a complete scan from the previous scan*'
        choice_b = 'match the phase of the coho and the stalo'
        choice_c = 'match the phase of the coho and the output oscillator'
        choice_d = 'delay a sweep so that the next sweep can be subtracted from it'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""THe function of the quartz delay line in an MTI radar is to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_270:
    def __init__(self, *args, **kwargs):
        choice_a = 'to change the Doppler frequency'
        choice_b = 'to vary the PRF*'
        choice_c = 'to use monopulse'
        choice_d = 'to use MTI'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""THe solution to the 'blind speed' problem is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_271:
    def __init__(self, *args, **kwargs):
        choice_a = 'target identification'
        choice_b = 'navigation'
        choice_c = 'very significant extension of the maximum range'
        choice_d = 'more accurate tracking of enemy targets*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which one of the following applications or advantages of radar beacons is false"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_272:
    def __init__(self, *args, **kwargs):
        choice_a = 'very fast scanning'
        choice_b = 'ability to track and scan simultaneously'
        choice_c = 'circuit simplicity*'
        choice_d = 'ability to track many targets simultaneously'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Compared with other types of radar, phase array radar has the following advantages (indicate the false statement)"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_273:
    def __init__(self, *args, **kwargs):
        choice_a = '262.5*'
        choice_b = '525'
        choice_c = '30'
        choice_d = '60'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The number of lines per field in the United States TV system is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_274:
    def __init__(self, *args, **kwargs):
        choice_a = '60'
        choice_b = '262.5'
        choice_c = '4.5'
        choice_d = '30*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The number of frames per second in the United States TV system is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_275:
    def __init__(self, *args, **kwargs):
        choice_a = '31500'
        choice_b = '15750'
        choice_c = '262.5'
        choice_d = '525*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The number of lines per second in the United States TV system is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_276:
    def __init__(self, *args, **kwargs):
        choice_a = '41.25'
        choice_b = '6*'
        choice_c = '4.5'
        choice_d = '3.58'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The channel width in the United States TV system, in MHz, is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_277:
    def __init__(self, *args, **kwargs):
        choice_a = 'produce the illusion of motion'
        choice_b = 'ensure that all the lines on the screen are scanned, not merely the alternate ones'
        choice_c = 'simplify the vertical sync pulse train'
        choice_d = 'avoid flicker*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Interlacing is used in television to"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_278:
    def __init__(self, *args, **kwargs):
        choice_a = 'sync*'
        choice_b = 'chroma'
        choice_c = 'luminance'
        choice_d = 'video'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The signals sent by the TV transmitter to ensure correct scanning in the receiver are called"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_279:
    def __init__(self, *args, **kwargs):
        choice_a = '3.58'
        choice_b = '3.579545'
        choice_c = '4.5*'
        choice_d = '45.75'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the United States color television system, the intercarrier frequency, in MHz is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_280:
    def __init__(self, *args, **kwargs):
        choice_a = 'sync'
        choice_b = 'video'
        choice_c = 'sweep*'
        choice_d = 'sound'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which voltages are not found in the output of a normal monochrome receiver video detector"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_281:
    def __init__(self, *args, **kwargs):
        choice_a = 'sound carrier'
        choice_b = 'chroma carrier'
        choice_c = 'intercarrier'
        choice_d = 'picture carrier*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The carrier transmitted 1.25 MHz above the bottom frequency in the United States TV channel is the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_282:
    def __init__(self, *args, **kwargs):
        choice_a = 'interlace ratio'
        choice_b = 'maximum horizontal deflection'
        choice_c = 'aspect ratio*'
        choice_d = 'ratio of the two diagonals'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In television, 4:3 represents"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_283:
    def __init__(self, *args, **kwargs):
        choice_a = 'horizontal blanking'
        choice_b = 'vertical blanking*'
        choice_c = 'the serrations'
        choice_d = 'the horizontal retrace'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Equalizing pulses in TV are sent during"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_284:
    def __init__(self, *args, **kwargs):
        choice_a = 'done to assist interlace*'
        choice_b = 'purely an accident'
        choice_c = 'to ensure that line and frame frequencies can be obtained from the same original source'
        choice_d = 'done to minimize interference with the chroma subcarrier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An odd number of lines per frame forms part of every one of the world's TV systems. This is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_285:
    def __init__(self, *args, **kwargs):
        choice_a = 'equalize the charge in the integrator before the start of vertical retrace'
        choice_b = 'help vertical synchronization'
        choice_c = 'help horizontal synchronization*'
        choice_d = 'simplify the generation of the vertical sync pulse'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The function of the serrations in the composite video waveform is to """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_286:
    def __init__(self, *args, **kwargs):
        choice_a = '21H'
        choice_b = '3H*'
        choice_c = 'H'
        choice_d = '0.5H'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The width of the vertical sync pulse in the United States"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_287:
    def __init__(self, *args, **kwargs):
        choice_a = '4.5 MHz*'
        choice_b = '41.25 MHz'
        choice_c = '45.75 MHz'
        choice_d = '42.17 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following frequencies will not be found in the output of a normal TV receiver tuner"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_288:
    def __init__(self, *args, **kwargs):
        choice_a = 'between grid and ground'
        choice_b = 'to the yoke'
        choice_c = 'to the anode'
        choice_d = 'between grid and cathode*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The video voltage applied to the picture tube of a television receiver is fed in"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_289:
    def __init__(self, *args, **kwargs):
        choice_a = 'the keyed AGC amplifier'
        choice_b = 'a clipper*'
        choice_c = 'an integrator'
        choice_d = 'a differentiator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The circuit that separates sync pulses from the composite video waveform"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_290:
    def __init__(self, *args, **kwargs):
        choice_a = 'direct current'
        choice_b = 'amplified vertical sync'
        choice_c = 'a sawtooth voltage'
        choice_d = 'a sawtooth current*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The output of the vertical amplifier, applied to the yoke in a TV receiver, consists of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_291:
    def __init__(self, *args, **kwargs):
        choice_a = 'mains transformer'
        choice_b = 'vertical output stage'
        choice_c = 'horizontal output stage*'
        choice_d = 'horizontal deflection oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The HV anode supply for the picture tube of a TV receiver is generated in the """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_292:
    def __init__(self, *args, **kwargs):
        choice_a = 'ringing'
        choice_b = 'burst'
        choice_c = 'damper'
        choice_d = 'flyback*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Another name for the horizontal retrace in a TV receiver is the"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_293:
    def __init__(self, *args, **kwargs):
        choice_a = 'Y'
        choice_b = 'Q'
        choice_c = 'R*'
        choice_d = 'I'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Indicate which of the following signals is not transmitted in color TV"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_294:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduce x-ray emission'
        choice_b = 'ensure that each beam hits only its own dots*'
        choice_c = 'increase screen brightness'
        choice_d = 'provide degaussing for the screen'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The shadow mask in a color picture tube is used to """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_295:
    def __init__(self, *args, **kwargs):
        choice_a = 'cuts off the chroma stages during monochrome reception*'
        choice_b = 'endsures that no color is transmitted to monochrome receivers'
        choice_c = 'prevents color overloading'
        choice_d = 'makes sure that the color burst is not mistaken for sync pulses, by cutting off reception during the back porch'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a TV receiver, the color killer"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_296:
    def __init__(self, *args, **kwargs):
        choice_a = 'approximately 0.5 MHz'
        choice_b = 'approximately 1.0 MHz*'
        choice_c = 'approximately 40 GHz'
        choice_d = 'none of the choices'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the frequency limit of copper wire?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_297:
    def __init__(self, *args, **kwargs):
        choice_a = '20 GHz*'
        choice_b = '1 MHz'
        choice_c = '100 MHz'
        choice_d = '40 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately what is the frequency limit of the optical fiber?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_298:
    def __init__(self, *args, **kwargs):
        choice_a = 'a pair of copper conductors'
        choice_b = 'a 1500-pair cable*'
        choice_c = 'a 500-pair cable'
        choice_d = 'a 1000-pair cable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A single fiber can handle as many voice channels as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_299:
    def __init__(self, *args, **kwargs):
        choice_a = 'a light ray reflected from a flat surface'
        choice_b = 'a light ray directed toward a surface*'
        choice_c = 'a diffused light ray'
        choice_d = 'a light ray that happens periodically'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An incident ray may be defined as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_300:
    def __init__(self, *args, **kwargs):
        choice_a = 'separating light into its component frequencies*'
        choice_b = 'reflecting light from a smooth surface'
        choice_c = 'the process by which light is absorbed by an uneven rough surface'
        choice_d = 'light scattering'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The term dispersion describes the process of"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_301:
    def __init__(self, *args, **kwargs):
        choice_a = 'photon energy changes with wavelength'
        choice_b = 'light is refracted a function of surface smoothness'
        choice_c = 'the angle is determined partly by a and b'
        choice_d = 'the angle is determined by the index of the materials*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following terms describes the reason that light is refracted at different angles"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_302:
    def __init__(self, *args, **kwargs):
        choice_a = 'the point at which light is refracted'
        choice_b = 'the point at which light becomes invisible'
        choice_c = 'the point at which light has gone from the refractive mode to the reflective mode*'
        choice_d = 'the point at which light has crossed the boundary layers from one index to another'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The term critical angle describes"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_303:
    def __init__(self, *args, **kwargs):
        choice_a = 'is used to reduce optical interference'
        choice_b = 'is used to protect the fiber'
        choice_c = 'acts to help guide the light to in the core*'
        choice_d = 'ensures that the refractive index remains constant'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The cladding which surrounds the fiber core"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_304:
    def __init__(self, *args, **kwargs):
        choice_a = 'a number which compares the transparency of a material with of air*'
        choice_b = 'a number assigned by the manufacture to the fiber in qusetion'
        choice_c = 'a number which determines the core diameter'
        choice_d = 'a term for describes core elasticity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The reflective index number is"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_305:
    def __init__(self, *args, **kwargs):
        choice_a = 'the number of fibers placed into a fiber-optic cable'
        choice_b = 'the number of voice channels each fiber can support'
        choice_c = 'the number of wavelengths each fiber can support*'
        choice_d = 'the index number'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The terms single mode and multimode are best described as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_306:
    def __init__(self, *args, **kwargs):
        choice_a = 'the lower the speed of light*'
        choice_b = 'the higher the speed of light'
        choice_c = 'has no effect on the speed of light'
        choice_d = 'the shorter the wavelength propagation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The higher the index number"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_307:
    def __init__(self, *args, **kwargs):
        choice_a = 'the components, the data rate and response time'
        choice_b = 'the source, the link, and the receiver'
        choice_c = 'the transmitter, the cable, and the receiver'
        choice_d = 'the source, the link, and the detector*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The three major groups in the optical system are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_308:
    def __init__(self, *args, **kwargs):
        choice_a = '1.5 dB'
        choice_b = '0.1 dB'
        choice_c = '0.5 dB*'
        choice_d = '0.001 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As light is coupled in t multipoint reflective device, the power is reduced by"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_309:
    def __init__(self, *args, **kwargs):
        choice_a = 'source power'
        choice_b = 'fiber attenuation'
        choice_c = 'connector and splice losses'
        choice_d = 'detector sensitivity*'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When connector losses, splice losses, and coupler losses are added, what is the final limiting factor?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_310:
    def __init__(self, *args, **kwargs):
        choice_a = 'the time required for the signal to go from 10 to 90 percent of maximum amplitude'
        choice_b = 'the ratio of the diode output current to optical input power*'
        choice_c = 'the ratio of output current to output power'
        choice_d = 'the ratio of output current to input current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The term responsivity as it applies to a light detector is best described as"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_311:
    def __init__(self, *args, **kwargs):
        choice_a = '1:10*'
        choice_b = '10:1'
        choice_c = '20:1'
        choice_d = '1:20'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Loss comparisons between fusion splices and mechanical splices are"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_312:
    def __init__(self, *args, **kwargs):
        choice_a = 'quicker installation under ideal conditions'
        choice_b = 'minimum attenuation losses'
        choice_c = 'field service conditions*'
        choice_d = 'situations in which cost of equipment is not a factor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The mechanical splice is best suited for"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class kennedy_313:
    def __init__(self, *args, **kwargs):
        choice_a = '70 percent of the core diameter and 70% of the fiber NA should be filled with light*'
        choice_b = '70 percent of the fiber diameter and 70% of the cone of acceptance should be filled with light'
        choice_c = '70 percent of the input light should be measured at the output'
        choice_d = '70 percent of the unwanted wavelengths should be attenuated by the fiber'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""EMD is best described by which statement?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""