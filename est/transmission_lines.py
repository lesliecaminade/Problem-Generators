
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


class jma_3_6:
    def __init__(self,*args,**kwargs): 
    
        inductance = c.inductance(ran.main(234), 'nH')
        frequency = c.frequency(ran.main(10), 'MHz')
        capacitance = c.capacitance(ran.main(93.5), 'pF')
        resistance = c.resistance(ran.main(0.568), 'ohms')
        
        
        self.question = f"""The primary line constant for a coaxial cable at a frequency of {frequency.MHz} MHz were determined to be approximately as follows: L = {inductance.nH} nH / m, C = {capacitance.pF} pF / m, R = {resistance.ohms} ohms /m, G = 0. Determine the characteristic impedance."""
        
        zo = c.resistance(math.sqrt( inductance.H / capacitance.F) )
        
        self.answer = f"""Characteristic Impedance = {zo.ohms} ohms"""
        
class jma_3_8:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            length = c.length(ran.main(25))
            vf = ran.main(0.66)
            frequency = c.frequency(ran.main(5), 'MHz')
            if vf < 1:  
                regen = 0
        
        self.question = f"""A signal will undergo a phase shift of how many radians per meter when propagating on a {length.m}-m coaxial cable with a velocity of {vf}c and operating at {frequency.MHz} MHz. Also compute for the total phase delay in degrees."""
        
        beta = c.angle( (2 * math.pi * frequency.Hz ) / ( vf * 3e8 ), 'radians')
        
        theta = c.angle( beta.degrees * length.m, 'degrees' )
        
        self.answer = f"""Phase Coefficient = {beta.rad} rad/m
Total phase delay = {theta.degrees} degrees"""

class jma_3_9_a:
    def __init__(self,*args,**kwargs): 
        
        zo = c.resistance(ran.main(50))
        capacitance = c.capacitance(ran.main(40), 'pF')
        inductance = c.inductance(ran.main(50), 'uH')
        
        self.question = f"""Calculate the velocity factor of a coaxial cable used as a transmission line, with the characteristic impedance of {zo.ohms} ohms, capacitance is {capacitance.pF} pF/m, and the inductance equal to {inductance.uH} uH / m."""
        
        vf = 1 / (3e8 * math.sqrt( inductance.H * capacitance.F ))
        
        self.answer = f"""Velocity factor = {vf}"""
        
class jma_3_9_b:
    def __init__(self,*args,**kwargs): 
        
        phasedelay = c.angle(ran.main(45), 'degrees')
        frequency = c.frequency(ran.main(300), 'MHz')
        
        self.question = f"""What length of standard RG-8/U coaxial cable would be required to obtain a {phasedelay.degrees} degrees phase shift at {frequency.MHz} MHz"""
        
        beta = c.angle(360 / (0.66 * 3e8 / frequency.Hz), 'degrees')
        
        length = c.length(
        (phasedelay.degrees / 360) * ( beta.degrees )
        )
        
        self.answer = f"""Length = {length.m} meters """
        
class jma_3_10:
    def __init__(self,*args,**kwargs): 
        
        zl = c.resistance(ran.main(75))
        zo = ran.main(50) + sym.I * ran.main(25)
        
        self.question = f"""Calculate the magnitude of reflection because of the mismatch between a {zo} ohms line and {sym.pretty(zl.ohms)} ohms load."""
        
        gamma = ((zl.ohms - zo) / (zl.ohms + zo)) 
        
        gamma_abs = sym.Abs(gamma)
        
        self.answer = f"""Reflection coefficient = {gamma_abs}"""
        
class jma_3_11:
    def __init__(self,*args,**kwargs): 
        
        pinc = c.power(ran.main(250))
        pref = c.power(ran.main(45))
        
        self.question = f"""Calculate the SWR & reflection coefficient of the line if the forward power is {pinc.W} W, and the reverse power is {pref.W} W."""
        
        gamma = math.sqrt(pref.W / pinc.W)
        
        swr = (1 + gamma) / (1 - gamma) 
        
        self.answer = f"""Reflection Coefficient = {gamma}
Standing wave ratio = {swr}"""

