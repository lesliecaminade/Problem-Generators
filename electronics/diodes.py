import random_handler as ran
import sympy as sym
import math
import constants_conversions as c
import random

x, y, z = sym.symbols('x y z', real = True)#generic variables


class floyd_2_1_a:
    def __init__(self,*args,**kwargs): 
        
        supplyvoltage = c.voltage(ran.main(10))
        resistance = c.resistance(ran.main(1000))
        bulkresistance = c.resistance(ran.main(10))
        
        self.question = f"""Determine the forward voltage and forward current for the diode with a supply voltage of {supplyvoltage.V} V  and a limiting resistor of {resistance.kohms} kohms. Also find the voltage across the limiting resistor in each case. Assume r'd = {bulkresistance.ohms} ohms at the determined value of forward current."""

        #using ideal model
        currentideal = c.current( supplyvoltage.V / resistance.ohms)
        diodevoltageideal = c.voltage(0)
        resistorvoltageideal = c.voltage(supplyvoltage.V)
        
        #using practical model
        diodevoltagepractical = c.voltage(0.7)
        currentpractical = c.current( (supplyvoltage.V - diodevoltagepractical.V) / resistance.ohms   )
        resistorvoltagepractical = c.voltage( currentpractical.A * resistance.ohms)
        
        #using complete model
        
        currentcomplete = c.current(
        (supplyvoltage.V - 0.7 ) / ( resistance.ohms + bulkresistance.ohms)
        )
        diodevoltagecomplete = c.voltage( 0.7 + currentcomplete.A * bulkresistance.ohms)
        resistorvoltagecomplete = c.voltage( currentcomplete.A * resistance.ohms)
        
        self.answer = f"""Ideal: {diodevoltageideal.V} V, {currentideal.A} A, {resistorvoltageideal.V} V,
Practical: {diodevoltagepractical.V} V, {currentpractical.A} A, {resistorvoltagepractical.V} V,
Complete: {diodevoltagecomplete.V} V, {currentcomplete.A} A, {resistorvoltagecomplete.V} V."""


class floyd_2_1_b:
    def __init__(self,*args,**kwargs): 
        
        supplyvoltage = c.voltage(ran.main(10))
        resistance = c.resistance(ran.main(1000))
        #bulkresistance = c.resistance(ran.main(10))
        reversecurrent = c.current(ran.main(1), 'uA')
        
        self.question = f"""Determine the reverse voltage and reverse current for the diode with a supply voltage of {supplyvoltage.V} V  and a limiting resistor of {resistance.kohms} kohms. Also find the voltage across the limiting resistor in each case. Assume IR = {reversecurrent.uA} uA."""

        #using ideal model
        currentideal = c.current(0)
        diodevoltageideal = c.voltage(supplyvoltage.V)
        resistorvoltageideal = c.voltage(0)
        
        #using practical model
        diodevoltagepractical = c.voltage(supplyvoltage.V)
        currentpractical = c.current(0)
        resistorvoltagepractical = c.voltage(0)
        
        #using complete model
        
        currentcomplete = c.current( reversecurrent.A )
        resistorvoltagecomplete = c.voltage( reversecurrent.A * resistance.ohms)
        diodevoltagecomplete = c.voltage(supplyvoltage.V - resistorvoltagecomplete.V)
        
        
        self.answer = f"""Ideal: {diodevoltageideal.V} V, {currentideal.A} A, {resistorvoltageideal.V} V,
Practical: {diodevoltagepractical.V} V, {currentpractical.A} A, {resistorvoltagepractical.V} V,
Complete: {diodevoltagecomplete.V} V, {currentcomplete.A} A, {resistorvoltagecomplete.V} V."""

class floyd_2_2:
    def __init__(self,*args,**kwargs): 
        
        peakvoltage = c.voltage(ran.main(50))
        
        self.question = f"""What is the average value of a half wave rectified voltage having a peak value of {peakvoltage.V} V?"""
        
        averagevoltage = c.voltage(  peakvoltage.V / math.pi  )
        
        self.answer = f"""Average voltage = {averagevoltage.V} V"""
        
