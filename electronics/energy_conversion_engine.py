from generator import random_handler as ran
from generator import constants_conversions as c
import sympy
import math
import random
x, y, z = sympy.symbols('x y z', real = True)#sympy variables
            
class johnbird_4_1:
    def __init__(self,*args,**kwargs): 
        
        cells = int(ran.main(8))
        cell_resistance = c.resistance(ran.main(0.2))
        cell_voltage = c.voltage(ran.main(2.2))
        
        
        self.question = f"""For {cells} cells, each with an internal resistance of {cell_resistance.ohm:4.4} ohms and an emf of {cell_voltage.V:4.4} V are connected to a) in series b) in parallel. Determine the emf and the internal resistance of the batteries so formed."""

        bat_emf_series = c.voltage( cells * cell_voltage.V)
        bat_resistance_series = c.resistance( cells * cell_resistance.ohm)


        bat_emf_parallel = c.voltage( cell_voltage.V )
        bat_resistance_parallel = c.resistance( cell_resistance.ohm / cells)
        
        self.answer = f"""{bat_emf_series.V:4.4} V , {bat_resistance_series.ohm:4.4} ohms; {bat_emf_parallel.V:4.4} V, {bat_resistance_parallel.ohm:4.4} ohms"""

class johnbird_4_2:
    def __init__(self,*args,**kwargs): 
        
        cell_resistance = c.resistance(ran.main(0.02))
        cell_voltage = c.voltage(ran.main(2.0))
        cell_current = c.current(ran.main(5))
        cell_current2 = c.current(ran.main(50))
        
        self.question = f"""A cell has an internal resistance of {cell_resistance.ohm:4.4} ohms and an emf of {cell_voltage.V:4.4} V. Calculate its terminal potential difference if it delivers a) {cell_current.A:4.4} A and b) {cell_current2.A:4.4} A"""
        
        terminal_voltage = c.voltage( cell_voltage.V -  cell_current.A * cell_resistance.ohm)
        terminal_voltage2 = c.voltage( cell_voltage.V -  cell_current2.A * cell_resistance.ohm)
        
        self.answer = f"""{terminal_voltage.V:4.4} V, {terminal_voltage2.V:4.4} V"""

class johnbird_4_3:
    def __init__(self,*args,**kwargs): 
        
        bat_voltage = c.voltage(ran.main(25))
        bat_voltage_loaded = c.voltage(bat_voltage.V - ran.main(1))
        bat_current = c.current(ran.main(10))
        
        
        self.question = f"""The potential difference at the terminals of a battery is {bat_voltage.V:4.4} V when no load is connected and {bat_voltage_loaded.V:4.4} V when a load taking {bat_current.A:4.4} A is connected. Determine the internal resistance of the battery"""
        
        bat_resistance = c.resistance( (bat_voltage.V - bat_voltage_loaded.V ) / (bat_current.A))
        
        self.answer = f"""{bat_resistance.ohm:4.4} ohms"""
        
class johnbird_4_4:
    def __init__(self,*args,**kwargs): 
        
        cells = int(ran.main(10))
        cell_voltage = c.voltage(ran.main(1.5))
        cell_resistance = c.resistance(ran.main(0.2))
        load_resistance = c.resistance(ran.main(58))
        
        
        self.question = f"""For {cells} {cell_voltage.V:4.4} V cells, each having an internal resistance of {cell_resistance.ohm:4.4} ohms, are connected in series to a load of {load_resistance.ohm:4.4} ohms. Determine a) the current flowing in the circuit and b) the potential difference at the battery terminals."""
        
        bat_voltage = c.voltage( cell_voltage.V * cells)
        bat_resistance = c.resistance( cell_resistance.ohm * cells)
        load_current = c.current(  (bat_voltage.V) / (load_resistance.ohm + bat_resistance.ohm)  )
        
        bat_voltage_loaded = c.voltage( bat_voltage.V - load_current.A * bat_resistance.ohm )
        
        self.answer = f"""{load_current.A:4.4} A, {bat_voltage_loaded.V:4.4} V"""

class johnbird_21_1:
    def __init__(self,*args,**kwargs): 
        
        n1 = int(ran.main(500))
        n2 = int(ran.main(3000))
        v1 = c.voltage(int(ran.main(240)))
        
        self.question = f"""A transformer has {n1} primary turns and {n2} secondary turns. If the primary voltage is {v1.V}V, determine the secondary voltage, assuming an ideal transformer."""
        
        v2 = c.voltage(( v1.V * n2) / n1)

        self.answer = f"""{v2.V:4.4} V"""
        
class johnbird_21_2:
    def __init__(self,*args,**kwargs): 
        
        n1 = int(ran.main(2))
        n2 = int(ran.main(7))
        v1 = c.voltage(int(ran.main(240)))
        
        self.question = f"""An ideal transformer with a turns ratio of {n1}:{n2} is fed from a {v1.V}V supply. Determine its output voltage."""
        
        v2 = c.voltage((v1.V * n2)/ n1)
        
        self.answer = f"""{v2.V:4.4} V"""
        
class johnbird_21_3:
    def __init__(self,*args,**kwargs): 
        np = int(ran.main(8))
        ns = 1
        ip = c.current(int(ran.main(3)))
        vp = c.voltage(int(ran.main(240)))
        
        self.question = f"""An ideal transformer has a turns ratio of {np}:{ns} and the primary current is {ip.A} A when it is supplied by {vp.V} V. Calculate the secondary voltage."""
        
        a = np / ns
        vs = c.voltage( (vp.V * ns) / np )
        isec = c.current(ip.A * np / ns)
        
        self.answer = f"""{vs.V:4.4} V, {isec.A:4.4} A"""

