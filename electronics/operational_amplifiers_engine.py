from generator import constants_conversions as c
from generator import random_handler as ran
import sympy as sym
import math
import random

#import randomizer_2 as ran2

x, y, z = sym.symbols('x y z', real = True)#generic variables

class boylestad_10_1:
	def __init__(self,*args,**kwargs): 
		
		rc = c.resistance(ran.main(3.9e3))
		re = c.resistance(ran.main(3.3e3))
		vcc = c.voltage(ran.main(9))
		vee = c.voltage(ran.main(-9))
		
		
		self.question = f"""Determine the values of VC for a BJT differential amplifier with RC1 = RC2 = {rc.kohms:.4} ohms, common RE = {re.kohms:.4} kohms, VCC = {vcc.V:.4} V and VEE = {vee.V:.4} V."""
		
		ie = c.current(
		( - vee.V - 0.7) / 
		re.ohms
		)
		
		ic = c.current(ie.A / 2)
		
		vc = c.voltage( vcc.V - ic.A * rc.ohms )
		
		self.answer = f"""{vc.V:.4} V"""

class boylestad_10_2:
	def __init__(self,*args,**kwargs): 
		
		
		vcc = c.voltage(ran.main(9))
		vee = c.voltage(ran.main(-9))
		re = c.resistance(ran.main(43), 'kohms')
		rc = c.resistance(ran.main(47), 'kohms')
		beta = ran.main(75)
		ri = c.resistance(ran.main(20), 'kohms')
		vi = c.voltage(ran.main(2), 'mV')
		
		
		self.question = f"""Calculate the single-ended output voltage Vo1 for a BJT differential amplifier setup with VCC = {vcc.V:.4} V, VEE = {vee.V:.4} V, RC1 = RC2 = {rc.kohms:.4} kohms, RE = {re.kohms:.4} kohms,  BJT characteristics are ri = {ri.kohms:.4} kohms, and beta = {beta:.4}. The input voltage is {vi.mV:.4} mV."""

		ie = c.current(
		(- vee.V - 0.7) / 
		re.ohms
		)
		
		ic = c.current(ie.A / 2)
		
		vc = c.voltage( vcc.V - ic.A * rc.ohms )
		
		resmall = c.resistance( c.voltage(26, 'mV').V / ic.A ) 
		
		av = rc.ohms / (2 * resmall.ohms)
		
		vo = c.voltage( vi.V * av )
		
		self.answer = f"""{vo.V:.4} V"""
		
		
class boylestad_10_3:
	def __init__(self,*args,**kwargs): 
		
		
		vcc = c.voltage(ran.main(9))
		vee = c.voltage(ran.main(-9))
		re = c.resistance(ran.main(43), 'kohms')
		rc = c.resistance(ran.main(47), 'kohms')
		beta = ran.main(75)
		ri = c.resistance(ran.main(20), 'kohms')
		vi = c.voltage(ran.main(2), 'mV')
		
		
		self.question = f"""Calculate the common-mode gain for a BJT differential amplifier setup with VCC = {vcc.V:.4} V, VEE = {vee.V:.4} V, RC1 = RC2 = {rc.kohms:.4} kohms, RE = {re.kohms:.4} kohms,  BJT characteristics are ri = {ri.kohms:.4} kohms, and beta = {beta:.4}. The input voltage is {vi.mV:.4} mV."""

		ie = c.current(
		(- vee.V - 0.7) / 
		re.ohms
		)
		
		ic = c.current(ie.A / 2)
		
		vc = c.voltage( vcc.V - ic.A * rc.ohms )
		
		resmall = c.resistance( c.voltage(26, 'mV').V / ic.A ) 
		
		ac = (
		(beta * rc.ohms) / 
		(ri.ohms + 2*(beta + 1)*re.ohms)
		)
		
		self.answer = f"""{ac:.4}"""
		
