from generator import constants_conversions as co
from generator import random_handler as ran
import sympy as sym
import math
import random
import fractions

x, y, z = sym.symbols('x y z', real = True)#generic variables

class Wien_Bridge_Oscillator():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		try:
			c_1 = co.capacitance(ran.main(kwargs['c']))
			r_1 = co.resistance(ran.main(kwargs['r']))
		except:
			c_1 = co.capacitance(ran.main(10) , 'nF')
			r_1 = co.resistance(ran.main(10), 'e12')

		f = co.frequency(
			1 / ( math.pi * 2 * r_1.ohms * c_1.F )
			)

		self.c = c_1
		self.r = r_1
		self.frequency = f
		self.A = 3
		self.B = fractions.Fraction(1,3)


class Phase_Shift_Oscillator():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		try:
			c = co.capacitance(ran.main(kwargs['c']))
			r = co.resistance(ran.main(kwargs['r']))
		except:
			c = co.capacitance(ran.main(1), 'nF')
			r = co.resistance(ran.main(10), 'e12')

		f = co.frequency(
			1 / ( 2 * math.pi * r.ohms * c.F * math.sqrt(6))
			)

		self.c = c
		self.r = r
		self.frequency = f
		self.A = 29
		self.B = fractions.Fraction(1, self.A)

class Colpitts_Oscillator():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		try:
			c1 = co.capacitance(ran.main(kwargs['c1']))
			l = co.inductance(ran.main(kwargs['l']))
			c2 = co.capacitance(ran.main(kwargs['c2']))

		except:
			c1 = co.capacitance(ran.main(100e-9), 'e12')
			c2 = c1
			l = co.inductance(ran.main(50e-3), 'e12')

		ct = c1.series(c2)	

		frequency = co.frequency(
			1 / (2 * math.pi * math.sqrt(l.H * ct.F))
			)

		try:
			q = ran.main(kwargs['q'])
		except:
			q = random.uniform(5, 100)

		frequency_loaded = co.frequency(frequency.Hz * math.sqrt(q**2 / (q**2 + 1)))

		self.c1 = c1
		self.c2 = c2
		self.l = l
		self.A = c1.F / c2.F
		self.B = 1/self.A

		self.frequency = frequency
		self.q = q
		self.frequency_loaded = frequency_loaded

class Clapp_Oscillator():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		try:
			c1 = co.capacitance(ran.main(kwargs['c1']))
			c2 = co.capacitance(ran.main(kwargs['c2']))
			c3 = co.capacitance(ran.main(kwargs['c3']))
			l = co.inductance(ran.main(kwargs['l']))
		except:
			c1 = co.capacitance(ran.main(100e-9), 'e12')
			c2 = c1
			l = co.inductance(ran.main(50e-3), 'e12')
			c3 = co.capacitance(ran.main(10e-9), 'e12')


		ct = c1.series(c2).series(c3)

		f = co.frequency(
			1 / (math.pi * 2 * math.sqrt(ct.F * l.H))
			)

		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		self.l = l
		self.f = f
		self.description = description

class Hartley_Oscillator():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		try:

			l1 = co.inductance(ran.main(kwargs['l1']))
			l2 = co.inductance(ran.main(kwargs['l2']))
			c = co.capacitance(ran.main(kwargs['c']))
		except:
			c = co.capacitance(ran.main(100e-9), 'e12')
			l1 = co.inductance(ran.main(25e-3), 'e12')
			l2 = co.inductance(ran.main(25e-3), 'e12')


		lt = l1.series(l2)

		f = co.frequency(
			1 / ( math.pi * 2 * math.sqrt(lt.H * c.F))
			)

		self.l1 = l1
		self.l2 = l2
		self.c = c
		self.frequency = f
		self.A = L2.H / L1.H
		self.B = 1 / self.A