class johnbird_21_4:
    def __init__(self,*args,**kwargs): 
        vmains = c.voltage(int(ran.main(240)))
        vload = c.voltage(int(ran.main(12)))
        pload = c.power(int(ran.main(150)), 'W')
        
        self.question = f"""An ideal transformer, connected to a {vmains.V} V mains, supplies a {vload.V}V, {pload.W} W lamp. Calculate the transformer turns ratio and the current taken from the supply."""
        
        ratio = vmains.V  / vload.V
        
        iload = c.current(pload.W / vload.V)
        imains = c.current(iload.A * vload.V / vmains.V)

        self.answer = f"""{ratio:4.4}, {imains.A:4.4} A"""

class johnbird_21_5:
    def __init__(self,*args,**kwargs): 
        resistance = c.resistance(int(ran.main(12)))
        voltage_sec = c.voltage(int(ran.main(120)))
        current_prim = c.current(int(ran.main(4)))
        
        
        self.question = f"""A {resistance.ohm} ohms resistor is connected across the secondary winding of an ideal transformer whose secondary voltage is {voltage_sec.V} V. Determine the primary voltage if the supply current is {current_prim.A}."""
        
        current_sec = c.current(voltage_sec.V / resistance.ohms)
        voltage_prim = c.voltage( voltage_sec.V * current_prim.A / current_sec.A)
        
        self.answer = f"""{voltage_prim.V:4.4} V"""

class johnbird_21_6:
    def __init__(self,*args,**kwargs): 
        
        power  = c.power(int(ran.main(5)), 'kVA')
        turns_primary = int(ran.main(10))
        turns_secondary = 1
        voltage_primary = c.voltage(ran.main(2500), 'V')
        
            
        self.question = f"""A {power.kVA} kVA single-phase transformer has a turns ratio of {turns_primary}:{turns_secondary} and is fed from a {voltage_primary.kV} kV supply. Neglecting losses, determine (a) the full-load secondary current, (b) the minimum load resistance which can be connected across the secondary winding to give full load kVA, (c) the primary current at full load kVA."""
            
        voltage_secondary = c.voltage( voltage_primary.V * turns_secondary / turns_primary)
        
        current_secondary = c.current( power.VA / voltage_primary.V  )
        
        resistance_minimum = c.resistance( voltage_primary.V / voltage_secondary.V )
        
        current_primary = c.current( current_secondary.A * turns_secondary / turns_primary  )
        
        self.answer = f"""{current_secondary.A:4.4} A, {resistance_minimum.ohm:4.4} ohms, {current_primary.A:4.4} A"""

####################################################################3
# added June 11 2019

class johnbird_21_7:
    def __init__(self,*args,**kwargs): 
        
        primary_voltage = c.voltage(int(ran.main(24))*100)
        secondary_voltage = c.voltage(int(ran.main(4))*100)
        noload_current = c.current(ran.main(0.5))
        core_power = c.power(int(ran.main(4))*100)
        
        
        self.question = f"""A {primary_voltage.V} V / {secondary_voltage.V} V single phase transformer takes a no-load current of {noload_current.A:4.4} A and the core loss is {core_power.W} W. Determine the values of the magnetising and the core loss components of the no-load current."""
        
        phase_angle = c.angle(math.acos(  (core_power.W) / (primary_voltage.V * noload_current.A)  ), 'rad')
        
        magnetizing_current = c.current( noload_current.A * math.sin(phase_angle.rad) )
        
        coreloss_current = c.current( noload_current.A * math.cos(phase_angle.rad))
        
        self.answer = f"""{magnetizing_current.A:4.4} A, {coreloss_current.A:4.4} A"""

class johnbird_21_8:
    def __init__(self,*args,**kwargs): 
        
        noload_current = c.current( ran.main(0.8))
        primary_voltage = c.voltage(ran.main(240))
        power = c.power(ran.main(72))
        
        self.question = f"""A transformer takes a current of {noload_current.A:4.4} A when its primary is connected to a {primary_voltage.V:4.4} volt, 50 Hz supply, the secondary being on open circuit. If the power absorbed is {power.W:4.4} watts, determine a) the iron loss current, b) the power factor on no-load, and c) the magnetizing current."""
        
        coreloss_current = c.current( power.W / primary_voltage.V )
        
        powerfactor = c.percentage(coreloss_current.A / noload_current.A, 'decimal')
        
        magnetizing_current = c.current(  math.sqrt(noload_current.A**2 - coreloss_current.A**2) )
        
        self.answer = f"""{coreloss_current.A:4.4} A, {powerfactor.decimal:4.4}, {magnetizing_current.A:4.4} A"""