class boylestad_10_4:
	def __init__(self,*args,**kwargs): 
		
		vdd = c.voltage(ran.main(9))
		rc = c.resistance(ran.main(10), 'kohms')
		beta1 = ran.main(75)
		ri = c.resistance(ran.main(11), 'kohms')
		r1 = c.resistance(ran.main(1), 'kohms')
		r2 = c.resistance(ran.main(8.2), 'kohms')
		r3 = c.resistance(ran.main(5.1), 'kohms')
		vee = c.voltage(ran.main(-9))
		beta2 = ran.main(75)
		ro = c.resistance(ran.main(200), 'kohms')
		
		self.question = f"""Calculate the common-mode voltage gain of a differential amplifier with VDD = {vdd.V:.4} V, RC1 = RC2 = {rc.kohms:.4} kohms, uses identical Q1 and Q2, and the BJT characteristics are beta = {beta1:.4} and ri = {ri.kohms:.4} kohms. This differential amplifier uses a BJT constant current source as a emitter resistance the BJT uses a limiter resistor R1 = {r1.kohms:.4} kohms, a bleeder resistor of R2 = {r2.kohms:.4} kohms, and an emitter resistance of R3 = {r3.kohms:.4} kohms. The BJT Q3 used in the constant current source has the characteristics ro = {ro.kohms:.4} kohms, and beta = {beta2:.4}."""
		
		ac = (
		( beta1 * rc.ohms ) / 
		( ri.ohms + 2*(beta1 + 1)*ro.ohms)
		)
		
		self.answer = f"""{ac:.4}"""
		
class boylestad_10_5:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(500), 'kohms')
		r1 = c.resistance(ran.main(100), 'kohms')
		v1 = c.voltage(ran.main(2))
		
		self.question = f"""An inverting amplifier opamp circuit has R1 = {r1.kohms:.4} kohms and RF = {rf.kohms:.4} kohms. What output voltage results for an input of V1 = {v1.V:.4} V?"""
		
		vo = c.voltage(
		(- rf.ohms * v1.V) / 
		( r1.ohms )
		)
		
		self.answer = f"""{vo.V:.4} V"""
		
class boylestad_10_6:
	def __init__(self,*args,**kwargs): 
		
		v1 = c.voltage(ran.main(2))
		rf = c.resistance(ran.main(500), 'kohms')
		r1 = c.resistance(ran.main(100), 'kohms')
		
		self.question = f"""Calculate the output voltage of a opamp noninverting amplifier for values V1 ={v1.V:.4} V, RF = {rf.kohms:.4} kohms, and R1 = {r1.kohms:.4} kohms."""
		
		vo = c.voltage((1 + (rf.ohms / r1.ohms)) * v1.V)
		
		self.answer = f"""{vo.V:.4} V"""
		
class boylestad_10_7:
	def __init__(self,*args,**kwargs): 
		
		temp = random.randint(0,1)
		rf = c.resistance(ran.main(1000), 'kohms')
		if temp == 0:
			v1 = c.voltage(ran.main(1))
			v2 = c.voltage(ran.main(2))
			v3 = c.voltage(ran.main(3))
			r1 = c.resistance(ran.main(500), 'kohms')
			r2 = c.resistance(ran.main(1), 'Mohms')
			r3 = c.resistance(ran.main(1), 'Mohms')
			
		if temp == 1:
			v1 = c.voltage(ran.main(-2))
			v2 = c.voltage(ran.main(3))
			v3 = c.voltage(ran.main(1))
			r1 = c.resistance(ran.main(200), 'kohms')
			r2 = c.resistance(ran.main(500), 'kohms')
			r3 = c.resistance(ran.main(1), 'Mohms')
			
		self.question = f"""Calculate the output voltage of an opamp summing amplifier for the set of voltages and resistors: RF = {rf.Mohms:.4} Mohms, V1 = {v1.V:.4} V, V2 = {v2.V:.4} V, V3 = {v3.V:.4} V, R1 = {r1.kohms:.4} kohms, R2 = {r2.kohms:.4} kohms, R3 = {r3.kohms:.4} kohms."""
		
		vo = c.voltage(- rf.ohms * ( v1.V / r1.ohms + v2.V / r2.ohms + v3.V / r3.ohms ))
		
		self.answer = f"""{vo.V:.4} V"""
		
class boylestad_10_8:
	def __init__(self,*args,**kwargs): 
		
		vio = c.voltage(ran.main(1.2), 'mV')
		r1 = c.resistance(ran.main(2), 'kohms')
		rf = c.resistance(ran.main(150), 'kohms')
		
		
		self.question = f"""Calculate the output offset voltage of a noninverting opamp circuit utilizing an opamp with input offset voltage VIO = {vio.mV:.4} mV and external resistors RF = {rf.kohms:.4} kohms and R1 = {r1.kohms:.4} kohms."""
		
		voo = c.voltage(
		vio.V * (1 + rf.ohms / r1.ohms)
		)
		
		self.answer = f"""{voo.mV:.4} mV"""
		