class jma_3_12:
    def __init__(self,*args,**kwargs): 
        
        zo = c.resistance(ran.main(50))
        zs = c.resistance(ran.main(50))
        zl = c.resistance(ran.main(20))
        
        
        self.question = f"""A coaxial TL with a Zo of {zo.ohms} ohms connected to the {zs.ohms} ohms output of a signal generator, and also to a {zl.ohms} ohms load impedance. Calculate the mismatch loss."""
        
        gamma = (zl.ohms - zo.ohms) / (zl.ohms + zo.ohms)
        mismatch = c.powerGain( 1 - gamma**2)
        
        self.answer = f"""Mismatch Loss =  - {mismatch.dB} dB"""
        
class jma_3_13:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            voltage = c.voltage(ran.main(10))
            length = c.length(ran.main(50))
            zo = c.resistance(ran.main(50))
            vf = ran.main(0.8)
            zl = c.resistance(ran.main(150))
            if vf < 1:
                regen = 0
        self.question = f"""A {voltage.V} V positive going pulse is sent down a {length.m} m of lossless {zo.ohms} ohms cable with a velocity factor of {vf}. The cable is terminated with a {zl.ohms} ohms resistor. Calculate the voltage and current transmission coefficient and the amount of transmitted voltage to the load."""
        
        gamma = (zl.ohms - zo.ohms) / (zl.ohms + zo.ohms)
        voltage_tau = 1 + gamma
        current_tau = 1 - gamma
        voltage_tx = c.voltage(voltage_tau * voltage.V) 
        
        self.answer = f"""Voltage transmission coefficient = {voltage_tau}
Current transmission coefficient = {current_tau}
Voltage transmitted to the load = {voltage_tx.V} V"""

class jma_3_14_a:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            pinc = c.power(ran.main(75), 'mW')
            zo = c.resistance(ran.main(50))
            gamma = ran.main(0.6)
            if gamma < 1:
                regen = 0
            
        
        
        self.question = f"""A generator sends a {pinc.mW} mW down a {zo.ohms} ohms line. The generator is matched to the line, but the load is not. If the coefficient of reflection is {gamma}, how much power is reflected and how much is dissipated in the load?"""
        
        pabs = c.power( pinc.W * ( 1 - gamma**2 ))
        pref = c.power( pinc.W - pabs.W )
        
        self.answer = f"""Power dissipated to the load = {pabs.W} W
Power reflected = {pref.W} W"""

class jma_3_14_b:
    def __init__(self,*args,**kwargs): 
        
        regen = 1
        while regen:
            length = c.length(ran.main(0.12))
            frequency = c.frequency(ran.main(3), 'GHz')
            zo = c.resistance(ran.main(75))
            vf = ran.main(0.65)
            if vf < 1:
                regen = 0
        
        self.question = f"""Calculate the effective inductance seen at the input of an open circuit transmission line of length {length.m} m at {frequency.GHz} GHz. Assume Zo = {zo.ohms} ohms, velocity factor = {vf}."""
        
        beta = (2 * math.pi * frequency.Hz) / ( vf * 3e8 ) 
        zi = - sym.I * zo.ohms * (1 / math.tan( beta * length.m ))
        
        xl = sym.Abs(sym.im(zi))
        l = c.inductance(   xl / (2 * math.pi * frequency.Hz ))
        
        self.answer = f"""Effective inductance = {l.nH} nH"""
        