class floyd_2_3:
    def __init__(self,*args,**kwargs): 
        diodes = ['1N4001', '1N4004']
        diode = diodes[random.randint(0, len(diodes) - 1)]
        resistance = c.resistance(ran.main(1000))
        voltages = [ran.main(100), ran.main(5)]
        peakinputvoltage = c.voltage(voltages[random.randint(0,1)])
        

        self.question = f"""A half wave rectifier circuit consists of a {diode} diode and a load resistance of {resistance.kohms} kohms. If the input is an AC voltage with a peak value of {peakinputvoltage.V} V, determine the peak output voltage of the half wave rectifier."""

        peakoutputvoltage = c.voltage(peakinputvoltage.V - 0.7)
        
        self.answer = f"""Peak output voltage = {peakoutputvoltage.V} V"""
        
class floyd_2_4:
    def __init__(self,*args,**kwargs): 
        
        primaryvoltage = c.voltage(ran.main(170, 'int'))
        turnsratio = ran.main(5, 'int')
        resistance = c.resistance(ran.main(1000))
        
        self.question = f"""Determine the peak value of the output voltage of a power supply system consisting of a transformer with a turns ratio of {turnsratio}:1 and a half wave rectifier circuit consisting of a single 1N4002 diode. The load resistance is {resistance.kohms} kohms and the peak supply voltage on the primary of the transformer is {primaryvoltage.V} V."""

        secondaryvoltage = c.voltage(primaryvoltage.V / turnsratio)
        
        peakoutputvoltage = c.voltage( secondaryvoltage.V - 0.7)
        
        self.answer = f"""Peak output voltage = {peakoutputvoltage.V} V"""
        
class floyd_2_5:
    def __init__(self,*args,**kwargs): 
        
        peakinputvoltage = c.voltage(ran.main(15))
        
        self.question = f"""Find the average value of a full wave rectified voltage having a peak value of {peakinputvoltage.V} V."""
        
        averagevoltage = c.voltage((2 / math.pi) * peakinputvoltage.V)
        
        self.answer = f"""Average voltage = {averagevoltage.V} V"""
        
class floyd_2_6:
    def __init__(self,*args,**kwargs): 
        
        turnsratio = ran.main(5, 'int')
        peakinputvoltage = c.voltage(ran.main(100))
        loadresistance = c.resistance(ran.main(10000))
        
        self.question = f"""A center - tapped power supply consists of a transformer with a turns ratio of {turnsratio}:1, two 1N4001 diodes, and a load resistance of {loadresistance.kohms} kohms. An input voltage of {peakinputvoltage.V} V peak is applied at the primary of the transformer. a) Show the voltage waveforms across each half of the secondary winding and across RL b) What minimum PIV rating must the diodes have?"""
        
        secondaryvoltage = c.voltage( peakinputvoltage.V / turnsratio)
        
        halfwindingvoltage = c.voltage(secondaryvoltage.V / 2)
        peakloadvoltage = c.voltage(halfwindingvoltage.V - 0.7)
        
        PIV = c.voltage( 2*peakloadvoltage.V + 0.7)
        
        self.answer = f"""Half winding waveform = {halfwindingvoltage.V} Vpeak sine wave.
Load waveform = {peakloadvoltage.V} Vpeak full wave rectified waveform
PIV rating for each diode = {PIV.V} V"""


class floyd_2_7:
    def __init__(self,*args,**kwargs): 
        
        rmssecondaryvoltage = c.voltage(ran.main(12))
        loadresistance = c.resistance(ran.main(1000))
        
        
        self.question = f"""Determine the peak output voltage for a bridge rectifier attached to a transformer secondary with a rms voltage of {rmssecondaryvoltage.V} V. The load resistance is {loadresistance.kohms} kohms. Assuming the practical model, what PIV rating is required for the diodes?"""
        
        peaksecondaryvoltage = c.voltage( 1.414 * rmssecondaryvoltage.V)
        
        peakloadvoltage = c.voltage(peaksecondaryvoltage.V - 1.4)
        
        PIV = c.voltage(peakloadvoltage.V + 0.7)
        
        self.answer = f"""Peak output voltage = {peakloadvoltage.V} V
PIV rating of each diode = {PIV.V} V"""