class boylestad_10_9:
	def __init__(self,*args,**kwargs): 
		
		
		iio = c.current(ran.main(100), 'nA')
		r1 = c.resistance(ran.main(2), 'kohms')
		rf = c.resistance(ran.main(150), 'kohms')
		
		self.question = f"""Calculate the offset voltage of a noninverting opamp circuit utilizing  an opamp with input offset current IIO = {iio.nA:.4} nA. The external resistors have values RF = {rf.kohms:.4} kohms and R1 = {r1.kohms:.4} kohms."""
		
		vo = c.voltage(iio.A * rf.ohms)
		
		self.answer = f"""{vo.mV:.4} mV"""
		
class boylestad_10_10:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(500), 'kohms')
		r1 = c.resistance(ran.main(5), 'kohms')
		vio = c.voltage(ran.main(4), 'mV')
		iio = c.current(ran.main(150), 'nA')
		
		self.question = f"""Calculate the total offset voltage an inverting opamp configuration with RF = {rf.kohms:.4} kohms and R1 = {r1.kohms:.4} kohms, and a compensating resistor RC = {r1.kohms:.4} kohms for an oapmp with specified values of input offset voltage = {vio.mV:.4} mV and input offset current IIO = {iio.nA:.4} nA."""
		
		vo = c.voltage(
		vio.V * (1 + rf.ohms/r1.ohms) +
		iio.A * rf.ohms
		)
		
		self.answer = f"""{vo.mV:.4} mV"""
		
class boylestad_10_11:
	def __init__(self,*args,**kwargs): 
		
		iio = c.current(ran.main(5), 'nA')
		iib = c.current(ran.main(30), 'nA')
		
		self.question = f"""Calculate the input bias currents at each input of an opamp having specified values of IIO = {iio.nA:.4} nA and IIB = {iib.nA:.4} nA."""
		
		iibplus = c.current(iib.A + iio.A/2)
		iibminus = c.current(iib.A - iio.A/2)
		
		self.answer = f"""{iibplus.nA:.4} nA, {iibminus.nA:.4} nA"""
		
class boylestad_10_12:
	def __init__(self,*args,**kwargs): 
		
		bandwidth = c.frequency(ran.main(1), 'MHz')
		avd = c.voltage(ran.main(200), 'V')
		avref = c.voltage(1, 'mV')
		
		self.question = f"""Determine the cutoff frequency of an opamp having specified values B = {bandwidth.MHz:.4} MHz and Avd = {avd.V/avref.V:.4} V/mV."""
		
		fc = c.frequency(bandwidth.Hz / avd.V)
		
		self.answer = f"""{fc.Hz:.4} Hz"""
		
class boylestad_10_13:
	def __init__(self,*args,**kwargs): 
		
		srref = c.time(1,'us')
		sr = c.voltage(ran.main(2))
		vi = c.voltage(ran.main(0.5))
		ti = c.time(ran.main(10), 'us')
		
		self.question = f"""For an opamp having a slew rate of SR = {sr.V/srref.us:.4} V/us, what is the minimum closed-loop voltage gain that can be used when the input signal varies by {vi.V:.4}V in {ti.us:.4} us?"""
		
		acl = (
		(sr.V / srref.s) / 
		(vi.V / ti.s)
		)
		
		self.answer = f"""{acl:.4}"""
		
		
class boylestad_10_14:
	def __init__(self,*args,**kwargs): 
		
		vi = c.voltage(ran.main(0.02))
		omega = c.angularVelocity(ran.main(300e3), 'radpers')
		r1 = c.resistance(ran.main(10), 'kohms')
		rf = c.resistance(ran.main(240), 'kohms')
		srref = c.time(1, 'us')
		sr = c.voltage(random.randint(1,5))
		
		self.question = f"""For a {vi.V:.4} V, omega = {omega.radpers:.4} rad/s signal as an input to an inverting opamp with R1 = {r1.kohms:.4} kohms and RF = {rf.kohms:.4} kohms. The opamp slew rate is SR = {sr.V:.4} V/us."""
		
		acl = rf.ohms / r1.ohms
		
		vo = c.voltage( acl * vi.V)
		
		omegaout = c.angularVelocity((sr.V * 1e6) / (vo.V))
		
		self.answer = f"""{omegaout.radpers:.4} rad/s"""
		
