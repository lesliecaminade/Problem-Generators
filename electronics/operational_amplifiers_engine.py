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
		
		
		self.question = f"""Determine the values of VC for a BJT differential amplifier with RC1 = RC2 = {rc.kohms} ohms, common RE = {re.kohms} kohms, VCC = {vcc.V} V and VEE = {vee.V} V."""
		
		ie = c.current(
		( - vee.V - 0.7) / 
		re.ohms
		)
		
		ic = c.current(ie.A / 2)
		
		vc = c.voltage( vcc.V - ic.A * rc.ohms )
		
		self.answer = f"""{vc.V} V"""

class boylestad_10_2:
	def __init__(self,*args,**kwargs): 
		
		
		vcc = c.voltage(ran.main(9))
		vee = c.voltage(ran.main(-9))
		re = c.resistance(ran.main(43), 'kohms')
		rc = c.resistance(ran.main(47), 'kohms')
		beta = ran.main(75)
		ri = c.resistance(ran.main(20), 'kohms')
		vi = c.voltage(ran.main(2), 'mV')
		
		
		self.question = f"""Calculate the single-ended output voltage Vo1 for a BJT differential amplifier setup with VCC = {vcc.V} V, VEE = {vee.V} V, RC1 = RC2 = {rc.kohms} kohms, RE = {re.kohms} kohms,  BJT characteristics are ri = {ri.kohms} kohms, and beta = {beta}. The input voltage is {vi.mV} mV."""

		ie = c.current(
		(- vee.V - 0.7) / 
		re.ohms
		)
		
		ic = c.current(ie.A / 2)
		
		vc = c.voltage( vcc.V - ic.A * rc.ohms )
		
		resmall = c.resistance( c.voltage(26, 'mV').V / ic.A ) 
		
		av = rc.ohms / (2 * resmall.ohms)
		
		vo = c.voltage( vi.V * av )
		
		self.answer = f"""{vo.V} V"""
		
		
class boylestad_10_3:
	def __init__(self,*args,**kwargs): 
		
		
		vcc = c.voltage(ran.main(9))
		vee = c.voltage(ran.main(-9))
		re = c.resistance(ran.main(43), 'kohms')
		rc = c.resistance(ran.main(47), 'kohms')
		beta = ran.main(75)
		ri = c.resistance(ran.main(20), 'kohms')
		vi = c.voltage(ran.main(2), 'mV')
		
		
		self.question = f"""Calculate the common-mode gain for a BJT differential amplifier setup with VCC = {vcc.V} V, VEE = {vee.V} V, RC1 = RC2 = {rc.kohms} kohms, RE = {re.kohms} kohms,  BJT characteristics are ri = {ri.kohms} kohms, and beta = {beta}. The input voltage is {vi.mV} mV."""

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
		
		self.answer = f"""{ac}"""
		
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
		
		self.question = f"""Calculate the common-mode voltage gain of a differential amplifier with VDD = {vdd.V} V, RC1 = RC2 = {rc.kohms} kohms, uses identical Q1 and Q2, and the BJT characteristics are beta = {beta1} and ri = {ri.kohms} kohms. This differential amplifier uses a BJT constant current source as a emitter resistance the BJT uses a limiter resistor R1 = {r1.kohms} kohms, a bleeder resistor of R2 = {r2.kohms} kohms, and an emitter resistance of R3 = {r3.kohms} kohms. The BJT Q3 used in the constant current source has the characteristics ro = {ro.kohms} kohms, and beta = {beta2}."""
		
		ac = (
		( beta1 * rc.ohms ) / 
		( ri.ohms + 2*(beta1 + 1)*ro.ohms)
		)
		
		self.answer = f"""{ac}"""
		
class boylestad_10_5:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(500), 'kohms')
		r1 = c.resistance(ran.main(100), 'kohms')
		v1 = c.voltage(ran.main(2))
		
		self.question = f"""An inverting amplifier opamp circuit has R1 = {r1.kohms} kohms and RF = {rf.kohms} kohms. What output voltage results for an input of V1 = {v1.V} V?"""
		
		vo = c.voltage(
		(- rf.ohms * v1.V) / 
		( r1.ohms )
		)
		
		self.answer = f"""{vo.V} V"""
		
