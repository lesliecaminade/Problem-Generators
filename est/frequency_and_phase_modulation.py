
import random_handler as ran
import sympy as sym
from sympy import init_printing
import math
import random
import mpmath

x, y, z = sym.symbols('x y z', real = True)#generic variables

def significant_sidebands(*args, **kwargs):
    #args[0] - represents modulation index input
    modulation_index = args[0]
    
    bessel = 1
    
    sideband_number = 0
    
    while bessel > 0.01:
        bessel = mpmath.besselj(sideband_number, modulation_index)
        sideband_number = sideband_number + 1
        
    return (sideband_number - 1)
    
        

class jma_1_73_a:
    def __init__(self,*args,**kwargs): 
        
        kp = c.angle(ran.main(2), 'radians')
        phi = c.angle(ran.main(30), 'degrees')
        
        self.question = f"""A phase modulator has kp = {kp.radians} radians / volt. What RMS voltage of a sine wave would cause a peak phase deviation of {phi.degrees} degrees."""
        
        vm = c.voltage(phi.radians / kp.radians)
        vmrms = c.voltage(vm.V / math.sqrt(2))
        
        self.answer = f"""Sine wave RMS voltage = {vmrms.V} V rms."""
        
class jma_1_73_b:
    def __init__(self,*args,**kwargs): 
        
        kf = c.frequency(ran.main(5), 'kHz')
        vm = c.voltage(ran.main(2))
        fm = c.frequency(ran.main(2000))
        
        self.question = f"""An FM modulator has a frequency deviation sensitivity of {kf.kHz} kHz / V and a modulating signal vm(t) = {vm.V} cos ( {2*fm.Hz} pi t ). Calculate the peak frequency deviation and modulation index.""" 
        
        deltaf = c.frequency(kf.Hz * vm.V)
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""Frequency deviation = {deltaf.kHz} kHz
Modulation index = {m}"""

class jma_1_74_a:
    def __init__(self,*args,**kwargs): 
        
        kp = c.angle(ran.main(2.5), 'radians')
        vm = c.voltage(ran.main(2))
        fm = c.frequency(ran.main(2000))
        
        self.question = f"""A PM modulator has a phase deviation sensitivity of {kp.radians} rad / V and modulating signal vm(t) = {vm.V} cos ( {2*fm.Hz} pi t ). Calculate the peak phase deviation and modulation index."""
        
        deltaphi = c.angle( kp.radians * vm.V, 'radians')
        m = deltaphi.radians
        
        self.answer = f"""Peak phase deviation = {deltaphi.radians} radians
Modulation index = {m}"""

class jma_1_74_b:
    def __init__(self,*args,**kwargs): 
        
        M = c.percentage(ran.main(80), 'percent')
        
        self.question = f"""What is the frequency swing of an FM broadcast transmitter when modulated {M.percent} %?"""
        
        deltaf_actual = c.frequency(M.decimal * 75_000)
        
        self.answer = f"""Frequency swing = {deltaf_actual.kHz} kHz"""
        
class jma_1_75:
    def __init__(self,*args,**kwargs): 
        
        cs = c.frequency(ran.main(100), 'kHz')
        
        self.question = f"""Calculate the frequency deviation and percent modulation under FCC standards for a given modulating signal that produces {cs.kHz} kHz carrier swing."""
        
        deltaf = c.frequency(cs.Hz / 2)
        M = c.percentage(deltaf.Hz / 75_000, 'decimal')

        self.answer = f"""Frequency deviation = {deltaf.kHz} kHz
Percent modulation = {M.percent} percent"""

class jma_1_76_a:
    def __init__(self,*args,**kwargs): 
        
        deltaf = c.frequency(ran.main(100), 'kHz')
        fm = c.frequency(ran.main(15), 'kHz')
        
        self.question = f"""A system uses a deviation of {deltaf.kHz} kHz and a modulating frequency of {fm.kHz} kHz. What is the approximate bandwidth?"""
        
        bandwidth = c.frequency(2 * (deltaf.Hz + fm.Hz))
        
        self.answer = f"""Bandwidth = {bandwidth.kHz} kHz"""
        
class jma_1_76_b:
    def __init__(self,*args,**kwargs): 
        
        self.question = f"""Calculate the deviation ratio and appproximate bandwidth for the worst-case modulation index for an FM broadcast-band transmitter"""
        
        self.answer = f"""Deviation ratio = 5