class Triangular_Wave_Generator():
	def __init__(self):
		pass

	def init_random(self, **kwargs):
		#for circuit information, see floyd chapter on oscillators
		try:
			r1 = co.resistance(ran.main(kwargs['r1']))
			r2 = co.resistance(ran.main(kwargs['r2']))
			r3 = co.resistance(ran.main(kwargs['r3']))
			c = co.capacitance(ran.main(kwargs['c']))
		except:
			r1 = co.resistance(ran.main(10), 'e12')
			r2 = co.resistance(ran.main(33), 'e12')
			r3 = co.resistance(ran.main(10), 'e12')
			c = co.capacitance(ran.main(10e-12), 'e12')

		f = co.frequency((1 / (4 * r1.ohms * c.F) ) * ( r2.ohms / r3.ohms) )

		self.r1 = r1
		self.r2 = r2
		self.r3 = r3
		self.c = c
		self.frequency = f

class Astable_555():
	def __init__(self):
		pass

	def init_random(self, **kwargs):

		try:
			r1 = co.resistance(ran.main(kwargs['r1']))
			r2 = co.resistance(ran.main(kwargs['r2']))
			c = co.capacitance(ran.main(kwargs['c']))
		except:
			r1 = co.resistance(ran.main(2.2e3), 'e12')
			r2 = co.resistance(ran.main(4.7e3), 'e12')
			c = co.capacitance(ran.main(22E-9), 'e12')

		t_high = co.time(math.log(2) * (r1.ohms + r2.ohms ) * c.F )
		t_low = co.time(math.log(2) * r2.ohms * c.F)
		period = co.time(t_high.s + t_low.s)

		#print('capacitance check: ', c.F)
		f = co.frequency(
			(1 / math.log(2) )/ ((r1.ohms + 2 * r2.ohms ) * c.F)
			)

		duty_cycle = co.percentage( 
			(r1.ohms + r2.ohms)  / 
			(r1.ohms + 2 * r2.ohms ), 'decimal'	)

		self.r1 = r1
		self.r2 = r2
		self.c = c
		self.time_high = t_high
		self.time_low = t_low
		self.period = period
		self.frequency = f
		self.duty_cycle = duty_cycle


#negative feedback classes
class Amplifier():
	def __init__(self):
		input_impedance = co.resistance(random.uniform(500, 5e6))
		output_impedance = co.resistance(random.uniform(100, 1e6))
		open_loop_gain = random.uniform(100, 100e6)
		distortion = co.percentage(random.uniform(0, 10), 'percent')
		bandwidth = co.frequency(random.uniform(10_000, 1e9))

		self.zi = input_impedance
		self.zo = output_impedance
		self.aol = open_loop_gain
		self.distortion = distortion
		self.bandwidth = bandwidth

class Feedback_Network():
	def __init__(self):
		feedback_factor = fractions.Fraction(
			1, random.randint(1,10)
			)

		self.B = feedback_factor

class Negative_Feedback():
	def __init__(self):
		a = Amplifier()
		b = Feedback_Network()
		types = ['voltage-series',
		'voltage-shunt',
		'current-series',
		'current-shunt',
		'series-series',
		'series-shunt',
		'shunt-series',
		'shunt-shunt']

		network = random.choice(types)

		loop_gain = b.B * a.aol
		factor = 1 + loop_gain
		acl = a.aol / factor
		bcl =co.frequency( a.bandwidth.Hz * factor)
		distortion_cl = co.percentage( a.distortion.percent / factor ,'percent')
		
		if network == 'series-series' or network == 'series-shunt' or network == 'voltage-series' or network == 'current-series':
			zicl = co.resistance(a.zi.ohms * factor)
		else:
			zicl = co.resistance( a.zi.ohms / factor)

		if network == 'series-series' or network == 'shunt-series' or network == 'current-series' or network == 'current-shunt':
			zocl = co.resistance( a.zo.ohms * factor )
		else:
			zocl = co.resistance( a.zo.ohms / factor )

		self.aol = a.aol
		self.acl = acl
		self.bol = a.bandwidth
		self.bcl = bcl
		self.ziol = a.zi
		self.zool = a.zo
		self.zicl = zicl
		self.zocl = zocl
		self.type = network
		self.distortion_ol = a.distortion
		self.distortion_cl = distortion_cl
		self.feedback_factor = b.B

class floyd_16_1():
	def __init__(self):
		wb = Wien_Bridge_Oscillator()
		wb.init_random()

		self.question = f"""Determine the resonant frequency for the Wien-Bridge oscillator with R1 = R2 = {wb.r.kohms:.4} kohms and C1 = C2 = {wb.c.uF:.4} uF."""
		self.answer = f"""{wb.frequency.kHz:.4} kHz"""

