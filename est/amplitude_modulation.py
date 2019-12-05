import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
import math
import random
import algebra
import analytic_geometry
import constants_conversions as c
#import randomizer_2 as ran2

x, y, z = sym.symbols('x y z', real = True)#generic variables

class schaums_ec_3_1:
    def __init__(self,*args,**kwargs): 
        
        vm = c.voltage(ran.main(15))
        vc = c.voltage(ran.main(60))
        fm = c.frequency(ran.main(1500))
        fc = c.frequency(ran.main(100_000))
        
        
        self.question = f"""An audio signal {vm.V} sin ( 2 pi {fm.Hz} t ) amplitude modulates a carrier {vc.V} sin ( 2 pi {fc.Hz} t ). a) Determine the modulation factor and percent modulation. b) What are the frequencies of the audio signal and the carrier? c) What frequencies would show up in the spectrum of the modulated wave?"""
        
        
        m = c.percentage( vm.V / vc.V, 'decimal')
        
        #fm = c.frequency( omegam.radpers / ( 2 * math.pi ))
        
        #fc = c.frequency( omegac.radpers / ( 2 * math.pi ))
        
        fc_plus_fm = c.frequency( fc.Hz + fm.Hz )
        
        fc_minus_fm = c.frequency( fc.Hz - fm.Hz )
        
        self.answer = f"""Modulation index = {m.decimal} 
Percent modulation = {m.percent} %
Audio signal frequency = {fm.Hz} Hz
Carrier frequency = {fc.Hz} Hz
Frequencies in the modulated wave = {fc.Hz} Hz, {fc_plus_fm.Hz} Hz and {fc_minus_fm.Hz} Hz"""

class schaums_ec_3_2:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(75), 'MHz' )
        fm = c.frequency(ran.main(3), 'kHz')
        vc = c.voltage(ran.main(50))
        vm = c.voltage(ran.main(20))
        
        
        self.question = f"""A {fc.MHz} MHz carrier having an amplitude of {vc.V} V is modulated by a {fm.kHz} kHz audio signal having an amplitude of {vm.V} V. a) Determine the modulation factor and the percent modulation. b) What frequencies would show up in a spectrum analysis of the modulated wave? c) Write the trigonometric equations for the carrier and the modulating wave."""
        
        
        m = c.percentage( vm.V / vc.V )
        
        fc_plus_fm = c.frequency( fc.Hz + fm.Hz )
        
        fc_minus_fm = c.frequency( fc.Hz - fm.Hz )
        
        self.answer = f"""Modulation factor = {m.decimal} 
Percent modulation = {m.percent} %
Frequencies in the modulated wave = {fc.Hz}, {fc_plus_fm.Hz} Hz, and {fc_minus_fm.Hz} Hz
vm (t) = {vm.V} sin ( {2*fc.Hz} pi t ) 
vc (t) = {vc.V} sin ( {2*fm.Hz} pi t )"""

class schaums_ec_3_3:
    def __init__(self,*args,**kwargs): 
        
        bandwidth = c.frequency(ran.main(100), 'kHz')
        fm = c.frequency(ran.main(5), 'kHz')
        
        self.question = f"""How many AM broadcast stations can be accomodated in a {bandwidth.kHz}-kHz bandwidth if the highest frequency modulating a carrier is {fm.kHz} kHz."""
        
        stations = math.floor( bandwidth.Hz / fm.Hz )
        
        self.answer = f"""Number of stations = {stations} stations"""
        
class schaums_ec_3_4:
    def __init__(self,*args,**kwargs): 
        
        bandwidth = c.frequency(ran.main(20), 'MHz' )
        fm = c.frequency(ran.main(3), 'kHz')
        
        self.question = f"""A bandwidth of {bandwidth.MHz} MHz is to be considered for the transmission of AM signals. If the highest audio frequencies used to modulate the carriers are not to exceed {fm.kHz} kHz, how many stations could broadcast within this band simultaneously without interfering with one another?"""
        
        stations = math.floor( bandwidth.Hz / fm.Hz )
        
        self.answer = f"""Number of stations = {stations} """
        