Approximate bandwidth = 180 kHz"""

class jma_1_77_a:
    def __init__(self,*args,**kwargs): 
        
        fo = c.frequency(ran.main(10), 'MHz')
        lr = c.frequency(ran.main(8), 'MHz')
        cr = c.frequency(ran.main(4), 'MHz')
        
        fcapturelow = c.frequency(fo.Hz - cr.Hz/2)
        flockhigh = c.frequency(fo.Hz + lr.Hz/2)
        
        self.question = f"""A phase-locked loop has a VCO with a free running frequency of {fo.MHz} MHz. As the frequency of the reference input is gradually raised from zero, the loop locks at {fcapturelow.MHz} MHz and comes out of lock again at {flockhigh.MHz} MHz. a) Determine the lock range b) Determine the capture range."""
        
        self.answer = f"""a) Lock range = {lr.MHz} MHz
b) Capture range = {cr.MHz} MHz"""

class jma_1_77_c:
    def __init__(self,*args,**kwargs): 
        
        fo = c.frequency(ran.main(10), 'MHz')
        cr = c.percentage(ran.main(10), 'percent')
        lr = c.percentage(ran.main(20), 'percent')
        
        
        self.question = f"""Calculate the range of frequencies will the PLL be able to capture and subsequently maintain lock if it is used as a VCO with a free-running frequency of {fo.MHz} MHz, PLL has a {cr.percent} % capture range and {lr.percent} % lock range."""
        
        fcapturelow = c.frequency(fo.Hz - cr.decimal * fo.Hz)
        fcapturehigh = c.frequency(fo.Hz + cr.decimal * fo.Hz)
        flocklow = c.frequency(fo.Hz - lr.decimal * fo.Hz)
        flockhigh = c.frequency(fo.Hz + lr.decimal * fo.Hz)
        
        self.answer =f"""Capture range: {fcapturelow.kHz} kHz to {fcapturehigh.kHz} kHz
Lock range: {flocklow.kHz} kHz to {flockhigh.kHz} kHz"""

class jma_1_79:
    def __init__(self,*args,**kwargs): 
        
        self.question = f"""Calculate the approximate break frequency for FM broadcast band pre-emphasis circuit (FCC standards)"""
        
        self.answer = f"""Break frequency = 2.12 kHz"""
        
        
class schaums_ec_4_1:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(107.6), 'MHz')
        fm = c.frequency(ran.main(7), 'kHz')
        deltaf = c.frequency(ran.main(50), 'kHz')
        
        self.question = f"""A {fc.MHz} MHz carrier is frequency modulated by a {fm.kHz} kHz sine wave. The resultant FM signal has a frequency deviation of {deltaf.kHz} kHz. a) Find the carrier swing of the FM signal b) Determine the highest and lowest frequencies attained by the modulated signal. c) What is the modulation index of the FM wave?"""

        cs = c.frequency(2 * deltaf.Hz)
        
        fh = c.frequency(fc.Hz + deltaf.Hz)
        fl = c.frequency(fc.Hz + deltaf.Hz)
        
        m = deltaf.Hz/fm.Hz
        
        self.answer = f"""Carrier swing = {cs.kHz} kHz
Lowest and highest frequencies attained by the modulated signal = {fl.MHz} MHz and {fh.MHz} MHz.
Modulation index = {m}"""

class schaums_ec_4_2:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(105), 'MHz')
        deltaf = c.frequency(ran.main(7), 'kHz')
        cs = c.frequency(2 * deltaf.Hz)
        fupper = c.frequency(fc.MHz + deltaf.Hz)
        
        self.question = f"""Determine the frequency deviation and carrier swing for a frequency modulated signal which has a resting frequency of {fc.MHz} MHz and whose upper frequency is {fupper.MHz} MHz when modulated by a particular wave. Find the lowest frequency reached by the FM wave."""
        
        flower = c.frequency(fc.Hz - deltaf.Hz)
        
        self.answer = f"""Frequency deviation = {deltaf.kHz} kHz
Carrier swing = {cs.kHz} kHz
Lowest FM frequency = {flower.MHz} MHz"""

class schaums_ec_4_3:
    def __init__(self,*args,**kwargs): 
        
        cs = c.frequency(ran.main(100), 'kHz')
        fm = c.frequency(ran.main(8), 'kHz')
        
        self.question = f"""What is the modulation index of an FM signal having a carrier swing of {cs.kHz} kHz when the modulating signal has a frequency of {fm.kHz} kHz.?"""
        
        deltaf = c.frequency(cs.Hz/2)
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""Modulation index = {m}"""
        
