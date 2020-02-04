import math
import random
import datetime
#LEGACY code

SPEED_OF_LIGHT = 299792458
question = ""
GRAMS = 1/1000
KILO = 10**3
GIGA = 10**9
MEGA = 10**6
CENTI = 10**-2
MILLI = 10**-3
DECI = 10**-1
MICRO = 10**-6
NANO = 10**-9
PICO = 10**-12
PERCENT = 1/100
DEGREES = math.pi/180
RADIANS = 180/math.pi
WATTS = 1/746
HORSEPOWER = 746
#GRAM = 
#note: Format for conversion factors is FROM_TO

#time
MIN_SEC = 60

#volume
M3_LITERS = 1000
LITERS_M3 = 1/1000
MILLILITERS_M3 = 1/(1000*1000)
STP_VOLUME = 22.4 #L
STP_VOLUME_LITERS = 22.4

#area
CM2_M2 = 1/10000
M2_CM2 = 10000
MM2_M2 = 1/(1E6)
M2_MM2 = 1E6

#constants
SPEED_OF_LIGHT = 3e8
UNIVERSALGASCONSTANT = 8.3144598 #DEPRECATED
UNIVERSAL_GAS_CONSTANT = 8.3144598
AVOGADROS_NUMBER = 6.0221409E23
BOLTZMANNS_CONSTANT = 1.38064852E-23
STEFAN_BOLTZMANNS_CONSTANT = 5.670367E-8 #WmK
CHARGE_ELECTRON = 1.60217662E-19 #coulombs
GRAVITATIONAL_CONSTANT = 6.67408e-11 
PERMITTIVITY_OF_FREE_SPACE = 8.8541878128e-12
PERMEABILITY_OF_FREE_SPACE = 1.25663706212e-6

#mass
GRAMS_KG = 1/1000
KG_GRAMS = 1000
GRAM = 1/1000 #depreceated
GRAMS = 1 / 1000 #DEPRECATED
MILLIGRAMS = 1/(1000*1000) #DEPRECATED
MILLIGRAMS_KG = 1/(1000*1000)

#prefixes
KILO = 10**3
GIGA = 10**9
MEGA = 10**6
CENTI = 10**-2
MILLI = 10**-3
DECI = 10**-1
MICRO = 10**-6
NANO = 10**-9
PICO = 10**-12
PERCENT = 1/100

#angle
DEGREES = math.pi/180
RADIANS = 180/math.pi

#f
WATTS_HORSEPOWER = 1/746
HORSEPOWER_WATTS = 746
KCALHR_WATTS = 1.16222222
WATTS_CALS = 1/4.184
CALS_WATTS = 1/4.184

#moles
KGKMOL = 1/1000
KGKMOL_KGMOL = 1/1000
KGMOL_KGKMOL = 1000

#pressure
ATM_PA = 101325/1
MMHG_PA = 101325/760
STP_PRESSURE = 101325 #Pa

#density
GCM3_KGM3 = 1000
DENSITY_WATER = 1000 #kg/m3

#energy
BIGCAL_CAL = 1000
CAL_BIGCAL = 1/1000
KCAL_JOULE = 4184
CAL_JOULE = 4.184
JOULE_CAL = (1/4.184)
JOULE_KCAL = ((1/4.184) / 1000)



#temperature
def CELSIUS_KELVIN(celsius):
	kelvin = celsius + 273
	return kelvin

STP_TEMPERATURE = 273
STP_TEMPERATURE_KELVIN = 273

#specific heats 
SPECIFIC_HEAT_WATER_JKGK = 4184   
SPECIFIC_HEAT_WATER_CALGC = 1

LATENT_HEAT_FUSION_ICE_CALG = 80
LATENT_HEAT_FUSION_WATER_CALG = 80
LATENT_HEAT_FUSION_ICE_JKG = 334E3
LATENT_HEAT_FUSION_WATER_JKG = 334E3

LATENT_HEAT_VAPORIZATION_WATER_CALG = 540
LATENT_HEAT_VAPORIZATION_STEAM_CALG = 540
LATENT_HEAT_VAPORIZATION_WATER_JKG = 2256E3
LATENT_HEAT_VAPORIZATION_STEAM_JKG = 2256E3

#thermal resistance
USCUSTOMARYUNIT_KELVINPERWATT = 0.176

#resistivities
RESISTIVITY_COPPER = 1.72E-8
RESISTIVITY_ALUMINUM = 2.65E-8
RESISTIVITY_CARBON = 3.5E-5


FLOAT_ROUND = 8
E6 = [10, 15, 22, 33, 47, 68]
E12 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39,43,47,51, 56, 62,68,75,82,91]