class schaums_ec_3_5:
    def __init__(self,*args,**kwargs): 
        pt = c.power(ran.main(1000))
        regen = True
        while regen:
            m = c.percentage(ran.main(100), 'percent')
            if m.percent < 100:
                regen = False
                
        self.question = f"""The total power content of an AM signal is {pt.W} W. Determine the power being transmitted at the carrier frequency and at each of the sidebands when the percent modulation is {m.percent}%."""
        
        equation = sym.Eq(
        pt.W,
        x * (1 + m.decimal**2/2)
        )
        
        pc_set = sym.solveset(equation,x)
        pc_list = list(pc_set)
        pc = c.power(pc_list[0])
        
        psb = c.power( ( pt.W - pc.W ) / 2 )

        self.answer =f"""Carrier power = {pc.W} W
Upper sideband power = Lower sideband power = {psb.W} W"""

class schaums_ec_3_6:
    def __init__(self,*args,**kwargs): 
        regen = True
        while regen:
            m = c.percentage(ran.main(80), 'percent')
            if m.percent < 100:
                regen = False
                
        pt = c.power(ran.main(2500))
        
        self.question = f"""Determine the power content of the carrier and each of the sidebands for an AM signal having a percent modulation of {m.percent} % and a total power of {pt.W} W"""
        
        equation = sym.Eq(
        pt.W,
        x * (1 + m.decimal**2/2)
        )
        
        pc_set = sym.solveset(equation,x)
        pc_list = list(pc_set)
        pc = c.power(pc_list[0])
        
        psb = c.power( ( pt.W - pc.W ) / 2)
        
        self.answer = f"""Carrier power = {pc.W} W
Upper sideband power = Lower sideband power = {psb.W} W"""

class schaums_ec_3_7:
    def __init__(self,*args,**kwargs): 
        
        pc = c.power(ran.main(5), 'kW')
        regen = True
        while regen:
            m = c.percentage(ran.main(75), 'percent')
            if m.percent < 100:
                regen = False
        
        self.question = f"""The power content of the carrier of an AM wave is {pc.kW} kW. Determine the power content of each of the sidebands and the total power transmitted when the arrier is modulated {m.percent} %."""

        psb = c.power( m.decimal**2 * pc.W / 4 )
        
        pt = c.power( pc.W + 2 * psb.W )
        
        self.answer = f"""Power in each sideband = {psb.W} W
Total power = {pt.W} W"""

class schaums_ec_3_8:
    def __init__(self,*args,**kwargs): 
        
        pc = c.power(ran.main(5), 'kW')
        regen = True
        while regen:
            m = c.percentage(ran.main(75), 'percent')
            if m.percent < 100:
                regen = False
        
        self.question = f"""An amplitude modulated wave has a power content of {pc.W} W at its carrier frequency. Determine the power content of each of the sidebands for a {m.percent} % modulation."""
        
        psb = c.power( pc.W * m.decimal**2 / 4)
        
        self.answer = f"""Power of each sideband = {psb.W} W"""
        
class schaums_ec_3_9:
    def __init__(self,*args,**kwargs): 
        
        pc = c.power(ran.main(8), 'kW' )
        psb = c.power(ran.main(2), 'kW')
        
        
        self.question = f"""Determine the percent modulation of an amplitude modulated wave which has a power content at the carrier of {pc.kW} kW and {psb.kW} kW in each of its sidebands when the carrier is modulated by a simple audio tone."""
         
        equation = sym.Eq(
        psb.W,
        x**2 * pc.W / 4
        )
        
        m_set = sym.solveset(equation,x)
        m_list = list(m_set)
        for i in range(len(m_list)):
            if m_list[i] >= 0 :
                m = c.percentage(m_list[i] , 'decimal')
        
        self.answer = f"""Percent Modulation = {m.percent} %"""
        
class schaums_ec_3_10:
    def __init__(self,*args,**kwargs): 
        
        pt = c.power(ran.main(600))
        psb = c.power(ran.main(75))
        
        self.question = f"""The total power of an AM wave is {pt.W} W. Determine the percent modulation of the signal if each of the sidebands contains {psb.W} W."""
        
        pc = c.power(pt.W - 2*psb.W)
        
        equation = sym.Eq(
        psb.W , 
        x**2 * pc.W / 4
        )
        
        m_set = sym.solveset(equation,x)
        m_list = list(m_set)
        for i in range(len(m_list)):
            if m_list[i] >= 0 :
                m = c.percentage(m_list[i] , 'decimal')
        
        self.answer = f"""Percent Modulation = {m.percent} %"""
        
