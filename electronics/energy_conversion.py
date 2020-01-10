from generator import random_handler as ran
from generator import constants_conversions as c

import sympy as sym
# from sympy import init_printing
import math
import random
# import algebra
# import analytic_geometry

# import randomizer_2 as ran2

x, y, z = sym.symbols('x y z', real = True)#generic variables
            

class johnbird_4_1:
    def __init__(self,*args,**kwargs): 
        
        cells = ran.main(8, 'int')
        cell_resistance = c.resistance(ran.main(0.2))
        cell_voltage = c.voltage(ran.main(2.2))
        
        
        self.question = f"""For {cells} cells, each with an internal resistance of {cell_resistance.ohm} ohms and an emf of {cell_voltage.V} V are connected to a) in series b) in parallel. Determine the emf and the internal resistance of the batteries so formed."""

        bat_emf_series = c.voltage( cells * cell_voltage.V)
        bat_resistance_series = c.resistance( cells * cell_resistance.ohm)


        bat_emf_parallel = c.voltage( cell_voltage.V )
        bat_resistance_parallel = c.resistance( cell_resistance.ohm / cells)
        
        self.answer = f"""Series = {bat_emf_series.V} V , {bat_resistance_series.ohm} ohms
Parallel = {bat_emf_parallel.V} V, {bat_resistance_parallel.ohm} ohms"""

class johnbird_4_2:
    def __init__(self,*args,**kwargs): 
        
        cell_resistance = c.resistance(ran.main(0.02))
        cell_voltage = c.voltage(ran.main(2.0))
        cell_current = c.current(ran.main(5))
        cell_current2 = c.current(ran.main(50))
        
        self.question = f"""A cell has an internal resistance of {cell_resistance.ohm} ohms and an emf of {cell_voltage.V} V. Calculate its terminal potential difference if it delivers a) {cell_current.A} A and b) {cell_current2.A} A"""
        
        terminal_voltage = c.voltage( cell_voltage.V -  cell_current.A * cell_resistance.ohm)
        terminal_voltage2 = c.voltage( cell_voltage.V -  cell_current2.A * cell_resistance.ohm)
        
        self.answer = f"""Terminal Voltage at {cell_current.A} A = {terminal_voltage.V} V
Terminal voltage at {cell_current2.A} A = {terminal_voltage2.V} V"""

class johnbird_4_3:
    def __init__(self,*args,**kwargs): 
        
        bat_voltage = c.voltage(ran.main(25))
        bat_voltage_loaded = c.voltage(bat_voltage.V - ran.main(1))
        bat_current = c.current(ran.main(10))
        
        
        self.question = f"""The potential difference at the terminals of a battery is {bat_voltage.V} V when no load is connected and {bat_voltage_loaded.V} V when a load taking {bat_current.A} A is connected. Determine the internal resistance of the battery"""
        
        bat_resistance = c.resistance( (bat_voltage.V - bat_voltage_loaded.V ) / (bat_current.A))
        
        self.answer = f"""Battery internal resistance = {bat_resistance.ohm} ohms"""
        
class johnbird_4_4:
    def __init__(self,*args,**kwargs): 
        
        cells = ran.main(10, 'int')
        cell_voltage = c.voltage(ran.main(1.5))
        cell_resistance = c.resistance(ran.main(0.2))
        load_resistance = c.resistance(ran.main(58))
        
        
        self.question = f"""For {cells} {cell_voltage.V} V cells, each having an internal resistance of {cell_resistance.ohm} ohms, are connected in series to a load of {load_resistance.ohm} ohms. Determine a) the current flowing in the circuit and b) the potential difference at the battery terminals."""
        
        bat_voltage = c.voltage( cell_voltage.V * cells)
        bat_resistance = c.resistance( cell_resistance.ohm * cells)
        load_current = c.current(  (bat_voltage.V) / (load_resistance.ohm + bat_resistance.ohm)  )
        
        bat_voltage_loaded = c.voltage( bat_voltage.V - load_current.A * bat_resistance.ohm )
        
        self.answer = f"""Current in the circuit = {load_current.A} A
Potential difference at the battery terminals = {bat_voltage_loaded.V} V"""

class johnbird_21_1:
    def __init__(self,*args,**kwargs): 
        
        n1 = ran.main(500, 'int')
        n2 = ran.main(3000, 'int')
        v1 = c.voltage(ran.main(240, 'int'))
        
        self.question = f"""A transformer has {n1} primary turns and {n2} secondary turns. If the primary voltage is {v1.V}V, determine the secondary voltage, assuming an ideal transformer."""
        
        v2 = c.voltage(( v1.V * n2) / n1)

        self.answer = f"""The secondary voltage is {v2.V} V"""
        
class johnbird_21_2:
    def __init__(self,*args,**kwargs): 
        
        n1 = ran.main(2,'int')
        n2 = ran.main(7,'int')
        v1 = c.voltage(ran.main(240,'int'))
        
        self.question = f"""An ideal transformer with a turns ratio of {n1}:{n2} is fed from a {v1.V}V supply. Determine its output voltage."""
        
        v2 = c.voltage((v1.V * n2)/ n1)
        
        self.answer = f"""Output voltage = {v2.V} V"""
        
