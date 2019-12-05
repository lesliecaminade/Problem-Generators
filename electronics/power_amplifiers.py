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

class boylestad_12_1:
    def __init__(self,*args,**kwargs): 
        #print('12_1')
        regen = True
        while regen:
            ibac = c.current(ran.main(10), 'mA')
            rb = c.resistance(ran.main(1000), 'ohms')
            rc = c.resistance(ran.main(20), 'ohms')
            beta = ran.main(25)
            vcc = c.voltage(ran.main(20))
            
            self.question = f"""Calculate the input power, output power, and efficiency of the amplifier circuit for an input voltage that results in a base current of {ibac.mA} mA peak, RB = {rb.ohms} ohms, and RC = {rc.ohms} ohms, beta = {beta}, and a VCC = {vcc.V} V. https://lesliecaminadecom.files.wordpress.com/2019/06/nt6zf378m6984qens2wa.png"""
            
            ib = c.current((vcc.V - 0.7)/rb.ohms)
            ic = c.current(beta*ib.A)
            vce = c.voltage(vcc.V - ic.A * rc.ohms)
            if vce.V > 0:
                regen = False
                
        icac = c.current(beta*ibac.A)
        
        pac = c.power( (icac.A**2/2) * rc.ohms)
        
        pdc = c.power( vcc.V * ic.A )
        
        efficiency = c.percentage(pac.W / pdc.W, 'decimal')
        
        self.answer = f"""Input power = {pdc.W} W
Output power = {pac.W} W
Efficiency = {efficiency.percent} %"""

class boylestad_12_2:
    def __init__(self,*args,**kwargs): 
        #print('12_2')
        turnsratio = ran.main(15, 'int')
        rload = c.resistance(ran.main(8))
        
        self.question = f"""Calculate the effective resistance seen looking into the primary of a {turnsratio} : 1 transformer connected to a/an {rload.ohm}-ohm load."""
        
        reff = c.resistance( turnsratio**2 * rload.ohms)
        
        self.answer = f"""Effective resistance = {reff.ohms} ohms"""
        
class boylestad_12_3:
    def __init__(self,*args,**kwargs): 
        #print('12_3')
        rload = c.resistance(ran.main(16), 'ohms')
        reff = c.resistance(ran.main(10), 'kohms')
        
        self.question  = f"""What transformer turns ratio is required to match a {rload.ohm}-ohm speaker load so that the effective load resistance seen at the primary is {reff.ohms} ohms?"""

        turnsratio = math.sqrt(reff.ohms/rload.ohms)
        
        self.answer = f"""Turns ratio = {turnsratio}"""
        
class boylestad_12_6:
    def __init__(self,*args,**kwargs): 
        #print('12_6')
        regen = True
        while regen:
            supply  = c.voltage(ran.main(12))
            vps = [12,6,2]
            vp1 = random.sample(vps, 1)
            vp = c.voltage(vp1[0])
            
            
            self.question = f"""Calculate the efficiency of a transformer coupled class A amplifier for a supply of {supply.V} V and output of V(p) = {vp.V} V."""
            
            if supply.V > vp.V:
                regen = False
        
        
        vcemax = c.voltage(supply.V + vp.V)
        vcemin = c.voltage(supply.V - vp.V)
        
        efficiency = c.percentage(50 * (
        (vcemax.V - vcemin.V) / 
        (vcemax.V + vcemin.V)
        ), 'percent' )
        
        self.answer = f"""Efficiency = {efficiency.percent} %"""
        
