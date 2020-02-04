from generator import random_handler as ran
import math
import random
from generator import constants_conversions as c
from est import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)


class jma_1_95:
    def __init__(self, *args, **kwargs):
    
        second = c.percentage(ran.main(2.5), 'percent')
        third = c.percentage(ran.main(1.25), 'percent')
        fundamental = c.voltage(ran.main(8), 'V')
        
    
        self.question = f"""Calculate the total harmonic distortion if the 2nd order and 3rd order are {second.percent:5.4} % and {third.percent:5.4} % respectively and the fundamental amplitude is {fundamental.V:5.4} V"""
        
        v2 = c.voltage(
        fundamental.V * second.decimal
        )
        
        v3 = c.voltage(
        fundamental.V * third.decimal
        )
        
        thd = c.percentage(
        math.sqrt( v2.V**2 + v3.V**2) / fundamental.V, 'decimal'
        )
        
        self.answer = f"""{thd.percent:5.4} %"""
        
class jma_1_98:
    def __init__(self, *args, **kwargs):
        
        bandwidth = c.frequency(ran.main(10.7), 'MHz')
        
        self.question = f"""Calculate the spectrum density and thermal noise power for a certain communication system with an IF bandwidth of {bandwidth.MHz:5.4} MHz"""

        spectrum_density = c.power(
        c.BOLTZMANNS_CONSTANT * 290
        )
        
        noise_power = c.power(
        c.BOLTZMANNS_CONSTANT * 290 * bandwidth.Hz
        )
        
        self.answer = f"""{spectrum_density.W:5.4} W/Hz, {noise_power.W:5.4} W"""

class jma_1_99_a:
    def __init__(self, *args, **kwargs):
        
        bandwidth = c.frequency(ran.main(5), 'MHz')
        input_resistance = c.resistance(ran.main(100), 'ohms')
        operating_temperature = c.temperature(ran.main(27), 'C')
        voltage_gain = ran.main(200)
        input_voltage = c.voltage(ran.main(6), 'uV')               
        
        self.question = f"""An amplifier operatin over a {bandwidth.MHz:5.4} MHz bandwidth has a {input_resistance.ohms:5.4} ohms input resistance. It is operating at {operating_temperature.C:5.4} degrees Celsius, has a voltage gain of {voltage_gain:5.4} and an input signal of {input_voltage.uV:5.4} uVrms. Calculate the output rms noise."""
        
        vinput = c.voltage( 
        math.sqrt( 4 * c.BOLTZMANNS_CONSTANT * operating_temperature.K * bandwidth.Hz * input_resistance.ohms )
        )
        
        voutput = c.voltage(
        voltage_gain * vinput.V
        )
        
        self.answer = f"""{voutput.V:5.4} V"""
        
class jma_1_99_b:
    def __init__(self, *args, **kwargs):
        
        r1temp = c.temperature(ran.main(300), 'K')
        r2temp = c.temperature(ran.main(400), 'K')
        r1resistance = c.resistance(ran.main(200), 'ohms')
        r2resistance = c.resistance(ran.main(300), 'ohms')
        loadresistance = c.resistance(ran.main(500), 'ohms')
        bandwidth = c.frequency(ran.main(100), 'kHz')
        
        self.question = f"""The resistor R1 and R2 are connected in series at {r1temp.K:5.4} K and {r2temp.K:5.4} K temperatures respectively. If R1 is {r1resistance.ohms:5.4} ohms and R2 is {r2resistance.ohms:5.4} ohms, find the power produced at the load ( RL = {loadresistance.ohms:5.4} ohms ) over a bandwidth of {bandwidth.kHz:5.4} kHz."""
        
        noise_voltage = c.voltage(
        math.sqrt( 4 * c.BOLTZMANNS_CONSTANT * bandwidth.Hz * ( r1temp.K * r1resistance.ohms + r2temp.K * r2resistance.ohms ))
        )
        
        power_load = c.power(
        ( noise_voltage.V / math.sqrt(2) )**2 /  ( 2 * loadresistance.ohms ) 
        )
        
        self.answer = f"""{power_load.W:5.4} W"""
        
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
        
        self.question = f"""The first stage of a two-stage amplifier has a voltage gain of {g1:5.4}, a {rin1.ohms:5.4}-ohm input resistor, a {req1.ohms:5.4}-ohm equivalent noise resistance and a {rout1.kohms:5.4}-kohm output resistor. For the second stage, these values are {g2:5.4}, {rin2.kohms:5.4} kohms, {req2.kohms:5.4} kohms, and {rout2.Mohms:5.4} Mohms respectively. Calculate the equivalent input noise resistance."""
        
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
        
        self.answer = f"""{req.kohms:5.4} kohms"""
        