class floyd_16_2():
	def __init__(self):
		pso = Phase_Shift_Oscillator()
		pso.init_random()

		self.question = f"""Determine the value of RF necessary in a phase shift oscillator if R1 = R2 = R3 = {pso.r.kohms:.4} kohms and C = {pso.c.uF:.4} uF."""

		rf = co.resistance( 29 * pso.r.ohms )
		self.answer = f"""{rf.kohms:.4} kohms"""

class floyd_16_2_b():
	def __init__(self):
		pso = Phase_Shift_Oscillator()
		pso.init_random()

		self.question  = f"""Determine the frequency of oscillation of a phase-shift oscillator if R1 = R2 = R3 = {pso.r.kohms:.4} kohms and C = {pso.c.uF:.4} uF"""
		self.answer = f"""{pso.frequency.kHz:.4} kHz"""

class floyd_16_3():
	def __init__(self):
		cp = Colpitts_Oscillator()
		cp.init_random()

		self.question = f"""Determine the frequency of a Colpitts oscillator with frequency selecting components C1 = {cp.c1.uF:.4} uF, C2 = {cp.c2.uF:.4} uF and L = {cp.l.mH:.4} mH. Assume that that the Q factor of the circuit is {cp.q:.4}."""
		self.answer = f"""{cp.frequency_loaded.kHz:.4} kHz""" 

class floyd_16_4():
	def __init__(self):
		twg = Triangular_Wave_Generator()
		twg.init_random()

		self.question = f"""Determine the frequency of oscillation of the circuit which is a triangular wave generator that utilizes hysteresis. R1 = {twg.r1.kohms:.4} kohms, R2 = {twg.r2.kohms:.4} kohms, R3 = {twg.r3.kohms:.4} kohms, and C = {twg.c.uF:.4} uF. https://lesliecaminadecom.files.wordpress.com/2020/01/screenshot-from-2020-01-25-19-03-23.png"""

		self.answer = f"""{twg.frequency.kHz:.4} kHz"""

class floyd_16_6():
	def __init__(self):
		ne555 = Astable_555()
		ne555.init_random()

		self.question = f"""A 555 timer configured to run in astable mode (oscillator) has R1 (VCC to DISCH) = {ne555.r1.kohms:.4} kohms, R2 (DISCH to THR/TRG) = {ne555.r2.kohms:.4} kohms and Cext = {ne555.c.uF:.4} uF. Determine the frequency of the output and the duty cycle."""
		self.answer = f"""{ne555.frequency.kHz:.4} kHz, {ne555.duty_cycle.percent:.4} %"""

class no_reference_1():
	def __init__(self):
		n = Negative_Feedback()

		self.question = f"""A {n.type} negative-feedback network consists of an amplifier with an open-loop gain of {n.aol:.4}, input impedance of {n.ziol.kohms:.4} kohms, and an output impedance of {n.zool.kohms:.4} kohms. Determine the closed-loop gain of the negative-feedback network if the feedack factor is {n.feedback_factor}."""
		self.answer = f"""{n.acl:.10} """

class no_reference_2():
	def __init__(self):
		n = Negative_Feedback()
		self.question = f"""A {n.type} negative-feedback network consists of an amplifier with an open-loop gain of {n.aol:.4}, input impedance of {n.ziol.kohms:.4} kohms, and an output impedance of {n.zool.kohms:.4} kohms. Determine the closed-loop input impedance of the negative-feedback network if the feedback factor is {n.feedback_factor}"""
		self.answer = f"""{n.zicl.kohms:.4} kohms"""

class no_reference_3():
	def __init__(self):
		n = Negative_Feedback()
		self.question = f"""A {n.type} negative-feedback network consists of an amplifier with an open-loop gain of {n.aol:.4}, input impedance of {n.ziol.kohms:.4} kohms, and an output impedance of {n.zool.kohms:.4} kohms. Determine the closed-loop output impedance of the negative-feedback network if the feedback factor is {n.feedback_factor}"""
		self.answer = f"""{n.zocl.kohms:.4} kohms """	