class boylestad_12_7:
    def __init__(self,*args,**kwargs): 
        #print('12_7')
        vloadpeak = c.voltage(ran.main(20))
        rload = c.resistance(ran.main(16))
        vcc = c.voltage(vloadpeak.V + ran.main(10))
        
        self.question = f"""For a class B amplifier providing a {vloadpeak.V}-V peak signal to {rload.ohms}-ohm load (speaker) and a power supply of VCC = {vcc.V} V, determine the input power, output power, and circuit efficiency."""

        iloadpeak = c.current(vloadpeak.V / rload.ohms)
        
        iloaddc  = c.current((2/math.pi) * iloadpeak.A)
        
        powerdc = c.power(vcc.V * iloaddc.A)
        
        powerac = c.power(vloadpeak.V**2 / (2 * rload.ohms))
        
        efficiency = c.percentage( powerac.W / powerdc.W, 'decimal')
        
        self.answer = f"""Input Power = {powerdc.W} W
Output Power = {powerac.W} W
Efficiency = {efficiency.percent} %"""

class boylestad_12_8:
    def __init__(self,*args,**kwargs): 
        #print('12_18')
        vcc = c.voltage(ran.main(30))
        rload = c.resistance(ran.main(16))
        
        self.question = f"""For a class B amplifier using a supply of VCC = {vcc.V} V and driving a load of {rload.ohms} ohms, determine the maximum input power, output power, and transistor dissipation."""
        
        maxpowerac = c.power( vcc.V**2 / (2 * rload.ohms) )
        
        maxpowerdc = c.power( ( 2 * vcc.V**2 ) / ( math.pi * rload.ohms) )
        
        efficiency = c.percentage( maxpowerac.W / maxpowerdc.W , 'decimal')
        
        maximumtrans = c.power(0.5 * ((2 * vcc.V**2)/(math.pi**2 * rload.ohms)))
        
        self.answer = f"""Maximum AC power  = {maxpowerac.W} W
Maximum DC power = {maxpowerdc.W} W
Maximum transistor power (1 transistor) = {maximumtrans.W} W"""

class boylestad_12_9:
    def __init__(self,*args,**kwargs): 
        #print('12_9')
        regen = True
        while regen:
            vcc = c.voltage(ran.main(24))
            list = [22,6]
            selected = random.sample(list,1)
            vloadpeak = c.voltage(ran.main(selected[0]))
            
            
            self.question = f"""Calculate the efficiency of a class B amplifier for a supply voltage of VCC = {vcc.V} V with peak output voltage of VL(p) = {vloadpeak.V} V"""
            
            if vcc.V > vloadpeak.V:
                regen = False
        
        efficiency = c.percentage(78.54 * (vloadpeak.V / vcc.V), 'percent')
        
        self.answer = f"""Efficiency = {efficiency.percent} percent"""
        
class boylestad_12_10:
    def __init__(self,*args,**kwargs): 
        #print('12_10')
        regen = True
        while regen:
            vinrms = c.voltage(ran.main(12))
            rload = c.resistance(ran.main(4))
            vcc = c.voltage(ran.main(25))
            
            
            self.question = f"""For a complementary push-pull amplifier, Calculate the input power, output power and the circuit efficiency for an input of {vinrms.V} Vrms. The load resistance is RL = {rload.ohms} ohms and the supply voltages are VCC = - VEE = {vcc.V} V.https://lesliecaminadecom.files.wordpress.com/2019/06/mmiulq3gvrfa34xeai6a.png""" 
            
            if vcc.V > vinrms.V:
                regen = False
        
        vinpeak = c.voltage(math.sqrt(2)*vinrms.V)
        vloadpeak = c.voltage(vinpeak.V)
        powerac = c.power(vloadpeak.V**2 / (2*rload.ohms))
        iloadpeak = c.current(vloadpeak.V / rload.ohms)
        iloaddc = c.current((2/math.pi)*iloadpeak.A)
        powerdc = c.power(vcc.V*iloaddc.A)
        powertrans = c.power((powerdc.W - powerac.W)/2)
        efficiency = c.percentage(powerac.W / powerdc.W, 'decimal')
        
        self.answer = f"""Input power = {powerdc.W} W
Output power = {powerac.W} W
Efficiency = {efficiency.percent} percent"""

