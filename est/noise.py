import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)


class jma_1_95:
    def __init__(self, *args, **kwargs):
    
        second = c.percentage(ran.main(2.5), 'percent')
        third = c.percentage(ran.main(1.25), 'percent')
        fundamental = c.voltage(ran.main(8), 'V')
        
    
        self.question = f"""Calculate the total harmonic distortion if the 2nd order and 3rd order are {second.percent} % and {third.percent} % respectively and the fundamental amplitude is {fundamental.V} V"""
        
        v2 = c.voltage(
        fundamental.V * second.decimal
        )
        
        v3 = c.voltage(
        fundamental.V * third.decimal
        )
        
        thd = c.percentage(
        math.sqrt( v2.V**2 + v3.V**2) / fundamental.V, 'decimal'
        )
        
        self.answer = f"""THD = {thd.percent} %"""
        
class jma_1_98:
    def __init__(self, *args, **kwargs):
        
        bandwidth = c.frequency(ran.main(10.7), 'MHz')
        
        self.question = f"""Calculate the spectrum density and thermal noise power for a certain communication system with an IF bandwidth of {bandwidth.MHz} MHz"""

        spectrum_density = c.power(
        c.BOLTZMANNS_CONSTANT * 290
        )
        
        noise_power = c.power(
        c.BOLTZMANNS_CONSTANT * 290 * bandwidth.Hz
        )
        
        self.answer = f"""Spectrum density = {spectrum_density.W} W/Hz
Noise power = {noise_power.W} W"""

class jma_1_99_a:
    def __init__(self, *args, **kwargs):
        
        bandwidth = c.frequency(ran.main(5), 'MHz')
        input_resistance = c.resistance(ran.main(100), 'ohms')
        operating_temperature = c.temperature(ran.main(27), 'C')
        voltage_gain = ran.main(200)
        input_voltage = c.voltage(ran.main(6), 'uV')               
        
        self.question = f"""An amplifier operatin over a {bandwidth.MHz} MHz bandwidth has a {input_resistance.ohms} ohms input resistance. It is operating at {operating_temperature.C} degrees Celsius, has a voltage gain of {voltage_gain} and an input signal of {input_voltage.uV} uVrms. Calculate the output rms noise."""
        
        vinput = c.voltage( 
        math.sqrt( 4 * c.BOLTZMANNS_CONSTANT * operating_temperature.K * bandwidth.Hz * input_resistance.ohms )
        )
        
        voutput = c.voltage(
        voltage_gain * vinput.V
        )
        
        self.answer = f"""Output voltage = {voutput.V} V"""
        
class jma_1_99_b:
    def __init__(self, *args, **kwargs):
        
        r1temp = c.temperature(ran.main(300), 'K')
        r2temp = c.temperature(ran.main(400), 'K')
        r1resistance = c.resistance(ran.main(200), 'ohms')
        r2resistance = c.resistance(ran.main(300), 'ohms')
        loadresistance = c.resistance(ran.main(500), 'ohms')
        bandwidth = c.frequency(ran.main(100), 'kHz')
        
        self.question = f"""The resistor R1 and R2 are connected in series at {r1temp.K} K and {r2temp.K} K temperatures respectively. If R1 is {r1resistance.ohms} ohms and R2 is {r2resistance.ohms} ohms, find the power produced at the load ( RL = {loadresistance.ohms} ohms ) over a bandwidth of {bandwidth.kHz} kHz."""
        
        noise_voltage = c.voltage(
        math.sqrt( 4 * c.BOLTZMANNS_CONSTANT * bandwidth.Hz * ( r1temp.K * r1resistance.ohms + r2temp.K * r2resistance.ohms ))
        )
        
        power_load = c.power(
        ( noise_voltage.V / math.sqrt(2) )**2 /  ( 2 * loadresistance.ohms ) 
        )
        
        self.answer = f"""Power at the load = {power_load.W} W"""
        
