import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)


class jma_5_65:
    def __init__(self, *args, **kwargs):
        
        
        d1 = c.length(ran.main(random.choice([2,10,22])), 'miles')
        d2 = c.length(d1.miles + ran.main(15), 'miles')
        
        self.question = f"""Calculate the earth bulge {d1.mi} miles away from a transmitter for a {d2.miles}-mile terrestrial link."""
        
        eb = c.length(
        (d1.miles * (d2.miles - d1.miles)) / (1.5 * (4/3)) , 'feet'
        )
        
        self.answer = f"""Earth bulge = {eb.feet} feet"""
       
       
class jma_5_66:
    def __init__(self, *args, **kwargs):
        
        d1 = c.length(ran.main(10), 'miles')
        d2 = c.length(ran.main(15), 'miles')
        dtotal = c.length(d1.miles + d2.miles, 'miles')
        height_obstruction = c.length(ran.main(100), 'feet')
        k = random.choice([4/3, 1/2, 5/2])
        
        self.question = f"""Calculate the effective height of a {height_obstruction.feet} feet obstruction situated {d1.miles} miles from the receiving end of a {dtotal.miles}-mile radio link for a k-value of {k}"""
        
        he = c.length(
        height_obstruction.feet + ((d1.miles * d2.miles)/(1.5 * k)), 'feet'
        )
        
        self.answer = f"""Effective height = {he.feet} feet"""
        
        
class jma_5_67:
    def __init__(self, *args, **kwargs):
        
        ht = c.length(ran.main(250))
        no = ran.main(312)
        
        self.question = f"""Determine the surface refractivity for a potential microwave site {ht.m} meters above sea level with a sea level surface refractivity of {no} and also calculate the effective earth radius."""
        
        ns = no * math.exp(-0.1057 * ht.km)
        
        re = c.length(
        6400 / (1 - 0.04665 * math.exp(0.005577 * ns)) , 'km'
        )
        
        self.answer = f"""Surface refractivity = {ns}
Effective earth radius = {re.km} km"""

class jma_5_68:
    def __init__(self, *args, **kwargs):
        
        
        hr = c.length(ran.main(100), 'feet')
        ht = c.length(ran.main(60), 'feet')
        
        
        self.question = f"""Calculate the maximum range for a microwave link for which the antenna heights are {ht.feet} feet and {hr.feet} feet."""
        
        distance = c.length(
        math.sqrt(2*ht.feet) + math.sqrt(2*hr.feet) , 'miles'
        )
        
        self.answer = f"""Distance = {distance.miles} miles"""

class jma_5_69:
    def __init__(self, *args, **kwargs):
        
        
        k = 4/3
        d1 = c.length(ran.main(27), 'miles')
        d2 = c.length(ran.main(35-27), 'miles')
        dtotal = c.length(d1.miles + d2.miles, 'miles')
        frequency = c.frequency(ran.main(6), 'GHz')
        htree = c.length(ran.main(40), 'ft')
        hadd = c.length(ran.main(10), 'ft')
        
        
        self.question = f"""Solve for the total height extended in feet for an obstacle situated {d1.mi} miles for a {dtotal.mi}-mile microwave system assuming if tree growth exists, add {htree.ft} ft for trees and {hadd.ft} feet for additional growth. Use {frequency.GHz} GHz and 0.6 F1"""
        
        eb = c.length(
        (d1.miles * d2.miles) / ( 1.5 * k), 'feet' 
        )
        
        wavelength = c.length(
        3e8 / frequency.Hz
        )
        
        f1 = c.length(
        math.sqrt(
        (1 * wavelength.m * d1.m * d2.m) / (d1.m + d2.m)
        )
        )
        
        htotal = c.length(
        eb.feet + 0.6 * f1.feet + hadd.ft + htree.ft, 'feet'
        )
        
        self.answer = f"""Total height extended = {htotal.feet} feet"""
        
class jma_5_70:
    def __init__(self, *args, **kwargs):
        
        d1 = c.length(ran.main(17.5), 'miles')
        d2 = c.length(d1.miles, 'miles')
        
        dtotal = c.length(d1.miles + d2.miles, 'miles')
        frequency = c.frequency(ran.main(12), 'GHz')
        
        wavelength = c.length(
        3e8 / frequency.Hz
        )
        
        f1 = c.length(
        math.sqrt((wavelength.m * d1.m * d2.m) / (dtotal.m))
        )
        
        f5 = c.length(
        f1.m * math.sqrt(5)
        )
        
        self.question = f"""Calculate the 5th Fresnel zone radius to clear a {dtotal.miles} miles radio link operating at {frequency.GHz} GHz if the 1st Fresnel zone radius is {f1.feet} feet."""
        

        
        self.answer = f"""5th Fresnel zone = {f5.feet} feet"""
        
