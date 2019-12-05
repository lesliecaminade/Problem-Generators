from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c

x, y, z = sym.symbols('x y z', real = True)#generic variables

#fewson
class fewson_2_1:
    def __init__(self,*args,**kwargs): 
        print('21')
        regen = True
        while regen:
            i = random.randint(0,1)
            ton_list = [1,3]
            ton = c.time(ran.main(ton_list[i]), 'ms')
            vsource = c.voltage(ran.main(48))
            rload = c.resistance(ran.main(24))
            freq = c.frequency(ran.main(350))
            
            self.question = f"""A dc to dc chopper operates from a {vsource.V} V battery source into a resistive load of {rload.ohms} ohms. The frequency of the chopper is set to {freq.Hz} Hz. Determine the average and rms load current and the load power values when chopper on time is {ton.ms} ms."""
            
            period = c.time(1/freq.Hz)
            print('period' + str(period.ms))
            print('ton' + str(ton.ms))
            if period.ms > ton.ms:
                regen = False
        
        vaverage = c.voltage(vsource.V * freq.Hz * ton.s )
        iaverage = c.current(vaverage.V / rload.ohms)
        vrms = c.voltage( vsource.V * math.sqrt(freq.Hz * ton.s))
        irms = c.current( vrms.V / rload.ohms )
        powerP = c.power( irms.A**2 * rload.ohms )
        
        self.answer = f"""I(ave) = {iaverage.A} A
I(rms) = {irms.A} A
Real Power = {powerP.W} W"""

class fewson_2_2:
    def __init__(self,*args,**kwargs): 
        print('22')
        regen = True
        while regen:
            rload = c.resistance(ran.main(1))
            lload = c.inductance(ran.main(10), 'mH')
            vsource = c.voltage(ran.main(24))
            frequency = c.frequency(ran.main(100))
            ton = c.time(ran.main(5), 'ms')
            
            self.question = f"""A dc to dc chopper has an inductive load of {rload.ohms} ohms resistance and {lload.mH} mH inductance. Source voltage is {vsource.V} V. The frequency of the chopper is set to {frequency.Hz} Hz and the on-time to {ton.ms} ms. Determine the average, maximum, minimum, and RMS load currents."""
            
            period = c.time(1/frequency.Hz)
            if period.s > ton.s:
                regen = False
        
        toff = c.time(period.s - ton.s)
        
        vaverage = c.voltage( vsource.V * frequency.Hz * ton.s )
        iaverage = c.current( vaverage.V / rload.ohms )
        #y is I1, x is Io
        equation1 = sym.Eq(
        y,
        (vsource.V / rload.ohms) * (1 - math.exp(-rload.ohms * ton.s / lload.H)) + x * math.exp( - rload.ohms * ton.s / lload.H )
        )
        
        equation2 = sym.Eq(
        x,
        y * math.exp(- rload.ohms * toff.s / lload.H)
        )
        
        equation_list = [equation1, equation2]
        solution_set = sym.linsolve(equation_list, x, y)
        solution_list = list(solution_set.args[0])
        print(solution_list)
        i0 = c.current(solution_list[0])
        i1 = c.current(solution_list[1])
        print(i0.A)
        print(i1.A)
        i_of_t_charge = (vsource.V/rload.ohms) * (1 - sym.exp(-rload.ohms * x/lload.H)) + (i0.A * sym.exp(- rload.ohms * x / lload.H ))
        
        #print(pretty(i_of_t_charge))
        
        i_of_t_discharge = i1.A * sym.exp(-rload.ohms * x / lload.H)
        
        
        
        irms = c.current(
        math.sqrt(
        (1/period.s) * (sym.integrate(i_of_t_charge**2, (x, 0, ton.s)) + sym.integrate(i_of_t_discharge**2, (x, 0, toff.s))
        )
        )
        )
        
        
        self.answer = f"""Average Current = {iaverage.A} A
Maximum Current = {i1.A} A
Minimum Current = {i0.A} A
RMS Current = {irms.A} A"""