class floyd_2_8:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            primaryvoltagerms = c.voltage(ran.main(120,'int'))
            turnsratio = ran.main(10, 'int')
            capacitance = c.capacitance(ran.main(1000), 'uF')
            frequency = c.frequency(120)
            loadresistance = c.resistance(ran.main(22, 'int') *10)
            
            
            self.question = f"""Determine the ripple factor for a filtered bridge rectifier with a primary supply voltage of {primaryvoltagerms.V} Vrms, 60 Hz, a turns ratio of {turnsratio} : 1, uses four 1N4001 diodes, capacitance of {capacitance.uF} uF, and load resistance of {loadresistance.ohms} ohms."""
            
            primaryvoltagepeak = c.voltage(primaryvoltagerms.V * 1.414)
            
            secondaryvoltagepeak = c.voltage(primaryvoltagepeak.V / turnsratio)
            
            peakloadvoltage = c.voltage(secondaryvoltagepeak.V - 1.4)
            
            ripplevoltage = c.voltage(
            (1 / (frequency.Hz * loadresistance.ohms * capacitance.F)) * peakloadvoltage.V
            )
            
            dcvoltage = c.voltage(
            (1 - (1/(2*frequency.Hz*capacitance.F*loadresistance.ohms)))*peakloadvoltage.V
            )
            
            ripplefactor = c.percentage(ripplevoltage.V/dcvoltage.V, 'decimal')
            
            if ripplefactor.percent > 0:
                regen = 0
            
            self.answer = f"""Ripple factor = {ripplefactor.decimal}
    Percent ripple = {ripplefactor.percent} percent"""

class floyd_2_9:
    def __init__(self,*args,**kwargs): 
        
        noloadvoltage = c.voltage(ran.main(5.18))
        fullloadvoltage = c.voltage(noloadvoltage.V - ran.main(0.03))
        
        self.question = f"""A certain 7805 regulator has a measured no-load output voltage of {noloadvoltage.V} V and a full load output of {fullloadvoltage.V} V. What is the load regulation expressed as a percentage?"""
        
        loadregulation = c.percentage(
        (noloadvoltage.V - fullloadvoltage.V) / (fullloadvoltage.V) , 'decimal'
        )
        
        self.answer = f"""Load regulation = {loadregulation.percent} percent"""
        
class floyd_2_10:
    def __init__(self,*args,**kwargs): 
        
        supplyvoltage = c.voltage(ran.main(10, 'int'))
        Rlimiting = c.resistance(ran.main(10,'int') * 1000)
        Rload = c.resistance(ran.main(100, 'int') * 1e3)
        
        
        self.question = f"""A parallel negative clipper has a limiting resistor of {Rlimiting.kohms} kohms and a 1N914 diode (silicon). It is attached to a load resistance of {Rload.kohms} kohms and a source voltage of {supplyvoltage.V} Vpeak. Determine the maximum and the minimum voltages of the output voltage across the load."""

        minvoltage = c.voltage(-0.7)
        maxvoltage = c.voltage( supplyvoltage.V *  ((Rload.ohms)/(Rload.ohms + Rlimiting.ohms)) )
        
        self.answer = f"""Min voltage = {minvoltage.V} V
Max voltage = {maxvoltage.V} V"""

class floyd_2_11:
    def __init__(self,*args,**kwargs): 
        
        Vsource = c.voltage(ran.main(10, 'int'))
        R1 = c.resistance(ran.main(1000))
        VD1 = c.voltage(ran.main(5, 'int'))
        VD2 = c.voltage(ran.main(5, 'int'))
        
        
        self.question = f"""Determine the maximum and minimum output voltage of the following circuit. The source voltage is {Vsource.V} Vpeak, the voltage source with D1 is {VD1.V} V, the voltage source with D2 is {VD2.V} V, and R1 is {R1.kohms} kohms. https://lesliecaminadecom.files.wordpress.com/2019/06/1jh1zj3sg858ms6f7r3l.png"""
        
        maxvoltage = c.voltage( VD1.V + 0.7)
        minvoltage = c.voltage( -VD2.V - 0.7 )
        
        self.answer = f"""Min voltage = {minvoltage.V} V
Max voltage = {maxvoltage.V} V"""


