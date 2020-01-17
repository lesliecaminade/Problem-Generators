from generator import random_handler as ran
from generator import constants_conversions as c
import sympy
import math
import random
from fractions import Fraction

x, y, z = sympy.symbols('x y z', real = True)#generic variables



class floyd_2_1_a:
    def __init__(self,*args,**kwargs): 
        
        supplyvoltage = c.voltage(ran.main(10))
        resistance = c.resistance(ran.main(1000))
        bulkresistance = c.resistance(10, 'e12')
        
        self.question = f"""Determine the forward voltage and forward current for the diode with a supply voltage of {supplyvoltage.V:5.5} V  and a limiting resistor of {resistance.kohms:5.5} kohms. Also find the voltage across the limiting resistor in each case. Assume r'd = {bulkresistance.ohms:5.5} ohms at the determined value of forward current."""

        #using ideal model
        currentideal = c.current( supplyvoltage.V / resistance.ohms)
        diodevoltageideal = c.voltage(float(0))
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
        
        self.answer = f"""{diodevoltageideal.V:5.5} V, {currentideal.A:5.5} A, {resistorvoltageideal.V:5.5} V; {diodevoltagepractical.V:5.5} V, {currentpractical.A:5.5} A, {resistorvoltagepractical.V:5.5} V; {diodevoltagecomplete.V:5.5} V, {currentcomplete.A:5.5} A, {resistorvoltagecomplete.V:5.5} V."""


class floyd_2_1_b:
    def __init__(self,*args,**kwargs): 
        
        supplyvoltage = c.voltage(ran.main(10))
        resistance = c.resistance(1000, 'e12')
        #bulkresistance = c.resistance(ran.main(10))
        reversecurrent = c.current(ran.main(1), 'uA')
        
        self.question = f"""Determine the reverse voltage and reverse current for the diode with a supply voltage of {supplyvoltage.V:5.5} V  and a limiting resistor of {resistance.kohms:5.5} kohms. Also find the voltage across the limiting resistor in each case. Assume IR = {reversecurrent.uA:5.5} uA."""

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
        
        
        self.answer = f"""{diodevoltageideal.V:5.5} V, {currentideal.A:5.5} A, {resistorvoltageideal.V:5.5} V; {diodevoltagepractical.V:5.5} V, {currentpractical.A:5.5} A, {resistorvoltagepractical.V:5.5} V; {diodevoltagecomplete.V:5.5} V, {currentcomplete.A:5.5} A, {resistorvoltagecomplete.V:5.5} V."""

class floyd_2_2:
    def __init__(self,*args,**kwargs): 
        
        peakvoltage = c.voltage(ran.main(50))
        
        self.question = f"""What is the average value of a half wave rectified voltage having a peak value of {peakvoltage.V:5.5} V?"""
        
        averagevoltage = c.voltage(  peakvoltage.V / math.pi  )
        
        self.answer = f"""{averagevoltage.V:5.5} V"""
        
class floyd_2_3:
    def __init__(self,*args,**kwargs): 
        diodes = ['1N4001', '1N4004']
        diode = diodes[random.randint(0, len(diodes) - 1)]
        resistance = c.resistance(1000, 'e12')
        voltages = [ran.main(100), ran.main(5)]
        peakinputvoltage = c.voltage(voltages[random.randint(0,1)])
        

        self.question = f"""A half wave rectifier circuit consists of a {diode:5.5} diode and a load resistance of {resistance.kohms:5.5} kohms. If the input is an AC voltage with a peak value of {peakinputvoltage.V:5.5} V, determine the peak output voltage of the half wave rectifier."""

        peakoutputvoltage = c.voltage(peakinputvoltage.V - 0.7)
        
        self.answer = f"""{peakoutputvoltage.V:5.5} V"""
        
class floyd_2_4:
    def __init__(self,*args,**kwargs): 
        
        primaryvoltage = c.voltage(ran.main(170, 'int'))
        turnsratio = Fraction(ran.main(5, 'int')).limit_denominator(1000)
        resistance = c.resistance(1000, 'e12')
        
        self.question = f"""Determine the peak value of the output voltage of a power supply system consisting of a transformer with a turns ratio of {turnsratio.numerator}:{turnsratio.denominator} and a half wave rectifier circuit consisting of a single 1N4002 diode. The load resistance is {resistance.kohms:5.5} kohms and the peak supply voltage on the primary of the transformer is {primaryvoltage.kV:5.5} kV."""

        secondaryvoltage = c.voltage(primaryvoltage.V / turnsratio)
        
        peakoutputvoltage = c.voltage( secondaryvoltage.V - 0.7)
        
        self.answer = f"""{peakoutputvoltage.V:5.5} V"""
        