class boylestad_10_15:
	def __init__(self,*args,**kwargs): 
		
		supply = c.voltage(ran.main(12))
		power = c.power(ran.main(500), 'mW')
		
		
		self.question = f"""Determine the current draw from a dual power supply of +/- {supply.V:.4}V if the IC dissipates {power.mW:.4} mW."""
		
		current = c.current((power.W / (2 * supply.V)))
		
		self.answer = f"""{current.mA:.4} mA"""
		
class boylestad_10_17:
	def __init__(self,*args,**kwargs): 
		
		vid = c.voltage(ran.main(0.5), 'mV')
		vod = c.voltage(ran.main(8))
		vic = c.voltage(ran.main(1), 'mV')
		voc = c.voltage(ran.main(12), 'mV')
		
		
		self.question = f"""Two input signals, both {vid.mV:.4} mV out of phase are directly applied to the inverting and non-inverting inputs of an opamp and the resulting output signal is of magnitude {vod.V:.4} V. Then the input signals are changed to {vic.mV:.4} mV in phase and are still directly applied to the inverting and non-inverting inputs and the resulting output signal is of magnitude {voc.mV:.4} mV. Calculate the CMRR in this case."""
		
		ad = vod.V / vid.V
		ac = voc.V / vic.V
		CMRR = ad/ac
		CMRR_log = 20*math.log(CMRR, 10)
		
		self.answer = f"""{CMRR:.4} or {CMRR_log:.4} dB"""
		
class boylestad_10_22:
	def __init__(self,*args,**kwargs): 
		
		vi1 = c.voltage(ran.main(150), 'uV')
		vi2 = c.voltage(ran.main(140), 'uV')
		ad = ran.main(4000)
		
		temp = random.randint(0,1)
		if temp == 0:
			CMRR = ran.main(100)
		if temp == 1:
			CMRR = ran.main(10e5)
			
		
		self.question = f"""Determine the output voltage of an opmap for input voltages Vi1 = {vi1.uV:.4} uV and Vi2 = {vi2.uV:.4} uV. THe amplifier has a differential gain of Ad = {ad:.4}  and the value of CMRR is {CMRR:.4}."""
		
		vd = c.voltage(vi1.V - vi2.V)
		vc = c.voltage((vi1.V + vi2.V) / 2)
		vo = c.voltage( ad * vd.V * ( 1 + (1/CMRR)*(vc.V / vd.V)))
		
		self.answer = f"""{vo.V:.4} V"""
		
class boylestad_11_1:
	def __init__(self,*args,**kwargs): 
		
		vi = c.voltage(ran.main(2.5), 'mV')
		r1 = c.resistance(ran.main(2), 'kohms')
		rf = c.resistance(ran.main(200), 'kohms')
		
		self.question = f"""Determine the output voltage of an inverting opamp amplifier with a sinusoidal input of {vi.mV:.4} mV, R1 = {r1.kohms:.4} kohms, and RF = {rf.kohms:.4} kohms."""
		
		av = - rf.ohms/r1.ohms
		
		vo = c.voltage(av * vi.V)
		
		self.answer = f"""{vo.V:.4} V"""
		
class boylestad_11_2:
	def __init__(self,*args,**kwargs): 
		
		vi = c.voltage(ran.main(120), 'uV')
		rf = c.resistance(ran.main(240), 'kohms')
		r1 = c.resistance(ran.main(2.4), 'kohms')
		
		self.question = f"""Calculate the output voltage from the circuit for a non-inverting amplifier with a sinusoidal input of {vi.uV:.4} uV, a feedback resistor of {rf.kohms:.4} kohms and an input resistor of {r1.kohms:.4} kohms."""
		
		av = 1 + rf.ohms/r1.ohms
		vo = c.voltage( av * vi.V)
		
		self.answer = f"""{vo.V:.4} V"""
		