class fewson_2_3:
    def __init__(self,*args,**kwargs): 
        print('23')
        regen = True
        while regen:
        
            vbattery = c.voltage(ran.main(96))
            rarf = c.resistance(ran.main(100), 'mohms')
            kv = c.voltage(ran.main(10), 'mV')
            frequency = c.frequency(ran.main(125))
            period = c.time(1/frequency.Hz)
            ton = c.time(ran.main(6), 'ms')
            ia = c.current(ran.main(100))
            toff = c.time(period.s - ton.s)
            
            torque2 = c.torque(ran.main(10))
            
            self.question = f"""A dc series chopper drive has the following parameters: Battery voltage = {vbattery.V} V, (Ra + Rf) = {rarf.ohms} ohms, kv = {kv.mV} mV / Arad/s , chopper frequency = {frequency.Hz} Hz. a) Calculate the armature speed and torque with an average armature current of {ia.A} A and a chopper on time of {ton.ms} ms. b) Determine the motor speed and armature current at a torque of {torque2.Nm} Nm with on time and off time similar to situation a."""
            
            if period.s > ton.s:
                regen = False
        
        vaverage = c.voltage( vbattery.V * ton.s * frequency.Hz )
        backemf = c.voltage( vaverage.V - ia.A * rarf.ohms )
        omega = c.angularVelocity( backemf.V / (kv.V * ia.A) , 'radpers')
        torque = c.torque( kv.V * ia.A**2 )
        
        ia2 = c.current( math.sqrt( torque2.Nm * kv.V ))
        backemf2 = c.voltage( vaverage.V - ia2.A * rarf.ohms )
        omega2 = c.angularVelocity( backemf2.V / (kv.V * ia2.A) , 'radpers')
        
        self.answer = f"""Armature speed and Torque at a) = {omega.revpermin} rev/min, {torque.Nm} Nm
Motor speed and Armature current at b) = {omega2.revpermin} rev/min, {ia2.A} A"""

class fewson_2_4:
    def __init__(self,*args,**kwargs): 
        print('24')
        iload = c.current(ran.main(3))
        rload = c.resistance(ran.main(10))
        vbattery = c.voltage(ran.main(12))
        lchopper = c.inductance(ran.main(20), 'uH')
        cchopper = c.capacitance(ran.main(100), 'uF')
        frequency = c.frequency(ran.main(50), 'kHz')
        
        
        self.question = f"""A stepup chopper is to deliver {iload.A} A into the {rload.ohms} ohms load. The battery voltage is {vbattery.V} V , L = {lchopper.uH} uH, C = {cchopper.uF} uF, and the chopper frequency is {frequency.kHz} kHz. Determine the on-time of the chopper, the battery current variation, and the average battery current."""
        
        vload = c.voltage(iload.A * rload.ohms)
        dutycycle = c.percentage( 1 - (vbattery.V / vload.V) , 'decimal')
        period = c.time(1/frequency.Hz)
        ton = c.time(dutycycle.decimal * period.s)
        deltai = c.current( vbattery.V * ton.s / lchopper.H )
        
        ibattery = c.current(iload.A / (1 - dutycycle.decimal))
        ibmax = c.current( ibattery.A + deltai.A/2)
        ibmin = c.current( ibattery.A - deltai.A/2)
        
        self.answer = f"""Chopper on - time = {ton.us} us
Average Battery Current = {ibattery.A} A
Maximum Battery Current = {ibmax.A} A
Minimum Battery Current = {ibmin.A} A"""

class fewson_2_5:
    def __init__(self,*args,**kwargs): 
        print('25')
        toff = c.time(ran.main(20), 'us')
        vbattery = c.voltage(ran.main(96))
        iload = c.current(ran.main(100))
        
        self.question = f"""What value of capacitor is required to force commutate a thyristor with a turnoff time of {toff.us} us with a {vbattery.V} V and a full load current of {iload.A} A?"""

        capacitor = c.capacitance(1.43 * toff.s * iload.A / vbattery.V)
        
        self.answer = f"""Capacitance required = {capacitor.uF} uF"""
        
