import random_handler as ran
import numpy_handler as num
import sympy as sym
# from sympy import init_printing
import math
import random
# import algebra
# import analytic_geometry
import constants_conversions as c
# import randomizer_2 as ran2

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables

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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        