class johnbird_21_3:
    def __init__(self,*args,**kwargs): 
        np = ran.main(8, 'int')
        ns = 1
        ip = c.current(ran.main(3, 'int'))
        vp = c.voltage(ran.main(240, 'int'))
        
        self.question = f"""An ideal transformer has a turns ratio of {np}:{ns} and the primary current is {ip.A} A when it is supplied by {vp.V} V. Calculate the secondary voltage."""
        
        a = np / ns
        vs = c.voltage( (vp.V * ns) / np )
        isec = c.current(ip.A * np / ns)
        
        self.answer = f"""Secondary Voltage = {vs.V} V
Secondary Current = {isec.A} A"""

class johnbird_21_4:
    def __init__(self,*args,**kwargs): 
        vmains = c.voltage(ran.main(240, 'int'))
        vload = c.voltage(ran.main(12, 'int'))
        pload = c.power(ran.main(150, 'int'), 'W')
        
        self.question = f"""An ideal transformer, connected to a {vmains.V} V mains, supplies a {vload.V}V, {pload.W} W lamp. Calculate the transformer turns ratio and the current taken from the supply."""
        
        ratio = vmains.V  / vload.V
        
        iload = c.current(pload.W / vload.V)
        imains = c.current(iload.A * vload.V / vmains.V)

        self.answer = f"""Turns ratio = {ratio}
Current taken from supply = {imains.A} A"""

class johnbird_21_5:
    def __init__(self,*args,**kwargs): 
        resistance = c.resistance(ran.main(12, 'int'))
        voltage_sec = c.voltage(ran.main(120, 'int'))
        current_prim = c.current(ran.main(4, 'int'))
        
        
        self.question = f"""A {resistance.ohm} ohms resistor is connected across the secondary winding of an ideal transformer whose secondary voltage is {voltage_sec.V} V. Determine the primary voltage if the supply current is {current_prim.A}."""
        
        current_sec = c.current(voltage_sec.V / resistance.ohms)
        voltage_prim = c.voltage( voltage_sec.V * current_prim.A / current_sec.A)
        
        self.answer = f"""Primary Voltage = {voltage_prim.V} V"""

class johnbird_21_6:
    def __init__(self,*args,**kwargs): 
        
        power  = c.power(ran.main(5, 'int'), 'kVA')
        turns_primary = ran.main(10, 'int')
        turns_secondary = 1
        voltage_primary = c.voltage(ran.main(2500), 'V')
        
            
        self.question = f"""A {power.kVA} kVA single-phase transformer has a turns ratio of {turns_primary}:{turns_secondary} and is fed from a {voltage_primary.kV} kV supply. Neglecting losses, determine (a) the full-load secondary current, (b) the minimum load resistance which can be connected across the secondary winding to give full load kVA, (c) the primary current at full load kVA."""
            
        voltage_secondary = c.voltage( voltage_primary.V * turns_secondary / turns_primary)
        
        current_secondary = c.current( power.VA / voltage_primary.V  )
        
        resistance_minimum = c.resistance( voltage_primary.V / voltage_secondary.V )
        
        current_primary = c.current( current_secondary.A * turns_secondary / turns_primary  )
        
        self.answer = f"""Full-load secondary current = {current_secondary.A} A
Minimum load resistance = {resistance_minimum.ohm} ohms
Primary current at full-load = {current_primary.A} A"""

####################################################################3
# added June 11 2019

class johnbird_21_7:
    def __init__(self,*args,**kwargs): 
        
        primary_voltage = c.voltage(ran.main(24, 'int')*100)
        secondary_voltage = c.voltage(ran.main(4, 'int')*100)
        noload_current = c.current(ran.main(0.5))
        core_power = c.power(ran.main(4,'int')*100)
        
        
        self.question = f"""A {primary_voltage.V} V / {secondary_voltage.V} V single phase transformer takes a no-load current of {noload_current.A} A and the core loss is {core_power.W} W. Determine the values of the magnetising and the core loss components of the no-load current."""
        
        phase_angle = c.angle(math.acos(  (secondary_voltage.V) / (primary_voltage.V * noload_current.A)  ), 'rad')
        
        magnetizing_current = c.current( noload_current.A * math.sin(phase_angle.rad) )
        
        coreloss_current = c.current( noload_current.A * math.cos(phase_angle.rad))
        
        self.answer = f"""Magnetizing Component = {magnetizing_current.A} A
Coreloss Component = {coreloss_current.A} A"""

class johnbird_21_8:
    def __init__(self,*args,**kwargs): 
        
        noload_current = c.current( ran.main(0.8))
        primary_voltage = c.voltage(ran.main(240))
        power = c.power(ran.main(72))
        
        self.question = f"""A transformer takes a current of {noload_current.A} A when its primary is connected to a {primary_voltage.V} volt, 50 Hz supply, the secondary being on open circuit. If the power absorbed is {power.W} watts, determine a) the iron loss current, b) the power factor on no-load, and c) the magnetizing current."""
        
        coreloss_current = c.current( power.W / primary_voltage.V )
        
        powerfactor = c.percentage(coreloss_current.A / noload_current.A, 'decimal')
        
        magnetizing_current = c.current(  math.sqrt(noload_current.A**2 - coreloss_current.A**2) )
        
        self.answer = f"""Iron loss current = {coreloss_current.A} A
Power factor on no-load = {powerfactor.decimal} 
Magnetizing Current = {magnetizing_current.A} A"""


