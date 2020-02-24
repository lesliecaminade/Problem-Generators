from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from num2words import num2words

x, y, z, t = sym.symbols('x y z t', real = True)

class jma_14_1:
	def __init__(self, *args, **kwargs):
		
		sampling_rate = round(random.uniform(10,80),2)
		max_input_freq = round(sampling_rate/2,2)
		self.question = """For a sample rate of {a:g} kHz in a PCM system, determine the maximum analog input frequency.""".format(a=sampling_rate)
		self.answer = """{a:g} kHz""".format(a = round(max_input_freq,2))
		
class jma_14_2:
	def __init__(self, *args, **kwargs):
		
		bits_with_sign = random.randint(5,20)
		bith_without_sign = bits_with_sign - 1
		dynamic_range_dB = 20*math.log(2**bith_without_sign - 1,10)
		max_decode_voltage = round(random.uniform(1.0,5.0),2)
		self.question = """What is the dynamic range in dB of an {a:g}-bit linear sign-magnitude PCM spectrum whose maximum decode voltage at the receiver is {b:g} V peak?""".format(a=bits_with_sign,b=max_decode_voltage)
		self.answer = """{a:g} dB""".format(a=round(dynamic_range_dB,2))
		
class jma_14_3:
	def __init__(self, *args, **kwargs):
		
		bits_with_sign = random.randint(5,9)
		bits_without_sign = bits_with_sign - 1
		v_max = random.uniform(1.0,9.0)
		resolution = v_max/sym.Pow(2,bits_without_sign)
		self.question = """Determine the resolution for an {a:g}-bit linear sign-magnitude PCM for a maximum decode voltage of {b:g} V peak.""".format(a=bits_with_sign,b=v_max)
		self.answer = """{a:g} V""".format(a=round(resolution,2))
		
class jma_14_4:
	def __init__(self, *args, **kwargs):
		
		levels = random.sample([8,16,32,64,128,256,512,1024,2048],1)[0]
		scale_factor = 100/ levels
		v_max = random.randint(2,6)
		resolution = v_max/levels
		bandwidth = round(random.uniform(2,6),1)
		sampling_rate = random.randint(5,9)
		
		self.question = """An audio signal with a bandwidth of {a:g} kHz and is converted to PCM signal by sampling at {b:g} kilosamples per second by using a uniform quantizer with scale factor of {c:g}% and a V_max of {d:g} V. Determine the number of levels and the resolution of this quantizer.""".format(a=bandwidth,b=sampling_rate,c=scale_factor,d=v_max)
		
		self.answer = """{a:g} levels, {b:g} V""".format(a=levels,b=resolution)
		
class jma_14_5:
	def __init__(self, *args, **kwargs):
		
		number_of_bits = random.randint(5,10)
		sampling_rate_khz = random.randint(8,16)
		sampling_rate = sampling_rate_khz * 1000
		bitrate = sampling_rate * number_of_bits
		bitrate_kbps = bitrate /1000
		signal_to_noise_ratio_db = 6.02*number_of_bits + 1.76
		bandwidth_khz = round(random.uniform(2,4),2)
		
		
		self.question = """Determine the signal-to-noise ratio in dB, if an audio signal with a bandwidth of {a:g} kHz is converted to PCM signal by sampling at {b:g} kilosamples per second and with a data rate of {c:g} kbps""".format(a=bandwidth_khz,b=sampling_rate_khz,c=bitrate_kbps)
		
		self.answer = """{a:g} dB""".format(a=round(signal_to_noise_ratio_db,2))
		
class jma_14_6:
	def __init__(self, *args, **kwargs):
		
		levels_temp = random.sample([16,32,64,128],1)
		levels = levels_temp[0]
		passband_temp = random.sample([3200,3400,3600,3800,4000],1)
		passband = passband_temp[0]
		probability_of_error_exponent = random.randint(-9,-5)
		probability_of_error = 10**probability_of_error_exponent
		sampling_rate_khz = random.randint(8,16)
		sampling_rate = sampling_rate_khz*1000
		snr = (3*levels**2)/(1+4*probability_of_error*(levels**2+1))
		snr_db = 10*math.log(snr,10)
		snr_db_approx = 6.02*(math.log(levels)/math.log(2)) + 4.76
		
		self.question = """An audio signal with a passband of {a:g} Hz is converted to PCM signal by sampling at {b:g} kilosamples/sec and by using a uniform quantizer with {c:g} steps. Determine the peak SQNR if the probability of error is 10^{d:g}""".format(a=passband,b=sampling_rate_khz,c=levels,d=probability_of_error_exponent)
		
		self.answer = """{a:g} dB, or {b:g} dB approx""".format(a=round(snr_db,2),b=round(snr_db_approx,2))
		