class floyd_2_5:
    def __init__(self,*args,**kwargs): 
        
        peakinputvoltage = c.voltage(ran.main(15))
        
        self.question = f"""Find the average value of a full wave rectified voltage having a peak value of {peakinputvoltage.V:5.5} V."""
        
        averagevoltage = c.voltage((2 / math.pi) * peakinputvoltage.V)
        
        self.answer = f"""{averagevoltage.V:5.5} V"""
        
class floyd_2_6:
    def __init__(self,*args,**kwargs): 
        
        turnsratio = ran.main(5, 'int')
        peakinputvoltage = c.voltage(ran.main(100))
        loadresistance = c.resistance(10e3, 'e12')
        
        self.question = f"""A center - tapped power supply consists of a transformer with a turns ratio of {turnsratio:5.5}:1, two 1N4001 diodes, and a load resistance of {loadresistance.kohms:5.5} kohms. An input voltage of {peakinputvoltage.V:5.5} V peak is applied at the primary of the transformer. a) Show the voltage waveforms across each half of the secondary winding and across RL b) What minimum PIV rating must the diodes have?"""
        
        secondaryvoltage = c.voltage( peakinputvoltage.V / turnsratio)
        
        halfwindingvoltage = c.voltage(secondaryvoltage.V / 2)
        peakloadvoltage = c.voltage(halfwindingvoltage.V - 0.7)
        
        PIV = c.voltage( 2*peakloadvoltage.V + 0.7)
        
        self.answer = f"""{halfwindingvoltage.V:5.5} Vpeak sine wave, {peakloadvoltage.V:5.5} Vpeak full wave rectified waveform, {PIV.V:5.5} V"""


class floyd_2_7:
    def __init__(self,*args,**kwargs): 
        
        rmssecondaryvoltage = c.voltage(ran.main(12))
        loadresistance = c.resistance(1000, 'e12')
        
        
        self.question = f"""Determine the peak output voltage for a bridge rectifier attached to a transformer secondary with a rms voltage of {rmssecondaryvoltage.V:5.5} V. The load resistance is {loadresistance.kohms:5.5} kohms. Assuming the practical model, what PIV rating is required for the diodes?"""
        
        peaksecondaryvoltage = c.voltage( 1.414 * rmssecondaryvoltage.V)
        
        peakloadvoltage = c.voltage(peaksecondaryvoltage.V - 1.4)
        
        PIV = c.voltage(peakloadvoltage.V + 0.7)
        
        self.answer = f"""{peakloadvoltage.V:5.5} V, {PIV.V:5.5} V"""

class floyd_2_8:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            primaryvoltagerms = c.voltage(ran.main(120,'int'))
            turnsratio = ran.main(10, 'int')
            capacitance = c.capacitance(ran.main(1000), 'uF')
            frequency = c.frequency(120)
            loadresistance = c.resistance(220, 'e12')
            
            
            self.question = f"""Determine the ripple factor for a filtered bridge rectifier with a primary supply voltage of {primaryvoltagerms.kV:5.5} kVrms, 60 Hz, a turns ratio of {turnsratio:5.5} : 1, uses four 1N4001 diodes, capacitance of {capacitance.uF:5.5} uF, and load resistance of {loadresistance.ohms:5.5} ohms."""
            
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
            
            self.answer = f"""{ripplefactor.decimal:5.5}, {ripplefactor.percent:5.5} %"""

class floyd_2_9:
    def __init__(self,*args,**kwargs): 
        
        noloadvoltage = c.voltage(ran.main(5.18))
        fullloadvoltage = c.voltage(noloadvoltage.V - ran.main(0.03))
        
        self.question = f"""A certain 7805 regulator has a measured no-load output voltage of {noloadvoltage.V:5.5} V and a full load output of {fullloadvoltage.V:5.5} V. What is the load regulation expressed as a percentage?"""
        
        loadregulation = c.percentage(
        (noloadvoltage.V - fullloadvoltage.V) / (fullloadvoltage.V) , 'decimal'
        )
        
        self.answer = f"""{loadregulation.percent:5.5} %"""
        
