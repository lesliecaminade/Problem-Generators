# import random_handler as ran
import math
import random
# import constants_conversions as c
# import interpolation
#import sympy as sym

#x, y, z, t = sym.symbols('x y z t', real = True)


class f_1_199:
    def __init__(self, *args, **kwargs):
        choice_a = 'peak-envelope power*'
        choice_b = 'mean power'
        choice_c = 'carrier power'
        choice_d = 'full power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The power supplied to the antenna transmission line by a transmitter during an RF cycle at the highest crest of the modulation envelope is known as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_200:
    def __init__(self, *args, **kwargs):
        choice_a = 'PEP*'
        choice_b = 'PIV'
        choice_c = 'ERP'
        choice_d = 'power factor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To compute one of the following, multiply the peak-envelope voltage by 0.707 to obtain the RMS value, square the result and divide by the load resistance. Which is the correct answer?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_201:
    def __init__(self, *args, **kwargs):
        choice_a = 'Peak-Envelope Voltage (PEV) multiplied by 0.707, squared and divided by the load resistance*'
        choice_b = 'peak-voltage multiplied by peak current'
        choice_c = 'equal to the RMS power'
        choice_d = 'a hypothetical measurement'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Peak-Envelope Power (PEP) for SSB transmission is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_202:
    def __init__(self, *args, **kwargs):
        choice_a = 'P = (E exponent 2) /R*'
        choice_b = 'P = EI/R'
        choice_c = 'P = EI cos 0'
        choice_d = 'P = IR'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The formula to be used to calculate the power output of a transmitter into a resistor load using a voltmeter is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_203:
    def __init__(self, *args, **kwargs):
        choice_a = 'PEP = [(0.707 PEV)(0.707 PEV)] / RL*'
        choice_b = 'PEP = [(Vp)(Vp)] / (RL)'
        choice_c = 'PEP = (Vp)(Vp)(RL)'
        choice_d = 'PEP = [(1.414 PEV)(1.414 PEV)] / RL'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How is the output Peak-Envelope Power of a transmitter calculated if an oscilloscope is used to measure the Peak-Envelope Voltage across a dummy resistive load (where PEP = Peak-Envelope Power, PEV = Peak-Envelope Voltage, Vp = peak-voltage, RL = load resistance)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_204:
    def __init__(self, *args, **kwargs):
        choice_a = '100 watts*'
        choice_b = '400 watts'
        choice_c = '1000 watts'
        choice_d = '200 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the output PEP from a transmitter if an oscilloscope measures 200 volts peak-to-peak across a 50-ohm dummy load connected to the transmitter output?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_205:
    def __init__(self, *args, **kwargs):
        choice_a = '625 watts*'
        choice_b = '1250 watts'
        choice_c = '2500 watts'
        choice_d = '500 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the output PEP from a transmitter if an oscilloscope measures 500 volts peak-to-peak across a 50-ohm dummy load connected to the transmitter output?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_206:
    def __init__(self, *args, **kwargs):
        choice_a = '1060 watts*'
        choice_b = '2120 watts'
        choice_c = '1500 watts'
        choice_d = '530 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the output PEP of an unmodulated carrier transmitter if a wattmeter connected to the transmitter output indicates an average reading of 1060 watts?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_207:
    def __init__(self, *args, **kwargs):
        choice_a = '400 watts*'
        choice_b = '200 watts'
        choice_c = '600 watts'
        choice_d = '1000 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the output PEP from a transmitter, if an oscilloscope measures 400 volts peak-to-peak across a 50 ohm dummy load connected to the transmitter output?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_208:
    def __init__(self, *args, **kwargs):
        choice_a = '1600 watts*'
        choice_b = '800 watts'
        choice_c = '6400 watts'
        choice_d = '3200 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the output PEP from a transmitter, if an oscilloscope measures 800 volts peak-to-peak across a 50 ohm dummy load connected to the transmitter output?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_209:
    def __init__(self, *args, **kwargs):
        choice_a = '625 watts*'
        choice_b = '427.5 watts'
        choice_c = '884 watts'
        choice_d = '442 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An oscilloscope measures 500 volts peak-to-peak across a 50 ohm dummy load connected to the transmitter output during unmodulated carrier conditions. What would an average-reading power meter indicate under the same transmitter conditions?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_210:
    def __init__(self, *args, **kwargs):
        choice_a = 'A variable frequency oscillator with metered feedback current*'
        choice_b = 'An SWR meter'
        choice_c = 'A marker generator'
        choice_d = 'A field-strength meter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a dip meter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_211:
    def __init__(self, *args, **kwargs):
        choice_a = 'It gives an indication of the resonant frequency of a circuit*'
        choice_b = 'It measures transmitter output power accurately'
        choice_c = 'It measures field strength accurately'
        choice_d = 'It measures frequency accurately'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does a dip meter do?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_212:
    def __init__(self, *args, **kwargs):
        choice_a = 'To measure resonant frequencies of antenna traps and to measure a tuned circuit resonant frequency*'
        choice_b = 'To measure antenna resonance and impedance'
        choice_c = 'To measure antenna resonance and percentage modulation'
        choice_d = 'To measure resonant frequency of antenna traps and percentage modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What two ways could a dip meter be used in an amateur station?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_213:
    def __init__(self, *args, **kwargs):
        choice_a = 'the resonant frequency of a circuit*'
        choice_b = 'the calibration of an absorption-type wavemeter'
        choice_c = 'the impedance mismatch in a circuit'
        choice_d = 'the adjustment of an inductor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A dip meter supplies the radio frequency energy which enables you to check:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_214:
    def __init__(self, *args, **kwargs):
        choice_a = 'measure the value of capacitance or inductance*'
        choice_b = 'align transmitter-tuned circuits'
        choice_c = 'determine the frequency of oscillations'
        choice_d = 'align receiver-tuned circuits'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A dip meter may not be used directly to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_215:
    def __init__(self, *args, **kwargs):
        choice_a = 'reads accurately only when the attenuator is properly terminated*'
        choice_b = 'always reads the true output of the signal generator'
        choice_c = 'reads twice the true output when the attenuator is properly terminated'
        choice_d = 'reads half the true output when the attenuator is properly terminated'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The dial calibration on the output attenuator of a signal generator:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_216:
    def __init__(self, *args, **kwargs):
        choice_a = 'A high-stability oscillator which can produce a wide range of frequencies and amplitudes*'
        choice_b = 'A low-stability oscillator which sweeps through a range of frequencies'
        choice_c = 'A low-stability oscillator used to inject a signal into a circuit under test'
        choice_d = 'A high-stability oscillator which generates reference signals at exact frequency intervals'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a signal generator?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_217:
    def __init__(self, *args, **kwargs):
        choice_a = 'should be loosely coupled to the circuit under test*'
        choice_b = 'should be tightly coupled to the circuit under test'
        choice_c = 'may be used only with series tuned circuits'
        choice_d = 'accurately measures frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A dip meter:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_218:
    def __init__(self, *args, **kwargs):
        choice_a = 'Calibrated RF signal generator with FM tone modulation and total harmonic distortion (THD) analyzer*'
        choice_b = 'RF signal generator with FM tone modulation and a deviation meter'
        choice_c = 'Oscilloscope and spectrum analyzer'
        choice_d = 'Receiver noise bridge and total harmonic distortion analyser'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which two instruments are needed to measure FM receiver sensitivity for a 12 dB SINAD ratio (signal + noise + distortion over noise + distortion)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_219:
    def __init__(self, *args, **kwargs):
        choice_a = 'parallel tuned circuits*'
        choice_b = 'operational amplifier circuits'
        choice_c = 'digital logic circuits'
        choice_d = 'series tuned circuits'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The dip meter is most directly applicable to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_220:
    def __init__(self, *args, **kwargs):
        choice_a = 'Transmitter power output*'
        choice_b = 'Hand capacity'
        choice_c = 'Stray capacity'
        choice_d = 'Over coupling'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not a factor affecting the frequency accuracy of a dip meter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_221:
    def __init__(self, *args, **kwargs):
        choice_a = 'It makes frequency measurements*'
        choice_b = 'It measures frequency deviation'
        choice_c = 'It generates broad-band white noise for calibration'
        choice_d = 'It produces a reference frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does a frequency counter do?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_222:
    def __init__(self, *args, **kwargs):
        choice_a = 'Time base accuracy, speed of the logic, and time base stability*'
        choice_b = 'Time base accuracy, temperature coefficient of the logic and time base stability'
        choice_c = 'Number of digits in the readout, speed of the logic, and time base stability'
        choice_d = 'Number of digits in the readout, external frequency reference and temperature coefficient of the logic'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What factors limit the accuracy, frequency response and stability of a frequency counter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_223:
    def __init__(self, *args, **kwargs):
        choice_a = 'By increasing the accuracy of the time base*'
        choice_b = 'By using slower digital logic'
        choice_c = 'By using faster digital logic'
        choice_d = 'By improving the accuracy of the frequency response'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can the accuracy of a frequency counter be improved?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_224:
    def __init__(self, *args, **kwargs):
        choice_a = '14.652 Hz*'
        choice_b = '0.1 MHz'
        choice_c = '1.4652 Hz'
        choice_d = '1.4652 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a frequency counter with a time base accuracy of +/- 0.1 PPM (parts per million) reads 146 520 000 Hz, what is the most that the actual frequency being measured could differ from that reading?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_225:
    def __init__(self, *args, **kwargs):
        choice_a = '1465.2 Hz*'
        choice_b = '146.52 Hz'
        choice_c = '146.52 kHz'
        choice_d = '1465.2 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a frequency counter, with a time base accuracy of 10 PPM (parts per million) reads 146 520 000 Hz, what is the most the actual frequency being measured could differ from that reading?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_226:
    def __init__(self, *args, **kwargs):
        choice_a = 'crystal oscillator*'
        choice_b = 'self-oscillating Hartley oscillator'
        choice_c = 'mechanical tuning fork'
        choice_d = 'free-running multivibrator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The clock in a frequency counter normally uses a:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_227:
    def __init__(self, *args, **kwargs):
        choice_a = 'the characteristics of the internal time-base generator*'
        choice_b = 'the size of the frequency counter'
        choice_c = 'type of display used in the counter'
        choice_d = 'the number of digits displayed'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The frequency accuracy of a frequency counter is determined by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_228:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequency-marker generator*'
        choice_b = 'Signal generator'
        choice_c = 'Harmonic calibrator'
        choice_d = 'Frequency counter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which device relies on a stable low-frequency oscillator, with harmonic output, to facilitate the frequency calibration of receiver dial settings?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_229:
    def __init__(self, *args, **kwargs):
        choice_a = 'Zero-beat the crystal oscillator against a standard frequency station such as WWV*'
        choice_b = 'Compare the oscillator with your transmitter'
        choice_c = 'Use a dip-meter to determine the oscillator\'s fundamental frequency'
        choice_d = 'Compare the oscillator with your receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the traditional way of verifying the accuracy of a crystal calibrator?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_230:
    def __init__(self, *args, **kwargs):
        choice_a = 'voltage-controlled crystal oscillator (VCXO)*'
        choice_b = 'temperature compensated crystal oscillator (TCXO)'
        choice_c = 'oven-controlled crystal oscillator (OCXO)'
        choice_d = 'GPS disciplined oscillator (GPSDO)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Out of the following oscillators, one is NOT, by itself, considered a high-stability reference:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_231:
    def __init__(self, *args, **kwargs):
        choice_a = 'of a frequency as low as possible and with a period as long as possible*'
        choice_b = 'a combined frequency above both'
        choice_c = 'the mathematical mean of both frequencies'
        choice_d = 'at the highest audio frequency possible'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You want to calibrate your station frequency reference to the WWV signal on your receiver. The resulting beat tone must be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_232:
    def __init__(self, *args, **kwargs):
        choice_a = 'A looping pattern with 3 horizontal loops, and 2 vertical loops*'
        choice_b = 'A rectangular pattern 100 mm wide and 150 mm high'
        choice_c = 'An oval pattern 100 mm wide and 150 mm high'
        choice_d = 'A looping pattern with 100 horizontal loops and 150 vertical loops'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a 100 Hz signal is fed to the horizontal input of an oscilloscope and a 150 Hz signal is fed to the vertical input, what type of pattern should be displayed on the screen?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_233:
    def __init__(self, *args, **kwargs):
        choice_a = 'Accuracy of the time base and the linearity and bandwidth of the deflection amplifiers*'
        choice_b = 'Deflection amplifier output impedance and tube face frequency increments'
        choice_c = 'Accuracy and linearity of the time base and tube face voltage increments'
        choice_d = 'Tube face voltage increments and deflection amplifier voltages'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What factors limit the accuracy, frequency response and stability of an oscilloscope?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_234:
    def __init__(self, *args, **kwargs):
        choice_a = 'By increasing the horizontal sweep rate and the vertical amplifier frequency response*'
        choice_b = 'By using a crystal oscillator as the time base and increasing the vertical sweep rate'
        choice_c = 'By increasing the vertical sweep rate and the horizontal amplifier frequency response'
        choice_d = 'By using triggered sweep and a crystal oscillator for the timebase'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can the frequency response of an oscilloscope be improved?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_235:
    def __init__(self, *args, **kwargs):
        choice_a = 'utilizing a dual trace oscilloscope*'
        choice_b = 'measuring the input on the X axis and the output on the Y axis'
        choice_c = 'measuring the input on the X axis and the output on the Z axis'
        choice_d = 'measuring the input on the Y axis and the output on the X axis'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You can use an oscilloscope to display the input and output of a circuit at the same time by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_236:
    def __init__(self, *args, **kwargs):
        choice_a = 'determine FM carrier deviation directly*'
        choice_b = 'measure frequency'
        choice_c = 'measure DC voltage'
        choice_d = 'determine the amplitude of complex voltage wave forms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An oscilloscope cannot be used to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_237:
    def __init__(self, *args, **kwargs):
        choice_a = 'the highest frequency signal the scope can display*'
        choice_b = 'directly related to gain compression'
        choice_c = 'indirectly related to screen persistence'
        choice_d = 'a function of the time-base accuracy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The bandwidth of an oscilloscope is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_238:
    def __init__(self, *args, **kwargs):
        choice_a = 'a diagonal straight line*'
        choice_b = 'a horizontal straight line'
        choice_c = 'an ellipse'
        choice_d = 'a circle'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When using Lissajous figures to determine phase differences, an indication of zero or 180 degrees is represented on the screen of an oscilloscope by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_239:
    def __init__(self, *args, **kwargs):
        choice_a = '40 kHz*'
        choice_b = '20 kHz'
        choice_c = '50 kHz'
        choice_d = '30 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A 100-kHz signal is applied to the horizontal channel of an oscilloscope. A signal of unknown frequency is applied to the vertical channel. The resultant wave form has 5 loops displayed vertically and 2 loops horizontally. The unknown frequency is:
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_240:
    def __init__(self, *args, **kwargs):
        choice_a = 'every time the probe is used with a different oscilloscope*'
        choice_b = 'when measuring a sine wave'
        choice_c = 'through the addition of a high-value series resistor'
        choice_d = 'when measuring a signal whose frequency varies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An oscilloscope probe must be compensated:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_241:
    def __init__(self, *args, **kwargs):
        choice_a = 'An oscilloscope*'
        choice_b = 'A sidetone monitor'
        choice_c = 'A signal tracer and an audio amplifier'
        choice_d = 'A field-strength meter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the best instrument to use to check the signal quality of a CW or single-sideband phone transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_242:
    def __init__(self, *args, **kwargs):
        choice_a = 'The RF output of the transmitter through a sampling device*'
        choice_b = 'The RF signals of a nearby receiving antenna'
        choice_c = 'The IF output of a monitoring receiver'
        choice_d = 'The audio input of the transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the best signal source to connect to the vertical input of an oscilloscope for checking the quality of a transmitted signal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_330:
    def __init__(self, *args, **kwargs):
        choice_a = 'lack of neutralization*'
        choice_b = 'overdriven stages'
        choice_c = 'poor voltage regulation'
        choice_d = 'excessive harmonic production'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Parasitic oscillations in an RF power amplifier may be caused by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_331:
    def __init__(self, *args, **kwargs):
        choice_a = 'Double sideband, suppressed carrier*'
        choice_b = 'FM with balanced deviation'
        choice_c = 'Full carrier'
        choice_d = 'Single sideband, suppressed carrier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of signal does a balanced modulator produce?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_332:
    def __init__(self, *args, **kwargs):
        choice_a = 'By using a balanced modulator followed by a filter*'
        choice_b = 'By driving a product detector with a DSB signal'
        choice_c = 'By using a loop modulator followed by a mixer'
        choice_d = 'By using a reactance modulator followed by a mixer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can a single-sideband phone signal be produced?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_333:
    def __init__(self, *args, **kwargs):
        choice_a = 'the balanced modulator stage*'
        choice_b = 'the carrier decouple stage'
        choice_c = 'the mechanical filter'
        choice_d = 'the frequency multiplier stage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Carrier suppression in a single-sideband transmitter takes place in:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_334:
    def __init__(self, *args, **kwargs):
        choice_a = '6 dB gain in the transmitter and 3 dB gain in the receiver*'
        choice_b = '6 dB gain in the receiver'
        choice_c = 'a greater bandpass requirement in the receiver'
        choice_d = '3 dB gain in the transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Transmission with SSB, as compared to conventional AM transmission, results in:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_335:
    def __init__(self, *args, **kwargs):
        choice_a = 'twice the RF power output of any of the tones*'
        choice_b = 'equal to the RF peak output power of any of the tones'
        choice_c = 'one-half of the RF peak output power of any of the tones'
        choice_d = 'one-quarter of the RF peak output power of any of the tones'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The peak power output of a single-sideband transmitter, when being tested by a two-tone generator is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_336:
    def __init__(self, *args, **kwargs):
        choice_a = 'Two audio-frequency sine waves*'
        choice_b = 'An audio-frequency sine wave'
        choice_c = 'An audio-frequency square wave'
        choice_d = 'Normal speech'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of input signal is used to test the amplitude linearity of a single-sideband phone transmitter while viewing the output on an oscilloscope?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_337:
    def __init__(self, *args, **kwargs):
        choice_a = 'Two non-harmonically related tones are fed in, and the output is observed on an oscilloscope*'
        choice_b = 'Two harmonically related tones are fed in, and the output is observed on an oscilloscope'
        choice_c = 'Two harmonically related tones are fed in, and the output is observed on a distortion analyzer'
        choice_d = 'Two non-harmonically related tones are fed in, and the output is observed on a distortion analyzer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When testing the amplitude linearity of a single-sideband transmitter what audio tones are fed into the microphone input and on what kind of kind of instrument is the output observed?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_338:
    def __init__(self, *args, **kwargs):
        choice_a = 'Any two audio tones may be used, but they must be within the transmitter audio passband, and should not be harmonically related*'
        choice_b = '20 Hz and 20 kHz tones must be used'
        choice_c = '1200 Hz and 2400 Hz tones must be used'
        choice_d = 'Any two audio tones may be used, but they must be within the transmitter audio passband, and must be harmonically related'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What audio frequencies are used in a two-tone test of the linearity of a single-sideband phone transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_339:
    def __init__(self, *args, **kwargs):
        choice_a = 'Its linearity*'
        choice_b = 'Its frequency deviation'
        choice_c = 'Its percent of carrier phase shift'
        choice_d = 'Its percent of frequency modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What measurement can be made of a single-sideband phone transmitter's amplifier by performing a two-tone test using an oscilloscope?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_340:
    def __init__(self, *args, **kwargs):
        choice_a = 'At least 40 dB*'
        choice_b = 'No more than 20 dB'
        choice_c = 'No more than 30 dB'
        choice_d = 'At least 60 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How much is the carrier suppressed below peak output power in a single-sideband phone transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_341:
    def __init__(self, *args, **kwargs):
        choice_a = 'Signal distortion caused by excessive drive*'
        choice_b = 'Signal distortion caused by insufficient collector current'
        choice_c = 'The transmitter\'s automatic level control is properly adjusted'
        choice_d = 'The transmitter\'s carrier is properly suppressed'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by "flat topping" in a single-sideband phone transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_342:
    def __init__(self, *args, **kwargs):
        choice_a = '3*'
        choice_b = '0.3'
        choice_c = '3000'
        choice_d = '1000'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an FM phone signal having a maximum frequency deviation of 3000 Hz either side of the carrier frequency, what is the modulation index, when the modulating frequency is 1000 Hz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_343:
    def __init__(self, *args, **kwargs):
        choice_a = '3*'
        choice_b = '0.333'
        choice_c = '2000'
        choice_d = '6000'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the modulation index of an FM phone transmitter producing an instantaneous carrier deviation of 6 kHz when modulated with a 2 kHz modulating frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_344:
    def __init__(self, *args, **kwargs):
        choice_a = '1.66*'
        choice_b = '60'
        choice_c = '0.16'
        choice_d = '0.6'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the deviation ratio of an FM phone transmitter having a maximum frequency swing of plus or minus 5 kHz and accepting a maximum modulation rate of 3 kHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_345:
    def __init__(self, *args, **kwargs):
        choice_a = '2.14*'
        choice_b = '0.47'
        choice_c = '47'
        choice_d = '0.214'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the deviation ratio of an FM phone transmitter having a maximum frequency swing of plus or minus 7.5 kHz and accepting a maximum modulation rate of 3.5 kHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_346:
    def __init__(self, *args, **kwargs):
        choice_a = 'centre frequency*'
        choice_b = 'frequency deviation'
        choice_c = 'frequency shift'
        choice_d = 'modulating frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When the transmitter is not modulated, or the amplitude of the modulating signal is zero, the frequency of the carrier is called its:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_347:
    def __init__(self, *args, **kwargs):
        choice_a = 'amplitude of the modulating frequency*'
        choice_b = 'frequency of the modulating frequency'
        choice_c = 'amplitude and the frequency of the modulating frequency'
        choice_d = 'modulating frequency and the amplitude of the centre frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an FM transmitter system, the amount of deviation from the centre frequency is determined solely by the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_348:
    def __init__(self, *args, **kwargs):
        choice_a = 'an infinite number of sideband frequencies*'
        choice_b = 'two sideband frequencies'
        choice_c = 'four sideband frequencies'
        choice_d = 'one sideband frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Any FM wave with single-tone modulation has:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_349:
    def __init__(self, *args, **kwargs):
        choice_a = 'a carrier null and multiplying the modulation frequency by the modulation index*'
        choice_b = 'detecting the frequencies in the sidebands'
        choice_c = 'the amplitude of power in the sidebands'
        choice_d = 'a carrier peak and dividing by the modulation index'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Some types of deviation meters work on the principle of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_350:
    def __init__(self, *args, **kwargs):
        choice_a = 'modulating frequency and the modulation index*'
        choice_b = 'modulation index'
        choice_c = 'modulating frequency'
        choice_d = 'modulating frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When using some deviation meters, it is important to know:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_351:
    def __init__(self, *args, **kwargs):
        choice_a = '16 kHz*'
        choice_b = '8 kHz'
        choice_c = '5 kHz'
        choice_d = '3 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the significant bandwidth of an FM-phone transmission having a +/- 5-kHz deviation and a 3-kHz modulating frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_352:
    def __init__(self, *args, **kwargs):
        choice_a = '+/- 416.7 Hz*'
        choice_b = '+/- 12 kHz'
        choice_c = '+/- 5 kHz'
        choice_d = '+/- 41.67 Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the frequency deviation for a 12.21-MHz reactance-modulated oscillator in a +/- 5-kHz deviation, 146.52-MHz FM-phone transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_353:
    def __init__(self, *args, **kwargs):
        choice_a = 'Intermodulation interference*'
        choice_b = 'Neutralization'
        choice_c = 'Adjacent channel interference'
        choice_d = 'Amplifier desensitization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the signals of two repeater transmitters mix together in one or both of their final amplifiers and unwanted signals at the sum and difference frequencies of the original signals are generated and radiated, what is this called?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_354:
    def __init__(self, *args, **kwargs):
        choice_a = 'When they are in close proximity and the signals mix in one or both of their final amplifiers*'
        choice_b = 'When the signals are reflected in phase by aircraft passing overhead'
        choice_c = 'When they are in close proximity and the signals cause feedback in one or both of their final amplifiers'
        choice_d = 'When the signals are reflected out of phase by aircraft passing overhead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does intermodulation interference between two repeater transmitters usually occur?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_355:
    def __init__(self, *args, **kwargs):
        choice_a = 'By installing a terminated circulator or ferrite isolator in the transmission line to the transmitter and duplexer*'
        choice_b = 'By installing a low-pass filter in the antenna transmission line'
        choice_c = 'By installing a high-pass filter in the antenna transmission line'
        choice_d = 'By using a Class C final amplifier with high driving power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can intermodulation interference between two repeater transmitters in close proximity often be reduced or eliminated?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_356:
    def __init__(self, *args, **kwargs):
        choice_a = '146.34 MHz and 146.61 MHz*'
        choice_b = '146.88 MHz and 146.34 MHz'
        choice_c = '146.01 MHz and 147.30 MHz'
        choice_d = '73.35 MHz and 239.40 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a receiver tuned to 146.70 MHz receives an intermodulation product signal whenever a nearby transmitter transmits on 146.52, what are the two most likely frequencies for the other interfering signal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_357:
    def __init__(self, *args, **kwargs):
        choice_a = 'A phase modulator*'
        choice_b = 'A balanced modulator'
        choice_c = 'A double balanced mixer'
        choice_d = 'An audio modulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of circuit varies the tuning of an amplifier tank circuit to produce FM signals?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_358:
    def __init__(self, *args, **kwargs):
        choice_a = 'A pre-emphasis network*'
        choice_b = 'An audio prescaler'
        choice_c = 'A heterodyne suppressor'
        choice_d = 'A de-emphasis network'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What audio shaping network is added at an FM transmitter to attenuate the lower audio frequencies?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_359:
    def __init__(self, *args, **kwargs):
        choice_a = 'A cavity filter*'
        choice_b = 'A DSP filter'
        choice_c = 'An L-C filter'
        choice_d = 'A crystal filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of filter would be best to use in a 2-metre repeater duplexer?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_360:
    def __init__(self, *args, **kwargs):
        choice_a = 'pre-emphasis*'
        choice_b = 'the centre frequency'
        choice_c = 'de-emphasis'
        choice_d = 'frequency inversion'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The characteristic difference between a phase modulator and a frequency modulator is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_361:
    def __init__(self, *args, **kwargs):
        choice_a = 'between the audio amplifier and the modulator*'
        choice_b = 'between the multiplier and the PA'
        choice_c = 'between the modulator and the oscillator'
        choice_d = 'in the microphone circuit, before the audio amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In most modern FM transmitters, to produce a better sound, a compressor and a clipper are placed:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_362:
    def __init__(self, *args, **kwargs):
        choice_a = 'power, frequency deviation and frequency stability*'
        choice_b = 'distortion, bandwidth and sideband power'
        choice_c = 'modulation, pre-emphasis and carrier suppression'
        choice_d = 'frequency stability, de-emphasis and linearity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Three important parameters to be verified in an FM transmitter are:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_363:
    def __init__(self, *args, **kwargs):
        choice_a = 'intermediate frequency stage*'
        choice_b = 'final amplifier stage'
        choice_c = 'receiver frontend'
        choice_d = 'passive intermodulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Intermodulation interference products are not typically associated with which of the following:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_364:
    def __init__(self, *args, **kwargs):
        choice_a = 'automatic level control (ALC)*'
        choice_b = 'automatic gain control (AGC)'
        choice_c = 'automatic output control (AOC)'
        choice_d = 'automatic volume control (AVC)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Maintaining the peak RF output of a SSB transmitter at a relatively constant level requires a circuit called the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_365:
    def __init__(self, *args, **kwargs):
        choice_a = 'full amplification of low level signals and reducing or eliminating amplification of high level signals*'
        choice_b = 'full amplification of high level signals and reducing or eliminating signals amplification of low level'
        choice_c = 'a lower signal-to-noise ratio'
        choice_d = 'circuit level instability'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Speech compression associated with SSB transmission implies:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_366:
    def __init__(self, *args, **kwargs):
        choice_a = 'Aliasing amplifier*'
        choice_b = 'Analog to digital converter'
        choice_c = 'Digital to analog converter'
        choice_d = 'Mathematical transform'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following functions is not included in a typical digital signal processor?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_367:
    def __init__(self, *args, **kwargs):
        choice_a = '8 bits*'
        choice_b = '6 bits'
        choice_c = '16 bits'
        choice_d = '4 bits'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How many bits are required to provide 256 discrete levels, or a ratio of 256:1?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_368:
    def __init__(self, *args, **kwargs):
        choice_a = '6 dB*'
        choice_b = '1 dB'
        choice_c = '4 dB'
        choice_d = '3 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Adding one bit to the word length, is equivalent to adding ____ dB to the dynamic range of the digitizer:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_369:
    def __init__(self, *args, **kwargs):
        choice_a = 'Digital signal processor*'
        choice_b = 'Digital formatter'
        choice_c = 'Mathematical transformer'
        choice_d = 'Digital transformer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What do you call the circuit which employs an analog to digital converter, a mathematical transform, a digital to analog converter and a low pass filter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_370:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequency division*'
        choice_b = 'Compression'
        choice_c = 'Bandwidth limiting'
        choice_d = 'Clipping'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which principle is not associated with analog signal processing?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_371:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequency clipping*'
        choice_b = 'RF clipping'
        choice_c = 'Compression'
        choice_d = 'AF clipping'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" """
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_372:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increased harmonic distortion*'
        choice_b = 'Reduced average power'
        choice_c = 'Increased average power'
        choice_d = 'Reduction in peak amplitude'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the undesirable result of AF clipping in a speech processor?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_373:
    def __init__(self, *args, **kwargs):
        choice_a = 'is easier to implement*'
        choice_b = 'has less distortion'
        choice_c = 'is more expensive to implement'
        choice_d = 'is more difficult to implement'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which description is not correct? You are planning to build a speech processor for your transceiver. Compared to AF clipping, RF clipping:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_374:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF compression*'
        choice_b = 'AF compression'
        choice_c = 'RF clipping'
        choice_d = 'AF clipping'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Automatic Level Control (ALC) is another name for:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_375:
    def __init__(self, *args, **kwargs):
        choice_a = 'Varicode*'
        choice_b = 'AX.25'
        choice_c = 'Baudot'
        choice_d = 'ASCII'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What digital code consists of elements having unequal length?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_376:
    def __init__(self, *args, **kwargs):
        choice_a = 'The physical layer*'
        choice_b = 'The link layer'
        choice_c = 'The network layer'
        choice_d = 'The transport layer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Open Systems Interconnection (OSI) model standardizes communications functions as layers within a data communications system.  Amateur digital radio systems often follow the OSI model in structure. What is the base layer of the OSI model involving the interconnection of a packet radio TNC to a computer terminal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_377:
    def __init__(self, *args, **kwargs):
        choice_a = 'Error detection*'
        choice_b = 'Lossy compression'
        choice_c = 'Error correction'
        choice_d = 'Lossless compression'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the purpose of a Cyclic Redundancy Check (CRC)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_378:
    def __init__(self, *args, **kwargs):
        choice_a = 'It includes both upper and lower case text characters in the code*'
        choice_b = 'ASCII includes built-in error correction'
        choice_c = 'ASCII characters contain fewer information bits'
        choice_d = 'The larger character set allows store-and-forward'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one advantage of using ASCII rather than Baudot code?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_379:
    def __init__(self, *args, **kwargs):
        choice_a = 'The receiving station automatically requests repeats when needed*'
        choice_b = 'The receiving station checks the frame check sequence (FCS) against the transmitted FCS'
        choice_c = 'Each character is sent twice'
        choice_d = 'Mode A AMTOR does not include an error control system'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of error control system is used in AMTOR ARQ (Mode A)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_380:
    def __init__(self, *args, **kwargs):
        choice_a = 'Each character is sent twice*'
        choice_b = 'Mode B AMTOR does not include an error-correction system'
        choice_c = 'The receiving station automatically requests repeats when needed'
        choice_d = 'The receiving station checks the frame check sequence (FCS) against the transmitted FCS'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What error-correction system is used in AMTOR FEC (Mode B)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_381:
    def __init__(self, *args, **kwargs):
        choice_a = 'Automatic link establishment*'
        choice_b = 'Two-way messaging'
        choice_c = 'Telemetry'
        choice_d = 'Amateur-specific local information broadcast'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""APRS (Automatic Packet Reporting System) does NOT support which one of these functions?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_382:
    def __init__(self, *args, **kwargs):
        choice_a = 'Hash function*'
        choice_b = 'Dynamic Huffman code'
        choice_c = 'Convolution code'
        choice_d = 'Lempel-Ziv routine'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which algorithm may be used to create a Cyclic Redundancy Check (CRC)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_383:
    def __init__(self, *args, **kwargs):
        choice_a = 'packet*'
        choice_b = 'RTTY'
        choice_c = 'ASCII'
        choice_d = 'spread spectrum speech'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The designator AX.25 is associated with which amateur radio mode?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_384:
    def __init__(self, *args, **kwargs):
        choice_a = '5*'
        choice_b = '7'
        choice_c = '8'
        choice_d = '6'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How many information bits are included in the Baudot code?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_385:
    def __init__(self, *args, **kwargs):
        choice_a = '8*'
        choice_b = '7'
        choice_c = '6'
        choice_d = '5'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How many information bits are included in the ISO-8859 extension to the ASCII code?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_386:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spread spectrum communication*'
        choice_b = 'Amplitude-companded single sideband'
        choice_c = 'AMTOR'
        choice_d = 'Time domain frequency modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What term describes a wide-band communications system in which the RF carrier varies according to some predetermined sequence?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_387:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequency hopping*'
        choice_b = 'Direct sequence'
        choice_c = 'Time-domain frequency modulation'
        choice_d = 'Frequency companded spread spectrum'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term used to describe a spread spectrum communications system where the centre frequency of a conventional carrier is changed many times per second in accordance with a pseudorandom list of channels?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_388:
    def __init__(self, *args, **kwargs):
        choice_a = 'Direct sequence*'
        choice_b = 'Frequency hopping'
        choice_c = 'Phase companded spread spectrum'
        choice_d = 'Binary phase-shift keying'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What term is used to describe a spread spectrum communications system in which a very fast binary bit stream is used to shift the phase of an RF carrier?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_389:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spread spectrum*'
        choice_b = 'AMTOR'
        choice_c = 'Packet'
        choice_d = 'RTTY'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Frequency hopping is used with which type of transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_390:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spread spectrum*'
        choice_b = 'AMTOR'
        choice_c = 'Packet'
        choice_d = 'RTTY'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" Direct sequence is used with which type of transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_391:
    def __init__(self, *args, **kwargs):
        choice_a = 'Pseudo-random sequence*'
        choice_b = 'Frequency-companded sequence'
        choice_c = 'Quantizing noise'
        choice_d = 'Random noise sequence'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of signal is used to produce a predetermined alteration in the carrier for spread spectrum communication?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_392:
    def __init__(self, *args, **kwargs):
        choice_a = 'Your receiver must be frequency-synchronized to the transmitter*'
        choice_b = 'It requires narrower bandwidth than most receivers have'
        choice_c = 'It varies too quickly in amplitude'
        choice_d = 'The signal is too distorted for comfortable listening'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is it difficult to monitor a spread spectrum transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_393:
    def __init__(self, *args, **kwargs):
        choice_a = 'The carrier frequency is changed in accordance with a pseudo-random list of channels*'
        choice_b = 'The carrier is amplitude-modulated over a wide range called the spread'
        choice_c = 'The carrier is frequency-companded'
        choice_d = 'The carrier is phase-shifted by a fast binary bit stream'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is frequency hopping spread spectrum?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_394:
    def __init__(self, *args, **kwargs):
        choice_a = 'The carrier is phase-shifted by a fast binary bit stream*'
        choice_b = 'The carrier is amplitude modulated over a range called the spread'
        choice_c = 'The carrier is frequency-companded'
        choice_d = 'The carrier is altered in accordance with a pseudo-random list of channels'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is direct-sequence spread spectrum?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_395:
    def __init__(self, *args, **kwargs):
        choice_a = 'Signals not using the spectrum-spreading algorithm are suppressed in the receiver*'
        choice_b = 'The receiver is always equipped with a special digital signal processor (DSP) interference filter'
        choice_c = 'If interference is detected by the receiver, it will signal the transmitter to change frequencies'
        choice_d = 'The high power used by a spread-spectrum transmitter keeps its signal from being easily overpowered'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why are received spread-spectrum signals so resistant to interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_396:
    def __init__(self, *args, **kwargs):
        choice_a = 'The frequency of an RF carrier is changed very rapidly according to a particular pseudo-random sequence*'
        choice_b = 'If interference is detected by the receiver, it will signal the transmitter to change frequency'
        choice_c = 'If interference is detected by the receiver, it will signal the transmitter to wait until the frequency is clear'
        choice_d = 'A pseudo-random bit stream is used to shift the phase of an RF carrier very rapidly in a particular sequence'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does the spread-spectrum technique of frequency hopping work?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_397:
    def __init__(self, *args, **kwargs):
        choice_a = 'Increased selectivity and optimal tuned circuit design*'
        choice_b = 'Automatic detection in the RF amplifier and increased sensitivity'
        choice_c = 'Automatic soft-limiting and automatic squelching'
        choice_d = 'Automatic squelching and increased sensitivity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What are the advantages of the frequency conversion process in a superheterodyne receiver?
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_398:
    def __init__(self, *args, **kwargs):
        choice_a = 'Image rejection and responses to unwanted signals*'
        choice_b = 'Noise figure and distortion'
        choice_c = 'Interference to other services'
        choice_d = 'Cross-modulation distortion and interference'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What factors should be considered when selecting an intermediate frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_399:
    def __init__(self, *args, **kwargs):
        choice_a = 'greater reduction of image interference for a given front end selectivity*'
        choice_b = 'is much more stable'
        choice_c = 'is much more sensitive'
        choice_d = 'produces a louder signal at the output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One of the greatest advantages of the double-conversion over the single-conversion receiver is that it:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_400:
    def __init__(self, *args, **kwargs):
        choice_a = 'IF circuits*'
        choice_b = 'local oscillator'
        choice_c = 'audio output stage'
        choice_d = 'detector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a communications receiver, a crystal filter would be located in the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_401:
    def __init__(self, *args, **kwargs):
        choice_a = 'additional oscillators and mixing frequencies involved in the design*'
        choice_b = 'poorer selectivity in the IF caused by the multitude of frequency changes'
        choice_c = 'greater sensitivity introducing higher levels of RF to the receiver'
        choice_d = 'AGC being forced to work harder causing the stages concerned to overload'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A multiple conversion superheterodyne receiver is more susceptible to spurious responses than a single-conversion receiver because of the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_402:
    def __init__(self, *args, **kwargs):
        choice_a = 'image rejection and selectivity*'
        choice_b = 'selectivity and image rejection'
        choice_c = 'selectivity and dynamic range'
        choice_d = 'image rejection and noise figure'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a dual-conversion superheterodyne receiver what are the respective aims of the first and second conversion:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_403:
    def __init__(self, *args, **kwargs):
        choice_a = 'The RF amplifier*'
        choice_b = 'The local oscillator'
        choice_c = 'The audio frequency amplifier'
        choice_d = 'The detector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which stage of a receiver has its input and output circuits tuned to the received frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_404:
    def __init__(self, *args, **kwargs):
        choice_a = 'Mixer*'
        choice_b = 'Radio frequency amplifier'
        choice_c = 'Intermediate frequency amplifier'
        choice_d = 'Local oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which stage of a superheterodyne receiver lies between a tuneable stage and a fixed tuned stage?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_405:
    def __init__(self, *args, **kwargs):
        choice_a = '7 MHz*'
        choice_b = '16 MHz'
        choice_c = '21 MHz'
        choice_d = '9 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A single conversion receiver with a 9 MHz IF has a local oscillator operating at 16 MHz. The frequency it is tuned to is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_406:
    def __init__(self, *args, **kwargs):
        choice_a = 'two IF stages and two local oscillators*'
        choice_b = 'one IF stage and one local oscillator'
        choice_c = 'two IF stages and three local oscillators'
        choice_d = 'two IF stages and one local oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A double conversion receiver designed for SSB reception has a beat frequency oscillator and:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_407:
    def __init__(self, *args, **kwargs):
        choice_a = 'suffers less from image interference for a given front end sensitivity*'
        choice_b = 'does not drift off frequency'
        choice_c = 'is a more sensitive receiver'
        choice_d = 'produces a louder audio signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The advantage of a double conversion receiver over a single conversion receiver is that it:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_408:
    def __init__(self, *args, **kwargs):
        choice_a = 'change the frequency of the incoming signal to that of the IF*'
        choice_b = 'allow a number of IF frequencies to be used'
        choice_c = 'remove image signals from the receiver'
        choice_d = 'produce an audio frequency for the speaker'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The mixer stage of a superheterodyne receiver is used to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_409:
    def __init__(self, *args, **kwargs):
        choice_a = 'the suppressed carrier must be replaced for detection*'
        choice_b = 'it phases out the unwanted sideband signal'
        choice_c = 'it reduces the pass-band of the IF stages'
        choice_d = 'it beats with the receiver carrier to produce the missing sideband'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A superheterodyne receiver designed for SSB reception must have a beat-frequency oscillator (BFO) because:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_410:
    def __init__(self, *args, **kwargs):
        choice_a = 'an intermediate frequency*'
        choice_b = 'an audio frequency'
        choice_c = 'a radio frequency'
        choice_d = 'a high frequency oscillator (HFO) frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The first mixer in the receiver mixes the incoming signal with the local oscillator to produce:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_411:
    def __init__(self, *args, **kwargs):
        choice_a = '5 400 kHz*'
        choice_b = '3 400 kHz'
        choice_c = '10 600 kHz'
        choice_d = '21 600 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the incoming signal to the mixer is 3 600 kHz and the first IF is 9 MHz, at which one of the following frequencies would the local oscillator (LO) operate?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_412:
    def __init__(self, *args, **kwargs):
        choice_a = 'to beat with the incoming signal*'
        choice_b = 'to pass the signal without interruption'
        choice_c = 'to provide additional amplification'
        choice_d = 'to protect the incoming signal from interference'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The BFO is off-set slightly (500 - 1 500 Hz) from the incoming signal to the detector. This is required:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_413:
    def __init__(self, *args, **kwargs):
        choice_a = 'stable and spectrally pure*'
        choice_b = 'sensitive and selective'
        choice_c = 'stable and sensitive'
        choice_d = 'selective and spectrally pure'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""It is very important that the oscillators contained in a superheterodyne receiver are:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_414:
    def __init__(self, *args, **kwargs):
        choice_a = 'tuning of the local oscillator (LO)*'
        choice_b = 'tuning both the antenna and the BFO'
        choice_c = 'tuning of the beat-frequency oscillator (BFO)'
        choice_d = 'tuning both the antenna and the LO'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a superheterodyne receiver, a stage before the IF amplifier has a variable capacitor in parallel with a trimmer capacitor and an inductance. The variable capacitor is for:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_415:
    def __init__(self, *args, **kwargs):
        choice_a = 'tuning the receiver preselector to the reception frequency*'
        choice_b = 'tuning both the antenna and the beat-frequency oscillator'
        choice_c = 'tuning the beat-frequency oscillator'
        choice_d = 'tuning both the antenna and the local oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a superheterodyne receiver without an RF amplifier, the input to the mixer stage has a variable capacitor in parallel with an inductance. The variable capacitor is for:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_416:
    def __init__(self, *args, **kwargs):
        choice_a = 'Mixer*'
        choice_b = 'BFO'
        choice_c = 'VFO'
        choice_d = 'Multiplier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What receiver stage combines a 14.25-MHz input signal with a 13.795-MHz oscillator signal to produce a 455-kHz intermediate frequency (IF) signal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_417:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF and first mixer*'
        choice_b = 'IF and local oscillator'
        choice_c = 'RF and IF'
        choice_d = 'RF and local oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which two stages in a superheterodyne receiver have input tuned circuits tuned to the same frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_418:
    def __init__(self, *args, **kwargs):
        choice_a = 'produces an intermediate frequency*'
        choice_b = 'produces spurious signals'
        choice_c = 'acts as a buffer stage'
        choice_d = 'demodulates SSB signals'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The mixer stage of a superheterodyne receiver:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class f_1_419:
    def __init__(self, *args, **kwargs):
        choice_a = 'The weakest signal that can be detected above the receiver internal noise*'
        choice_b = 'The weakest signal that can be detected under noisy atmospheric conditions'
        choice_c = 'The minimum level of noise that will overload the receiver RF amplifier stage'
        choice_d = 'The amount of noise generated by the receiver local oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by the noise floor of a receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_420:
    def __init__(self, *args, **kwargs):
        choice_a = 'To improve selectivity and gain*'
        choice_b = 'To tune out cross-modulation distortion'
        choice_c = 'To increase dynamic response'
        choice_d = 'To improve noise figure performance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is a purpose of the first IF amplifier stage in a receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_421:
    def __init__(self, *args, **kwargs):
        choice_a = 'Sufficient gain to allow weak signals to overcome noise generated in the first mixer stage*'
        choice_b = 'As much gain as possible, short of self-oscillation'
        choice_c = 'It depends on the amplification factor of the first IF stage'
        choice_d = 'Sufficient gain to keep weak signals below the noise of the first mixer stage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How much gain should be used in the RF amplifier stage of a receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_422:
    def __init__(self, *args, **kwargs):
        choice_a = 'To improve the receiver noise figure*'
        choice_b = 'To vary the receiver image rejection by using the AGC'
        choice_c = 'To develop the AGC voltage'
        choice_d = 'To provide most of the receiver gain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the primary purpose of an RF amplifier in a receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_423:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF level for 12 dB SINAD*'
        choice_b = 'RF level for a given Bit Error Rate (BER)'
        choice_c = 'Noise Figure in decibels'
        choice_d = 'Overall gain in decibels'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How is receiver sensitivity often expressed for UHF FM receivers?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_424:
    def __init__(self, *args, **kwargs):
        choice_a = 'Dynamic range*'
        choice_b = 'Design parameter'
        choice_c = 'Stability'
        choice_d = 'Noise figure'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term used for the decibel difference (or ratio) between the largest tolerable receiver input signal (without causing audible distortion products) and the minimum discernible signal (sensitivity)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_425:
    def __init__(self, *args, **kwargs):
        choice_a = 'sensitivity*'
        choice_b = 'rejection of unwanted signals'
        choice_c = 'selectivity'
        choice_d = 'stability'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The lower the receiver noise figure becomes, the greater will be the receiver's _________:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_426:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF amplifier and mixer*'
        choice_b = 'detector and AF amplifier'
        choice_c = 'BFO and detector'
        choice_d = 'IF amplifier and detector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The noise generated in a receiver of good design originates in the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_427:
    def __init__(self, *args, **kwargs):
        choice_a = 'External HF noise, man-made and natural, are higher than the internal noise generated by the receiver*'
        choice_b = 'Ionospheric distortion of the received signal creates high noise levels'
        choice_c = 'The use of SSB and CW on the HF bands overcomes the noise'
        choice_d = 'Regardless of the front end, the succeeding stages when used on HF are very noisy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why are very low noise figures relatively unimportant for a high frequency receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_428:
    def __init__(self, *args, **kwargs):
        choice_a = 'dynamic range*'
        choice_b = 'AGC'
        choice_c = 'cross-modulation index'
        choice_d = 'noise figure'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The term which relates specifically to the amplitude levels of multiple signals that can be accommodated during reception is called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_429:
    def __init__(self, *args, **kwargs):
        choice_a = 'preselector*'
        choice_b = 'preamble'
        choice_c = 'preamplifier'
        choice_d = 'pass-selector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Normally, front-end selectivity is provided by the resonant networks both before and after the RF stage in a superheterodyne receiver. This whole section of the receiver is often referred to as the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_430:
    def __init__(self, *args, **kwargs):
        choice_a = 'A de-emphasis network*'
        choice_b = 'A pre-emphasis network'
        choice_c = 'An audio prescaler'
        choice_d = 'A heterodyne suppressor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What audio shaping network is added at an FM receiver to restore proportionally attenuated lower audio frequencies?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_431:
    def __init__(self, *args, **kwargs):
        choice_a = 'It mixes an incoming signal with a locally generated carrier*'
        choice_b = 'It provides local oscillations for input to a mixer'
        choice_c = 'It amplifies and narrows band-pass frequencies'
        choice_d = 'It detects cross-modulation products'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does a product detector do?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_432:
    def __init__(self, *args, **kwargs):
        choice_a = 'automatic gain control (AGC)*'
        choice_b = 'IF amplifier'
        choice_c = 'AF amplifier'
        choice_d = 'RF amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Distortion in a receiver that only affects strong signals usually indicates a defect in or mis-adjustment of the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_433:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduces the receiver gain*'
        choice_b = 'increases the receiver gain'
        choice_c = 'distorts the signal'
        choice_d = 'introduces limiting'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a superheterodyne receiver with automatic gain control (AGC), as the strength of the signal increases, the AGC:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_434:
    def __init__(self, *args, **kwargs):
        choice_a = 'detector*'
        choice_b = 'RF amplifier'
        choice_c = 'audio output'
        choice_d = 'LO'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The amplified IF signal is applied to the ____________ stage in a superheterodyne receiver:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_435:
    def __init__(self, *args, **kwargs):
        choice_a = 'applied to the AF amplifier*'
        choice_b = 'grounded via the chassis'
        choice_c = 'fed directly to the speaker'
        choice_d = 'applied to the RF amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The low-level output of a detector is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_436:
    def __init__(self, *args, **kwargs):
        choice_a = 'automatic gain control*'
        choice_b = 'automatic frequency control'
        choice_c = 'inverse gain control'
        choice_d = 'automatic load control'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The overall output of an AM/CW/SSB receiver can be adjusted by means of manual controls on the receiver or by use of a circuit known as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_437:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF and IF amplifiers*'
        choice_b = 'AF and IF amplifiers'
        choice_c = 'RF and AF amplifiers'
        choice_d = 'detector and AF amplifiers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""AGC voltage is applied to the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_438:
    def __init__(self, *args, **kwargs):
        choice_a = 'IF derived or audio derived*'
        choice_b = 'RF derived or audio derived'
        choice_c = 'IF derived or RF derived'
        choice_d = 'detector derived or audio derived'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""AGC is derived in a receiver from one of two circuits. Depending on the method used, it is called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_439:
    def __init__(self, *args, **kwargs):
        choice_a = 'Threshold and decay time*'
        choice_b = 'Blanking level and slope'
        choice_c = 'Slope and bandwidth'
        choice_d = 'Clipping level and hang time'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which two variables primarily determine the behaviour of an automatic gain control (AGC) loop?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_440:
    def __init__(self, *args, **kwargs):
        choice_a = 'A product detector circuit*'
        choice_b = 'An AGC circuit'
        choice_c = 'A power supply circuit'
        choice_d = 'A VFO circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What circuit combines signals from an IF amplifier stage and a beat-frequency oscillator (BFO), to produce an audio signal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_441:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF amplifier pre-selector*'
        choice_b = 'Product detector'
        choice_c = 'AGC loop'
        choice_d = 'IF filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What part of a superheterodyne receiver determines the image rejection ratio of the receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_442:
    def __init__(self, *args, **kwargs):
        choice_a = 'Desensitization*'
        choice_b = 'Cross-modulation interference'
        choice_c = 'Squelch gain rollback'
        choice_d = 'Quieting'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term for the reduction in receiver sensitivity caused by a strong signal near the received frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_443:
    def __init__(self, *args, **kwargs):
        choice_a = 'Strong near frequency signals*'
        choice_b = 'Squelch gain adjusted too high'
        choice_c = 'Squelch gain adjusted too low'
        choice_d = 'Audio gain adjusted too low'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes receiver desensitization?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_444:
    def __init__(self, *args, **kwargs):
        choice_a = 'Use a cavity filter*'
        choice_b = 'Decrease the receiver squelch gain'
        choice_c = 'Increase the receiver bandwidth'
        choice_d = 'Increase the transmitter audio gain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one way receiver desensitization can be reduced?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_445:
    def __init__(self, *args, **kwargs):
        choice_a = 'Nonlinear circuits or devices*'
        choice_b = 'Too little gain'
        choice_c = 'Positive feedback'
        choice_d = 'Lack of neutralization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes intermodulation in an electronic circuit?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_446:
    def __init__(self, *args, **kwargs):
        choice_a = 'To move the image response far away from the filter passband*'
        choice_b = 'To provide a greater tuning range'
        choice_c = 'To tune out cross-modulation distortion'
        choice_d = 'To prevent the generation of spurious mixer products'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is an important reason for using a VHF intermediate frequency in an HF receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_447:
    def __init__(self, *args, **kwargs):
        choice_a = 'the mixing of two or more signals in the front-end of a superheterodyne receiver*'
        choice_b = 'the interaction of products from high-powered transmitters in the area'
        choice_c = 'the high-voltage stages in the final amplifier of an amplitude or frequency-modulated transmitter'
        choice_d = 'the mixing of more than one signal in the first or second intermediate frequency amplifiers of a receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Intermodulation interference is produced by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_448:
    def __init__(self, *args, **kwargs):
        choice_a = 'Dial display accuracy*'
        choice_b = 'Mechanical rigidity'
        choice_c = 'Feedback components'
        choice_d = 'Temperature variations'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is NOT a direct cause of instability in a receiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_449:
    def __init__(self, *args, **kwargs):
        choice_a = 'local oscillator and power supply*'
        choice_b = 'detector'
        choice_c = 'RF amplifier'
        choice_d = 'mixer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Poor frequency stability in a receiver usually originates in the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_450:
    def __init__(self, *args, **kwargs):
        choice_a = 'Feedback*'
        choice_b = 'Desensitization'
        choice_c = 'Intermodulation'
        choice_d = 'Cross-modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Poor dynamic range of a receiver can cause many problems when a strong signal appears within or near the front-end bandpass. Which of the following is NOT caused as a direct result?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_451:
    def __init__(self, *args, **kwargs):
        choice_a = 'Two-tone Third-Order IMD Dynamic Range, 10 MHz spacing*'
        choice_b = 'Third-Order Intercept Point'
        choice_c = 'Blocking Dynamic Range'
        choice_d = 'Intermediate frequency rejection ratio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these measurements is a good indicator of VHF receiver performance in an environment of strong out-of-band signals?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_452:
    def __init__(self, *args, **kwargs):
        choice_a = 'The circuit is known as a Pi-type antenna tuner*'
        choice_b = 'The input is suitable for 50 ohm impedance'
        choice_c =  'The output is suitable for impedances from low to high'
        choice_d = 'The circuit is known as a transformer-type antenna tuner'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For an antenna tuner of the "Transformer" type, which of the following statements is FALSE?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_453:
    def __init__(self, *args, **kwargs):
        choice_a = 'The circuit is known as a Pi-type antenna tuner*'
        choice_b = 'The circuit is known as a Series-type antenna tuner'
        choice_c = 'The output is suitable for impedances from low to high'
        choice_d = 'The input is suitable for impedance of 50 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For an antenna tuner of the "Series" type, which of the following statements is false?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_454:
    def __init__(self, *args, **kwargs):
        choice_a = 'The circuit is suitable for matching to a vertical ground plane antenna*'
        choice_b = 'The transmitter input is suitable for 50 ohms impedance'
        choice_c = 'The antenna output is high impedance'
        choice_d = 'The circuit is known as an L-type antenna tuner'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For an antenna tuner of the "L" type, which of the following statements is false?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_455:
    def __init__(self, *args, **kwargs):
        choice_a = 'The circuit is a series-type antenna tuner*'
        choice_b = 'The transmitter input is suitable for impedance of 50 ohms'
        choice_c = 'The antenna output is suitable for impedances from low to high'
        choice_d = 'The circuit is a Pi-type antenna tuner'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For an antenna tuner of the "Pi" type, which of the following statements is false?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_456:
    def __init__(self, *args, **kwargs):
        choice_a = 'A network consisting of one inductor and two capacitors or two inductors and one capacitor*'
        choice_b = 'An antenna matching network that is isolated from ground'
        choice_c = 'A network consisting of four inductors or four capacitors'
        choice_d = 'A power incidence network'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a pi-network?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_457:
    def __init__(self, *args, **kwargs):
        choice_a = 'Pi-network*'
        choice_b = 'Chebyshev'
        choice_c = 'Butterworth'
        choice_d = 'L-network'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of network offers the greatest transformation ratio?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_458:
    def __init__(self, *args, **kwargs):
        choice_a = 'It matches only a small impedance range*'
        choice_b = 'It is thermally unstable'
        choice_c = 'It is prone to self-resonance'
        choice_d = 'It has limited power handling capability'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is an L-network of limited utility in impedance matching?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_459:
    def __init__(self, *args, **kwargs):
        choice_a = 'It cancels the reactive part of an impedance and changes the resistive part*'
        choice_b = 'It produces transconductance to cancel the reactive part of an impedance'
        choice_c = 'It introduces negative resistance to cancel the resistive part of an impedance'
        choice_d = 'Network resistances substitute for load resistances'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does a network transform one impedance to another?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_460:
    def __init__(self, *args, **kwargs):
        choice_a = 'Greater harmonic suppression*'
        choice_b = 'Higher efficiency'
        choice_c = 'Lower losses'
        choice_d = 'Greater transformation range'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What advantage does a pi-L network have over a pi-network for impedance matching between a vacuum tube linear amplifier and a multiband antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_461:
    def __init__(self, *args, **kwargs):
        choice_a = 'Pi-L network*'
        choice_b = 'Inverse pi-network'
        choice_c = 'Pi-network'
        choice_d = 'L-network'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which type of network provides the greatest harmonic suppression?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_462:
    def __init__(self, *args, **kwargs):
        choice_a = 'because it simplifies mathematical operations*'
        choice_b = 'only to solve matching and transmission line problems'
        choice_c = 'to solve problems in direct current circuits'
        choice_d = 'because it only works with complex numbers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Smith Chart is useful:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class f_1_463:
    def __init__(self, *args, **kwargs):
        choice_a = 'A very high impedance*'
        choice_b = 'The same as the characteristic impedance of the transmission line'
        choice_c = 'The same as the output impedance of the source'
        choice_d = 'A very low impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of impedance does a quarter wavelength transmission line present to the source when the line is shorted at the far end?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_464:
    def __init__(self, *args, **kwargs):
        choice_a = 'A very low impedance*'
        choice_b = 'A very high impedance'
        choice_c = 'The same as the output impedance of the source'
        choice_d = 'The same as the characteristic impedance of the transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of impedance does a quarter wavelength transmission line present to the source if the line is open at the far end?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_465:
    def __init__(self, *args, **kwargs):
        choice_a = 'A very high impedance*'
        choice_b = 'The same as the characteristic impedance of the transmission line'
        choice_c = 'The same as the output impedance of the source'
        choice_d = 'A very low impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of impedance does a half wavelength transmission line present to the source when the line is open at the far end?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_466:
    def __init__(self, *args, **kwargs):
        choice_a = 'A very low impedance*'
        choice_b = 'A very high impedance'
        choice_c = 'The same as the characteristic impedance of the transmission line'
        choice_d = 'The same as the output impedance of the source'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of impedance does a half wavelength transmission line present to the source when the line is shorted at the far end?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_467:
    def __init__(self, *args, **kwargs):
        choice_a = 'The velocity of the wave on the transmission line divided by the velocity of light*'
        choice_b = 'The velocity of the wave on the transmission line multiplied by the velocity of light in a vacuum'
        choice_c = 'The index of shielding for coaxial cable'
        choice_d = 'The ratio of the characteristic impedance of the line to the terminating impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the velocity factor of a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_468:
    def __init__(self, *args, **kwargs):
        choice_a = 'Velocity factor*'
        choice_b = 'Characteristic impedance'
        choice_c = 'Surge impedance'
        choice_d = 'Standing wave ratio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term for the ratio of the actual velocity at which a signal travels through a transmission line to the speed of light in a vacuum?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_469:
    def __init__(self, *args, **kwargs):
        choice_a = '0.66*'
        choice_b = '0.33'
        choice_c = '0.1'
        choice_d = '2.7'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a typical velocity factor for coaxial cable with polyethylene dielectric?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_470:
    def __init__(self, *args, **kwargs):
        choice_a = 'Dielectrics in the line*'
        choice_b = 'The line length'
        choice_c = 'The centre conductor resistivity'
        choice_d = 'The terminal impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What determines the velocity factor in a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_471:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF energy moves slower along the coaxial cable than in air*'
        choice_b = 'The surge impedance is higher in the parallel transmission line'
        choice_c = 'Skin effect is less pronounced in the coaxial cable'
        choice_d = 'The characteristic impedance is higher in a parallel transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is the physical length of a coaxial cable shorter than its electrical length?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_472:
    def __init__(self, *args, **kwargs):
        choice_a = 'velocity factor*'
        choice_b = 'VSWR'
        choice_c = 'impedance'
        choice_d = 'hermetic losses'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The reciprocal of the square root of the dielectric constant of the material used to separate the conductors in a transmission line gives the ____________ of the line:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_473:
    def __init__(self, *args, **kwargs):
        choice_a = 'ratio of the velocity of propagation in the transmission line to the velocity of propagation in free space*'
        choice_b = 'impedance of the line, e.g. 50 ohm, 75 ohm, etc.'
        choice_c = 'speed at which the signal travels in free space'
        choice_d = 'speed to which the standing waves are reflected back to the transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The velocity factor of a transmission line is the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_474:
    def __init__(self, *args, **kwargs):
        choice_a = 'The T match*'
        choice_b = 'The gamma match'
        choice_c = 'The omega match'
        choice_d = 'The stub match'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What term describes a method used to match a high-impedance transmission line to a lower impedance antenna by connecting the line to the driven element in two places, spaced a fraction of a wavelength on each side of the driven element centre?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_475:
    def __init__(self, *args, **kwargs):
        choice_a = 'The gamma match*'
        choice_b = 'The omega match'
        choice_c = 'The stub match'
        choice_d = 'The T match'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What term describes an unbalanced feed system in which the driven element of an antenna is fed both at the centre and a fraction of a wavelength to one side of centre?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_476:
    def __init__(self, *args, **kwargs):
        choice_a = 'The stub match*'
        choice_b = 'The omega match'
        choice_c = 'The delta match'
        choice_d = 'The gamma match'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What term describes a method of antenna impedance matching that uses a short section of transmission line connected to the antenna transmission line near the antenna and perpendicular to the transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_477:
    def __init__(self, *args, **kwargs):
        choice_a = '3.51 metres (11.5 feet)*'
        choice_b = '20 metres (65.6 feet)'
        choice_c = '2.33 metres (7.64 feet)'
        choice_d = '0.25 metre (0.82 foot)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Assuming a velocity factor of 0.66 what would be the physical length of a typical coaxial stub that is electrically one quarter wavelength long at 14.1 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_478:
    def __init__(self, *args, **kwargs):
        choice_a = 'gamma match*'
        choice_b = 'lambda match'
        choice_c = 'T match'
        choice_d = 'zeta match'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The driven element of a Yagi antenna is connected to a coaxial transmission line. The coax braid is connected to the centre of the driven element and the centre conductor is connected to a variable capacitor in series with an adjustable mechanical arrangement on one side of the driven element. The type of matching is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_479:
    def __init__(self, *args, **kwargs):
        choice_a = '4 m (13.1 ft)*'
        choice_b = '12 m (39.4 ft)'
        choice_c = '8 m (26.2 ft)'
        choice_d = '7.5 m (24.6 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A quarter-wave stub, for use at 15 MHz, is made from a coaxial cable having a velocity factor of 0.8. Its physical length will be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_480:
    def __init__(self, *args, **kwargs):
        choice_a = 'a "gamma" match*'
        choice_b = 'a "T" match'
        choice_c = 'an "omega" match'
        choice_d = 'a "Y" match'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The matching of a driven element with a single adjustable mechanical and capacitive arrangement is descriptive of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_481:
    def __init__(self, *args, **kwargs):
        choice_a = 'the centre of the driven element*'
        choice_b = 'the variable capacitor'
        choice_c = 'the adjustable gamma rod'
        choice_d = 'the centre of the reflector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Yagi antenna uses a gamma match. The coaxial braid connects to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_482:
    def __init__(self, *args, **kwargs):
        choice_a = 'the coaxial line braid*'
        choice_b = 'the coaxial line centre conductor'
        choice_c = 'the adjustable gamma rod'
        choice_d = 'a variable capacitor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Yagi antenna uses a gamma match. The centre of the driven element connects to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_483:
    def __init__(self, *args, **kwargs):
        choice_a = 'the variable capacitor*'
        choice_b = 'the coaxial line centre conductor'
        choice_c = 'an adjustable point on the reflector'
        choice_d = 'the centre of the driven element'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Yagi antenna uses a gamma match. The adjustable gamma rod connects to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_484:
    def __init__(self, *args, **kwargs):
        choice_a = 'adjustable gamma rod*'
        choice_b = 'an adjustable point on the director'
        choice_c = 'center of the driven element'
        choice_d = 'coaxial line braid'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A Yagi antenna uses a gamma match. The variable capacitor connects to the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_485:
    def __init__(self, *args, **kwargs):
        choice_a = 'voltage*'
        choice_b = 'current'
        choice_c = 'inductance'
        choice_d = 'capacitance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, the distribution of _______ is highest at each end."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_486:
    def __init__(self, *args, **kwargs):
        choice_a = 'current*'
        choice_b = 'voltage'
        choice_c = 'inductance'
        choice_d = 'capacitance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, the distribution of _______ is lowest at each end."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_487:
    def __init__(self, *args, **kwargs):
        choice_a = 'maximum current*'
        choice_b = 'minimum current'
        choice_c = 'minimum voltage and current'
        choice_d = 'maximum voltage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The feed point in a centre-fed half-wave antenna is at the point of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_488:
    def __init__(self, *args, **kwargs):
        choice_a = 'voltage*'
        choice_b = 'capacity'
        choice_c = 'inductance'
        choice_d = 'current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, the lowest distribution of _________ occurs at the middle."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_489:
    def __init__(self, *args, **kwargs):
        choice_a = 'current*'
        choice_b = 'inductance'
        choice_c = 'voltage'
        choice_d = 'capacity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, the highest distribution of ________ occurs at the middle."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_490:
    def __init__(self, *args, **kwargs):
        choice_a = 'the current is maximum*'
        choice_b = 'the voltage is maximum'
        choice_c = 'the resistance is maximum'
        choice_d = 'the antenna is resonant'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A half-wave dipole antenna is normally fed at the point where:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_491:
    def __init__(self, *args, **kwargs):
        choice_a = 'voltage is high and current is low*'
        choice_b = 'voltage and current are both high'
        choice_c = 'voltage and current are both low'
        choice_d = 'voltage is low and current is high'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At the ends of a half-wave dipole:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_492:
    def __init__(self, *args, **kwargs):
        choice_a = 'voltage is low and current is high*'
        choice_b = 'voltage and current are both high'
        choice_c = 'voltage and current are both low'
        choice_d = 'voltage is high and current is low'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The impedance of a half-wave antenna at its centre is low, because at this point:
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_493:
    def __init__(self, *args, **kwargs):
        choice_a = 'The centre*'
        choice_b = 'At the right end'
        choice_c = 'It is equal at all points'
        choice_d = 'Both ends'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, where does minimum voltage occur?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_494:
    def __init__(self, *args, **kwargs):
        choice_a = 'At both ends*'
        choice_b = 'At the centre'
        choice_c = 'It is equal at all points'
        choice_d = 'At the right end'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, where does the minimum current occur?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_495:
    def __init__(self, *args, **kwargs):
        choice_a = 'At the centre*'
        choice_b = 'It is the same at all points'
        choice_c = 'At the right end'
        choice_d = 'At both ends'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a half-wave dipole, where does the minimum impedance occur?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_496:
    def __init__(self, *args, **kwargs):
        choice_a = 'Waves with a rotating electric field*'
        choice_b = 'Waves with an electric field bent into circular shape'
        choice_c = 'Waves that circle the earth'
        choice_d = 'Waves produced by a circular loop antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by circularly polarized electromagnetic waves?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_497:
    def __init__(self, *args, **kwargs):
        choice_a = 'Circular polarization*'
        choice_b = 'Cross-polarization'
        choice_c = 'Perpendicular polarization'
        choice_d = 'None of the other answers, the two fields cancel out'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of polarization is produced by crossed dipoles fed 90 degrees out of phase?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_498:
    def __init__(self, *args, **kwargs):
        choice_a = 'Loaded helical-wound antenna*'
        choice_b = 'Crossed dipoles fed 90 degrees out of phase'
        choice_c = 'Lindenblad antenna'
        choice_d = 'Axial-mode helical antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these antennas does not produce circular polarization?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_499:
    def __init__(self, *args, **kwargs):
        choice_a = 'Contact via satellite*'
        choice_b = 'Contact through a hilltop repeater'
        choice_c = 'Simplex line-of-sight contact between hand-held transceivers'
        choice_d = 'Contact with terrestrial mobile stations'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On VHF/UHF frequencies, Doppler shift becomes of consequence on which type of communication?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_500:
    def __init__(self, *args, **kwargs):
        choice_a = '20 dB or more*'
        choice_b = '3 dB'
        choice_c = '6 dB'
        choice_d = '10 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For VHF and UHF signals over a fixed path, what extra loss can be expected when linearly-polarized antennas are crossed-polarized (90 degrees)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_501:
    def __init__(self, *args, **kwargs):
        choice_a = 'Newtonian*'
        choice_b = 'Front feed'
        choice_c = 'Offset feed'
        choice_d = 'Cassegrain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is NOT a valid parabolic dish illumination arrangement?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_502:
    def __init__(self, *args, **kwargs):
        choice_a = 'all the received energy is focused to a point where the pick-up antenna is located*'
        choice_b = 'a dipole antenna can be used to pick up the received energy'
        choice_c = 'no impedance matching is required'
        choice_d = 'a horn-type radiator can be used to trap the received energy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parabolic antenna is very efficient because:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_503:
    def __init__(self, *args, **kwargs):
        choice_a = 'right-hand polarization*'
        choice_b = 'left-hand polarization'
        choice_c = 'vertical polarization only'
        choice_d = 'horizontal polarization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A helical-beam antenna with right-hand polarization will best receive signals with:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_504:
    def __init__(self, *args, **kwargs):
        choice_a = 'helical-beam antenna*'
        choice_b = 'folded dipole antenna'
        choice_c = 'ground-plane antenna'
        choice_d = 'quad antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One antenna which will respond simultaneously to vertically- and horizontally-polarized signals is the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_505:
    def __init__(self, *args, **kwargs):
        choice_a = '0.1 lambda*'
        choice_b = '0.25 lambda'
        choice_c = '5 mm (0.2 in) regardless of frequency'
        choice_d = '1% of the diameter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In amateur work, what is the surface error upper limit you should try not to exceed on a parabolic reflector?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_506:
    def __init__(self, *args, **kwargs):
        choice_a = 'the diameter of the antenna in wavelengths*'
        choice_b = 'the polarization of the feed device illuminating it'
        choice_c = 'the focal length of the antenna'
        choice_d = 'the material composition of the dish'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You want to convert a surplus parabolic dish for amateur radio use, the gain of this antenna depends on:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_507:
    def __init__(self, *args, **kwargs):
        choice_a = '200 watts*'
        choice_b = '350 watts'
        choice_c = '400 watts'
        choice_d = '300 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmitter has an output of 100 watts. The cable and connectors have a composite loss of 3 dB, and the antenna has a gain of 6 dBd. What is the Effective Radiated Power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_508:
    def __init__(self, *args, **kwargs):
        choice_a = 'dielectric and conductor heat losses*'
        choice_b = 'high antenna currents'
        choice_c = 'high antenna voltage'
        choice_d = 'leakage to ground through the dielectric'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" As standing wave ratio rises, so does the loss in the transmission line. This is caused by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_509:
    def __init__(self, *args, **kwargs):
        choice_a = '390 watts*'
        choice_b = '197 watts'
        choice_c = '228 watts'
        choice_d = '178 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the Effective Radiated Power of an amateur transmitter, if the transmitter output power is 200 watts, the transmission line loss is 5 watts, and the antenna power gain is 3 dBd?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_510:
    def __init__(self, *args, **kwargs):
        choice_a = 'transmitter output power, minus line losses, plus antenna gain relative to a dipole*'
        choice_b = 'power supplied to the antenna before the modulation of the carrier'
        choice_c = 'power supplied to the transmission line plus antenna gain'
        choice_d = 'ratio of signal output power to signal input power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Effective Radiated Power means the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_511:
    def __init__(self, *args, **kwargs):
        choice_a = '800 watts*'
        choice_b = '3200 watts'
        choice_c = '1600 watts'
        choice_d = '400 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmitter has an output power of 200 watts. The coaxial and connector losses are 3 dB in total, and the antenna gain is 9 dBd. What is the approximate Effective Radiated Power of this system?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_512:
    def __init__(self, *args, **kwargs):
        choice_a = '200 watts*'
        choice_b = '800 watts'
        choice_c = '400 watts'
        choice_d = '100 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmitter has a power output of 100 watts. There is a loss of 1.30 dB in the transmission line, a loss of 0.2 dB through the antenna tuner, and a gain of 4.50 dBd in the antenna. The Effective Radiated Power (ERP) is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_513:
    def __init__(self, *args, **kwargs):
        choice_a = 'double*'
        choice_b = 'decrease by 3 watts'
        choice_c = 'remain the same'
        choice_d = 'be cut in half'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the overall gain of an amateur station is increased by 3 dB the ERP (Effective Radiated Power) will:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_514:
    def __init__(self, *args, **kwargs):
        choice_a = '1000*'
        choice_b = '1250'
        choice_c = '1125'
        choice_d = '134'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmitter has a power output of 125 watts. There is a loss of 0.8 dB in the transmission line, 0.2 dB in the antenna tuner, and a gain of 10 dBd in the antenna. The Effective Radiated Power (ERP) is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_515:
    def __init__(self, *args, **kwargs):
        choice_a = '4*'
        choice_b = '6'
        choice_c = '1.5'
        choice_d = '2'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a 3 dBd gain antenna is replaced with a 9 dBd gain antenna, with no other changes, the Effective Radiated Power (ERP) will increase by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_516:
    def __init__(self, *args, **kwargs):
        choice_a = '16 000*'
        choice_b = '18 000'
        choice_c = '20 000'
        choice_d = '2009'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmitter has an output of 2000 watts PEP. The transmission line, connectors and antenna tuner have a composite loss of 1 dB, and the gain from the stacked Yagi antenna is 10 dBd. What is the Effective Radiated Power (ERP) in watts PEP?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_517:
    def __init__(self, *args, **kwargs):
        choice_a = '8000*'
        choice_b = '1009'
        choice_c = '10 000'
        choice_d = '9000'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A transmitter has an output of 1000 watts PEP. The coaxial cable, connectors and antenna tuner have a composite loss of 1 dB, and the antenna gain is 10 dBd. What is the Effective Radiated Power (ERP) in watts PEP?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_518:
    def __init__(self, *args, **kwargs):
        choice_a = 'It decreases with increasing height*'
        choice_b = 'It increases with increasing height'
        choice_c = 'It does not vary with height'
        choice_d = 'It depends on E-region height, not antenna height'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For a 3-element Yagi antenna with horizontally mounted elements, how does the main lobe takeoff angle vary with height above flat ground?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_519:
    def __init__(self, *args, **kwargs):
        choice_a = 'a half wavelength or more above the ground*'
        choice_b = 'an eighth of a wavelength above the ground'
        choice_c = 'center of the driven element'
        choice_d = 'three-eighths of a wavelength above the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Most simple horizontally polarized antennas do not exhibit significant directivity unless they are:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_520:
    def __init__(self, *args, **kwargs):
        choice_a = 'several centimeters to as much as 2 meters below ground, depending upon soil conditions*'
        choice_b = 'as much as 6 cm below ground depending upon soil conditions'
        choice_c = 'as much as a meter above ground'
        choice_d = 'at ground level exactly'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The plane from which ground reflections can be considered to take place, or the effective ground plane for an antenna is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_521:
    def __init__(self, *args, **kwargs):
        choice_a = 'The vertical radiation angle is lower*'
        choice_b = 'The radiation resistance is lower'
        choice_c = 'It has an omnidirectional characteristic'
        choice_d = 'It uses vertical polarization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is a ground-mounted vertical quarter-wave antenna in reasonably open surroundings better for long distance contacts than a half-wave dipole at a quarter wavelength above ground?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_522:
    def __init__(self, *args, **kwargs):
        choice_a = 'vertical or upward radiation is effectively cancelled*'
        choice_b = 'radiation pattern changes to produce side lobes at 15 and 50 degrees'
        choice_c = 'side lobe radiation is cancelled'
        choice_d = 'radiation pattern is unaffected'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a half-wave dipole antenna is installed one-half wavelength above ground, the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_523:
    def __init__(self, *args, **kwargs):
        choice_a = 'If the antenna is less than one-half wavelength high, reflected radio waves from the ground significantly distort the pattern*'
        choice_b = 'Antenna height has no effect on the pattern'
        choice_c = 'If the antenna is less than one-half wavelength high, radiation off the ends of the wire is eliminated'
        choice_d = 'If the antenna is too high, the pattern becomes unpredictable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does antenna height affect the horizontal (azimuthal) radiation pattern of a horizontal dipole HF antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_524:
    def __init__(self, *args, **kwargs):
        choice_a = 'less than 30 degrees*'
        choice_b = 'more than 45 degrees but less than 90 degrees'
        choice_c = '90 degrees'
        choice_d = 'more than 30 degrees but less than 45 degrees'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For long distance propagation, the vertical radiation angle of the energy from the antenna should be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_525:
    def __init__(self, *args, **kwargs):
        choice_a = 'vertical radiation angle of the antenna*'
        choice_b = 'power applied to the antenna'
        choice_c = 'main height of the antenna'
        choice_d = 'length of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Greater distance can be covered with multiple-hop transmissions by decreasing the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_526:
    def __init__(self, *args, **kwargs):
        choice_a = '75 ohms*'
        choice_b = '25 ohms'
        choice_c = '300 ohms'
        choice_d = '600 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The impedance at the centre of a dipole antenna more than 3 wavelengths above ground would be nearest to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_527:
    def __init__(self, *args, **kwargs):
        choice_a = 'The ground tends to act as a reflector*'
        choice_b = 'Lower antenna noise temperature'
        choice_c = 'Low radiation angle for closer distances'
        choice_d = 'The radiation resistance is higher'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why can a horizontal antenna closer to ground be advantageous for close range communications on lower HF bands?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_528:
    def __init__(self, *args, **kwargs):
        choice_a = 'A horizontal antenna less than 1/4 wavelength above ground and a frequency below the current critical frequency*'
        choice_b = 'A horizontal antenna at a height of half a wavelength and an operating frequency at the optimum working frequency'
        choice_c = 'A vertical antenna and a frequency below the maximum usable frequency'
        choice_d = 'A vertical antenna and a frequency above the lowest usable frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" Which antenna system and operating frequency are most suitable for Near Vertical Incidence (NVIS) communications?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_529:
    def __init__(self, *args, **kwargs):
        choice_a = 'The equivalent resistance that would dissipate the same amount of power as that radiated from an antenna*'
        choice_b = 'The resistance in the atmosphere that an antenna must overcome to be able to radiate a signal'
        choice_c = 'The specific impedance of an antenna'
        choice_d = 'The combined losses of the antenna elements and transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by the radiation resistance of an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_530:
    def __init__(self, *args, **kwargs):
        choice_a = 'To match impedances for maximum power transfer*'
        choice_b = 'To measure the near-field radiation density from a transmitting antenna'
        choice_c = 'To calculate the front-to-side ratio of the antenna'
        choice_d = 'To calculate the front-to-back ratio of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why would one need to know the radiation resistance of an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_531:
    def __init__(self, *args, **kwargs):
        choice_a = 'Antenna location with respect to nearby objects and the conductors length/diameter ratio*'
        choice_b = 'Transmission line length and antenna height'
        choice_c = 'Sunspot activity and time of day'
        choice_d = 'It is a physical constant and is the same for all antennas'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What factors determine the radiation resistance of an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_532:
    def __init__(self, *args, **kwargs):
        choice_a = 'Antenna efficiency*'
        choice_b = 'Beamwidth'
        choice_c = 'Effective Radiated Power'
        choice_d = 'Radiation conversion loss'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term for the ratio of the radiation resistance of an antenna to the total resistance of the system?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_533:
    def __init__(self, *args, **kwargs):
        choice_a = 'Radiation resistance plus ohmic resistance*'
        choice_b = 'Radiation resistance plus transmission resistance'
        choice_c = 'Transmission line resistance plus radiation resistance'
        choice_d = 'Radiation resistance plus space impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is included in the total resistance of an antenna system?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_534:
    def __init__(self, *args, **kwargs):
        choice_a = 'Note the two points where the signal strength is down 3 dB from the maximum signal point and compute the angular difference*'
        choice_b = 'Draw two imaginary lines through the ends of the elements and measure the angle between the lines'
        choice_c = 'Measure the ratio of the signal strengths of the radiated power lobes from the front and side of the antenna'
        choice_d = 'Measure the ratio of the signal strengths of the radiated power lobes from the front and rear of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can the approximate beamwidth of a beam antenna be determined?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_535:
    def __init__(self, *args, **kwargs):
        choice_a = '(radiation resistance / total resistance) x 100*'
        choice_b = '(radiation resistance / transmission resistance) x 100'
        choice_c = '(total resistance / radiation resistance) x 100'
        choice_d = '(effective radiated power / transmitter output) x 100'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How is antenna percent efficiency calculated?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_536:
    def __init__(self, *args, **kwargs):
        choice_a = 'Radiation resistance*'
        choice_b = 'j factor'
        choice_c = 'Antenna resistance'
        choice_d = 'K factor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term used for an equivalent resistance which would dissipate the same amount of energy as that radiated from an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_537:
    def __init__(self, *args, **kwargs):
        choice_a = 'the points on the major lobe at the half-power points*'
        choice_b = 'the maximum lobe spread points on the major lobe'
        choice_c = 'the 6 dB power points on the major lobe'
        choice_d = 'the 3 dB power points on the first minor lobe'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Antenna beamwidth is the angular distance between:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_538:
    def __init__(self, *args, **kwargs):
        choice_a = '97.3%*'
        choice_b = '74%'
        choice_c = '72%'
        choice_d = '100%'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the ohmic resistance of a half-wave dipole is 2 ohms, and the radiation resistance is 72 ohms, what is the antenna efficiency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_539:
    def __init__(self, *args, **kwargs):
        choice_a = '96.15%*'
        choice_b = '52%'
        choice_c = '25%'
        choice_d = '50%'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the ohmic resistance of a miniloop antenna is 2 milliohms and the radiation resistance is 50 milliohms, what is the antenna efficiency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_540:
    def __init__(self, *args, **kwargs):
        choice_a = 'at frequencies above 3000 MHz*'
        choice_b = 'at frequencies above 2 MHz'
        choice_c = 'at frequencies below 150 MHz'
        choice_d = 'at frequencies below 1500 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Waveguide is typically used:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_541:
    def __init__(self, *args, **kwargs):
        choice_a = 'low hysteresis loss*'
        choice_b = 'low radiation loss'
        choice_c = 'low dielectric loss'
        choice_d = 'low copper loss'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not correct? Waveguide is an efficient transmission medium because it features:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_542:
    def __init__(self, *args, **kwargs):
        choice_a = 'Low loss*'
        choice_b = 'Frequency sensitive based on dimensions'
        choice_c = 'Expensive'
        choice_d = 'Heavy and difficult to install'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is an advantage of waveguide as a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_543:
    def __init__(self, *args, **kwargs):
        choice_a = 'one-half wavelength*'
        choice_b = 'three-eighths wavelength'
        choice_c = 'one-eighth wavelength'
        choice_d = 'one-quarter wavelength'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For rectangular waveguide to transfer energy, the cross-section should be at least:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_544:
    def __init__(self, *args, **kwargs):
        choice_a = 'Waveguide has high loss at high frequencies, but low loss below cutoff frequency*'
        choice_b = 'In the transverse electric mode, a component of the magnetic field is in the direction of propagation'
        choice_c = 'In the transverse magnetic mode, a component of the electric field is in the direction of propagation'
        choice_d = 'Waveguide has low loss at high frequencies, but high loss below cutoff frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following statements about waveguide IS NOT correct?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_545:
    def __init__(self, *args, **kwargs):
        choice_a = 'Very low losses*'
        choice_b = 'Frequency response from 1.8 MHz to 24GHz'
        choice_c = 'Easy to install'
        choice_d = 'Inexpensive to install'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is a major advantage of waveguide over coaxial cable for use at microwave frequencies?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_546:
    def __init__(self, *args, **kwargs):
        choice_a = 'Microstripline*'
        choice_b = 'Dielectric substrate'
        choice_c = 'Dielectric imprinting'
        choice_d = 'Ground plane'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is printed circuit transmission line called?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_547:
    def __init__(self, *args, **kwargs):
        choice_a = 'has poorer shielding*'
        choice_b = 'has superior shielding'
        choice_c = 'must have much lower characteristic impedance'
        choice_d = 'must have much higher characteristic impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Compared with coaxial cable, microstripline:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_548:
    def __init__(self, *args, **kwargs):
        choice_a = 'operates like a high-pass filter*'
        choice_b = 'operates like a low-pass filter'
        choice_c = 'operates like a band-stop filter'
        choice_d = 'is lightweight and easy to install'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A section of waveguide:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_549:
    def __init__(self, *args, **kwargs):
        choice_a = 'printed circuit transmission line*'
        choice_b = 'small semiconductor family'
        choice_c = 'high power microwave antenna'
        choice_d = 'family of fluids for removing coatings from small parts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Stripline is a:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_1_550:
    def __init__(self, *args, **kwargs):
        choice_a = 'Be sure the transmitter is turned off and the power source is disconnected*'
        choice_b = 'Be sure the weather is dry and sunny'
        choice_c = 'Be sure propagation conditions are unfavourable for tropospheric ducting'
        choice_d = 'Be sure to wear tight-fitting clothes and gloves to protect your body and hands from sharp edges'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What precautions should you take before beginning repairs on a microwave feed horn or waveguide?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_289:
    def __init__(self, *args, **kwargs):
        choice_a = 'as close as possible to the transceiver output*'
        choice_b = 'as close as possible to the antenna tuner output'
        choice_c = 'as close as possible to the antenna'
        choice_d = 'midway between the transceiver and antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A low pass filter in an HF station is most effective when connected:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_290:
    def __init__(self, *args, **kwargs):
        choice_a = 'as close as possible to the linear amplifier output*'
        choice_b = 'as close as possible to the antenna'
        choice_c = 'as close as possible to the antenna tuner output'
        choice_d = 'as close as possible to the linear amplifier input'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A low pass filter in an HF station is most effective when connected:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_291:
    def __init__(self, *args, **kwargs):
        choice_a = 'Low pass filter*'
        choice_b = 'Dummy load'
        choice_c = 'Antenna switch'
        choice_d = 'SWR bridge'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In designing an HF station, which component would you use to reduce the effects of harmonic radiation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_292:
    def __init__(self, *args, **kwargs):
        choice_a = 'SWR bridge*'
        choice_b = 'Antenna switch'
        choice_c = 'Linear amplifier'
        choice_d = 'Dummy load'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which component in an HF station is the most useful for determining the effectiveness of the antenna system?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_293:
    def __init__(self, *args, **kwargs):
        choice_a = 'Antenna switch*'
        choice_b = 'Transceiver'
        choice_c = 'Low pass filter'
        choice_d = 'SWR bridge'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Of the components in an HF station, which component would normally be connected closest to the antenna, antenna tuner and dummy load?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_294:
    def __init__(self, *args, **kwargs):
        choice_a = 'Antenna tuner*'
        choice_b = 'Antenna switch'
        choice_c = 'Dummy load'
        choice_d = 'SWR bridge'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Of the components in an HF station, which component would be used to match impedances between the transceiver and antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_295:
    def __init__(self, *args, **kwargs):
        choice_a = 'Dummy load*'
        choice_b = 'SWR bridge'
        choice_c = 'Low pass filter'
        choice_d = 'Antenna tuner'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an HF station, which component is temporarily connected in the tuning process or for adjustments to the transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_296:
    def __init__(self, *args, **kwargs):
        choice_a = 'most antennas when operating below 14 MHz*'
        choice_b = 'most antennas when operating above 14 MHz'
        choice_c = 'mono-band Yagi type antennas'
        choice_d = 'tri-band Yagi antennas'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an HF station, the antenna tuner is usually used for matching the transceiver with:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_297:
    def __init__(self, *args, **kwargs):
        choice_a = 'with most antennas when operating below 14 MHz*'
        choice_b = 'with most antennas when operating above 14 MHz'
        choice_c = 'to tune into dummy loads'
        choice_d = 'to tune low pass filters'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an HF Station, the antenna tuner is commonly used:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_298:
    def __init__(self, *args, **kwargs):
        choice_a = 'microphone*'
        choice_b = 'modulator'
        choice_c = 'power amplifier'
        choice_d = 'frequency multiplier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the input to the speech amplifier is connected to the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_299:
    def __init__(self, *args, **kwargs):
        choice_a = 'speech amplifier*'
        choice_b = 'modulator'
        choice_c = 'power amplifier'
        choice_d = 'oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the microphone is connected to the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_300:
    def __init__(self, *args, **kwargs):
        choice_a = 'modulator*'
        choice_b = 'power amplifier'
        choice_c = 'microphone'
        choice_d = 'frequency multiplier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the ____________is in between the speech amplifier and the oscillator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_301:
    def __init__(self, *args, **kwargs):
        choice_a = 'oscillator*'
        choice_b = 'speech amplifier'
        choice_c = 'power amplifier'
        choice_d = 'microphone'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the __________is located between the modulator and the frequency multiplier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_302:
    def __init__(self, *args, **kwargs):
        choice_a = 'frequency multiplier*'
        choice_b = 'microphone'
        choice_c = 'speech amplifier'
        choice_d = 'speech amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the ___________is located between the oscillator and the power amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_303:
    def __init__(self, *args, **kwargs):
        choice_a = 'power amplifier*'
        choice_b = 'modulator'
        choice_c = 'speech amplifier'
        choice_d = 'oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the _________ is located between the frequency multiplier and the antenna."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_304:
    def __init__(self, *args, **kwargs):
        choice_a = 'antenna*'
        choice_b = 'frequency multiplier'
        choice_c = 'microphone'
        choice_d = 'modulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation transmitter, the power amplifier output is connected to the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_305:
    def __init__(self, *args, **kwargs):
        choice_a = 'antenna*'
        choice_b = 'mixer'
        choice_c = 'frequency discriminator'
        choice_d = 'limiter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the ________is connected to the input of the radio frequency amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_306:
    def __init__(self, *args, **kwargs):
        choice_a = 'radio frequency amplifier*'
        choice_b = 'audio frequency amplifier'
        choice_c = 'local oscillator'
        choice_d = 'intermediate frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the __________ is in between the antenna and the mixer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_307:
    def __init__(self, *args, **kwargs):
        choice_a = 'mixer*'
        choice_b = 'radio frequency amplifier'
        choice_c = 'limiter'
        choice_d = 'antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the output of the local oscillator is fed to the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_308:
    def __init__(self, *args, **kwargs):
        choice_a = 'local oscillator*'
        choice_b = 'frequency discriminator'
        choice_c = 'intermediate frequency amplifier'
        choice_d = 'speaker or headphones'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the output of the ________is connected to the mixer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_309:
    def __init__(self, *args, **kwargs):
        choice_a = 'filter*'
        choice_b = 'limiter'
        choice_c = 'frequency discriminator'
        choice_d = 'radio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the_________ is in between the mixer and the intermediate frequency amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_310:
    def __init__(self, *args, **kwargs):
        choice_a = 'intermediate frequency amplifier*'
        choice_b = 'local oscillator'
        choice_c = 'mixer'
        choice_d = 'radio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the ________ is located between the filter and the limiter."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_311:
    def __init__(self, *args, **kwargs):
        choice_a = 'limiter*'
        choice_b = 'filter'
        choice_c = 'local oscillator'
        choice_d = 'radio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the__________ is in between the intermediate frequency amplifier and the frequency discriminator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_312:
    def __init__(self, *args, **kwargs):
        choice_a = 'frequency discriminator*'
        choice_b = 'intermediate frequency amplifier'
        choice_c = 'speaker or headphones'
        choice_d = 'local oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the __________ is located between the limiter and the audio frequency amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_313:
    def __init__(self, *args, **kwargs):
        choice_a = 'audio frequency amplifier*'
        choice_b = 'limiter'
        choice_c = 'intermediate frequency amplifier'
        choice_d = 'radio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the _________ is located between the speaker or headphones and the frequency discriminator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_314:
    def __init__(self, *args, **kwargs):
        choice_a = 'speaker or headphones*'
        choice_b = 'intermediate frequency amplifier'
        choice_c = 'frequency discriminator'
        choice_d = 'limiter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a frequency modulation receiver, the __________ connects to the audio frequency amplifier output."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_315:
    def __init__(self, *args, **kwargs):
        choice_a = 'master oscillator*'
        choice_b = 'power amplifier'
        choice_c = 'telegraph key'
        choice_d = 'power supply'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a CW transmitter, the output from the __________ is connected to the driver/buffer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_316:
    def __init__(self, *args, **kwargs):
        choice_a = 'power supply*'
        choice_b = 'driver/buffer'
        choice_c = 'power amplifier'
        choice_d = 'master oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a typical CW transmitter, the ___________ is the primary source of direct current."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_317:
    def __init__(self, *args, **kwargs):
        choice_a = 'driver/buffer*'
        choice_b = 'audio amplifier'
        choice_c = 'power supply'
        choice_d = 'telegraph key'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a CW transmitter, the_________ is between the master oscillator and the power amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_318:
    def __init__(self, *args, **kwargs):
        choice_a = 'telegraph key*'
        choice_b = 'master oscillator'
        choice_c = 'driver/buffer'
        choice_d = 'power amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" In a CW transmitter, the_____________ controls when RF energy is applied to the antenna."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_319:
    def __init__(self, *args, **kwargs):
        choice_a = 'power amplifier*'
        choice_b = 'power supply'
        choice_c = 'telegraph key'
        choice_d = 'master oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a CW transmitter, the ______________ is in between the driver/buffer stage and the antenna."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_320:
    def __init__(self, *args, **kwargs):
        choice_a = 'power amplifier*'
        choice_b = 'driver/buffer'
        choice_c = 'power supply'
        choice_d = 'master oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a CW transmitter, the output of the _____________ is transferred to the antenna."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_321:
    def __init__(self, *args, **kwargs):
        choice_a = 'radio frequency amplifier*'
        choice_b = 'product detector'
        choice_c = 'local oscillator'
        choice_d = 'intermediate frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the antenna is connected to the ____________ ."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_322:
    def __init__(self, *args, **kwargs):
        choice_a = 'radio frequency amplifier*'
        choice_b = 'filter'
        choice_c = 'intermediate frequency amplifier'
        choice_d = 'audio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the output of the _____________ is connected to the mixer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_323:
    def __init__(self, *args, **kwargs):
        choice_a = 'mixer*'
        choice_b = 'beat frequency oscillator'
        choice_c = 'product detector'
        choice_d = 'filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the __________ is connected to the radio frequency amplifier and the local oscillator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_324:
    def __init__(self, *args, **kwargs):
        choice_a = 'local oscillator*'
        choice_b = 'intermediate frequency amplifier'
        choice_c = 'beat frequency oscillator'
        choice_d = 'product detector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the output of the ___________ is connected to the mixer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_325:
    def __init__(self, *args, **kwargs):
        choice_a = 'filter*'
        choice_b = 'radio frequency amplifier'
        choice_c = 'beat frequency oscillator'
        choice_d = 'product detector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the _____________ is in between the mixer and intermediate frequency amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_326:
    def __init__(self, *args, **kwargs):
        choice_a = 'intermediate frequency amplifier*'
        choice_b = 'audio frequency amplifier'
        choice_c = 'beat frequency oscillator'
        choice_d = 'radio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the __________ is in between the filter and product detector."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_327:
    def __init__(self, *args, **kwargs):
        choice_a = 'product detector*'
        choice_b = 'local oscillator'
        choice_c = 'beat frequency oscillator'
        choice_d = 'intermediate frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the __________ output is connected to the audio frequency amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_328:
    def __init__(self, *args, **kwargs):
        choice_a = 'beat frequency oscillator*'
        choice_b = 'mixer'
        choice_c = 'radio frequency amplifier'
        choice_d = 'audio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the output of the ___________ is connected to the product detector."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_329:
    def __init__(self, *args, **kwargs):
        choice_a = 'audio frequency amplifier*'
        choice_b = 'intermediate frequency amplifier'
        choice_c = 'local oscillator'
        choice_d = 'radio frequency amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the __________ is connected to the output of the product detector."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_330:
    def __init__(self, *args, **kwargs):
        choice_a = 'speaker or headphones*'
        choice_b = 'mixer'
        choice_c = 'radio frequency amplifier'
        choice_d = 'beat frequency oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband and CW receiver, the __________ is connected to the output of the audio frequency amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_331:
    def __init__(self, *args, **kwargs):
        choice_a = 'radio frequency oscillator*'
        choice_b = 'variable frequency oscillator'
        choice_c = 'linear amplifier'
        choice_d = 'mixer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the output of the ________ is connected to the balanced modulator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_332:
    def __init__(self, *args, **kwargs):
        choice_a = 'balanced modulator*'
        choice_b = 'microphone'
        choice_c = 'mixer'
        choice_d = 'radio frequency oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the output of the ____________ is connected to the filter."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_333:
    def __init__(self, *args, **kwargs):
        choice_a = 'filter*'
        choice_b = 'radio frequency oscillator'
        choice_c = 'speech amplifier'
        choice_d = 'microphone'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the _____________ is in between the balanced modulator and the mixer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_334:
    def __init__(self, *args, **kwargs):
        choice_a = 'microphone*'
        choice_b = 'radio frequency oscillator'
        choice_c = 'filter'
        choice_d = 'mixer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the ______________ is connected to the speech amplifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_335:
    def __init__(self, *args, **kwargs):
        choice_a = 'speech amplifier*'
        choice_b = 'filter'
        choice_c = 'variable frequency oscillator'
        choice_d = 'linear amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the output of the ___________ is connected to the balanced modulator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_336:
    def __init__(self, *args, **kwargs):
        choice_a = 'mixer*'
        choice_b = 'antenna'
        choice_c = 'balanced modulator'
        choice_d = 'linear amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the output of the variable frequency oscillator is connected to the __________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_337:
    def __init__(self, *args, **kwargs):
        choice_a = 'variable frequency oscillator*'
        choice_b = 'radio frequency oscillator'
        choice_c = 'linear amplifier'
        choice_d = 'antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the output of the _________ is connected to the mixer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_338:
    def __init__(self, *args, **kwargs):
        choice_a = 'linear amplifier*'
        choice_b = 'variable frequency oscillator'
        choice_c = 'balanced modulator'
        choice_d = 'radio frequency oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an single sideband transmitter, the ____________ is in between the mixer and the antenna."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_339:
    def __init__(self, *args, **kwargs):
        choice_a = 'antenna*'
        choice_b = 'filter'
        choice_c = 'variable frequency oscillator'
        choice_d = 'speech amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a single sideband transmitter, the output of the linear amplifier is connected to the ______________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_340:
    def __init__(self, *args, **kwargs):
        choice_a = 'input/output*'
        choice_b = 'antenna'
        choice_c = 'power supply'
        choice_d = 'transceiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an amateur digital radio system, the __________________interfaces with the computer."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_341:
    def __init__(self, *args, **kwargs):
        choice_a = 'computer*'
        choice_b = 'amplifier'
        choice_c = 'antenna'
        choice_d = 'input/output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an amateur digital radio system, the modem is connected to the ________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_342:
    def __init__(self, *args, **kwargs):
        choice_a = 'modem*'
        choice_b = 'computer'
        choice_c = 'scanner'
        choice_d = 'input/output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an amateur digital radio system, the transceiver is connected to the ___________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_343:
    def __init__(self, *args, **kwargs):
        choice_a = 'transceiver*'
        choice_b = 'input/output'
        choice_c = 'scanner'
        choice_d = 'antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an amateur digital radio system, the audio connections of the modem/sound card are connected to the ___________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_344:
    def __init__(self, *args, **kwargs):
        choice_a = 'sound card*'
        choice_b = 'keyboard'
        choice_c = 'scanner'
        choice_d = 'serial port'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In an amateur digital radio system, the modem function is often performed by the computer____________ ."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_345:
    def __init__(self, *args, **kwargs):
        choice_a = 'input*'
        choice_b = 'reflector'
        choice_c = 'driven element'
        choice_d = 'director'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a regulated power supply, the transformer connects to an external source which is referred to as______________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_346:
    def __init__(self, *args, **kwargs):
        choice_a = 'transformer*'
        choice_b = 'output'
        choice_c = 'regulator'
        choice_d = 'filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a regulated power supply, the _______________ is between the input and the rectifier."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_347:
    def __init__(self, *args, **kwargs):
        choice_a = 'rectifier*'
        choice_b = 'input'
        choice_c = 'output'
        choice_d = 'regulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a regulated power supply, the _______________ is between the transformer and the filter."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_348:
    def __init__(self, *args, **kwargs):
        choice_a = 'filter*'
        choice_b = 'output'
        choice_c = 'transformer'
        choice_d = 'regulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a regulated power supply, the output of the rectifier is connected to the ______________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_349:
    def __init__(self, *args, **kwargs):
        choice_a = 'regulator*'
        choice_b = 'transformer'
        choice_c = 'rectifier'
        choice_d = 'output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a regulated power supply, the output of the filter connects to the ____________________."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_350:
    def __init__(self, *args, **kwargs):
        choice_a = 'output*'
        choice_b = 'rectifier'
        choice_c = 'input'
        choice_d = 'transformer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a regulated power supply, the _______________is connected to the regulator."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_351:
    def __init__(self, *args, **kwargs):
        choice_a = 'boom*'
        choice_b = 'reflector'
        choice_c = 'driven element'
        choice_d = 'director'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a Yagi 3 element directional antenna, the ____________ is primarily for mechanical support purposes."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_352:
    def __init__(self, *args, **kwargs):
        choice_a = 'reflector*'
        choice_b = 'director'
        choice_c = 'driven element'
        choice_d = 'boom'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a Yagi 3 element directional antenna, the ________ is the longest radiating element."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_353:
    def __init__(self, *args, **kwargs):
        choice_a = 'director*'
        choice_b = 'boom'
        choice_c = 'reflector'
        choice_d = 'driven element'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a Yagi 3 element directional antenna, the ______________ is the shortest radiating element."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_354:
    def __init__(self, *args, **kwargs):
        choice_a = 'driven element*'
        choice_b = 'boom'
        choice_c = 'director'
        choice_d = 'reflector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a Yagi 3 element directional antenna, the ______________is not the longest nor the shortest radiating element."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_355:
    def __init__(self, *args, **kwargs):
        choice_a = 'CW, RTTY, SSB voice, FM voice*'
        choice_b = 'CW, SSB voice, RTTY, FM voice'
        choice_c = 'CW, FM voice, RTTY, SSB voice'
        choice_d = 'RTTY, CW, SSB voice, FM voice'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which list of emission types is in order from the narrowest bandwidth to the widest bandwidth?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_356:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF input signal needed to achieve a given signal plus noise to noise ratio'
        choice_b = 'audio output in watts'
        choice_c = 'bandwidth of the IF in kilohertz'
        choice_d = 'number of RF amplifiers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The figure in a receiver's specifications which indicates its sensitivity is the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_357:
    def __init__(self, *args, **kwargs):
        choice_a = 'less signal or more noise*'
        choice_b = 'a steady oscillator drift'
        choice_c = 'more than one signal'
        choice_d = 'more signal or less noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If two receivers of different sensitivity are compared, the less sensitive receiver will produce:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_358:
    def __init__(self, *args, **kwargs):
        choice_a = 'Single sideband suppressed carrier*'
        choice_b = 'Double sideband full carrier'
        choice_c = 'Frequency modulation'
        choice_d = 'Pulse modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following modes of transmission is usually detected with a product detector?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_359:
    def __init__(self, *args, **kwargs):
        choice_a = 'the suppressed carrier must be replaced for detection*'
        choice_b = 'it beats with the received carrier to produce the other sideband'
        choice_c = 'it reduces the passband of the IF stages'
        choice_d = 'it phases out the unwanted sideband signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A receiver designed for SSB reception must have a BFO (beat frequency oscillator) because:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_360:
    def __init__(self, *args, **kwargs):
        choice_a = '455 kHz*'
        choice_b = '7.435 MHz'
        choice_c = '3.995 MHz'
        choice_d = '3.54 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A receiver receives an incoming signal of 3.54 MHz, and the local oscillator produces a signal of 3.995 MHz. To which frequency should the IF be tuned?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_361:
    def __init__(self, *args, **kwargs):
        choice_a = 'A notch filter*'
        choice_b = 'A band pass filter'
        choice_c = 'An all pass filter'
        choice_d = 'A pi-network filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of filter would you use to attenuate an interfering carrier signal while receiving an SSB transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_362:
    def __init__(self, *args, **kwargs):
        choice_a = 'sensitivity, selectivity and stability*'
        choice_b = 'selectivity, stability and frequency range'
        choice_c = 'sensitivity, stability and cross-modulation'
        choice_d = 'sensitivity, selectivity and image rejection'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The three main parameters against which the quality of a receiver is measured are:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_363:
    def __init__(self, *args, **kwargs):
        choice_a = '2.4 kHz*'
        choice_b = '250 Hz'
        choice_c = '6 kHz'
        choice_d = '500 Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A communications receiver has four filters installed in it, respectively designated as 250 Hz, 500 Hz, 2.4 kHz, and 6 kHz. If you were listening to single sideband, which filter would you utilize?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_364:
    def __init__(self, *args, **kwargs):
        choice_a = '250 Hz*'
        choice_b = '500 Hz'
        choice_c = '2.4 kHz'
        choice_d = '6 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A communications receiver has four filters installed in it, respectively designated as 250 Hz, 500 Hz, 2.4 kHz and 6 kHz. You are copying a CW transmission and there is a great deal of interference. Which one of the filters would you choose?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_365:
    def __init__(self, *args, **kwargs):
        choice_a = '750 - 850 Hz*'
        choice_b = '2100 - 2300 Hz'
        choice_c = '300 - 2700 Hz'
        choice_d = '100 - 1100 Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Selectivity can be placed in the audio stages of a receiver by the utilization of RC active or passive audio filters. If you were to copy CW, which of the following bandpasses would you choose?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_366:
    def __init__(self, *args, **kwargs):
        choice_a = 'A small change in a transmitter\'s frequency each time it is keyed*'
        choice_b = 'A high-pitched tone which is received along with a CW signal'
        choice_c = 'A slow change in transmitter frequency as the circuit warms up'
        choice_d = 'An overload in a receiver\'s audio circuit whenever CW is received'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does chirp mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_367:
    def __init__(self, *args, **kwargs):
        choice_a = 'Keep the power supply voltages very steady under transmit load*'
        choice_b = 'Add a key-click filter'
        choice_c = 'Keep the power supply current very steady under transmit load'
        choice_d = 'Add a low pass filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What can be done to keep a CW transmitter from chirping?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_368:
    def __init__(self, *args, **kwargs):
        choice_a = 'A VFO-controlled CW transmitter*'
        choice_b = 'A crystal-controlled AM transmitter'
        choice_c = 'A single-sideband transmitter'
        choice_d = 'A digital radio transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What circuit has a variable-frequency oscillator connected to a buffer/driver and a power amplifier?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_369:
    def __init__(self, *args, **kwargs):
        choice_a = 'Amplitude modulation*'
        choice_b = 'Phase modulation'
        choice_c = 'Amplitude-rectification modulation'
        choice_d = 'Frequency modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of modulation system changes the amplitude of an RF wave for the purpose of conveying information?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_370:
    def __init__(self, *args, **kwargs):
        choice_a = 'Amplitude modulation*'
        choice_b = 'Frequency modulation'
        choice_c = 'Pulse modulation'
        choice_d = 'Frequency shift keying'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In what emission type does the instantaneous amplitude (envelope) of the RF signal vary in accordance with the modulating audio?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_371:
    def __init__(self, *args, **kwargs):
        choice_a = 'an interrupted carrier*'
        choice_b = 'a series of key-clicks'
        choice_c = 'a continuous carrier'
        choice_d = 'a voice-modulated carrier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Morse code is usually transmitted by radio as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_372:
    def __init__(self, *args, **kwargs):
        choice_a = 'full power will not be transferred to the antenna*'
        choice_b = 'loss of modulation in the transmitted signal'
        choice_c = 'the driver stage will not deliver power to the final'
        choice_d = 'the output tank circuit breaks down'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A mismatched antenna or transmission line may present an incorrect load to the transmitter. The result may be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_373:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduced antenna radiation*'
        choice_b = 'smaller DC current drain'
        choice_c = 'lower modulation percentage'
        choice_d = 'radiated key-clicks'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One result of a slight mismatch between the power amplifier of a transmitter and the antenna would be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_374:
    def __init__(self, *args, **kwargs):
        choice_a = 'drift in frequency*'
        choice_b = 'become over modulated'
        choice_c = 'generate key-clicks'
        choice_d = 'cause undue distortion'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An RF oscillator should be electrically and mechanically stable. This is to ensure that the oscillator does not:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_375:
    def __init__(self, *args, **kwargs):
        choice_a = 'It has been dissipated as heat loss*'
        choice_b = 'It has been used to provide greater efficiency'
        choice_c = 'It has been used to provide negative feedback'
        choice_d = 'It has been used to provide positive feedback'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The input power to the final stage of your transmitter is 200 watts and the output is 125 watts. What has happened to the remaining power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_376:
    def __init__(self, *args, **kwargs):
        choice_a = 'appears as heat dissipation*'
        choice_b = 'is lost in the transmission line'
        choice_c = 'is due to oscillating'
        choice_d = 'radiates from the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The difference between DC input power and RF output power of a transmitter RF amplifier:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_377:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may cause splatter interference to other stations operating near its frequency*'
        choice_b = 'It may cause interference to other stations operating on a higher frequency band'
        choice_c = 'It may cause atmospheric interference in the air around the antenna'
        choice_d = 'It may cause digital interference to computer equipment'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What may happen if an SSB transmitter is operated with the microphone gain set too high?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_378:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may cause audio distortion or splatter interference to other stations operating near its frequency*'
        choice_b = 'It may cause digital interference to computer equipment'
        choice_c = 'It may cause atmospheric interference in the air around the antenna'
        choice_d = 'It may cause interference to other stations operating on a higher frequency band'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What may happen if an SSB transmitter is operated with too much speech processing?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_379:
    def __init__(self, *args, **kwargs):
        choice_a = 'Peak envelope power*'
        choice_b = 'Peak output power'
        choice_c = 'Average radio-frequency power'
        choice_d = 'Peak transmitter power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the term for the average power supplied to an antenna transmission line during one RF cycle, at the crest of the modulation envelope?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_380:
    def __init__(self, *args, **kwargs):
        choice_a = 'Between 2 and 3 kHz*'
        choice_b = '1 kHz'
        choice_c = '2 kHz'
        choice_d = 'Between 3 and 6 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the usual bandwidth of a single-sideband amateur signal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_381:
    def __init__(self, *args, **kwargs):
        choice_a = 'Filter*'
        choice_b = 'IF amplifier'
        choice_c = 'RF amplifier'
        choice_d = 'Carrier oscillator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a typical single-sideband phone transmitter, what circuit processes signals from the balanced modulator and sends signals to the mixer?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_382:
    def __init__(self, *args, **kwargs):
        choice_a = 'More power can be put into the sidebands for a given power amplifier capacity*'
        choice_b = 'Only half the bandwidth is required for the same information content'
        choice_c = 'Greater modulation percentage is obtainable with lower distortion'
        choice_d = 'Simpler equipment can be used to receive a double-sideband suppressed-carrier signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one advantage of carrier suppression in a double-sideband phone transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_383:
    def __init__(self, *args, **kwargs):
        choice_a = 'It becomes distorted and occupies more bandwidth*'
        choice_b = 'It becomes stronger with no other effects'
        choice_c = 'It occupies less bandwidth with poor high-frequency response'
        choice_d = 'It has higher fidelity and improved signal-to-noise ratio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What happens to the signal of an overmodulated single-sideband or double-sideband phone transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_384:
    def __init__(self, *args, **kwargs):
        choice_a = 'For slight movement of the ALC meter on modulation peaks*'
        choice_b = 'For full deflection of the ALC meter on modulation peaks'
        choice_c = 'For 100% frequency deviation on modulation peaks'
        choice_d = 'For a dip in plate current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How should the microphone gain control be adjusted on a single-sideband phone transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_385:
    def __init__(self, *args, **kwargs):
        choice_a = 'suppress the carrier and pass on the two sidebands*'
        choice_b = 'make sure that the carrier and both sidebands are 180 degrees out of phase'
        choice_c = 'ensure that the percentage of modulation is kept constant'
        choice_d = 'make sure that the carrier and both sidebands are in phase'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The purpose of a balanced modulator in an SSB transmitter is to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_386:
    def __init__(self, *args, **kwargs):
        choice_a = 'reinserted at the receiver*'
        choice_b = 'transmitted with one sideband'
        choice_c = 'inserted at the transmitter'
        choice_d = 'of no use at the receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a SSB transmission, the carrier is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_387:
    def __init__(self, *args, **kwargs):
        choice_a = 'controls the peak audio input so that the power amplifier is not overdriven*'
        choice_b = 'reduces transmitter audio feedback'
        choice_c = 'increases the occupied bandwidth'
        choice_d = 'reduces the system noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The automatic level control (ALC) in a SSB transmitter:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_388:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may cause interference to other stations operating near its frequency*'
        choice_b = 'It may cause digital interference to computer equipment'
        choice_c = 'It may cause atmospheric interference in the air around the antenna'
        choice_d = 'It may cause interference to other stations operating on a higher frequency band'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What may happen if an FM transmitter is operated with the microphone gain or deviation control set too high?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_389:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may cause interference to other stations operating near its frequency*'
        choice_b = 'It may cause digital interference to computer equipment'
        choice_c = 'It may cause atmospheric interference in the air around the antenna'
        choice_d = 'It may cause interference to other stations operating on a higher frequency band'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What may your FM hand-held or mobile transceiver do if you shout into its microphone and the deviation adjustment is set too high?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_390:
    def __init__(self, *args, **kwargs):
        choice_a = 'Talk farther away from the microphone*'
        choice_b = 'Talk louder into the microphone'
        choice_c = 'Let the transceiver cool off'
        choice_d = 'Change to a higher power level'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What can you do if you are told your FM hand-held or mobile transceiver is overdeviating?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_391:
    def __init__(self, *args, **kwargs):
        choice_a = 'An unmodulated carrier*'
        choice_b = 'A frequency-modulated carrier'
        choice_c = 'An amplitude-modulated carrier'
        choice_d = 'A phase-modulated carrier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of emission would your FM transmitter produce if its microphone failed to work?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_392:
    def __init__(self, *args, **kwargs):
        choice_a = 'It provides good signal plus noise to noise ratio at low RF signal levels*'
        choice_b = 'The carrier is not detectable'
        choice_c = 'It is more resistant to distortion caused by reflected signals'
        choice_d = 'Its RF carrier stays on frequency better than the AM modes'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is FM voice best for local VHF/UHF radio communications?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_393:
    def __init__(self, *args, **kwargs):
        choice_a = 'Between 10 and 20 kHz*'
        choice_b = 'Less than 5 kHz'
        choice_c = 'Between 5 and 10 kHz'
        choice_d = 'Greater than 20 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the usual bandwidth of a frequency-modulated amateur signal for +/- 5kHz deviation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_394:
    def __init__(self, *args, **kwargs):
        choice_a = 'Out-of-channel emissions*'
        choice_b = 'Increased transmitter power'
        choice_c = 'Increased transmitter range'
        choice_d = 'Poor carrier suppression'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the result of overdeviation in an FM transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_395:
    def __init__(self, *args, **kwargs):
        choice_a = 'Phase modulation*'
        choice_b = 'Multiplex modulation'
        choice_c = 'Amplitude modulation'
        choice_d = 'Pulse modulation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What emission is produced by a reactance modulator connected to an RF power amplifier?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_396:
    def __init__(self, *args, **kwargs):
        choice_a = 'The bandwidth would exceed limits in the Regulations*'
        choice_b = 'The transmitter efficiency for this mode is low'
        choice_c = 'Harmonics could not be attenuated to practical levels'
        choice_d = 'The frequency stability would not be adequate'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why isn't frequency modulated (FM) phone used below 28.0 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_397:
    def __init__(self, *args, **kwargs):
        choice_a = 'The frequency deviation of your transmitter is set too high*'
        choice_b = 'The power supply output voltage is low'
        choice_c = 'The repeater is reversing your sidebands'
        choice_d = 'The frequency counter is giving an incorrect reading and you are indeed off frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You are transmitting FM on the 2 metre band. Several stations advise you that your transmission is loud and distorted. A quick check with a frequency counter tells you that the transmitter is on the proper frequency. Which of the following is the most probable cause of the distortion?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_398:
    def __init__(self, *args, **kwargs):
        choice_a = 'capture effect*'
        choice_b = 'attach effect'
        choice_c = 'interference effect'
        choice_d = 'surrender effect'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""FM receivers perform in an unusual manner when two or more stations are present. The strongest signal, even though it is only two or three times stronger than the other signals, will be the only transmission demodulated. This is called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_399:
    def __init__(self, *args, **kwargs):
        choice_a = 'An electronic keyer*'
        choice_b = 'A key-operated on/off switch'
        choice_c = 'A notch filter'
        choice_d = 'A DTMF keypad'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What do many amateurs use to help form good Morse code characters?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_400:
    def __init__(self, *args, **kwargs):
        choice_a = 'To a transceiver*'
        choice_b = 'To a power supply'
        choice_c = 'To an antenna switch'
        choice_d = 'To an antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Where would you connect a microphone for voice operation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_401:
    def __init__(self, *args, **kwargs):
        choice_a = 'A microphone*'
        choice_b = 'A receiver audio filter'
        choice_c = 'A terminal-voice controller'
        choice_d = 'A splatter filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What would you connect to a transceiver for voice operation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_402:
    def __init__(self, *args, **kwargs):
        choice_a = 'Because it changes RF energy into heat*'
        choice_b = 'Because it absorbs static electricity'
        choice_c = 'Because it stores radio waves'
        choice_d = 'Because it stores electric current'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why might a dummy antenna get warm when in use?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_403:
    def __init__(self, *args, **kwargs):
        choice_a = 'VOX*'
        choice_b = 'VXO'
        choice_c = 'VCO'
        choice_d = 'VFO'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the circuit called which causes a transmitter to automatically transmit when an operator speaks into its microphone?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_404:
    def __init__(self, *args, **kwargs):
        choice_a = 'It improves signal intelligibility at the receiver*'
        choice_b = 'It reduces average transmitter power requirements'
        choice_c = 'It reduces unwanted noise pickup from the microphone'
        choice_d = 'It improves voice frequency fidelity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the reason for using a properly adjusted speech processor with a single-sideband phone transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_405:
    def __init__(self, *args, **kwargs):
        choice_a = 'It will add nothing to the output Peak Envelope Power (PEP)*'
        choice_b = 'It will increase the output PEP'
        choice_c = 'It will decrease the peak power output'
        choice_d = 'It will decrease the average power output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a single-sideband phone transmitter is 100% modulated, what will a speech processor do to the transmitter's power?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_406:
    def __init__(self, *args, **kwargs):
        choice_a = 'the receiver should be muted*'
        choice_b = 'the transmit oscillator should be turned off'
        choice_c = 'the receiving antenna should be connected'
        choice_d = 'the power supply should be off'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When switching from receive to transmit:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_407:
    def __init__(self, *args, **kwargs):
        choice_a = 'disable the unit not being used*'
        choice_b = 'ground the antenna on receive'
        choice_c = 'switch between meters'
        choice_d = 'disconnect the antenna tuner'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A switching system to enable the use of one antenna for a transmitter and receiver should also:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_408:
    def __init__(self, *args, **kwargs):
        choice_a = 'so that one antenna can be used for transmitter and receiver*'
        choice_b = 'to change antennas for operation on other frequencies'
        choice_c = 'to prevent RF currents entering the receiver circuits'
        choice_d = 'to allow more than one transmitter to be used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An antenna changeover switch in a transmitter-receiver combination is necessary:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_409:
    def __init__(self, *args, **kwargs):
        choice_a = 'Loudspeaker*'
        choice_b = 'Crystal earpiece'
        choice_c = 'Resistor'
        choice_d = 'Capacitor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following components could be used as a dynamic microphone?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_410:
    def __init__(self, *args, **kwargs):
        choice_a = 'A transmitting station is sending data to only one receiving station, it replies that the data is being received correctly*'
        choice_b = 'A telephone link is working between two stations'
        choice_c = 'A message has reached an amateur station for local delivery'
        choice_d = 'A transmitting and receiving station are using a digipeater, so no other contacts can take place until they are finished'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does "connected" mean in an AX.25 packet-radio link?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_411:
    def __init__(self, *args, **kwargs):
        choice_a = 'A receiving station is displaying messages that may not be sent to it, and is not replying to any message*'
        choice_b = 'A member of the Amateur Auxiliary is copying all messages'
        choice_c = 'A receiving station is displaying all messages sent to it, and replying that the messages are being received correctly'
        choice_d = 'Industry Philippines is monitoring all messages'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does "monitoring" mean on a packet-radio frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_412:
    def __init__(self, *args, **kwargs):
        choice_a = 'A station that retransmits only data that is marked to be retransmitted*'
        choice_b = 'A repeater built using only digital electronics parts'
        choice_c = 'A repeater that changes audio signals to digital data'
        choice_d = 'A station that retransmits any data that it receives'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a digipeater?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_413:
    def __init__(self, *args, **kwargs):
        choice_a = 'A way of connecting packet-radio stations so data can be sent over long distances*'
        choice_b = 'A way of connecting terminal-node controllers by telephone so data can be sent over long distances'
        choice_c = 'The connections on terminal-node controllers'
        choice_d = 'The programming in a terminal-node controller that rejects other callers if a station is already connected'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does "network" mean in packet radio?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_414:
    def __init__(self, *args, **kwargs):
        choice_a = 'A transceiver, a computer and possibly a GPS receiver*'
        choice_b = 'A transceiver and a modem'
        choice_c = 'A DTMF keypad, a monitor and a transceiver'
        choice_d = 'A DTMF microphone, a monitor and a transceiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In AX.25 packet-radio operation, what equipment connects to a terminal-node controller?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_415:
    def __init__(self, *args, **kwargs):
        choice_a = 'Connect a terminal-node controller to the transceiver\'s microphone input*'
        choice_b = 'Connect a terminal-node controller to interrupt the transceiver\'s carrier wave'
        choice_c = 'Connect a keyboard to the transceiver\'s microphone input'
        choice_d = 'Connect a DTMF key pad to the transceiver\'s microphone input'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How would you modulate a 2 meter FM transceiver to produce packet-radio emissions?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_416:
    def __init__(self, *args, **kwargs):
        choice_a = '250 to 500 Hz*'
        choice_b = 'Approximately 6 kHz*'
        choice_c = 'Approximately 3 kHz'
        choice_d = '60 Hz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When selecting a RTTY transmitting frequency, what minimum frequency separation from a contact in progress should you allow (center to center) to minimize interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_417:
    def __init__(self, *args, **kwargs):
        choice_a = 'mark and space*'
        choice_b = 'packet and AMTOR'
        choice_c = 'Baudot and ASCII'
        choice_d = 'dot and dash'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Digital transmissions use signals called __________ to transmit the states 1 and 0:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_418:
    def __init__(self, *args, **kwargs):
        choice_a = 'Baudot*'
        choice_b = 'ASCII'
        choice_c = 'Automatic Packet Reporting System (APRS)'
        choice_d = 'AX.25'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following terms does not apply to packet radio?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_419:
    def __init__(self, *args, **kwargs):
        choice_a = 'for communications after contact has been established*'
        choice_b = 'at all times. Mode B is for test purposes only'
        choice_c = 'only when communications have been completed'
        choice_d = 'when making a general call'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When using AMTOR transmissions, there are two modes that may be utilized. Mode A uses Automatic Repeat Request (ARQ) protocol and is normally used:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_420:
    def __init__(self, *args, **kwargs):
        choice_a = 'Splatter or out-of-channel emissions*'
        choice_b = 'Higher signal-to-noise ratio'
        choice_c = 'Lower error rate'
        choice_d = 'Power amplifier overheating'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""With a digital communication mode based on a computer sound card, what is the result of feeding too much audio in the transceiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_421:
    def __init__(self, *args, **kwargs):
        choice_a = 'About 12 volts*'
        choice_b = 'About 240 volts'
        choice_c = 'About 120 volts'
        choice_d = 'About 9 volts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How much voltage does a standard automobile battery usually supply?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_422:
    def __init__(self, *args, **kwargs):
        choice_a = 'A battery*'
        choice_b = 'A potentiometer'
        choice_c = 'A fuse'
        choice_d = 'A resistor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which component has a positive and a negative side?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_423:
    def __init__(self, *args, **kwargs):
        choice_a = 'storage cell*'
        choice_b = 'low leakage cell'
        choice_c = 'memory cell'
        choice_d = 'primary cell'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A cell, that can be repeatedly recharged by supplying it with electrical energy, is known as a:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_424:
    def __init__(self, *args, **kwargs):
        choice_a = 'lithium-ion battery*'
        choice_b = 'germanium diode'
        choice_c = 'P channel FET'
        choice_d = 'carbon resistor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is a source of electromotive force (EMF)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_425:
    def __init__(self, *args, **kwargs):
        choice_a = 'can be repeatedly recharged*'
        choice_b = 'has two terminals'
        choice_c = 'can be completely discharged'
        choice_d = 'contains an electrolyte'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An important difference between a conventional flashlight battery and a lead acid battery is that only the lead acid battery:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_426:
    def __init__(self, *args, **kwargs):
        choice_a = 'internal resistance*'
        choice_b = 'electrolyte becoming dry'
        choice_c = 'current capacity'
        choice_d = 'voltage capacity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An alkaline cell has a nominal voltage of 1.5 volts. When supplying a great deal of current, the voltage may drop to 1.2 volts. This is caused by the cell's:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_427:
    def __init__(self, *args, **kwargs):
        choice_a = 'never*'
        choice_b = 'twice'
        choice_c = 'many times'
        choice_d = 'once'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An inexpensive primary cell in use today is the carbon-zinc or flashlight cell. This type of cell can be recharged:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_428:
    def __init__(self, *args, **kwargs):
        choice_a = 'A battery charge will not last as long*'
        choice_b = 'The internal resistance of the cell is short-circuited'
        choice_c = 'The battery will accept the subsequent charge in shorter time'
        choice_d = 'The voltage delivered will be higher'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Battery capacity is commonly stated as a value of current delivered over a specified period of time. What is the effect of exceeding that specified current?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_429:
    def __init__(self, *args, **kwargs):
        choice_a = 'parallel*'
        choice_b = 'series'
        choice_c = 'parallel resonant'
        choice_d = 'series resonant'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To increase the current capacity of a cell, several cells should be connected in:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_430:
    def __init__(self, *args, **kwargs):
        choice_a = 'series*'
        choice_b = 'parallel'
        choice_c = 'series-parallel'
        choice_d = 'resonance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To increase the voltage output, several cells are connected in:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_431:
    def __init__(self, *args, **kwargs):
        choice_a = 'short-circuited*'
        choice_b = 'recharged'
        choice_c = 'left disconnected'
        choice_d = 'left overnight at room temperature'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A lithium-ion battery should never be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_432:
    def __init__(self, *args, **kwargs):
        choice_a = 'The power supply*'
        choice_b = 'The speaker'
        choice_c = 'The microphone'
        choice_d = 'The SWR meter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If your mobile transceiver works in your car but not in your home, what should you check first?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_433:
    def __init__(self, *args, **kwargs):
        choice_a = 'A power supply*'
        choice_b = 'A low pass filter'
        choice_c = 'An RS-232 interface'
        choice_d = 'A catalytic converter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What device converts household current to 12 volts DC?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_434:
    def __init__(self, *args, **kwargs):
        choice_a = 'A transceiver*'
        choice_b = 'An antenna switch'
        choice_c = 'A receiver'
        choice_d = 'An SWR meter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these usually needs a high current capacity power supply?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_435:
    def __init__(self, *args, **kwargs):
        choice_a = 'A bad filter capacitor in the transmitter\'s power supply*'
        choice_b = 'Using an antenna which is the wrong length*'
        choice_c = 'Energy from another transmitter'
        choice_d = 'Bad design of the transmitter\'s RF power output circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What may cause a buzzing or hum in the signal of an AC-powered transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_436:
    def __init__(self, *args, **kwargs):
        choice_a = '60 watts*'
        choice_b = '17 watts'
        choice_c = '2.4 watts'
        choice_d = '6 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A power supply is to supply DC at 12 volts at 5 amperes. The power transformer should be rated higher than:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_437:
    def __init__(self, *args, **kwargs):
        choice_a = 'allows electrons to flow in only one direction from cathode to anode*'
        choice_b = 'has a high resistance to AC but not to DC'
        choice_c = 'has a high resistance to DC but not to AC'
        choice_d = 'allows electrons to flow in only one direction from anode to cathode'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The diode is an important part of a simple power supply. It converts AC to DC, since it:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_438:
    def __init__(self, *args, **kwargs):
        choice_a = 'diode*'
        choice_b = 'transformer'
        choice_c = 'capacitor'
        choice_d = 'resistor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To convert AC to pulsating DC, you could use a:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_439:
    def __init__(self, *args, **kwargs):
        choice_a = '120 and 240 volts*'
        choice_b = '110 and 220 volts'
        choice_c = '100 and 200 volts'
        choice_d = '130 and 260 volts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Power-line voltages have been made standard over the years and the voltages generally supplied to homes are approximately:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_440:
    def __init__(self, *args, **kwargs):
        choice_a = 'Number 10, 0.07 V per metre (0.02 V per foot)*'
        choice_b = 'Number 14, 0.19 V per metre (0.06 V per foot)'
        choice_c = 'Number 12, 0.11 V per metre (0.03 V per foot)'
        choice_d = 'Number 8, 0.05 V per metre (0.01 V per foot)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Your mobile HF transceiver draws 22 amperes on transmit. The manufacturer suggests limiting voltage drop to 0.5 volt and the vehicle battery is 3 metres (10 feet) away. Given the losses below at that current, which minimum wire gauge must you use?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_441:
    def __init__(self, *args, **kwargs):
        choice_a = 'To prevent an overcurrent situation from starting a fire*'
        choice_b = 'To prevent interference to the vehicle\'s electronic systems'
        choice_c = 'To reduce the voltage drop in the radio\'s DC supply'
        choice_d = 'To protect the radio from transient voltages'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why are fuses needed as close as possible to the vehicle battery when wiring a transceiver directly to the battery?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_442:
    def __init__(self, *args, **kwargs):
        choice_a = 'The power supply*'
        choice_b = 'The variable-frequency oscillator'
        choice_c = 'The driver circuit'
        choice_d = 'The power amplifier circuit'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You have a very loud low-frequency hum appearing on your transmission. In what part of the transmitter would you first look for the trouble?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_443:
    def __init__(self, *args, **kwargs):
        choice_a = 'Use a key-operated on/off switch in the main power line*'
        choice_b = 'Use a carrier-operated relay in the main power line'
        choice_c = 'Put a "Danger - High Voltage" sign in the station'
        choice_d = 'Put fuses in the main power line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How could you best keep unauthorized persons from using your amateur station at home?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_444:
    def __init__(self, *args, **kwargs):
        choice_a = 'Disconnect the microphone when you are not using it*'
        choice_b = 'Tune the radio to an unused frequency when you are done using it'
        choice_c = 'Turn the radio off when you are not using it'
        choice_d = 'Put a "Do not touch" sign on the radio'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How could you best keep unauthorized persons from using a mobile amateur station in your car?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_445:
    def __init__(self, *args, **kwargs):
        choice_a = 'To keep unauthorized persons from using your station*'
        choice_b = 'For safety, in case the main fuses fail'
        choice_c = 'To keep the power company from turning off your electricity during an emergency'
        choice_d = 'For safety, to turn off the station in the event of an emergency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why would you use a key-operated on/off switch in the main power line of your station?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_446:
    def __init__(self, *args, **kwargs):
        choice_a = 'To keep anyone opening the cabinet from getting shocked by dangerous high voltages*'
        choice_b = 'To keep dangerous RF radiation from leaking out through an open cabinet'
        choice_c = 'To keep dangerous RF radiation from coming in through an open cabinet'
        choice_d = 'To turn the power supply off when it is not being used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why would there be a switch in a high-voltage power supply to turn off the power if its cabinet is opened?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_447:
    def __init__(self, *args, **kwargs):
        choice_a = 'As little as 20 milliamperes*'
        choice_b = 'Approximately 10 amperes'
        choice_c = 'More than 20 amperes'
        choice_d = 'Current flow through the human body is never fatal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How little electrical current flowing through the human body can be fatal?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_448:
    def __init__(self, *args, **kwargs):
        choice_a = 'The heart*'
        choice_b = 'The brain'
        choice_c = 'The liver'
        choice_d = 'The lungs'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which body organ can be fatally affected by a very small amount of electrical current?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_449:
    def __init__(self, *args, **kwargs):
        choice_a = '30 volts*'
        choice_b = '100 volts'
        choice_c = '1000 volts'
        choice_d = '2000 volts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the minimum voltage which is usually dangerous to humans?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_450:
    def __init__(self, *args, **kwargs):
        choice_a = 'Turn off the power, call for emergency help and provide first-aid if needed*'
        choice_b = 'Wait for a few minutes to see if the person can get away from the high voltage on their own, then try to help'
        choice_c = 'Immediately drag the person away from the high voltage'
        choice_d = 'Run from the area so you won\'t be burned too'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should you do if you discover someone who is being burned by high voltage?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class f_2_451:
    def __init__(self, *args, **kwargs):
        choice_a = 'Turn off the high voltage switch before removing the person from contact with the source*'
        choice_b = 'Wrap the person in a blanket and pull him to a safe area'
        choice_c = 'Call an electrician'
        choice_d = 'Remove the person by pulling an arm or a leg'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the safest method to remove an unconscious person from contact with a high voltage source?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_452:
    def __init__(self, *args, **kwargs):
        choice_a = 'turn off the power and remove power plug*'
        choice_b = 'short out leads of filter capacitor'
        choice_c = 'check action of capacitor bleeder resistance'
        choice_d = 'remove and check fuse from power supply'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Before checking a fault in a mains operated power supply unit, it would be safest to first:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_453:
    def __init__(self, *args, **kwargs):
        choice_a = 'electric shock*'
        choice_b = 'damaging the transmitter'
        choice_c = 'overmodulation'
        choice_d = 'blowing the fuse'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Fault finding in a power supply of an amateur transmitter while the supply is operating is not a recommended technique because of the risk of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_454:
    def __init__(self, *args, **kwargs):
        choice_a = 'All station equipment*'
        choice_b = 'The antenna transmission line'
        choice_c = 'The AC power line'
        choice_d = 'The power supply primary'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For best protection from electrical shock, what should be grounded in an amateur station?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_455:
    def __init__(self, *args, **kwargs):
        choice_a = 'a metallic cold water pipe*'
        choice_b = 'a plastic cold water pipe'
        choice_c = 'a window screen'
        choice_d = 'a metallic natural gas pipe'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a separate ground system is not possible for your amateur station, an alternative indoor grounding point could be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_456:
    def __init__(self, *args, **kwargs):
        choice_a = 'a good ground connection*'
        choice_b = 'a dummy load'
        choice_c = 'insulated shock mounts'
        choice_d = 'the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To protect you against electrical shock, the chassis of each piece of your station equipment should be connected to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_457:
    def __init__(self, *args, **kwargs):
        choice_a = 'Copper-clad steel*'
        choice_b = 'Hard plastic'
        choice_c = 'Iron or steel'
        choice_d = 'Fiberglass'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these materials is best for a ground rod driven into the earth?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_458:
    def __init__(self, *args, **kwargs):
        choice_a = 'The station ground system must conform to applicable electrical code requirements*'
        choice_b = '1.2 metre (4 ft)'
        choice_c = '2.5 metres (8 ft)'
        choice_d = '3 metres (10 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you ground your station equipment to a ground rod driven into the earth, what is the shortest length the rod should be?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_459:
    def __init__(self, *args, **kwargs):
        choice_a = 'To the chassis*'
        choice_b = 'To the white wire'
        choice_c = 'To the "hot" side of the power switch'
        choice_d = 'To the fuse'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Where should the green wire in a three-wire AC line cord be connected in a power supply?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_460:
    def __init__(self, *args, **kwargs):
        choice_a = 'Because the ground wire has significant reactance and acts more like an antenna than an RF ground connection*'
        choice_b = 'Because of a bad antenna connection, allowing the RF energy to take an easier path out of the transceiver through you'
        choice_c = 'Because the transceiver\'s heat-sensing circuit is not working to start the cooling fan'
        choice_d = 'Because the ground rod is not making good contact with moist earth'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If your third-floor amateur station has a ground wire running 10 metres (33 feet) down to a ground rod, why might you get an RF burn if you touch the front panel of your HF transceiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_461:
    def __init__(self, *args, **kwargs):
        choice_a = 'Keep the station\'s ground wire as short as possible*'
        choice_b = 'Make a couple of loops in the ground wire where it connects to your station'
        choice_c = 'Drive the ground rod at least 4m (14 feet) into the ground'
        choice_d = 'Use a beryllium ground wire for best conductivity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one good way to avoid stray RF energy in your amateur station?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_462:
    def __init__(self, *args, **kwargs):
        choice_a = 'RF hot spots can occur in a station located above the ground floor if the equipment is grounded by a long ground wire*'
        choice_b = 'A ground loop is an effective way to ground station equipment'
        choice_c = 'If the chassis of all station equipment is connected with a good conductor, there is no need to tie them to an earth ground'
        choice_d = 'The chassis of each piece of station equipment should be tied together with high-impedance conductors'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which statement about station grounding is true?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_463:
    def __init__(self, *args, **kwargs):
        choice_a = 'does not develop a high voltage with respect to the ground*'
        choice_b = 'does not become conductive to prevent electric shock'
        choice_c = 'becomes conductive to prevent electric shock'
        choice_d = 'develops a high voltage compared to the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On mains operated power supplies, the ground wire should be connected to the metal chassis of the power supply. This ensures, in case there is a fault in the power supply, that the chassis:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_464:
    def __init__(self, *args, **kwargs):
        choice_a = 'prevent the chassis from becoming live*'
        choice_b = 'prevent the plug from being reversed in the wall outlet'
        choice_c = 'prevent internal short circuits'
        choice_d = 'make it inconvenient to use'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The purpose of using a three-wire power cord and plug on amateur radio equipment is to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_465:
    def __init__(self, *args, **kwargs):
        choice_a = 'To help protect the station equipment and building from lightning damage*'
        choice_b = 'To lock the antenna system in one position'
        choice_c = 'To avoid radio frequency interference'
        choice_d = 'To make sure everything will stay in place'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you ground all antenna and rotator cables when your amateur station is not in use?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_466:
    def __init__(self, *args, **kwargs):
        choice_a = 'Outside, as close to earth grounding as possible*'
        choice_b = 'Close to the antenna'
        choice_c = 'Behind the transceiver'
        choice_d = 'Anywhere on the line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You want to install a lightning arrestor on your antenna transmission line, where should it be inserted?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_467:
    def __init__(self, *args, **kwargs):
        choice_a = 'Disconnect all equipment from the power lines and antenna cables*'
        choice_b = 'Use heavy insulation on the wiring'
        choice_c = 'Never turn off the equipment'
        choice_d = 'Disconnect the ground system from all radios'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can amateur station equipment best be protected from lightning damage?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_468:
    def __init__(self, *args, **kwargs):
        choice_a = 'Approved equipment in accordance with applicable standards concerning fall protection*'
        choice_b = 'A reflective vest of approved colour'
        choice_c = 'A flashing red, yellow or white light'
        choice_d = 'A grounding chain'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What equipment should be worn for working on an antenna tower?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_469:
    def __init__(self, *args, **kwargs):
        choice_a = 'To prevent you from accidentally falling*'
        choice_b = 'To safely bring any tools you might use up and down the tower'
        choice_c = 'To keep the tower from becoming unbalanced while you are working'
        choice_d = 'To safely hold your tools so they don\'t fall and injure someone on the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you wear approved fall arrest equipment if you are working on an antenna tower?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_470:
    def __init__(self, *args, **kwargs):
        choice_a = 'High enough so that no one can touch any part of it from the ground*'
        choice_b = 'Above high-voltage electrical lines'
        choice_c = 'Just high enough so you can easily reach it for adjustments or repairs'
        choice_d = 'As close to the ground as possible'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For safety, how high should you place a horizontal wire antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_471:
    def __init__(self, *args, **kwargs):
        choice_a = 'To protect your head from something dropped from the tower*'
        choice_b = 'So you won\'t be hurt if the tower should accidentally fall'
        choice_c = 'To keep RF energy away from your head during antenna testing'
        choice_d = 'So someone passing by will know that work is being done on the tower and will stay away'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you wear a hard hat if you are on the ground helping someone work on an antenna tower?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_472:
    def __init__(self, *args, **kwargs):
        choice_a = 'Touching the antenna might cause RF burns*'
        choice_b = 'Touching the antenna might reflect the signal back to the transmitter and cause damage'
        choice_c = 'Touching the antenna might radiate harmonics'
        choice_d = 'Touching the antenna might cause television interference'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should your outside antennas be high enough so that no one can touch them while you are transmitting?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_473:
    def __init__(self, *args, **kwargs):
        choice_a = 'Because high-voltage radio energy might burn the person*'
        choice_b = 'Because contact might break the transmission line'
        choice_c = 'Because contact might cause spurious emissions'
        choice_d = 'Because contact might cause a short circuit and damage the transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you make sure that no one can touch an open wire transmission line while you are transmitting with it?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_474:
    def __init__(self, *args, **kwargs):
        choice_a = 'Be sure to turn off the transmitter and disconnect the transmission line*'
        choice_b = 'Be sure you and the antenna structure are grounded'
        choice_c = 'Inform your neighbours so they are aware of your intentions'
        choice_d = 'Turn off the main power switch in your house'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What safety precautions should you take before beginning repairs on an antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_475:
    def __init__(self, *args, **kwargs):
        choice_a = 'It should be installed so no one can come in contact with it*'
        choice_b = 'It should be painted so people or animals do not accidentally run into it'
        choice_c = 'It should not be installed in a wet area'
        choice_d = 'It should not be installed higher than you can reach'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What precaution should you take when installing a ground-mounted antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_476:
    def __init__(self, *args, **kwargs):
        choice_a = 'Keep antenna away from your eyes when RF is applied*'
        choice_b = 'Make sure that an RF leakage filter is installed at the antenna feed point'
        choice_c = 'Make sure the standing wave ratio is low before you conduct a test'
        choice_d = 'Never use a horizontally polarized antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should you do for safety when operating at UHF and microwave frequencies?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_477:
    def __init__(self, *args, **kwargs):
        choice_a = 'Make sure the antenna will be in a place where no one can get near it when you are transmitting*'
        choice_b = 'Make sure the antenna is near the ground to keep its RF energy pointing in the correct direction'
        choice_c = 'Make sure you connect an RF leakage filter at the antenna feed point'
        choice_d = 'Make sure that RF field screens are in place'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should you do for safety if you put up a UHF transmitting antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_478:
    def __init__(self, *args, **kwargs):
        choice_a = 'Make sure the amplifier cannot accidentally be turned on*'
        choice_b = 'Make sure that RF leakage filters are connected'
        choice_c = 'Make sure the antenna transmission line is properly grounded'
        choice_d = 'Make sure all RF screens are in place at the antenna transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should you do for safety, before removing the shielding on a UHF power amplifier?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_479:
    def __init__(self, *args, **kwargs):
        choice_a = 'To reduce your exposure to the radio-frequency energy*'
        choice_b = 'To use your body to reflect the signal in one direction'
        choice_c = 'To keep static charges from building up'
        choice_d = 'To help the antenna radiate energy equally in all directions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you make sure the antenna of a hand-held transceiver is not close to your head when transmitting?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_480:
    def __init__(self, *args, **kwargs):
        choice_a = 'Away from your head and away from others*'
        choice_b = 'Pointed towards the station you are contacting'
        choice_c = 'Pointed away from the station you are contacting'
        choice_d = 'Pointed down to bounce the signal off the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How should you position the antenna of a hand-held transceiver while you are transmitting?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_481:
    def __init__(self, *args, **kwargs):
        choice_a = 'It heats the tissue*'
        choice_b = 'It lowers blood pressure'
        choice_c = 'It paralyzes the tissue'
        choice_d = 'It causes hair to fall out'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can exposure to a large amount of RF energy affect body tissue?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_482:
    def __init__(self, *args, **kwargs):
        choice_a = 'Eyes*'
        choice_b = 'Heart'
        choice_c = 'Liver'
        choice_d = 'Hands'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which body organ is the most likely to be damaged from the heating effects of RF radiation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_483:
    def __init__(self, *args, **kwargs):
        choice_a = 'It heats the tissue*'
        choice_b = 'It causes ionizing radiation poisoning'
        choice_c = 'It causes blood flow to stop'
        choice_d = 'It has no effect on the body'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Depending on the wavelength of the signal, the energy density of the RF field, and other factors, in what way can RF energy affect body tissue?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_484:
    def __init__(self, *args, **kwargs):
        choice_a = 'Locate the antennas as far away as possible from living spaces that will be occupied while you are operating*'
        choice_b = 'Position the antennas parallel to electrical power wires to take advantage of parasitic effects'
        choice_c = 'Position the antennas along the edge of a wall where it meets the floor or ceiling to reduce parasitic radiation'
        choice_d = 'Locate the antennas close to your operating position to minimize transmission line length'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you operate your amateur station with indoor antennas, what precautions should you take when you install them?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_485:
    def __init__(self, *args, **kwargs):
        choice_a = 'So they will not direct RF energy toward people in nearby structures*'
        choice_b = 'So they will be dried by the wind after a heavy rain storm'
        choice_c = 'So they will not damage nearby structures with RF energy'
        choice_d = 'So they will receive more sky waves and fewer ground waves'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should directional high-gain antennas be mounted higher than nearby structures?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_486:
    def __init__(self, *args, **kwargs):
        choice_a = 'As high as possible to prevent people from coming in contact with the antenna*'
        choice_b = 'Near or over moist ground so RF energy will be radiated away from the ground'
        choice_c = 'As close to the transmitter as possible so RF energy will be concentrated near the transmitter'
        choice_d = 'Close to the ground so simple adjustments can be easily made without climbing a ladder'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For best RF safety, where should the ends and center of a dipole antenna be located?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_630:
    def __init__(self, *args, **kwargs):
        choice_a = 'S9*'
        choice_b = 'S9 plus 3 dB'
        choice_c = 'S9 minus 10 dB'
        choice_d = 'S9 plus 5 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a signal-strength report is "10 dB over S9", what should the report be if the transmitter power is reduced from 1500 watts to 150 watts?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_631:
    def __init__(self, *args, **kwargs):
        choice_a = 'S9 plus 10 dB*'
        choice_b = 'S9 plus 5 dB'
        choice_c = 'S9 plus 3 dB'
        choice_d = 'S9'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a signal-strength report is "20 dB over S9", what should the report be if the transmitter power is reduced from 1500 watts to 150 watts?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_635:
    def __init__(self, *args, **kwargs):
        choice_a = '16 watts*'
        choice_b = '11 watts'
        choice_c = '20 watts'
        choice_d = '18 watts'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You add a 9 dB gain amplifier to your 2 watt handheld. What is the power output of the combination?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_636:
    def __init__(self, *args, **kwargs):
        choice_a = '6 dB*'
        choice_b = '3 dB'
        choice_c = '8 dB'
        choice_d = '9 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The power of a transmitter is increased from 2 watts to 8 watts. This is a power gain of __________ dB."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_637:
    def __init__(self, *args, **kwargs):
        choice_a = '100 mW*'
        choice_b = '1 W'
        choice_c = '10 W'
        choice_d = '33.3 W'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A local amateur reports your 100W 2M simplex VHF transmission as 30 dB over S9. To reduce your signal to S9, you would reduce your power to ______ watts."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_692:
    def __init__(self, *args, **kwargs):
        choice_a = 'A transmission line*'
        choice_b = 'The power cord'
        choice_c = 'A ground wire'
        choice_d = 'A dummy load'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What connects your transceiver to your antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_693:
    def __init__(self, *args, **kwargs):
        choice_a = 'physical dimensions and relative positions of the conductors*'
        choice_b = 'length of the line'
        choice_c = 'frequency at which the line is operated'
        choice_d = 'load placed on the line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The characteristic impedance of a transmission line is determined by the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_694:
    def __init__(self, *args, **kwargs):
        choice_a = '52 ohms*'
        choice_b = '26 ohms'
        choice_c = '39 ohms'
        choice_d = '13 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The characteristic impedance of a 20 metre piece of transmission line is 52 ohms. If 10 metres were cut off, the impedance would be:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_695:
    def __init__(self, *args, **kwargs):
        choice_a = 'can be the same for different diameter line*'
        choice_b = 'changes significantly with the frequency of the energy it carries'
        choice_c = 'is correct for only one size of line'
        choice_d = 'is greater for larger diameter line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The characteristic impedance of a coaxial line:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_696:
    def __init__(self, *args, **kwargs):
        choice_a = 'Coaxial cable*'
        choice_b = '300 ohm twin-lead'
        choice_c = '600 ohm open-wire line'
        choice_d = '75 ohm twin-lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What commonly available antenna transmission line can be buried directly in the ground for some distance without adverse effects?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_697:
    def __init__(self, *args, **kwargs):
        choice_a = 'equal to the pure resistance which, if connected to the end of the line, will absorb all the power arriving along it*'
        choice_b = 'the impedance of a section of the line one wavelength long'
        choice_c = 'the dynamic impedance of the line at the operating frequency'
        choice_d = 'the ratio of the power supplied to the line to the power delivered to the load'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The characteristic impedance of a transmission line is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_698:
    def __init__(self, *args, **kwargs):
        choice_a = 'propagation delay*'
        choice_b = 'capacitive reactance'
        choice_c = 'inductive reactance'
        choice_d = 'resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Capacitive reactance:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_699:
    def __init__(self, *args, **kwargs):
        choice_a = 'velocity of energy on the line*'
        choice_b = 'radius of the conductors'
        choice_c = 'centre to centre distance between conductors'
        choice_d = 'dielectric'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The characteristic impedance of a parallel wire transmission line does not depend on the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_700:
    def __init__(self, *args, **kwargs):
        choice_a = 'Some value of impedance influenced by line length*'
        choice_b = 'An infinite impedance'
        choice_c = 'A negative impedance'
        choice_d = 'An impedance nearly equal to the characteristic impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the impedance terminating a transmission line differs significantly from the characteristic impedance of the line, what will be observed at the input of the line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_701:
    def __init__(self, *args, **kwargs):
        choice_a = 'The distance between the centres of the conductors and the radius of the conductors*'
        choice_b = 'The distance between the centres of the conductors and the length of the line'
        choice_c = 'The radius of the conductors and the frequency of the signal'
        choice_d = 'The frequency of the signal and the length of the line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What factors determine the characteristic impedance of a parallel-conductor antenna transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_702:
    def __init__(self, *args, **kwargs):
        choice_a = 'The ratio of the diameter of the inner conductor to the diameter of the outer shield*'
        choice_b = 'The diameter of the shield and the length of the line'
        choice_c = 'The diameter of the shield and the frequency of the signal'
        choice_d = 'The frequency of the signal and the length of the line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What factors determine the characteristic impedance of a coaxial antenna transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_703:
    def __init__(self, *args, **kwargs):
        choice_a = 'A center wire inside an insulating material which is covered by a metal sleeve or shield*'
        choice_b = 'Two wires side-by-side in a plastic ribbon'
        choice_c = 'Two wires side-by-side held apart by insulating rods'
        choice_d = 'Two wires twisted around each other in a spiral'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a coaxial cable?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_704:
    def __init__(self, *args, **kwargs):
        choice_a = 'Two wires side-by-side held apart by insulating material*'
        choice_b = 'Two wires twisted around each other in a spiral'
        choice_c = 'A center wire inside an insulating material which is covered by a metal sleeve or shield'
        choice_d = 'A metal pipe which is as wide or slightly wider than a wavelength of the signal it carries'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is parallel-conductor transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_705:
    def __init__(self, *args, **kwargs):
        choice_a = 'Open wire line*'
        choice_b = 'Coaxial cable'
        choice_c = 'Twin lead in a plastic ribbon'
        choice_d = 'Twisted pair'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of antenna transmission line is made of two conductors held apart by insulated rods?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_706:
    def __init__(self, *args, **kwargs):
        choice_a = 'Balanced to unbalanced*'
        choice_b = 'Balanced unloader'
        choice_c = 'Balanced unmodulator'
        choice_d = 'Balanced antenna network'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does the term "balun" mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_707:
    def __init__(self, *args, **kwargs):
        choice_a = 'Between the coaxial cable and the antenna*'
        choice_b = 'Between the transmitter and the coaxial cable'
        choice_c = 'Between the antenna and the ground'
        choice_d = 'Between the coaxial cable and the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Where would you install a balun to feed a dipole antenna with 50-ohm coaxial cable?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_708:
    def __init__(self, *args, **kwargs):
        choice_a = 'Transmission line with one conductor connected to ground*'
        choice_b = 'Transmission line with neither conductor connected to ground'
        choice_c = 'Transmission line with both conductors connected to ground'
        choice_d = 'Transmission line with both conductors connected to each other'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is an unbalanced line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_709:
    def __init__(self, *args, **kwargs):
        choice_a = 'A balun*'
        choice_b = 'A triaxial transformer'
        choice_c = 'A wave trap'
        choice_d = 'A loading coil'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What device can be installed to feed a balanced antenna with an unbalanced transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_710:
    def __init__(self, *args, **kwargs):
        choice_a = 'braided shield conductor and insulation around a central conductor*'
        choice_b = 'four or more conductors running parallel'
        choice_c = 'only one conductor'
        choice_d = 'two parallel conductors separated by spacers'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A flexible coaxial line contains:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_711:
    def __init__(self, *args, **kwargs):
        choice_a = 'is made of two parallel wires*'
        choice_b = 'has one conductor inside the other'
        choice_c = 'carries RF current on one wire only'
        choice_d = 'is made of one conductor only'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A balanced transmission line:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_712:
    def __init__(self, *args, **kwargs):
        choice_a = 'by using a 4 to 1 impedance transformer*'
        choice_b = 'with an extra 250 ohm resistor'
        choice_c = 'by using a 4 to 1 trigatron'
        choice_d = 'by inserting a diode in one leg of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" A 75 ohm transmission line could be matched to the 300 ohm feed point of an antenna:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_713:
    def __init__(self, *args, **kwargs):
        choice_a = '600 ohm open wire line*'
        choice_b = 'Coaxial cable'
        choice_c = '75 ohm twin-lead'
        choice_d = '300 ohm twin-lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of antenna transmission line can be constructed using two conductors which are maintained a uniform distance apart using insulated spreaders?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_714:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is weatherproof, and its impedance matches most amateur antennas*'
        choice_b = 'It is weatherproof, and its impedance is higher than that of most amateur antennas'
        choice_c = 'It can be used near metal objects, and its impedance is higher than that of most amateur antennas'
        choice_d = 'You can make it at home, and its impedance matches most amateur antennas'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why does coaxial cable make a good antenna transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_715:
    def __init__(self, *args, **kwargs):
        choice_a = 'Coaxial cable*'
        choice_b = 'Ladder-line'
        choice_c = 'Twisted pair'
        choice_d = 'Twin lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" What is the best antenna transmission line to use, if it must be put near grounded metal objects?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_716:
    def __init__(self, *args, **kwargs):
        choice_a = 'It does not work well when tied down to metal objects, and you should use a balun and may have to use an impedance-matching device with your transceiver*'
        choice_b = 'You must use an impedance-matching device with your transceiver, and it does not work very well with a high SWR'
        choice_c = 'It does not work well when tied down to metal objects, and it cannot operate under high power'
        choice_d = 'It is difficult to make at home, and it does not work very well with a high SWR'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What are some reasons not to use parallel-conductor transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_717:
    def __init__(self, *args, **kwargs):
        choice_a = 'A PL-259 connector*'
        choice_b = 'An F-type cable connector'
        choice_c = 'A banana plug connector'
        choice_d = 'A binding post connector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What common connector type usually joins RG-213 coaxial cable to an HF transceiver?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_718:
    def __init__(self, *args, **kwargs):
        choice_a = 'An SMA connector*'
        choice_b = 'A PL-259 connector'
        choice_c = 'An F-type cable connector'
        choice_d = 'A binding post connector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What common connector usually joins a hand-held transceiver to its antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_719:
    def __init__(self, *args, **kwargs):
        choice_a = 'A type-N connector*'
        choice_b = 'An F-type cable connector'
        choice_c = 'A BNC connector'
        choice_d = 'A PL-259 connector'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of these common connectors has the lowest loss at UHF?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_720:
    def __init__(self, *args, **kwargs):
        choice_a = 'RG-213*'
        choice_b = 'RG-174'
        choice_c = 'RG-59'
        choice_d = 'RG-58'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you install a 6 metre Yagi on a tower 60 metres (200 ft) from your transmitter, which of the following transmission lines provides the least loss?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_721:
    def __init__(self, *args, **kwargs):
        choice_a = 'To help keep their contact resistance at a minimum*'
        choice_b = 'To keep them looking nice'
        choice_c = 'To keep them from getting stuck in place'
        choice_d = 'To increase their capacitance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you regularly clean and tighten all antenna connectors?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_722:
    def __init__(self, *args, **kwargs):
        choice_a = 'Coaxial cable*'
        choice_b = '75 ohm twin-lead'
        choice_c = '600 ohm open wire line'
        choice_d = '300 ohm twin-lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What commonly available antenna transmission line can be buried directly in the ground for some distance without adverse effects?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_723:
    def __init__(self, *args, **kwargs):
        choice_a = 'Coaxial cable*'
        choice_b = '300 ohm twin-lead'
        choice_c = '600 ohm open wire line'
        choice_d = '75 ohm twin-lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When antenna transmission lines must be placed near grounded metal objects, which of the following transmission lines should be used?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_724:
    def __init__(self, *args, **kwargs):
        choice_a = '300 ohms*'
        choice_b = '600 ohms'
        choice_c = '50 ohms'
        choice_d = '70 ohms'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" TV twin-lead transmission line can be used for a transmission line in an amateur station. The impedance of this line is approximately:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_725:
    def __init__(self, *args, **kwargs):
        choice_a = 'To keep RF loss low*'
        choice_b = 'To keep television interference high'
        choice_c = 'To keep the power going to your antenna system from getting too high'
        choice_d = 'To keep the standing wave ratio of your antenna system high'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why should you use only good quality coaxial cable and connectors for a UHF antenna system?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_726:
    def __init__(self, *args, **kwargs):
        choice_a = 'It will operate with a high SWR, and has less loss than coaxial cable*'
        choice_b = 'It has low impedance, and will operate with a high SWR'
        choice_c = 'It will operate with a high SWR, and it works well when tied down to metal objects'
        choice_d = 'It has a low impedance, and has less loss than coaxial cable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What are some reasons to use parallel-conductor transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_727:
    def __init__(self, *args, **kwargs):
        choice_a = 'Shorten the excess cable*'
        choice_b = 'Shorten the excess cable so the transmission line is an odd number of wavelengths long'
        choice_c = 'Roll the excess cable into a coil which is as small as possible'
        choice_d = 'Shorten the excess cable so the transmission line is an even number of wavelengths long'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" If your transmitter and antenna are 15 metres (50 ft) apart, but are connected by 60 metres (200 ft) of RG-58 coaxial cable, what should be done to reduce transmission line loss?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_728:
    def __init__(self, *args, **kwargs):
        choice_a = 'Signal loss increases as length increases*'
        choice_b = 'Signal loss decreases as length increases'
        choice_c = 'Signal loss is the least when the length is the same as the signal\'s wavelength'
        choice_d = 'Signal loss is the same for any length of transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the length of a transmission line is changed, what happens to signal loss?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_729:
    def __init__(self, *args, **kwargs):
        choice_a = 'Signal loss increases with increasing frequency*'
        choice_b = 'Signal loss increases with decreasing frequency'
        choice_c = 'Signal loss is the least when the signal\'s wavelength is the same as the transmission line\'s length'
        choice_d = 'Signal loss is the same for any frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""As the frequency of a signal is changed, what happens to signal loss in a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_730:
    def __init__(self, *args, **kwargs):
        choice_a = 'less RF power being radiated*'
        choice_b = 'an SWR reading of 1:1'
        choice_c = 'reflections occurring in the line'
        choice_d = 'the wire radiating RF energy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Losses occurring on a transmission line between transmitter and antenna results in:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_731:
    def __init__(self, *args, **kwargs):
        choice_a = 'open wire line*'
        choice_b = '75 ohm twin-lead'
        choice_c = 'coaxial cable'
        choice_d = '300 ohm twin-lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The lowest loss transmission line on HF is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_732:
    def __init__(self, *args, **kwargs):
        choice_a = 'dB per unit length*'
        choice_b = 'Ohms per MHz'
        choice_c = 'dB per MHz'
        choice_d = 'Ohms per metre'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In what values are RF transmission line losses expressed?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_733:
    def __init__(self, *args, **kwargs):
        choice_a = 'It would be increased by 100%*'
        choice_b = 'It would be reduced by 10%'
        choice_c = 'It would be increased by 10%'
        choice_d = 'It would be reduced to 50%'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the length of coaxial transmission line is increased from 20 metres (66 ft) to 40 metres (132 ft), how would this affect the line loss?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_734:
    def __init__(self, *args, **kwargs):
        choice_a = 'It would increase*'
        choice_b = 'It is independent of frequency'
        choice_c = 'It depends on the line length'
        choice_d = 'It would decrease'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the frequency is increased, how would this affect the loss on a transmission line?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_735:
    def __init__(self, *args, **kwargs):
        choice_a = 'The best impedance match has been attained*'
        choice_b = 'An antenna for another frequency band is probably connected'
        choice_c = 'No power is going to the antenna'
        choice_d = 'The SWR meter is broken'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does an SWR reading of 1:1 mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_736:
    def __init__(self, *args, **kwargs):
        choice_a = 'A fairly good impedance match*'
        choice_b = 'An impedance match which is too low'
        choice_c = 'A serious impedance mismatch, something may be wrong with the antenna system'
        choice_d = 'An antenna gain of 1.5'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does an SWR reading of less than 1.5:1 mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_737:
    def __init__(self, *args, **kwargs):
        choice_a = 'A jumpy reading*'
        choice_b = 'A negative reading'
        choice_c = 'No reading at all'
        choice_d = 'A very low reading'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of SWR reading may mean poor electrical contact between parts of an antenna system?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_738:
    def __init__(self, *args, **kwargs):
        choice_a = 'The antenna is the wrong length for the operating frequency, or the transmission line may be open or short circuited*'
        choice_b = 'The transmitter is putting out more power than normal, showing that it is about to go bad'
        choice_c = 'There is a large amount of solar radiation, which means very poor radio conditions'
        choice_d = 'The signals coming from the antenna are unusually strong, which means very good radio condition'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does a very high SWR reading mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_739:
    def __init__(self, *args, **kwargs):
        choice_a = 'The ratio of maximum to minimum voltages on a transmission line*'
        choice_b = 'The ratio of maximum to minimum inductances on a transmission line'
        choice_c = 'The ratio of maximum to minimum resistances on a transmission line'
        choice_d = 'The ratio of maximum to minimum impedances on a transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does standing-wave ratio mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_740:
    def __init__(self, *args, **kwargs):
        choice_a = 'The SWR may be too high, or the transmission line loss may be high*'
        choice_b = 'You should transmit using less power'
        choice_c = 'The conductors in the transmission line are not insulated very well'
        choice_d = 'The transmission line is too long'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If your antenna transmission line gets hot when you are transmitting, what might this mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_741:
    def __init__(self, *args, **kwargs):
        choice_a = 'standing waves are produced in the transmission line*'
        choice_b = 'heat is produced at the junction'
        choice_c = 'the SWR reading falls to 1:1'
        choice_d = 'the antenna will not radiate any signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the characteristic impedance of the transmission line does not match the antenna input impedance then:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_742:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduced transfer of RF energy to the antenna*'
        choice_b = 'perfect impedance match between transmitter and transmission line'
        choice_c = 'maximum transfer of energy to the antenna from the transmitter'
        choice_d = 'lack of radiation from the transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The result of the presence of standing waves on a transmission line is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_743:
    def __init__(self, *args, **kwargs):
        choice_a = 'comparing forward and reflected voltage*'
        choice_b = 'measuring radiated RF energy'
        choice_c = 'measuring the conductor temperature'
        choice_d = 'inserting a diode in the transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An SWR meter measures the degree of match between transmission line and antenna by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_744:
    def __init__(self, *args, **kwargs):
        choice_a = '4:1*'
        choice_b = '6:1'
        choice_c = '3:1'
        choice_d = '5:1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A resonant antenna having a feed point impedance of 200 ohms is connected to a transmission line which has an impedance of 50 ohms. What will the standing wave ratio of this system be?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_745:
    def __init__(self, *args, **kwargs):
        choice_a = '600 ohm open wire line*'
        choice_b = '75 ohm twin-lead'
        choice_c = 'coaxial line'
        choice_d = '300 ohm twin-lead'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The type of transmission line best suited to operating at a high standing wave ratio is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class f_2_746:
    def __init__(self, *args, **kwargs):
        choice_a = 'An antenna tuner*'
        choice_b = 'An SWR meter'
        choice_c = 'A low pass filter'
        choice_d = 'A high pass filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What device might allow use of an antenna on a band it was not designed for?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_747:
    def __init__(self, *args, **kwargs):
        choice_a = 'It matches a transceiver to a mismatched antenna system*'
        choice_b = 'It helps a receiver automatically tune in stations that are far away'
        choice_c = 'It switches an antenna system to a transmitter when sending, and to a receiver when listening'
        choice_d = 'It switches a transceiver between different kinds of antennas connected to one transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does an antenna tuner do?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_748:
    def __init__(self, *args, **kwargs):
        choice_a = 'An impedance-matching device*'
        choice_b = 'An SWR meter'
        choice_c = 'A low pass filter'
        choice_d = 'A terminating resistor'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What would you use to connect a coaxial cable of 50 ohms impedance to an antenna of 17 ohms impedance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_749:
    def __init__(self, *args, **kwargs):
        choice_a = 'When the impedance of the load is equal to the impedance of the source*'
        choice_b = 'When air wound transformers are used instead of iron-core transformers'
        choice_c = 'When the power-supply fuse rating equals the primary winding current'
        choice_d = 'When the load resistance is infinite'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When will a power source deliver maximum output to the load?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_750:
    def __init__(self, *args, **kwargs):
        choice_a = 'The source delivers maximum power to the load*'
        choice_b = 'The electrical load is shorted'
        choice_c = 'No current can flow through the circuit'
        choice_d = 'The source delivers minimum power to the load'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What happens when the impedance of an electrical load is equal to the internal impedance of the power source?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_751:
    def __init__(self, *args, **kwargs):
        choice_a = 'So the source can deliver maximum power to the load*'
        choice_b = 'So the load will draw minimum power from the source'
        choice_c = 'To ensure that there is less resistance than reactance in the circuit'
        choice_d = 'To ensure that the resistance and reactance in the circuit are equal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is impedance matching important?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_752:
    def __init__(self, *args, **kwargs):
        choice_a = 'matching of impedances*'
        choice_b = 'high load impedance'
        choice_c = 'low load resistance'
        choice_d = 'inductive impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To obtain efficient power transmission from a transmitter to an antenna requires:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_753:
    def __init__(self, *args, **kwargs):
        choice_a = 'matching of impedance*'
        choice_b = 'high load impedance'
        choice_c = 'proper method of balance'
        choice_d = 'low load resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To obtain efficient transfer of power from a transmitter to an antenna, it is important that there is a:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_754:
    def __init__(self, *args, **kwargs):
        choice_a = 'will have no effect on the matching*'
        choice_b = 'must be a full wavelength long'
        choice_c = 'must be an odd number of quarter-wave'
        choice_d = 'must be an even number of half-waves'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an antenna is correctly matched to a transmitter, the length of transmission line:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_755:
    def __init__(self, *args, **kwargs):
        choice_a = 'transfer the maximum amount of power to the antenna*'
        choice_b = 'ensure that the radiated signal has the intended polarization'
        choice_c = 'prevent frequency drift'
        choice_d = 'overcome fading of the transmitted signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Compared with a horizontal antenna, a vertical antenna will receive a vertically polarized radio wave:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_756:
    def __init__(self, *args, **kwargs):
        choice_a = '6:1*'
        choice_b = '2:1'
        choice_c = '4:1'
        choice_d = '10:1'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the centre impedance of a folded dipole is approximately 300 ohms, and you are using RG8U (50 ohms) coaxial lines, what is the ratio required to have the line and the antenna matched?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_757:
    def __init__(self, *args, **kwargs):
        choice_a = 'The electric lines of force of a radio wave are parallel to the Earth\'s surface*'
        choice_b = 'The electric and magnetic lines of force of a radio wave are perpendicular to the Earth\'s surface'
        choice_c = 'The electric lines of force of a radio wave are perpendicular to the Earth\'s surface'
        choice_d = 'The magnetic lines of force of a radio wave are parallel to the Earth\'s surface'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does horizontal wave polarization mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_758:
    def __init__(self, *args, **kwargs):
        choice_a = 'The electric lines of force of a radio wave are perpendicular to the Earth\'s surface*'
        choice_b = 'The magnetic lines of force of a radio wave are perpendicular to the Earth\'s surface'
        choice_c = 'The electric and magnetic lines of force of a radio wave are parallel to the Earth\'s surface'
        choice_d = 'The electric lines of force of a radio wave are parallel to the Earth\'s surface'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does vertical wave polarization mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_759:
    def __init__(self, *args, **kwargs):
        choice_a = 'Horizontal*'
        choice_b = 'Helical'
        choice_c = 'Vertical'
        choice_d = 'Circular'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What electromagnetic wave polarization does a Yagi antenna have when its elements are parallel to the Earth's surface?
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_760:
    def __init__(self, *args, **kwargs):
        choice_a = 'Vertical*'
        choice_b = 'Circular'
        choice_c = 'Horizontal'
        choice_d = 'Parabolical'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What electromagnetic wave polarization does a half-wavelength antenna have when it is perpendicular to the Earth's surface?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_761:
    def __init__(self, *args, **kwargs):
        choice_a = 'the orientation of the electric field relative to the Earth\'s surface*'
        choice_b = 'the height of the antenna'
        choice_c = 'the type of antenna'
        choice_d = 'the magnetic field'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Polarization of an antenna is determined by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_762:
    def __init__(self, *args, **kwargs):
        choice_a = 'a hypothetical point source*'
        choice_b = 'an infinitely long piece of wire'
        choice_c = 'a dummy load'
        choice_d = 'a half-wave reference dipole'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An isotropic antenna is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_763:
    def __init__(self, *args, **kwargs):
        choice_a = 'A sphere*'
        choice_b = 'A parabola'
        choice_c = 'A cardioid'
        choice_d = 'A unidirectional cardioid'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the antenna radiation pattern for an isotropic radiator?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_764:
    def __init__(self, *args, **kwargs):
        choice_a = 'vertical ground-plane antenna*'
        choice_b = 'random length of wire'
        choice_c = 'horizontal ground-plane antenna'
        choice_d = 'horizontal dipole antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""VHF signals from a mobile station using a vertical whip antenna will normally be best received using a:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_765:
    def __init__(self, *args, **kwargs):
        choice_a = 'mounted vertically*'
        choice_b = 'fed with the correct type of RF'
        choice_c = 'too near to the ground'
        choice_d = 'parallel with the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A dipole antenna will emit a vertically polarized wave if it is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_766:
    def __init__(self, *args, **kwargs):
        choice_a = 'vertically polarized*'
        choice_b = 'polarized at right angles to original'
        choice_c = 'horizontally polarized'
        choice_d = 'polarized in any plane'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an electromagnetic wave leaves an antenna vertically polarized, it will arrive at the receiving antenna, by ground wave:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_767:
    def __init__(self, *args, **kwargs):
        choice_a = 'at greater strength*'
        choice_b = 'at weaker strength'
        choice_c = 'without any comparative difference'
        choice_d = 'if the antenna changes the polarization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Compared with a horizontal antenna, a vertical antenna will receive a vertically polarized radio wave:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_768:
    def __init__(self, *args, **kwargs):
        choice_a = 'It decreases*'
        choice_b = 'It increases'
        choice_c = 'It stays the same'
        choice_d = 'It disappears'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an antenna is made longer, what happens to its resonant frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_769:
    def __init__(self, *args, **kwargs):
        choice_a = 'It increases*'
        choice_b = 'It stays the same'
        choice_c = 'It disappears'
        choice_d = 'It decreases'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If an antenna is made shorter, what happens to its resonant frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_770:
    def __init__(self, *args, **kwargs):
        choice_a = '12 metres (39.4 ft)*'
        choice_b = '15 metres (49.2 ft)'
        choice_c = '4 metres (13.1 ft)'
        choice_d = '32 metres (105 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The wavelength for a frequency of 25 MHz is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_771:
    def __init__(self, *args, **kwargs):
        choice_a = '300 000 kilometres per second*'
        choice_b = '3000 kilometres per second'
        choice_c = '150 kilometres per second'
        choice_d = '186 000 kilometres per second'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The velocity of propagation of radio frequency energy in free space is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_772:
    def __init__(self, *args, **kwargs):
        choice_a = 'decrease the resonant frequency*'
        choice_b = 'increase the resonant frequency'
        choice_c = 'have little effect'
        choice_d = 'have no change on the resonant frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Adding a series inductance to an antenna would:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_773:
    def __init__(self, *args, **kwargs):
        choice_a = 'shortening the radiating element*'
        choice_b = 'lowering the radiating element'
        choice_c = 'increasing the height of the radiating element'
        choice_d = 'lengthening the radiating element'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The resonant frequency of an antenna may be increased by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_774:
    def __init__(self, *args, **kwargs):
        choice_a = 'is the same as the speed of light*'
        choice_b = 'is infinite in space'
        choice_c = 'is always less than half speed of light'
        choice_d = 'varies directly with frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The speed of a radio wave:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_775:
    def __init__(self, *args, **kwargs):
        choice_a = 'limit the electrical length of the antenna*'
        choice_b = 'increase the effective antenna length'
        choice_c = 'allow the antenna to be more easily held vertically'
        choice_d = 'prevent any loss of radio waves by the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At the end of suspended antenna wire, insulators are used. These act to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_776:
    def __init__(self, *args, **kwargs):
        choice_a = 'lengthen it*'
        choice_b = 'shorten it'
        choice_c = 'ground one end'
        choice_d = 'centre feed it with TV ribbon transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To lower the resonant frequency of an antenna, the operator should:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_777:
    def __init__(self, *args, **kwargs):
        choice_a = 'a coil and capacitor in parallel*'
        choice_b = 'large wire-wound resistors'
        choice_c = 'coils wrapped around a ferrite rod'
        choice_d = 'hollow metal cans'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One solution to multiband operation with a shortened radiator is the "trap dipole" or trap vertical. These "traps" are actually:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_778:
    def __init__(self, *args, **kwargs):
        choice_a = '150 m (492 ft)*'
        choice_b = '360 m (1181 ft)'
        choice_c = '1500 m (4921 ft)'
        choice_d = '30 m (98 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The wavelength corresponding to a frequency of 2 MHz is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_779:
    def __init__(self, *args, **kwargs):
        choice_a = 'An antenna where some elements obtain their radio energy by induction or radiation from a driven element*'
        choice_b = 'An antenna where the driven element obtains its radio energy by induction or radiation from director elements'
        choice_c = 'An antenna where all elements are driven by direct connection to the transmission line'
        choice_d = 'An antenna where wave traps are used to magnetically couple the elements'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a parasitic beam antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_780:
    def __init__(self, *args, **kwargs):
        choice_a = 'Use larger diameter elements*'
        choice_b = 'Use traps on the elements'
        choice_c = 'Use tapered-diameter elements'
        choice_d = 'Use closer element spacing'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can the bandwidth of a parasitic beam antenna be increased?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_781:
    def __init__(self, *args, **kwargs):
        choice_a = 'A major lobe will develop in the horizontal plane, from the dipole toward the parasitic element*'
        choice_b = 'A major lobe will develop in the horizontal plane, parallel to the two elements'
        choice_c = 'A major lobe will develop in the vertical plane, away from the ground'
        choice_d = 'The radiation pattern will not be affected'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a parasitic element slightly shorter than a horizontal dipole antenna is placed parallel to the dipole 0.1 wavelength from it and at the same height, what effect will this have on the antenna's radiation pattern?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_782:
    def __init__(self, *args, **kwargs):
        choice_a = 'A major lobe will develop in the horizontal plane, from the parasitic element toward the dipole*'
        choice_b = 'A major lobe will develop in the horizontal plane, parallel to the two elements'
        choice_c = 'A major lobe will develop in the vertical plane, away from the ground'
        choice_d = 'The radiation pattern will not be affected'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a parasitic element slightly longer than a horizontal dipole antenna is placed parallel to the dipole 0.1 wavelength from it and at the same height, what effect will this have on the antenna's radiation pattern?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_783:
    def __init__(self, *args, **kwargs):
        choice_a = 'bandwidth*'
        choice_b = 'front-to-back ratio'
        choice_c = 'impedance'
        choice_d = 'polarization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The property of an antenna, which defines the range of frequencies to which it will respond, is called its:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_784:
    def __init__(self, *args, **kwargs):
        choice_a = '2.1 dB*'
        choice_b = '1.5 dB'
        choice_c = '3.0 dB'
        choice_d = '6.0 dB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how much gain does a half-wave dipole have over an isotropic radiator?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_785:
    def __init__(self, *args, **kwargs):
        choice_a = 'The numerical ratio relating the radiated signal strength of an antenna to that of another antenna*'
        choice_b = 'The numerical ratio of the signal in the forward direction to the signal in the back direction'
        choice_c = 'The numerical ratio of the amount of power radiated by an antenna compared to the transmitter output power'
        choice_d = 'The power amplifier gain minus the transmission line losses'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by antenna gain?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_786:
    def __init__(self, *args, **kwargs):
        choice_a = 'The frequency range over which the antenna may be expected to perform well*'
        choice_b = 'Antenna length divided by the number of elements'
        choice_c = 'The angle between the half-power radiation points'
        choice_d = 'The angle formed between two imaginary lines drawn through the ends of the elements'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by antenna bandwidth?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_787:
    def __init__(self, *args, **kwargs):
        choice_a = 'Minimum radiation from the ends, maximum broadside*'
        choice_b = 'Maximum radiation from the ends, minimum broadside'
        choice_c = 'Omnidirectional'
        choice_d = 'Maximum radiation at 45 degrees to the plane of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" In free space, what is the radiation characteristic of a half-wave dipole?
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_788:
    def __init__(self, *args, **kwargs):
        choice_a = 'isotropic*'
        choice_b = 'ideal'
        choice_c = 'ionosphere'
        choice_d = 'interpolated'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The gain of an antenna, especially on VHF and above, is quoted in dBi. The "i" in this expression stands for:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_789:
    def __init__(self, *args, **kwargs):
        choice_a = 'the ratio of the maximum forward power in the major lobe to the maximum backward power radiation*'
        choice_b = 'the forward power of the major lobe to the power in the backward direction both being measured at the 3 dB points'
        choice_c = 'undefined'
        choice_d = 'the ratio of the forward power at the 3 dB points to the power radiated in the backward direction'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The front-to-back ratio of a beam antenna is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_790:
    def __init__(self, *args, **kwargs):
        choice_a = 'Divide 71.5 (234) by the antenna\'s operating frequency in MHz*'
        choice_b = 'Divide 468 (1532) by the antenna\'s operating frequency in MHz'
        choice_c = 'Divide 300 (982) by the antenna\'s operating frequency in MHz'
        choice_d = 'Divide 150 (491) by the antenna\'s operating frequency in MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" How do you calculate the length in metres (feet) of a quarter-wavelength vertical antenna?
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_791:
    def __init__(self, *args, **kwargs):
        choice_a = '3.36 metres (11.0 ft)*'
        choice_b = '3.6 metres (11.8 ft)'
        choice_c = '7.2 metres (23.6 ft)'
        choice_d = '6.76 metres (22.2 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you made a quarter-wavelength vertical antenna for 21.125 MHz, how long would it be?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_792:
    def __init__(self, *args, **kwargs):
        choice_a = '64 cm (25.2 in)*'
        choice_b = '128 cm (50.4 in)'
        choice_c = '105 cm (41.3 in)'
        choice_d = '134.6 cm (53 in)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you made a half-wavelength vertical antenna for 223 MHz, how long would it be?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_793:
    def __init__(self, *args, **kwargs):
        choice_a = 'A 5/8-wavelength antenna has more gain*'
        choice_b = 'A 5/8-wavelength antenna has less corona loss'
        choice_c = 'A 5/8-wavelength antenna is easier to install on a car'
        choice_d = 'A 5/8-wavelength antenna can handle more power'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is a 5/8-wavelength vertical antenna better than a 1/4-wavelength vertical antenna for VHF or UHF mobile operations?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_794:
    def __init__(self, *args, **kwargs):
        choice_a = 'It goes out equally well in all horizontal directions*'
        choice_b = 'Most of it is aimed high into the sky'
        choice_c = 'Most of it goes equally in two opposite directions'
        choice_d = 'Most of it goes in one direction'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a magnetic-base whip antenna is placed on the roof of a car, in what direction does it send out radio energy?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_795:
    def __init__(self, *args, **kwargs):
        choice_a = 'It brings the feed point impedance closer to 50 ohms*'
        choice_b = 'It increases the radiation angle'
        choice_c = 'It brings the feed point impedance closer to 300 ohms'
        choice_d = 'It lowers the radiation angle'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is an advantage of downward sloping radials on a ground plane antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_796:
    def __init__(self, *args, **kwargs):
        choice_a = 'It increases*'
        choice_b = 'It decreases'
        choice_c = 'It stays the same'
        choice_d = 'It approaches zero'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What happens to the feed point impedance of a ground-plane antenna when its radials are changed from horizontal to downward-sloping?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_797:
    def __init__(self, *args, **kwargs):
        choice_a = '50 ohms coaxial cable*'
        choice_b = '300 ohms balanced transmission line'
        choice_c = '75 ohms balanced transmission line'
        choice_d = '300 ohms coaxial cable'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following transmission lines will give the best match to the base of a quarter-wave ground-plane antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_798:
    def __init__(self, *args, **kwargs):
        choice_a = 'receive signals equally well from all compass points around it*'
        choice_b = 'be very sensitive to signals coming from horizontal antennas'
        choice_c = 'require few insulators'
        choice_d = 'be easy to feed with TV ribbon transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The main characteristic of a vertical antenna is that it will:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_799:
    def __init__(self, *args, **kwargs):
        choice_a = 'To tune out capacitive reactance*'
        choice_b = 'To lower the losses'
        choice_c = 'To lower the Q'
        choice_d = 'To filter out electrical noise'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is a loading coil often used with an HF mobile vertical antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_800:
    def __init__(self, *args, **kwargs):
        choice_a = 'The angle of radiation is low*'
        choice_b = 'The angle of radiation is high giving excellent local coverage'
        choice_c = 'It is easy to match the antenna to the transmitter'
        choice_d = 'It\'s a convenient length on VHF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the main reason why so many VHF base and mobile antennas are 5/8 of a wavelength?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_801:
    def __init__(self, *args, **kwargs):
        choice_a = 'One*'
        choice_b = 'Two'
        choice_c = 'Three'
        choice_d = 'None'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How many directly driven elements do most Yagi antennas have?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_802:
    def __init__(self, *args, **kwargs):
        choice_a = '10.21 metres (33.5 feet)*'
        choice_b = '5.21 metres (17 feet)'
        choice_c = '10.67 metres (35 feet)'
        choice_d = '20.12 metres (66 feet)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how long is the driven element of a Yagi antenna for 14.0 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_803:
    def __init__(self, *args, **kwargs):
        choice_a = '6.4 metres (21 feet)*'
        choice_b = '5.18 metres (17 feet)'
        choice_c = '3.2 metres (10.5 feet)'
        choice_d = '12.8 metres (42 feet)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how long is the director element of a Yagi antenna for 21.1 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_804:
    def __init__(self, *args, **kwargs):
        choice_a = '5.33 metres (17.5 feet)*'
        choice_b = '4.88 metres (16 feet)'
        choice_c = '10.67 metres (35 feet)'
        choice_d = '2.66 metres (8.75 feet)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how long is the reflector element of a Yagi antenna for 28.1 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_805:
    def __init__(self, *args, **kwargs):
        choice_a = 'Gain increases*'
        choice_b = 'SWR increases'
        choice_c = 'Weight decreases'
        choice_d = 'Wind load decreases'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one effect of increasing the boom length and adding directors to a Yagi antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_806:
    def __init__(self, *args, **kwargs):
        choice_a = 'High gain, less critical tuning and wider bandwidth*'
        choice_b = 'High gain, lower loss and a low SWR'
        choice_c = 'High front-to-back ratio and lower input resistance'
        choice_d = 'Shorter boom length, lower weight and wind resistance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What are some advantages of a Yagi with wide element spacing?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_807:
    def __init__(self, *args, **kwargs):
        choice_a = 'It helps reduce interference from other stations off to the side or behind*'
        choice_b = 'It provides excellent omnidirectional coverage in the horizontal plane'
        choice_c = 'It is smaller, less expensive and easier to erect than a dipole or vertical antenna'
        choice_d = 'It provides the highest possible angle of radiation for the HF bands'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is a Yagi antenna often used for radiocommunications on the 20-metre band?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_808:
    def __init__(self, *args, **kwargs):
        choice_a = 'The power radiated in the major radiation lobe compared to the power radiated in exactly the opposite direction*'
        choice_b = 'The relative position of the driven element with respect to the reflectors and directors'
        choice_c = 'The power radiated in the major radiation lobe compared to the power radiated 90 degrees away from that direction'
        choice_d = 'The number of directors versus the number of reflectors'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does "antenna front-to-back ratio" mean in reference to a Yagi antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_809:
    def __init__(self, *args, **kwargs):
        choice_a = 'Optimize the lengths and spacing of the elements*'
        choice_b = 'Use RG-58 transmission line'
        choice_c = 'Use a reactance bridge to measure the antenna performance from each direction around the antenna'
        choice_d = 'Avoid using towers higher than 9 metres (30 feet) above the ground'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a good way to get maximum performance from a Yagi antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_810:
    def __init__(self, *args, **kwargs):
        choice_a = '0.20*'
        choice_b = '0.10'
        choice_c = '0.50'
        choice_d = '0.75'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The spacing between the elements on a three-element Yagi antenna, representing the best overall choice, is _____ of a wavelength."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_811:
    def __init__(self, *args, **kwargs):
        choice_a = '13 dBi*'
        choice_b = '7 dBi'
        choice_c = '20 dBi'
        choice_d = '10 dBi'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the forward gain of a six-element Yagi is about 10 dBi, what would the gain of two of these antennas be if they were "stacked"?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_812:
    def __init__(self, *args, **kwargs):
        choice_a = '5.08 metres (16.62 ft)*'
        choice_b = '10.5 metres (34.37 ft)'
        choice_c = '28.55 metres (93.45 ft)'
        choice_d = '10.16 metres (33.26 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you made a half-wavelength dipole antenna for 28.150 MHz, how long would it be?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_813:
    def __init__(self, *args, **kwargs):
        choice_a = 'You may experience RF feedback in your station*'
        choice_b = 'It usually produces vertically polarized radiation'
        choice_c = 'It must be longer than 1 wavelength'
        choice_d = 'You must use an inverted T matching network for multi-band operation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one disadvantage of a random wire antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_814:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is a figure-eight, perpendicular to the antenna*'
        choice_b = 'It is a circle (equal radiation in all directions)'
        choice_c = 'It is two smaller lobes on one side of the antenna, and one larger lobe on the other side'
        choice_d = 'It is a figure-eight, off both ends of the antenna'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the low angle radiation pattern of an ideal half-wavelength dipole HF antenna in free space installed parallel to the Earth?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_815:
    def __init__(self, *args, **kwargs):
        choice_a = '73 and 300*'
        choice_b = '73 and 150'
        choice_c = '52 and 100'
        choice_d = '52 and 200'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The impedances in ohms at the feed point of the dipole and folded dipole in free space are, respectively:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_816:
    def __init__(self, *args, **kwargs):
        choice_a = 'mostly to the East and West*'
        choice_b = 'mostly to the South and North'
        choice_c = 'mostly to the South'
        choice_d = 'equally in all directions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A horizontal dipole transmitting antenna, installed at an ideal height so that the ends are pointing North/South, radiates:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_817:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is greater*'
        choice_b = 'It is essentially the same'
        choice_c = 'It is less than 50%'
        choice_d = 'It is 0.707 times the bandwidth'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does the bandwidth of a folded dipole antenna compare with that of a simple dipole antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_818:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may radiate harmonics more readily*'
        choice_b = 'It is too sharply directional at lower frequencies'
        choice_c = 'It must be neutralized'
        choice_d = 'It can only be used for one band'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a disadvantage of using an antenna equipped with traps?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_819:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may be used for multi-band operation*'
        choice_b = 'It has high directivity at the higher frequencies'
        choice_c = 'It has high gain'
        choice_d = 'It minimizes harmonic radiation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is an advantage of using a trap antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_820:
    def __init__(self, *args, **kwargs):
        choice_a = '38 meters (125 ft)*'
        choice_b = '32 meters (105 ft)'
        choice_c = '45 meters (145 ft)'
        choice_d = '75 meters (245 ft)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you were to cut a half wave dipole for 3.75 MHz, what would be its approximate length?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_821:
    def __init__(self, *args, **kwargs):
        choice_a = 'Two or more parallel four-sided wire loops, each approximately one-electrical wavelength long*'
        choice_b = 'A center-fed wire 1/2-electrical wavelength long'
        choice_c = 'A vertical conductor 1/4-electrical wavelength high, fed at the bottom'
        choice_d = 'Four straight, parallel elements in line with each other, each approximately 1/2-electrical wavelength long'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a cubical quad antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_822:
    def __init__(self, *args, **kwargs):
        choice_a = 'An antenna whose elements are each a three sided loop whose total length is approximately one electrical wavelength*'
        choice_b = 'A large copper ring or wire loop, used in direction finding'
        choice_c = 'An antenna system made of three vertical antennas, arranged in a triangular shape'
        choice_d = 'An antenna made from several triangular coils of wire on an insulating form'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a delta loop antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_823:
    def __init__(self, *args, **kwargs):
        choice_a = '3.54 metres (11.7 feet)*'
        choice_b = '0.36 metres (1.17 feet)'
        choice_c = '14.33 metres (47 feet)'
        choice_d = '143 metres (469 feet)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how long is each side of a cubical quad antenna driven element for 21.4 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_824:
    def __init__(self, *args, **kwargs):
        choice_a = '5.36 metres (17.6 feet)*'
        choice_b = '21.43 metres (70.3 feet)'
        choice_c = '53.34 metres (175 feet)'
        choice_d = '7.13 metres (23.4 feet)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how long is each side of a cubical quad antenna driven element for 14.3 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_825:
    def __init__(self, *args, **kwargs):
        choice_a = '3.5 metres (11.5 feet)*'
        choice_b = '2.67 metres (8.75 feet)'
        choice_c = '7.13 metres (23.4 feet)'
        choice_d = '10.67 metres (35 feet)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Approximately how long is each leg of a symmetrical delta loop antenna driven element for 28.7 MHz?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_826:
    def __init__(self, *args, **kwargs):
        choice_a = 'They compare favourably with a three-element Yagi*'
        choice_b = 'They perform very well only at HF'
        choice_c = 'They are effective only when constructed using insulated wire'
        choice_d = 'They perform poorly above HF'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which statement about two-element delta loops and quad antennas is true?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_827:
    def __init__(self, *args, **kwargs):
        choice_a = 'The quad has more directivity in both horizontal and vertical planes*'
        choice_b = 'The quad has more directivity in the horizontal plane but less directivity in the vertical plane'
        choice_c = 'The quad has less directivity in the horizontal plane but more directivity in the vertical plane'
        choice_d = 'The quad has less directivity in both horizontal and vertical planes'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Compared to a dipole antenna, what are the directional radiation characteristics of a cubical quad antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_828:
    def __init__(self, *args, **kwargs):
        choice_a = 'It will change the antenna polarization from horizontal to vertical*'
        choice_b = 'It will change the antenna polarization from vertical to horizontal'
        choice_c = 'It will significantly decrease the antenna feed point impedance'
        choice_d = 'It will significantly increase the antenna feed point impedance'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Moving the feed point of a multi-element quad antenna from a side parallel to the ground to a side perpendicular to the ground will have what effect?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_829:
    def __init__(self, *args, **kwargs):
        choice_a = 'The power radiated in the major radiation lobe compared to the power radiated in exactly the opposite direction*'
        choice_b = 'The relative position of the driven element with respect to the reflectors and directors'
        choice_c = 'The power radiated in the major radiation lobe compared to the power radiated 90 degrees away from that direction'
        choice_d = 'The number of directors versus the number of reflectors'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does the term "antenna front-to-back ratio" mean in reference to a delta loop antenna?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_830:
    def __init__(self, *args, **kwargs):
        choice_a = 'one wavelength*'
        choice_b = 'three-quarters of a wavelength'
        choice_c = 'two wavelengths'
        choice_d = 'one-half wavelength'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The cubical "quad" or "quad" antenna consists of two or more square loops of wire. The driven element has an approximate overall length of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_831:
    def __init__(self, *args, **kwargs):
        choice_a = 'one wavelength*'
        choice_b = 'one-quarter of a wavelength'
        choice_c = 'two wavelengths'
        choice_d = 'one-half of a wavelength'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The delta loop antenna consists of two or more triangular structures mounted on a boom. The overall length of the driven element is approximately:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_832:
    def __init__(self, *args, **kwargs):
        choice_a = 'Line-of-sight propagation*'
        choice_b = 'Tunnel propagation'
        choice_c = 'Skywave propagation'
        choice_d = 'Auroral propagation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of propagation usually occurs from one hand-held VHF transceiver to another nearby?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_833:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is much longer*'
        choice_b = 'It is much shorter'
        choice_c = 'It is about the same'
        choice_d = 'It depends on the weather'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does the range of sky-wave propagation compare to ground-wave propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_834:
    def __init__(self, *args, **kwargs):
        choice_a = 'Sky-wave propagation*'
        choice_b = 'Tropospheric propagation'
        choice_c = 'Ground-wave propagation'
        choice_d = 'Earth-Moon-Earth propagation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a signal is returned to Earth by the ionosphere, what is this called?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_835:
    def __init__(self, *args, **kwargs):
        choice_a = 'By direct wave*'
        choice_b = 'By sky wave'
        choice_c = 'By plane wave'
        choice_d = 'By geometric wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How are VHF signals propagated within the range of the visible horizon?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_836:
    def __init__(self, *args, **kwargs):
        choice_a = 'ionospheric wave*'
        choice_b = 'tropospheric wave'
        choice_c = 'ground wave'
        choice_d = 'inverted wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Skywave is another name for:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_837:
    def __init__(self, *args, **kwargs):
        choice_a = 'ground wave*'
        choice_b = 'tropospheric wave'
        choice_c = 'ionospheric wave'
        choice_d = 'inverted wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""That portion of the radiation which is directly affected by the surface of the Earth is called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_838:
    def __init__(self, *args, **kwargs):
        choice_a = 'ground wave*'
        choice_b = 'troposphere'
        choice_c = 'skip wave'
        choice_d = 'ionosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At lower HF frequencies, radiocommunication out to 200 km is made possible by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_839:
    def __init__(self, *args, **kwargs):
        choice_a = 'is less at higher frequencies*'
        choice_b = 'depends on the maximum usable frequency'
        choice_c = 'is more at higher frequencies'
        choice_d = 'is the same for all frequencies'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The distance travelled by ground waves:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_840:
    def __init__(self, *args, **kwargs):
        choice_a = 'ionospheric wave*'
        choice_b = 'F layer'
        choice_c = 'surface wave'
        choice_d = 'skip wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The radio wave which follows a path from the transmitter to the ionosphere and back to Earth is known correctly as the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_841:
    def __init__(self, *args, **kwargs):
        choice_a = 'ionospheric wave*'
        choice_b = 'ground wave'
        choice_c = 'skip wave'
        choice_d = 'surface wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Reception of high frequency (HF) radio waves beyond 4000 km is generally made possible by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_842:
    def __init__(self, *args, **kwargs):
        choice_a = 'Solar radiation ionizing the outer atmosphere*'
        choice_b = 'Lightning ionizing the outer atmosphere'
        choice_c = 'Release of fluorocarbons into the atmosphere'
        choice_d = 'Temperature changes ionizing the outer atmosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes the ionosphere to form?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_843:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ultraviolet*'
        choice_b = 'Microwave'
        choice_c = 'Ionized particles'
        choice_d = 'Thermal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of solar radiation is most responsible for ionization in the outer atmosphere?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_844:
    def __init__(self, *args, **kwargs):
        choice_a = 'The D region*'
        choice_b = 'The E region'
        choice_c = 'The F region'
        choice_d = 'The A region'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which ionospheric region is closest to the Earth?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_845:
    def __init__(self, *args, **kwargs):
        choice_a = 'The D region*'
        choice_b = 'The F2 region'
        choice_c = 'The F1 region'
        choice_d = 'The E region'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which region of the ionosphere is the least useful for long distance radio-wave propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_846:
    def __init__(self, *args, **kwargs):
        choice_a = 'F1 and F2*'
        choice_b = 'Troposphere and stratosphere'
        choice_c = 'Electrostatic and electromagnetic'
        choice_d = 'D and E'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What two sub-regions of ionosphere exist only in the daytime?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_847:
    def __init__(self, *args, **kwargs):
        choice_a = 'Midday*'
        choice_b = 'Dawn'
        choice_c = 'Midnight'
        choice_d = 'Dusk'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When is the ionosphere most ionized?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_848:
    def __init__(self, *args, **kwargs):
        choice_a = 'Shortly before dawn*'
        choice_b = 'Just after noon'
        choice_c = 'Just after dusk'
        choice_d = 'Shortly before midnight'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When is the ionosphere least ionized?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_849:
    def __init__(self, *args, **kwargs):
        choice_a = 'Because it is the highest ionospheric region*'
        choice_b = 'Because it exists only at night'
        choice_c = 'Because it is the lowest ionospheric region'
        choice_d = 'Because it does not absorb radio waves as much as other ionospheric regions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is the F2 region mainly responsible for the longest distance radio-wave propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_850:
    def __init__(self, *args, **kwargs):
        choice_a = 'Because of D-region absorption*'
        choice_b = 'Because of auroral propagation'
        choice_c = 'Because of magnetic flux'
        choice_d = 'Because of a lack of activity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the main reason the 160, 80 and 40 metre amateur bands tend to be useful only for short-distance communications during daylight hours?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_851:
    def __init__(self, *args, **kwargs):
        choice_a = 'F1 and F2*'
        choice_b = 'D1 and D2'
        choice_c = 'E1 and E2'
        choice_d = 'A and B'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""During the day, one of the ionospheric layers splits into two parts called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_852:
    def __init__(self, *args, **kwargs):
        choice_a = 'below the F layer*'
        choice_b = 'below the D layer'
        choice_c = 'sporadic'
        choice_d = 'above the F layer'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The position of the E layer in the ionosphere is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_853:
    def __init__(self, *args, **kwargs):
        choice_a = 'An area which is too far away for ground-wave propagation, but too close for sky-wave propagation*'
        choice_b = 'An area which is too far away for ground-wave or sky-wave propagation'
        choice_c = 'An area covered by sky-wave propagation'
        choice_d = 'An area covered by ground-wave propagation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a skip zone?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_854:
    def __init__(self, *args, **kwargs):
        choice_a = '4000 km (2500 miles)*'
        choice_b = 'None, the F2 region does not support radio-wave propagation'
        choice_c = '2000 km (1250 miles)'
        choice_d = '300 km (190 miles)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the maximum distance along the Earth's surface that is normally covered in one hop using the F2 region?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_855:
    def __init__(self, *args, **kwargs):
        choice_a = '2000 km (1250 miles)*'
        choice_b = '300 km (190 miles)'
        choice_c = '4000 km (2500 miles)'
        choice_d = 'None, the E region does not support radio-wave propagation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the maximum distance along the Earth's surface that is normally covered in one hop using the E region?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_856:
    def __init__(self, *args, **kwargs):
        choice_a = 'a zone between the end of the ground wave and the point where the first refracted wave returns to Earth*'
        choice_b = 'a zone of silence caused by lost sky waves'
        choice_c = 'a zone between any two refracted waves'
        choice_d = 'a zone between the antenna and the return of the first refracted wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Skip zone is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_857:
    def __init__(self, *args, **kwargs):
        choice_a = 'Multihop*'
        choice_b = 'Sporadic "E"'
        choice_c = 'Back scatter'
        choice_d = 'Tropospheric scatter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The distance to Europe from your location is approximately 5000 km. What sort of propagation is the most likely to be involved?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_858:
    def __init__(self, *args, **kwargs):
        choice_a = 'height of the ionosphere and the angle of radiation*'
        choice_b = 'power fed to the power amplifier'
        choice_c = 'angle of radiation'
        choice_d = 'type of transmitting antenna used'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""For radio signals, the skip distance is determined by the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_859:
    def __init__(self, *args, **kwargs):
        choice_a = 'skip distance*'
        choice_b = 'skip zone'
        choice_c = 'angle of radiation'
        choice_d = 'maximum usable frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The distance from the transmitter to the nearest point where the sky wave returns to the Earth is called the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_860:
    def __init__(self, *args, **kwargs):
        choice_a = 'the minimum distance reached by a signal after one reflection by the ionosphere*'
        choice_b = 'the maximum distance reached by a signal after one reflection by the ionosphere'
        choice_c = 'the minimum distance reached by a ground-wave signal'
        choice_d = 'the maximum distance a signal will travel by both a ground wave and reflected wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Skip distance is the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_861:
    def __init__(self, *args, **kwargs):
        choice_a = 'reflection and refraction from the ionosphere*'
        choice_b = 'selective fading of local signals'
        choice_c = 'high gain antennas being used'
        choice_d = 'local cloud cover'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Skip distance is a term associated with signals from the ionosphere. Skip effects are due to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_862:
    def __init__(self, *args, **kwargs):
        choice_a = 'angle between the ground and the radiation is smallest*'
        choice_b = 'polarization is vertical'
        choice_c = 'ionosphere is most densely ionized'
        choice_d = 'signal given out is strongest'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The skip distance of a sky wave will be greatest when the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_863:
    def __init__(self, *args, **kwargs):
        choice_a = 'becomes greater*'
        choice_b = 'stays the same'
        choice_c = 'varies regularly'
        choice_d = 'decreases'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If the height of the reflecting layer of the ionosphere increases, the skip distance of a high frequency (HF) transmission:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_864:
    def __init__(self, *args, **kwargs):
        choice_a = 'It absorbs the signals*'
        choice_b = 'It bends the radio waves out into space'
        choice_c = 'It refracts the radio waves back to Earth'
        choice_d = 'It has little or no effect on 80-metre radio waves'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What effect does the D region of the ionosphere have on lower frequency HF signals in the daytime?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_865:
    def __init__(self, *args, **kwargs):
        choice_a = 'The ionization of the D region*'
        choice_b = 'The presence of ionized clouds in the E region'
        choice_c = 'The splitting of the F region'
        choice_d = 'The weather below the ionosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes distant AM broadcast and 160 metre ham band stations not to be heard during daytime hours?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_866:
    def __init__(self, *args, **kwargs):
        choice_a = 'fading*'
        choice_b = 'baffling'
        choice_c = 'absorption'
        choice_d = 'skip'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two or more parts of the radio wave follow different paths during propagation and this may result in phase differences at the receiver. This "change" at the receiver is called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_867:
    def __init__(self, *args, **kwargs):
        choice_a = 'fading*'
        choice_b = 'absorption'
        choice_c = 'fluctuation'
        choice_d = 'path loss'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A change or variation in signal strength at the antenna, caused by differences in path lengths, is called:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_868:
    def __init__(self, *args, **kwargs):
        choice_a = 'variations in signal strength*'
        choice_b = 'consistent fading of received signal'
        choice_c = 'consistently stronger signals'
        choice_d = 'a change in the ground-wave signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When a transmitted radio signal reaches a station by a one-hop and two-hop skip path, small changes in the ionosphere can cause:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_869:
    def __init__(self, *args, **kwargs):
        choice_a = 'cause a fade-out of sky-wave signals*'
        choice_b = 'produce extreme weather changes'
        choice_c = 'prevent communications by ground wave'
        choice_d = 'increase the maximum usable frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The usual effect of ionospheric storms is to:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_870:
    def __init__(self, *args, **kwargs):
        choice_a = 'The ionosphere can change the polarization of the signal from moment to moment*'
        choice_b = 'The ground wave and the sky wave continually shift the polarization'
        choice_c = 'Anomalies in the Earth\'s magnetic field produce a profound effect on HF polarization but not on VHF & UHF frequencies'
        choice_d = 'Greater selectivity is possible with HF receivers making changes in polarization redundant'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On the VHF and UHF bands, polarization of the receiving antenna is very important in relation to the transmitting antenna, yet on HF bands it is relatively unimportant. Why is that so?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_871:
    def __init__(self, *args, **kwargs):
        choice_a = 'Phase differences between radio wave components of the same transmission, as experienced at the receiving station*'
        choice_b = 'Small changes in beam heading at the receiving station'
        choice_c = 'Time differences between the receiving and transmitting stations'
        choice_d = 'Large changes in the height of the ionosphere at the receiving station ordinarily occurring shortly before sunrise and sunset'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes selective fading?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_872:
    def __init__(self, *args, **kwargs):
        choice_a = 'It is more pronounced at wide bandwidths*'
        choice_b = 'It is the same for both wide and narrow bandwidths'
        choice_c = 'Only the receiver bandwidth determines the selective fading effect'
        choice_d = 'It is more pronounced at narrow bandwidths'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How does the bandwidth of a transmitted signal affect selective fading?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_873:
    def __init__(self, *args, **kwargs):
        choice_a = 'Parabolic interaction*'
        choice_b = 'Reflections'
        choice_c = 'Passage through magnetic fields (Faraday rotation)'
        choice_d = 'Refractions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Polarization change often takes place on radio waves that are propagated over long distances. Which of these does not cause polarization change?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_874:
    def __init__(self, *args, **kwargs):
        choice_a = 'little or no phase-shift distortion*'
        choice_b = 'phase-shift distortion'
        choice_c = 'signal cancellation at the receiver'
        choice_d = 'a high-pitch squeal at the receiver'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Reflection of a SSB transmission from the ionosphere causes:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_875:
    def __init__(self, *args, **kwargs):
        choice_a = 'The more sunspots there are, the greater the ionization*'
        choice_b = 'The more sunspots there are, the less the ionization'
        choice_c = 'Unless there are sunspots, the ionization is zero'
        choice_d = 'They have no effect'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How do sunspots change the ionization of the atmosphere?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_876:
    def __init__(self, *args, **kwargs):
        choice_a = '11 years*'
        choice_b = '17 years'
        choice_c = '5 years'
        choice_d = '7 years'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How long is an average sunspot cycle?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_877:
    def __init__(self, *args, **kwargs):
        choice_a = 'The radio energy emitted by the sun*'
        choice_b = 'A measure of the tilt of the Earth\'s ionosphere on the side toward the sun'
        choice_c = 'The number of sunspots on the side of the sun facing the Earth'
        choice_d = 'The density of the sun\'s magnetic field'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is solar flux?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_878:
    def __init__(self, *args, **kwargs):
        choice_a = 'A measure of solar activity that is taken at a specific frequency*'
        choice_b = 'Another name for the American sunspot number'
        choice_c = 'A measure of solar activity that compares daily readings with results from the last six months'
        choice_d = 'A measure of solar activity that is taken annually'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is the solar-flux index?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_879:
    def __init__(self, *args, **kwargs):
        choice_a = 'Solar radiation*'
        choice_b = 'The F2 region of the ionosphere'
        choice_c = 'The F1 region of the ionosphere'
        choice_d = 'Lunar tidal effects'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What influences all radiocommunication beyond ground-wave or line-of-sight ranges?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_880:
    def __init__(self, *args, **kwargs):
        choice_a = 'Electromagnetic and particle emissions*'
        choice_b = 'Subaudible and audio-frequency emissions'
        choice_c = 'Polar region and equatorial emissions'
        choice_d = 'Infrared and gamma-ray emissions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which two types of radiation from the sun influence propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_881:
    def __init__(self, *args, **kwargs):
        choice_a = 'Frequencies up to 40 MHz or even higher become usable for long-distance communication*'
        choice_b = 'High frequency radio signals are absorbed'
        choice_c = 'Frequencies up to 100 MHz or higher are normally usable for long-distance communication'
        choice_d = 'High frequency radio signals become weak and distorted'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""When sunspot numbers are high, how is propagation affected?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_882:
    def __init__(self, *args, **kwargs):
        choice_a = 'sun*'
        choice_b = 'ionosphere'
        choice_c = 'aurora borealis'
        choice_d = 'atmospheric conditions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""All communication frequencies throughout the spectrum are affected in varying degrees by the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_883:
    def __init__(self, *args, **kwargs):
        choice_a = '11 years*'
        choice_b = '3 years'
        choice_c = '6 years'
        choice_d = '1 year'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Average duration of a solar cycle is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_884:
    def __init__(self, *args, **kwargs):
        choice_a = 'the amount of solar radiation*'
        choice_b = 'the power of the transmitted signal'
        choice_c = 'the receiver sensitivity'
        choice_d = 'upper atmosphere weather conditions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The ability of the ionosphere to reflect high frequency radio signals depends on:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_885:
    def __init__(self, *args, **kwargs):
        choice_a = 'years*'
        choice_b = 'months'
        choice_c = 'days'
        choice_d = 'centuries'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""HF radio propagation cycles have a period of approximately 11:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_886:
    def __init__(self, *args, **kwargs):
        choice_a = 'They pass through the ionosphere*'
        choice_b = 'They are absorbed by the ionosphere'
        choice_c = 'Their frequency is changed by the ionosphere to be below the maximum usable frequency'
        choice_d = 'They are reflected back to their source'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What happens to signals higher in frequency than the critical frequency?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_887:
    def __init__(self, *args, **kwargs):
        choice_a = 'The amount of radiation received from the sun, mainly ultraviolet*'
        choice_b = 'The temperature of the ionosphere'
        choice_c = 'The speed of the winds in the upper atmosphere'
        choice_d = 'The type of weather just below the ionosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes the maximum usable frequency to vary?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_888:
    def __init__(self, *args, **kwargs):
        choice_a = 'The highest frequency signal that will reach its intended destination*'
        choice_b = 'The lowest frequency signal that will reach its intended destination'
        choice_c = 'The highest frequency signal that is most absorbed by the ionosphere'
        choice_d = 'The lowest frequency signal that is most absorbed by the ionosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What does maximum usable frequency mean?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_889:
    def __init__(self, *args, **kwargs):
        choice_a = 'Try a higher frequency band*'
        choice_b = 'Try the other sideband'
        choice_c = 'Try a different antenna polarization'
        choice_d = 'Try a different frequency shift'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What can be done at an amateur station to continue HF communications during a sudden ionospheric disturbance?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_890:
    def __init__(self, *args, **kwargs):
        choice_a = 'Listen for signals from 10-metre beacon stations*'
        choice_b = 'Listen for signals from 20-metre beacon stations'
        choice_c = 'Listen for signals from 39-metre broadcast stations'
        choice_d = 'Listen for WWVH time signals on 20 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one way to determine if the maximum usable frequency (MUF) is high enough to support 28 MHz propagation between your station and western Europe?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_891:
    def __init__(self, *args, **kwargs):
        choice_a = 'They are bent back to the Earth*'
        choice_b = 'They are changed to a frequency above the MUF'
        choice_c = 'They are completely absorbed by the ionosphere'
        choice_d = 'They pass through the ionosphere'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What usually happens to radio waves with frequencies below the maximum usable frequency (MUF) when they are sent into the ionosphere?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_892:
    def __init__(self, *args, **kwargs):
        choice_a = 'At any point in the solar cycle*'
        choice_b = 'Only at the minimum point of the solar cycle'
        choice_c = 'Only at the maximum point of the solar cycle'
        choice_d = 'At the summer solstice'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""At what point in the solar cycle does the 20-metre band usually support worldwide propagation during daylight hours?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_893:
    def __init__(self, *args, **kwargs):
        choice_a = 'maximum usable frequency*'
        choice_b = 'skip distance'
        choice_c = 'speed of light'
        choice_d = 'sunspot frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If we transmit a signal, the frequency of which is so high we no longer receive a reflection from the ionosphere, the signal frequency is above the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_894:
    def __init__(self, *args, **kwargs):
        choice_a = 'daytime in summer*'
        choice_b = 'evening in winter'
        choice_c = 'evening in summer'
        choice_d = 'daytime in winter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Communication on the 80 metre band is generally most difficult during:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_895:
    def __init__(self, *args, **kwargs):
        choice_a = 'slightly lower*'
        choice_b = 'double the MUF'
        choice_c = 'half the MUF'
        choice_d = 'slightly higher'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""The optimum working frequency provides the best long range HF communication. Compared with the maximum usable frequency (MUF), it is usually:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_896:
    def __init__(self, *args, **kwargs):
        choice_a = '160 and 80 metres*'
        choice_b = '40 metres'
        choice_c = '30 metres'
        choice_d = '20 metres'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""During summer daytime, which bands are the most difficult for communications beyond ground wave?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_897:
    def __init__(self, *args, **kwargs):
        choice_a = 'The E region*'
        choice_b = 'The F2 region'
        choice_c = 'The F1 region'
        choice_d = 'The D region'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which ionospheric region most affects sky-wave propagation on the 6 metre band?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_898:
    def __init__(self, *args, **kwargs):
        choice_a = 'It lets you contact stations farther away*'
        choice_b = 'It causes them to travel shorter distances'
        choice_c = 'It garbles the signal'
        choice_d = 'It reverses the sideband of the signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What effect does tropospheric bending have on 2-metre radio waves?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_899:
    def __init__(self, *args, **kwargs):
        choice_a = 'A temperature inversion*'
        choice_b = 'Lightning between the transmitting and receiving stations'
        choice_c = 'An aurora to the north'
        choice_d = 'A very low pressure area'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes tropospheric ducting of radio waves?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_900:
    def __init__(self, *args, **kwargs):
        choice_a = 'tropospheric wave*'
        choice_b = 'inverted wave'
        choice_c = 'ground wave'
        choice_d = 'ionospheric wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""That portion of the radiation kept close to the Earth's surface due to bending in the atmosphere is called the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_901:
    def __init__(self, *args, **kwargs):
        choice_a = 'Patches of dense ionization at E-region height*'
        choice_b = 'Partial tropospheric ducting at E-region height'
        choice_c = 'Variations in E-region height caused by sunspot variations'
        choice_d = 'A brief decrease in VHF signals caused by sunspot variations'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a sporadic-E condition?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_902:
    def __init__(self, *args, **kwargs):
        choice_a = '6 metres*'
        choice_b = '160 metres'
        choice_c = '20 metres'
        choice_d = '2 metres'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On which amateur frequency band is the extended-distance propagation effect of sporadic-E most often observed?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_903:
    def __init__(self, *args, **kwargs):
        choice_a = 'North*'
        choice_b = 'East'
        choice_c = 'West'
        choice_d = 'South'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In the northern hemisphere, in which direction should a directional antenna be pointed to take maximum advantage of auroral propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_904:
    def __init__(self, *args, **kwargs):
        choice_a = 'At E-region height*'
        choice_b = 'At F-region height'
        choice_c = 'In the equatorial band'
        choice_d = 'At D-region height'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Where in the ionosphere does auroral activity occur?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_905:
    def __init__(self, *args, **kwargs):
        choice_a = 'CW*'
        choice_b = 'RTTY'
        choice_c = 'FM'
        choice_d = 'SSB'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which emission mode is best for auroral propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_906:
    def __init__(self, *args, **kwargs):
        choice_a = '800 km (500 miles)*'
        choice_b = '2400 km (1500 miles)'
        choice_c = '3200 km (2000 miles)'
        choice_d = '1600 km (1000 miles)'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Excluding enhanced propagation modes, what is the approximate range of normal VHF tropospheric propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_907:
    def __init__(self, *args, **kwargs):
        choice_a = 'Tropospheric ducting*'
        choice_b = 'Faraday rotation'
        choice_c = 'D-region absorption'
        choice_d = 'Moon bounce (EME) Earth - Moon - Earth'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What effect is responsible for propagating a VHF signal over 800 km (500 miles)?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_908:
    def __init__(self, *args, **kwargs):
        choice_a = 'Scatter-mode*'
        choice_b = 'Sky-wave with low radiation angle'
        choice_c = 'Ducting'
        choice_d = 'Ground-wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What kind of unusual HF propagation allows weak signals from the skip zone to be heard occasionally?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_909:
    def __init__(self, *args, **kwargs):
        choice_a = 'Scatter*'
        choice_b = 'Ground-wave'
        choice_c = 'Line-of-sight'
        choice_d = 'Ducting'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you receive a weak, distorted signal from a distance, and close to the maximum usable frequency, what type of propagation is probably occurring?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_910:
    def __init__(self, *args, **kwargs):
        choice_a = 'Rapid flutter or hollow sounding distortion*'
        choice_b = 'Reversed modulation'
        choice_c = 'Reversed sidebands'
        choice_d = 'High intelligibility'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is a characteristic of HF scatter signals?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_911:
    def __init__(self, *args, **kwargs):
        choice_a = 'Energy scattered into the skip zone through several radio-wave paths*'
        choice_b = 'Auroral activity and changes in the Earth\'s magnetic field'
        choice_c = 'Propagation through ground waves that absorb much of the signal'
        choice_d = 'The state of the E-region at the point of refraction'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What makes HF scatter signals often sound distorted?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_912:
    def __init__(self, *args, **kwargs):
        choice_a = 'Only a small part of the signal energy is scattered into the skip zone*'
        choice_b = 'Propagation through ground waves absorbs most of the signal energy'
        choice_c = 'The F region of the ionosphere absorbs most of the signal energy'
        choice_d = 'Auroral activity absorbs most of the signal energy'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why are HF scatter signals usually weak?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_913:
    def __init__(self, *args, **kwargs):
        choice_a = 'Scatter*'
        choice_b = 'Short-path skip'
        choice_c = 'Sporadic-E skip'
        choice_d = 'Ground wave'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of propagation may allow a weak signal to be heard at a distance too far for ground-wave propagation but too near for normal sky-wave propagation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_914:
    def __init__(self, *args, **kwargs):
        choice_a = 'When weak and distorted signals near or above the maximum usable frequency for normal propagation can be heard over unusual paths*'
        choice_b = 'When the sunspot cycle is at a minimum and D-region absorption is high'
        choice_c = 'At night'
        choice_d = 'When the F1 and F2 regions are combined'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""On the HF bands, when is scatter propagation most likely involved?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_915:
    def __init__(self, *args, **kwargs):
        choice_a = 'Absorption scatter*'
        choice_b = 'Meteor scatter'
        choice_c = 'Tropospheric scatter'
        choice_d = 'Ionospheric scatter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not a scatter mode?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_916:
    def __init__(self, *args, **kwargs):
        choice_a = '6 metres*'
        choice_b = '40 metres'
        choice_c = '15 metres'
        choice_d = '160 metres'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Meteor scatter is most effective on what band?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_917:
    def __init__(self, *args, **kwargs):
        choice_a = 'Inverted scatter*'
        choice_b = 'Side scatter'
        choice_c = 'Back scatter'
        choice_d = 'Forward scatter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Which of the following is not a scatter mode?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_918:
    def __init__(self, *args, **kwargs):
        choice_a = '30 - 100 MHz*'
        choice_b = '10 - 30 MHz'
        choice_c = '3 - 10 MHz'
        choice_d = '100 - 300 MHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In which frequency range is meteor scatter most effective for extended-range communication?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_919:
    def __init__(self, *args, **kwargs):
        choice_a = 'Interference caused by strong signals from a nearby transmitter*'
        choice_b = 'Interference caused by turning the volume up too high'
        choice_c = 'Too much current from the power supply'
        choice_d = 'Too much voltage from the power supply'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by receiver overload?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_920:
    def __init__(self, *args, **kwargs):
        choice_a = 'If the interference is about the same no matter what frequency is used for the transmitter*'
        choice_b = 'If grounding the receiver makes the problem worse'
        choice_c = 'If connecting a low pass filter to the receiver greatly cuts down the interference'
        choice_d = 'If connecting a low pass filter to the transmitter greatly cuts down the interference'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is one way to tell if radio frequency interference to a receiver is caused by front-end overload?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_921:
    def __init__(self, *args, **kwargs):
        choice_a = 'Receiver overload*'
        choice_b = 'Incorrect antenna length'
        choice_c = 'Receiver VR tube discharge'
        choice_d = 'Too little transmitter harmonic suppression'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a neighbour reports television interference whenever you transmit, no matter what band you use, what is probably the cause of the interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_922:
    def __init__(self, *args, **kwargs):
        choice_a = 'High-pass*'
        choice_b = 'Low-pass'
        choice_c = 'Band-pass'
        choice_d = 'No filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of filter should be connected to a TV receiver as the first step in trying to prevent RF overload from an amateur HF station transmission?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_923:
    def __init__(self, *args, **kwargs):
        choice_a = 'Receiver desensitization*'
        choice_b = 'Both stations are fed from the same generator'
        choice_c = 'Improper station grounding'
        choice_d = 'Harmonic radiation'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""During an outing, reception on the 20 m SSB station is compromised every time the 20 m CW station is on the air. What might cause such interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_924:
    def __init__(self, *args, **kwargs):
        choice_a = 'the undesired signal in the background of the desired signal*'
        choice_b = 'interference only when a broadcast signal is tuned'
        choice_c = 'distortion on transmitted voice peaks'
        choice_d = 'interference continuously across the dial'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Inter-modulation in a broadcast receiver by a nearby transmitter would be noticed in the receiver as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_925:
    def __init__(self, *args, **kwargs):
        choice_a = 'Receiver intermodulation interference*'
        choice_b = 'Harmonic interference from other stations'
        choice_c = 'Audio stage overload interference'
        choice_d = 'Audio stage intermodulation interference'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""You have connected your hand-held VHF transceiver to an outside gain antenna. You now hear a mixture of signals together with different modulation on your desired frequency. What is the nature of this interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_926:
    def __init__(self, *args, **kwargs):
        choice_a = 'Intermodulation interference*'
        choice_b = 'Receiver quieting'
        choice_c = 'Capture effect'
        choice_d = 'Front-end desensitization'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two or more strong out-of-band signals mix in your receiver to produce interference on a desired frequency. What is this called?