class boylestad_11_3:
	def __init__(self,*args,**kwargs): 
		
		temp = random.randint(0,1)
		if temp == 0:
			vi = c.voltage(ran.main(80), 'uV')
			rf = c.resistance(ran.main(470), 'kohms')
			r1 = c.resistance(ran.main(4.3), 'kohms')
			r2 = c.resistance(ran.main(33), 'kohms')
			r3 = c.resistance(ran.main(33), 'kohms')
		if temp == 1:
			vi = c.voltage(ran.main(150), 'uV')
			rf = c.resistance(ran.main(270), 'kohms')
			r1 = c.resistance(ran.main(30), 'kohms')
			r2 = c.resistance(ran.main(15), 'kohms')
			r3 = c.resistance(ran.main(10), 'kohms')

		self.question = f"""A multiple-stage operational amplifier circuit has a non-inverting amplifier as a first stage, and the next two amplifiers as inverting types. An input signal of {vi.uV:.4} uV is applied. All the stages use a feedback resistor of RF = {rf.kohms:.4} kohms, R1st = {r1.kohms:.4}, R2nd = {r2.kohms:.4}, R3rd = {r3.kohms:.4} kohms. Calculate the output voltage."""
		
		a1 = 1 + rf.ohms/r1.ohms
		a2 = - rf.ohms/r2.ohms
		a3 = - rf.ohms/r3.ohms
		
		vo = c.voltage( a1 * a2 * a3 * vi.V)
		
		self.answer = f"""{vo.V:.4} V"""
		
		
class boylestad_11_6:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(300), 'kohms')
		r1 = c.resistance(ran.main(33), 'kohms')
		r2 = c.resistance(ran.main(10), 'kohms')
		vi1 = c.voltage(ran.main(50), 'mV')
		vi2 = c.voltage(ran.main(10), 'mV')
		omega1 = c.angularVelocity(ran.main(3000, 'int'), 'radpers')
		omega2 = c.angularVelocity(ran.main(1000, 'int'), 'radpers')
		
		self.question = f"""Calculate the output voltage of a operational amplifier summing circuit with a {rf.kohms:.4} kohms feedback resistor, R1 = {r1.kohms:.4} kohms and R2 = {r2.kohms:.4} kohms. The inputs are V1 = {vi1.mV:.4} mV sin ({omega1.radpers:.4}t) and V2 = {vi2.mV:.4} mV sin ({omega2.radpers:.4}t )."""
		
		av1 =  rf.ohms/r1.ohms
		av2 =  rf.ohms/r2.ohms
		vo1 = c.voltage(vi1.V * av1)
		vo2 = c.voltage(vi2.V * av2)
		
		self.answer = f""" - [{vo1.V:.4} sin ({omega1.radpers:.4} t) + {vo2.V:.4} sin ({omega2.radpers:.4} t)] """
		

class boylestad_11_7:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(1), 'Mohms')
		r1 = c.resistance(ran.main(100), 'kohms')
		r2 = c.resistance(ran.main(50), 'kohms')
		r3 = c.resistance(ran.main(500), 'kohms')
		vi1 = c.voltage(ran.main(10), 'mV')
		vi2 = c.voltage(ran.main(5), 'mV')
		
		self.question = f"""Determine the output voltage for the circuit with components RF = {rf.kohms:.4} kohms, R1 = {r1.kohms:.4} kohms, R2 = {r2.kohms:.4} kohms and R3 = {r3.kohms:.4} kohms. The input voltages are V1 =  {vi1.mV:.4} mV sine wave and V2 = {vi2.mV:.4} mV sine wave.https://lesliecaminadecom.files.wordpress.com/2019/06/3d9hy67csq0037yl2x55.png"""
		
		vo = c.voltage(
		- (rf.ohms/r2.ohms)*vi2.V + ((rf.ohms**2)/(r3.ohms*r1.ohms))*vi1.V
		)
		
		self.answer = f"""{vo.mV:.4} mV"""
		
class boylestad_11_8:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(100), 'kohms')
		r2 = c.resistance(ran.main(100), 'kohms')
		r3 = c.resistance(ran.main(20), 'kohms')
		r4 = c.resistance(ran.main(20), 'kohms')
		vi1 = c.voltage(ran.main(5), 'mV')
		vi2 = c.voltage(ran.main(10), 'mV')
		
		self.question = f"""Determine the output voltage for the circuit where R1 = {r1.kohms:.4} kohms, R2 = {r2.kohms:.4} kohms, R3 = {r3.kohms:.4} kohms, R4 = {r4.kohms:.4} kohms. V1 = {vi1.mV:.4} mV and V2 = {vi2.mV:.4} mV
		https://lesliecaminadecom.files.wordpress.com/2019/06/udquqc14msx6k2n885w2.png"""
		
		vo = c.voltage(
		(r4.ohms / (r3.ohms + r4.ohms))*((r2.ohms + r1.ohms) / r2.ohms)*vi1.V - 
		(r1.ohms/r2.ohms)*vi2.V
		)
		
		self.answer = f"""{vo.mV:.4} mV"""
		
		