class floyd_2_10:
    def __init__(self,*args,**kwargs): 
        
        supplyvoltage = c.voltage(int(ran.main(10)))
        Rlimiting = c.resistance(10e3, 'e12')
        Rload = c.resistance(100e3, 'e12')
        
        
        self.question = f"""A parallel negative clipper has a limiting resistor of {Rlimiting.kohms:5.5} kohms and a 1N914 diode (silicon). It is attached to a load resistance of {Rload.kohms:5.5} kohms and a source voltage of {supplyvoltage.V:5.5} Vpeak. Determine the peak voltages of the output voltage across the load."""

        minvoltage = c.voltage(-0.7)
        maxvoltage = c.voltage( supplyvoltage.V *  ((Rload.ohms)/(Rload.ohms + Rlimiting.ohms)) )
        
        self.answer = f"""{minvoltage.V:5.5} V, {maxvoltage.V:5.5} V"""

class floyd_2_11:
    def __init__(self,*args,**kwargs): 
        
        Vsource = c.voltage(int(ran.main(10)))
        R1 = c.resistance(1000, 'e12')
        VD1 = c.voltage(int(ran.main(5)))
        VD2 = c.voltage(int(ran.main(5)))
        
        
        self.question = f"""Determine the peak voltages of the following circuit. The source voltage is {Vsource.V:5.5} Vpeak, the voltage source with D1 is {VD1.V:5.5} V, the voltage source with D2 is {VD2.V:5.5} V, and R1 is {R1.kohms:5.5} kohms. https://lesliecaminadecom.files.wordpress.com/2019/06/1jh1zj3sg858ms6f7r3l.png"""
        
        maxvoltage = c.voltage( VD1.V + 0.7)
        minvoltage = c.voltage( -VD2.V - 0.7 )
        
        self.answer = f"""{minvoltage.V:5.5} V, {maxvoltage.V:5.5} V"""


class floyd_2_12:
    def __init__(self,*args,**kwargs): 
        
        R2 = c.resistance(100, 'e12')
        R3 = c.resistance(220, 'e12')
        Vsource = c.voltage(18)
        Vbiassource = c.voltage(12)
        
        self.question = f"""Determine the peak voltages of the output of the following circuit if R2 = {R2.ohms:5.5} ohms and R3 = {R3.ohms:5.5} ohms.https://lesliecaminadecom.files.wordpress.com/2019/06/no15x1d0qzdtbd1ydymr.png"""
        
        Vbias = c.voltage(
        ( (R3.ohms) / (R3.ohms + R2.ohms)) * Vbiassource.V
        )
        
        maxvoltage = c.voltage(Vbias.V + 0.7)
        minvoltage = c.voltage(-Vsource.V)
        
        self.answer = f"""{float(minvoltage.V):5.5} V, {maxvoltage.V:5.5} V"""

class floyd_2_13:
    def __init__(self,*args,**kwargs): 
        
        Vsource = c.voltage(int(ran.main(24)))
        C1 = c.capacitance(int(ran.main(10)), 'uF')
        Rload = c.resistance(10e3, 'e12')
        
        self.question = f"""A negative clamper has C = {C1.uF:5.5} uF and a 1N914(silicon) diode. It is attached to a load resistance of {Rload.kohms:5.5} kohms. If the peak source voltage is {Vsource.V:5.5} Vpeak, determine the peak voltages, and Dc output voltages.""" 
        
        Vdc = c.voltage( - (Vsource.V - 0.7))
        Vmax = c.voltage(0.7)
        Vmin = c.voltage(Vdc.V - Vsource.V)
        
        self.answer = f"""{Vdc.V:5.5} V, {Vmax.V:5.5} V, {Vmin.V:5.5} V"""
        