def eng_string( x, format='%s', si=False):
    '''
    Returns float/int value <x> formatted in a simplified engineering format -
    using an exponent that is a multiple of 3.

    format: printf-style string used to format the value before the exponent.

    si: if true, use SI suffix for exponent, e.g. k instead of e3, n instead of
    e-9 etc.

    E.g. with format='%.2f':
        1.23e-08 => 12.30e-9
             123 => 123.00
          1230.0 => 1.23e3
      -1230000.0 => -1.23e6

    and with si=True:
          1230.0 => 1.23k
      -1230000.0 => -1.23M
    '''
    sign = ''
    if x < 0:
        x = -x
        sign = '-'
    exp = int( math.floor( math.log10( x)))
    exp3 = exp - ( exp % 3)
    x3 = x / ( 10 ** exp3)

    if si and exp3 >= -24 and exp3 <= 24 and exp3 != 0:
        exp3_text = 'yzafpnum kMGTPEZY'[ ( exp3 - (-24)) / 3]
    elif exp3 == 0:
        exp3_text = ''
    else:
        exp3_text = 'e%s' % exp3

    return ( '%s'+format+'%s') % ( sign, x3, exp3_text)


class acceleration:
	def __init__(self,*args,**kwargs):
		self.mpers2 = float(args[0])
		for arg in args:
			if arg == 'mpers2':
				self.mpers2 = float(args[0])
			if arg == 'cmpers2':
				self.mpers2 = float(args[0]) /100
			if arg == 'kmpers2':
				self.mpers2 = float(args[0]) * 1000
				
		self.cmpers2 = self.mpers2 * 100
		self.kmpers2 = self.mpers2 / 1000
		

class angle:
	def __init__(self,*args,**kwargs):
		self.radians = float(args[0])
		self.degrees = float(args[0]) * (180 / math.pi)
		self.degree = self.degrees
		self.deg = self.degrees
		for arg in args:
			if arg == 'deg' or arg=='degree' or arg == 'degrees':
				self.degrees = float(args[0])                      
				self.degree = self.degrees
				self.deg = self.degrees
			if arg == 'rev' or arg == 'revs':
				self.degrees = float(args[0]) * 360
				self.degree = self.degrees
				self.deg = self.degrees
				
				
		self.radians = self.degrees * (math.pi / 180)
		self.rad = self.radians
		self.radian = self.radians
		
		self.rev = self.degrees / 360
		self.revs = self.rev

	def complementary(self):
		return angle(math.pi/2 - self.radians)

	def supplementary(self):
		return angle(math.pi - self.radians)

	def explementary(self):
		return angle(2 * math.pi - self.radians)

		
class angularAcceleration:
	def __init__(self,*args,**kwargs): 
		self.radpers2 = float(args[0])
		for arg in args:
			if arg == 'radpers2':
				pass
			if arg == 'revpers2':
				self.radpers2 = float(args[0]) * math.pi * 2 
		
		self.revpers2 = self.radpers2 / (math.pi  * 2)

class angularMomentum:
	def __init__(self,*args,**kwargs): 
		
		self.kgm2pers = float(args[0])
		
class angularVelocity:
	def __init__(self,*args,**kwargs):
		self.radpers = float(args[0])
		for arg in args:
			if arg == 'radpers':
				pass
			if arg == 'revpers':
				self.radpers = float(args[0]) * math.pi * 2
			if arg == 'revpermin' or arg == 'rpm' or arg == 'revperm':
				self.radpers = float(args[0]) * ((math.pi * 2) / 60 )
		self.revpers = self.radpers / (math.pi * 2)
		self.revpermin = self.radpers / ((math.pi * 2)/60)
		self.rpm = self.revpermin
		self.revperm = self.revpermin

class angular_velocity(angularVelocity):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class antennaGain:
	def __init__(self,*args,**kwargs): 
		self.factor = float(args[0])
		for arg in args:
			if arg == 'dB' or arg == 'dBi':
				self.factor = 10**(float(args[0])/10)
			if arg == 'dBd':
				self.factor = 10**((float(args[0]) + 2.15)/10)
		self.dB = 10 * math.log(self.factor, 10)
		self.dBi = 10 * math.log(self.factor, 10)
		self.dBd = self.dBi - 2.15
		