class johnbird_21_9:
    def __init__(self,*args,**kwargs): 
        
        frequency = c.frequency(50, 'Hz')
        primary_voltage = c.voltage( ran.main(4000))
        secondary_voltage = c.voltage( ran.main(200))
        secondary_turns = ran.main(100)
        power = c.power(100, 'kVA')
        
        
        self.question = f"""A {power.kVA:4.4} kVA, {primary_voltage.V:4.4} V / {secondary_voltage.V:4.4} V, 50 Hz, single-phase transformer has {secondary_turns:4.4} secondary turns. Determine a) the primary and the secondary current, b) the number of primary turns and c) the maximum value of the flux."""

        primary_current = c.current( power.W / primary_voltage.V )
        secondary_current = c.current( power.W / secondary_voltage.V )
        
        primary_turns = (primary_voltage.V / secondary_voltage.V) * secondary_turns
        
        maxflux = c.magneticFlux( secondary_voltage.V / (  4.44 * frequency.Hz * secondary_turns  ) )
        
        self.answer = f"""{primary_current.A:4.4} A, {secondary_current.A:4.4} A, {primary_turns:4.4} turns, {maxflux.mWb:4.4} mWb"""
        
class johnbird_21_10:
    def __init__(self,*args,**kwargs): 
        
        primary_turns = int(ran.main(25))
        secondary_turns = int(ran.main(300))
        area = c.area(ran.main(300), 'cm2')
        primary_voltage = c.voltage(ran.main(250))
        
        self.question = f"""A single phase, 50 Hz transformer has {primary_turns} primary turns and {secondary_turns} secondary turns. The cross sectional area of the core is {area.cm2:4.4} cm2. When the primary winding is connected to a {primary_voltage.V:4.4} V supply, determine a) the maximum value of the flux density in the core and b) the voltage induced in the secondary winding."""

        flux = c.magneticFlux( (primary_voltage.V) / (  4.44 * 50 * primary_turns )   )
        
        fluxdensity = c.magneticFluxDensity(  (flux.Wb) / (area.m2) )
        
        secondary_voltage = c.voltage( primary_voltage.V * (secondary_turns / primary_turns))
        
        self.answer = f"""{fluxdensity.T:4.4} T, {secondary_voltage.kV:4.4} kV"""

class johnbird_21_11:
    def __init__(self,*args,**kwargs): 
        
        primary_voltage = c.voltage(int(ran.main(500)))
        secondary_voltage = c.voltage(int(ran.main(100)))
        fluxdensity = c.magneticFluxDensity(ran.main(1.5))
        area = c.area(ran.main(50), 'cm2')
        
        self.question = f"""A single phase {primary_voltage.V} V / {secondary_voltage.V} V, 50 Hz transformer has a maximum core flux density of {fluxdensity.T:4.4} T and an effective core cross-sectional area of {area.cm2:4.4} cm2. Determine the number of primary and secondary turns."""
        
        
        flux = c.magneticFlux(fluxdensity.T * area.m2)
        primary_turns = primary_voltage.V / (4.44 * 50 * flux.Wb )
        secondary_turns = secondary_voltage.V / (4.44 * 50 * flux.Wb)
        
        self.answer = f"""{int(primary_turns)} turns, {int(secondary_turns)} turns"""

class johnbird_21_12:
    def __init__(self,*args,**kwargs): 
        
        primary_voltage = c.voltage(int(ran.main(4500)))
        secondary_voltage = c.voltage(int(ran.main(225)))
        emfperturn = c.voltage(int(ran.main(15)))
        fluxdensity = c.magneticFluxDensity(ran.main(1.4))
        
        
        self.question = f"""A {primary_voltage.V} V / {secondary_voltage.V} V, 50 Hz single phase transformer is to have an approximate emf per turn of {emfperturn.V} V and operate with a maximum flux density of {fluxdensity.T:4.4} T. Calculate a) the number of primary and secondary turns and b) the cross sectional area of the core."""  
        
        primary_turns = primary_voltage.V / emfperturn.V
        secondary_turns = secondary_voltage.V / emfperturn.V
        flux = c.magneticFlux( (primary_voltage.V) / (4.44 * 50 * primary_turns) )
        area = c.area(flux.Wb / fluxdensity.T)
        
        self.answer = f"""{area.cm2:4.4} cm2"""
        
class johnbird_21_13:
    def __init__(self,*args,**kwargs): 
        
        primary_turns = int(ran.main(2000))
        secondary_turns = int(ran.main(800))
        noload_current = c.current(ran.main(5))
        powerfactor = ran.main(0.2)
        secondary_current = c.current(ran.main(100))
        powerfactor2 = powerfactor + ran.main(0.5)
        
        self.question = f"""A single-phase transformer has {primary_turns} turns on its primary and {secondary_turns} on its secondary. Its no-load current is {noload_current.A:4.4} A at a power factor of {powerfactor:4.4} lagging. Assuming the voltage drop in the windings is negligible, determine the primary current and power factor when the secondary curent is {secondary_current.A:4.4} A at a power factor of {powerfactor2:4.4} lagging."""

        primary_current = c.current((secondary_current.A * secondary_turns) / (primary_turns))
        
        theta2 = c.angle(math.acos(powerfactor2), 'rad')
        
        theta0 = c.angle(math.acos(powerfactor), 'rad')
        
        primary_current_x = c.current(noload_current.A * powerfactor + primary_current.A * powerfactor2)
        
        primary_current_y = c.current(noload_current.A * math.sin(theta0.rad) + primary_current.A * math.sin(theta2.rad))
        
        primary_current_loaded = c.current(math.sqrt(primary_current_x.A**2 + primary_current_y.A**2))
        
        theta1 = c.angle(math.atan(primary_current_y.A / primary_current_x.A), 'rad')
        
        powerfactor = math.cos(theta1.rad)
        
        self.answer = f"""{primary_current_loaded.A:4.4} A, {powerfactor:4.4} """