class johnbird_21_9:
    def __init__(self,*args,**kwargs): 
        
        frequency = c.frequency(50, 'Hz')
        primary_voltage = c.voltage( ran.main(4000))
        secondary_voltage = c.voltage( ran.main(200))
        secondary_turns = ran.main(100)
        power = c.power(100, 'kVA')
        
        
        self.question = f"""A {power.kVA} kVA, {primary_voltage.V} V / {secondary_voltage.V} V, 50 Hz, single-phase transformer has {secondary_turns} secondary turns. Determine a) the primary and the secondary current, b) the number of primary turns and c) the maximum value of the flux."""

        primary_current = c.current( power.W / primary_voltage.V )
        secondary_current = c.current( power.W / secondary_voltage.V )
        
        primary_turns = (primary_voltage.V / secondary_voltage.V) * secondary_turns
        
        maxflux = c.magneticFlux( secondary_voltage.V / (  4.44 * frequency.Hz * secondary_turns  ) )
        
        self.answer = f"""Primary Current = {primary_current.A} A
Secondary Current = {secondary_current.A} A
Primary Turns = {primary_turns} turns
Maximum Value of the Flux = {maxflux.mWb} mWb"""
        
class johnbird_21_10:
    def __init__(self,*args,**kwargs): 
        
        primary_turns = ran.main(25, 'int')
        secondary_turns = ran.main(300, 'int')
        area = c.area(ran.main(300), 'cm2')
        primary_voltage = c.voltage(ran.main(250))
        
        self.question = f"""A single phase, 50 Hz transformer has {primary_turns} primary turns and {secondary_turns} secondary turns. The cross sectional area of the core is {area.cm2} cm2. When the primary winding is connected to a {primary_voltage.V} V supply, determine a) the maximum value of the flux density in the core and b) the voltage induced in the secondary winding."""

        flux = c.magneticFlux( (primary_voltage.V) / (  4.44 * 50 * primary_turns )   )
        
        fluxdensity = c.magneticFluxDensity(  (flux.Wb) / (area.m2) )
        
        secondary_voltage = c.voltage( primary_voltage.V * (secondary_turns / primary_turns))
        
        self.answer = f"""Maximum Flux Density = {fluxdensity.T} T
Voltage at the secondary winding = {secondary_voltage.kV} kV"""

class johnbird_21_11:
    def __init__(self,*args,**kwargs): 
        
        primary_voltage = c.voltage(ran.main(500, 'int'))
        secondary_voltage = c.voltage(ran.main(100, 'int'))
        fluxdensity = c.magneticFluxDensity(ran.main(1.5))
        area = c.area(ran.main(50), 'cm2')
        
        self.question = f"""A single phase {primary_voltage.V} V / {secondary_voltage.V} V, 50 Hz transformer has a maximum core flux density of {fluxdensity.T} T and an effective core cross-sectional area of {area.cm2} cm2. Determine the number of primary and secondary turns."""
        
        
        flux = c.magneticFlux(fluxdensity.T * area.m2)
        primary_turns = primary_voltage.V / (4.44 * 50 * flux.Wb )
        secondary_turns = secondary_voltage.V / (4.44 * 50 * flux.Wb)
        
        self.answer = f"""Primary turns = {primary_turns}
Secondary turns = {secondary_turns}"""

class johnbird_21_12:
    def __init__(self,*args,**kwargs): 
        
        primary_voltage = c.voltage(ran.main(4500, 'int'))
        secondary_voltage = c.voltage(ran.main(225, 'int'))
        emfperturn = c.voltage(ran.main(15, 'int'))
        fluxdensity = c.magneticFluxDensity(ran.main(1.4))
        
        
        self.question = f"""A {primary_voltage.V} V / {secondary_voltage.V} V, 50 Hz single phase transformer is to have an approximate emf per turn of {emfperturn.V} V and operate with a maximum flux of {fluxdensity.T} T. Calculate a) the number of primary and secondary turns and b) the cross sectional area of the core."""  
        
        primary_turns = primary_voltage.V / emfperturn.V
        secondary_turns = secondary_voltage.V / emfperturn.V
        flux = c.magneticFlux( (primary_voltage.V) / (4.44 * 50 * primary_turns) )
        area = c.area(flux.Wb / fluxdensity.T)
        
        self.answer = f"""Area = {area.cm2} cm2"""
        
class johnbird_21_13:
    def __init__(self,*args,**kwargs): 
        
        primary_turns = ran.main(2000, 'int')
        secondary_turns = ran.main(800, 'int')
        noload_current = c.current(ran.main(5))
        powerfactor = ran.main(0.2)
        secondary_current = c.current(ran.main(100))
        powerfactor2 = powerfactor + ran.main(0.5)
        
        self.question = f"""A single-phase transformer has {primary_turns} turns on its primary and {secondary_turns} on its secondary. Its no-load current is {noload_current.A} A at a power factor of {powerfactor} lagging. Assuming the voltage drop in the windings is negligible, determine the primary current and power factor when the secondary curent is {secondary_current.A} A at a power factor of {powerfactor2} lagging."""

        primary_current = c.current((secondary_current.A * secondary_turns) / (primary_turns))
        
        theta2 = c.angle(math.acos(powerfactor2), 'rad')
        
        theta0 = c.angle(math.acos(powerfactor), 'rad')
        
        primary_current_x = c.current(noload_current.A * powerfactor + primary_current.A * powerfactor2)
        
        primary_current_y = c.current(noload_current.A * math.sin(theta0.rad) + primary_current.A * math.sin(theta2.rad))
        
        primary_current_loaded = c.current(math.sqrt(primary_current_x.A**2 + primary_current_y.A**2))
        
        theta1 = c.angle(math.atan(primary_current_y.A / primary_current_x.A), 'rad')
        
        powerfactor = math.cos(theta1.rad)
        
        self.answer = f"""Magnitude of the primary current = {primary_current_loaded.A} A
Power Factor = {powerfactor} """

