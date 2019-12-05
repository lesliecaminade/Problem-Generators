import math
import random
import sympy as sp
import stringHandling

#from sympy import *

#symbols for sympy
spa, spb, spc, spd, spx, spy, spz = sp.symbols('a b c d x y z', real = True)
spn = sp.symbols('n', real = True)


title_string = """Antenna Fundamentals by JMA
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""
SPEED_OF_LIGHT = 299792458

class antennaFundamentalsClass:

    def __init__(self):
        form = random.randint(1,9) #check
        if form == 1:
            radiation_resistance = random.randint(50,80)
            loss_resistance = random.randint(1,10)
            efficiency = (radiation_resistance/(radiation_resistance + loss_resistance))*100
            
            question = """Calculate the efficiency of a dipole antenna that has a radiation resistance of {a:g} ohms and a loss resistance of {b:g} ohms, measured at the feedpoint.""".format(a=radiation_resistance,b=loss_resistance)
            
            soln = """Efficiency: {a:g} %""".format(a=round(efficiency,2))
        
        if form == 2:
            gain_dBd = round(random.uniform(3,7),1)
            efficiency = random.randint(80,99)
            
            gain_dBi = gain_dBd - 2.14
            
            power_gain = 10**(gain_dBi/10)*(efficiency/100)
            power_gain_dB = 10*math.log(power_gain,10)
            
            question = """Calculate the gain of a certain antenna relative to a dipole antenna with a gain of {a:g} dB with respect to an isotropic radiator. Also compute for the power gain if the antenna has an efficiency of {b:g}%""".format(a=gain_dBd,b=efficiency)
            
            soln = """Gain(iso): {a:g} dBi, Power gain: {b:g} dBi""".format(a=round(gain_dBi,2),b=round(power_gain_dB,2))
            
        if form == 3:
            temp = random.randint(1,2)
            antenna_type_list = ['none','Hertzian Dipole','Half-wave dipole']
            antenna_type = antenna_type_list[temp]
            antenna_gain_list = [0,1.5,1.64]
            gain = antenna_gain_list[temp]
            freq = random.randint(10,30) * 10 * 10**6
            
            power_tx = random.randint(10,50)
            distance = random.randint(10,50)*1000

            wavelength = SPEED_OF_LIGHT/freq
            power_density = (power_tx*gain)/(4*math.pi*distance**2)
            capture_area = (wavelength**2*gain)/(4*math.pi)            
            captured_power = power_density * capture_area
            
            question = """Calculate the captured power {a:g} km away from a half-wave dipole transmitter with {b:g} W transmit power for the following antenna at {c:g} MHz; {type:s}""".format(a=distance/1000,b=power_tx,c=freq/10**6,type = antenna_type )
            
            soln = """Captured Power: {a:g} W""".format(a=captured_power)
            
        if form == 4:
            freq = random.randint(10,50)*10*10**6
            distance = random.randint(10,50)/100
            
            radiation_resistance = 75/(math.sin((distance*math.pi)/(SPEED_OF_LIGHT/freq))**2)
            
            question = """Calculate the radiation resistance of a half-wave dipole antenna if the feedpoint is {a:g} m from one end at {b:g} MHz""".format(a=distance,b=freq/10**6)
            
            soln = """Radiation Resistance: {a:g} ohms""".format(a=round(radiation_resistance,2))
            
        if form == 5:
            velocity_factor = random.randint(50,90)/100
            freq = random.randint(10,50)*10**6
            
            length = (SPEED_OF_LIGHT*velocity_factor)/freq
            length_in_feet = length*3.28
            
            question = """What is the actual length in feet of one-half wavelength of a coax with velocity factor of {a:g} at {b:g} MHz""".format(a=velocity_factor,b=freq/10**6)
            
            soln = """Actual length: {a:g} ft""".format(a=round(length_in_feet,2))
            
        if form == 6:
            freq = random.randint(100,200)*10**6
            wavelength = SPEED_OF_LIGHT/freq
            
            driven_length = 0.475*wavelength
            reflector_length = 0.49875*wavelength
            director_length = 0.451*wavelength
            
            question = """A Yagi-Uda antenna is designed to receive signals centered at {a:g} MHz. Calculate the length of the driven element, reflector, and director.""".format(a=freq/10**6)
            
            soln = """Driven element length: {a:g} m, Reflector element length: {b:g} m, Director element length {c:g} m""".format(a=round(driven_length,2),b=round(reflector_length,2),c=round(director_length,2))
        
        if form == 7:
            N = random.randint(5,9) 
            S = random.randint(500,999)/10
            D = random.randint(50,100)
            f = random.randint(10,20)/10 * 10**6
            wavelength = SPEED_OF_LIGHT/f
            
            G_dB = round(10*math.log(15*N*S*(math.pi*D)**2/wavelength**3,10),2)
            beamwidth_deg = round(((52*wavelength)/(math.pi*D))*math.sqrt(wavelength/(N*S)),2)
            
        
            question = """Calculate the gain and beamwidth of a helical antenna if the optimum diameter is {a:g} mm, pitch of {b:g} mm, with {c:g} turns and will operate at {d:g} GHz""".format(a=D,b=S,c=N,d=f/10**6)
            
            soln = """Gain: {a:g} dB, Beamwidth: {b:g}""".format(a=round(G_dB,2),b=round(beamwidth_deg,2))
            
        if form == 8:
            eff = random.randint(50,70)/100
            D = random.randint(10,30)/10
            f = random.randint(2,6)*10**9
            wavelength = SPEED_OF_LIGHT/f
            
            
            G = eff * (math.pi*D/wavelength)**2
            G_dB = 10*math.log(G)
            
            beamwidth_nulls_deg = 140* (wavelength/D)
            
            
            question = """Calculate the directive gain and beamwidth between nulls for a parabolic reflector antenna with a mouth diameter of {a:g} m and the illumination efficiency is {b:g}% operating at {c:g} GHz""".format(a=D, b = eff*100,c=f/10**9)
            
            soln = """Directive Gain: {a:g} dB, Beamwidth between nulls: {b:g} deg""".format(a=round(G_dB,2),b=round(beamwidth_nulls_deg,2))
            
        if form == 8:
            f = random.randint(3,7)*100*10**6
            wavelength = SPEED_OF_LIGHT/f
            beamwidth = random.randint(1,5)
            D = (70*wavelength)/beamwidth
        
            question = """To minimize interference, a {a:g}-MHz dish needs to have a {b:g}° beamwidth. What diameter dish is required?""".format(a=f/10**6,b=beamwidth)
            
            soln = """Diameter: {a:g} m""".format(a=round(D,2))
            
        if form == 9:
            f = random.randint(3,7)*10**9
            wavelength = SPEED_OF_LIGHT/f
            
            de = random.randint(50,99)/1000
            dh = random.randint(50,99)/1000
                        
            G = (7.5*de*dh)/(wavelength**2)
            G_dB = round(10*math.log(G,10),2)
            
            
            beamwidth_e = round((56*wavelength)/de,2)
            beamwidth_h = round((70*wavelength)/dh,2)
            
            question = """Calculate the gain and beamwidth in the E and H plane of a pyramidal horn antenna that has an aperture of {a:g} mm in the E-plane, {b:g} mm in the H-plane and operating at {c:g} GHz""".format(a=de*1000, b = dh*1000, c = f/10**9 )
            
            soln = """Gain: {a:g} dB, Beamwidth(E): {b:g}deg, Beamwidth(H): {c:g}deg""".format(a=round(G_dB,2),b=round(beamwidth_e,2),c=round(beamwidth_h,2))
            
            
        
        self.question = question
        self.soln = soln
        
            
            


print(title_string)
print()


 
for i in range (1,3):
    A = antennaFundamentalsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""*{a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))

    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