class johnbird_22_1:
    def __init__(self,*args,**kwargs): 
        poles = int(ran.main(4)) * 2
        conductors = int(ran.main(600))
        omega = c.angularVelocity(ran.main(625), 'revpermin')
        fluxperpole = c.magneticFlux(ran.main(20), 'mWb')
        config = 2
        
        self.question = f"""An {poles}-pole, wave-connected armature has {conductors} conductors and is driven at {omega.revpermin:4.4} rev/min. If the flux per pole is {fluxperpole.mWb:4.4} mWb, determine the generated e.m.f."""
        
        voltage = c.voltage(
        (2 * poles * fluxperpole.Wb * omega.revpers * conductors) / 
        (config)
        )
        
        self.answer = f"""{voltage.V:4.4} V"""
        
class johnbird_22_2:
    def __init__(self,*args,**kwargs): 
        
        polepairs = int(ran.main(2))
        poles = polepairs * 2
        config = 2 * polepairs
        slots = int(ran.main(50))
        conductorsperslot = int(ran.main(16))
        conductors = slots * conductorsperslot
        fluxperpole = c.magneticFlux(ran.main(30), 'mWb')
        emf = c.voltage(ran.main(240), 'V')
        
        
        
        self.question = f"""A {poles}-pole generator has a lap-wound armature with {slots} slots with {conductorsperslot} conductors per slot. The useful flux per pole is {fluxperpole.mWb:4.4}mWb. Determine the speed at which the machine must be driven to generate an e.m.f. of {emf.V:4.4}V."""
        
        speed = c.angularVelocity(
        emf.V / (fluxperpole.Wb * conductors), 'revpers'
        )
        
        self.answer = f"""{speed.revpers:4.4} rev/s or {speed.revpermin:4.4} rev/min"""
        
class johnbird_22_3:
    def __init__(self,*args,**kwargs): 
        
        polepairs = int(ran.main(4))
        poles = polepairs * 2
        conductors = int(ran.main(1200))
        fluxperpole = c.magneticFlux(ran.main(0.03), 'Wb')
        speed = c.angularVelocity(ran.main(500), 'revpermin')
        config = 2 * poles
        
        self.question = f"""An {poles}-pole, lap-wound armature has {conductors} conductors and a flux per pole of {fluxperpole.Wb:4.4} Wb. Determine the e.m.f. generated when running at {speed.revpermin:4.4} rev/min."""
        
        voltage = c.voltage(fluxperpole.Wb * speed.revpers * conductors)
        
        self.answer = f"""{voltage.V:4.4} V"""
        
class johnbird_22_4:
    def __init__(self,*args,**kwargs): 
        polepairs = int(ran.main(4))
        poles = polepairs * 2
        conductors = int(ran.main(1200))
        fluxperpole = c.magneticFlux(ran.main(0.03), 'Wb')
        speed = c.angularVelocity(ran.main(500), 'revpermin')
        config = 2
        
        self.question = f"""An {poles}-pole, wave-wound armature has {conductors} conductors and a flux per pole of {fluxperpole.Wb:4.4} Wb. Determine the e.m.f. generated when running at {speed.revpermin:4.4} rev/min."""
        
        voltage = c.voltage(poles * fluxperpole.Wb * speed.revpers * conductors)
        
        self.answer = f"""{voltage.V:4.4} V"""
        
class johnbird_22_5:
    def __init__(self,*args,**kwargs): 
        voltage = c.voltage(ran.main(150))
        fieldcurrentreduction = c.percentage(ran.main(20), 'percent')
        
        self.question = f"""A DC shunt wound generator running at a constant speed generates a voltage of {voltage.V:4.4} V at a certain value of field current. Determine the new generated voltage when the field current is reduced by {fieldcurrentreduction.percent:4.4} percent, assuming the flux is proportional to field current."""
        
        voltage2 = c.voltage( voltage.V *  (1 - fieldcurrentreduction.decimal))
        
        self.answer = f"""{voltage2.V:4.4} V"""
        
class johnbird_22_6:
    def __init__(self,*args,**kwargs): 
        
        speed = c.angularVelocity(ran.main(30), 'revpers')
        voltage= c.voltage(ran.main(200))
        voltage2 = c.voltage(voltage.V + ran.main(50))
        speed2 = c.angularVelocity(ran.main(20), 'revpers')
        
        
        self.question = f"""A DC generator running at {speed.revpers:4.4} rev/s generates an EMF of {voltage.V:4.4} V. Determine the percentage increase in the flux per pole required to generate {voltage2.V:4.4} V at {speed2.revpers:4.4} rev/s."""
        
        ratio = (speed.revpers * voltage2.V)/(speed2.revpers * voltage.V)
        percentageincrease = c.percentage( ratio - 1, 'decimal')
        
        self.answer = f"""{percentageincrease.percent:4.4} %."""
        
class johnbird_22_7:
    def __init__(self,*args,**kwargs): 
        
        emf = c.voltage(ran.main(200))
        armaturecurrent = c.current(ran.main(30))
        armatureresistance = c.resistance(ran.main(0.30))
        
        self.question = f"""Determine the terminal voltage of a generator which develops an EMF of {emf.V:4.4} V and has an armature current of {armaturecurrent.A:4.4} A on load. Assume the armature resistance is {armatureresistance.ohms:4.4} ohms"""
        
        terminalvoltage = c.voltage(emf.V - armaturecurrent.A * armatureresistance.ohms)
        
        self.answer = f"""{terminalvoltage.V:4.4} V"""
        