class floyd_3_5:
    def __init__(self,*args,**kwargs): 
        
        Vz = c.voltage(int(ran.main(51))/10)
        Iz = c.current(int(ran.main(49)), 'mA')
        Izk = c.current(1, 'mA')
        Zz = c.resistance(int(ran.main(7)))
        R1 = c.resistance(100, 'e12')
        Pzmax = c.power(1)
        
        self.question = f"""Determine the minimum and the maximum input voltages that can be regulated by the zener diode. R = {R1.ohms:5.5} ohms, Zener diode: Vz = {Vz.V:5.5} V, Iz = {Iz.mA:5.5} mA, Izk = {Izk.mA:5.5} mA, Zz = {Zz.ohms:5.5} ohms at Iz. Pzmax = {Pzmax.W:5.5} W. https://lesliecaminadecom.files.wordpress.com/2019/06/d17z552uz3ava3j77llr.png"""
        
        deltaVz = c.voltage( (Iz.A - Izk.A) * Zz.ohms) 
        Voutmin = c.voltage(Vz.V - deltaVz.V)
        Vinmin = c.voltage( Izk.A * R1.ohms + Voutmin.V )
        
        Izmax = c.current(Pzmax.W / Vz.V)
        deltaVzmax = c.voltage((Izmax.A - Iz.A)*Zz.ohms)
        Voutmax = c.voltage(Vz.V + deltaVzmax.V)
        Vinmax = c.voltage(Voutmax.V + Izmax.A * R1.ohms)
        
        self.answer = f"""{Vinmin.V:5.5} V, {Vinmax.V:5.5} V"""

class floyd_3_6:
    def __init__(self,*args,**kwargs): 
        repeat = True
        while repeat:
            Vz = c.voltage(int(ran.main(12)))
            Vin = c.voltage(Vz.V + int(ran.main(12)))
            Rs = c.resistance(470, 'e12')
            Izk = c.current(random.randint(1,3), 'mA')
            Izm = c.current(int(ran.main(50)), 'mA')
            
            
            self.question = f"""For an input voltage of {Vin.V:5.5} V, determine the minimum and the maximum load currents for which the zener diode will maintain regulation. What is the minimum value of RL that can be used? R = {Rs.ohms:5.5} ohms, Vz = {Vz.V:5.5} V, Izk = {Izk.mA:5.5} mA, and Izm = {Izm.mA:5.5} mA. Assume an ideal zener diode where Zz = 0 ohms and Vz remains a constant {Vz.V:5.5} V over the range of current values, for simplicity.https://lesliecaminadecom.files.wordpress.com/2019/06/2qq8d3u9659jmxxe5nps.png"""
            
            Itotal = c.current(
            (Vin.V - Vz.V) / Rs.ohms
            )
            
            if Itotal.A <= Izm.A:
                repeat = True
            else:
                Iloadmin = c.current(Itotal.A - Izm.A)
                Rloadmax = c.resistance(Vz.V / Iloadmin.A)
                repeat = False
                
            Iloadmax = c.current(Itotal.A - Izk.A)
            
            Rloadmin = c.resistance(Vz.V / Iloadmax.A)
        
        self.answer = f"""{Iloadmin.mA:5.5} mA, {Iloadmax.mA:5.5} mA, {Rloadmin.ohms:5.5} ohms, {Rloadmax.ohms:5.5} ohms"""

class floyd_3_7:
    def __init__(self,*args,**kwargs): 
        
        Vin = c.voltage(int(ran.main(24)))
        Vz = c.voltage(int(ran.main(15)))
        Iz = c.current(int(ran.main(17)), 'mA')
        Izk = c.current(int(ran.main(25))/100, 'mA')
        Zz = c.resistance(int(ran.main(14)))
        Pzmax = c.power(1)
        
        self.question = f"""For an input voltage of {Vin.V:5.5} V, a) Determine Vout at Izk and a Izm. b) Calculate the value of R that should be used. c) Determine the minimum value of RL that can be used. Specifications for the diode are: Vz = {Vz.V:5.5} V @ Iz = {Iz.mA:5.5} mA, Izk = {Izk.mA:5.5} mA, and Zz = {Zz.ohms:5.5} ohms, Pzmax = {Pzmax.W:5.5} W. https://lesliecaminadecom.files.wordpress.com/2019/06/af6qgi3si4t4i7zhf6oc.png"""
        
        VoutIzk = c.voltage(Vz.V - (Iz.A - Izk.A)*Zz.ohms)
        Izm = c.current(Pzmax.W / Vz.V)
        VoutIzm = c.voltage(Vz.V + (Izm.A - Iz.A)*Zz.ohms)
        
        R = c.resistance(
        (Vin.V - VoutIzm.V) / Izm.A
        )
        
        Itotal = c.current((Vin.V - VoutIzk.V) / R.ohms)
        Iload = c.current(Itotal.A - Izk.A)
        Rloadmin = c.resistance(VoutIzk.V / Iload.A)
        
        
        self.answer = f"""{VoutIzk.V:5.5} V, {VoutIzm.V:5.5} V, {R.ohms:5.5} ohms, {Rloadmin.ohms:5.5} ohms"""