class area:
	def __init__(self,*args, **kwargs):
		self.m2 = float(args[0])
		for arg in args:
			if arg == 'in2':
				self.m2 = float(args[0]) / 1550.003
			if arg == 'mm2':
				self.m2 = float(args[0]) / 1e6
			if arg == 'cm2':
				self.m2 = float(args[0]) / 10000
			if arg == 'km2':
				self.m2 = float(args[0]) * 1e6
		
		#put other units here
		self.Tm2 = self.m2 * 1E-12**2
		self.Gm2 = self.m2 * 1E-9**2
		self.Mm2 = self.m2 * 1E-6**2
		self.km2 = self.m2 * 1E-3**2
		self.dm2 = self.m2 * 1E1**2
		self.cm2 = self.m2 * 1E2**2
		self.mm2 = self.m2 * 1E3**2
		self.um2 = self.m2 * 1E6**2
		self.nm2 = self.m2 * 1E9**2
		self.pm2 = self.m2 * 1E12**2
		self.fm2 = self.m2 * 1E15**2
		self.am2 = self.m2 * 1E18**2
		self.in2 = self.m2 * 1550.003
		
		
class bitrate:
	def __init__(self, *args, **kwargs):
		self.bps = float(args[0])
		for arg in args:
			if arg == 'kbps':
				self.bps = float(args[0]) * 1000
			if arg == 'Mbps':
				self.bps = float(args[0]) * 1e6
			if arg == 'Gbps':
				self.bps = float(args[0]) * 1e9
				
		self.kbps = self.bps / 1000
		self.Mbps = self.bps / 1e6
		self.Gbps = self.bps / 1e9
					
class conductance:
	def __init__(self,*args,**kwargs): 
			
		self.S = float(args[0])
		
		for arg in args:
			if arg == 'mS':
				self.S = float(args[0]) / 1e3
			if arg == 'uS':
				self.S = float(args[0]) / 1e6
				
		self.mS = self.S * 1e3
		self.uS = self.S * 1e6
		
class capacitance:
	def __init__(self,*args,**kwargs): 
		self.F = float(args[0])
		#print('capacitance: ', self.F)
		
		for arg in args:
			#print('looking _for arguments...')
			if arg == 'uF':
				self.F = float(args[0]) / 1e6
			if arg == 'nF':
				self.F = float(args[0]) / 1e9
			if arg == 'pF':
				self.F = float(args[0]) / 1e12
			if arg == 'e12':
				#print('e12 detected')
				digits = float(random.choice(E12))
				for i in range(-22, 22):
					if 10**i <= float(args[0]) < 10**(i+1):
						self.F = digits * 10**i
						# print('reducing')
						# print('digits: ', digits)
						# print('self.F ', self.F)
				
		self.uF = self.F * 1e6
		self.nF = self.F * 1e9
		self.pF = self.F * 1e12

	def parallel(self, capacitance_object):
		capacitance_new = self.F + capacitance_object.F
		return capacitance(capacitance_new)

	def series(self, capacitance_object):
		capacitance_new = (self.F * capacitance_object.F) / (self.F + capacitance_object.F)
		return capacitance(capacitance_new)


		
class charge:
	def __init__(self, *args, **kwargs):
		self.C = float(args[0])
		
		for arg in args:
			if arg == 'C':
				pass
			if arg == 'mC':
				self.C = float(args[0]) / 1000
			if arg == 'uC':
				self.C = float(args[0]) / 1e6
			if arg == 'nC':
				self.C = float(args[0]) / 1e9
			if arg == 'pC':
				self.C = float(args[0]) / 1e12
				
		self.C = self.C
		self.mC = self.C * 1E3
		self.uC = self.C * 1E6
		self.nC = self.C * 1E9
		self.pC = self.C * 1E12
		
class current:
	def __init__ (self,*args, **kwargs):
		self.A = float(args[0])
		
		for arg in args:
			if arg == 'mA':
				self.A = float(args[0]) / 1000
			if arg == 'uA':
				self.A = float(args[0]) / 1e6
			if arg == 'kA':
				self.A = float(args[0]) * 1000
			if arg == 'nA':
				self.A = float(args[0]) / 1e9
			if arg == 'pA':
				self.A = float(args[0]) / 1e12
					
		
		self.kA = self.A * 1E-3
		self.mA = self.A * 1E3
		self.uA = self.A * 1E6
		self.nA = self.A * 1e9
		self.pA = self.A * 1e12
		
class dbvalue:
	def __init__(self,*args,**kwargs): 
		self.unitless = float(args[0])
		for arg in args:
			if arg == 'dB':
				self.unitless = 10**(float(args[0]) / 10)
			if arg == 'dB20':
				self.unitless = 10**(float(args[0]) / 20)
		
		self.dB = 10 * math.log(self.unitless, 10)
		self.dB20 = 20 * math.log(self.unitless, 10)
		
