
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

class jma_5_43:
    def __init__(self,*args,**kwargs): 
        
        material = c.relativePermittivity_material()
        
        self.question = f"""Find the characteristic impedance of {material.name}, which has a dielectric constant of {material.relativePermittivity}."""
        
        impedance = c.resistance( 120 * math.pi / math.sqrt(material.relativePermittivity))
        
        self.answer = f"""Characteristic impedance = {impedance.ohms} ohms"""
    
class jma_5_44_a:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            distance = c.length(ran.main(25), 'km')
            efficiency = c.percentage(ran.main(90), 'percent')
            powertx = c.power(ran.main(125), 'W')
            gaintx = 1.64
            if efficiency.percent < 100:
                regen = 0
            
        self.question = f"""Calculate the power density {distance.km} km away from a {efficiency.percent} % efficient halfwave dipole if the transmit power is {powertx.W} W."""
       
        powerdensity = c.powerDensity(
        (powertx.W * gaintx * efficiency.decimal) / (4 * math.pi * distance.m**2)
        )
        
        self.answer = f"""Power density = {powerdensity.nWperm2} nW / m2"""
        
class jma_5_44_b:
    def __init__(self,*args,**kwargs): 
        
        distance = c.length(ran.main(20), 'km')
        distance2 = c.length(distance.km + ran.main(5), 'km')
        powerdensity = c.powerDensity(ran.main(200), 'uWperm2')
        
        self.question = f"""At {distance.km} km in free space from a point source, the power density is {powerdensity.uWperm2} uW/m2. What is the power density {distance2.km} km away from this source?"""
        
        powerdensity2 = c.powerDensity(
        powerdensity.Wperm2 * (distance.m / distance2.m)**2
        )
        
        self.answer = f"""Power density = {powerdensity2.uWperm2} uW/m2."""
        
class jma_5_45_a:
    def __init__(self,*args,**kwargs): 
        
        powertx = c.power(ran.main(100))
        distance = c.length(ran.main(10), 'km')
        
        self.question = f"""Determine the electric field strength {distance.km} km away from a halfwave dipole transmitter with an input power of {powertx.W} W?"""
        
        pd = c.powerDensity( powertx.W / (4 * math.pi * distance.m**2))
        
        e = c.electricField( math.sqrt( pd.Wperm2 * 120 * math.pi))
        
        self.answer = f"""Electric field = {e.mVperm} mV / m"""
        
class jma_5_45_b:
    def __init__(self,*args,**kwargs): 
        
        powertx = c.power(ran.main(100))
        frequency = c.frequency(ran.main(160), 'MHz')
        htx = c.length(ran.main(20))
        hrx = c.length(ran.main(4))
        distance = c.length(ran.main(30), 'km')
        gain = 1.64
        
        self.question = f"""In a VHF mobile radio system, the base station transmits {powertx.W} W at {frequency.MHz} MHz frequency using half-wave dipole antenna {htx.m} meters above the ground. Calculate the field strength at a receiving antenna at a height of {hrx.m} meters and a distance of {distance.km} km. Gain of the half wave dipole antenna is {gain}."""
        
        wavelength = c.length( c.SPEED_OF_LIGHT / frequency.Hz )
        
        eo = c.electricField( math.sqrt(30 * powertx.W * gain) )
        
        e = c.electricField( 
        eo.Vperm *  (( 4 * math.pi * htx.m * hrx.m ) / (wavelength.m * distance.m**2)) ) 
        
        self.answer = f"""Electric field = {e.nVperm} nV/m"""

class jma_5_46:
    def __init__(self,*args,**kwargs): 
        
        powertx = c.power(ran.main(12))
        frequency = c.frequency(ran.main(280), 'MHz')
        txlinelength = c.length(ran.main(10))
        lossper100m = ran.main(3)
        gaintx = c.antennaGain(ran.main(12), 'dBi')
        distance = c.length(ran.main(20), 'km')
        gainrx = c.antennaGain(ran.main(8), 'dBi')
        zo = c.resistance(ran.main(50))
        zl = c.resistance(ran.main(75))
        
        self.question = f"""Calculate the power delivered to the receiver, assuming free-space propagation for a transmitter that has a power output of {powertx.W} W at a carrier frequency of {frequency.GHz} GHz. It is connected by {txlinelength.m} m of a transmission line having a loss of {lossper100m} dB/100m to an antenna with a gain of {gaintx.dBi} dBi. The receiving antenna is {distance.km} km away and has a gain of {gainrx.dBi} dBi. There is negligible loss in the receiver feedline, but the receiver is mismatched; the antenna and line are designed for a {zo.ohms} ohms, but the receiver input is {zl.ohms} ohms."""
        
        wavelength = c.length(3e8 / frequency.Hz)
        fsl = c.powerGain((4 * math.pi * distance.m) / (wavelength.m))
        Ltl = c.powerGain(lossper100m * txlinelength.m /100, 'dB')
        Lm = c.powerGain(1 - ((zl.ohms - zo.ohms)/(zl.ohms + zo.ohms))**2 )
        powerrx = c.power(powertx.dBW + gaintx.dBi + gainrx.dBi - fsl.dB - Ltl.dB - Lm.dB, 'dBW')
        
        self.answer = f"""Received Power = {powerrx.dBW} dBW"""
        
class jma_5_51:
    def __init__(self,*args,**kwargs): 
        
        htx = c.length(ran.main(125))
        frequency = c.frequency(ran.main(1.5), 'MHz')
        itx = c.current(ran.main(8))
        distance = c.length(ran.main(40), 'km')
        hrx = c.length(ran.main(2))
        
        self.question = f"""A {htx.m}-m antenna, transmitting at {frequency.MHz} MHz has an antenna current of {itx.A} A. What field strength and voltage is received by a receiving antenna {distance.km} km away, with a height of {hrx.m} m?"""
        
        wavelength = c.length(3e8 / frequency.Hz)
        e = c.electricField((120 * math.pi * htx.m * itx.A) / (wavelength.m * distance.m))
        
        voltage = c.voltage(e.Vperm * hrx.m)
        
        self.answer = f"""Electric Field = {e.mVperm} mV / m
Received voltage = {voltage.mV} mV"""
        
class jma_5_52:
    def __init__(self,*args,**kwargs): 
        
        htx = c.length(ran.main(600), 'ft')
        hrx = c.length(ran.main(240), 'ft')
        
        self.question = f"""A microwave transmitting antenna is {hrx.ft} feet high. The receive antenna is {hrx.ft} feet high. The maximum transmission distance is _____."""

        distance = c.length( math.sqrt( 2 * htx.ft ) + math.sqrt( 2 * hrx.ft ), 'mi')
        
        self.answer = f"""Maximum transmission distance = {distance.mi} miles"""
        
class jma_5_55:
    def __init__(self,*args,**kwargs): 
        
        fc = c.frequency(ran.main(11.6), 'MHz')
        angle = c.angle(ran.main(70), 'degrees')
        
        self.question = f"""The critical frequency at a particular time is {fc.MHz} MHz. What is the OWF for a transmitting station if the required angle of incidence for propagation to a desired station is {angle.degrees} degrees."""        
        
        muf = c.frequency(fc.Hz / math.cos(angle.radians))
        
        self.answer = f"""Maximum useable frequency = {muf.MHz} MHz"""
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        