class fewson_3_1:
    def __init__(self,*args,**kwargs): 
        print('31')
        vsourceRMS = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        rload = c.resistance(ran.main(100))
        alpha_list = [30, 140, 120]
        i = random.randint(0,2)
        alpha = c.angle(ran.main(alpha_list[i]), 'degrees')
        
        self.question = f"""A thyristor half-wave half controlled converter has a supply voltage of {vsourceRMS.V} V at {frequency.Hz} Hz and a load resistance of {rload.ohms} ohms. What are the average values of load voltage and current when the firing delay angle is {alpha.degrees} degrees?"""
        
        if alpha.degrees > 180:
            alpha = c.angle(180, 'degrees')
            
        vaverage = c.voltage(
        ((math.sqrt(2) * vsourceRMS.V) / (2*math.pi)) * ( 1 + math.cos(alpha.radians))
        )
        
        iaverage = c.current(vaverage.V / rload.ohms) 
        
        vrms = c.voltage(
        (1/(2*math.pi)) * sym.integrate((vsourceRMS.V * math.sqrt(2) * sym.sin(x))**2, (x, alpha.radians, sym.pi))
        )
        
        irms = c.current(vrms.V / rload.ohms)
        
        powerP = c.power( irms.A**2 * rload.ohms )
        
        pf = float(powerP.W / (vsourceRMS.V * irms.A))
        
        
        self.answer = f"""V average = {vaverage.V} V
I average = {iaverage.A} A
V rms = {vrms.V} V
I rms = {irms.A} A
Power Factor = {pf}"""

class fewson_3_3:
    def __init__(self,*args,**kwargs): 
        print('33')
        regen = True
        while regen:
            regen = False
            capacitance = c.capacitance(ran.main(100), 'nF')
            rlow = c.resistance(ran.main(10), 'kohms')
            rhigh = c.resistance(ran.main(120), 'kohms')
            frequency = c.frequency(ran.main(50))
            vsourcerms = c.voltage(ran.main(240))
            
            self.question = f"""In the circuit, C = {capacitance.nF} nF and R is variable from {rlow.kohms} kohms to {rhigh.kohms} kohms. Determine the range of the firing delay angle available. The ECG6412 hs a breakdown voltage of 63 V.
            https://lesliecaminadecom.files.wordpress.com/2019/06/9kg2vb0qwvu54wpuz28a.png"""

            xc = c.resistance( 1 / (2*math.pi*frequency.Hz*capacitance.F))
            vm = c.voltage(math.sqrt(2) * vsourcerms.V )
            
            #for rlow
            zlow = c.resistance( math.sqrt( rlow.ohms**2 + xc.ohms**2 ) )
            philow = c.angle( math.atan(xc.ohms / rlow.ohms) , 'radians' )
            
            try:
                omegat_phi_90 = c.angle( 
                math.asin(63 / (vm.V * xc.ohms / zlow.ohms )) , 'radians')


        
                alphalow = c.angle( omegat_phi_90.radians - philow.radians + math.pi/2 , 'radians')
                
                #for rhigh
                zhigh = c.resistance( math.sqrt( rhigh.ohms**2 + xc.ohms**2 ) )
                phihigh = c.angle( math.atan(xc.ohms / rhigh.ohms) , 'radians' )
            

                omegat_phi_90 = c.angle( 
                math.asin(63 / (vm.V * xc.ohms / zhigh.ohms )) , 'radians'
                )

                alphahigh = c.angle( omegat_phi_90.radians - phihigh.radians + math.pi/2 , 'radians')
        
                self.answer = f"""Firing angle range: {alphalow.degrees} deg to {alphahigh.degrees} deg."""
            except:
                regen = True
        