class boylestad_11_10:
	def __init__(self,*args,**kwargs): 
		temp = random.randint(0,1)
		if temp == 0:
			v1 = c.voltage(ran.main(8))
			r1 = c.resistance(ran.main(2), 'kohms')
			rl = c.resistance(ran.main(4), 'kohms')
			rc = c.resistance(ran.main(2), 'kohms')
			
			self.question = f"""Calculate IL for the circuit if V1 = {v1.V:.4} V, R1 = {r1.kohms:.4} kohms, RC = {rc.kohms:.4} kohms, and RL = {rl.kohms:.4} kohms. https://lesliecaminadecom.files.wordpress.com/2019/06/22o4e3vhc0kbvj5ir1v8.png"""
			
			il = c.current(v1.V / r1.ohms)
			
			self.answer = f"""Load current IL = {il.mA:.4} mA"""
		if temp == 1:
			ii = c.current(ran.main(10), 'mA')
			r1 = c.resistance(ran.main(2), 'kohms')
			
			self.question = f"""Calculate Vo for the circuit if Ii = {ii.mA:.4} mA and R1 = {r1.kohms:.4} kohms.https://lesliecaminadecom.files.wordpress.com/2019/06/lrdxv9z3wg4hmhmby2sa.png"""
			
			vo = c.voltage( - ii.A * r1.ohms)
			
			self.answer = f"""{vo.V:.4} V"""
			
class boylestad_11_11:
	def __init__(self,*args,**kwargs): 
		
		rmain = c.resistance(ran.main(500), 'kohms')
		rp = c.resistance(ran.main(500))
		vi1 = c.voltage(ran.main(10), 'mV')
		vi2 = c.voltage(ran.main(5), 'mV')
		
		self.question = f"""Calculate the output voltage for the instrumentation amplifier where R = {rmain.kohms:.4} kohms and Rp = {rp.ohms:.4} ohms. The input voltages are V1 = {vi1.mV:.4} mV while V2 = {vi2.mV:.4} mV.https://lesliecaminadecom.files.wordpress.com/2019/06/yg773cdlps895pl4tb89.png"""
		
		vo = c.voltage((1 + (2*rmain.ohms/rp.ohms)) * (vi1.V - vi2.V))
		
		self.answer = f"""{vo.mV:.4} mV"""
		
class boylestad_11_12:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(1.2), 'kohms')
		c1 = c.capacitance(ran.main(0.02), 'uF')
		
		self.question = f"""Calculate the cutoff frequency of a first-order low-pass filter for R1 = {r1.kohms:.4} kohms, and C1 = {c1.uF:.4} uF."""
		
		fc = c.frequency(1 / (2*math.pi*r1.ohms*c1.F))
		
		self.answer = f"""Cutoff frequency = {fc.kHz:.4} kHz"""
		
class boylestad_11_13:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(2.1), 'kohms')
		c1 = c.capacitance(ran.main(0.05), 'uF')
		rg = c.resistance(ran.main(10), 'kohms')
		rf = c.resistance(ran.main(50), 'kohms')
		
		
		self.question = f"""Calculate the cutoff frequency of a second-order high-pass filter for R1 = R2 = {r1.kohms:.4} kohms and C1 = C2 = {c1.uF:.4} uF, RG = {rg.kohms:.4} kohms, and RF = {rf.kohms:.4} kohms.https://lesliecaminadecom.files.wordpress.com/2019/06/qtpcae4eyx2ire4q7zk3.png"""
		
		fc = c.frequency(1 / (2*math.pi*r1.ohms*c1.F))
		
		self.answer = f"""{fc.kHz:.4} kHz"""
		
class boylestad_11_14:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(10), 'kohms')
		c1 = c.capacitance(ran.main(0.1), 'uF')
		c2 = c.capacitance(ran.main(2), 'nF')
		
		
		self.question = f"""Calculate the cutoff frequencies of the bandpass filter circuit with R1 = R2 = {r1.kohms:.4} kohms, C1 = {c1.uF:.4} uF, and C2 = {c2.uF:.4} uF.https://lesliecaminadecom.files.wordpress.com/2019/06/7w08dlp8p1jq0rqw7t5o.png"""
		
		fcl = c.frequency(1 / (2*math.pi*r1.ohms*c1.F))
		fch = c.frequency(1 / (2*math.pi*r1.ohms*c2.F))
		
		self.answer = f"""{fcl.Hz:.4} Hz, {fch.kHz:.4} kHz"""
		

		
		
		
		
		
		
		


		


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		