import randomizer
import math
import random
import sympy as sp
import stringHandling

from common_names import *
#from sympy import *


#symbols for sympy
a, b, c, d, x, y, z = sp.symbols('a b c d x y z', real = True)
n = sp.symbols('n', real = True)


title_string = """Digital Modulation EST Superbook by JMA
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""

class digitalModulationClass:

    def __init__(self):
        form = random.randint(1,16) #check
        if form == 1:
            probability_0_to_9 = round(random.uniform(0.05,0.09),3)
            all_from_0_to_9 = probability_0_to_9*10
            probability_asterisk_and_number_sign = (1 - all_from_0_to_9)/2
            info_measure_0_to_9_each = math.log(1/probability_0_to_9,2)
            info_measure_asterisk_and_number_sign_each = math.log(1/probability_asterisk_and_number_sign,2)
            
            rate_of_keypress = random.randint(1,3)
            
            
            average_info_or_entropy = 10*(probability_0_to_9*info_measure_0_to_9_each) + 2*(probability_asterisk_and_number_sign*info_measure_asterisk_and_number_sign_each)
            
            bitrate = average_info_or_entropy*rate_of_keypress
            
            question = """A telephone touch-tone keypad has the digits 0 to 9, plus the * and # keys. Assume the probability of sending * and # is {a:g} and the probability of sending 0 to 9 is {b:g} each. If the keys are pressed at a rate of {c:g} keys/s, compute the entropy and the data rate for this source.""".format(
            a=probability_asterisk_and_number_sign,
            b=probability_0_to_9,
            c=rate_of_keypress)
            
            soln = """Entropy: {a:g} bits/key, Bitrate: {b:g} bps""".format(
            a = round(average_info_or_entropy,2),
            b = round(bitrate,2))
        
        if form == 2:
            time_to_transmits = []

            probabilities = random.sample([0.21,0.14,0.09,0.11,0.15,0.18,0.12],7)
            
            for i in range(0,7):
                time_to_transmits.append(random.sample([10,15,20,25,30],1)[0])
              
            entropy = 0
            
            for i in range(0,7):
                entropy = entropy + probabilities[i]*math.log(1/probabilities[i],2)
            
            max_entropy = math.log(7,2)
            relative_entropy = entropy/max_entropy
            
            time_of_information = 0
            for i in range(0,7):
                time_of_information = time_of_information + probabilities[i]*time_to_transmits[i]
            
            bitrate = entropy/time_of_information
           
            question = """From the given table:
Symbol          Probability         Time to transmit
x1              {a:g}               {h:g}
x2              {b:g}               {i:g}
x3              {c:g}               {j:g}
x4              {d:g}               {k:g}
x5              {e:g}               {l:g}
x6              {f:g}               {m:g}
x7              {g:g}               {n:g}
Determine the entropy, relative entropy, and the rate of information.
""".format(
            a = probabilities[0],
            b = probabilities[1],
            c = probabilities[2],
            d = probabilities[3],
            e = probabilities[4],
            f = probabilities[5],
            g = probabilities[6],
            h = time_to_transmits[0],
            i = time_to_transmits[1],
            j = time_to_transmits[2],
            k = time_to_transmits[3],
            l = time_to_transmits[4],
            m = time_to_transmits[5],
            n = time_to_transmits[6])
            
            soln = """Entropy: {a:g} bits/symbol, Relative Entropy: {b:g}, Rate of Information: {c:g} bps""".format(
            a = round(entropy,2),
            b = round(relative_entropy,2),
            c = round(bitrate,2))
            
      
            
        if form == 3:
            question = """Calculate the coding efficiency in representing the 26 letters of the alphabet using a binary and a decimal system."""
            
            soln = """Binary: 94%, Decimal: 71%"""
            
        if form == 4:
            bitrate_kbps = random.sample([10,15,20,25,30,35,40,45,50],1)[0]
            bitrate = bitrate_kbps*1000
            bandwidth = bitrate/2
            bandwidth_khz = bandwidth/1000
            question = """A binary digital signal is to be transmitted at {a:g} kbps, what is the absolute minimum bandwidth required to pass the fastest information change.""".format(a = bitrate_kbps)
            
            soln = """Bandwidth is {a:g} kHz""".format(a = round(bandwidth_khz,2))
            
        if form == 5:
            bitrate_kbps = random.sample([10,15,20,25,30,35,40,45,50,55,60],1)[0]
            bitrate = bitrate_kbps*1000
            signal_to_noise_ratio = random.sample([100,150,200,250,300,350,500,750,1000],1)[0]
            bandwidth = bitrate/math.log(1+signal_to_noise_ratio,2)
            information_density = bitrate/bandwidth
            
            question = """What is the bandwidth needed to support a capacity of {a:g},000 bits/s (using Shannon's Theory), when the ratio of the power to noise is {b:g}? Also compute the information density.""".format(a=bitrate_kbps,b=signal_to_noise_ratio)
            
            soln = """Bandwidth: {a:g} Hz, Information Density: {b:g} bps/Hz""".format(a = round(bandwidth,2),b=round(information_density,2))
       
        if form == 6:
            signal_power = random.randint(1,9)*100
            noise_power = random.randint(1,9)*10
            bandwidth = random.randint(1,9)*1000
            channel_capacity = bandwidth*math.log(1 + signal_power/noise_power,2)
            efficiency = math.log(1+signal_power/noise_power,2)
            
            question = """What is the channel capacity for a signal power of {a:g}00 W, noise power of {b:g}0 W, and a bandwidth of {c:g} kHz of a digital system? Also calculate the spectrum efficiency.""".format(
            a = signal_power/100,
            b = noise_power/10,
            c = bandwidth/1000)
            
            soln = """Channel Capacity: {a:g} kbps, Spectrum Efficiency: {b:g} bps/Hz""".format(
            a = round(channel_capacity/1000,2),
            b = round(efficiency,2))
        
        if form == 7:
            sampling_multiplier = random.sample([1.10,1.25,1.30,1.50,1.75,2.0],1)[0]
            levels = random.sample([256,512,1024,2048],1)[0]
            bandwidth = random.randint(10,15)*1000
            signal_to_noise_ratio_dB = random.randint(10,20)
            signal_to_noise_ratio = round(10**(signal_to_noise_ratio_dB/10),2)
            entropy = math.log(levels,2) 
            nyquist_rate = 2*4000 #voice signal assumption
            actual_rate = sampling_multiplier*nyquist_rate
            information_rate = entropy*actual_rate
            
            channel_limitation = bandwidth*math.log(1+signal_to_noise_ratio,2)
            bit_error_rate = information_rate - channel_limitation
            
            
            signal_to_noise_ratio_error_free = round(sp.solveset(sp.Eq(information_rate,bandwidth*sp.log(1+x,2)),x,sp.Reals).args[0],2)
            signal_to_noise_ratio_error_free_dB = round(10*math.log(signal_to_noise_ratio,10),2)
            
            bandwidth_error_free = sp.solveset(sp.Eq(information_rate,x*sp.log(1+signal_to_noise_ratio,2)),x,sp.Reals).args[0]
            bandwidth_error_free = round(float(bandwidth_error_free),2)
            
            
        
            question = """Consider a digital source that converts an analog signal into digital form. If an input analog signal is sampled at {a:g}x the Nyquist sampling rate and each sample is quantized into one of {b:g} equally likely levels.
a. What is the information rate of this source?
b. Calculate the min bit error rate of this source if transmitted over an AWGN channel with a bandwidth of {c:g} kHz, and  {d:g} dB S/N ratio.
c. Find the S/N in dB require for error free transmission if the bandwidth is {c:g} kHz.
d. Find the bandwidth required for error free transmission if the signal to noise ratio is {d:g} dB
Assume that the sucessive samples are statistically independent.
""".format(a = sampling_multiplier, b = levels, c = bandwidth/1000, d= signal_to_noise_ratio_dB)
            
            soln = """Information Rate: {a:g} kbps, Bit Error Rate: {b:g} kbps, Error-Free SNR: {c:g} or {d:g} dB, Error-Free Bandwidth: {e:g} kHz""".format(
            a = round(information_rate/1000,2),
            b = round(bit_error_rate/1000,2),
            c = round(signal_to_noise_ratio_error_free,2),
            d = round(signal_to_noise_ratio_error_free_dB,2),
            e = round(bandwidth_error_free,2))
       
        if form == 8:
            bitrate = random.randint(1,9)*100*1000
            ratio = random.randint(1,9)
            baudrate = bitrate/ratio
            
            question = """A signal is carrying data in which {a:g} data elements are encoded as one signal element. If the bitrate is {b:g} kbps, what is the average value of the baud rate?""".format(a=ratio,b=bitrate/1000)
            
            soln = """Baudrate: {a:g} kBaud""".format(a=round(baudrate/1000,2))
            
        if form == 9:
            bitrate = round(random.uniform(100.000,500.000),3)*1000
            deviation = bitrate/2
            question = """Calculate the frequency shift (deviation) between mark and space frequency for GSM cellular radio system that uses Gaussian MSK (GMSK) with  a transmission rate of {a:g} kbps""".format(a = bitrate/1000)
            
            soln = """Deviation: {a:g} kHz""".format(a = round(deviation/1000,2))

        if form == 10:
            input_bitrate = random.randint(1,9)*10
            carrier_freq = random.randint(1,9)*10
            ratio = random.randint(1,5)
            modulation_type_list = ['none','BPSK','QPSK','8-PSK','16-PSK','32-PSK']
            modulation_type = modulation_type_list[ratio]
            baudrate = input_bitrate/ratio
            question = """Determine the minimum Nyquist bandwidth and the baudrate for a {type:s} modulator with a carrier frequency of {a:g} MHz and an input bitrate of {b:g} Mbps""".format(a=carrier_freq,b=input_bitrate,type=modulation_type)
            
            soln = """Baudrate: {a:g} MBaud""".format(a=round(baudrate,2))
            
        if form == 11:
            levels = random.sample([2,4,8,16,32,64,128,256,512,1024,2048],1)[0]
            bits = math.log(levels,2)
            
            question = """How many bits are needed to address {a:g} different level combinations?""".format(a=levels)
            
            soln = """Number of bits: {a:g} bits""".format(a=round(bits,2))
            
        if form == 12:
            ratio = random.randint(1,5)
            modulation_type_list = ['none','BPSK','QPSK','8-PSK','16-PSK','32-PSK']
            modulation_type = modulation_type_list[ratio]
            input_bitrate = random.randint(1,9)*10
            carrier_freq = random.randint(11,99)*10
            baudrate = input_bitrate/ratio
            question = """Calculate the minimum double-sided Nyquist bandwidth and the baudrate for a {type:s} modulator with an input data rate equal to {a:g} Mbps and a carrier frequency of {b:g} MHz.""".format(type = modulation_type, a = input_bitrate,b= carrier_freq)
            
            soln = """Nyquist bandwidth: {a:g} MHz, Baudrate: {a:g} MBaud""".format(a=round(baudrate,2))
            
        if form == 13:
            ratio = random.randint(1,5)
            modulation_type_list = ['none','BPSK','QPSK','8-PSK','16-PSK','32-PSK']
            modulation_type = modulation_type_list[ratio]
            input_bitrate = random.randint(10,99)
            
            question = """Determine the bandwidth efficiency for the following modulation scheme. {type:s}, input bitrate = {a:g} Mbps""".format(type=modulation_type,a=input_bitrate)
            
            soln = """Efficiency: {a:g} bps/Hz""".format(a=round(ratio,2))
            
        if form == 14:
            carrier_power_exponent = random.randint(-13,-10)
            carrier_power = 10**carrier_power_exponent
            noise_power_exponent = random.randint(-17,-14)
            noise_power = 10**noise_power_exponent
            bitrate = random.randint(1,9)*10*1000
            bandwidth = random.randint(1,9)*10*1000
            
            energy_per_bit = carrier_power/bitrate
            noise_density = noise_power/bandwidth
            probability_of_error = 0.5*math.exp(-0.5*(energy_per_bit/noise_density))
            
            
            question = """Calculate the probability of error for a non-coherent FSK system if the carrier power is 10^{a:g} W, bitrate of {b:g} kbps, bandwidth of {c:g} kHz and noise power of 10^{d:g} W.""".format(a=carrier_power_exponent,b=bitrate/1000, c=bandwidth/1000,d=noise_power_exponent)
            
            soln = """Probability of error: {a:g}""".format(a=round(probability_of_error,2))
       
        if form == 15:
            bits = random.sample([16,32,64,128,256,512],1)[0]
            hammings = sp.solveset(sp.Pow(2,x) - (x + bits +1) >=0,x,sp.Reals)
            
            question = """How many hamming bits would be added to a data block containing {a:g} bits?""".format(a = bits)
            
            soln = """Hamming bits: {a:s}""".format(a=str(hammings))
            
        if form == 16:
            number_of_errors = random.randint(2,5)
            number_of_data_bits = random.randint(10,30)
            
            bits_error_correction = number_of_errors + 1
            bits_error_detection = 2*number_of_errors + 1
            number_of_hamming_bits = sp.solveset(2**x - (number_of_data_bits + x + 1) >=0,x,sp.Reals)
            
            question = """Calculate the Hamming distance to detect and correct {a:g} single bit errors that occurred during transmission. Also compute fot the number of Hamming bits for a {b:g} bit data string.""".format(a = number_of_errors,b=number_of_data_bits)
            
            soln = """Hamming bits(detection): {a:g}, Hamming bits(correction): {b:g}, Number of hamming bits: {c:s}""".format(a=round(bits_error_detection,2),b=round(bits_error_correction,2),c=str(number_of_hamming_bits))
            
            
            
        self.question = question
        self.soln = soln

            
            


print(title_string)
print()


 
for i in range (1,5):
    A = digitalModulationClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""*{a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))

    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