class johnbird_22_8:
    def __init__(self,*args,**kwargs): 
        
        load_resistance = c.resistance(ran.main(60))
        arm_current =  c.current(ran.main(8))
        arm_resistance = c.resistance(ran.main(1))
        
        
        self.question = f"""A generator is connected to a {load_resistance.ohm:4.4} ohms load and a current of {arm_current.A:4.4} A flows. If the armature resistance is {arm_resistance.ohm:4.4} ohm determine a) the terminal voltage and b) the generated emf."""
        
        term_voltage = c.voltage( arm_current.A * load_resistance.ohm )
        gen_emf = c.voltage( term_voltage.V + arm_current.A * arm_resistance.ohm)
        
        self.answer = f"""{term_voltage.V:4.4} V, {gen_emf.V:4.4} V"""

class johnbird_22_9:
    def __init__(self,*args,**kwargs): 
        
        
        emf1 = c.voltage(ran.main(150))
        speed1 = c.angularVelocity(ran.main(20), 'revpers')
        fluxperpole1 = c.magneticFlux(ran.main(0.10), 'Wb')
        
        speed2 = c.angularVelocity(speed1.revpers + ran.main(5), 'revpers')
        fluxperpole2 = c.magneticFlux(fluxperpole1.Wb)
        
        speed3 = c.angularVelocity(speed1.revpers, 'revpers')
        fluxperpole3 = c.magneticFlux(fluxperpole1.Wb - ran.main(0.02), 'Wb')
        
        speed4 = c.angularVelocity(speed1.revpers + ran.main(4), 'revpers')
        fluxperpole4 = c.magneticFlux(fluxperpole1.Wb - ran.main(0.03))
        
        
        self.question = f"""A separately excited generator develops a no - load emf of {emf1.V:4.4} V, at an armature speed of {speed1.revpers:4.4} rev/s and a flux per pole of {fluxperpole1.Wb:4.4} Wb. Determine the generated emf when a) the speed increases to {speed2.revpers:4.4} rev/s and the pole flux remains unchanged, b) the speed remains at {speed1.revpers:4.4} rev/s and the pole flux is decreased to {fluxperpole3.Wb:4.4} Wb, and c) the speed increases to {speed4.revpers:4.4} rev/s and the pole flux is decreased to {fluxperpole4.Wb:4.4} Wb."""
        
        emf2 = c.voltage( emf1.V * (speed2.revpers / speed1.revpers))
        
        emf3 = c.voltage( emf1.V * (fluxperpole3.Wb / fluxperpole1.Wb))
        
        emf4 = c.voltage( emf1.V * (fluxperpole4.Wb / fluxperpole1.Wb) * (speed4.revpers / speed1.revpers))
        
        self.answer = f"""{emf2.V:4.4} V, {emf3.V:4.4} V, {emf4.V:4.4} V"""

class johnbird_22_10():
    def __init__(self,*args,**kwargs): 
        
        power = c.power(ran.main(20000))
        load_voltage = c.voltage(ran.main(200))
        cable_resistance = c.resistance(ran.main(100), 'mohm')
        field_resistance = c.resistance(ran.main(50), 'ohm')
        arm_resistance = c.resistance(ran.main(40), 'mohm')
        
        self.question = f"""A shunt generator supplies a {power.kW:4.4} kW load at {load_voltage.V:4.4} V through cables of resistance, R = {cable_resistance.mohms:4.4} mohms. If the field winding resistance Rf = {field_resistance.ohms:4.4} ohms and the armature resistance, Ra = {arm_resistance.mohms:4.4} mohms, determine the a) terminal voltage and b) the emf generated in the armature."""

        load_current = c.current(power.W / load_voltage.V)
        cable_voltage = c.voltage(load_current.A * cable_resistance.ohms)
        terminal_voltage = c.voltage(load_voltage.V + cable_voltage.V)
        
        field_current = c.current(terminal_voltage.V / field_resistance.ohm)
        arm_current = c.current( field_current.A + load_current.A )
        
        generated_emf = c.voltage(terminal_voltage.V + arm_current.A * arm_resistance.ohm )
        
        self.answer = f"""{terminal_voltage.V:4.4} V, {generated_emf.V:4.4} V"""

class johnbird_22_11:
    def __init__(self,*args,**kwargs): 
        
        load_current = c.current(ran.main(80))
        load_voltage = c.voltage(ran.main(200))
        field_resistance = c.resistance(ran.main(40))
        series_resistance = c.resistance(ran.main(0.02))
        arm_resistance = c.resistance(ran.main(0.04))
        
        
        self.question = f"""A short shunt compound generator supplies {load_current.A:4.4} A at {load_voltage.V:4.4} V. If the field resistance, Rf = {field_resistance.ohm:4.4} ohms, the series resistance, Rse = {series_resistance.ohm:4.4} ohms, and the armature resistance, Ra = {arm_resistance.ohm:4.4} ohms, determine the emf generated."""
        
        
        field_voltage = c.voltage( load_voltage.V + series_resistance.ohm * load_current.A)
        arm_voltage = c.voltage( field_voltage.V )
        
        field_current = c.current( field_voltage.V / field_resistance.ohm)
        
        arm_current = c.current( load_current.A + field_current.A)
        
        generated_emf = c.voltage( field_voltage.V + arm_current.A * arm_resistance.ohm)
        
        self.answer = f"""{generated_emf.V:4.4} V"""
        