class boylestad_10_6:
	def __init__(self,*args,**kwargs): 
		
		v1 = c.voltage(ran.main(2))
		rf = c.resistance(ran.main(500), 'kohms')
		r1 = c.resistance(ran.main(100), 'kohms')
		
		self.question = f"""Calculate the output voltage of a opamp noninverting amplifier for values V1 ={v1.V} V, RF = {rf.kohms} kohms, and R1 = {r1.kohms} kohms."""
		
		vo = c.voltage((1 + (rf.ohms / r1.ohms)) * v1.V)
		
		self.answer = f"""{vo.V} V"""
		
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
			
		self.question = f"""Calculate the output voltage of an opamp summing amplifier for the set of voltages and resistors: RF = {rf.Mohms} Mohms, V1 = {v1.V} V, V2 = {v2.V} V, V3 = {v3.V} V, R1 = {r1.kohms} kohms, R2 = {r2.kohms} kohms, R3 = {r3.kohms} kohms."""
		
		vo = c.voltage(- rf.ohms * ( v1.V / r1.ohms + v2.V / r2.ohms + v3.V / r3.ohms ))
		
		self.answer = f"""{vo.V} V"""
		
class boylestad_10_8:
	def __init__(self,*args,**kwargs): 
		
		vio = c.voltage(ran.main(1.2), 'mV')
		r1 = c.resistance(ran.main(2), 'kohms')
		rf = c.resistance(ran.main(150), 'kohms')
		
		
		self.question = f"""Calculate the output offset voltage of a noninverting opamp circuit utilizing an opamp with input offset voltage VIO = {vio.mV} mV and external resistors RF = {rf.kohms} kohms and R1 = {r1.kohms} kohms."""
		
		voo = c.voltage(
		vio.V * (1 + rf.ohms / r1.ohms)
		)
		
		self.answer = f"""{voo.mV} mV"""
		
class boylestad_10_9:
	def __init__(self,*args,**kwargs): 
		
		
		iio = c.current(ran.main(100), 'nA')
		r1 = c.resistance(ran.main(2), 'kohms')
		rf = c.resistance(ran.main(150), 'kohms')
		
		self.question = f"""Calculate the offset voltage of a noninverting opamp circuit utilizing  an opamp with input offset current IIO = {iio.nA} nA. The external resistors have values RF = {rf.kohms} kohms and R1 = {r1.kohms} kohms."""
		
		vo = c.voltage(iio.A * rf.ohms)
		
		self.answer = f"""{vo.mV} mV"""
		
class boylestad_10_10:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(500), 'kohms')
		r1 = c.resistance(ran.main(5), 'kohms')
		vio = c.voltage(ran.main(4), 'mV')
		iio = c.current(ran.main(150), 'nA')
		
		self.question = f"""Calculate the total offset voltage an inverting opamp configuration with RF = {rf.kohms} kohms and R1 = {r1.kohms} kohms, and a compensating resistor RC = {r1.kohms} kohms for an oapmp with specified values of input offset voltage = {vio.mV} mV and input offset current IIO = {iio.nA} nA."""
		
		vo = c.voltage(
		vio.V * (1 + rf.ohms/r1.ohms) +
		iio.A * rf.ohms
		)
		
		self.answer = f"""{vo.mV} mV"""
		
class boylestad_10_11:
	def __init__(self,*args,**kwargs): 
		
		iio = c.current(ran.main(5), 'nA')
		iib = c.current(ran.main(30), 'nA')
		
		self.question = f"""Calculate the input bias currents at each input of an opamp having specified values of IIO = {iio.nA} nA and IIB = {iib.nA} nA."""
		
		iibplus = c.current(iib.A + iio.A/2)
		iibminus = c.current(iib.A - iio.A/2)
		
		self.answer = f"""{iibplus.nA} nA, {iibminus.nA} nA"""
		
class boylestad_10_12:
	def __init__(self,*args,**kwargs): 
		
		bandwidth = c.frequency(ran.main(1), 'MHz')
		avd = c.voltage(ran.main(200), 'V')
		avref = c.voltage(1, 'mV')
		
		self.question = f"""Determine the cutoff frequency of an opamp having specified values B = {bandwidth.MHz} MHz and Avd = {avd.V/avref.V} V/mV."""
		
		fc = c.frequency(bandwidth.Hz / avd.V)
		
		self.answer = f"""{fc.Hz} Hz"""
		