class jma_3_18:
    def __init__(self,*args,**kwargs): 
        
        zl = ran.main(15) - sym.I * ran.main(20)
        zo = ran.main(50)
        
        self.question = f"""Calculate the voltage reflection coefficient, SWR, and determine the position of the first voltage minimum from the load which has an impedance of ({zl}) ohms. Use Zo = {zo} ohms."""
        
        gamma = sym.simplify(( zl - zo ) / ( zl + zo ))
        swr = (1 + sym.Abs(gamma))  / (1 - sym.Abs(gamma))
        dmin = (sym.arg(gamma) + math.pi) / (4*math.pi)
        
        self.answer = f"""Reflection coefficient = {sym.Abs(gamma)} angle {sym.arg(gamma)} radians
Standing wave ratio = {swr}
Position of the first voltage minimum from the load = {dmin} lambda"""
        
class jma_3_20:
    def __init__(self,*args,**kwargs): 
        
        zl = ran.main(35) - sym.I * ran.main(47.5)
        zo = ran.main(50)
        
        self.question = f"""Determine the relative position of the stub needed to match the load with an impedance of {zl} ohms to a transmission line with a characteristic impedance of {zo} ohms using a shunt, short-circuited single stub tuner."""
        
        xl = sym.im(zl)
        rl = sym.re(zl)
        t1 = (xl   +    math.sqrt(  (rl/zo) * ( (zo - rl)**2 + (xl)**2)  ) ) / (rl - zo)
        
        t2 = (xl   -    math.sqrt(  (rl/zo) * ( (zo - rl)**2 + (xl)**2)  ) ) / (rl - zo)
        
        d1 = (1/(2*math.pi)) * math.atan(t1)
        d2 = (1/(2*math.pi)) * math.atan(t2)
        
        self.answer = f"""Possible positions of the stub: {d1} lambda and {d2} lambda"""
        
class jma_3_21:
    def __init__(self,*args,**kwargs): 
        
        er = ran.main(2)
        width = c.length(ran.main(0.1), 'inch')
        trackthick = c.length(ran.main(5)/1000, 'inch')
        boardthick = c.length(ran.main(75)/1000, 'inch')
        
        self.question = f"""What is the value of Zo for a single {width.inch} in wide, {trackthick.inch} inch track plus groundplane microstrip line? Assume that the PC board is {boardthick.inch} in thick and that the dielectric constant of the board is {er}"""
        
        zo = c.resistance(
        (200 / math.sqrt(er + 1.41)) * math.log((6 * boardthick.inch)/( 0.8 * width.inch + trackthick.inch ),10)
        )
        
        self.answer = f"""Characteristic impedance = {zo.ohms} ohms"""
        
class jma_3_22:
    def __init__(self,*args,**kwargs): 
        
        er = ran.main(1.8)
        boardthick = c.length(ran.main(95)/1000, 'inch')
        trackthick = c.length(ran.main(8)/1000, 'inch')
        width = c.length(ran.main(150)/1000, 'inch')
        distance = c.length(ran.main(200)/1000, 'inch')
        
        self.question = f"""A microstrip line is formed using a {boardthick.inch} inch thick PC board (er = {er}) with a bottom groundplane and a double {width.inch} inch wide, {trackthick.inch} inch thick track on the top separated {distance.inch} inch. What is the characteristic impedance?"""  
        
        zo = c.resistance(
        (276 / math.sqrt(er)) * math.log( (math.pi * distance.inch) / (width.inch + trackthick.inch)  ,10))
        
        self.answer = f"""Characteristic impedance = {zo.ohms} ohms"""
        
class jma_3_23:
    def __init__(self,*args,**kwargs): 
        
        width = c.length(ran.main(150)/1000, 'inch')
        centerthick = c.length(ran.main(5)/1000, 'inch')
        boardthick = c.length(ran.main(50)/1000, 'inch')
        er = ran.main(2)
        
        self.question = f"""A stripline is formed using multilayer board (er = {er}). The center track is {width.inch} inch and {centerthick.inch} inch, and the PC board first layer thickness is {boardthick.inch} inch, with an overall board thickness of twice the single layer. What is the characteristic impedance?"""
        
        zo = c.resistance(
        (138/math.sqrt(er)) * math.log( (2 * 2 * boardthick.inch) / (width.inch * (0.8 + centerthick.inch / boardthick.inch)), 10) )
        
        self.answer = f"""Characteristic impedance = {zo.ohms} ohms"""
        