class schaums_ec_3_11:
    def __init__(self,*args,**kwargs): 
        
        pt = c.power(ran.main(2500))
        psb = c.power(ran.main(400))
        
        
        self.question = f"""Find the percent modulation of an AM wave whose total power content is {pt.W} W and whose sidebands each contain {psb.W} W."""

        pc = c.power( pt.W - 2*psb.W )
        
        equation = sym.Eq(
        psb.W,
        x**2 * pc.W / 4
        )
        
        m_set = sym.solveset(equation,x)
        m_list = list(m_set)
        for i in range(len(m_list)):
            if m_list[i] >= 0 :
                m = c.percentage(m_list[i] , 'decimal')
        
        self.answer = f"""Percent Modulation = {m.percent} %"""
        
class schaums_ec_3_12:
    def __init__(self,*args,**kwargs): 
        
        pt = c.power(ran.main(1200))
        regen = True
        while regen:
            m = c.percentage(ran.main(75), 'percent')
            if m.percent < 100:
                regen = False
        
        self.question = f"""Determine the power content of each of the sidebands and of the carrier of an Am signal that has a percent modulation of {m.percent} % and contains {pt.W} W total power."""
        
        equation = sym.Eq(
        pt.W,
        x * (1 + m.decimal**2/2)
        )
        
        pc_set = sym.solveset(equation,x)
        pc_list = list(pc_set)
        pc = c.power(pc_list[0])
        
        psb = c.power( pc.W * m.decimal**2 / 4 )
        
        self.answer = f"""Carrier Power = {pc.W} W
Power in each sideband = {psb.W} W"""

class schaums_ec_3_13:
    def __init__(self,*args,**kwargs): 
        
        m_i = random.randint(0,1)
        m_list = [50,70]
        
        
        m = c.percentage(ran.main(m_list[m_i]), 'percent') 
        m2 = c.percentage(m.percent * 0.8, 'percent')
        pc = c.power(ran.main(1500))
            
        
        self.question = f"""An AM signal in which the carrier is modulated {m.percent} % contains {pc.W} W at the carrier frequency. Determine the power content of the upper and lower sidebands for this percent modulation. Calculate the power at the carrier and the power content of each of the sidebands when the percent modulation drops to {m2.percent} %."""
        
        psb = c.power(m.decimal**2 * pc.W / 4 )
        
        self.answer = f"""Power of each sideband = {psb.W} W"""
        
class schaums_ec_3_14:
    def __init__(self,*args,**kwargs): 
        
        m = c.percentage(ran.main(40), 'percent')
        m2 = c.percentage(m.percent + ran.main(20), 'percent')
        pc = c.power(ran.main(900))
        
        self.question = f"""The percent modulation of an AM wave changes from {m.percent} % to {m2.percent} %. Originally, the power content at the carrier frequency was {pc.W} W. Determine the power content at the carrier frequency and within each of the sidebands after the percent modulation has risen to {m2.percent} %.""" 
        
        psb = c.power(m2.decimal**2 * pc.W /4)
        
        self.answer = f"""Power in each sideband = {psb.W} W"""
        
class schaums_ec_3_15:
    def __init__(self,*args,**kwargs): 
        
        pt = c.power(ran.main(1000))
        
        self.question = f"""A single-sideband (SSB) signal contains {pt.W} W. How much power is contained in the sidebands and how much at the carrier frequency?"""
        
        psb = c.power(pt.W) 
        
        pc = c.power(0)
        
        self.answer = f"""Power at each sideband = {psb.W} W
Power at the carrier frequency = {pc.W} W"""

class schaums_ec_3_16:
    def __init__(self,*args,**kwargs): 
        
        pt = c.power(ran.main(10), 'kW')
        regen = True
        while regen:
            m = c.percentage(ran.main(80), 'percent')
            if m.percent <= 100:
                regen = False
                
        self.question = f"""An SSB transmission contains {pt.kW} kW. This transmission is to be replaced by a standard amplitude-modulated signal with the same power content. Determine the power content of the carrier and each of the sidebands when the percent modulation is {m.percent} %."""
        
        equation = sym.Eq(
        pt.W, 
        x * ( 1 + m.decimal**2 / 2)
        )
        
        pc_set = sym.solveset(equation, x)
        pc_list = list(pc_set)
        pc = c.power(pc_list[0])
        
        psb2 = c.power( (pt.W - pc.W) / 2 )
        
        self.answer = f"""Power at the carrier = {pc.W} W
Power at each sideband = {psb2.W} W"""