class johnbird_22_1:
    def __init__(self,*args,**kwargs): 
        poles = ran.main(4, 'int') * 2
        conductors = ran.main(600, 'int')
        omega = c.angularVelocity(ran.main(625), 'revpermin')
        fluxperpole = c.magneticFlux(ran.main(20), 'mWb')
        config = 2
        
        self.question = f"""An {poles}-pole, wave-connected armature has {conductors} conductors and is driven at {omega.revpermin} rev/min. If the flux per pole is {fluxperpole.mWb} mWb, determine the generated e.m.f."""
        
        voltage = c.voltage(
        (2 * poles * fluxperpole.Wb * omega.revpers * conductors) / 
        (config)
        )
        
        self.answer = f"""Generated EMF = {voltage.V} V"""
        
class johnbird_22_2:
    def __init__(self,*args,**kwargs): 
        
        polepairs = ran.main(2, 'int')
        poles = polepairs * 2
        config = 2 * polepairs
        slots = ran.main(50, 'int')
        conductorsperslot = ran.main(16, 'int')
        conductors = slots * conductorsperslot
        fluxperpole = c.magneticFlux(ran.main(30), 'mWb')
        emf = c.voltage(ran.main(240), 'V')
        
        
        
        self.question = f"""A {poles}-pole generator has a lap-wound armature with {slots} slots with {conductorsperslot} conductors per slot. The useful flux per pole is {fluxperpole.mWb}mWb. Determine the speed at which the machine must be driven to generate an e.m.f. of {emf.V}V."""
        
        speed = c.angularVelocity(
        emf.V / (fluxperpole.Wb * conductors), 'revpers'
        )
        
        self.answer = f"""Speed = {speed.revpers} rev/s or {speed.revpermin} rev/min"""
        
class johnbird_22_3:
    def __init__(self,*args,**kwargs): 
        
        polepairs = ran.main(4, 'int')
        poles = polepairs * 2
        conductors = ran.main(1200, 'int')
        fluxperpole = c.magneticFlux(ran.main(0.03), 'Wb')
        speed = c.angularVelocity(ran.main(500), 'revpermin')
        config = 2 * poles
        
        self.question = f"""An {poles}-pole, lap-wound armature has {conductors} conductors and a flux per pole of {fluxperpole.Wb} Wb. Determine the e.m.f. generated when running at {speed.revpermin} rev/min."""
        
        voltage = c.voltage(fluxperpole.Wb * speed.revpers * conductors)
        
        self.answer = f"""Generated EMF = {voltage.V} V"""
        
class johnbird_22_4:
    def __init__(self,*args,**kwargs): 
        polepairs = ran.main(4, 'int')
        poles = polepairs * 2
        conductors = ran.main(1200, 'int')
        fluxperpole = c.magneticFlux(ran.main(0.03), 'Wb')
        speed = c.angularVelocity(ran.main(500), 'revpermin')
        config = 2
        
        self.question = f"""An {poles}-pole, wave-wound armature has {conductors} conductors and a flux per pole of {fluxperpole.Wb} Wb. Determine the e.m.f. generated when running at {speed.revpermin} rev/min."""
        
        voltage = c.voltage(poles * fluxperpole.Wb * speed.revpers * conductors)
        
        self.answer = f"""Generated EMF = {voltage.V} V"""
        
class johnbird_22_5:
    def __init__(self,*args,**kwargs): 
        voltage = c.voltage(ran.main(150))
        fieldcurrentreduction = c.percentage(ran.main(20), 'percent')
        
        self.question = f"""A DC shunt wound generator running at a constant speed generates a voltage of {voltage.V} V at a certain value of field current. Determine the change in the generated voltage when the field current is reduced by {fieldcurrentreduction.percent} percent, assuming the flux is proportional to field current."""
        
        voltage2 = c.voltage( voltage.V *  (1 - fieldcurrentreduction.decimal))
        
        self.answer = f"""A reduction of {fieldcurrentreduction.percent} percent in the value of the flux reduces the generated voltage to {voltage2.V} V at constant speed"""
        
class johnbird_22_6:
    def __init__(self,*args,**kwargs): 
        
        speed = c.angularVelocity(ran.main(30), 'revpers')
        voltage= c.voltage(ran.main(200))
        voltage2 = c.voltage(voltage.V + ran.main(50))
        speed2 = c.angularVelocity(ran.main(20), 'revpers')
        
        
        self.question = f"""A DC generator running at {speed.revpers} rev/s generates an EMF of {voltage.V} V. Determine the percentage increase in the flux per pole required to generate {voltage2.V} V at {speed2.revpers} rev/s."""
        
        ratio = (speed.revpers * voltage2.V)/(speed2.revpers * voltage.V)
        percentageincrease = c.percentage( ratio - 1, 'decimal')
        
        self.answer = f"""Increase in flux per pole = {percentageincrease.percent} percent."""
        