class johnbird_22_12:
    def __init__(self,*args,**kwargs): 
        
        power = c.power(ran.main(10000))
        arm_resistance = c.resistance(ran.main(0.75))
        field_resistance = c.resistance(ran.main(125))
        terminal_voltage = c.voltage(ran.main(250))
        ironfrictionwindageloss = c.power(ran.main(600))
        
        self.question = f"""A {power.kW:4.4} kW shunt generator having an armature circuit resistance of {arm_resistance.ohm:4.4} ohms and a field resistance of {field_resistance.ohm:4.4} ohms, generates a terminal voltage of {terminal_voltage.V:4.4} V at full load. Determine the efficiency of the generator at full load, assuming the iron, friction and windage losses amount to {ironfrictionwindageloss.W:4.4} W"""

        load_current = c.current( power.W / terminal_voltage.V )
        field_current = c.current( terminal_voltage.V / field_resistance.ohm )
        arm_current = c.current( field_current.A + load_current.A )
        
        efficiency = c.percentage(power.W / ( power.W + arm_current.A**2 * arm_resistance.ohm + field_current.A*terminal_voltage.V + ironfrictionwindageloss.W ), 'decimal' )
        
        self.answer = f"""{efficiency.percent:4.4} %"""
        
class johnbird_22_13:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(240))
        arm_resistance = c.resistance(ran.main(0.2))
        arm_current = c.current(ran.main(50))
        
        self.question = f"""A dc motor operates from a {supply_voltage.V:4.4} V. The armature resistance is {arm_resistance.ohm:4.4} ohm. Determine the back emf when the armature current is {arm_current.A:4.4} A."""
        
        emf = c.voltage(supply_voltage.V - arm_current.A * arm_resistance.ohm)
        
        self.answer = f"""{emf.V:4.4} V"""
        
class johnbird_22_14:
    def __init__(self,*args,**kwargs): 
        
        arm_resistance = c.resistance( ran.main(0.25))
        supply_voltage = c.voltage( ran.main(300))
        generator_current = c.current(ran.main(100))
        motor_current = c.current(ran.main(80))
        
        self.question = f"""The armature of a DC machine has a resistance of {arm_resistance.ohm:4.4} ohm and is connected to a {supply_voltage.V:4.4} V supply. Calculate the emf generated when it is running a) as a generator giving {generator_current.A:4.4} A, and b) as a motor taking {motor_current.A:4.4} A"""
        
        emf_generator = c.voltage( supply_voltage.V + generator_current.A * arm_resistance.ohm )
        
        emf_motor = c.voltage( supply_voltage.V - motor_current.A * arm_resistance.ohm )
        
        self.answer = f"""{emf_generator.V:4.4} V, {emf_motor.V:4.4} V"""

class johnbird_22_15:
    def __init__(self,*args,**kwargs): 
        
        polepairs = int(ran.main(4))
        poles = polepairs * 2
        conductors = int(ran.main(900))
        fluxperpole = c.magneticFlux(ran.main(25), 'mWb')
        arm_current = c.current(ran.main(30))
        config = 2
        
        self.question = f"""An {poles}-pole dc motor has a wave-wound armature with {conductors} conductors. The useful flux per pole is {fluxperpole.mWb:4.4} mWb. Determine the torque exerted when a current of {arm_current.A:4.4} A flows in each armature conductor"""
        
        torque = c.torque( 
        (polepairs * fluxperpole.Wb * conductors * arm_current.A) / 
        ( math.pi * config )
        )
        
        self.answer = f"""{torque.Nm:4.4} Nm"""
        
class johnbird_22_16:
    def __init__(self,*args,**kwargs): 
        
        
        supply_voltage = c.voltage(ran.main(350))
        arm_resistance = c.resistance(ran.main(0.5))
        speed = c.angularVelocity(ran.main(15), 'revpers')
        arm_current = c.current(ran.main(60))
        
        self.question = f"""Determine the torque developed by a {supply_voltage.V:4.4} V dc motor having an armature resistance of {arm_resistance.ohms:4.4} ohms and running at {speed.revpers:4.4} rev/s. The armature current is {arm_current.A:4.4} A."""
        
        emf = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm)
        
        torque = c.torque( (emf.V * arm_current.A) / (2*math.pi*speed.revpers) )
        
        self.answer = f"""{torque.Nm:4.4} Nm"""
        
class johnbird_22_17:
    def __init__(self,*args,**kwargs): 
        
        polepairs = int(ran.main(3))
        poles = 2* polepairs
        supply_voltage = c.voltage(ran.main(250))
        conductors = int(ran.main(500))
        arm_resistance = c.resistance(ran.main(1))
        fluxperpole = c.magneticFlux(ran.main(20), 'mWb')
        arm_current = c.current(ran.main(40))
        config = 2 * polepairs
        
        self.question = f"""A {poles} - pole lapwound motor is connected to a {supply_voltage.V:4.4} V supply. The armature has {conductors} conductors and a resistance of {arm_resistance.ohm:4.4} ohm. The flux per pole is {fluxperpole.mWb:4.4} mWb. Calculate a) the speed and b) the torque developed when the armature current is {arm_current.A:4.4} A."""
        
        
        emf = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm)
        
        speed = c.angularVelocity( (emf.V) / (conductors * fluxperpole.Wb), 'revpers' )
        
        torque = c.torque( (emf.V * arm_current.A) / (2*math.pi*speed.revpers) )
        
        self.answer = f"""{speed.revpers:4.4} rev/s, {torque.Nm:4.4} Nm"""
        
