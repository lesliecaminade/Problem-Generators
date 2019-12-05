import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

class jma_1_127_a:
    def __init__(self, *args, **kwargs):
        
        power = c.power(ran.main(40))
        voltage = c.voltage(ran.main(60))
        
        regen = 1
        while regen:
            efficiency = c.percentage(ran.main(70), 'percent')
            if efficiency.percent > 0  and efficiency.percent < 100:
                regen = 0
        
        self.question = f"""A transistor RF power amplifier operating class C is designed to produce {power.W} W output with a supply voltage of {voltage.V} V. If the efficiency is {efficiency.percent} %, what is the average collector current?"""
        
        power_source = c.power(
        power.W / efficiency.decimal
        )
        
        current = c.current(
        power_source.W / voltage.V
        )
        
        self.answer = f"""Collector current = {current.A} A"""
        
class jma_1_127_b:
    def __init__(self, *args, **kwargs):
        
        regen = 1
        while regen:
            modulation = c.percentage(ran.main(100), 'percent')
            if modulation.percent < 100:
                regen = 0
        
        power_carrier = c.power(ran.main(25))
        
        regen = 1
        while regen:
            efficiency = c.percentage(ran.main(70), 'percent')
            if efficiency.percent < 100:
                regen = 0
                
        
        self.question = f"""The power amplifier of an AM transmitter has an output carrier power of {power_carrier.W} W and an efficiency of {efficiency.percent} % and is collector-modulated. How much audio power will have to be supplied to this stage for {modulation.percent}% modulation?"""

        
        power_sideband = c.power(
        power_carrier.W * (modulation.decimal**2 / 2)
        )
        
        power_modulation = c.power(
        power_sideband.W / efficiency.decimal
        )
        
        
        self.answer=  f"""Audio power required = {power_modulation.W} W"""
        
class jma_1_128:
    def __init__(self, *args, **kwargs):
        
        regen = 1
        while regen:
            lowtemp = c.temperature(ran.main(-5), 'C')
            if lowtemp.C < 20:
                regen = 0
                
        regen = 1
        while regen:
            hightemp = c.temperature(ran.main(35), 'C')
            if hightemp.C > 20:
                regen = 0
        
        tempcoe_ppmperdegC = random.randint(1,5)
        frequency_20 = c.frequency(ran.main(146), 'MHz')
        
        self.question = f"""A portable radio transmitter has to operate at a temperature from {lowtemp.C} degC to {hightemp.C} degC. If its signal is derived from a crystal oscillator with a temperature coefficient of {tempcoe_ppmperdegC} ppm/degC and it transmits at exactly {frequency_20.MHz} MHz at 20 degC, find the transmitting frequency at the lower extreme of the operating temperature range."""
        
        
        fout = c.frequency(
        frequency_20.Hz + (tempcoe_ppmperdegC/1e6) * frequency_20.Hz * ( lowtemp.C - 20 ) 
        )
        
        self.answer= f"""Frequency at the lower temperature end = {fout.MHz} MHz"""
        
class jma_1_129:
    def __init__(self, *args, **kwargs):
        
        secondsperyear = c.time(ran.main(125))
        hoursperyear = c.time(8760, 'hours')
        
        
        self.question = f"""A quartz watch is guaranteed accurate to {secondsperyear.s} secondsperyear. Assuming a year has 8760 hrs, calculate the accuracy of the crystal oscillator in the watch in parts per million."""
        
        ppm = ( secondsperyear.s / hoursperyear.s ) * 1e6
        
        self.answer = f"""Accuracy = {ppm} ppm"""
        
class jma_1_130:
    def __init__(self, *args, **kwargs):
        
        
        Q = ran.main(110)
        inductance = c.inductance(ran.main(10), 'uH')
        
        
        self.question = f"""A TRF receiver is to be designed with a single tuned circuit using a {inductance.uH} uH inductor. Calculate the capacitance range of the variable capacitor requrired to cover the entire AM band (535 - 1605 kHz) and also calculate the bandwidth of this receiver at 535 kHz and 1605 kHz (Assume Q = {Q})."""
        
        
        capacitance_low = c.capacitance(
        1 / (inductance.H * (2 * math.pi * 535e3)**2)
        )
        
        capacitance_high = c.capacitance(
        1 / (inductance.H * (2 * math.pi * 1605e3)**2)
        )
        
        bw_low = c.frequency(
        535e3 / Q
        )
        
        bw_high = c.frequency(
        1605e3 / Q
        )
        
        self.answer = f"""Capacitance range: {capacitance_low.nF} nF to {capacitance_high.pF} pF
Bandwidth at low end = {bw_low.kHz} kHz
Bandwidth at high end = {bw_high.kHz} kHz"""