class schaums_ec_4_4:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(100), 'MHz')
        fm = c.frequency(ran.main(3), 'kHz')
        deltaf = c.frequency(ran.main(20), 'kHz')
        
        fupper = c.frequency(fc.Hz + deltaf.Hz)
        flower = c.frequency(fc.Hz - deltaf.Hz)
        
        self.question = f"""A frequency-modulated signal which is modulated by a {fm.kHz} kHz sine wave reaches a maximum frequency of {fupper.MHz} MHz and a minimum frequency of {flower.MHz} MHz."""
        
        cs = c.frequency(2 * deltaf.Hz)
        
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""Carrier swing = {cs.kHz} kHz
Carrier frequency = {fc.MHz} MHz
Frequency deviation = {deltaf.kHz} kHz
Modulation index = {m}"""

class schaums_ec_4_5:
    def __init__(self,*args,**kwargs): 
        
        deltaf = c.frequency(ran.main(20), 'kHz')
        
        self.question = f"""An FM transmission has a frequency deviation of {deltaf.kHz} kHz. a) Determine the percent modulation of this signal if it is broadcast in the 88 - 108 MHz band. b) Calculate the percent modulation if this signal were broadcast as the audio portion of a television broadcast (NTSC)."""
        
        M_fm = c.percentage(deltaf.Hz / 75_000, 'decimal')
        M_tv = c.percentage(deltaf.Hz / 25_000, 'decimal')
        
        self.answer = f"""Percent modulation (commercial) = {M_fm.percent} %
Percent modulation (TV NTSC) = {M_tv.percent} %"""

class schaums_ec_4_6:
    def __init__(self,*args,**kwargs): 
        
        M = c.percentage(ran.main(75), 'percent')
        
        self.question = f"""a) What is the frequency deviation and carrier swing necessary to provide {M.percent} % modulation in the FM broadcast band? b) Repeat for an FM signal serving as the audio portion of an NTSC TV broadcast."""
        
        deltaf_fm = c.frequency(75_000 * M.decimal)
        cs_fm = c.frequency(2*deltaf_fm.Hz)
        deltaf_tv = c.frequency(25_000 * M.decimal)
        cs_tv = c.frequency(2*deltaf_tv.Hz)
        
        self.answer = f"""For commercial FM: 
Frequency deviation = {deltaf_fm.kHz} kHz
Carrier swing = {cs_fm.kHz} kHz

For NTSC TV broadcast:
Frequency deviation = {deltaf_tv.kHz} kHz
Carrier swing = {cs_tv.kHz} kHz"""

class schaums_ec_4_7:
    def __init__(self,*args,**kwargs): 
        
        cs = c.frequency(ran.main(125), 'kHz')
        
        self.question = f"""Determine the percent modulation of an FM signal which is being broadcast in the 88 - 108 MHz band having a carrier swing of {cs.kHz} kHz"""
        
        deltaf = c.frequency(cs.Hz / 2)
        M = c.percentage(deltaf.Hz / 75_000, 'decimal')
        
        self.answer = f"""Percent modulation = {M.percent} %"""
        
class schaums_ec_4_8:
    def __init__(self,*args,**kwargs): 
        
        M = c.percentage(ran.main(80), 'percent')
        
        self.question = f"""The percent modulation of the sound portion of an NTSC TV signal is {M.percent} %. Determine the frequency deviation and the carrier swing of the signal."""
        
        deltaf = c.frequency(25_000 * M.decimal)
        
        cs = c.frequency(2 * deltaf.Hz)
        
        self.answer = f"""Frequency deviation = {deltaf.kHz} kHz
Carrier swing = {cs.kHz} kHz"""

class schaums_ec_4_9:
    def __init__(self,*args,**kwargs): 
        
        fm = c.frequency(ran.main(5), 'kHz')
        fc = c.frequency(ran.main(50), 'MHz')
        deltaf = c.frequency(ran.main(20), 'kHz')
        
        self.question = f"""A {fm.kHz} kHz tone is used to modulate a {fc.MHz} MHz carrier causing a frequency deviation of {deltaf.kHz} kHz. Determine a) the modulation index."""
        
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""Modulation index = {m}"""
        
class schaums_ec_4_12:
    def __init__(self,*args,**kwargs): 
        
        bandwidth = c.frequency(ran.main(6, 'int'), 'MHz')
        
        self.question = f"""If a {bandwidth.MHz} MHz band were being considered for use with the same standards that apply to the 88 - 108 MHz band, how many FM stations could be accomodated?"""
        
        stations = math.floor(bandwidth.Hz / 400_000)
        #each station requires a bandwidth of 400 kHz, 150 kHz for the signal, 25 kHz guardband above and below, with only alternating channels used.
        
        
        self.answer = f"""Number of stations = {stations}"""
        
class schaums_ec_4_13:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(125), 'MHz')
        fm = c.frequency(ran.main(4), 'kHz')
        
        self.question = f"""Determine the bandwidth of a narrowband FM signal which is generated by a {fm.kHz} kHz audio signal modulating a {fc.MHz} MHz carrier."""
        
        bandwidth = c.frequency(2 * fm.Hz)
        
        self.answer = f"""Bandwidth ~ {bandwidth.kHz} kHz"""
        