class fewson_3_4:
    def __init__(self,*args,**kwargs): 
        print('34')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(220))
            frequency = c.frequency(ran.main(50))
            alpha = c.angle(ran.main(90), 'degrees')
            rload = c.resistance(ran.main(100))
            rload2 = c.resistance(ran.main(100))
            
            self.question = f"""A full - wave half controlled bridge has a supply voltage of {vsourcerms.V} V at {frequency.Hz} Hz. The firing angle delay alpha = {alpha.degrees} degrees. Determine the values of average and rms currents, load power, and power factor for a a) resistive load of R = {rload.ohms} ohms, b) a highly inductive load with a resistance of R = {rload2.ohms} ohms."""
            
            if alpha.radians < math.pi:
                regen = False
        
        #for a
        vave = c.voltage(
        (1 / math.pi ) * sym.integrate(vsourcerms.V * math.sqrt(2) * sym.sin(x), (x, alpha.radians, sym.pi))
        )
        
        iave = c.current(vave.V / rload.ohms )
        
        vave = c.voltage(math.sqrt(
        (1 / math.pi ) * sym.integrate((vsourcerms.V * math.sqrt(2) * sym.sin(x))**2, (x, alpha.radians, sym.pi)))
        )
        
        irms = c.current(vsourcerms.V / rload.ohms )
        
        powerP = c.power(irms.A**2 * rload.ohms )
        powerS = c.power(vsourcerms.V * irms.A )
        pf = powerP.W / powerS.W
        
        #for b
        iaveb = c.current(iave.A)
        irmsb = c.current( iave.A * math.sqrt((math.pi - alpha.radians)/(math.pi)))
        powerPb = c.power( iave.A**2 * rload.ohms )
        powerSb = c.power( vsourcerms.V * irms.A )
        pfb = powerP.W / powerS.W
        
        
        self.answer = f"""For situation A:
IAVE = {iave.A} A, IRMS = {irms.A} A, Load power = {powerP.W} W, power factor = {pf}

For situation B:
IAVE = {iaveb.A} A, IRMS = {irmsb.A} A, Load power = {powerPb.W} W, power factor = {pfb}"""

class fewson_3_5:
    def __init__(self,*args,**kwargs): 
        print('35')
        regen = True
        while regen:
            rload = c.resistance(ran.main(55))
            vsourcerms = c.voltage(ran.main(110))
            frequency = c.frequency(ran.main(50))
            alpha = c.angle(ran.main(75), 'degrees')
            
            self.question = f"""A full - wave fully controlled bridge has a highly inductive load with a resistance of {rload.ohms} ohms, and a supply voltage of {vsourcerms.V} V at {frequency.Hz} Hz. a) Calculate the values of load current, power, and converter power factor for a firing delay angle of {alpha.degrees} degrees."""
            
            if alpha.radians < math.pi:
                regen = False
        
        vave = c.voltage(
        (2*vsourcerms.V * math.sqrt(2) /math.pi ) * math.cos(alpha.radians)
        )
        
        iave = c.current(vave.V / rload.ohms)
        
        powerP = c.power( iave.A**2 * rload.ohms )
        
        pf = 0.9 * math.cos( alpha.radians )
        
        self.answer = f"""Load current = {iave.A} A, 
Power = {powerP.W} W
Power Factor = {pf}"""

class fewson_3_6:
    def __init__(self,*args,**kwargs): 
        print('36')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(240))
            frequency = c.frequency(ran.main(50))
            rload = c.resistance(ran.main(50))
            alpha = c.angle(ran.main(75), 'degrees')
            
            self.question = f"""A {vsourcerms.V} V,  {frequency.Hz} Hz supply feeds a highly inductive load of {rload.ohms} ohms resistance through a thyristor bridge that is a) half controlled and b) full controlled. Calculate the load current, power, and power factor for each case when the firing angle delay is {alpha.degrees} degrees."""
            
            if alpha.degrees < 180:
                regen = False
        
        #for a
        vave = c.voltage(
        ( vsourcerms.V * math.sqrt(2) / math.pi ) * ( 1 + math.cos(alpha.radians)) 
        )
        
        iave = c.current( vave.V / rload.ohms )
        
        irms = c.current( iave.A * math.sqrt( (math.pi - alpha.radians) / (math.pi)    ))
        
        powerP = c.power( irms.A**2 * rload.ohms )
        powerS = c.power( vsourcerms.V * irms.A )
        pf = powerP.W / powerS.W
        
        #forb
        vaveb = c.voltage(
        ( 2 * vsourcerms.V * math.sqrt(2) / math.pi ) * math.cos(alpha.radians) 
        )
        
        iaveb = c.current( vave.V / rload.ohms )
        
        irmsb = c.current( iave.A )
        
        powerPb = c.power( irms.A**2 * rload.ohms )
        #powerSb = c.power( vsourcerms.V * irms.A )
        pfb = 0.9 * math.cos(alpha.radians)
        
        
        self.answer = f"""For situation A:
Load current = {irms.A} A
Power = {powerP.W} W
Power Factor = {pf}

For situation B:
Load current = {irmsb.A} A
Power = {powerPb.W} W
Power Factor = {pfb}"""