class schaums_ec_3_17:
    def __init__(self,*args,**kwargs): 
        
        vmin = c.voltage(ran.main(20))
        vmax = c.voltage(vmin.V + ran.main(60))
        
        self.question = f"""Determine the modulation factor and the percent modulation for an AM signal showing on a oscillocope with a value of Vmax = {vmax.V} V and Vmin = {vmin.V} V."""
        
        m = c.percentage(
        ( vmax.V - vmin.V ) / 
        ( vmax.V + vmin.V )
        )
        
        self.answer = f"""Modulation factor = {m.decimal}
Percent modulation = {m.percent} %"""

class schaums_ec_3_19:
    def __init__(self,*args,**kwargs): 
        
        
        
        b = c.length(ran.main(2), 'cm')
        a = c.length(b.cm + ran.main(3), 'cm')
        
        
        self.question = f"""The trapezoidal pattern shown results when examining an AM wave. Determine the modulation factor and percent modulation of the wave. A = {a.cm} cm while B = {b.cm} cm.
        https://lesliecaminadecom.files.wordpress.com/2019/07/sj9i71tc63cqu1tlyjb4.png
        """
        
        m = c.percentage(
        ( a.cm - b.cm ) / 
        ( a.cm + b.cm )
        )
        
        self.answer = f"""Percent modulation = {m.percent} %
Modulation factor = {m.decimal}"""

class schaums_ec_3_20:
    def __init__(self,*args,**kwargs): 
        
        b = c.length(ran.main(3), 'cm')
        a = c.length(b.cm + ran.main(5), 'cm')
        
        
        self.question = f"""The trapezoidal pattern shown results when examining an AM wave. Determine the modulation factor and percent modulation of the wave. A = {a.cm} cm while B = {b.cm} cm.
        https://lesliecaminadecom.files.wordpress.com/2019/07/sj9i71tc63cqu1tlyjb4.png
        """
        
        m = c.percentage(
        ( a.cm - b.cm ) / 
        ( a.cm + b.cm )
        )
        
        self.answer = f"""Percent modulation = {m.percent} %
Modulation factor = {m.decimal}"""
        
class schaums_ec_3_21:
    def __init__(self,*args,**kwargs): 
        
        fif = c.frequency(455, 'kHz')
        regen = True
        while regen:
            frf = c.frequency(ran.main(540), 'kHz')
            if frf.Hz > 535_000 and frf.Hz < 1605_000:
                regen = False
        
        
        self.question = f"""An AM standard broadcast receiver is to be designed having an intermediate frequency (IF) of 455 kHz. a) Calculate the required frequency that the local oscillator should be at when the receiver is tuned to {frf.kHz} kHz if the local oscillator tracks above the frequency of the received signal. b) Repeat situation "a" if the local oscillator tracks below the frequency of the received signal.""" 
        
        flo = c.frequency( frf.Hz + fif.Hz )
        
        flo2 = c.frequency( frf.Hz - fif.Hz )
        
        self.answer = f"""Local oscillator frequency for situtaion A = {flo.kHz} kHz
Local oscillator frequency for situation B = {flo2.kHz} kHz"""

class jma_1_40_a:
    def __init__(self,*args,**kwargs): 
        
        regen = True
        while regen:
            fc = c.frequency(ran.main(150), 'MHz')
            fm = c.frequency(ran.main(3), 'MHz')
            vc = c.voltage(ran.main(40))
            vm = c.voltage(ran.main(30))
            
            if vc.V > vm.V:
                regen = False
                
        self.question = f"""An AM signal has the foloowing characteristics: carrier frequency = {fc.MHz} MHz; modulating frequency = {fm.MHz} MHz; peak carrier voltage = {vc.V} V; and peak modulating voltage is {vm.V} V. Calculate the peak voltage of the lower sideband frequency."""
        
        m = c.percentage(vm.V / vc.V, 'decimal')
        vsb = c.voltage(m.decimal * vc.V / 2)
        
        self.answer = f"""Peak voltage in the lower sideband = {vsb.V} V"""
        