class boylestad_10_13:
	def __init__(self,*args,**kwargs): 
		
		srref = c.time(1,'us')
		sr = c.voltage(ran.main(2))
		vi = c.voltage(ran.main(0.5))
		ti = c.time(ran.main(10), 'us')
		
		self.question = f"""For an opamp having a slew rate of SR = {sr.V/srref.us} V/us, what is the minimum closed-loop voltage gain that can be used when the input signal varies by {vi.V}V in {ti.us} us?"""
		
		acl = (
		(sr.V / srref.s) / 
		(vi.V / ti.s)
		)
		
		self.answer = f"""{acl}"""
		
		
class boylestad_10_14:
	def __init__(self,*args,**kwargs): 
		
		vi = c.voltage(ran.main(0.02))
		omega = c.angularVelocity(ran.main(300e3), 'radpers')
		r1 = c.resistance(ran.main(10), 'kohms')
		rf = c.resistance(ran.main(240), 'kohms')
		srref = c.time(1, 'us')
		sr = c.voltage(random.randint(1,5))
		
		self.question = f"""For a {vi.V} V, omega = {omega.radpers} rad/s signal as an input to an inverting opamp with R1 = {r1.kohms} kohms and RF = {rf.kohms} kohms. The opamp slew rate is SR = {sr.V} V/us."""
		
		acl = rf.ohms / r1.ohms
		
		vo = c.voltage( acl * vi.V)
		
		omegaout = c.angularVelocity((sr.V * 1e6) / (vo.V))
		
		self.answer = f"""{omegaout.radpers} rad/s"""
		
class boylestad_10_15:
	def __init__(self,*args,**kwargs): 
		
		supply = c.voltage(ran.main(12))
		power = c.power(ran.main(500), 'mW')
		
		
		self.question = f"""Determine the current draw from a dual power supply of +/- {supply.V}V if the IC dissipates {power.mW} mW."""
		
		current = c.current((power.W / (2 * supply.V)))
		
		self.answer = f"""{current.mA} mA"""
		
class boylestad_10_17:
	def __init__(self,*args,**kwargs): 
		
		vid = c.voltage(ran.main(0.5), 'mV')
		vod = c.voltage(ran.main(8))
		vic = c.voltage(ran.main(1), 'mV')
		voc = c.voltage(ran.main(12), 'mV')
		
		
		self.question = f"""Two input signals, both {vid.mV} mV out of phase are directly applied to the inverting and non-inverting inputs of an opamp and the resulting output signal is of magnitude {vod.V} V. Then the input signals are changed to {vic.mV} mV in phase and are still directly applied to the inverting and non-inverting inputs and the resulting output signal is of magnitude {voc.mV} mV. Calculate the CMRR in this case."""
		
		ad = vod.V / vid.V
		ac = voc.V / vic.V
		CMRR = ad/ac
		CMRR_log = 20*math.log(CMRR, 10)
		
		self.answer = f"""{CMRR} or {CMRR_log} dB"""
		
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
			
		
		self.question = f"""Determine the output voltage of an opmap for input voltages Vi1 = {vi1.uV} uV and Vi2 = {vi2.uV} uV. THe amplifier has a differential gain of Ad = {ad}  and the value of CMRR is {CMRR}."""
		
		vd = c.voltage(vi1.V - vi2.V)
		vc = c.voltage((vi1.V + vi2.V) / 2)
		vo = c.voltage( ad * vd.V * ( 1 + (1/CMRR)*(vc.V / vd.V)))
		
		self.answer = f"""{vo.V} V"""
		
class boylestad_11_1:
	def __init__(self,*args,**kwargs): 
		
		vi = c.voltage(ran.main(2.5), 'mV')
		r1 = c.resistance(ran.main(2), 'kohms')
		rf = c.resistance(ran.main(200), 'kohms')
		
		self.question = f"""Determine the output voltage of an inverting opamp amplifier with a sinusoidal input of {vi.mV} mV, R1 = {r1.kohms} kohms, and RF = {rf.kohms} kohms."""
		
		av = - rf.ohms/r1.ohms
		
		vo = c.voltage(av * vi.V)
		
		self.answer = f"""{vo.V} V"""
		