class johnbird_22_18:
    def __init__(self,*args,**kwargs): 
        
        voltage = c.voltage(ran.main(100))
        torque = c.torque(ran.main(25))
        arm_current = c.current(ran.main(16))
        percentreduction = c.percentage(ran.main(15), 'percent')
        torque2 = c.torque(torque.Nm + ran.main(10))
        
        
        self.question = f"""The shaft torque of a diesel motor driving a {voltage.V:4.4} V dc shunt wound generator is {torque.Nm:4.4} Nm. The armature current of the generator is {arm_current.A:4.4} A at this value of torque. If the shunt field regulator is adjusted so that the flux is reduced by {percentreduction.percent:4.4} percent, the torque increases to {torque2.Nm:4.4} Nm. Determine the armature current at this new value of torque."""
        
        arm_current2 = c.current( (arm_current.A * torque2.Nm) / ((1 - percentreduction.decimal) * torque.Nm)  )
        
        self.answer = f"""{arm_current2.A:4.4} A"""
        
class johnbird_22_19:
    def __init__(self,*args,**kwargs): 
        
        
        load_voltage = c.voltage(ran.main(100))
        load_current = c.current(ran.main(15))
        speed = c.angularVelocity(ran.main(1500), 'revpermin')
        torque = c.torque(ran.main(12))
        
        
        self.question = f"""A {load_voltage.V:4.4} V dc generator supplies a current of {load_current.A:4.4} A when running at {speed.revpermin:4.4} rev/min. If the torque on the shaft driving the generator is {torque.Nm:4.4} Nm, determine a) the efficiency of the generator and b) the power loss in the generator."""
        
        efficiency = c.percentage( (load_voltage.V * load_current.A) / (torque.Nm * math.pi * 2 * speed.revpers), 'decimal')
        
        losses = c.power( torque.Nm * math.pi * 2 * speed.revpers - load_voltage.V * load_current.A )
        
        self.answer = f"""{efficiency.percent:4.4} %, {losses.W:4.4} W"""

class johnbird_22_20:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(240))
        supply_current = c.current(ran.main(30))
        field_resistance = c.resistance(ran.main(150))
        arm_resistance = c.resistance(ran.main(0.4))
        
        
        self.question = f"""A {supply_voltage.V:4.4} V shunt motor takes a total current of {supply_current.A:4.4} A. If the field winding resistance Rf = {field_resistance.ohm:4.4} ohms and the armature resistance Ra = {arm_resistance.ohm:4.4} ohms, determine a) the current in the armature and b) the back emf."""
        
        field_current = c.current( supply_voltage.V / field_resistance.ohm )
        arm_current = c.current( supply_current.A - field_current.A )
        
        back_emf = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm )
        
        self.answer = f"""{arm_current.A:4.4} A, {back_emf.V:4.4} V"""

class johnbird_22_21:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage( ran.main(200) )
        arm_resistance = c.resistance(ran.main(0.4))
        arm_current = c.current(ran.main(30))
        speed = c.angularVelocity(ran.main(1350), 'revpermin')
        arm_current2 = c.current(arm_current.A + ran.main(15))
        
        
        
        self.question = f"""A {supply_voltage.V:4.4} V dc shunt wound motor has an armature resistance of {arm_resistance.ohm:4.4} ohm and at a certain load has an armature current of {arm_current.A:4.4} A and runs at {speed.revpermin:4.4} rev/min. If the load on the shaft of the motor is increased so that the armature current increases to {arm_current2.A:4.4} A, determine the speed of the motor, assuming the flux remains constant."""
        
        emf = c.voltage(supply_voltage.V - arm_current.A * arm_resistance.ohm)
        emf2 = c.voltage(supply_voltage.V - arm_current2.A * arm_resistance.ohm)
        
        speed2 = c.angularVelocity(
        (speed.revpermin * emf2.V)/(emf.V), 'revpermin'
        )
        
        self.answer = f"""{speed2.revpermin:4.4} rev/min"""
        
class johnbird_22_22:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage( ran.main(220) )
        speed = c.angularVelocity( ran.main(800), 'revpermin' )
        arm_current = c.current( ran.main(30))
        arm_resistance = c.resistance( ran.main(0.4))
        fluxreduction = c.percentage(  ran.main(10), 'percent')
        
        self.question = f"""A {supply_voltage.V:4.4} V dc shunt-wound motor runs at {speed.revpermin:4.4} rev/min and the armature current is {arm_current.A:4.4} A. The armature circuit resistance is {arm_resistance.ohm:4.4} ohms. Determine a) the maximum value of armature current if the flux is suddenly reduced by {fluxreduction.percent:4.4} percent and b) the steady state value of the armature current at the new value of flux, assuming the shaft torque of the motor remains constant."""
        
        emf_initial = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm )
        
        emf_transient  = c.voltage( emf_initial.V * (1 - fluxreduction.decimal) )
        #print(f"""EMF initial = {emf_initial.V:4.4}""")
        #print(f"""EMF transient = {emf_transient.V:4.4}""")
        arm_voltage_transient = c.voltage( supply_voltage.V - emf_transient.V )
        arm_current_transient = c.current( arm_voltage_transient.V / arm_resistance.ohm)
        
        arm_current2 = c.current( arm_current.A  / (1 - fluxreduction.decimal) )
        
        self.answer = f"""{arm_current_transient.A:4.4} A, {arm_current2.A:4.4} A"""