class density:
	def __init__(self,*args,**kwargs):
		self.kgperm3 = float(args[0])
		for arg in args:
			if arg == 'kgperm3':
				pass
			if arg == 'gpercm3':
				self.kgperm3 = float(args[0]) * 1000
				
		self.gpercm3 = self.kgperm3 / 1000
		
	   
class energy:
#work is also included here
	def __init__(self,*args,**kwargs):
		self.J = float(args[0])
		for arg in args:
			if arg == 'J' or arg == 'joule':
				pass
			if arg == 'kJ':
				self.J = float(args[0]) * 1000
			if arg == 'Wh':
				self.J = float(args[0]) * 3600
			if arg == 'kWh':
				self.J = float(args[0]) * 3.6e6
			if arg == 'MJ':
				self.J = float(args[0]) * 1e6
		
		self.kJ = self.J / 1000
		self.MJ = self.J / 1e6
		self.Wh = self.J / 3600
		self.kWh = self.J / 3.6e6
	
class electricField:
	def __init__(self,*args,**kwargs): 
		self.Vperm = float(args[0])
		for arg in args:
			if arg == 'mVperm':
				self.Vperm = float(args[0]) / 1000
			if arg == 'uVperm':
				self.Vperm = float(args[0]) / 1e6
			if arg == 'nVperm':
				self.Vperm = float(args[0]) / 1e9
			if arg == 'pVperm':
				self.Vperm = float(args[0]) / 1e12
			if arg == 'kVperm':
				self.Vperm = float(args[0]) * 1e3
			if arg == 'MVperm':
				self.Vperm = float(args[0]) * 1e6
		self.mVperm = self.Vperm * 1000
		self.uVperm = self.Vperm * 1e6
		self.nVperm = self.Vperm * 1e9
		self.pVperm = self.Vperm * 1e12
		self.kVperm = self.Vperm / 1E3
		self.MVperm = self.Vperm / 1E6



class electricFluxDensity:
	def __init__(self,*args,**kwargs): 
		self.Cperm2 = float(args[0])
		for arg in args:
			if arg == 'Cperm2':
				pass
			if arg == 'uCperm2':
				self.Cperm2 = float(args[0]) / 1e6

		self.uCperm2 = self.Cperm2 * 1E6

class force:
	def __init__(self,*args,**kwargs):
		self.N = float(args[0])
		for arg in args:
			if arg == 'N':
				pass
			if arg == 'kN':
				self.N = float(args[0]) * 1000
			if arg == 'lb' or arg =='lbf':
				self.N = float(args[0]) * 4.44822
			if arg == 'kips':
				self.N = float(args[0]) * 4.44822 * 1000
	   
		self.kN = self.N / 1000
		self.mN = self.N * 1e3
		self.uN = self.N * 1e6
		self.nN = self.N * 1e9
		self.pN = self.N * 1e12
		
		self.lb = self.N / 4.44822 
		self.lbf = self.N / 4.44822
		self.kips = self.N / (4.44822 * 1000)
		
class forcePerLength:
	def __init__(self,*args,**kwargs): 
		self.Nperm = float(args[0])
		for arg in args:
			if arg == 'Nperm':
				self.Nperm = float(args[0])
			if arg == 'Npercm':
				self.Nperm = float(args[0]) * 100
			if arg == 'kipsperft':
				self.Nperm = float(args[0]) * 9.81 * 3.28 * 1000 / (2.2)
		self.Npercm = self.Nperm / 100
		self.kipsperft = self.Nperm 
		
class frequency:
	def __init__ (self, *args, **kwargs):
		self.Hz = float(args[0])
		self.hz = float(args[0])
		
		for arg in args:
			if arg == 'hz' or arg == 'Hz':
				self.Hz = float(args[0])
				self.hz = float(args[0])
			if arg == 'kHz':
				self.Hz = float(args[0])*1000
			if arg == 'MHz':
				self.Hz = float(args[0])*1e6
			if arg == 'GHz':
				self.Hz = float(args[0])*1e9
				
				
		self.kHz = self.Hz / 1000
		self.MHz = self.Hz / 1e6
		self.GHz = self.Hz / 1e9
		
class inductance:
	def __init__(self,*args,**kwargs): 
		
		self.H = float(args[0]) 
		for arg in args:
			if arg == 'mH':
				self.H = float(args[0]) / 1000
			if arg == 'uH':
				self.H = float(args[0]) / 1e6
			if arg == 'nH':
				self.H = float(args[0]) / 1e9
			if arg == 'pH':
				self.H = float(args[0]) / 1e12

			if arg == 'e12':
				digits = float(random.choice(E12))
				for i in range(-22, 22):
					if 10**i <= float(args[0]) < 10**(i+1):
						self.H = digits * 10**i
		
		self.mH = self.H * 1000
		self.uH = self.H * 1e6
		self.nH = self.H * 1e9
		self.pH = self.H * 1e12

	def series(self, object):
		return inductance(self.H + object.H)

	def parallel(self, object):
		return inductance( (self.H * object.H) / ( self.H + object.H))
		
			