class floyd_2_12:
    def __init__(self,*args,**kwargs): 
        
        R2 = c.resistance(ran.main(100, 'int'))
        R3 = c.resistance(ran.main(220, 'int'))
        Vsource = c.voltage(18)
        Vbiassource = c.voltage(12)
        
        self.question = f"""Determine the minimum and the maximum voltages of the output of the following circuit if R2 = {R2.ohms} ohms and R3 = {R3.ohms} ohms.https://lesliecaminadecom.files.wordpress.com/2019/06/no15x1d0qzdtbd1ydymr.png"""
        
        Vbias = c.voltage(
        ( (R3.ohms) / (R3.ohms + R2.ohms)) * Vbiassource.V
        )
        
        maxvoltage = c.voltage(Vbias.V + 0.7)
        minvoltage = c.voltage(-Vsource.V)
        
        self.answer = f"""Minimum voltage = {minvoltage.V} V
Max voltage = {maxvoltage.V} V"""

class floyd_2_13:
    def __init__(self,*args,**kwargs): 
        
        Vsource = c.voltage(ran.main(24, 'int'))
        C1 = c.capacitance(ran.main(10, 'int'), 'uF')
        Rload = c.resistance(ran.main(10, 'int')*1000)
        
        self.question = f"""A negative clamper has C = {C1.uF} uF and a 1N914(silicon) diode. It is attached to a load resistance of {Rload.kohms} kohms. If the peak source voltage is {Vsource.V} Vpeak, determine the maximum, minimum, and Dc output voltages.""" 
        
        Vdc = c.voltage( - (Vsource.V - 0.7))
        Vmax = c.voltage(0.7)
        Vmin = c.voltage(Vdc.V - Vsource.V)
        
        self.answer = f"""DC voltage = {Vdc.V} V
Maximum voltage = {Vmax.V} V
Minimum voltage = {Vmin.V} V"""
        
        
        
class floyd_3_5:
    def __init__(self,*args,**kwargs): 
        
        Vz = c.voltage(ran.main(51, 'int')/10)
        Iz = c.current(ran.main(49, 'int'), 'mA')
        Izk = c.current(1, 'mA')
        Zz = c.resistance(ran.main(7, 'int'))
        R1 = c.resistance(ran.main(100, 'int'))
        Pzmax = c.power(1)
        
        self.question = f"""Determine the minimum and the maximum input voltages that can be regulated by the zener diode. R = {R1.ohms} ohms, Zener diode: Vz = {Vz.V} V, Iz = {Iz.mA} mA, Izk = {Izk.mA} mA, Zz = {Zz.ohms} ohms at Iz. Pzmax = {Pzmax.W} W. https://lesliecaminadecom.files.wordpress.com/2019/06/d17z552uz3ava3j77llr.png"""
        
        deltaVz = c.voltage( (Iz.A - Izk.A) * Zz.ohms) 
        Voutmin = c.voltage(Vz.V - deltaVz.V)
        Vinmin = c.voltage( Izk.A * R1.ohms + Voutmin.V )
        
        Izmax = c.current(Pzmax.W / Vz.V)
        deltaVzmax = c.voltage((Izmax.A - Iz.A)*Zz.ohms)
        Voutmax = c.voltage(Vz.V + deltaVzmax.V)
        Vinmax = c.voltage(Voutmax.V + Izmax.A * R1.ohms)
        
        self.answer = f"""Minimum input voltage = {Vinmin.V} V
Maximum input voltage = {Vinmax.V} V"""

