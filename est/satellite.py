import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

gravity = c.acceleration(9.81, 'mpers2')

class jma_5_89:
    def __init__(self, *args, **kwargs):
        self.question = f"""Calculate the approximate height of a GEO satellite using Kepler's third law. A = 42241.0979, P = 0.9972."""
        
        self.answer = f"""Height from earth's surface = 35876.21 km"""
        
class jma_5_93:
    def __init__(self, *args, **kwargs):
        
        latitude = c.angle(ran.main(38.8), 'degrees')
        longitude = c.angle(ran.main(77), 'degrees')
        satlongitude = c.angle(ran.main(134), 'degrees')
        re = c.length(6400, 'km')
        
        self.question = f"""Calculate the elevation angle, azimuth and slant range between the TVRO site ( {latitude.degrees} degrees N, {longitude.degrees} degrees W) and a satellite that is in a geo-stationary orbit at {satlongitude.degrees} degrees W longitude above the equator."""
        
        phi = c.angle(
        math.acos(
        math.cos(latitude.rad) * math.cos(satlongitude.rad -longitude.rad) 
        )
        )
        
        
        
        elevation = c.angle(
        math.atan(
        (1/math.tan(phi.rad)) - (re.km/((re.km + 36_000) * math.sin(phi.rad)))
        )
        )
        
        azimuth = c.angle(
        math.acos(
        -math.tan(latitude.rad) / math.tan(phi.rad)
        )
        )
        
        distance = c.length(
        - re.km * math.sin(elevation.rad) + math.sqrt(
        (re.km + 36_000)**2 + re.km**2 * math.cos(elevation.rad)**2
        ), 'km'
        )
        
        self.answer = f"""Elevation angle = {elevation.degrees} degrees
Azimuth = {azimuth.degrees} degrees
Distance = {distance.km} km"""

class jma_5_94:
    def __init__(self, *args, **kwargs):
        
        h = c.length(ran.main(15_000), 'km')
        
        self.question = f"""Determine the orbital period and orbital velocity of a satellite located {h.km} km above the surface of the earth."""
        
        period = c.time(
        2 * math.pi * math.sqrt(
        (6400 + h.km)**3 / ( gravity.kmpers2 * 6400**2 )
        )
        )
        
        velocity = c.velocity(
        math.sqrt(
        ( gravity.kmpers2 * 6400**2 ) / ( 6400 + h.km )
        )
        )
        
class jma_5_96:
    def __init__(self, *args, **kwargs):
        
        frequency = c.frequency(ran.main(12), 'GHz')
        
        self.question = f"""Calculate the propagation time, propagation delay, and FSL for a geo-stationary satellite located directly above an earth station antenna with an operating frequency of {frequency.GHz} GHz."""
        
        propagation_time = c.time(
        36_000 * 1000 / 3e8
        )
        
        propagation_delay = c.time(
        2 * propagation_time.s
        )
        
        fsl = c.powerGain(
        92.4 + 20 * math.log(frequency.GHz * 36_000, 10), 'dB'
        )
        
        self.answer = f"""Propagation time = {propagation_time.ms} ms
Propagation delay = {propagation_delay.ms} ms
Free space loss = {fsl.dB} dB"""

class jma_5_97:
    def __init__(self, *args, **kwargs):
        
        txpower = c.power(
        ran.main(500), 'W'
        )
        
        bitrate = c.bitrate(
        ran.main(50), 'Mbps'
        )
        
        self.question = f"""In satellite communications system, for a total transmit power of {txpower.W} watts, determine the energy per bit for a transmission rate of {bitrate.Mbps} Mbps expressed in dBW."""
        
        eb = c.power(
        txpower.dBW - 10 * math.log(bitrate.Mbps, 10), 'dBW'
        )
        
        self.answer = f"""Energy per bit = {eb.dBW} dBW / bps"""
        
class jma_5_98:
    def __init__(self, *args, **kwargs):
        
        bandwidth = c.frequency(
        ran.main(10), 'MHz'
        )
        
        noisepower = c.power(
        ran.main(0.0280), 'pW'
        )
        
        self.question = f"""For an equivalent noise bandwidth of {bandwidth.MHz} MHz in a satellite system and noise power of {noisepower.pW} pW, determine the noise density in dBW."""
        
        no = c.power(
        noisepower.dBW - 10 * math.log(bandwidth.Hz, 10), 'dBW'
        )
        
        self.answer = f"""Noise bandwidth = {no.dBW} dBW / Hz"""
        