class jma_14_7:
	def __init__(self, *args, **kwargs):
		
		levels_temp = random.sample([16,32,64,128],1)
		levels = levels_temp[0]
		passband_temp = random.sample([3200,3400,3600,3800,4000],1)
		passband = passband_temp[0]
		probability_of_error_exponent = random.randint(-9,-5)
		probability_of_error = 10**probability_of_error_exponent
		sampling_rate_khz = random.randint(8,16)
		sampling_rate = sampling_rate_khz*1000
		snr = (levels**2)/(1+4*probability_of_error*(levels**2+1))
		snr_db = 10*math.log(snr,10)
		snr_db_approx = 6.02*(math.log(levels)/math.log(2))
		
		self.question = """An audio signal with a passband of {a:g} Hz is converted to PCM signal by sampling at {b:g} kilosamples/sec and by using a uniform quantizer with {c:g} steps. Determine the average SQNR if the probability of error is 10^{d:g}""".format(a=passband,b=sampling_rate_khz,c=levels,d=probability_of_error_exponent)
		
		self.answer = """{a:g} dB, or {b:g} dB approx""".format(a=round(snr_db,2),b=round(snr_db_approx,2)) 
		
class jma_14_8:
	def __init__(self, *args, **kwargs):
		
		temp = random.randint(0,4)
		one_third = 1/3
		input_signal_fraction_temp = [0.5,one_third,0.25,0.2,0.75]
		input_signal_fraction = input_signal_fraction_temp[temp]
		input_signal_fraction_string = ['one-half','one-third','one-fourth','one-fifth','three-fourth']
		
		vo_fraction = math.log(1+255*input_signal_fraction)/math.log(1+255)
		
		self.question = """What proportion of the maximum output voltage is produced if a positive input signal is applied to a mu-Law compressor with its voltage {a:s} the maximum value?""".format(a=input_signal_fraction_string[temp])
		
		self.answer = """{a:g} Vo_max""".format(a=round(vo_fraction,2))


class jma_15_1():
	def __init__(self):

		probability_number_keys = c.percentage(random.randint(90, 99), 'percent')
		probabiity_other_keys = c.percentage(1 - probability_number_keys.decimal, 'decimal')

		probabability_num_key = c.percentage(probability_number_keys.decimal / 10, 'decimal')
		probability_other_key = c.percentage(probabiity_other_keys.decimal / 2, 'decimal')

		keypress_rate = random.randint(1,3) #per second

		information_measure_number = c.bitrate(math.log(1/probabability_num_key.decimal, 2))

		information_measure_other = c.bitrate(math.log(1/probability_other_key.decimal, 2))

		entropy = probability_number_keys.decimal * information_measure_number.bps + 2 * probabiity_other_keys.decimal * information_measure_other.bps #bits per key

		data_rate = c.bitrate(entropy * keypress_rate)

		answers = {'entropy':str(round(entropy, 2)) + ' bits/key', 'data rate':str(round(data_rate.bps, 2)) + ' bps'}
		pick = random.choice(list(answers.keys()))

		self.question = f"""A telephone touch-tone keypad has the digits 0 to 9, plus the asterisk and the octothorpe keys. Assume the probability of sending the asterisk and the octothorpe is {probability_other_key.percent:5.4} % and the probability of sending 0 to 9 is {probabability_num_key.percent:5.4} % each. If the keys are pressed at a rate of {keypress_rate} keys per second, compute the {pick} for this source."""
		self.answer = f"""{answers[pick]}"""


class jma_15_2():
	def __init__(self):


		bitrate = c.bitrate(ran.main(10), 'kbps')

		self.question = f"""A binary signal is to be transmitted at {bitrate.kbps:5.4} kbps. What is the absolute minimum bandwidth that is required to pass the fastest information change undistorted?"""

		bandwidth = c.frequency(bitrate.bps / 2)

		self.answer = f"""{bandwidth.kHz:5.4} kHz"""

class jma_15_3():
	def __init__(self):

		bitrate = c.bitrate(ran.main(20), 'kbps') 
		snr = ran.main(200)

		bandwidth = c.frequency(bitrate.bps / math.log(1 + snr,2))

		information_density = bitrate.bps / bandwidth.Hz

		answers = {'bandwidth':str(round(bandwidth.Hz, 2)) + ' Hz', 'information density':str(round(information_density,2)) + ' bps/Hz'}

		pick = random.choice(list(answers.keys()))

		self.question = f"""What is the {pick} of a system with an input bitrate of {bitrate.bps:5.4} bps, when the ratio of signal to noise is {snr:5.4}?"""
		self.answer = f"""{answers[pick]}"""