class schaums_ec_4_14:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            fm = c.frequency(ran.main(2), 'kHz')
            fc = c.frequency(ran.main(50), 'MHz')
            deltaf = c.frequency(ran.main(2.5), 'kHz')
            
            self.question = f"""A {fm.kHz} kHz audio signal modulates a {fc.MHz} carrier, causing a frequency deviation of {deltaf.kHz} kHz. Determine the bandwidth of the FM signal."""
            
            m = deltaf.Hz / fm.Hz
            
            if m < math.pi/2:
                regen = 0
        
        bandwidth = c.frequency(2*fm.Hz)
        
        self.answer = f"""Bandwidth = {bandwidth.kHz} kHz"""
        
class schaums_ec_4_15:
    def __init__(self,*args,**kwargs): 
        
        hie = c.resistance(ran.main(600), 'ohms')
        beta = ran.main(65)
        betalow = ran.main(50)
        betahigh = betalow + ran.main(20)
        r2 = c.resistance(ran.main(12), 'kohms')
        c2 = c.capacitance(ran.main(150), 'pF')
        
        self.question = f"""The transistor reactance modulator shown is to be used in an FM transmitter. The resistance of the transistor (hie) is {hie.ohms} ohms and the beta of the transistor is {beta}. a) How much capacitance does this circuit present to the tank circuit it is attached to? b) If the beta of the transistor can be caused to swing from {betalow} to {betahigh}, determine the swing in capacitance presented by this circuit. Note that resistor R2 = {r2.kohms} kohms and capacitor C2 = {c2.pF} pF.
        https://lesliecaminadecom.files.wordpress.com/2019/07/q33678d2mdswv2pmf7qm.png"""
        
       
        
        ceq = c.capacitance(
        (beta * r2.ohms * c2.F) / (hie.ohms + r2.ohms)
        )
        
        ceqlow = c.capacitance(
        (betalow * r2.ohms * c2.F) / (hie.ohms + r2.ohms)
        )
        
        ceqhigh = c.capacitance(
        (betahigh * r2.ohms * c2.F) / (hie.ohms + r2.ohms)
        )
        
        self.answer = f"""Capacitance at situation a = {ceq.nF} nF
Capacitance range at situation b = {ceqlow.nF} nF to {ceqhigh.nF} nF"""

class schaums_ec_4_16:
    def __init__(self,*args,**kwargs): 
        
        gmlow = c.conductance(ran.main(2500), 'uS')
        gmhigh = c.conductance(gmlow.uS + ran.main(1000), 'uS')
        r1 = c.resistance(ran.main(100), 'kohms')
        c1 = c.capacitance(ran.main(75), 'pF')
        
        
        self.question = f"""The reactance tube modulator uses a remote cutoff tube whose transconductance (gm) varies from {gmlow.uS} uS to {gmhigh.uS} uS. Determine the range of capacitance it presents. Note that R = {r1.kohms} kohms and C = {c1.pF} pF
        https://lesliecaminadecom.files.wordpress.com/2019/07/l8ayo9y1kmca171wzq4z.png"""
        
        
        ceqlow = c.capacitance( gmlow.S * r1.ohms * c1.F )
        ceqhigh = c.capacitance( gmhigh.S * r1.ohms * c1.F)
        
        self.answer = f"""Capacitance range possible: {ceqlow.nF} nF to {ceqhigh.nF} nF"""
        
class schaums_ec_4_17:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(7.5), 'MHz')
        deltaf = c.frequency(ran.main(6), 'kHz')
        fosc = c.frequency(ran.main(6), 'MHz')
        
        self.question = f"""Shown is the block diagram of the frequency multiplier and heterodyne portion of an FM transmitter. Calculate the carrier frequency and frequency deviation of each of the points: a) 1, b) 2, and c) 3. Note that fc = {fc.MHz} MHz, deltaf = {deltaf.kHz} kHz and the oscillator frequency is  {fosc.MHz} MHz.
        https://lesliecaminadecom.files.wordpress.com/2019/07/340i9sce5lfd0lu8q7bv.png"""
        
        fc1 = c.frequency(3 * fc.Hz)
        deltaf1 = c.frequency(3 * deltaf.Hz)
        
        fc2 = c.frequency(4 * fc1.Hz)
        deltaf2 = c.frequency(4 * deltaf1.Hz)
        
        fc3 = c.frequency( fc2.Hz + fosc.Hz)
        deltaf3 = c.frequency(deltaf2.Hz)
        
        self.answer =f"""At point 1:
Carrier frequency = {fc1.MHz} MHz
Frequency deviation = {deltaf1.kHz} kHz

At point 2:
Carrier frequency = {fc2.MHz} MHz
Frequency deviation = {deltaf2.kHz} kHz

At point 3:
Carrier frequency = {fc3.MHz} MHz
Frequency deviation = {deltaf3.kHz} kHz"""

         
          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        