class jma_1_100:
    def __init__(self, *args, **kwargs):
        
        g1 = ran.main(10)
        rin1 = c.resistance(ran.main(600), 'ohms')
        req1 = c.resistance(ran.main(1600), 'ohms')
        rout1 = c.resistance(ran.main(27), 'kohms')
        
        g2 = ran.main(25)
        rin2 = c.resistance(ran.main(81), 'kohms')
        req2 = c.resistance(ran.main(10), 'kohms')
        rout2 = c.resistance(ran.main(1), 'Mohms')
        
        self.question = f"""The first stage of a two-stage amplifier has a voltage gain of {g1}, a {rin1.ohms}-ohm input resistor, a {req1.ohms}-ohm equivalent noise resistance and a {rout1.kohms}-kohm output resistor. For the second stage, these values are {g2}, {rin2.kohms} kohms, {req2.kohms} kohms, and {rout2.Mohms} Mohms respectively. Calculate the equivalent input noise resistance."""
        
        r1 = c.resistance(
        rin1.ohms + req1.ohms
        )
        
        r2 = c.resistance(
        rout1.parallel(rin2).ohms + req2.ohms
        )
        
        r3 = c.resistance(
        rout2.ohms
        )
        
        req = c.resistance(
        r1.ohms + (r2.ohms/g1**2) + (r3.ohms/(g1**2 * g2**2))
        )
        
        self.answer = f"""Equivalent input noise resistance = {req.kohms} kohms"""
        
class jma_1_102_a:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(125), 'MHz')
        capacitance = c.capacitance(ran.main(23.5), 'pF')
        Q = ran.main(40)
        bandwidth = c.frequency(ran.main(10), 'kHz')
        
        self.question = f"""A parallel tuned circuit at the input of a radio receiver is tuned to resonate at {frequency.MHz} MHz by a capacitance {capacitance.pF} pF. The Q-factor of the circuit is {Q} and with a channel bandwidth of the receiver limited to {bandwidth.kHz} kHz  by the audio sections. Determine the effective noise voltage of this radio receiver tuned circuit."""
        
        rd = c.resistance(
        Q / (2 * math.pi * frequency.Hz * capacitance.F)
        )
        
        noise_voltage = c.voltage(
        math.sqrt(
        4 * c.BOLTZMANNS_CONSTANT * 290 * bandwidth.Hz * rd.ohms
        )
        )
        
        self.answer = f"""Noise voltage = {noise_voltage.uV} uV"""
        
class jma_1_102_b:
    def __init__(self, *args, **kwargs):
        
        noise_voltage = c.voltage(ran.main(10), 'uV')
        input_impedance = c.resistance(ran.main(75), 'ohms')
        bandwidth = c.frequency(ran.main(200), 'kHz')
        
        self.question = f"""A diode noise generator is required to produce {noise_voltage.uV} uV of noise in a receiver with an input impedance of {input_impedance.ohms} ohms resistive, and a noise power bandwidth of {bandwidth.kHz} kHz. What must the current through the diode be?"""
        
        noise_current = c.current(
        noise_voltage.V / input_impedance.ohms
        )
        
        diode_current = c.current(
        noise_current.A**2 / (2 * c.CHARGE_ELECTRON * bandwidth.Hz)
        )
        
        self.answer = f"""Diode current = {diode_current.mA} mA"""

class jma_1_104:
    def __init__(self, *args, **kwargs):
        
        spern_input = c.dbvalue(ran.main(100), 'unitless')
        spern_output = c.dbvalue(ran.main(20), 'unitless')
        
        self.question = f"""A transistor has a measured S/N power of {spern_input.unitless} and {spern_output.unitless} at its output. Determine the noise figure of the transistor."""
        
        noise_factor = c.dbvalue(
        spern_input.unitless / spern_output.unitless, 'unitless'
        )
        
        self.answer = f"""Noise figure = {noise_factor.dB} dB"""
        
class jma_1_105:
    def __init__(self, *args, **kwargs):
        regen = 1
        while regen:
            gain2 = c.dbvalue(ran.main(20), 'dB')
            gain3 = c.dbvalue(ran.main(15), 'dB')
            gain1 = c.dbvalue(ran.main(10), 'dB')
            
            total_gain = c.dbvalue(
            gain1.dB + gain2.dB + gain3.dB, 'dB'
            )
            
            teq = c.temperature(ran.main(70), 'K')
            
            f2 = c.dbvalue(ran.main(3), 'dB')
            f3 = c.dbvalue(ran.main(6), 'dB')
            
            self.question = f"""A three-stage amplifier is to have an overall noise temperature no greater than {teq.K} K. The overall gain of the amplifier is to be at least {total_gain.dB} dB. The amplifier is to be built by adding a low-noise first stage to an existing amplifier with existing characteristics as follows: Stage 2 has {gain2.dB} dB power gain, {f2.dB} dB noise figure. Stage 3 has {gain3.dB} dB power gain and {f3.dB} dB noise figure. Calculate the maximum noise figure ( in dB ) that the first stage can have."""
            
            ft = c.dbvalue(
            1 + teq.K/290
            )
            
            f1 = c.dbvalue(
            ft.unitless - (((f2.unitless - 1)/gain2.unitless) + ((f3.unitless - 1)/(gain2.unitless * gain3.unitless)))
            )
            
            if f1.dB > 0:
                regen = 0
            
        self.answer = f"""Noise figure of stage 1 = {f1.dB} dB"""
        