class jma_3_29_a:
    def __init__(self,*args,**kwargs): 
        
        regen = 1
        while regen:
            width = c.length(ran.main(1.2), 'inch')
            height = c.length(ran.main(0.7), 'inch')
            if width.inch > height.inch:
                regen = 0
        
        self.question = f"""A rectangular wavegude has a width of {width.inch} inches and a height of {height.inch} inches. The waveguide will pass all signals above _______ GHz."""
        
        fc = c.frequency( 3e8 / (2 * width.m))
        
        self.answer = f"""{fc.GHz} GHz"""
        
class jma_3_29_b:
    def __init__(self,*args,**kwargs): 
        
        width = c.length(ran.main(0.6), 'inch')
        
        self.question = f"""A rectangular waveguide has a wdth of {width.inch} inch. Calculate the waveguide cutoff frequency."""
        
        fc = c.frequency(3e8 / (2 * width.m))
        
        self.answer = f"""Cutoff frequency = {fc.GHz} GHz"""
        
class jma_3_29_c:
    def __init__(self,*args,**kwargs): 
        width = c.length(ran.main(1.5), 'inch')
        self.question = f"""Determine the high pass cutoff of a rectangular waveguide which has a broad dimension wall of {width.inch} inches."""
        fc = c.frequency(3e8 / (2 * width.m))
        self.answer = f"""Cutoff frequency = {fc.GHz} GHz"""
        
class jma_3_31:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            length = c.length(ran.main(1.52), 'inch')
            width = c.length(ran.main(0.9), 'inch')
            frequency = c.frequency(ran.main(12), 'GHz')
            wavelength = c.length(3e8 / frequency.Hz )
            vg = c.velocity( 3e8 * math.sqrt(1 - (wavelength.m/(2*width.m))**2))
            vp = c.velocity((3e8)**2 / vg.mpers)
            if length.inch > width.inch and (2*width.m) > wavelength.m:
                regen = 0
                
            
        self.question = f"""Determine the group and phase velocities within a rectangular waveguide with an internal dimension of {length.inch} x {width.inch} inches and is fed by a {frequency.GHz} GHz carrier using a coaxial probe."""
        
 
        
        self.answer = f"""Group velocity = {vg.mpers} m/s
Phase velocity = {vp.mpers}"""

class jma_3_32_a:
    def __init__(self,*args,**kwargs):
        regen = 1
        while regen:
            fc = c.frequency(ran.main(3.75), 'GHz')
            fo = c.frequency(ran.main(5), 'GHz')
            if fo.Hz > fc.Hz:
                regen = 0
        self.question = f"""Calculate the characteristic impedance of a waveguide with a cutoff frequency of {fc.GHz} GHz, at a frequency of {fo.GHz} GHz."""
        zo = c.resistance(
        (120 * math.pi)  / math.sqrt(1 - (fc.Hz / fo.Hz)**2)
        )
        self.answer=f"""Characteristic impedance = {zo.ohms} ohms"""
        
class jma_3_32_b:
    def __init__(self,*args,**kwargs): 
        fo = c.frequency(ran.main(5.6), 'GHz')
        angle = c.angle(ran.main(42), 'degrees')
        self.question = f"""A {fo.GHz} GHz microwave signal is propagated in a waveguide. Assuming that the internal angle of incidence to the waveguide surface is {angle.degrees} degrees. Calculate the wavelength of the signal in the waveguide."""
        vp = c.velocity(3e8 / math.sin(angle.radians))
        guide_wavelength = c.length(vp.mpers / fo.Hz)
        self.answer = f"""Guide wavelength = {guide_wavelength.m} m"""
        

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        