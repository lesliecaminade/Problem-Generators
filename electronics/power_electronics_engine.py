from generator import random_handler as ran
from generator import constants_conversions as c
import sympy as sym
import math
import random

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
            
            self.question = f"""A dc to dc chopper operates from a {vsource.V:.4} V battery source into a resistive load of {rload.ohms:.4} ohms. The frequency of the chopper is set to {freq.Hz:.4} Hz. Determine the average and rms load current and the load power values when chopper on time is {ton.ms:.4} ms."""
            
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
        
        self.answer = f"""{iaverage.A:.4} A, {irms.A:.4} A, {powerP.W:.4} W"""

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
            
            self.question = f"""A dc to dc chopper has an inductive load of {rload.ohms:.4} ohms resistance and {lload.mH:.4} mH inductance. Source voltage is {vsource.V:.4} V. The frequency of the chopper is set to {frequency.Hz:.4} Hz and the on-time to {ton.ms:.4} ms. Determine the average, maximum, minimum, and RMS load currents."""
            
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
        
        
        self.answer = f"""{iaverage.A:.4} A, {i1.A:.4} A, {i0.A:.4} A, {irms.A:.4} A"""

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
            
            self.question = f"""A dc series chopper drive has the following parameters: Battery voltage = {vbattery.V:.4} V, (Ra + Rf) = {rarf.ohms:.4} ohms, kv = {kv.mV:.4} mV / Arad/s , chopper frequency = {frequency.Hz:.4} Hz. a) Calculate the armature speed and torque with an average armature current of {ia.A:.4} A and a chopper on time of {ton.ms:.4} ms. b) Determine the motor speed and armature current at a torque of {torque2.Nm:.4} Nm with on time and off time similar to situation a."""
            
            if period.s > ton.s:
                regen = False
        
        vaverage = c.voltage( vbattery.V * ton.s * frequency.Hz )
        backemf = c.voltage( vaverage.V - ia.A * rarf.ohms )
        omega = c.angularVelocity( backemf.V / (kv.V * ia.A) , 'radpers')
        torque = c.torque( kv.V * ia.A**2 )
        
        ia2 = c.current( math.sqrt( torque2.Nm * kv.V ))
        backemf2 = c.voltage( vaverage.V - ia2.A * rarf.ohms )
        omega2 = c.angularVelocity( backemf2.V / (kv.V * ia2.A) , 'radpers')
        
        self.answer = f"""{omega.revpermin:.4} rev/min, {torque.Nm:.4} Nm; {omega2.revpermin:.4} rev/min, {ia2.A:.4} A"""

class fewson_2_4:
    def __init__(self,*args,**kwargs): 
        print('24')
        iload = c.current(ran.main(3))
        rload = c.resistance(ran.main(10))
        vbattery = c.voltage(ran.main(12))
        lchopper = c.inductance(ran.main(20), 'uH')
        cchopper = c.capacitance(ran.main(100), 'uF')
        frequency = c.frequency(ran.main(50), 'kHz')
        
        
        self.question = f"""A stepup chopper is to deliver {iload.A:.4} A into the {rload.ohms:.4} ohms load. The battery voltage is {vbattery.V:.4} V , L = {lchopper.uH:.4} uH, C = {cchopper.uF:.4} uF, and the chopper frequency is {frequency.kHz:.4} kHz. Determine the on-time of the chopper, the battery current variation, and the average battery current."""
        
        vload = c.voltage(iload.A * rload.ohms)
        dutycycle = c.percentage( 1 - (vbattery.V / vload.V) , 'decimal')
        period = c.time(1/frequency.Hz)
        ton = c.time(dutycycle.decimal * period.s)
        deltai = c.current( vbattery.V * ton.s / lchopper.H )
        
        ibattery = c.current(iload.A / (1 - dutycycle.decimal))
        ibmax = c.current( ibattery.A + deltai.A/2)
        ibmin = c.current( ibattery.A - deltai.A/2)
        
        self.answer = f"""{ton.us:.4} us, {ibattery.A:.4} A, {ibmax.A:.4} A, {ibmin.A:.4} A"""