class johnbird_22_7:
    def __init__(self,*args,**kwargs): 
        
        emf = c.voltage(ran.main(200))
        armaturecurrent = c.current(ran.main(30))
        armatureresistance = c.resistance(ran.main(0.30))
        
        self.question = f"""Determine the terminal voltage of a generator which develops an EMF of {emf.V} V and has an armature current of {armaturecurrent.A} A on load. Assume the armature resistance is {armatureresistance.ohms} ohms"""
        
        terminalvoltage = c.voltage(emf.V - armaturecurrent.A * armatureresistance.ohms)
        
        self.answer = f"""Terminal Voltage = {terminalvoltage.V} V"""
        
class johnbird_22_8:
    def __init__(self,*args,**kwargs): 
        
        load_resistance = c.resistance(ran.main(60))
        arm_current =  c.current(ran.main(8))
        arm_resistance = c.resistance(ran.main(1))
        
        
        self.question = f"""A generator is connected to a {load_resistance.ohm} ohms load and a current of {arm_current.A} A flows. If the armature resistance is {arm_resistance.ohm} ohm determine a) the terminal voltage and b) the generated emf."""
        
        term_voltage = c.voltage( arm_current.A * load_resistance.ohm )
        gen_emf = c.voltage( term_voltage.V + arm_current.A * arm_resistance.ohm)
        
        self.answer = f"""Terminal Voltage = {term_voltage.V} V
Generated emf = {gen_emf.V} V"""

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
        
        
        self.question = f"""A separately excited generator develops a no - load emf of {emf1.V} V, at an armature speed of {speed1.revpers} rev/s and a flux per pole of {fluxperpole1.Wb} Wb. Determine the generated emf when a) the speed increases to {speed2.revpers} rev/s and the pole flux remains unchanged, b) the speed remains at {speed1.revpers} rev/s and the pole flux is decreased to {fluxperpole3.Wb} Wb, and c) the speed increases to {speed4.revpers} rev/s and the pole flux is decreased to {fluxperpole4.Wb} Wb."""
        
        emf2 = c.voltage( emf1.V * (speed2.revpers / speed1.revpers))
        
        emf3 = c.voltage( emf1.V * (fluxperpole3.Wb / fluxperpole1.Wb))
        
        emf4 = c.voltage( emf1.V * (fluxperpole4.Wb / fluxperpole1.Wb) * (speed4.revpers / speed1.revpers))
        
        self.answer = f"""EMF for a = {emf2.V} V
EMF for b = {emf3.V} V
EMF for c = {emf4.V} V"""

class johnbird_22_10:
    def __init__(self,*args,**kwargs): 
        
        power = c.power(ran.main(20000))
        load_voltage = c.voltage(ran.main(200))
        cable_resistance = c.resistance(ran.main(100), 'mohm')
        field_resistance = c.resistance(ran.main(50), 'ohm')
        arm_resistance = c.resistance(ran.main(40), 'mohm')
        
        self.question = f"""A shunt generator supplies a {power.kW} kW load at {load_voltage.V} V through cables of resistance, R = {cable_resistance.mohms} mohms. If the field winding resistance Rf = {field_resistance.ohms} ohms and the armature resistance, Ra = {arm_resistance.mohms} mohms, determine the a) terminal voltage and b) the emf generated in the armature."""

        load_current = c.current(power.W / load_voltage.V)
        cable_voltage = c.voltage(load_current.A * cable_resistance.ohms)
        terminal_voltage = c.voltage(load_voltage.V + cable_voltage.V)
        
        field_current = c.current(terminal_voltage.V / field_resistance.ohm)
        arm_current = c.current( field_current.A + load_current.A )
        
        generated_emf = c.voltage(terminal_voltage.V + arm_current.A * arm_resistance.ohm )
        
        self.answer = f"""Terminal Voltage = {terminal_voltage.V} V
Generated EMF = {generated_emf.V} V"""

class johnbird_22_11:
    def __init__(self,*args,**kwargs): 
        
        load_current = c.current(ran.main(80))
        load_voltage = c.voltage(ran.main(200))
        field_resistance = c.resistance(ran.main(40))
        series_resistance = c.resistance(ran.main(0.02))
        arm_resistance = c.resistance(ran.main(0.04))
        
        
        self.question = f"""A short shunt compound generator supplies {load_current.A} A at {load_voltage.V} V. If the field resistance, Rf = {field_resistance.ohm} ohms, the series resistance, Rse = {series_resistance.ohm} ohms, and the armature resistance, Ra = {arm_resistance.ohm} ohms, determine the emf generated."""
        
        
        field_voltage = c.voltage( load_voltage.V + series_resistance.ohm * load_current.A)
        arm_voltage = c.voltage( field_voltage.V )
        
        field_current = c.current( field_voltage.V / field_resistance.ohm)
        
        arm_current = c.current( load_current.A + field_current.A)
        
        generated_emf = c.voltage( field_voltage.V + arm_current.A * arm_resistance.ohm)
        
        self.answer = f"""Generated EMF = {generated_emf.V} V"""
        