class jma_1_108:
    def __init__(self, *args, **kwargs):
        
        powerlevel = c.dbvalue(ran.main(-27), 'dB')
        reference = c.dbvalue(ran.main(-24), 'dB')
        
        self.question = f"""Calculate the strength of a signal in dBmO if it has an absolute power level of {powerlevel.dB} dBm at {reference.dB} dBm TLP.""" 

        signal = c.dbvalue(
        powerlevel.dB - reference.dB, 'dB'
        )
        
        self.answer = f"""Signal strength = {signal.dB} dBmO"""
        
class jma_1_109_a:
    def __init__(self, *args, **kwargs):
        
        reference = c.dbvalue(ran.main(-4), 'dB')
        measurement = c.dbvalue(ran.main(-76), 'dB')
        
        self.question = f"""When measuring a voice channel at a {reference.dB} dB test point level, the meter reads {measurement.dB} dBm. Calculate the reading in dBrnCO."""
        
        reading = c.dbvalue(
        measurement.dB + 90 - reference.dB, 'dB'
        )
        
        self.answer = f"""Reading in dBrnCO = {reading.dB} dBrnCO"""
        
class jma_1_109_b:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(1000), 'Hz')
        signal = c.dbvalue(ran.main(70), 'dB')
        reference = c.dbvalue(ran.main(-9), 'dB')
        spern = c.dbvalue(ran.main(30), 'dB')
        
        self.question = f"""A {frequency.kHz} kHz tone has a level of {signal.dB} dBrnC at a point that is {reference.dB} dB TLP. What would be the maximum C-message weighted noise level at the 0 TLP for a signal-to-noise ratio of {spern.dB} dB?"""

        signal_dbrnco = c.dbvalue(
        signal.dB - reference.dB, 'dB'
        )
        
        noise_dbrnco = c.dbvalue(
        signal_dbrnco.dB - spern.dB, 'dB'
        )
        
        self.answer = f"""Noise level = {noise_dbrnco.dB} dBrnCO"""
        
class jma_1_110:
    def __init__(self, *args, **kwargs):
        
        noise_dBmp = c.dbvalue(ran.main(-42), 'dB')
        reference_dBr = c.dbvalue(ran.main(-5), 'dB')
        
        self.question = f"""A {noise_dBmp.dB} dBmp of noise at a {reference_dBr.dB} dBr point would be reported as _________ dBmOp."""
        
        noise_dBmOp = c.dbvalue(
        noise_dBmp.dB - reference_dBr.dB, 'dB'
        )
        
        self.answer= f"""Noise level = {noise_dBmOp.dB} dBmOp"""
        
class jma_1_112:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(1), 'kHz')
        signal_dBm = c.dbvalue(ran.main(4), 'dB')
        level_tlp = c.dbvalue(ran.main(10), 'dB')
        attenuation = c.dbvalue(ran.main(5), 'dB')
        
        self.question = f"""A {frequency.kHz} kHz test tone is inserted at a local loop with an amplitude of + {signal_dBm.dB} dBm and is transmitted towards the central office. In this direction the loop has a level of + {level_tlp.dB} dB TLP, because the signal will be attenuated towards the central office (about {attenuation.dB} dB). Express the level of the tone in dBrnCO."""
        
        signal_dBrnc = c.dbvalue(
        signal_dBm.dB + 90, 'dB'
        )
        
        signal_dBrnco = c.dbvalue(
        signal_dBrnc.dB - level_tlp.dB - attenuation.dB, 'dB'
        )
        
        self.answer = f"""Tone level = {signal_dBrnco.dB} dBrnCO"""
        
class jma_1_113:
    def __init__(self, *args, **kwargs):
        
        vu = ran.main(5)
        
        self.question = f"""Calculate the approximate talker power in dBm for a complex signal with VU meter readout of {vu} VU"""
        
        power = c.dbvalue(
        vu - 1.4, 'dB'
        )
        
        self.answer=  f"""Talker power  = {power.dB} dBm"""
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