class floyd_3_8_a:
    def __init__(self,*args,**kwargs): 
        
        R1 = c.resistance(random.randint(1,5)*1000)
        Vz1 = c.voltage(int(ran.main(33))/10)
        Vz2 = c.voltage(int(ran.main(51))/10)
        
        self.question = f"""With a peak input voltage of 50V, determine the minimum and maximum voltage of the output waveform for the zener limiting circuit. R = {R1.kohms:5.5} kohms, top zener voltage = {Vz1.V:5.5} V, bottom zener voltage = {Vz2.V:5.5} V. https://lesliecaminadecom.files.wordpress.com/2019/06/6d29y6yjxl43lz61pue2.png"""
        
        vmaximum = c.voltage(Vz2.V + 0.7)
        vminimum = c.voltage(-(Vz1.V + 0.7))
        
        self.answer = f"""{vmaximum.V:5.5} V, {vminimum.V:5.5} V"""
#-----------------------------------------------------------

class boylestad_2_4():
    def __init__(self):
        E = c.voltage(ran.main(8))
        VD = c.voltage(0.7)
        R = c.resistance(ran.main(2.2), 'kohms')

        I = c.current(
            (E.V - VD.V) / R.ohms
            )

        self.question = f"""For the series diode configuration of https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-13-47-10-1.png, determine ID. E = {E.V:5.5} V, R = {R.kohms:5.5} kohms"""
        self.answer = f"""{I.mA:5.5} mA"""

class boylestad_2_6():
    def __init__(self):
        E = c.voltage(ran.main(0.5))
        R = c.resistance(ran.main(1.2), 'kohms')
        VD = c.voltage(0.7)
        if E.V < 0.7:
            I = c.current(0)
        else:
            I = c.current(
                (E.V - VD.V) / R.ohms
                )

        self.question = f"""For the series diode configuration https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-13-56-29.png, determine ID. E = {E.V:5.5} V, R = {R.kohms:5.5} kohms"""
        self.answer = f"""{I.mA:5.5} mA"""

class boylestad_2_9():
    def __init__(self):
        E1 = c.voltage(ran.main(10))
        E2 = c.voltage( - ran.main(5))
        VD = c.voltage(0.7)
        R1 = c.resistance(4.7e3, 'e12')
        R2 = c.resistance(2.2e3, 'e12')
        equation = sympy.Eq(
            - E1.V + x*(R1.ohms + R2.ohms) - VD.V - E2.V, 0 
            )
        I = c.current(sympy.solveset(equation, x).args[0])
        V1 = c.voltage(I.A * R1.ohms)
        V2 = c.voltage(I.A * R2.ohms)
        VO = V2
        self.question = f"""Determine I, V1, V2 and VO for the series dc configuration https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-14-16-32.png, E1 = {E1.V:5.5} V, E2 = {E2.V:5.5} V, R1 = {R1.kohms:5.5} kohms, R2 = {R2.kohms:5.5} kohms"""
        self.answer= f"""{I.mA:5.5} mA, {V1.V:5.5} V, {V2.V:5.5} V, {VO.V:5.5} V"""

class boylestad_2_10():
    def __init__(self):
        E = c.voltage(ran.main(10))
        R = c.resistance(330, 'e12')
        VD = c.voltage(0.7)

        I1 = c.current(
            (E.V - VD.V) / R.ohms
            )

        ID1 = c.current(I1.A / 2)
        ID2 = ID1
        VO = VD

        self.question = f"""Determine VO, I1, ID1, ID2 for the parallel diode configuration of https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-14-25-46.png, E = {E.V:5.5} V, R = {R.ohms:5.5} ohms"""
        self.answer = f"""{VO.V:5.5} V, {I1.mA:5.5} mA, {ID1.mA:5.5} mA, {ID2.mA:5.5} mA"""

class boylestad_2_11():
    def __init__(self):
        VTO = c.voltage(2)
        VBR = c.voltage(3)
        E = c.voltage(ran.main(8))
        ION = c.current(ran.main(20), 'mA')

        R = c.resistance(
            (E.V - VTO.V) / ION.A
            )

        self.question = f"""There are two LEDS that can be used as a polarity detector. Apply a positive source and the green light results. Negative supplies result in a red light. Find the resistor R to ensure that a current of {ION.mA:5.5} mA through the "on" diode for the configuration in (https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-14-36-57.png). Both diodes have a reverse breakdown voltage of {VBR.V:5.5} V and an average turn-on voltage of {VTO.V:5.5} V. E = {E.V:5.5} V"""
        self.answer = f"""{R.ohms:5.5} ohms"""

