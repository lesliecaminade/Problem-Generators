from generator import constants_conversions as c
from generator import random_handler as ran
import sympy as sym
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
        
        self.question = f"""A phase modulator has kp = {kp.radians:5.3} radians / volt. What RMS voltage of a sine wave would cause a peak phase deviation of {phi.degrees:5.3} degrees."""
        
        vm = c.voltage(phi.radians / kp.radians)
        vmrms = c.voltage(vm.V / math.sqrt(2))
        
        self.answer = f"""{vmrms.V:5.3} V rms."""
        
class jma_1_73_b:
    def __init__(self,*args,**kwargs): 
        
        kf = c.frequency(ran.main(5), 'kHz')
        vm = c.voltage(ran.main(2))
        fm = c.frequency(ran.main(2000))
        
        self.question = f"""An FM modulator has a frequency deviation sensitivity of {kf.kHz:5.3} kHz / V and a modulating signal vm(t) = {vm.V:5.3} cos ( {2*fm.Hz:5.3} pi t ). Calculate the peak frequency deviation and modulation index.""" 
        
        deltaf = c.frequency(kf.Hz * vm.V)
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""{deltaf.kHz:5.3} kHz, {m:5.3}"""

class jma_1_74_a:
    def __init__(self,*args,**kwargs): 
        
        kp = c.angle(ran.main(2.5), 'radians')
        vm = c.voltage(ran.main(2))
        fm = c.frequency(ran.main(2000))
        
        self.question = f"""A PM modulator has a phase deviation sensitivity of {kp.radians:5.3} rad / V and modulating signal vm(t) = {vm.V:5.3} cos ( {2*fm.Hz:5.3} pi t ). Calculate the peak phase deviation and modulation index."""
        
        deltaphi = c.angle( kp.radians * vm.V, 'radians')
        m = deltaphi.radians
        
        self.answer = f"""{deltaphi.radians:5.3} radians, {m:5.3}"""

class jma_1_74_b:
    def __init__(self,*args,**kwargs): 
        
        M = c.percentage(ran.main(80), 'percent')
        
        self.question = f"""What is the frequency swing of an FM broadcast transmitter when modulated {M.percent:5.3} %?"""
        
        deltaf_actual = c.frequency(M.decimal * 75_000)
        
        self.answer = f"""{deltaf_actual.kHz:5.3} kHz"""
        
class jma_1_75:
    def __init__(self,*args,**kwargs): 
        
        cs = c.frequency(ran.main(100), 'kHz')
        
        self.question = f"""Calculate the frequency deviation and percent modulation under FCC standards for a given modulating signal that produces {cs.kHz:5.3} kHz carrier swing."""
        
        deltaf = c.frequency(cs.Hz / 2)
        M = c.percentage(deltaf.Hz / 75_000, 'decimal')

        self.answer = f"""{deltaf.kHz:5.3} kHz, {M.percent:5.3} percent"""

class jma_1_76_a:
    def __init__(self,*args,**kwargs): 
        
        deltaf = c.frequency(ran.main(100), 'kHz')
        fm = c.frequency(ran.main(15), 'kHz')
        
        self.question = f"""A system uses a deviation of {deltaf.kHz:5.3} kHz and a modulating frequency of {fm.kHz:5.3} kHz. What is the approximate bandwidth?"""
        
        bandwidth = c.frequency(2 * (deltaf.Hz + fm.Hz))
        
        self.answer = f"""{bandwidth.kHz:5.3} kHz"""

class jma_1_77_a:
    def __init__(self,*args,**kwargs): 
        
        fo = c.frequency(ran.main(10), 'MHz')
        lr = c.frequency(ran.main(8), 'MHz')
        cr = c.frequency(ran.main(4), 'MHz')
        
        fcapturelow = c.frequency(fo.Hz - cr.Hz/2)
        flockhigh = c.frequency(fo.Hz + lr.Hz/2)
        
        self.question = f"""A phase-locked loop has a VCO with a free running frequency of {fo.MHz:5.3} MHz. As the frequency of the reference input is gradually raised from zero, the loop locks at {fcapturelow.MHz:5.3} MHz and comes out of lock again at {flockhigh.MHz:5.3} MHz. a) Determine the lock range b) Determine the capture range."""
        
        self.answer = f"""{lr.MHz:5.3} MHz, {cr.MHz:5.3} MHz"""

class jma_1_77_c:
    def __init__(self,*args,**kwargs): 
        
        fo = c.frequency(ran.main(10), 'MHz')
        cr = c.percentage(ran.main(10), 'percent')
        lr = c.percentage(ran.main(20), 'percent')
        
        
        self.question = f"""Calculate the range of frequencies will the PLL be able to capture and subsequently maintain lock if it is used as a VCO with a free-running frequency of {fo.MHz:5.3} MHz, PLL has a {cr.percent:5.3} % capture range and {lr.percent:5.3} % lock range."""
        
        fcapturelow = c.frequency(fo.Hz - cr.decimal * fo.Hz)
        fcapturehigh = c.frequency(fo.Hz + cr.decimal * fo.Hz)
        flocklow = c.frequency(fo.Hz - lr.decimal * fo.Hz)
        flockhigh = c.frequency(fo.Hz + lr.decimal * fo.Hz)
        
        self.answer =f"""{fcapturelow.kHz:5.3} kHz to {fcapturehigh.kHz:5.3} kHz; {flocklow.kHz:5.3} kHz to {flockhigh.kHz:5.3} kHz"""
        
class schaums_ec_4_1:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(107.6), 'MHz')
        fm = c.frequency(ran.main(7), 'kHz')
        deltaf = c.frequency(ran.main(50), 'kHz')
        
        self.question = f"""A {fc.MHz:5.3} MHz carrier is frequency modulated by a {fm.kHz:5.3} kHz sine wave. The resultant FM signal has a frequency deviation of {deltaf.kHz:5.3} kHz. a) Find the carrier swing of the FM signal b) Determine the highest and lowest frequencies attained by the modulated signal. c) What is the modulation index of the FM wave?"""

        cs = c.frequency(2 * deltaf.Hz)
        
        fh = c.frequency(fc.Hz + deltaf.Hz)
        fl = c.frequency(fc.Hz + deltaf.Hz)
        
        m = deltaf.Hz/fm.Hz
        
        self.answer = f"""{cs.kHz:5.3} kHz; {fl.MHz:5.3} MHz and {fh.MHz:5.3} MHz., {m:5.3}"""

class schaums_ec_4_2:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(105), 'MHz')
        deltaf = c.frequency(ran.main(7), 'kHz')
        cs = c.frequency(2 * deltaf.Hz)
        fupper = c.frequency(fc.MHz + deltaf.Hz)
        
        self.question = f"""Determine the frequency deviation and carrier swing for a frequency modulated signal which has a resting frequency of {fc.MHz:5.3} MHz and whose upper frequency is {fupper.MHz:5.3} MHz when modulated by a particular wave. Find the lowest frequency reached by the FM wave."""
        
        flower = c.frequency(fc.Hz - deltaf.Hz)
        
        self.answer = f"""{deltaf.kHz:5.3} kHz, {cs.kHz:5.3} kHz, {flower.MHz:5.3} MHz"""

class schaums_ec_4_3:
    def __init__(self,*args,**kwargs): 
        
        cs = c.frequency(ran.main(100), 'kHz')
        fm = c.frequency(ran.main(8), 'kHz')
        
        self.question = f"""What is the modulation index of an FM signal having a carrier swing of {cs.kHz:5.3} kHz when the modulating signal has a frequency of {fm.kHz:5.3} kHz.?"""
        
        deltaf = c.frequency(cs.Hz/2)
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""{m:5.3}"""
        