class jma_5_76:
    def __init__(self, *args, **kwargs):
        regen = 1
        while regen:
            frequency = c.frequency(
            ran.main(6.15), 'GHz'
            )
            
            output = c.power(
            ran.main(30), 'dBm'
            )
            
            nf = c.powerGain(
            ran.main(9), 'dB'
            )
            
            pathlength = c.length(
            ran.main(21), 'miles'
            )
            
            antennagain = c.antennaGain(
            ran.main(35), 'dB'
            )
            
            transmissionlosses = c.powerGain(
            ran.main(3), 'dB'
            )
            
            bandwidth = c.frequency(
            ran.main(20), 'MHz'
            )
            
            
            
            self.question = f"""An FM LOS microwave link operates at {frequency.GHz} GHz. The required receiver IF bandwidth is {bandwidth.MHz} MHz. The transmitter output power is {output.dBm} dBm. The receiver front end's first active stage is a mixer with a noise figure of {nf.dB} dB. The path length is {pathlength.mi} miles; the antennas at each end have a {antennagain.dB} dB. If the FM improvement threshold is used as the unfaded reference, what is the reliability of the radio link?"""


            eirp = c.power(
            output.dBm - transmissionlosses.dB + antennagain.dB, 'dBm'
            )
            
            fsl = c.powerGain(
            96.6 + 20 * math.log( frequency.GHz * pathlength.miles , 10), 'dB'
            )
            
            irl = c.power(
            eirp.dBm - fsl.dB, 'dBm'
            )
            
            rsl = c.power(
            irl.dBm + antennagain.dB - transmissionlosses.dB, 'dBm'
            )
            
            noisethreshold = c.power(
            - 174 + 10*math.log(bandwidth.Hz, 10) + nf.dB, 'dBm'
            )
            
            fmit = c.power(
            noisethreshold.dBm + 10, 'dBm'
            )
            
            carriertonoiseratio = c.powerGain(
            rsl.dBm - noisethreshold.dBm, 'dB'
            )
            
            fademargin = c.powerGain(
            rsl.dBm - fmit.dBm, 'dB'
            )
            
            if fademargin.dB > 0:
                regen = 0
            
            if fademargin.dB < 8:
                reliability = interpolation.translate(fademargin.dB, 0, 8, 0, 90)
            if fademargin.dB >= 8 and fademargin.dB < 18:
                reliability = interpolation.translate(fademargin.dB, 8, 18, 90, 99)
            if fademargin.dB >= 18 and fademargin.dB < 28:
                reliability = interpolation.translate(fademargin.dB, 18, 28, 99.9, 99.99)
            if fademargin.dB >= 28 and fademargin.dB < 38:
                reliability = interpolation.translate(fademargin.dB, 28, 38, 99.99, 99.999)
            if fademargin.dB >= 38 and fademargin.dB < 48:
                reliability = interpolation.translate(fademargin.dB, 38, 48, 99.999, 99.9999)
            if fademargin.dB >= 48 and fademargin.dB < 58:
                reliability = interpolation.translate(fademargin.dB, 48, 58, 99.9999, 99.99999)
            if fademargin.dB >= 58:
                reliability = 100
            print('fademargin ' + str(fademargin.dB) + 'dB')
            self.answer = f"""Reliability = {reliability} %"""
            
class jma_5_78:
    def __init__(self, *args, **kwargs):
        
        reliability = round(random.uniform(90, 100),5)
        
        
        self.question = f"""What fade margin is required for a microwave LOS link with a time availability requirements of {reliability}%"""
        
        if reliability < 90:
            fademargin = interpolation.translate(reliability, 0, 90, 0, 8)
        if reliability >= 90  and reliability < 99:
            fademargin = interpolation.translate(reliability, 90, 99, 8, 18)
        if reliability >= 99 and reliability < 99.9:
            fademargin = interpolation.translate(reliability, 99, 99.9, 18, 28)
        if reliability >= 99.9 and reliability < 99.99:
            fademargin = interpolation.translate(reliability, 99.9, 99.99, 28, 38)
        if reliability >= 99.99 and reliability < 99.999:
            fademargin = interpolation.translate(reliability, 99.99, 99.999, 38, 48)
        if reliability >= 99.999 and reliability < 99.9999:
            fademargin = interpolation.translate(reliability, 99.999, 99.9999, 48, 58)
        if reliability >= 99.9999:
            fademargin = 'unrealizeable'
       
        self.answer = f"""Fade margin = {fademargin} dB"""
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        