class fewson_3_7:
    def __init__(self,*args,**kwargs): 
        print('37')
        regen = True
        while regen:
            regen2 = True
            while regen2:
                vsourcerms = c.voltage(ran.main(240))
                frequency = c.frequency(ran.main(50))
                ra = c.resistance(ran.main(1000), 'mohms')
                kv = c.voltage(ran.main(800), 'mV')
                speed = c.angularVelocity(ran.main(1600), 'revpermin')
                alpha = c.angle(ran.main(30), 'degrees')
                
                self.question = f"""A separately excited dc motor is driven from a {vsourcerms.V} V, {frequency.Hz} Hz supply using a fully controlled thyristor bridge. The motor has an armature resistance Ra = {ra.ohms} ohms and an armature voltage constant kv of {kv.V} V/rad s . The field current is constant at its rated value. Assume that the armature current is steady. a) Determine the values of armature current and torque for an armature speed of {speed.revpermin} rev/min and a firing angle of {alpha.degrees} degrees. b) Calculate the limits of the firing delay for this speed."""
            
                eb = c.voltage(kv.V * speed.radpers )
                vave = c.voltage( (2 * vsourcerms.V / math.pi) * math.cos(alpha.radians))
                
                if vave.V > eb.V:
                    regen2 = False

            iave = c.current(
            (vave.V - eb.V) / ra.ohms
            )
            
            torque = c.torque( kv.V * iave.A )
            
            alphalow = c.angle(
            math.asin(  eb.V / ( vsourcerms.V * math.sqrt(2)) ), 'radians'
            )
            
            alphahigh = c.angle(
            math.pi - math.asin(  eb.V / ( vsourcerms.V * math.sqrt(2)) ), 'radians'
            )
            
            if vave.V > eb.V and alpha.degrees > alphalow.degrees and alpha.degrees < alphahigh.degrees:
                regen = False
        
        self.answer =f"""Armature current = {iave.A} A
Torque = {torque.Nm} Nm
Lowest firing angle = {alphalow.degrees} degrees
Highest firing angle = {alphahigh.degrees} degrees"""

class fewson_3_8:
    def __init__(self,*args,**kwargs): 
        print('38')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(240))
            frequency = c.frequency(ran.main(50))
            ra = c.resistance(ran.main(1000), 'mohms')
            kv = c.voltage(ran.main(800), 'mV')
            speed = c.angularVelocity(ran.main(1600), 'revpermin')
            alpha_list = [30,60]
            alpha_i = random.randint(0,len(alpha_list)-1)
            alpha = c.angle(alpha_list[alpha_i], 'degrees')
            
            self.question = f"""A separately excited dc motor is driven from a {vsourcerms.V} V, {frequency.Hz} Hz supply using a half controlled thyristor bridge with a flywheel diode connected across the armature. The motor has an armature resistance Ra of {ra.ohms} ohms, and an armature voltage constant kv of {kv.V} V/rad/s. The field current is constant at its rated value. Assume that the armature current is steady. Determin the values of armauture current and torque for an armature speed of {speed.revpermin} rev/min and a firing delay angle of {alpha.degrees} degrees."""

            eb = c.voltage( kv.V * speed.radpers )
            vave = c.voltage( (math.sqrt(2) * vsourcerms.V / math.pi) * (1 + math.cos(alpha.radians)) ) 
        
            if vave.V > eb.V:
                regen = False
        
        iave = c.current((vave.V - eb.V) / ra.ohms)
        
        torque = c.torque( kv.V * iave.A )
        
        self.answer = f"""Armature current = {iave.A} A
Torque = {torque.Nm} Nm"""