class jma_1_102_a:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(125), 'MHz')
        capacitance = c.capacitance(ran.main(23.5), 'pF')
        Q = ran.main(40)
        bandwidth = c.frequency(ran.main(10), 'kHz')
        
        self.question = f"""A parallel tuned circuit at the input of a radio receiver is tuned to resonate at {frequency.MHz:5.4} MHz by a capacitance {capacitance.pF:5.4} pF. The Q-factor of the circuit is {Q:5.4} and with a channel bandwidth of the receiver limited to {bandwidth.kHz:5.4} kHz  by the audio sections. Determine the effective noise voltage of this radio receiver tuned circuit."""
        
        rd = c.resistance(
        Q / (2 * math.pi * frequency.Hz * capacitance.F)
        )
        
        noise_voltage = c.voltage(
        math.sqrt(
        4 * c.BOLTZMANNS_CONSTANT * 290 * bandwidth.Hz * rd.ohms
        )
        )
        
        self.answer = f"""{noise_voltage.uV:5.4} uV"""
        
class jma_1_102_b:
    def __init__(self, *args, **kwargs):
        
        noise_voltage = c.voltage(ran.main(10), 'uV')
        input_impedance = c.resistance(ran.main(75), 'ohms')
        bandwidth = c.frequency(ran.main(200), 'kHz')
        
        self.question = f"""A diode noise generator is required to produce {noise_voltage.uV:5.4} uV of noise in a receiver with an input impedance of {input_impedance.ohms:5.4} ohms resistive, and a noise power bandwidth of {bandwidth.kHz:5.4} kHz. What must the current through the diode be?"""
        
        noise_current = c.current(
        noise_voltage.V / input_impedance.ohms
        )
        
        diode_current = c.current(
        noise_current.A**2 / (2 * c.CHARGE_ELECTRON * bandwidth.Hz)
        )
        
        self.answer = f"""{diode_current.mA:5.4} mA"""

class jma_1_104:
    def __init__(self, *args, **kwargs):
        
        spern_input = c.dbvalue(ran.main(100), 'unitless')
        spern_output = c.dbvalue(ran.main(20), 'unitless')
        
        self.question = f"""A transistor has a measured S/N power of {spern_input.unitless:5.4} and {spern_output.unitless:5.4} at its output. Determine the noise figure of the transistor."""
        
        noise_factor = c.dbvalue(
        spern_input.unitless / spern_output.unitless, 'unitless'
        )
        
        self.answer = f"""{noise_factor.dB:5.4} dB"""
        
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
            
            self.question = f"""A three-stage amplifier is to have an overall noise temperature no greater than {teq.K:5.4} K. The overall gain of the amplifier is to be at least {total_gain.dB:5.4} dB. The amplifier is to be built by adding a low-noise first stage to an existing amplifier with existing characteristics as follows: Stage 2 has {gain2.dB:5.4} dB power gain, {f2.dB:5.4} dB noise figure. Stage 3 has {gain3.dB:5.4} dB power gain and {f3.dB:5.4} dB noise figure. Calculate the maximum noise figure ( in dB ) that the first stage can have."""
            
            ft = c.dbvalue(
            1 + teq.K/290
            )
            
            f1 = c.dbvalue(
            ft.unitless - (((f2.unitless - 1)/gain2.unitless) + ((f3.unitless - 1)/(gain2.unitless * gain3.unitless)))
            )
            
            if f1.dB > 0:
                regen = 0
            
        self.answer = f"""{f1.dB:5.4} dB"""
        