class length:
	def __init__(self,*args,**kwargs):
		self.m = float(args[0])   
		for arg in args:
			if arg == 'cm':
				self.m = float(args[0])/100
			if arg == 'mm':
				self.m = float(args[0])/1000
			if arg == 'um':
				self.m = float(args[0])/1e6
			if arg == 'nm':
				self.m = float(args[0])/1e9
			if arg == 'pm':
				self.m = float(args[0])/1e12
			if arg == 'km':
				self.m = float(args[0])*1000
			if arg == 'in' or arg == 'inch':
				self.m = float(args[0]) / 39.37
			if arg == 'ft' or arg == 'feet':
				self.m = float(args[0]) / 3.281
			if arg == 'mi' or arg == 'miles':
				self.m = float(args[0]) * 1609.344
			
				
				
		self.Tm = self.m * 1E-12
		self.Gm = self.m * 1E-9
		self.Mm = self.m * 1E-6
		self.km = self.m * 1E-3
		self.dm = self.m * 1E1
		self.cm = self.m * 1E2
		self.mm = self.m * 1E3
		self.um = self.m * 1E6
		self.nm = self.m * 1E9
		self.pm = self.m * 1E12
		self.fm = self.m * 1E15
		self.am = self.m * 1E18
		self.inch = self.m * 39.37
		
		self.ft = self.m * 3.281
		self.feet = self.ft
		
		self.mi = self.m / 1609.344
		self.miles = self.mi
		self.mile = self.mi

class linearMassDensity:
	def __init__(self,*args,**kwargs):
		self.kgperm = float(args[0])

class magneticFlux:
	def __init__(self,*args,**kwargs): 
		self.weber = float(args[0])
		self.Wb = float(args[0])
		for arg in args:
			if arg == 'Wb':
				pass
			if arg == 'mWb' or arg == 'mweber':
				self.Wb = float(args[0]) / 1000
			if arg == 'uWb':
				self.Wb = float(args[0]) / 1e6
			
		self.weber = self.Wb
		self.mWb = self.Wb * 1000
		self.uWb = self.Wb * 1e6

		
class magneticFluxDensity:
	def __init__(self,*args,**kwargs): 
		self.T = float(args[0])
		for arg in args:
			if arg == 'T' or arg == 'tesla':
				pass
			if arg == 'mT':
				self.T = float(args[0]) / 1E3
			if arg == 'uT':
				self.T = float(args[0]) / 1e6

		self.uT = self.T * 1e6
		self.mT = self.T * 1e3

class magnetizingForce:
	def __init__(self, *args, **kwargs):
		self.Aperm = float(args[0])
		
class mass:
	def __init__(self, *args, **kwargs):
		self.kg = float(args[0])
			
		for arg in args:
			if arg == 'kg':
				self.kg = float(args[0])
			if arg == 'g':
				self.kg = float(args[0]) / 1000
			if arg == 'lbm' or arg == 'lb':
				self.kg = float(args[0]) / 2.205
			if arg == 'slug':
				self.kg = float(args[0]) * 14.594
		
		self.g = self.kg * 1000
		self.lbm = self.kg * 2.205
		self.slug = self.kg * 14.594		

class momentOfInertia:
	def __init__(self,*args,**kwargs): 
		self.kgm2 = float(args[0])

class pesos:
	def __init__(self,*args,**kwargs): 
		try:
			self.pesos = round(float(args[0]),2)
			self.pesos_string = f"""PHP {self.pesos:,}"""
		except:
			self.pesos = 'N/A'
			self.pesos_string = 'N/A'
	
		
class percentage:
	def __init__(self,*args, **kwargs):
		self.decimal = float(args[0])
		for arg in args:
			if arg == 'whole' or arg == 'decimal':
				self.whole = float(args[0])
				self.decimal = float(args[0])
				
			if arg == 'percent':
				self.whole = float(args[0]) / 100 #for backward compatibility
				self.decimal = float(args[0]) / 100
				
		self.percent = self.decimal * 100

class polar_moment_of_inertia():
	def __init__(self, *args):
		self.m4 = float(args[0])
		
		