"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_927:
    def __init__(self, *args, **kwargs):
        choice_a = 'The strong signal of one mobile transmitter may desensitize the receiver of the other mobile receiver*'
        choice_b = 'Simplex operation does not require the use of CTCSS tones'
        choice_c = 'There is less time delay using simplex operation compared to using a repeater'
        choice_d = 'There are many more simplex frequencies than repeater frequencies available'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Two mobile stations are traveling along the same road in close proximity to each other and having trouble communicating through a local repeater. Why may it be necessary to use simplex operation to communicate between these cars?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_928:
    def __init__(self, *args, **kwargs):
        choice_a = 'Insert a high pass filter at the antenna connector of the television*'
        choice_b = 'Insert a low pass filter at the antenna connector of the HF transmitter'
        choice_c = 'Insert a high pass filter at the antenna connector of the HF transmitter'
        choice_d = 'Insert a low pass filter at the antenna connector of the television'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A television receiver suffers interference on channel 5 (76 - 82 MHz) only when you transmit on 14 MHz. From your home you see the tower of a commercial FM station known to broadcast on 92.5 MHz. Which of these solutions would you try first?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_929:
    def __init__(self, *args, **kwargs):
        choice_a = 'By installing a suitable filter at the receiver*'
        choice_b = 'By using a better antenna'
        choice_c = 'By increasing the receiver RF gain while decreasing the AF gain'
        choice_d = 'By adjusting the passband tuning'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can intermodulation be reduced?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_930:
    def __init__(self, *args, **kwargs):
        choice_a = 'Coils on ferrite cores*'
        choice_b = 'Bypass resistors'
        choice_c = 'Metal-oxide varistors'
        choice_d = 'Bypass inductors'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What devices would you install to reduce or eliminate audio-frequency interference to home entertainment systems?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_931:
    def __init__(self, *args, **kwargs):
        choice_a = 'Install a modular plug-in telephone RFI filter close to the telephone device*'
        choice_b = 'Ground and shield the local telephone distribution amplifier'
        choice_c = 'Stop transmitting whenever the telephone is in use'
        choice_d = 'Make internal adjustments to the telephone equipment'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should be done if a properly operating amateur station is the cause of interference to a nearby telephone?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_932:
    def __init__(self, *args, **kwargs):
        choice_a = 'Distorted speech from the transmitter\'s signals*'
        choice_b = 'Clearly audible speech from the transmitter\'s signals'
        choice_c = 'On-and-off humming or clicking'
        choice_d = 'A steady hum whenever the transmitter\'s carrier is on the air'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What sound is heard from a public-address system if audio rectification of a nearby single-sideband phone transmission occurs?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_933:
    def __init__(self, *args, **kwargs):
        choice_a = 'On-and-off humming or clicking*'
        choice_b = 'Audible, possibly distorted speech'
        choice_c = 'Muffled, severely distorted speech'
        choice_d = 'A steady whistling'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What sound is heard from a public-address system if audio rectification of a nearby CW transmission occurs?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_934:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ensure that all station equipment is properly grounded*'
        choice_b = 'Install bypass capacitors on all power supply rectifiers'
        choice_c = 'Use CW only'
        choice_d = 'Use a solid-state transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""How can you minimize the possibility of audio rectification of your transmitter's signals?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_935:
    def __init__(self, *args, **kwargs):
        choice_a = 'audio rectification in the receiver*'
        choice_b = 'harmonics interference from the transmitter'
        choice_c = 'poor image rejection'
        choice_d = 'splatter from the transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An amateur transmitter is being heard across the entire dial of a broadcast receiver. The receiver is most probably suffering from:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_936:
    def __init__(self, *args, **kwargs):
        choice_a = 'Audio rectification of strong signals*'
        choice_b = 'Harmonics generated at the transmitter'
        choice_c = 'Improper filtering in the transmitter'
        choice_d = 'Lack of receiver sensitivity and selectivity'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Your SSB HF transmissions are heard muffled on a sound system in the living room regardless of its volume setting. What causes this?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_937:
    def __init__(self, *args, **kwargs):
        choice_a = 'Ferrite core*'
        choice_b = 'Magnet'
        choice_c = 'Attenuator'
        choice_d = 'Diode'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What device can be used to minimize the effect of RF pickup by audio wires connected to stereo speakers, intercom amplifiers, telephones, etc.?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_938:
    def __init__(self, *args, **kwargs):
        choice_a = 'Shorten the leads*'
        choice_b = 'Lengthen the leads'
        choice_c = 'Connect the speaker through an audio attenuator'
        choice_d = 'Connect a diode across the speaker'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Stereo speaker leads often act as antennas to pick up RF signals. What is one method you can use to minimize this effect?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_939:
    def __init__(self, *args, **kwargs):
        choice_a = 'through a ferrite core*'
        choice_b = 'around a copper bar'
        choice_c = 'around an iron bar'
        choice_d = 'around a wooden dowel'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One method of preventing RF from entering a stereo set through the speaker leads is to wrap each of the speaker leads:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_940:
    def __init__(self, *args, **kwargs):
        choice_a = 'receiving antennas*'
        choice_b = 'transmitting antennas'
        choice_c = 'RF attenuators'
        choice_d = 'frequency discriminators'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Stereo amplifiers often have long leads which pick up transmitted signals because they act as:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_941:
    def __init__(self, *args, **kwargs):
        choice_a = 'By using a key-click filter*'
        choice_b = 'By increasing power'
        choice_c = 'By using a better power supply'
        choice_d = 'By sending CW more slowly'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f""" How can you prevent key-clicks?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_942:
    def __init__(self, *args, **kwargs):
        choice_a = 'Your hand-held is transmitting spurious emissions*'
        choice_b = 'You need a power amplifier for your hand-held'
        choice_c = 'Your hand-held has a chirp from weak batteries'
        choice_d = 'You need to turn the volume up on your hand-held'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If someone tells you that signals from your hand-held transceiver are interfering with other signals on a frequency near yours, what could be the cause?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_943:
    def __init__(self, *args, **kwargs):
        choice_a = 'Spurious emissions*'
        choice_b = 'Side tones'
        choice_c = 'Transmitter chirping'
        choice_d = 'Off-frequency emissions'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If your transmitter sends signals outside the band where it is transmitting, what is this called?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_944:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may radiate spurious emissions*'
        choice_b = 'It may transmit a weak signal'
        choice_c = 'It may interfere with other stations operating near its frequency'
        choice_d = 'It may transmit a chirpy signal'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What problem may occur if your transmitter is operated without the cover and other shielding in place?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_945:
    def __init__(self, *args, **kwargs):
        choice_a = 'the making and breaking of the circuit at the Morse key*'
        choice_b = 'frequency shifting caused by poor voltage regulation'
        choice_c = 'the power amplifier, and is caused by high frequency parasitic oscillations'
        choice_d = 'poor waveshaping caused by a poor voltage regulator'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In Morse code transmission, local RF interference (key-clicks) is produced by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_946:
    def __init__(self, *args, **kwargs):
        choice_a = 'too sharp rise and decay times of the keyed carrier*'
        choice_b = 'power supply hum modulating the carrier'
        choice_c = 'sparks emitting RF from the key contacts'
        choice_d = 'changes in oscillator frequency on keying'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Key-clicks, heard from a Morse code transmitter at a distant receiver, are the result of:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_947:
    def __init__(self, *args, **kwargs):
        choice_a = 'poor shaping of the waveform*'
        choice_b = 'shift in frequency when keying the transmitter'
        choice_c = 'sparking at the key contacts'
        choice_d = 'sudden movement in the receiver loudspeaker'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a Morse code transmission, broad bandwidth RF interference (key-clicks) heard at a distance is produced by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_948:
    def __init__(self, *args, **kwargs):
        choice_a = 'Check the keying filter and the functioning of later stages*'
        choice_b = 'Turn the receiver down'
        choice_c = 'Regulate the oscillator supply voltage'
        choice_d = 'Use a choke in the RF power output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should you do if you learn your transmitter is producing key clicks?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_949:
    def __init__(self, *args, **kwargs):
        choice_a = 'is an unwanted signal developed in a transmitter*'
        choice_b = 'is generated by parasitic elements of a Yagi beam'
        choice_c = 'does not cause any radio interference'
        choice_d = 'is produced in a transmitter oscillator stage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A parasitic oscillation:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_950:
    def __init__(self, *args, **kwargs):
        choice_a = 'at high or low frequencies*'
        choice_b = 'on harmonic frequencies'
        choice_c = 'at high frequencies only'
        choice_d = 'at low frequencies only'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Parasitic oscillations in the RF power amplifier stage of a transmitter may be found:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_951:
    def __init__(self, *args, **kwargs):
        choice_a = 'above or below the transmitter frequency*'
        choice_b = 'on VHF frequencies only'
        choice_c = 'on the transmitter fundamental frequency'
        choice_d = 'on harmonics of the transmitter frequency'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Transmitter RF amplifiers can generate parasitic oscillations:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_952:
    def __init__(self, *args, **kwargs):
        choice_a = 'Harmonic radiation from your transmitter*'
        choice_b = 'De ionization of the ionosphere near your neighbour\'s TV antenna'
        choice_c = 'TV receiver front-end overload'
        choice_d = 'Too much low pass filtering on the transmitter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If a neighbour reports television interference on one or two channels only when you transmit on 15 metres, what is probably the cause of the interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_953:
    def __init__(self, *args, **kwargs):
        choice_a = 'Unwanted signals at frequencies which are multiples of the fundamental (chosen) frequency*'
        choice_b = 'Unwanted signals that are combined with a 60-Hz hum'
        choice_c = 'Unwanted signals caused by sympathetic vibrations from a nearby transmitter'
        choice_d = 'Signals which cause skip propagation to occur'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What is meant by harmonic radiation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_954:
    def __init__(self, *args, **kwargs):
        choice_a = 'It may cause interference to other stations and may result in out-of-band signals*'
        choice_b = 'It uses large amounts of electric power'
        choice_c = 'It may cause sympathetic vibrations in nearby transmitters'
        choice_d = 'It may cause auroras in the air'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why is harmonic radiation from an amateur station not wanted?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_955:
    def __init__(self, *args, **kwargs):
        choice_a = 'Harmonic radiation*'
        choice_b = 'Parasitic excitation'
        choice_c = 'Intermodulation'
        choice_d = 'Auroral distortion'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of interference may come from a multi-band antenna connected to a poorly tuned transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_956:
    def __init__(self, *args, **kwargs):
        choice_a = 'Your transmitter was radiating harmonic signals*'
        choice_b = 'Your transmitter\'s power-supply filter choke was bad'
        choice_c = 'You were sending CW too fast'
        choice_d = 'Your transmitter\'s power-supply filter capacitor was bad'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""If you are told your station was heard on 21 375 kHz, but at the time you were operating on 7125 kHz, what is one reason this could happen?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_957:
    def __init__(self, *args, **kwargs):
        choice_a = 'Overmodulating a transmitter*'
        choice_b = 'Keying a transmitter too fast'
        choice_c = 'Signals from a transmitter\'s output circuit are being sent back to its input circuit'
        choice_d = 'The transmitting antenna is the wrong length'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What causes splatter interference?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_958:
    def __init__(self, *args, **kwargs):
        choice_a = 'harmonic radiation from the transmitter*'
        choice_b = 'no high-pass filter on the TV'
        choice_c = 'a bad ground at the transmitter'
        choice_d = 'front-end overload of the TV'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Your amateur radio transmitter appears to be creating interference to the television on channel 3 (60-66 MHz) when you are transmitting on the 15 metre band. Other channels are not affected. The most likely cause is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_959:
    def __init__(self, *args, **kwargs):
        choice_a = 'reduce microphone gain*'
        choice_b = 'retune transmitter output'
        choice_c = 'use another antenna'
        choice_d = 'reduce oscillator output'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""One possible cause of TV interference by harmonics from an SSB transmitter is from "flat topping" - driving the power amplifier into non-linear operation. The most appropriate remedy for this is:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_960:
    def __init__(self, *args, **kwargs):
        choice_a = 'overdriven stages*'
        choice_b = 'low SWR'
        choice_c = 'resonant circuits'
        choice_d = 'a linear amplifier'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In a transmitter, excessive harmonics are produced by:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_961:
    def __init__(self, *args, **kwargs):
        choice_a = 'second harmonic of a 10 metre transmission*'
        choice_b = 'crystal oscillator operating on its fundamental'
        choice_c = 'seventh harmonic of an 80 metre transmission'
        choice_d = 'third harmonic of a 15 metre transmission'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""An interfering signal from a transmitter is found to have a frequency of 57 MHz (TV Channel 2 is 54 - 60 MHz). This signal could be the:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_962:
    def __init__(self, *args, **kwargs):
        choice_a = 'excessive drive signal is applied to it*'
        choice_b = 'the output tank circuit is tuned to the fundamental frequency'
        choice_c = 'the oscillator frequency is unstable'
        choice_d = 'modulation is applied to a high-level stage'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Harmonics may be produced in the RF power amplifier of a transmitter if:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_963:
    def __init__(self, *args, **kwargs):
        choice_a = 'A low pass filter*'
        choice_b = 'A key-click filter'
        choice_c = 'A high pass filter'
        choice_d = 'A CW filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What type of filter might be connected to an amateur HF transmitter to cut down on harmonic radiation?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_964:
    def __init__(self, *args, **kwargs):
        choice_a = 'To reduce harmonic radiation*'
        choice_b = 'To reduce fundamental radiation'
        choice_c = 'To reduce low frequency interference to other amateurs'
        choice_d = 'To reduce RF energy below a cut-off point'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""Why do modern HF transmitters have a built-in low pass filter in their RF output circuits?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_965:
    def __init__(self, *args, **kwargs):
        choice_a = 'A band pass filter*'
        choice_b = 'A high pass filter'
        choice_c = 'An input filter'
        choice_d = 'A low pass filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What circuit blocks RF energy above and below a certain limit?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_966:
    def __init__(self, *args, **kwargs):
        choice_a = 'About the same*'
        choice_b = 'Substantially lower'
        choice_c = 'Twice the transmission line impedance'
        choice_d = 'Substantially higher'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""What should be the impedance of a low pass filter as compared to the impedance of the transmission line into which it is inserted?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_967:
    def __init__(self, *args, **kwargs):
        choice_a = 'Low pass*'
        choice_b = 'Key click'
        choice_c = 'High pass'
        choice_d = 'Rejection'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""In order to reduce the harmonic output of a high frequency (HF) transmitter, which of the following filters should be installed at the transmitter?"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_968:
    def __init__(self, *args, **kwargs):
        choice_a = 'low pass filter*'
        choice_b = 'high pass filter'
        choice_c = 'band reject filter'
        choice_d = 'wave trap'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To reduce harmonic output from a high frequency transmitter, you would put a ____________ in the transmission line as close to the transmitter as possible."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_969:
    def __init__(self, *args, **kwargs):
        choice_a = 'high pass filter*'
        choice_b = 'low pass filter'
        choice_c = 'wave trap'
        choice_d = 'band reject filter'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""To reduce energy from an HF transmitter getting into a television set, you would place a ____________ as close to the TV as possible."""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_970:
    def __init__(self, *args, **kwargs):
        choice_a = 'allow only certain frequencies through*'
        choice_b = 'attenuate high frequencies but not low'
        choice_c = 'pass frequencies each side of a band'
        choice_d = 'stop frequencies in a certain band'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A band pass filter will:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_971:
    def __init__(self, *args, **kwargs):
        choice_a = 'pass frequencies each side of a band*'
        choice_b = 'allow only two frequencies through'
        choice_c = 'pass frequencies below 100 MHz'
        choice_d = 'stop frequencies each side of a band'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A band reject filter will:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_972:
    def __init__(self, *args, **kwargs):
        choice_a = 'at the antenna terminals of the TV receiver*'
        choice_b = 'between microphone and speech amplifier'
        choice_c = 'at the Morse key or keying relay in a transmitter'
        choice_d = 'between transmitter output and transmission line'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A high pass filter would normally be fitted:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class f_2_973:
    def __init__(self, *args, **kwargs):
        choice_a = 'attenuate frequencies above 30 MHz*'
        choice_b = 'pass audio frequencies above 3 kHz'
        choice_c = 'attenuate frequencies below 30 MHz'
        choice_d = 'pass audio frequencies below 3 kHz'

        choices = [choice_a, choice_b, choice_c, choice_d]
        random.shuffle(choices)

        self.question = f"""A low pass filter suitable for a high frequency transmitter would:"""
        self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""