class schaums_ec_4_4:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(100), 'MHz')
        fm = c.frequency(ran.main(3), 'kHz')
        deltaf = c.frequency(ran.main(20), 'kHz')
        
        fupper = c.frequency(fc.Hz + deltaf.Hz)
        flower = c.frequency(fc.Hz - deltaf.Hz)
        
        self.question = f"""A frequency-modulated signal which is modulated by a {fm.kHz:5.3} kHz sine wave reaches a maximum frequency of {fupper.MHz:5.3} MHz and a minimum frequency of {flower.MHz:5.3} MHz."""
        
        cs = c.frequency(2 * deltaf.Hz)
        
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""{cs.kHz:5.3} kHz, {fc.MHz:5.3} MHz, {deltaf.kHz:5.3} kHz, {m:5.3}"""

class schaums_ec_4_5:
    def __init__(self,*args,**kwargs): 
        
        deltaf = c.frequency(ran.main(20), 'kHz')
        
        self.question = f"""An FM transmission has a frequency deviation of {deltaf.kHz:5.3} kHz. a) Determine the percent modulation of this signal if it is broadcast in the 88 - 108 MHz band. b) Calculate the percent modulation if this signal were broadcast as the audio portion of a television broadcast (NTSC)."""
        
        M_fm = c.percentage(deltaf.Hz / 75_000, 'decimal')
        M_tv = c.percentage(deltaf.Hz / 25_000, 'decimal')
        
        self.answer = f"""{M_fm.percent:5.3} %, {M_tv.percent:5.3} %"""

class schaums_ec_4_6:
    def __init__(self,*args,**kwargs): 
        
        M = c.percentage(ran.main(75), 'percent')
        
        self.question = f"""a) What is the frequency deviation and carrier swing necessary to provide {M.percent:5.3} % modulation in the FM broadcast band? b) Repeat for an FM signal serving as the audio portion of an NTSC TV broadcast."""
        
        deltaf_fm = c.frequency(75_000 * M.decimal)
        cs_fm = c.frequency(2*deltaf_fm.Hz)
        deltaf_tv = c.frequency(25_000 * M.decimal)
        cs_tv = c.frequency(2*deltaf_tv.Hz)
        
        self.answer = f"""{deltaf_fm.kHz:5.3} kHz, {cs_fm.kHz:5.3} kHz; {deltaf_tv.kHz:5.3} kHz, {cs_tv.kHz:5.3} kHz"""

class schaums_ec_4_7:
    def __init__(self,*args,**kwargs): 
        
        cs = c.frequency(ran.main(125), 'kHz')
        
        self.question = f"""Determine the percent modulation of an FM signal which is being broadcast in the 88 - 108 MHz band having a carrier swing of {cs.kHz:5.3} kHz"""
        
        deltaf = c.frequency(cs.Hz / 2)
        M = c.percentage(deltaf.Hz / 75_000, 'decimal')
        
        self.answer = f"""{M.percent:5.3} %"""
        
class schaums_ec_4_8:
    def __init__(self,*args,**kwargs): 
        
        M = c.percentage(ran.main(80), 'percent')
        
        self.question = f"""The percent modulation of the sound portion of an NTSC TV signal is {M.percent:5.3} %. Determine the frequency deviation and the carrier swing of the signal."""
        
        deltaf = c.frequency(25_000 * M.decimal)
        
        cs = c.frequency(2 * deltaf.Hz)
        
        self.answer = f"""{deltaf.kHz:5.3} kHz, {cs.kHz:5.3} kHz"""

class schaums_ec_4_9:
    def __init__(self,*args,**kwargs): 
        
        fm = c.frequency(ran.main(5), 'kHz')
        fc = c.frequency(ran.main(50), 'MHz')
        deltaf = c.frequency(ran.main(20), 'kHz')
        
        self.question = f"""A {fm.kHz:5.3} kHz tone is used to modulate a {fc.MHz:5.3} MHz carrier causing a frequency deviation of {deltaf.kHz:5.3} kHz. Determine a) the modulation index."""
        
        m = deltaf.Hz / fm.Hz
        
        self.answer = f"""{m:5.3}"""
        
class schaums_ec_4_12:
    def __init__(self,*args,**kwargs): 
        
        bandwidth = c.frequency(ran.main(6, 'int'), 'MHz')
        
        self.question = f"""If a {bandwidth.MHz:5.3} MHz band were being considered for use with the same standards that apply to the 88 - 108 MHz band, how many FM stations could be accomodated?"""
        
        stations = math.floor(bandwidth.Hz / 400_000)
        #each station requires a bandwidth of 400 kHz, 150 kHz for the signal, 25 kHz guardband above and below, with only alternating channels used.
        
        
        self.answer = f"""{stations}"""
        
class schaums_ec_4_13:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(125), 'MHz')
        fm = c.frequency(ran.main(4), 'kHz')
        
        self.question = f"""Determine the bandwidth of a narrowband FM signal which is generated by a {fm.kHz:5.3} kHz audio signal modulating a {fc.MHz:5.3} MHz carrier."""
        
        bandwidth = c.frequency(2 * fm.Hz)
        
        self.answer = f"""{bandwidth.kHz:5.3} kHz"""
        
class schaums_ec_4_14:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            fm = c.frequency(ran.main(2), 'kHz')
            fc = c.frequency(ran.main(50), 'MHz')
            deltaf = c.frequency(ran.main(2.5), 'kHz')
            
            self.question = f"""A {fm.kHz:5.3} kHz audio signal modulates a {fc.MHz:5.3} carrier, causing a frequency deviation of {deltaf.kHz:5.3} kHz. Determine the bandwidth of the FM signal."""
            
            m = deltaf.Hz / fm.Hz
            
            if m < math.pi/2:
                regen = 0
        
        bandwidth = c.frequency(2*fm.Hz)
        
        self.answer = f"""{bandwidth.kHz:5.3} kHz"""
        
class schaums_ec_4_15:
    def __init__(self,*args,**kwargs): 
        
        hie = c.resistance(ran.main(600), 'ohms')
        beta = ran.main(65)
        betalow = ran.main(50)
        betahigh = betalow + ran.main(20)
        r2 = c.resistance(ran.main(12), 'kohms')
        c2 = c.capacitance(ran.main(150), 'pF')
        
        self.question = f"""The transistor reactance modulator shown is to be used in an FM transmitter. The resistance of the transistor (hie) is {hie.ohms:5.3} ohms and the beta of the transistor is {beta:5.3}. a) How much capacitance does this circuit present to the tank circuit it is attached to? b) If the beta of the transistor can be caused to swing from {betalow:5.3} to {betahigh:5.3}, determine the swing in capacitance presented by this circuit. Note that resistor R2 = {r2.kohms:5.3} kohms and capacitor C2 = {c2.pF:5.3} pF.
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
        
        self.answer = f"""{ceq.nF:5.3} nF; {ceqlow.nF:5.3} nF to {ceqhigh.nF:5.3} nF"""