class fewson_3_9:
    def __init__(self,*args,**kwargs): 
        print('39')
        rload = c.resistance(ran.main(10))
        vsourcerms = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        alpha_list = [30, 75]
        alpha_i = random.randint(0,len(alpha_list)-1)
        alpha = c.angle(alpha_list[alpha_i], 'degrees')
        
        self.question = f"""A three - phase half controlled thyristor converter has a highly inductive load of {rload.ohms} ohms, and a supply voltage of {vsourcerms.V} V at {frequency.Hz} Hz. a) Determine the values of average load voltage and current, rms phase current, load power, and converter power factor for a firing delay angle of {alpha.degrees} degrees. b) What are the maximum values of load power and converter power factor obtainable from the circuit?"""
        
        num = (3 * math.sqrt(3)) / (2 * math.pi)
        
        vave = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(alpha.radians))
        
        iave = c.current( vave.V / rload.ohms )
        irms = c.current(iave.A / math.sqrt(3))
        powerP = c.power(iave.A**2 * rload.ohms)
        pf = powerP.W / (3 * vsourcerms.V * irms.A)
        
        #for max alpha = 0 deg
        
        vavemax = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(0))
        
        iavemax = c.current( vavemax.V / rload.ohms )
        irmsmax = c.current(iavemax.A / math.sqrt(3))
        powerPmax = c.power(iavemax.A**2 * rload.ohms)
        pfmax = powerPmax.W / (3 * vsourcerms.V * irmsmax.A)
        
        
        self.answer = f"""For situation A:
load voltage = {vave.V} V
load current = {iave.A} A
rms phase current = {irms.A} A
load power = {powerP.W} W
power factor = {pf}

For situation B:
load power max = {powerPmax.W} W
power factor = {pfmax}"""

class fewson_3_10:
    def __init__(self,*args,**kwargs): 
        print('310')
        rload = c.resistance(ran.main(10))
        vsourcerms = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        alpha_list = [30, 75]
        alpha_i = random.randint(0,len(alpha_list)-1)
        alpha = c.angle(alpha_list[alpha_i], 'degrees')
        
        self.question = f"""A three - phase full controlled thyristor converter has a highly inductive load of {rload.ohms} ohms, and a supply voltage of {vsourcerms.V} V at {frequency.Hz} Hz. a) Determine the values of average load voltage and current, rms phase current, load power, and converter power factor for a firing delay angle of {alpha.degrees} degrees. b) What are the maximum values of load power and converter power factor obtainable from the circuit?"""
        
        num = (3 * math.sqrt(3)) / (math.pi)
        
        vave = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(alpha.radians))
        
        iave = c.current( vave.V / rload.ohms )
        irms = c.current(iave.A * (math.sqrt(6)/3))
        powerP = c.power(iave.A**2 * rload.ohms)
        pf = powerP.W / (3 * vsourcerms.V * irms.A)
        
        #for max alpha = 0 deg
        
        vavemax = c.voltage( num * math.sqrt(2) * vsourcerms.V * math.cos(0))
        
        iavemax = c.current( vavemax.V / rload.ohms )
        irmsmax = c.current(iavemax.A  * (math.sqrt(6)/3))
        powerPmax = c.power(iavemax.A**2 * rload.ohms)
        pfmax = powerPmax.W / (3 * vsourcerms.V * irmsmax.A)
        
        
        self.answer = f"""For situation A:
load voltage = {vave.V} V
load current = {iave.A} A
rms phase current = {irms.A} A
load power = {powerP.W} W
power factor = {pf}

For situation B:
load power max = {powerPmax.W} W
power factor = {pfmax}"""
        
        
        
        


        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        