class jma_1_131:
    def __init__(self, *args, **kwargs):
        
        regen = 1
        while regen:
            frf = c.frequency(ran.main(600), 'kHz')
            if frf.kHz > 535 and frf.kHz < 1605:
                regen = 0
        
        Q = ran.main(60)
        
        self.question = f"""An AM receiver is tuned to broadcast station at {frf.kHz} kHz. Calculate the image frequency rejection in Db, assuming that the input filter consists of one tuned circuit with a Q of {Q}"""
        
        
        fimage = c.frequency(
        frf.Hz + 2 * 455e3
        )
        
        rho = (fimage.Hz / frf.Hz) - (frf.Hz / fimage.Hz)
        
        ifrr_dB = 20 * math.log( math.sqrt(1 + Q**2 * rho**2 ), 10)
        
        self.answer= f"""Image frequency rejection ratio = {ifrr_dB} dB"""
        
class jma_1_132:
    def __init__(self, *args, **kwargs):
        
        Q = ran.main(75)
        regen = 1
        while regen:
            frf = c.frequency(ran.main(100.1), 'MHz')
            if frf.MHz > 88 and frf.MHz < 108:
                regen = 0
                
        self.qusetion = f"""A receiver has two uncoupled tuned circuits before the mixer, each with a Q of {Q}. The signal frequency is {frf.MHz} MHz. The IF is 10.7 MHz. The local oscillator uses high-side injection. Calculate the image rejection ratio in dB."""
        
        fimage = c.frequency(
        frf.Hz + 2 * 10.7e6
        )
        
        rho = (fimage.Hz / frf.Hz) - (frf.Hz / fimage.Hz)
         
        ifrr_db_total = 2 * 20 * math.log( math.sqrt(1 + (Q**2 * rho**2)), 10)
        
        self.answer = f"""Image frequency rejection ratio = {ifrr_db_total} dB"""
        
class jma_1_133:
    def __init__(self, *args, **kwargs):
        
        Qp = ran.main(50)
        Qs = ran.main(40)
        
        self.question = f"""An IF transformer of a radio receiver operates at 455 kHz. The primary circuit has a Q of {Qp} and the secondary has a Q of {Qs}. Find tha bandwidth using the optimum coupling factor."""
        
        kc = 1 / math.sqrt(Qp * Qs)
        
        ko = 1.5 * kc
        
        bandwidth = c.frequency(
        ko * 455e3
        )
        
        self.answer = f"""Bandwidth = {bandwidth.kHz} kHz"""
        
class jma_1_135:
    def __init__(self, *args, **kwargs):
        
        signal_level = c.voltage(ran.main(450), 'uV')
        signal_level_2 = c.voltage(ran.main(1), 'uV')
        
        self.question = f"""When measuring the selectivity of a receiver, you discover that a signal level of {signal_level.uV} uV on an adjacent channel is required to give the same output as {signal_level_2.uV} uV on the channel to which the receiver is tuned. Calculate the adjacent channel selectivity in dB."""
        
        acs = 20 * math.log( signal_level.V / signal_level_2.V ,10)
        
        self.answer=f"""Adjacent channel selectivity = {acs} dB"""
        
class jma_1_137_a:
    def __init__(self, *args, **kwargs):
        
        sensitivity = c.voltage(ran.main(0.6), 'uV')
        bdr = c.dbvalue(ran.main(60), 'dB20')
        
        self.question = f"""A receiver has a sensitivity of {sensitivity.uV} uV and a blocking dynamic range of {bdr.dB20} dB. What is the strongest signal that can be present along with a {sensitivity.uV} uV signal without blocking taking place?"""
        
        vinput = c.voltage(
        sensitivity.V * bdr.unitless
        )
        
        self.answer = f"""Strongest signal without blocking = {vinput.uV} uV"""
        
class jma_1_137_b:
    def __init__(self, *args, **kwargs):
        
        dr = c.dbvalue(ran.main(85), 'dB')
        sensitivity = c.power(ran.main(1.5), 'nW')
        
        self.question = f"""A receiver has a dynamic range of {dr.dB} dB. It has {sensitivity.nW} nW sensitivity threshold. Determine the maximum allowable input signal."""

        equation = sym.Eq(
        85, 10 * sym.log(x / sensitivity.W,10)
        )
        
        power_max_set = sym.solveset(equation, x)
        power_max_list = list(power_max_set)

        power_max = c.power(
        power_max_list[0]
        )
        
        self.answer =f"""Maximum allowable input signal = {power_max.W} W"""
        

        
        
        
        
        
        
        
        
        
        
        