class boylestad_2_12():
    def __init__(self):
        E = c.voltage(ran.main(12))
        R = c.resistance(2.2e3, 'e12')

        I = c.current(
            (E.V - 0.7) / R.ohms
            )

        VO = c.voltage( I.A * R.ohms )

        self.question = f"""Determine the voltage V0 for the network of https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-14-42-22.png. E = {E.V:5.5} V"""
        self.answer = f"""{VO.V:5.5} V"""

class boylestad_2_13():
    def __init__(self):
        repeat = True
        while repeat:

            E = c.voltage(ran.main(20))
            R1 = c.resistance(3.3e3, 'e12')
            R2 = c.resistance(5.6e3, 'e12')

            I1 = c.current( 0.7 / R1.ohms)

            equation = sympy.Eq(
                - E.V + 0.7 + 0.7 + x * R2.ohms, 0
                )

            I2 = c.current(sympy.solveset(equation, x).args[0])
            ID2  = c.current(I2.A - I1.A)
            
            if I2.A > I1.A:
                repeat = False

        self.question = f"""Determine the currents I1, I2, and ID2 for the network (https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-14-49-25.png). E = {E.V:5.5} V, R1 = {R1.kohms:5.5} kohms, R2 = {R2.kohms:5.5} kohms"""
        self.answer = f"""{I1.mA:5.5} mA, {I2.mA:5.5} mA, {ID2.mA:5.5} mA"""

class boylestad_2_14():
    def __init__(self):
        E = c.voltage(ran.main(10))
        R = c.resistance(1000, 'e12')

        I = c.current(
            (E.V - 0.7) / R.ohms
            )

        VO = c.voltage( I.A * R.ohms )

        self.question = f"""Determine VO for the network of (https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-14-17-25-05.png). E = {E.V:5.5} V and R = {R.kohms:5.5} kohms"""
        self.answer = f"""{VO.V:5.5} V"""

class boylestad_2_15():
    def __init__(self):
        E = c.voltage(ran.main(10))
        zero = c.voltage(0)
        E1 = random.choice([E, zero])
        E2 = random.choice([E, zero])
        R = c.resistance(1000, 'e12')

        if E1.V > 0 and E2.V > 0 :
            VO = E
        else:
            VO = c.voltage(0.7)

        self.question = f"""Determine the output level for the circuit at (https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-15-07-55-52-1.png). E = {float(E.V):5.5}, E1 = {float(E1.V):5.5} V, E2 = {float(E2.V):5.5} V, R = {R.kohms:5.5} kohms."""
        self.answer = f"""{VO.V:5.5} V"""

class boylestad_2_16():
    def __init__(self):
        VI_peak = c.voltage(ran.main(20))
        R = c.resistance(2000, 'e12')
        VI_peak_2 = c.voltage(VI_peak.V * 10)

        VDC1 = c.voltage( - VI_peak.V * 0.318)
        VDC2 = c.voltage( - (VI_peak.V - 0.7 ) * 0.318)
        VDC3 = c.voltage( - (VI_peak_2.V - 0.7) * 0.318)

        self.question = f"""Determine the output voltage of the circuit and the input voltage shown (https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-15-08-13-58.png) if a) Vi(peak) = {VI_peak.V:5.5} V, and an ideal diode. b) Vi(peak) = {VI_peak.V:5.5} V, and a silicon diode. c) Vi(peak) = {VI_peak_2.V:5.5} V,  and a silicon diode. In all cases, R = {R.kohms:5.5}"""

        self.answer = f"""{VDC1.V:5.5} V, {VDC2.V:5.5} V, {VDC3.V:5.5} V"""

class boylestad_2_17():
    def __init__(self):
        VI_peak = c.voltage(ran.main(10))
        R = c.resistance(ran.main(2000), 'e12')

        VO = c.voltage( (VI_peak.V / 2) * 0.636 )
        PIV = c.voltage(VI_peak.V / 2)

        self.question = f"""Determine the output waveform for the network on (https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-15-08-24-01.png) and calculate the output DC level and the required PIV of each diode. Vi(peak) = {VI_peak.V:5.5} V and all resistors are {R.kohms:5.5} kohms"""
        self.answer = f"""{PIV.V:5.5} V"""









        
        















        