class johnbird_22_23:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(240))
        arm_resistance = c.resistance(ran.main(0.2))
        field_resistance = c.resistance(ran.main(0.3))
        speed = c.angularVelocity(ran.main(24), 'revpers')
        arm_current = c.current(ran.main(15))
        arm_current2 = c.current(arm_current.A + ran.main(15))
        
        
        self.question = f"""A series motor has an armature resistance of {arm_resistance.ohm:4.4} ohms and a series field resistance of {field_resistance.ohm:4.4} ohms. It is connected to a {supply_voltage.V:4.4} V supply and at a particaular load runs at {speed.revpers:4.4} rev/s when drawing {arm_current.A:4.4} A from the supply. a) Determine the generated emf at this load. b) Calculate the speed of the motor when the load is changed such that the current is increased to {arm_current2.A:4.4} A. Assume that this causes a doubling of the flux."""
        
        emf = c.voltage( supply_voltage.V - arm_current.A * (arm_resistance.ohm + field_resistance.ohm) )
        
        emf2 = c.voltage( supply_voltage.V - arm_current2.A * (arm_resistance.ohm + field_resistance.ohm) )
        
        speed2 = c.angularVelocity( (speed.revpers * emf2.V) / (2 * emf.V), 'revpers' )
        
        self.answer = f"""{emf.V:4.4} V, {speed2.revpers:4.4} rev/s"""

class johnbird_22_24:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(320))
        supply_current = c.current(ran.main(80))
        speed = c.angularVelocity(ran.main(1000), 'revpermin')
        losses = c.power(ran.main(1500),'W')
        field_resistance = c.resistance(ran.main(40))
        arm_resistance = c.resistance(ran.main(0.2))
        
        self.question = f"""A {supply_voltage.V:4.4} V shunt motor takes a total current of {supply_current.A:4.4} A and runs at {speed.revpermin:4.4} rev/min. If the iron, friction, and windage losses amount to {losses.kW:4.4} kW, the shunt field resistance is {field_resistance.ohm:4.4} ohms and the armature resistance is {arm_resistance.ohm:4.4} ohms, determine the overall efficiency of the motor."""
        
        field_current = c.current(supply_voltage.V / field_resistance.ohm)
        arm_current = c.current(supply_current.A - field_current.A)
        efficiency = c.percentage( (supply_voltage.V * supply_current.A - arm_current.A**2 * arm_resistance.ohm - field_current.A * supply_voltage.V - losses.W)/(supply_voltage.V * supply_current.A), 'decimal')
        
        self.answer = f"""{efficiency.percent:4.4} %"""
        
class johnbird_22_25:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(250))
        supply_current = c.current(ran.main(40))
        arm_resistance = c.resistance(ran.main(0.15))
        field_resistance = c.resistance(ran.main(0.05))
        
        
        self.question = f"""A {supply_voltage.V:4.4} V series motor draws a current of {supply_current.A:4.4} A. The armature resistance is {arm_resistance.ohm:4.4} ohms and the field resistance is {field_resistance.ohm:4.4} ohms. Determine the maximum efficiency of the motor."""
        
        efficiency = c.percentage((supply_voltage.V * supply_current.A - 2 * supply_current.A**2 *(arm_resistance.ohm + field_resistance.ohm) )/(supply_voltage.V * supply_current.A), 'decimal')
        
        self.answer = f"""{efficiency.percent:4.4} %"""
        
class johnbird_22_26:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(200))
        torque = c.torque(ran.main(15))
        speed = c.angularVelocity(ran.main(1200), 'revpermin')
        efficiency = c.percentage(100 - ran.main(20), 'percent')
        
        
        self.question = f"""A {supply_voltage.V:4.4} V dc motor develops a shaft torque of {torque.Nm:4.4} Nm at {speed.revpermin:4.4} rev/min. If the efficiency is {efficiency.percent:4.4} percent, determine the current supplied to the motor."""
        
        current = c.current((torque.Nm * math.pi * 2 * speed.revpers)/(supply_voltage.V * efficiency.decimal))
        
        self.answer = f"""{current.A:4.4} A"""
        
class johnbird_22_27:
    def __init__(self,*args,**kwargs): 
        
        speed = c.angularVelocity(ran.main(30), 'revpers')
        supply_current = c.current(ran.main(10))
        supply_voltage = c.voltage(ran.main(400))
        total_resistance = c.resistance(ran.main(2))
        losses = c.power(ran.main(300))
        
        
        self.question = f"""A dc series motor drives a load at {speed.revpers:4.4} rev/s and takes a current of {supply_current.A:4.4} A when the supply voltage is {supply_voltage.V:4.4} V. If the total resistance of the motor is {total_resistance.ohm:4.4} ohms and the iron, friction, and windage losses amount to {losses.W:4.4} W, determine the efficiency of the motor."""
        
        efficiency = c.percentage( (supply_voltage.V * supply_current.A - supply_current.A**2 * total_resistance.ohm - losses.W) / (supply_voltage.V * supply_current.A) , 'decimal'  )
        
        self.answer = f"""{efficiency.percent:4.4} percent"""
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        