class jma_5_99_a:
    def __init__(self, *args, **kwargs):
        
        cpernup = c.dbvalue(ran.main(80), 'dB')
        cperndown = c.dbvalue(ran.main(90), 'dB')
        
        
        self.question = f"""For a satellite communication channel, the uplink C / No ratio is {cpernup.dB} dB / Hz. And the downlink value is {cperndown.dB} dB/Hz. Calculate the overall C / No ratio in dB / Hz."""
        
        cpernoverall = c.dbvalue(
        1 / (
        (1/cpernup.unitless) + (1/cperndown.unitless)
        )
        )
        
        self.answer = f"""Overall C / No  = {cpernoverall.dB} dB / Hz"""

class jma_5_99_b:
    def __init__(self, *args, **kwargs):
        
        bitrate = c.bitrate(ran.main(20), 'Mbps')
        cpern = c.dbvalue(ran.main(8.8), 'dB')
        
        self.question = f"""A coherent binary phase shift keyed BPSK transmitter operates at a bit rate of {bitrate.Mbps} Mbps with a carrier to noise ratio C/N of {cpern.dB} dB. Find the Eb/No."""
        
        ebno = c.dbvalue(
        cpern.dB + 10 * math.log( 1 ), 'dB'
        )
        
        self.answer=  f"""Eb / No = {ebno.dB} dB"""
        
class jma_5_100:
    def __init__(self, *args, **kwargs):
        
        
        gpert = c.dbvalue(ran.main(25), 'dB')
        distance_satellite = c.length(ran.main(38_000), 'km')
        power = c.power(ran.main(100), 'W')
        antenna_satellite = c.antennaGain(ran.main(30), 'dBi')
        bandwidth = c.frequency(ran.main(1), 'MHz')
        frequency = c.frequency(ran.main(12), 'GHz')
        
        
        self.question = f"""A receiving antenna with a G/T of {gpert.dB} dB is used to receive signals from a satellite {distance_satellite.km} km away. The satellite has a {power.W}-watt transmitter and an antenna with a gain of {antenna_satellite.dB} dBi. The signal has a bandwidth of {bandwidth.MHz} MHz at a frequency of {frequency.GHz} GHz. Calculate the C/N at the receiver."""
        
        eirp = c.power(
        power.dBW + antenna_satellite.dBi, 'dBW'
        )
        
        fsl = c.dbvalue(
        92.4 + 20 * math.log( frequency.GHz * distance_satellite.km , 10) , 'dB'
        )
        
        cpern = c.dbvalue(
        eirp.dBW - fsl.dB + gpert.dB + 228.6 - 10 * math.log( bandwidth.Hz , 10), 'dB'
        )
        
        self.answer = f"""C/N  = {cpern.dB} dB"""
        
class jma_5_101:
    def __init__(self, *args, **kwargs):
        
        antenna_receiver = c.antennaGain(ran.main(38), 'dB')
        sky_noisetemp = c.temperature(ran.main(15), 'K')
        feedhorn_loss = c.dbvalue(ran.main(0.5), 'dB')
        LNA_noisetemp = c.temperature(ran.main(38), 'K')
        
        self.question = f"""Calculate the G/T of a receiving antenna with a gain of {antenna_receiver.dB} dB and looks at the sky with a noise temperature of {sky_noisetemp.K} K if the loss between the antenna and the LNA input, due to feedhorn, is {feedhorn_loss.dB} dB, and the LNA has a noise temperature of {LNA_noisetemp.K} K"""
        
        gain = c.dbvalue(
        antenna_receiver.dB - feedhorn_loss.dB, 'dB'
        )
        
        ta = c.temperature(
        (290 * (feedhorn_loss.unitless - 1) + sky_noisetemp.K ) / 
        ( feedhorn_loss.unitless )
        ,'K')
        
        gpert = c.dbvalue(
        gain.dB - 10 * math.log( sky_noisetemp.K + LNA_noisetemp.K, 10), 'dB'
        )
        
        self.answer = f"""G/T = {gpert.dB} dB"""
        