class johnbird_22_12:
    def __init__(self,*args,**kwargs): 
        
        power = c.power(ran.main(10000))
        arm_resistance = c.resistance(ran.main(0.75))
        field_resistance = c.resistance(ran.main(125))
        terminal_voltage = c.voltage(ran.main(250))
        ironfrictionwindageloss = c.power(ran.main(600))
        
        self.question = f"""A {power.kW} kW shunt generator having an armature circuit resistance of {arm_resistance.ohm} ohms and a field resistance of {field_resistance.ohm} ohms, generates a terminal voltage of {terminal_voltage.V} V at full load. Determine the efficiency of the generator at full load, assuming the iron, friction and windage losses amount to {ironfrictionwindageloss.W} W"""

        load_current = c.current( power.W / terminal_voltage.V )
        field_current = c.current( terminal_voltage.V / field_resistance.ohm )
        arm_current = c.current( field_current.A + load_current.A )
        
        efficiency = c.percentage(power.W / ( power.W + arm_current.A**2 * arm_resistance.ohm + field_current.A*terminal_voltage.V + ironfrictionwindageloss.W ), 'decimal' )
        
        self.answer = f"""Efficiency = {efficiency.percent} %"""
        
class johnbird_22_13:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(240))
        arm_resistance = c.resistance(ran.main(0.2))
        arm_current = c.current(ran.main(50))
        
        self.question = f"""A dc motor operates from a {supply_voltage.V} V. The armature resistance is {arm_resistance.ohm} ohm. Determine the back emf when the armature current is {arm_current.A} A."""
        
        emf = c.voltage(supply_voltage.V - arm_current.A * arm_resistance.ohm)
        
        self.answer = f"""Back EMF = {emf.V} V"""
        
class johnbird_22_14:
    def __init__(self,*args,**kwargs): 
        
        arm_resistance = c.resistance( ran.main(0.25))
        supply_voltage = c.voltage( ran.main(300))
        generator_current = c.current(ran.main(100))
        motor_current = c.current(ran.main(80))
        
        self.question = f"""The armature of a DC machine has a resistance of {arm_resistance.ohm} ohm and is connected to a {supply_voltage.V} V supply. Calculate the emf generated when it is running a) as a generator giving {generator_current.A} A, and b) as a motor taking {motor_current.A} A"""
        
        emf_generator = c.voltage( supply_voltage.V + generator_current.A * arm_resistance.ohm )
        
        emf_motor = c.voltage( supply_voltage.V - motor_current.A * arm_resistance.ohm )
        
        self.answer = f"""Generated emf as generator = {emf_generator.V} V
Back emf as motor = {emf_motor.V} V"""

class johnbird_22_15:
    def __init__(self,*args,**kwargs): 
        
        polepairs = ran.main(4, 'int')
        poles = polepairs * 2
        conductors = ran.main(900)
        fluxperpole = c.magneticFlux(ran.main(25), 'mWb')
        arm_current = c.current(ran.main(30))
        config = 2
        
        self.question = f"""An {poles}-pole dc motor has a wave-wound armature with {conductors} conductors. The useful flux per pole is {fluxperpole.mWb} mWb. Determine the torque exerted when a current of {arm_current.A} A flows in each armature conductor"""
        
        torque = c.torque( 
        (polepairs * fluxperpole.Wb * conductors * arm_current.A) / 
        ( math.pi * config )
        )
        
        self.answer = f"""Torque = {torque.Nm} Nm"""
        
class johnbird_22_16:
    def __init__(self,*args,**kwargs): 
        
        
        supply_voltage = c.voltage(ran.main(350))
        arm_resistance = c.resistance(ran.main(0.5))
        speed = c.angularVelocity(ran.main(15), 'revpers')
        arm_current = c.current(ran.main(60))
        
        self.question = f"""Determine the torque developed by a {supply_voltage.V} V dc motor having an armature resistance of {arm_resistance.ohms} ohms and running at {speed.revpers} rev/s. The armature current is {arm_current.A} A."""
        
        emf = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm)
        
        torque = c.torque( (emf.V * arm_current.A) / (2*math.pi*speed.revpers) )
        
        self.answer = f"""Torque = {torque.Nm} Nm"""
        
class johnbird_22_17:
    def __init__(self,*args,**kwargs): 
        
        polepairs = ran.main(3, 'int')
        poles = 2* polepairs
        supply_voltage = c.voltage(ran.main(250))
        conductors = ran.main(500, 'int')
        arm_resistance = c.resistance(ran.main(1))
        fluxperpole = c.magneticFlux(ran.main(20), 'mWb')
        arm_current = c.current(ran.main(40))
        config = 2 * polepairs
        
        self.question = f"""A {poles} - pole lapwound motor is connected to a {supply_voltage.V} V supply. The armature has {conductors} conductors and a resistance of {arm_resistance.ohm} ohm. The flux per pole is {fluxperpole.mWb} mWb. Calculate a) the speed and b) the torque developed when the armature current is {arm_current.A} A."""
        
        
        emf = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm)
        
        speed = c.angularVelocity( (emf.V) / (conductors * fluxperpole.Wb), 'revpers' )
        
        torque = c.torque( (emf.V * arm_current.A) / (2*math.pi*speed.revpers) )
        
        self.answer = f"""Speed = {speed.revpers} rev/s
Torque = {torque.Nm} Nm"""
        