class power:
	def __init__ (self, *args, **kwargs):
		self.W = float(args[0])
		for arg in args:
			if arg =='W':
				pass
			if arg == 'hp':
				self.W = float(args[0]) * 746
			if arg == 'kW':
				self.W = float(args[0]) * 1000
			if arg == 'MW':
				self.W = float(args[0]) * 1e6
			if arg == 'VA':
				self.W = float(args[0])
			if arg == 'kVA':
				self.W = float(args[0]) * 1000
			if arg == 'mW':
				self.W = float(args[0]) / 1000
			if arg == 'uW':
				self.W = float(args[0]) / 1e6
			if arg == 'nW':
				self.W = float(args[0]) / 1e9
			if arg == 'pW':
				self.W = float(args[0]) / 1e12
			if arg == 'dBW' or arg == 'dB':
				self.W = 10**(float(args[0])/10)
			if arg == 'dBm':
				self.W = (10**(float(args[0])/10) / 1000 )
		
		self.hp = self.W / 746
		self.kW = self.W / 1000
		self.MW = self.W / 1e6
		self.VA = self.W
		self.kVA = self.W / 1000
		self.mW = self.W * 1000
		self.uW = self.W * 1e6
		self.nW = self.W * 1e9
		self.pW = self.W * 1e12


		try:
			self.dBW = 10 * math.log(self.W , 10)
			self.dB = self.dBW
		except:
			pass
		try:
			self.dBm = 10 * math.log(self.W / 1e-3, 10)
		except:
			pass
			
class powerDensity:
	def __init__(self,*args,**kwargs): 
		self.Wperm2 = float(args[0])
		for arg in args:
			if arg == 'kWperm2':
				self.Wperm2 = float(args[0]) * 1000
			if arg == 'mWperm2':
				self.Wperm2 = float(args[0]) / 1000
			if arg == 'uWperm2':
				self.Wperm2 = float(args[0]) / 1e6
			if arg == 'nWperm2':
				self.Wperm2 = float(args[0]) / 1e9
			if arg == 'pWperm2':
				self.Wperm2 = float(args[0]) / 1e12
		
		
		self.mWperm2 = self.Wperm2 * 1000
		self.uWperm2 = self.Wperm2 * 1e6
		self.nWperm2 = self.Wperm2 * 1e9
		self.pWperm2 = self.Wperm2 * 1e12
		
class powerGain:
	def __init__(self,*args,**kwargs): 
		self.unitless = float(args[0])
		for arg in args:
			if arg == 'dB':
				self.unitless = 10**(float(args[0]) / 10)
		
		self.dB = 10 * math.log(self.unitless, 10)
		

class pressure:
	def __init__(self,*args,**kwargs): 
		self.Pa = float(args[0])
		for arg in args:
			if arg == 'Pa':
				self.Pa = float(args[0])
			if arg == 'kPa' or arg == 'kNperm2':
				self.Pa = float(args[0]) * 1e3
			if arg == 'MPa' or arg == 'MNperm2':
				self.Pa = float(args[0]) * 1e6
			if arg == 'psi':
				self.Pa = float(args[0]) * 6894.757
			if arg == 'ksi':
				self.Pa = float(args[0]) * 6894.757 * 1000
			if arg == 'mmHg':
				self.Pa = float(args[0]) * 133.322
			if arg == 'cmHg':
				self.Pa = float(args[0]) * 133.322 * 10
			if arg == 'mHg':
				self.Pa = float(args[0]) * 133.322 * 1000
			
		self.MPa = self.Pa / 1e6
		self.kPa = self.Pa / 1e3
		self.MNperm2 = self.Pa / 1e6
		self.psi = self.Pa / 6894.757
		self.ksi = self.Pa / (6894.757 * 1000)
		self.mmHg = self.Pa / 133.322
		self.cmHg = self.Pa / (133.322 * 10)
		self.mHg = self.Pa / (133.322 * 1000)

class reluctance:
	def __init__(self, *args, **kwargs):
		self.perH = float(args[0])

class resistance:
	def __init__(self, *args, **kwargs):
		
		self.ohm = float(args[0])
		#self.E12 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39,43,47,51, 56, 62,68,75,82,91]

		for arg in args:
			if arg == 'mohm' or arg == 'mohms':
				self.ohm = float(args[0]) / 1000
			if arg == 'kohm' or arg == 'kohms':
				self.ohm = float(args[0]) * 1000
			if arg == 'Mohm' or arg == 'Mohms':
				self.ohm = float(args[0]) * 1e6

			if arg == 'e12':
				digits = float(random.choice(E12))
				for i in range(-22, 22):
					if 10**i <= float(args[0]) < 10**(i+1):
						self.ohm = digits * 10**i

		self.ohms = self.ohm
		self.Gohm = self.ohm * 1E-9
		self.Mohm = self.ohm * 1E-6
		self.kohm = self.ohm * 1E-3
		self.mohm = self.ohm * 1E3
		
		#duplicate for ohms
		self.Gohms = self.ohm * 1E-9
		self.Mohms = self.ohm * 1E-6
		self.kohms = self.ohm * 1E-3
		self.mohms = self.ohm * 1E3

		
	def parallel(self, resistance_object):
		
		result = (self.ohms * resistance_object.ohms) / ( self.ohms + resistance_object.ohms )
		
		return resistance(result)

	def series(self, resistance_object):

		result = (self.ohms + resistance_object.ohms)

		return resistance(result)

		