class boylestad_12_11:
    def __init__(self,*args,**kwargs): 
        #regen = True
        #while regen:
            #vinrms = c.voltage(ran.main(12))
        #print('12_11')
        rload = c.resistance(ran.main(4))
        vcc = c.voltage(ran.main(25))
        
        self.question = f"""For a complementary push-pull amplifier, Calculate the maximum input power, maximum output power, input voltage for maximum power operation, and power dissipated by the output transistors at this voltage. The load resistance is RL = {rload.ohms} ohms and the supply voltages are VCC = - VEE = {vcc.V} V..https://lesliecaminadecom.files.wordpress.com/2019/06/mmiulq3gvrfa34xeai6a.png""" 
            
            #if vcc.V > vinrms.V:
                #regen = False
                
        maxpowerdc = c.power((2 * vcc.V**2) /(math.pi * rload.ohms))
        
        maxpowerac = c.power((vcc.V**2)/(2 * rload.ohms))
        
        efficiency = c.percentage(maxpowerac.W / maxpowerdc.W)
        
        vinput = c.voltage(vcc.V)
        
        powertrans = c.power(maxpowerdc.W - maxpowerac.W)
        
        self.answer = f"""Max input power = {maxpowerdc.W} W
Max output power = {maxpowerac.W} W
Input voltage for max power  = {vinput.V} V
Power dissipated by transistors = {powertrans.W} W"""

class boylestad_12_12:
    def __init__(self,*args,**kwargs): 
        #print('12_12')
        #vinrms = c.voltage(ran.main(12))
        rload = c.resistance(ran.main(4))
        vcc = c.voltage(ran.main(25))
        
        self.question = f"""For a complementary push-pull amplifier, Calculate the maximum power dissipated by the output transistors and the input voltage at which this occurs. The load resistance is RL = {rload.ohms} ohms and the supply voltages are VCC = - VEE = {vcc.V} V..https://lesliecaminadecom.files.wordpress.com/2019/06/mmiulq3gvrfa34xeai6a.png""" 
        
        maxpowertrans = c.power((2 * vcc.V**2) / (math.pi**2 * rload.ohms))
        
        vinput = c.voltage( (2 / math.pi) * vcc.V)
        
        self.answer = f"""Max power dissipated (2 transistors) = {maxpowertrans.W} W
This maximum dissipation occurs at vin = {vinput.V} V"""

class boylestad_12_13:
    def __init__(self,*args,**kwargs): 
        #print('12_13')
        a1 = c.voltage(ran.main(2.5))
        a2 = c.voltage(ran.main(0.25))
        a3 = c.voltage(ran.main(0.1))
        a4 = c.voltage(ran.main(0.05))
        
        self.question = f"""Calculate the harmonic distortion components and the THD for an output signal having fundamental amplitude of {a1.V} V, second harmonic amplitude of {a2.V} V, third harmonic amplitude of {a3.V} V, and fourth harmonic amplitude of {a4.V}V."""
        
        d2 = c.percentage(a2.V / a1.V, 'decimal')
        d3 = c.percentage(a3.V / a1.V, 'decimal')
        d4 = c.percentage(a4.V / a1.V, 'decimal')
        
        thd = c.percentage(math.sqrt(d2.decimal**2 + d3.decimal**2 + d4.decimal**2), 'decimal')
        
        self.answer = f"""Components = {d2.percent} %, {d3.percent} %, {d4.percent} %
THD = {thd.percent} %"""