class jma_1_40_b:
    def __init__(self,*args,**kwargs): 
        
        regen = True
        while regen:
            vmax = c.voltage(ran.main(150))
            vm = c.voltage(ran.main(50))
            if vmax.V > vm.V:
                regen = False
        
        self.question = f"""Calculate the modulation index for a standard AM transmission, if the maximum peak voltage of the modulated wave is {vmax.V} V and the modulating signal voltage is {vm.V} V."""
        
        m = c.percentage(vm.V /( vmax.V - vm.V) , 'decimal')
        
        self.answer = f"""Modulation index = {m.decimal} """
        
class jma_1_42:
    def __init__(self,*args,**kwargs): 
        
        regen = True
        while regen:
            vmpp = c.voltage(ran.main(11))
            vc = c.voltage(ran.main(10))
            if vc.V > vmpp.V/2:
                regen = False
        
        self.question = f"""A modulating signal consists of a symmetrical triangular wave having zero DC component and peak - to - peak voltage of {vmpp.V} V. Calculate the value of modulation index if it is used to amplitude modulate a carrier of peak voltage {vc.V} V."""
        
        vmax = c.voltage(vc.V + vmpp.V/2)
        vmin = c.voltage(vc.V - vmpp.V/2)
        m = c.percentage(
        (vmax.V - vmin.V) / (vmax.V + vmin.V), 'decimal'
        )
        
        self.answer = f"""Modulation index = {m.decimal}"""
        
class jma_1_43_a:
    def __init__(self,*args,**kwargs): 
        
        fm1 = c.frequency(ran.main(1.5), 'kHz')
        fm2 = c.frequency(ran.main(2.5), 'kHz')
        m1 = c.percentage(ran.main(20), 'percent')
        m2 = c.percentage(ran.main(80), 'percent')
        
        self.question = f"""An AM transmitter is modulated by two sine waves at {fm1.kHz} kHz and {fm2.kHz} kHz, with modulation of {m1.percent} % and {m2.percent} % respectively. Calculate the effective modulation index."""
        
        mt = c.percentage(math.sqrt( m1.decimal**2 + m2.decimal**2))
        
        self.answer = f"""Total modulation index = {mt.decimal} """
        
class jma_1_43_b:
    def __init__(self,*args,**kwargs): 
        
        regen = True
        while regen:
            m1 = c.percentage(ran.main(75), 'percent')
            m2 = c.percentage(ran.main(45), 'percent')
            m3 = c.percentage(ran.main(48.5), 'percent')
            mt = c.percentage(math.sqrt(m1.decimal**2 + m2.decimal**2 + m3.decimal**2))
            
            if mt.percent < 100:
                regen = False
        
        vc = c.voltage(ran.main(100))
        

        self.question = f"""Calculate the modulating voltage of an audio signal necessary to provide {mt.percent} % modulation of a {vc.V} V carrier that is simultaneously modulated by two audio waves with m1 and m2 equal to {m1.percent}% and {m2.percent}% respectively."""

        vm3 = c.voltage(m3.decimal * vc.V)
        
        self.answer =f"""Modulating signal voltage = {vm3.V} V"""
        
        
class jma_1_46_a:
    def __init__(self,*args,**kwargs): 
        
        regen = True
        while regen:
            pc = c.power(ran.main(1200))
            m = c.percentage(ran.main(95), 'percent')
            if m.percent < 100:
                regen = False
        
        self.question = f"""What will be the total sideband power of an AM transmitting station whose carrier power is {pc.W} W and a modulation of {m.percent} %"""
        
        psb = c.power(m.decimal**2 * pc.W / 2)
        
        self.answer = f"""Total sideband power = {psb.W} W"""
        
class jma_1_46_b:
    def __init__(self,*args,**kwargs): 
        
        pc = c.power(ran.main(50))
        ic = c.current(ran.main(2))
        it = c.current(ic.A + ran.main(0.4))
        
        
        self.question = f"""Calculate the power in one sideband of an AM signal whose carrier power is {pc.W} W. The unmodulated current is {ic.A} A while the modulated current is {it.A} A."""
        
        
        m = c.percentage(
        math.sqrt( 2 * ( (it.A / ic.A)**2 - 1 ) )
        )
        
        pusb = c.power(m.decimal**2 * pc.W / 4)
        
        self.answer = f"""Power in one sideband = {pusb.W} W"""
        