class johnbird_22_18:
    def __init__(self,*args,**kwargs): 
        
        voltage = c.voltage(ran.main(100))
        torque = c.torque(ran.main(25))
        arm_current = c.current(ran.main(16))
        percentreduction = c.percentage(ran.main(15), 'percent')
        torque2 = c.torque(torque.Nm + ran.main(10))
        
        
        self.question = f"""The shaft torque of a diesel motor driving a {voltage.V} V dc shunt wound generator is {torque.Nm} Nm. The armature current of the generator is {arm_current.A} A at this value of torque. If the shunt field regulator is adjusted so that the flux is reduced by {percentreduction.percent} percent, the torque increases to {torque2.Nm} Nm. Determine the armature current at this new value of torque."""
        
        arm_current2 = c.current( (arm_current.A * torque2.Nm) / ((1 - percentreduction.decimal) * torque.Nm)  )
        
        self.answer = f"""New armature current = {arm_current2.A} A"""
        
class johnbird_22_19:
    def __init__(self,*args,**kwargs): 
        
        
        load_voltage = c.voltage(ran.main(100))
        load_current = c.current(ran.main(15))
        speed = c.angularVelocity(ran.main(1500), 'revpermin')
        torque = c.torque(ran.main(12))
        
        
        self.question = f"""A {load_voltage.V} V dc generator supplies a current of {load_current.A} A when running at {speed.revpermin} rev/min. If the torque on the shaft driving the generator is {torque.Nm} Nm, determine a) the efficiency of the generator and b) the power loss in the generator."""
        
        efficiency = c.percentage( (load_voltage.V * load_current.A) / (torque.Nm * math.pi * 2 * speed.revpers), 'decimal')
        
        losses = c.power( torque.Nm * math.pi * 2 * speed.revpers - load_voltage.V * load_current.A )
        
        self.answer = f"""Efficiency = {efficiency.percent} percent
Losses = {losses.W} W"""

class johnbird_22_20:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(240))
        supply_current = c.current(ran.main(30))
        field_resistance = c.resistance(ran.main(150))
        arm_resistance = c.resistance(ran.main(0.4))
        
        
        self.question = f"""A {supply_voltage.V} V shunt motor takes a total current of {supply_current.A} A. If the field winding resistance Rf = {field_resistance.ohm} ohms and the armature resistance Ra = {arm_resistance.ohm} ohms, determine a) the current in the armature and b) the back emf."""
        
        field_current = c.current( supply_voltage.V / field_resistance.ohm )
        arm_current = c.current( supply_current.A - field_current.A )
        
        back_emf = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm )
        
        self.answer = f"""Armature current = {arm_current.A} A
Back EMF = {back_emf.V} V"""

class johnbird_22_21:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage( ran.main(200) )
        arm_resistance = c.resistance(ran.main(0.4))
        arm_current = c.current(ran.main(30))
        speed = c.angularVelocity(ran.main(1350), 'revpermin')
        arm_current2 = c.current(arm_current.A + ran.main(15))
        
        
        
        self.question = f"""A {supply_voltage.V} V dc shunt wound motor has an armature resistance of {arm_resistance.ohm} ohm and at a certain load has an armature current of {arm_current.A} A and runs at {speed.revpermin} rev/min. If the load on the shaft of the motor is increased so that the armature current increases to {arm_current2.A} A, determine the speed of the motor, assuming the flux remains constant."""
        
        emf = c.voltage(supply_voltage.V - arm_current.A * arm_resistance.ohm)
        emf2 = c.voltage(supply_voltage.V - arm_current2.A * arm_resistance.ohm)
        
        speed2 = c.angularVelocity(
        (speed.revpermin * emf2.V)/(emf.V), 'revpermin'
        )
        
        self.answer = f"""The speed of motor when Ia = {arm_current2.A} A = {speed2.revpermin} rev/min."""
        
class johnbird_22_22:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage( ran.main(220) )
        speed = c.angularVelocity( ran.main(800), 'revpermin' )
        arm_current = c.current( ran.main(30))
        arm_resistance = c.resistance( ran.main(0.4))
        fluxreduction = c.percentage(  ran.main(10), 'percent')
        
        self.question = f"""A {supply_voltage.V} V dc shunt-wound motor runs at {speed.revpermin} rev/min and the armature current is {arm_current.A} A. The armature circuit resistance is {arm_resistance.ohm} ohms. Determine a) the maximum value of armature current if the flux is suddenly reduced by {fluxreduction.percent} percent and b) the steady state value of the armature current at the new value of flux, assuming the shaft torque of the motor remains constant."""
        
        emf_initial = c.voltage( supply_voltage.V - arm_current.A * arm_resistance.ohm )
        
        emf_transient  = c.voltage( emf_initial.V * (1 - fluxreduction.decimal) )
        #print(f"""EMF initial = {emf_initial.V}""")
        #print(f"""EMF transient = {emf_transient.V}""")
        arm_voltage_transient = c.voltage( supply_voltage.V - emf_transient.V )
        arm_current_transient = c.current( arm_voltage_transient.V / arm_resistance.ohm)
        
        arm_current2 = c.current( arm_current.A  / (1 - fluxreduction.decimal) )
        
        self.answer = f"""Max armature current = {arm_current_transient.A} A
Steady-state armature current = {arm_current2.A} A"""