class boylestad_11_2:
	def __init__(self,*args,**kwargs): 
		
		vi = c.voltage(ran.main(120), 'uV')
		rf = c.resistance(ran.main(240), 'kohms')
		r1 = c.resistance(ran.main(2.4), 'kohms')
		
		self.question = f"""Calculate the output voltage from the circuit for a non-inverting amplifier with a sinusoidal input of {vi.uV} uV, a feedback resistor of {rf.kohms} kohms and an input resistor of {r1.kohms} kohms."""
		
		av = 1 + rf.ohms/r1.ohms
		vo = c.voltage( av * vi.V)
		
		self.answer = f"""{vo.V} V"""
		
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

		self.question = f"""A multiple-stage operational amplifier circuit has a non-inverting amplifier as a first stage, and the next two amplifiers as inverting types. An input signal of {vi.uV} uV is applied. All the stages use a feedback resistor of RF = {rf.kohms} kohms, R1st = {r1.kohms}, R2nd = {r2.kohms}, R3rd = {r3.kohms} kohms. Calculate the output voltage."""
		
		a1 = 1 + rf.ohms/r1.ohms
		a2 = - rf.ohms/r2.ohms
		a3 = - rf.ohms/r3.ohms
		
		vo = c.voltage( a1 * a2 * a3 * vi.V)
		
		self.answer = f"""{vo.V} V"""
		
		
class boylestad_11_6:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(300), 'kohms')
		r1 = c.resistance(ran.main(33), 'kohms')
		r2 = c.resistance(ran.main(10), 'kohms')
		vi1 = c.voltage(ran.main(50), 'mV')
		vi2 = c.voltage(ran.main(10), 'mV')
		omega1 = c.angularVelocity(ran.main(3000, 'int'), 'radpers')
		omega2 = c.angularVelocity(ran.main(1000, 'int'), 'radpers')
		
		self.question = f"""Calculate the output voltage of a operational amplifier summing circuit with a {rf.kohms} kohms feedback resistor, R1 = {r1.kohms} kohms and R2 = {r2.kohms} kohms. The inputs are V1 = {vi1.mV} mV sin ({omega1.radpers}t) and V2 = {vi2.mV} mV sin ({omega2.radpers}t )."""
		
		av1 =  rf.ohms/r1.ohms
		av2 =  rf.ohms/r2.ohms
		vo1 = c.voltage(vi1.V * av1)
		vo2 = c.voltage(vi2.V * av2)
		
		self.answer = f""" - [{vo1.V} sin ({omega1.radpers} t) + {vo2.V} sin ({omega2.radpers} t)] """
		

class boylestad_11_7:
	def __init__(self,*args,**kwargs): 
		
		rf = c.resistance(ran.main(1), 'Mohms')
		r1 = c.resistance(ran.main(100), 'kohms')
		r2 = c.resistance(ran.main(50), 'kohms')
		r3 = c.resistance(ran.main(500), 'kohms')
		vi1 = c.voltage(ran.main(10), 'mV')
		vi2 = c.voltage(ran.main(5), 'mV')
		
		self.question = f"""Determine the output voltage for the circuit with components RF = {rf.kohms} kohms, R1 = {r1.kohms} kohms, R2 = {r2.kohms} kohms and R3 = {r3.kohms} kohms. The input voltages are V1 =  {vi1.mV} mV sine wave and V2 = {vi2.mV} mV sine wave.https://lesliecaminadecom.files.wordpress.com/2019/06/3d9hy67csq0037yl2x55.png"""
		
		vo = c.voltage(
		- (rf.ohms/r2.ohms)*vi2.V + ((rf.ohms**2)/(r3.ohms*r1.ohms))*vi1.V
		)
		
		self.answer = f"""{vo.mV} mV"""
		
class boylestad_11_8:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(100), 'kohms')
		r2 = c.resistance(ran.main(100), 'kohms')
		r3 = c.resistance(ran.main(20), 'kohms')
		r4 = c.resistance(ran.main(20), 'kohms')
		vi1 = c.voltage(ran.main(5), 'mV')
		vi2 = c.voltage(ran.main(10), 'mV')
		
		self.question = f"""Determine the output voltage for the circuit where R1 = {r1.kohms} kohms, R2 = {r2.kohms} kohms, R3 = {r3.kohms} kohms, R4 = {r4.kohms} kohms. V1 = {vi1.mV} mV and V2 = {vi2.mV} mV
		https://lesliecaminadecom.files.wordpress.com/2019/06/udquqc14msx6k2n885w2.png"""
		
		vo = c.voltage(
		(r4.ohms / (r3.ohms + r4.ohms))*((r2.ohms + r1.ohms) / r2.ohms)*vi1.V - 
		(r1.ohms/r2.ohms)*vi2.V
		)
		
		self.answer = f"""{vo.mV} mV"""
		
		