class fewson_2_5:
    def __init__(self,*args,**kwargs): 
        print('25')
        toff = c.time(ran.main(20), 'us')
        vbattery = c.voltage(ran.main(96))
        iload = c.current(ran.main(100))
        
        self.question = f"""What value of capacitor is required to force commutate a thyristor with a turnoff time of {toff.us:.4} us with a {vbattery.V:.4} V and a full load current of {iload.A:.4} A?"""

        capacitor = c.capacitance(1.43 * toff.s * iload.A / vbattery.V)
        
        self.answer = f"""{capacitor.uF:.4} uF"""
        
class fewson_3_1:
    def __init__(self,*args,**kwargs): 
        print('31')
        vsourceRMS = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        rload = c.resistance(ran.main(100))
        alpha_list = [30, 140, 120]
        i = random.randint(0,2)
        alpha = c.angle(ran.main(alpha_list[i]), 'degrees')
        
        self.question = f"""A thyristor half-wave half controlled converter has a supply voltage of {vsourceRMS.V:.4} V at {frequency.Hz:.4} Hz and a load resistance of {rload.ohms:.4} ohms. What are the average values of load voltage and current when the firing delay angle is {alpha.degrees:.4} degrees?"""
        
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
        
        
        self.answer = f"""{vaverage.V:.4} V, {iaverage.A:.4} A, {vrms.V:.4} V, {irms.A:.4} A, {pf:.4}"""

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
            
            self.question = f"""In the circuit, C = {capacitance.nF:.4} nF and R is variable from {rlow.kohms:.4} kohms to {rhigh.kohms:.4} kohms. Determine the range of the firing delay angle available. The ECG6412 hs a breakdown voltage of 63 V.
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
        
                self.answer = f"""{alphalow.degrees:.4} deg to {alphahigh.degrees:.4} deg."""
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
            
            self.question = f"""A full - wave half controlled bridge has a supply voltage of {vsourcerms.V:.4} V at {frequency.Hz:.4} Hz. The firing angle delay alpha = {alpha.degrees:.4} degrees. Determine the values of average and rms currents, load power, and power factor for a a) resistive load of R = {rload.ohms:.4} ohms, b) a highly inductive load with a resistance of R = {rload2.ohms:.4} ohms."""
            
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
        
        
        self.answer = f"""{iave.A:.4} A, {irms.A:.4} A, {powerP.W:.4} W, {pf:.4}; {iaveb.A:.4} A, {irmsb.A:.4} A, {powerPb.W:.4} W, {pfb:.4}"""

class fewson_3_5:
    def __init__(self,*args,**kwargs): 
        print('35')
        regen = True
        while regen:
            rload = c.resistance(ran.main(55))
            vsourcerms = c.voltage(ran.main(110))
            frequency = c.frequency(ran.main(50))
            alpha = c.angle(ran.main(75), 'degrees')
            
            self.question = f"""A full - wave fully controlled bridge has a highly inductive load with a resistance of {rload.ohms:.4} ohms, and a supply voltage of {vsourcerms.V:.4} V at {frequency.Hz:.4} Hz. a) Calculate the values of load current, power, and converter power factor for a firing delay angle of {alpha.degrees:.4} degrees."""
            
            if alpha.radians < math.pi:
                regen = False
        
        vave = c.voltage(
        (2*vsourcerms.V * math.sqrt(2) /math.pi ) * math.cos(alpha.radians)
        )
        
        iave = c.current(vave.V / rload.ohms)
        
        powerP = c.power( iave.A**2 * rload.ohms )
        
        pf = 0.9 * math.cos( alpha.radians )
        
        self.answer = f"""{iave.A:.4} A, {powerP.W:.4} W, {pf:.4}"""

class fewson_3_6:
    def __init__(self,*args,**kwargs): 
        print('36')
        regen = True
        while regen:
            vsourcerms = c.voltage(ran.main(240))
            frequency = c.frequency(ran.main(50))
            rload = c.resistance(ran.main(50))
            alpha = c.angle(ran.main(75), 'degrees')
            
            self.question = f"""A {vsourcerms.V:.4} V,  {frequency.Hz:.4} Hz supply feeds a highly inductive load of {rload.ohms:.4} ohms resistance through a thyristor bridge that is a) half controlled and b) full controlled. Calculate the load current, power, and power factor for each case when the firing angle delay is {alpha.degrees:.4} degrees."""
            
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
        
        
        self.answer = f"""{irms.A:.4} A, {powerP.W:.4} W, {pf:.4}, {irmsb.A:.4} A, {powerPb.W:.4} W, {pfb:.4}"""


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
                
                self.question = f"""A separately excited dc motor is driven from a {vsourcerms.V:.4} V, {frequency.Hz:.4} Hz supply using a fully controlled thyristor bridge. The motor has an armature resistance Ra = {ra.ohms:.4} ohms and an armature voltage constant kv of {kv.V:.4} V/rad s . The field current is constant at its rated value. Assume that the armature current is steady. a) Determine the values of armature current and torque for an armature speed of {speed.revpermin:.4} rev/min and a firing angle of {alpha.degrees:.4} degrees. b) Calculate the limits of the firing delay for this speed."""
            
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
        
        self.answer =f"""{iave.A:.4} A, {torque.Nm:.4} Nm, {alphalow.degrees:.4} degrees, {alphahigh.degrees:.4} degrees"""

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
            
            self.question = f"""A separately excited dc motor is driven from a {vsourcerms.V:.4} V, {frequency.Hz:.4} Hz supply using a half controlled thyristor bridge with a flywheel diode connected across the armature. The motor has an armature resistance Ra of {ra.ohms:.4} ohms, and an armature voltage constant kv of {kv.V:.4} V/rad/s. The field current is constant at its rated value. Assume that the armature current is steady. Determin the values of armauture current and torque for an armature speed of {speed.revpermin:.4} rev/min and a firing delay angle of {alpha.degrees:.4} degrees."""

            eb = c.voltage( kv.V * speed.radpers )
            vave = c.voltage( (math.sqrt(2) * vsourcerms.V / math.pi) * (1 + math.cos(alpha.radians)) ) 
        
            if vave.V > eb.V:
                regen = False
        
        iave = c.current((vave.V - eb.V) / ra.ohms)
        
        torque = c.torque( kv.V * iave.A )
        
        self.answer = f"""{iave.A:.4} A, {torque.Nm:.4} Nm"""

class fewson_3_9:
    def __init__(self,*args,**kwargs): 
        print('39')
        rload = c.resistance(ran.main(10))
        vsourcerms = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        alpha_list = [30, 75]
        alpha_i = random.randint(0,len(alpha_list)-1)
        alpha = c.angle(alpha_list[alpha_i], 'degrees')
        
        self.question = f"""A three - phase half controlled thyristor converter has a highly inductive load of {rload.ohms:.4} ohms, and a supply voltage of {vsourcerms.V:.4} V at {frequency.Hz:.4} Hz. a) Determine the values of average load voltage and current, rms phase current, load power, and converter power factor for a firing delay angle of {alpha.degrees:.4} degrees. b) What are the maximum values of load power and converter power factor obtainable from the circuit?"""
        
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
        
        
        self.answer = f"""{vave.V:.4} V, {iave.A:.4} A, {irms.A:.4} A, {powerP.W:.4} W, {pf:.4}, {powerPmax.W:.4} W, {pfmax:.4}"""

class fewson_3_10:
    def __init__(self,*args,**kwargs): 
        print('310')
        rload = c.resistance(ran.main(10))
        vsourcerms = c.voltage(ran.main(240))
        frequency = c.frequency(ran.main(50))
        alpha_list = [30, 75]
        alpha_i = random.randint(0,len(alpha_list)-1)
        alpha = c.angle(alpha_list[alpha_i], 'degrees')
        
        self.question = f"""A three - phase full controlled thyristor converter has a highly inductive load of {rload.ohms:.4} ohms, and a supply voltage of {vsourcerms.V:.4} V at {frequency.Hz:.4} Hz. a) Determine the values of average load voltage and current, rms phase current, load power, and converter power factor for a firing delay angle of {alpha.degrees:.4} degrees. b) What are the maximum values of load power and converter power factor obtainable from the circuit?"""
        
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
        
        
        self.answer = f"""{vave.V:.4} V, {iave.A:.4} A, {irms.A:.4} A, {powerP.W:.4} W, {pf:.4}, {powerPmax.W:.4} W, {pfmax:.4}"""
        
        
        
        


        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        