class floyd_3_6:
    def __init__(self,*args,**kwargs): 
        
        Vz = c.voltage(ran.main(12, 'int'))
        Vin = c.voltage(Vz.V + ran.main(12, 'int'))
        Rs = c.resistance(ran.main(47 ,'int') * 10)
        Izk = c.current(random.randint(1,3), 'mA')
        Izm = c.current(ran.main(50, 'int'), 'mA')
        
        
        self.question = f"""For an input voltage of {Vin.V} V, determine the minimum and the maximum load currents for which the zener diode will maintain regulation. What is the minimum value of RL that can be used? R = {Rs.ohms} ohms, Vz = {Vz.V} V, Izk = {Izk.mA} mA, and Izm = {Izm.mA} mA. Assume an ideal zener diode where Zz = 0 ohms and Vz remains a constant {Vz.V} V over the range of current values, for simplicity.https://lesliecaminadecom.files.wordpress.com/2019/06/2qq8d3u9659jmxxe5nps.png"""
        
        Itotal = c.current(
        (Vin.V - Vz.V) / Rs.ohms
        )
        
        if Itotal.A < Izm.A:
            Iloadmin = c.current(0)
            Rloadmax = c.resistance(float('inf'))
        else:
            Iloadmin = c.current(Itotal.A - Izm.A)
            Rloadmax = c.resistance(Vz.V / Iloadmin.A)
            
        Iloadmax = c.current(Itotal.A - Izk.A)
        
        Rloadmin = c.resistance(Vz.V / Iloadmax.A)
        
        self.answer = f"""Minimum load current = {Iloadmin.mA} mA
Maximum load current = {Iloadmax.mA} mA
Minimum load resistance = {Rloadmin.ohms} ohms
Maximum load resistance = {Rloadmax.ohms} ohms"""

class floyd_3_7:
    def __init__(self,*args,**kwargs): 
        
        Vin = c.voltage(ran.main(24, 'int'))
        Vz = c.voltage(ran.main(15, 'int'))
        Iz = c.current(ran.main(17, 'int'), 'mA')
        Izk = c.current(ran.main(25, 'int')/100, 'mA')
        Zz = c.resistance(ran.main(14, 'int'))
        Pzmax = c.power(1)
        
        self.question = f"""For an input voltage of {Vin.V} V, a) Determine Vout at Izk and a Izm. b) Calculate the value of R that should be used. c) Determine the minimum value of RL that can be used. Specifications for the diode are: Vz = {Vz.V} V @ Iz = {Iz.mA} mA, Izk = {Izk.mA} mA, and Zz = {Zz.ohms} ohms, Pzmax = {Pzmax.W} W. https://lesliecaminadecom.files.wordpress.com/2019/06/af6qgi3si4t4i7zhf6oc.png"""
        
        VoutIzk = c.voltage(Vz.V - (Iz.A - Izk.A)*Zz.ohms)
        Izm = c.current(Pzmax.W / Vz.V)
        VoutIzm = c.voltage(Vz.V + (Izm.A - Iz.A)*Zz.ohms)
        
        R = c.resistance(
        (Vin.V - VoutIzm.V) / Izm.A
        )
        
        Itotal = c.current((Vin.V - VoutIzk.V) / R.ohms)
        Iload = c.current(Itotal.A - Izk.A)
        Rloadmin = c.resistance(VoutIzk.V / Iload.A)
        
        
        self.answer = f"""Vout at Izk = {VoutIzk.V} V
Vout at Izmax = {VoutIzm.V} V
R that should be used (based on Izmax) = {R.ohms} ohms
Minimum value of Rl = {Rloadmin.ohms} ohms"""


class floyd_3_8_a:
    def __init__(self,*args,**kwargs): 
        
        R1 = c.resistance(random.randint(1,5)*1000)
        Vz1 = c.voltage(ran.main(33, 'int')/10)
        Vz2 = c.voltage(ran.main(51, 'int')/10)
        
        self.question = f"""With a peak input voltage of 50V, determine the minimum and maximum voltage of the output waveform for the zener limiting circuit. R = {R1.kohms} kohms, top zener voltage = {Vz1.V} V, bottom zener voltage = {Vz2.V} V. https://lesliecaminadecom.files.wordpress.com/2019/06/6d29y6yjxl43lz61pue2.png"""
        
        vmaximum = c.voltage(Vz2.V + 0.7)
        vminimum = c.voltage(-(Vz1.V + 0.7))
        
        self.answer = f"""Max voltage = {vmaximum.V} V
Minimum voltage = {vminimum.V} V"""
#-----------------------------------------------------------



        
        















        