class jma_1_108:
    def __init__(self, *args, **kwargs):
        
        powerlevel = c.dbvalue(ran.main(-27), 'dB')
        reference = c.dbvalue(ran.main(-24), 'dB')
        
        self.question = f"""Calculate the strength of a signal in dBmO if it has an absolute power level of {powerlevel.dB:5.4} dBm at {reference.dB:5.4} dBm TLP.""" 

        signal = c.dbvalue(
        powerlevel.dB - reference.dB, 'dB'
        )
        
        self.answer = f"""{signal.dB:5.4} dBmO"""
        
class jma_1_109_a:
    def __init__(self, *args, **kwargs):
        
        reference = c.dbvalue(ran.main(-4), 'dB')
        measurement = c.dbvalue(ran.main(-76), 'dB')
        
        self.question = f"""When measuring a voice channel at a {reference.dB:5.4} dB test point level, the meter reads {measurement.dB:5.4} dBm. Calculate the reading in dBrnCO."""
        
        reading = c.dbvalue(
        measurement.dB + 90 - reference.dB, 'dB'
        )
        
        self.answer = f"""{reading.dB:5.4} dBrnCO"""
        
class jma_1_109_b:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(1000), 'Hz')
        signal = c.dbvalue(ran.main(70), 'dB')
        reference = c.dbvalue(ran.main(-9), 'dB')
        spern = c.dbvalue(ran.main(30), 'dB')
        
        self.question = f"""A {frequency.kHz:5.4} kHz tone has a level of {signal.dB:5.4} dBrnC at a point that is {reference.dB:5.4} dB TLP. What would be the maximum C-message weighted noise level at the 0 TLP for a signal-to-noise ratio of {spern.dB:5.4} dB?"""

        signal_dbrnco = c.dbvalue(
        signal.dB - reference.dB, 'dB'
        )
        
        noise_dbrnco = c.dbvalue(
        signal_dbrnco.dB - spern.dB, 'dB'
        )
        
        self.answer = f"""{noise_dbrnco.dB:5.4} dBrnCO"""
        
class jma_1_110:
    def __init__(self, *args, **kwargs):
        
        noise_dBmp = c.dbvalue(ran.main(-42), 'dB')
        reference_dBr = c.dbvalue(ran.main(-5), 'dB')
        
        self.question = f"""A {noise_dBmp.dB:5.4} dBmp of noise at a {reference_dBr.dB:5.4} dBr point would be reported as _________ dBmOp."""
        
        noise_dBmOp = c.dbvalue(
        noise_dBmp.dB - reference_dBr.dB, 'dB'
        )
        
        self.answer= f"""{noise_dBmOp.dB:5.4} dBmOp"""
        
class jma_1_112:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(1), 'kHz')
        signal_dBm = c.dbvalue(ran.main(4), 'dB')
        level_tlp = c.dbvalue(ran.main(10), 'dB')
        attenuation = c.dbvalue(ran.main(5), 'dB')
        
        self.question = f"""A {frequency.kHz:5.4} kHz test tone is inserted at a local loop with an amplitude of + {signal_dBm.dB:5.4} dBm and is transmitted towards the central office. In this direction the loop has a level of + {level_tlp.dB:5.4} dB TLP, because the signal will be attenuated towards the central office (about {attenuation.dB:5.4} dB). Express the level of the tone in dBrnCO."""
        
        signal_dBrnc = c.dbvalue(
        signal_dBm.dB + 90, 'dB'
        )
        
        signal_dBrnco = c.dbvalue(
        signal_dBrnc.dB - level_tlp.dB - attenuation.dB, 'dB'
        )
        
        self.answer = f"""{signal_dBrnco.dB:5.4} dBrnCO"""
        
class jma_1_113:
    def __init__(self, *args, **kwargs):
        
        vu = ran.main(5)
        
        self.question = f"""Calculate the approximate talker power in dBm for a complex signal with VU meter readout of {vu:5.4} VU"""
        
        power = c.dbvalue(
        vu - 1.4, 'dB'
        )
        
        self.answer=  f"""{power.dB:5.4} dBm"""
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
