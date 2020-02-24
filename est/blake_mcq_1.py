import random


class chapter_7_1():
	def __init__(self):
		
		choice_a = 'ASCII'
		choice_b = 'Baudot code'
		choice_c = 'Morse code #'
		choice_d = 'none of the above'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The first digital code was the """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_2():
	def __init__(self):
		
		choice_a = 'an amplifier'
		choice_b = 'a filter'
		choice_c = 'a regenerative amplifier #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In a digital transmission, signal degradation can be removed using"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_3():
	def __init__(self):
		
		choice_a = 'Time - Division multiplexing #'
		choice_b = 'Time - Domain multiplexing'
		choice_c = 'Ten - Digital Manchester'
		choice_d = 'Ten Dual - Manchester'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""TDM stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_4():
	def __init__(self):
		
		choice_a = 'I = ktB #'
		choice_b = 'C = 2B log_2 M'
		choice_c = 'C = B log_2 (1 + S/N )'
		choice_d = 'SR = 2 fmax'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Hartley's Law is """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_5():
	def __init__(self):
		
		choice_a = 'I = ktB'
		choice_b = 'C = 2Blog_2(M) #'
		choice_c = 'C = Blog_2(1 + S/N)'
		choice_d = 'SR = 2 fmax'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The Shannon-Hartley theorem is :"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_6():
	def __init__(self):
		
		choice_a = 'I = ktB'
		choice_b = 'C = 2Blog_2(M)'
		choice_c = 'C = Blog_2(1 + S/N) #'
		choice_d = 'SR = 2 fmax'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The Shannon Limit is given by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_7():
	def __init__(self):
		
		choice_a = 'I = ktB'
		choice_b = 'C = 2Blog_2(M)'
		choice_c = 'C = Blog_2(1 + S/N)'
		choice_d = 'SR = 2 fmax #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The Nyquist rate can be expressed as:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_8():
	def __init__(self):
		
		choice_a = 'a sample-and-hold circuit #'
		choice_b = 'true binary numbers'
		choice_c = 'a fixed sample rate'
		choice_d = 'an analog-to-digital converter'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Natural sampling does not use"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_9():
	def __init__(self):
		
		choice_a = 'They are two types of sampling error'
		choice_b = 'You can ahve one or the other,  but not both'
		choice_c = 'Aliasing is a technique to prevent foldover distortion'
		choice_d = 'They are the same thing #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""What is true about aliasing and foldover distortion?"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_10():
	def __init__(self):
		
		choice_a = 'noise'
		choice_b = 'too many samples per second'
		choice_c = 'too few samples per second #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Folover distortion is caused by """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_11():
	def __init__(self):
		
		choice_a = 'a sample alias'
		choice_b = 'PAM #'
		choice_c = 'PCM'
		choice_d = 'PDM'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The immediate result of sampling is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_12():
	def __init__(self):
		
		choice_a = 'PDM'
		choice_b = 'PWM'
		choice_c = 'PPM'
		choice_d = 'PPS #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Which of these is not a pulse-modulation technique"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_13():
	def __init__(self):
		
		choice_a = 'decreases as the sample rate increases'
		choice_b = 'decreases as the sample rate decreases'
		choice_c = 'decreases as the bits per sample increases #'
		choice_d = 'decreases as the bits per sample decreases'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Quantizing noise (quantization noise)"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_14():
	def __init__(self):
		
		choice_a = 'the strong transmittable signal to the weakest discernable signal #'
		choice_b = 'the maximum rate of conversion to the minimum rate of conversion'
		choice_c = 'the maximum bits per sample to the minimum bits per sample'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The dynamic range of a system is the ratio of"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_15():
	def __init__(self):
		
		choice_a = 'compress the range of base-band frequencies'
		choice_b = 'reduce dynamic range at higher bit-rates'
		choice_c = 'preserve dynamic range while keeping bit-rate low #'
		choice_d = 'maximize the useable bandwidth in digital transmission'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Companding is used to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_16():
	def __init__(self):
		
		choice_a = 'the Logarithmic Law'
		choice_b = 'the A Law'
		choice_c = 'the alpha law '
		choice_d = 'the mu law #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In North America, companding uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_17():
	def __init__(self):
		
		choice_a = 'the Logarithmic Law'
		choice_b = 'the A Law #'
		choice_c = 'the alpha law'
		choice_d = 'the mu law'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In Europe, companding uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_18():
	def __init__(self):
		
		choice_a = 'Coder - Decoder #'
		choice_b = 'Coded - Carrier'
		choice_c = 'Code - Compression'
		choice_d = 'none of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Codec stands for"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_19():
	def __init__(self):
		
		choice_a = '4 - bit numbers'
		choice_b = '8 - bit numbers #'
		choice_c = '12 - bit numbers'
		choice_d = '16 - bit numbers'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A typical codec in a telephone system sends and receives"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_20():
	def __init__(self):
		
		choice_a = 'transmits fewer bits per sample'
		choice_b = 'requires a much higher sampling rate'
		choice_c = 'can suffer slope overload'
		choice_d = 'all of the above #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Compared to PCM, delta modulation"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_21():
	def __init__(self):
		
		choice_a = 'the signal changes too rapidly'
		choice_b = 'the signal does not change #'
		choice_c = 'the bit rate is too high'
		choice_d = 'the sample is too large'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In delta modulation, "granular noise" is produced when"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_22():
	def __init__(self):
		
		choice_a = 'with a lower bit rate but reduced quality'
		choice_b = 'with a lower bit rate but the same quality #'
		choice_c = 'only over shorter distances'
		choice_d = 'only if the voice is band-limited'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Compared to PCM, adaptive delta modulation can transmit voice:"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_23():
	def __init__(self):
		
		choice_a = 'AMI'
		choice_b = 'Manchester'
		choice_c = 'unipolar NRZ #'
		choice_d = 'bipolar RZ'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Which coding scheme requires DC continuity"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_24():
	def __init__(self):
		
		choice_a = 'is a biphase code'
		choice_b = 'has a level transition in the middle of every bit period'
		choice_c = 'provides string timing information'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Manchester coding"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_25():
	def __init__(self):
		
		choice_a = '1 #'
		choice_b = '2'
		choice_c = '4'
		choice_d = '8'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of framing bits in DS - 1 is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_26():
	def __init__(self):
		
		choice_a = 'detect errors'
		choice_b = 'carry signaling'
		choice_c = 'synchronize the transmitter and receiver #'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Framing bits in DS - 1 are used to"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_27():
	def __init__(self):
		
		choice_a = 'detect errors'
		choice_b = 'carry signaling #'
		choice_c = 'synchronize the transmitter and receiver'
		choice_d = 'all of the choices'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""So-called "stolen" bits in DS - 1 are used to """
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_28():
	def __init__(self):
		
		choice_a = '1'
		choice_b = '2'
		choice_c = '4'
		choice_d = '8 #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of bits per sample in DS - 1 is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_29():
	def __init__(self):
		
		choice_a = '8k #'
		choice_b = '56k '
		choice_c = '64k'
		choice_d = '1.544 x 10^6'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of samples per second is DS - 1 is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_30():
	def __init__(self):
		
		choice_a = '8k #'
		choice_b = '56k'
		choice_c = '64k'
		choice_d = '1.544 x 10^6'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The bitrate for each channel in DS - 1"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_31():
	def __init__(self):
		
		choice_a = '1.544 Mbps #'
		choice_b = '64 kbps '
		choice_c = '56 kbps'
		choice_d = '8 kbps'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""In DS -1, bites are transmitter over a T - 1 cable at"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_32():
	def __init__(self):
		
		choice_a = 'Manchester coding'
		choice_b = 'bipolar RZ AMI coding #'
		choice_c = 'NRZ coding'
		choice_d = 'pulse-width coding'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A T-1 cable uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_33():
	def __init__(self):
		
		choice_a = '6'
		choice_b = '12 #'
		choice_c = '24'
		choice_d = '48'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""The number of frames in a superframe is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_34():
	def __init__(self):
		
		choice_a = 'twisted - pair wire #'
		choice_b = 'coaxial cable'
		choice_c = 'fiber-optic cable'
		choice_d = 'microwave'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A typical T - 1 line uses"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_35():
	def __init__(self):
		
		choice_a = 'on-hook / off-hook condition'
		choice_b = 'busy signal'
		choice_c = 'ringing'
		choice_d = 'all of the choices #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Signaling is used to indicate"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""

class chapter_7_36():
	def __init__(self):
		
		choice_a = 'constructing a model of the transmission medium'
		choice_b = 'constructing a model of the human vocal system #'
		choice_c = 'find redundancies in the digitized data'
		choice_d = 'using lossless techniques'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""A vocoder implements compression by"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""


class chapter_7_37():
	def __init__(self):
		
		choice_a = 'much better'
		choice_b = 'somewhat better'
		choice_c = 'about the same'
		choice_d = 'not as good #'
		
		choices = [choice_a, choice_b, choice_c, choice_d]
		random.shuffle(choices)
		
		
		self.question = f"""Compared to standard PCM systems, the quality of the output of a vocoder is"""
		self.answer = f"""A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}"""