class boylestad_11_10:
	def __init__(self,*args,**kwargs): 
		temp = random.randint(0,1)
		if temp == 0:
			v1 = c.voltage(ran.main(8))
			r1 = c.resistance(ran.main(2), 'kohms')
			rl = c.resistance(ran.main(4), 'kohms')
			rc = c.resistance(ran.main(2), 'kohms')
			
			self.question = f"""Calculate IL for the circuit if V1 = {v1.V} V, R1 = {r1.kohms} kohms, RC = {rc.kohms} kohms, and RL = {rl.kohms} kohms. https://lesliecaminadecom.files.wordpress.com/2019/06/22o4e3vhc0kbvj5ir1v8.png"""
			
			il = c.current(v1.V / r1.ohms)
			
			self.answer = f"""Load current IL = {il.mA} mA"""
		if temp == 1:
			ii = c.current(ran.main(10), 'mA')
			r1 = c.resistance(ran.main(2), 'kohms')
			
			self.question = f"""Calculate Vo for the circuit if Ii = {ii.mA} mA and R1 = {r1.kohms} kohms.https://lesliecaminadecom.files.wordpress.com/2019/06/lrdxv9z3wg4hmhmby2sa.png"""
			
			vo = c.voltage( - ii.A * r1.ohms)
			
			self.answer = f"""{vo.V} V"""
			
class boylestad_11_11:
	def __init__(self,*args,**kwargs): 
		
		rmain = c.resistance(ran.main(500), 'kohms')
		rp = c.resistance(ran.main(500))
		vi1 = c.voltage(ran.main(10), 'mV')
		vi2 = c.voltage(ran.main(5), 'mV')
		
		self.question = f"""Calculate the output voltage for the instrumentation amplifier where R = {rmain.kohms} kohms and Rp = {rp.ohms} ohms. The input voltages are V1 = {vi1.mV} mV while V2 = {vi2.mV} mV.https://lesliecaminadecom.files.wordpress.com/2019/06/yg773cdlps895pl4tb89.png"""
		
		vo = c.voltage((1 + (2*rmain.ohms/rp.ohms)) * (vi1.V - vi2.V))
		
		self.answer = f"""{vo.mV} mV"""
		
class boylestad_11_12:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(1.2), 'kohms')
		c1 = c.capacitance(ran.main(0.02), 'uF')
		
		self.question = f"""Calculate the cutoff frequency of a first-order low-pass filter for R1 = {r1.kohms} kohms, and C1 = {c1.uF} uF."""
		
		fc = c.frequency(1 / (2*math.pi*r1.ohms*c1.F))
		
		self.answer = f"""Cutoff frequency = {fc.kHz} kHz"""
		
class boylestad_11_13:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(2.1), 'kohms')
		c1 = c.capacitance(ran.main(0.05), 'uF')
		rg = c.resistance(ran.main(10), 'kohms')
		rf = c.resistance(ran.main(50), 'kohms')
		
		
		self.question = f"""Calculate the cutoff frequency of a second-order high-pass filter for R1 = R2 = {r1.kohms} kohms and C1 = C2 = {c1.uF} uF, RG = {rg.kohms} kohms, and RF = {rf.kohms} kohms.https://lesliecaminadecom.files.wordpress.com/2019/06/qtpcae4eyx2ire4q7zk3.png"""
		
		fc = c.frequency(1 / (2*math.pi*r1.ohms*c1.F))
		
		self.answer = f"""{fc.kHz} kHz"""
		
class boylestad_11_14:
	def __init__(self,*args,**kwargs): 
		
		r1 = c.resistance(ran.main(10), 'kohms')
		c1 = c.capacitance(ran.main(0.1), 'uF')
		c2 = c.capacitance(ran.main(2), 'nF')
		
		
		self.question = f"""Calculate the cutoff frequencies of the bandpass filter circuit with R1 = R2 = {r1.kohms} kohms, C1 = {c1.uF} uF, and C2 = {c2.uF} uF.https://lesliecaminadecom.files.wordpress.com/2019/06/7w08dlp8p1jq0rqw7t5o.png"""
		
		fcl = c.frequency(1 / (2*math.pi*r1.ohms*c1.F))
		fch = c.frequency(1 / (2*math.pi*r1.ohms*c2.F))
		
		self.answer = f"""{fcl.Hz} Hz, {fch.kHz} kHz"""
		

		
		
		
		
		
		
		


		


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		