class johnbird_22_23:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(240))
        arm_resistance = c.resistance(ran.main(0.2))
        field_resistance = c.resistance(ran.main(0.3))
        speed = c.angularVelocity(ran.main(24), 'revpers')
        arm_current = c.current(ran.main(15))
        arm_current2 = c.current(arm_current.A + ran.main(15))
        
        
        self.question = f"""A series motor has an armature resistance of {arm_resistance.ohm} ohms and a series field resistance of {field_resistance.ohm} ohms. It is connected to a {supply_voltage.V} V supply and at a particaular load runs at {speed.revpers} rev/s when drawing {arm_current.A} A from the supply. a) Determine the generated emf at this load. b) Calculate the speed of the motor when the load is changed such that the current is increased to {arm_current2.A} A. Assume that this causes a doubling of the flux."""
        
        emf = c.voltage( supply_voltage.V - arm_current.A * (arm_resistance.ohm + field_resistance.ohm) )
        
        emf2 = c.voltage( supply_voltage.V - arm_current2.A * (arm_resistance.ohm + field_resistance.ohm) )
        
        speed2 = c.angularVelocity( (speed.revpers * emf2.V) / (2 * emf.V) )
        
        self.answer = f"""EMF generated at initial load = {emf.V} V
Speed of motor = {speed2.revpers} rev/s"""

class johnbird_22_24:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(320))
        supply_current = c.current(ran.main(80))
        speed = c.angularVelocity(ran.main(1000), 'revpermin')
        losses = c.power(ran.main(1500),'W')
        field_resistance = c.resistance(ran.main(40))
        arm_resistance = c.resistance(ran.main(0.2))
        
        self.question = f"""A {supply_voltage.V} V shunt motor takes a total current of {supply_current.A} A and runs at {speed.revpermin} rev/min. If the iron, friction, and windage losses amount to {losses.kW} kW, the shunt field resistance is {field_resistance.ohm} ohms and the armature resistance is {arm_resistance.ohm} ohms, determine the overall efficiency of the motor."""
        
        field_current = c.current(supply_voltage.V / field_resistance.ohm)
        arm_current = c.current(supply_current.A - field_current.A)
        efficiency = c.percentage( (supply_voltage.V * supply_current.A - arm_current.A**2 * arm_resistance.ohm - field_current.A * supply_voltage.V - losses.W)/(supply_voltage.V * supply_current.A), 'decimal')
        
        self.answer = f"""Efficiency = {efficiency.percent} percent"""
        
class johnbird_22_25:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(250))
        supply_current = c.current(ran.main(40))
        arm_resistance = c.resistance(ran.main(0.15))
        field_resistance = c.resistance(ran.main(0.05))
        
        
        self.question = f"""A {supply_voltage.V} V series motor draws a current of {supply_current.A} A. The armature resistance is {arm_resistance.ohm} ohms and the field resistance is {field_resistance.ohm} ohms. Determine the maximum efficiency of the motor."""
        
        efficiency = c.percentage((supply_voltage.V * supply_current.A - 2 * supply_current.A**2 *(arm_resistance.ohm + field_resistance.ohm) )/(supply_voltage.V * supply_current.A), 'decimal')
        
        self.answer = f"""Efficiency = {efficiency.percent} percent"""
        
class johnbird_22_26:
    def __init__(self,*args,**kwargs): 
        
        supply_voltage = c.voltage(ran.main(200))
        torque = c.torque(ran.main(15))
        speed = c.angularVelocity(ran.main(1200), 'revpermin')
        efficiency = c.percentage(100 - ran.main(20), 'percent')
        
        
        self.question = f"""A {supply_voltage.V} V dc motor develops a shaft torque of {torque.Nm} Nm at {speed.revpermin} rev/min. If the efficiency is {efficiency.percent} percent, determine the current supplied to the motor."""
        
        current = c.current((torque.Nm * math.pi * 2 * speed.revpers)/(supply_voltage.V * efficiency.decimal))
        
        self.answer = f"""Current supplied = {current.A} A"""
        
class johnbird_22_27:
    def __init__(self,*args,**kwargs): 
        
        speed = c.angularVelocity(ran.main(30), 'revpers')
        supply_current = c.current(ran.main(10))
        supply_voltage = c.voltage(ran.main(400))
        total_resistance = c.resistance(ran.main(2))
        losses = c.power(ran.main(300))
        
        
        self.question = f"""A dc series motor drives a load at {speed.revpers} rev/s and takes a current of {supply_current.A} A when the supply voltage is {supply_voltage.V} V. If the total resistance of the motor is {total_resistance.ohm} ohms and the iron, friction, and windage losses amount to {losses.W} W, determine the efficiency of the motor."""
        
        efficiency = c.percentage( (supply_voltage.V * supply_current.A - supply_current.A**2 * total_resistance.ohm - losses.W) / (supply_voltage.V * supply_current.A) , 'decimal'  )
        
        self.answer = f"""Efficiency = {efficiency.percent} percent"""
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        