class resistor:
	def __init__(self, band = 4, **kwargs):
		if band == 4 or band == 3 :
			color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']
			tolerance_list = ['gold', 'silver', 'no band']
			Tvalue = [0.05, 0.1, 0.2]
			tolerance = ['5%', '10%', '20%']


			D1 = random.randint(0, len(color_list) - 1 )
			D0 = random.randint(0, len(color_list) - 1 )
			M = random.randint(0, 5)
			T = random.randint(0, 1)

			if band == 3:
				T = 2

			D1word = color_list[D1]
			D0word = color_list[D0]
			Mword = color_list[M]
			Tword = tolerance_list[T]

			self.color = D1word + '-' + D0word + '-' + Mword + '-' + Tword
			self.resistance = resistance( (D1 * 10 + D0) * 10**(M), 'ohms')
			self.tolerance = tolerance[T]
			self.tolerance_value = Tvalue[T]

			self.maxresistance = resistance(self.resistance.ohms * (1 + self.tolerance_value))
			self.minresistance = resistance(self.resistance.ohms * (1 - self.tolerance_value))

		if band == 5:
			color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']
			tolerance_list = ['red', 'brown', 'green', 'blue', 'violet']
			Tvalue = [0.02, 0.01, 0.005, 0.0025, 0.001]
			tolerance = ['2%', '1%', '0.5%', '0.25%', '0.1%']

			D2 = random.randint(0, len(color_list) - 1 )
			D1 = random.randint(0, len(color_list) - 1 )
			D0 = random.randint(0, len(color_list) - 1 )
			M = random.randint(0, 5)
			T = random.randint(0, 1)

			D2word = color_list[D2]
			D1word = color_list[D1]
			D0word = color_list[D0]
			Mword = color_list[M]
			Tword = tolerance_list[T]

			self.color = D2word + '-' + D1word + '-' + D0word + '-' + Mword + '-' + Tword
			self.resistance = resistance( (D2 * 100 + D1 * 10 + D0) * 10**(M), 'ohms')
			self.tolerance = tolerance[T]
			self.tolerance_value = Tvalue[T]

			self.maxresistance = resistance(self.resistance.ohms * (1 + self.tolerance_value))
			self.minresistance = resistance(self.resistance.ohms * (1 - self.tolerance_value))

class resistivity:   
	def __init__(self,*args, **kwargs):
		
		self.ohm_m = float(args[0])
		
		for arg in args:
			if arg == 'ohm cm':
				self.ohm_m = float(args[0]) * 100
				  
		self.mohm_m = self.ohm_m * 1e3
		self.uohm_m = self.ohm_m * 1E6
		self.ohm_cm = self.ohm_m / 100
		
class relativePermittivity_material:
	def __init__(self,*args,**kwargs): 
		
		list_materials = [
		['vacuum', 1],
		['air', 1.000_589_86],
		['PTFE / Teflon', 2.1],
		['polyethelyne', 2.25],
		['polyimide', 3.4],
		['polypropylene', 2.3],
		['polystyrene', 2.55],
		['carbon disulfide', 2.6],
		['mylar', 3.1],
		['paper', 1.4],
		]
		
		i = random.randint(0, len(list_materials) - 1)
		self.name = list_materials[i][0]
		self.relativePermittivity = list_materials[i][1]
		
class springConstant:
	def __init__(self,*args,**kwargs):
		self.Nperm = float(args[0])
		for arg in args:
			if arg == 'Nperm':
				self.Nperm = float(args[0])
			if arg == 'Npercm':
				self.Nperm = float(args[0]) * 100  
			if arg == 'kNperm':
				self.Nperm = float(args[0]) * 1000
				
		self.Npercm = self.Nperm / 100
		