class jma_1_46_c:
    def __init__(self,*args,**kwargs): 
        
        regen = 1
        while regen:
            m = c.percentage(ran.main(80), 'percent')
            pc = c.power(ran.main(50), 'kW')
            if m.percent <= 100:
                regen = 0
        
        self.question = f"""Calculate the total power and the power in each side frequency for a standard AM transmission that is sinusoidally modulated to a depth of {m.percent}% if the unmodulated carrier power is {pc.W} W."""
        
        pt = c.power(pc.W * (1 + m.decimal**2 / 2))
        pusb = c.power(m.decimal**2 * pc.W / 4)
        
        self.answer = f"""Total power = {pt.W} W
Power in each side frequency = {pusb.W} W"""

class jma_1_47_a:
    def __init__(self,*args,**kwargs): 
        
        regen = 1
        while regen:
            fc = c.frequency(ran.main(10), 'MHz')
            vc = c.voltage(ran.main(10))
            fm = c.frequency(ran.main(5), 'kHz')
            vm = c.voltage(ran.main(6))
            regen = 0
        
        self.question = f"""Calculate the amplitude and resulting side frequency if a carrier wave of frequency {fc.MHz} MHz with a peak value of {vc.V} V is amplitude modulated by a {fm.kHz} kHz sine wave of amplitude {vm.V} V."""
        
        m = c.percentage(vm.V / vc.V, 'decimal')
        fusb = c.frequency( fc.Hz + fm.Hz )
        flsb = c.frequency( fc.Hz - fm.Hz )
        vsb = c.voltage( m.decimal * vc.V / 2)
        
        self.answer = f"""Vsb = {vsb.V} V
fside = {fusb.MHz} MHz and {flsb.MHz} MHz"""

class jma_1_47_b:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            vt = c.voltage(ran.main(40))
            m = c.percentage(ran.main(100), 'percent')
            m2 = c.percentage(m.percent - ran.main(50), 'percent')
            if m.percent > m2.percent and m.percent <= 100 and m2.percent > 0 :
                regen = 0
        
        self.question = f"""The output voltage of an AM transmitter is {vt.V} V when sinusoidally modulated to a depth of {m.percent} %. Calculate the voltage at each side frequency when the modulation depth is reduced to {m2.percent}%."""
        
        vc = c.voltage(vt.V / (math.sqrt( 1 + m.decimal**2/2 )))
        vside = c.voltage(m2.decimal * vc.V / 2)
        
        self.answer = f"""Carrier voltage = {vc.V} V
Side frequency voltage = {vside.V} V"""

class jma_1_49:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            s = c.powerGain(ran.main(50), 'dB')
            p = c.power(ran.main(10))
            regen  = 0
            
        self.question = f"""A DSBSC system must suppress the carrier by {s.dB} dB from its original value of {p.W} W. To what value must the carrier be reduced?"""
        
        p2 = c.power( p.W / s.unitless)
        
        self.answer = f"""Carrier is reduced to {p2.uW} uW"""
        
class jma_1_50:
    def __init__(self,*args,**kwargs): 
        
        regen = 1
        while regen:
            m = c.percentage(ran.main(100), 'percent')
            pc = c.power(ran.main(1000))
            if m.percent <= 100:
                regen = 0
            
        self.question = f"""Assuming {m.percent}% modulation H3E system, what would be the transmitted power in the remaining sideband of an AM signal if the carrier power is {pc.W} W?"""
    
        psb = c.power(m.decimal**2 * pc.W / 4) 
        
        self.answer = f"""Sideband power = {psb.W} W"""
        
class jma_1_52_a:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            m = c.percentage(ran.main(80), 'percent')
            if m.percent <=100:
                regen = 0
        
        self.question = f"""Determine the power saving in percent when the carrier is suppressed in an AM signal modulated to {m.percent} %."""
        
        ptam = c.power( 1 + m.decimal**2 / 2)
        ptsc = c.power( m.decimal**2 / 2 )
        
        ps = c.percentage( (ptam.W - ptsc.W) / ptam.W , 'decimal')
        
        self.answer = f"""Power saving percentage = {ps.percent} %"""
        
class jma_1_52_b:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            m = c.percentage( ran.main(90), 'percent')
            if m.percent <= 100:
                regen = 0
        
        self.question = f"""Calculate the percentage power saving for a J3E system at {m.percent}% modulation."""

        ptam = c.power( 1 + m.decimal**2/2 )
        ptssbsc = c.power( m.decimal**2/4 )
        ps = c.percentage( (ptam.W - ptssbsc.W) / ptam.W, 'decimal')
        
        self.answer = f"""Power saving percentage = {ps.percent} %"""
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        