class schaums_ec_4_16:
    def __init__(self,*args,**kwargs): 
        
        gmlow = c.conductance(ran.main(2500), 'uS')
        gmhigh = c.conductance(gmlow.uS + ran.main(1000), 'uS')
        r1 = c.resistance(ran.main(100), 'kohms')
        c1 = c.capacitance(ran.main(75), 'pF')
        
        
        self.question = f"""The reactance tube modulator uses a remote cutoff tube whose transconductance (gm) varies from {gmlow.uS:5.3} uS to {gmhigh.uS:5.3} uS. Determine the range of capacitance it presents. Note that R = {r1.kohms:5.3} kohms and C = {c1.pF:5.3} pF
        https://lesliecaminadecom.files.wordpress.com/2019/07/l8ayo9y1kmca171wzq4z.png"""
        
        
        ceqlow = c.capacitance( gmlow.S * r1.ohms * c1.F )
        ceqhigh = c.capacitance( gmhigh.S * r1.ohms * c1.F)
        
        self.answer = f"""{ceqlow.nF:5.3} nF to {ceqhigh.nF:5.3} nF"""
        
class schaums_ec_4_17:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(7.5), 'MHz')
        deltaf = c.frequency(ran.main(6), 'kHz')
        fosc = c.frequency(ran.main(6), 'MHz')
        
        self.question = f"""Shown is the block diagram of the frequency multiplier and heterodyne portion of an FM transmitter. Calculate the carrier frequency and frequency deviation of each of the points: a) 1, b) 2, and c) 3. Note that fc = {fc.MHz:5.3} MHz, deltaf = {deltaf.kHz:5.3} kHz and the oscillator frequency is  {fosc.MHz:5.3} MHz.
        https://lesliecaminadecom.files.wordpress.com/2019/07/340i9sce5lfd0lu8q7bv.png"""
        
        fc1 = c.frequency(3 * fc.Hz)
        deltaf1 = c.frequency(3 * deltaf.Hz)
        
        fc2 = c.frequency(4 * fc1.Hz)
        deltaf2 = c.frequency(4 * deltaf1.Hz)
        
        fc3 = c.frequency( fc2.Hz + fosc.Hz)
        deltaf3 = c.frequency(deltaf2.Hz)
        
        self.answer =f"""{fc1.MHz:5.3} MHz, {deltaf1.kHz:5.3} kHz; {fc2.MHz:5.3} MHz, {deltaf2.kHz:5.3} kHz; {fc3.MHz:5.3} MHz, {deltaf3.kHz:5.3} kHz"""

         
          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        