class jma_15_4():
	def __init__(self):

		signal_power = c.power(ran.main(200))
		noise_power = c.power(ran.main(10))
		bandwidth = c.frequency(ran.main(2000))

		capacity = c.bitrate( bandwidth.Hz * math.log(1 + signal_power.W / noise_power.W,2))

		spectral_efficiency = capacity.bps / bandwidth.Hz

		answers = {'channel capacity':str(round(capacity.kbps, 2)) + ' kbps', 'spectral efficiency':str(round(spectral_efficiency,2)) + ' bps/Hz'}

		pick = random.choice(list(answers.keys()))

		self.question = f"""What is the {pick} for a signal power of {signal_power.W:5.4} W, noise power of {noise_power.W:5.4} W and a bandwidth of {bandwidth.kHz:5.4} kHz of a digital system?"""

		self.answer = f"""{answers[pick]}"""

class jma_15_5():
	def __init__(self):

		data_elements = random.randint(1,5)
		bitrate = c.bitrate(ran.main(100), 'kbps')

		self.question = f"""A signal is carrying data in which {num2words(data_elements)} data element(s) is(are) encoded as one signal element. If the bitrate is {bitrate.kbps:5.4} kbps, what is the average value of the baud rate?"""

		baudrate = c.baudrate(bitrate.bps / data_elements)

		self.answer = f"""{baudrate.kbaud:5.4} kbaud"""

class jma_15_6():
	def __init__(self):

		bitrate = c.bitrate(ran.main(270.833), 'kbps')

		self.question = f"""Calculate the frequency shift (deviation) between mark and space for GSM cellular radio system that uses Gaussian MSK (GMSK) with a transmission rate of {bitrate.kbps:5.4} kbps."""

		deviation = c.frequency(bitrate.bps / 2)

		self.answer= f"""{deviation.kHz:5.4} kHz"""

class jma_15_7():
	def __init__(self):
		carrier_freq = c.frequency(ran.main(70), 'MHz')
		input_bitrate = c.bitrate(ran.main(10), 'Mbps')

		psk_types = {'BPSK':1, 'QPSK':2, '8-PSK':3, '16-PSK':4, '32-PSK':5, '8-QAM':3, '16-QAM':4, '32-QAM':5}
		psk_type = random.choice(list(psk_types.keys()))
		
		bandwidth = c.frequency(input_bitrate.bps/ psk_types[psk_type])
		baudrate = c.baudrate(input_bitrate.bps / psk_types[psk_type])

		answers = {'minimum nyquist bandwidth':str(round(bandwidth.MHz, 2)) + ' MHz', 'baud rate':str(round(baudrate.Mbaud,2)) + ' Mbaud', 'bandwidth efficiency':str(psk_types[psk_type]) + ' bps/Hz'}

		pick = random.choice(list(answers.keys()))

		self.question = f"""Determine the {pick} for a {psk_type} modulator with a carrier frequency of {carrier_freq.MHz:5.4} MHz and an input bitrate of {input_bitrate.Mbps:5.4} Mbps"""
		self.answer = f"""{answers[pick]}"""

class jma_15_8():
	def __init__(self):

		bits = random.randint(1,10)
		levels = 2**bits

		self.question = f"""How many bits are needed to address {levels} different level combinations?"""
		self.answer = f"""{bits} bits"""

class jma_15_9():
	def __init__(self):

		carrier_power = c.power(ran.main(10**-13), 'W')
		bitrate = c.bitrate(ran.main(30), 'kbps')
		bandwidth = c.frequency(ran.main(60), 'kHz')
		noise_power = c.power(ran.main(10**-14), 'W')

		energy_per_bit = c.power(carrier_power.W / bitrate.bps)
		noise_density = c.power(noise_power.W / bandwidth.Hz)

		probability = 0.5 * math.exp( - energy_per_bit.W / noise_density.W )

		self.question = f"""Calculate the probability of error a non-coherent FSK system if the carrier power is {carrier_power.W:5.4} W, bit rate of {bitrate.kbps:5.4} kbps, bandwidth of {bandwidth.kHz:5.4} kHz and noise power of {noise_power.W:5.4} W."""

		self.answer = f"""{probability:5.4}"""











		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		