class boylestad_12_15:
    def __init__(self,*args,**kwargs): 
        #print('12_15')
        regen = True
        while regen:
            temp = random.randint(0,1)
            
            if temp == 0:
                vcemin = c.voltage(1)
                vcemax = c.voltage(22)
                vce = c.voltage(12)
                
            if temp == 1:
                vcemin = c.voltage(4)
                vcemax = c.voltage(20)
                vce = c.voltage(12)
                
            if vcemin.V < vce.V and vcemax.V > vce.V:
                regen = False
            
        
        
        self.question = f"""Calculate the second harmonic distortion if an output waveform displayed on an oscilloscope provides the measurements VCEmin = {vcemin.V} V, VCEmax = {vcemax.V} V, VCEQ = {vce.V} V."""
        
        d2 = c.percentage(
        abs(
        (0.5*(vcemax.V + vcemin.V) - vce.V) / 
        (vcemax.V - vcemin.V)
        )
        )
        
        self.answer = f"""Second harmonic distortion = {d2.percent} %"""
        
class boylestad_12_16:
    def __init__(self,*args,**kwargs): 
        #print('12_16')
        d2 = c.percentage(ran.main(0.1), 'decimal')
        d3 = c.percentage(ran.main(0.02, 'noround'), 'decimal')
        d4 = c.percentage(ran.main(0.01, 'noround'), 'decimal')
        i1 = c.current(ran.main(4))
        rc = c.resistance(ran.main(8))
        
        self.question = f"""For a harmonic distortion reading of D2 = {d2.decimal}, D3 = {d3.decimal} and D4 = {d4.decimal} with I1 = {i1.A} A and RC = {rc.ohms} ohms, calculate the total harmonic distortion, fundamental power component and total power."""

        thd = c.percentage(
        math.sqrt( d2.decimal**2 + d3.decimal**2 + d4.decimal**2
        ) , 'decimal'
        )
        
        fundpower = c.power(
        (i1.A**2 * rc.ohms) / 2
        )
        
        totalpower = c.power(( 1 + thd.decimal**2 ) *fundpower.W)
        
        self.answer = f"""Total harmonic distortion (THD) = {thd.percent} %
Fundamental power = {fundpower.W} W
Total power = {totalpower.W} W"""


class boylestad_12_17:
    def __init__(self,*args,**kwargs): 
        #print('12_17')
        power1 = c.power(ran.main(80))
        temp1 = c.temperature(ran.main(25), 'C')
        temp2 = c.temperature(ran.main(125), 'C')
        derating = c.power(ran.main(0.5))
        
        self.question = f"""Determine what maximum dissipation will be allowed for an {power1.W}-W silicon transistor (rated at {temp1.C}degC) if derating is required above {temp1.C}degC by a derating factor of {derating.W} W/degC at a case temperature of {temp2.C} degC."""
        
        power2 = c.power(
        power1.W - (temp2.C - temp1.C)*(derating.W)
        )
        
        self.answer = f"""Dissipation allowed at {temp2.C}degC = {power2.W} W"""
        
class boylestad_12_18:
    def __init__(self,*args,**kwargs): 
        #print('12_18')
        sinkambient = c.thermalResistance(ran.main(1.5))
        power = c.power(ran.main(150))
        ratedtransistortemp = c.temperature(ran.main(25), 'C')
        junctioncase = c.thermalResistance(ran.main(0.5))
        casesink = c.thermalResistance(ran.main(0.6))
        ambienttemp = c.temperature(ran.main(40), 'C')
        junctiontempmax = c.temperature(ran.main(200), 'C')
        
        
        
        self.question = f"""A silicon power transistor is operated with a heat sink (theta(sink-ambient) = {sinkambient.CperW} degC/W). The transistor, rated at {power.W} W ({ratedtransistortemp.C} degC) , has theta(junction-case) = {junctioncase.CperW} degC/W, and the mounting insulation has theta(case-sink) = {casesink.CperW} degC/W. What maximum power can be dissipated if the ambient temperature if {ambienttemp.C} degC and Tjmax = {junctiontempmax.C} degC?""" 
        
        powerdissipated = c.power(
        (junctiontempmax.C - ambienttemp.C) / 
        (junctioncase.CperW + casesink.CperW + sinkambient.CperW)
        )
        
        self.answer = f"""Power dissipated = {powerdissipated.W} W"""
        

        
        
        
        
        


        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        