class stress:
	def __init__(self,*args,**kwargs): 
		self.Pa = float(args[0])
		for arg in args:
			if arg == 'Pa':
				self.Pa = float(args[0])
			if arg == 'kPa' or arg == 'kNperm2':
				self.Pa = float(args[0]) * 1e3
			if arg == 'MPa' or arg == 'MNperm2':
				self.Pa = float(args[0]) * 1e6
			if arg == 'GPa' or arg == 'GNperm2':
				self.Pa = float(args[0]) * 1e9
			if arg == 'psi':
				self.Pa = float(args[0]) * 6894.757
			if arg == 'ksi':
				self.Pa = float(args[0]) * 6894.757 * 1000
				
				
		self.MPa = self.Pa / 1e6
		self.GPa = self.Pa / 1e9
		self.MNperm2 = self.Pa / 1e6
		self.GNperm2 = self.Pa / 1e9
		self.psi = self.Pa / 6894.757
		self.ksi = self.Pa / (6894.757 * 1000)
				 
class temperature:
	def __init__(self,input,*args):
		kelvin = input
		for arg in args:
			if arg == 'K':
				kelvin = input
			if arg == 'C':
				kelvin = input + 273.15
			if arg == 'F':
				kelvin = (input*(5/9) - 32) + 273.15
			if arg == 'R':
				kelvin = ((input-460)*(5/9) - 32) + 273.15
		self.K = kelvin
		self.C = kelvin - 273.15
		self.F = (self.C * (9/5)) + 32
		self.R = self.F + 460
		
class thermalResistance:
	def __init__(self,*args,**kwargs): 
		self.CperW = float(args[0])
				
class time:
	def __init__(self, *args, **kwargs):
		self.s = float(args[0])       
		for arg in args:
			if arg == 's':
				pass
			if arg == 'min':
				self.s = float(args[0])*60
			if arg == 'ms':
				self.s = float(args[0]) / 1000
			if arg == 'hours' or arg == 'hour' or arg == 'hr':
				self.s = float(args[0]) * 3600
				
		self.min = self.s / 60
		self.hour = self.s / 3600
		self.hours = self.s / 3600
		self.day = self.s /(3600*24)
		self.days = self.s / (3600*24)
		self.ms = self.s * 1000
		self.us = self.s * 1E6
		self.ns = self.s * 1E9
		self.ps = self.s * 1E12
		self.fs = self.s * 1E15

		
class torque:
	def __init__(self,*args,**kwargs): 
		self.Nm = float(args[0])
		for arg in args:
			if arg == 'Nm':
				pass
			if arg == 'kNm':
				self.Nm = float(args[0]) * 1000
			if arg == 'lbft' or arg == 'lbsft':
				self.Nm = float(args[0]) * 1.35582
			if arg == 'kipft' or arg == 'kipsft':
				self.Nm = float(args[0]) * 1000 * 1.35582
				
		self.kNm = self.Nm / 1000
		self.lbft = self.Nm  / 1.35582
		self.kipft = self.Nm / (1000*1.35582)
		self.kipsft = self.kipft

class moment(torque):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class velocity:
	def __init__(self, *args, **kwargs):
		self.mpers = float(args[0])
		for arg in args:
			if arg == 'mpers':
				self.mpers = float(args[0])
			if arg == 'cmpers':
				self.mpers = float(args[0])/100
			if arg == 'kmperh':
				self.mpers = float(args[0]) / 3.6
			if arg == 'kmperyear':
				self.mpers = float(args[0])*31536
			if arg == 'kmpers':
				self.mpers = float(args[0])*1000
				
		self.cmpers = self.mpers * 100
		self.kmperh = self.mpers * 3.6
		self.kmperyear = self.mpers / 31536
		self.kmpers = self.mpers / 1000
	 
class voltage:
	def __init__(self, *args, **kwargs):
		self.V = float(args[0])		
		
		for arg in args:
			if arg == 'kV':
				self.V = float(args[0]) * 1000
			if arg == 'mV':
				self.V = float(args[0]) / 1e3
			if arg == 'uV':
				self.V = float(args[0]) / 1e6
		
		self.kV = self.V / 1e3
		self.mV = self.V * 1e3
		self.uV = self.V * 1e6
		self.nV = self.V * 1e9
		self.pV = self.V * 1e12

class volume:
	def __init__(self,*args,**kwargs):
		self.m3 = float(args[0])
		for arg in args:
			if arg == 'm3':
				pass
			if arg == 'L' or arg == 'liters':
				self.m3 = float(args[0]) / 1000
			if arg == 'mL':
				self.m3 = float(args[0]) / 1e6
			if arg == 'cm3':
				self.m3 = float(args[0]) / 1e6
				
		self.L = self.m3 * 1000
		self.mL = self.m3 * 1e6
		self.cm3 = self.m3 * 1e6
		
