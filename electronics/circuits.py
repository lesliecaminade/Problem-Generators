import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables
            
#SADIKU FILES
class sadiku_1_1:
    def __init__(self,*args,**kwargs): 
        #print('1_1')
        electrons = ran.main(4600)
        
        self.question = f"""How much charge is represented by {electrons} electrons?"""
        
        charge = c.charge(
        electrons * c.CHARGE_ELECTRON
        )
        
        self.answer = f"""Charge = {charge.C} C"""

class sadiku_1_2:
    def __init__(self,*args,**kwargs):
        #print('1_2')
        time = c.time(ran.main(0.5))
        charge = ran.main(5, 'int') * t * sym.sin(ran.main(4, 'int') * sym.pi * t) 
        
        self.question = f"""The total charge entering a terminal is given by 
q = {sym.pretty(charge)} mC. Calculate the current at t = {time.ms} ms"""

        current = sym.diff(charge, t)
        
        #print(current)
        
        current_at_t = c.current(
        float(current.subs(t, time.s)), 'mA'
        )
        self.answer =f"""Current = {current_at_t.mA} mA"""
        
class sadiku_1_3:
    def __init__(self,*args,**kwargs):

        time1 = c.time(ran.main(1))
        time2 = c.time(time1.s + ran.main(1))
        current_function = (ran.main(3, 'int') * t**2 - t)
        
        self.question = f"""Determine the total charge entering a terminal between {time1.s} s and {time2.s} s if the current passing the terminal is i = 
{sym.pretty(current_function)} A."""

        charge = c.charge(sym.integrate(
        current_function, (t, time1.s, time2.s) 
        ))
        
        self.answer = f"""Charge = {charge.C} C"""

class sadiku_1_4:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(2))
        time = c.time(ran.main(10))
        energy = c.energy(ran.main(2300))
        
        self.question = f"""An energy source forces a constant current of {current.A} A for {time.s} s to flow through a light bulb. If {energy.kJ} kJ is given off in the form of light and heat energy, calculate the voltage drop across the bulb."""

        charge = c.charge(
        current.A * time.s
        )
        
        voltage = c.voltage(
        energy.J / charge.C
        )
        
        self.answer = f"""Voltage drop = {voltage.V} V"""
        
class sadiku_1_5:
    def __init__(self,*args,**kwargs): 
        
        factor = random.randint(2,4)
        current_function = ran.main(5, 'int') * sym.cos(ran.main(60, 'int') * sym.pi * t)
        time = c.time(ran.main(3), 'ms')
        
        
        self.question = f"""Find the power delivered to an element at t = {time.ms} ms if the current entering the positive terminal is i = 
{current_function} A
and the voltage is a) {factor} i ,  b) {factor} di / dt."""

        #A
        voltage_function_a = 3 * current_function
        power_function_a = voltage_function_a * current_function
        power_a = c.power(
        float(power_function_a.subs(t, time.s))
        )
        
        #B
        voltage_function_b = 3 * current_function.diff(t)
        power_function_b = voltage_function_b * current_function
        power_b = c.power(
        float(power_function_b.subs(t, time.s))
        )
        
        self.answer = f"""Power at A = {power_a.W} W
Power at B = {power_b.W} W"""


class sadiku_1_6:
    def __init__(self,*args,**kwargs):
        
        power = c.power(ran.main(100))
        time = c.time(ran.main(2), 'hours')
        
        self.question = f"""How much energy does a {power.W}-W electric bulb consume in {time.hours} hour(s)?"""
    
        energy = c.energy(
        power.W * time.s
        )
        
        self.answer = f"""Energy = {energy.Wh} Wh = {energy.kJ} kJ"""
        
class sadiku_1_7:
    def __init__(self,*args,**kwargs): 
        
        vs1 = c.voltage(ran.main(20))
        k = random.randint(2,5)/10
        
        #i2 = i1 + i3
        i1 = c.current(ran.main(5))
        i3 = c.current(k * i1.A)
        i2 = c.current(i1.A + i3.A)
        
        v1 = c.voltage(random.randint(5,15))
        v2 = c.voltage(vs1.V - v1.V)
        
        self.question = f"""Calculate the power supplied or absorbed by each element in the figure. VS = {vs1.V} V, I = {i1.A} A, k = {k}, V1 = {v1.V} V, V2 = {v2.V} V
        https://lesliecaminadecom.files.wordpress.com/2019/07/f1aptq67o9fhyo3faxt6.png"""
        
        p1 = c.power(
        - vs1.V * i1.A
        )
        
        p2 = c.power(
        v1.V * i1.A
        )
        
        p3 = c.power(
        v2.V * i2.A
        )
        
        p4 = c.power(
        - i3.A * v2.V 
        )
        
        self.answer = f"""P1 = {p1.W} W
P2 = {p2.W} W
P3 = {p3.W} W
P4 = {p4.W} W"""

class sadiku_1_8:
    def __init__(self,*args,**kwargs): 
        
        electrons = ran.main(10**15)
        power = c.power(ran.main(4))
        
        self.question = f"""The electron bean in a TV picture tube carries {electrons} electrons per second. As a design engineer, determine the voltage needed to accelerate the electron beam to achieve {power.W} W."""
        
        current = c.current(
        c.CHARGE_ELECTRON * electrons
        )
        
        voltage = c.voltage(
        power.W / current.A
        )
        
        self.answer = f"""Voltage  = {voltage.V} V"""
        
class sadiku_1_9:
    def __init__(self,*args,**kwargs): 
        regen = 1
        while regen:
            
            consumed = c.energy(ran.main(700), 'kWh')
            base = c.money(ran.main(12))
            rate1 = c.money(ran.main(16)/100)
            rate2 = c.money(ran.main(10)/100)
            rate3 = c.money(ran.main(6)/100)
            
            self.question = f"""A homeowner consumes {consumed.kWh} kWh in January. Determine the electricity bill for the month using the following residential rate schedule:
Base monthly charge of ${base.money}
First 100 kWh per month at {rate1.money} cents per kWh.
Next 200 kWh per month at {rate2.money} cents per kWh.
Over 300 kWh per month at {rate3.money} cents per kWh."""
            
            
            if consumed.kWh > 300:
                regen = 0
        
        cost = c.money(
        base.money + rate1.money * 100 + rate2.money * 200 + rate3.money * (consumed.kWh - 300)
        )
        
        self.answer = f"""Total charge = $ {cost.money}"""
        
class sadiku_2_1:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(2))
        voltage = c.voltage(ran.main(120))
        
        self.question = f"""An electric iron draws {current.A} A at {voltage.V} V. Find its resistance."""
        
        resistance = c.resistance(
        voltage.V / current.A
        )
        
        self.answer = f"""Resistance = {resistance.ohms} ohms"""
        
class sadiku_2_2:
    def __init__(self,*args,**kwargs): 
        
        vs = c.voltage(ran.main(30))
        r1 = c.resistance(ran.main(1000), 'ohms')
        
        self.question = f"""Calculate the current I, the conductance G, and the power P if the source voltage is {vs.V} V and the resistance is {r1.kohms} kohms.
        https://lesliecaminadecom.files.wordpress.com/2019/07/v95ojza08zd6oum3k8x8.png"""
        
        i1 = c.current(
        vs.V / r1.ohms
        )
        
        g1 = c.conductance(
        1/r1.ohms
        )
        
        p1 = c.power(
        vs.V * i1.A
        )
        
        self.answer = f"""I = {i1.mA} mA
G = {g1.mS} mS
P = {p1.mW} mW"""

class sadiku_2_3:
    def __init__(self,*args,**kwargs): 
        
        voltage_function = ran.main(20, 'int') * sym.sin(sym.pi * t)
        r1 = c.resistance(ran.main(5), 'kohms')
        
        self.question = f"""A voltage source of 
{sym.pretty(voltage_function)}
(volts) is connected across a {r1.kohms} kohms resistor. Find the current through the resistor and the power dissipated.""" 

        i1 = c.current(
        voltage_function / r1.ohms
        )
        
        p1 = c.power(
        voltage_function * i1.A
        )
        
        self.answer = f"""Current:
{sym.pretty(i1.mA)} mA

Power:
{sym.pretty(p1.mW)} mW"""

class sadiku_2_5:
    def __init__(self,*args,**kwargs): 
        
        vs = c.voltage(ran.main(20))
        r1 = c.resistance(ran.main(2))
        r2 = c.resistance(ran.main(3))
        
        self.question = f"""Find voltages v1 and v2 given that the source voltage is {vs.V} V and the resistances are {r1.ohms} ohms and {r2.ohms} respectively.
        https://lesliecaminadecom.files.wordpress.com/2019/07/k5h9rj10ayhw26p8k4m0.png"""
        
        i1 = c.current(
        vs.V / (r1.ohms + r2.ohms)
        )
        
        v1 = c.voltage(
        i1.A * r1.ohms
        )
        
        v2 = c.voltage(
        i1.A * r2.ohms
        )
        
        self.answer = f"""v1 = {v1.V} V, v2 = {v2.V} V"""


class sadiku_2_6:
    def __init__(self,*args,**kwargs):

        vs1 = c.voltage(ran.main(12))
        vs2 = c.voltage(ran.main(4))
        r1 = c.resistance(ran.main(4))
        r2 = c.resistance(ran.main(6))
        k = ran.main(2)
        
        self.question = f"""Determine "vo" and "i" in the circuit shown.
        VS1 = {vs1.V} V, VS2 = {vs2.V} V, R1 = {r1.ohms} ohms, R2 = {r2.ohms} ohms, k = {k}.
        https://lesliecaminadecom.files.wordpress.com/2019/07/w1g4cq0kw95sihf1reww.png"""
        
        equation = sym.Eq(
        - vs1.V + r1.ohms * x + k * (r2.ohms * x) - vs2.V + r2.ohms * x, 0
        )
        
        i_set = sym.solveset(equation, x)
        i_list = list(i_set)
        i1 = c.current(i_list[0])
        
        vo = c.voltage(
        i1.A * r2.ohms
        )
        
        self.answer = f"""i = {i1.A} A, vo = {vo.V} V"""
        
class sadiku_2_7:
    def __init__(self, *args, **kwargs):
        
        k = ran.main(0.5)
        r1 = c.resistance(ran.main(4))
        i1 = c.current(ran.main(3))
        
        self.question = f"""Find the current "io" and voltage "vo" in the circuit where k = {k}, R1 = {r1.ohms} ohms and I1 = {i1.A} A
        https://lesliecaminadecom.files.wordpress.com/2019/07/o7mkhkni8anq87u9gf9o.png"""
        
        equation = sym.Eq(
        i1.A + k * x, x
        )
        
        io_set = sym.solveset(equation, x)
        io_list = list(io_set)
        io = c.current(io_list[0])
        
        vo = c.voltage(
        r1.ohms * io.A
        )
        
        self.answer = f"""io = {io.A} A, vo = {vo.V} V"""
        
class sadiku_2_8:
    def __init__(self, *args, **kwargs):
        
        vs = c.voltage(ran.main(30))
        r1 = c.resistance(ran.main(8))
        r2 = c.resistance(ran.main(3))
        r3 = c.resistance(ran.main(6))
        
        self.question = f"""Find the currents and voltages in the circuit where VS = {vs.V}V, R1 = {r1.ohms} ohms, R2 = {r2.ohms} ohms,  and R3 = {r3.ohms} ohms.
        https://lesliecaminadecom.files.wordpress.com/2019/07/v3j2nfz2zo65lrffdt56.png"""
        
        equations = [
        sym.Eq(x - y - z, 0),
        sym.Eq(- vs.V + r1.ohms * x + r2.ohms * y, 0),
        sym.Eq(r3.ohms * z , r2.ohms * y)
        ]
        
        solutions_set = sym.linsolve(equations, x, y, z)
        #print(solutions_set)
        # print(solutions_set.args[0])
        
        i1 = c.current(solutions_set.args[0][0])
        i2 = c.current(solutions_set.args[0][1])
        i3 = c.current(solutions_set.args[0][2])

        
        v1 = c.voltage(
        r1.ohms * i1.A
        )
        
        v2 = c.voltage(
        r2.ohms * i2.A
        )
        
        v3 = c.voltage(
        r3.ohms * i3.A
        )
        
        self.answer = f"""I1, I2, I3 = {i1.A} A, {i2.A} A, {i3.A} A
V1, V2, V3 = {v1.V} V, {v2.V} V, {v3.V} V"""


        

#JOHNBIRD
class johnbird_2_1:
    def __init__(self,*args,**kwargs): 
        
        charge = c.charge( ran.main(0.24))
        time = c.time(ran.main(15), 'ms')
        
        
        self.question = f"""What current must flow if {charge.C} coulombs is to be transferred in {time.ms} ms?"""
        
        current = c.current(charge.C / time.s)
        
        self.answer = f"""Current = {current.A} A"""
        
class johnbird_2_2:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(10))
        time = c.time(ran.main(4), 'min')
        
        self.question = f"""If a current of {current.A} A flows {time.min} minutes, find the quantity of electricity transferred."""
        
        charge = c.charge(current.A * time.s)
        
        self.answer = f"""Charge = {charge.C} C"""
        
class johnbird_2_3:
    def __init__(self,*args,**kwargs): 
        
        
        current = c.current(ran.main(0.8))
        voltage = c.voltage(ran.main(20))
        
        self.question = f"""The current flowing through a resistor is {current.A} A when a p.d. of {voltage.V} V is applied. Determine the value of the resistance."""
        
        resistance = c.resistance(voltage.V / current.A)
        
        self.answer = f"""Resistance = {resistance.ohm} ohms"""
        
        
class johnbird_2_4:
    def __init__(self,*args,**kwargs): 
        
        resistance = c.resistance(ran.main(2), 'kohm')
        current = c.current(ran.main(10), 'mA')
        
        self.question = f"""Determine the p.d. which must be applied to a {resistance.kohm} kohm resistor in order that a current of {current.mA} mA mat flow."""
        
        voltage = c.voltage(current.A * resistance.ohm)
        
        self.answer = f"""Voltage = {voltage.V} V"""
        
class johnbird_2_5:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(50), 'mA')
        voltage = c.voltage(ran.main(12))
        
        self.question = f"""A coil has a current of {current.mA} mA flowing through it when the applied voltage is {voltage.V} V. What is the resistance of the coil?"""
        
        resistance = c.resistance( voltage.V / current.A)
        
        self.answer = f"""Resistance = {resistance.ohm} ohms"""
        
class johnbird_2_6:
    def __init__(self,*args,**kwargs): 
        
        
        voltage = c.voltage(ran.main(100))
        voltage2 = c.voltage(voltage.V - ran.main(25))
        current = c.current(ran.main(5), 'mA')
        
        self.question = f"""A {voltage.V} V battery is connected across a resistor and causes a current of {current.mA} to flow. Determine the resistance of the resistor. If the voltage is now reduced to {voltage2.V} V, what will be the new value of the current flowing?"""
        
        resistance = c.resistance(voltage.V / current.A)
        current2 = c.current(voltage2.V / resistance.ohm)
        
        self.answer = f"""Resistance = {resistance.ohm} ohms
New Current = {current2.mA} mA"""

class johnbird_2_7:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(50), 'mA')
        current2 = c.current(ran.main(200), 'uA')
        voltage = c.voltage(ran.main(120))
        
        self.question = f"""What is the resistance of a coil which draws a current of a) {current.mA} mA and b) {current2.uA} uA from a {voltage.V} V supply?"""
        
        resistance = c.resistance(voltage.V / current.A)
        resistance2 = c.resistance(voltage.V / current2.A)
        
        self.answer = f"""Resistance A = {resistance.ohm} ohms
Resistance B = {resistance2.ohm} ohms"""

class johnbird_2_9:
    def __init__(self,*args,**kwargs): 
        
        power = c.power(ran.main(100))
        voltage = c.voltage(ran.main(250))
        
        
        self.question = f"""A {power.W} W electric light bulb is connected to a {voltage.V} V supply. Determine a) the current flowing through the bulb and b) the resistance of the bulb."""
        
        current = c.current(power.W / voltage.V)
        resistance = c.resistance(voltage.V / current.A)
        
        self.answer = f"""Current = {current.A} A
Resistance = {resistance.ohm} ohms"""

class johnbird_2_10:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(4), 'mA')
        resistance = c.resistance(ran.main(5), 'kohms')
        
        self.question = f"""Calculate the power dissipated when a current of {current.mA} mA flows through a resistance of {resistance.kohms} kohms"""
        
        power = c.power(current.A**2 *  resistance.ohm)
        
        self.answer = f"""Power = {power.mW} mW"""
        
class johnbird_2_11:
    def __init__(self,*args,**kwargs): 
        
        resistance = c.resistance(ran.main(30))
        voltage = c.voltage(ran.main(240))
        
        
        self.question = f"""An electric kettle has a resistance of {resistance.ohms} ohms. What current will flow when it is connected to a {voltage.V} V supply? Find also the power rating of the kettle."""
        
        current = c.current(voltage.V / resistance.ohm)
        
        power = c.power(voltage.V * current.A)
        
        self.answer = f"""Current = {current.A}  A
Power = {power.kW} kW"""

class johnbird_2_12:
    def __init__(self,*args,**kwargs): 
        
        current = c.current(ran.main(5))
        resistance = c.resistance(ran.main(100))
        
        self.question = f"""A current of {current.A} A flows in the winding of an electric motor, the resistance of the winding being {resistance.ohm} ohms. Determine a)the p.d. across the winding and b) the power dissipated by the coil."""
        
        voltage = c.voltage(current.A * resistance.ohm)
        power = c.power(current.A**2 * resistance.ohm)
        
        self.answer = f"""Potential across winding = {voltage.V} V
Power dissipated by coil = {power.kW} kW"""

class johnbird_2_13:
    def __init__(self,*args,**kwargs): 
        
        voltage = c.voltage(ran.main(240))
        resistance = c.resistance(ran.main(960))
        
        self.question = f"""The hot resistance of a {voltage.V}  V filament lamp is {resistance.ohms} ohms. Find the current taken by the lamp and its power rating."""
        
        current = c.current(voltage.V / resistance.ohm)
        
        power = c.power(voltage.V * current.A)
        
        self.answer = f"""Current = {current.A} A
Power Rating = {power.W}  W"""

class johnbird_2_14:
    def __init__(self,*args,**kwargs): 
        
        voltage = c.voltage(ran.main(12))
        resistance = c.resistance(ran.main(40))
        time = c.time(ran.main(2), 'min')
        
        self.question = f"""A {voltage.V} V battery is connected across a load having a resistance of {resistance.ohms} ohms. Determine the current flowing in the load, the power consumed and the energy dissipated in {time.min} minutes."""
        
        current = c.current(voltage.V  / resistance.ohm)
        power = c.power(voltage.V * current.A)
        energy = c.energy(power.W * time.s)
        
        self.answer = f"""Current = {current.A} A
Power = {power.W} W
Energy = {energy.J} J"""

class johnbird_2_15:
    def __init__(self,*args,**kwargs): 
        
        voltage = c.voltage(ran.main(15))
        current = c.current(ran.main(2))
        time = c.time(ran.main(6), 'min')
        
        self.question = f"""A source of emf of {voltage.V} V supplies a current of {current.A} A for {time.min} minutes. How much energy is provided in this time?"""
        
        energy = c.energy(voltage.V * current.A * time.s)
        
        self.answer = f"""Energy = {energy.kJ} kJ"""
        
class johnbird_2_16:
    def __init__(self,*args,**kwargs): 
        
        voltage = c.voltage(ran.main(240))
        current = c.current(ran.main(13))
        time = c.time(ran.main(30, 'int'), 'hours')
        priceperkw = ran.main(12.5)
        
        self.question = f"""Electrical component in an office takes a current of {current.A} from a {voltage.V} supply. Estimate the cost per week of electricity if the equipment is used for {time.hours} hours each week and 1 kWh of energy costs P{priceperkw}"""
        
        power = c.power(voltage.V * current.A)
        energyperweek = c.energy(power.W * time.s)
        costperweek = energyperweek.kWh * priceperkw
        
        self.answer = f"""Weekly Cost of electricity = P{costperweek}"""
        
class johnbird_2_17:
    def __init__(self,*args,**kwargs): 
        
        energy = c.energy(ran.main(3.6), 'MJ')
        voltage = c.voltage(ran.main(250))
        time = c.time(ran.main(40), 'min')
        
        self.question = f"""An electric heater consumes {energy.MJ} MJ when connected to a {voltage.V} V supply for {time.min} minutes. Find the power rating of the heater and the current taken from the supply."""
        
        power = c.power(energy.J / time.s)
        
        current = c.current(power.W / voltage.V)
        
        self.answer = f"""Power rating of heater = {power.kW} kW
Current taken from the supply = {current.A} A"""

class johnbird_2_18:
    def __init__(self,*args,**kwargs): 
        
        resistance = c.resistance(ran.main(20))
        current = c.current(ran.main(10))
        time = c.time(ran.main(6), 'hours')
        costperunit = ran.main(13)
        self.question = f"""Determine the power dissipated by the element of an electric fire of resistance {resistance.ohm} ohms when a current of {current.A} A flows through it. If the fire is on for {time.hours} hours, determine the energy used and the cost if 1 unit of electricity costs P {costperunit}"""
        power = c.power(current.A**2 * resistance.ohms)
        energy = c.energy(power.W * time.s)
        cost = energy.kWh * costperunit
        
        self.answer = f"""Cost = P {cost}"""
        
class johnbird_2_19:
    def __init__(self,*args,**kwargs): 
        costperunit = ran.main(14)
        power = c.power(ran.main(3), 'kW')
        time = c.time(ran.main(20), 'hours')
        power2 = c.power(ran.main(150))
        time2 = c.time(ran.main(30))
        
        self.question = f"""A business uses two {power.kW} kW fires for an average of {time.hours} hours each per week, and six {power2.W} W lights for {time2.hours} hours each per week. If the cost of electricity is {costperunit} cents per unit, determine the weekly cost of electricity to the business"""
        
        energy = c.energy(2 * power.W * time.s)
        energy2 = c.energy(6 * power2.W * time2.s)
        energytotal = c.energy(energy.J + energy2.J)
        cost = costperunit * energytotal.kWh
        
        self.answer = f"""Cost per week = $ {cost}"""
        
class johnbird_3_1:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(5))
        resistance = c.resistance(ran.main(600))
        length2 = c.length(ran.main(8))
        
        resistance3 = c.resistance(ran.main(420))
        
        self.question = f"""The resistance of a {length.m} m length of wire is {resistance.ohms} ohms. Determine a) the resistance of an {length2.m} m length of the same wire and b) the length of the same wire when the resistance is {resistance3.ohms} ohms"""
        
        constant = resistance.ohms / length.m
        resistance2 = c.resistance(constant * length2.m)
        
        length3 = c.length(resistance3.ohms / constant)
        
        self.answer = f"""Resistance A = {resistance2.ohms} ohms
Length B = {length3.m} meters"""

        
class johnbird_3_2:
    def __init__(self,*args,**kwargs): 
        
        area = c.area(ran.main(2), 'mm2')
        resistance = c.resistance(ran.main(300))
        area2 = c.area(area.mm2 + ran.main(3), 'mm2')
        resistance3 = c.resistance(resistance.ohms + ran.main(450))
        
        
        self.question = f"""A piece of wire of cross-sectional area {area.mm2} mm2 has a resistance of {resistance.ohms} ohms. Find a) the resistance of the wire of the same length and material if the cross-sectional area is {area2.mm2} mm2, b) the cross-sectional area of a wire of the same length and material of resistance {resistance3.ohms} ohms."""
        
        
        constant = resistance.ohms * area.m2
        
        resistance2 = c.resistance( constant / area.m2   )
        
        area3 = c.area( constant / resistance3.ohms )
        
        self.answer = f"""Resistance in A = {resistance2.ohms} ohms
Cross Sectional area in B = {area3.mm2} mm2"""

class johnbird_3_3:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(8))
        area = c.area(ran.main(3), 'mm2')
        resistance = c.resistance(ran.main(0.16), 'ohms')
        area2 = c.area(area.mm2 - ran.main(2), 'mm2')
        
        
        self.question = f"""A wire of length {length.m} m and cross-sectional area {area.mm2} mm2 has a resistance of {resistance.ohms} ohms. If the wire is drawn out until its cross-sectional area is {area2.mm2} mm2, determine the resistance of the wire."""
        
        constant = resistance.ohms * area.m2 / length.m
        
        length2 = c.length( length.m * (area2.m2 / area.m2))
        
        resistance2 = c.resistance(constant * length2.m  / area2.m2)
        
        self.answer = f"""New resistance = {resistance2.ohms} ohms."""
        
        
class johnbird_3_4:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(2), 'km')
        area = c.area(ran.main(100), 'mm2')
        resistivity = c.resistivity(0.03e-6)
        
        
        self.question = f"""Calculate the resistance of a {length.km} km length of aluminum overhead power cable if the cross sectional area of the cable is {area.mm2} mm2. Take the resistivity of aluminum to be {resistivity.ohm_m} ohm - m"""
        
        resistance = c.resistance(  (resistivity.ohm_m * length.m) / ( area.m2 )  )
        
        self.answer = f"""Resistance = {resistance.ohm} ohm"""
        
class johnbird_3_5:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(40))
        resistance = c.resistance(ran.main(0.25))
        resistivity = c.resistivity(0.02e-6)
        
        self.question = f"""Calculate the cross-sectional area in mm2, of a piece of copper wire, {length.m} m in length and having a resistance of {resistance.ohms} ohms. Take the resistivity of copper as {resistivity.ohm_m} ohm - m."""
        
        area = c.area(resistivity.ohm_m * length.m / resistance.ohms)
        
        self.answer = f"""Area = {area.mm2} mm2"""
        
        
class johnbird_3_6:
    def __init__(self,*args,**kwargs): 
        
        
        length = c.length(ran.main(1.5), 'km')
        area = c.area(ran.main(0.17), 'mm2')
        resistance = c.resistance(ran.main(150))
        
        
        self.question = f"""The resistance of {length.km} km of wire of cross-sectional area of {area.mm2} mm2 is {resistance.ohms} ohms. Determine the resistivity of the wire."""
        
        resistivity = c.resistivity(resistance.ohms * area.m2 / length.m)
        
        self.answer = f"""Resistivity = {resistivity.uohm_m} uohm - m"""
        
class johnbird_3_7:
    def __init__(self,*args,**kwargs): 
        
        length = c.length(ran.main(1200))
        diameter = c.length(ran.main(12), 'mm')
        resistivity = c.resistivity(1.7e-8)
        
        self.question = f"""Determine the resistance of {length.m} m of copper cable having a diameter of {diameter.mm} mm if the resistivity of copper is {resistivity.ohm_m} ohm - m"""
        
        area = c.area(math.pi * diameter.m**2 / 4)
        
        resistance = c.resistance(resistivity.ohm_m * length.m / area.m2)
        
        self.answer = f"""Resistance = {resistance.ohms} ohms"""
        
class johnbird_3_8:
    def __init__(self,*args,**kwargs): 
        
        resistance = c.resistance(ran.main(100))
        temperature = c.temperature(0, 'C')
        temperature2 = c.temperature(ran.main(70), 'C')
        coefficient = c.temperatureCoefficient(0.0043, 'perC')
        
        self.question = f"""A coil of copper wire has a resistance of {resistance.ohms} ohms when its temperature is {temp.C} degC. Determine its resistance at {temp2.C} degC if the temperature coefficient of resistance of copper at {temp.C} degC is {coefficient.perC} per degC."""
        
        resistance2 = c.resistance(resistance.ohms + resistance.ohms * coefficient.perC * (temperature2.C - temperature.C))
        
        self.answer  = f"""New Resistance = {resistance2.ohms} ohms"""
        
class johnbird_3_9:
    def __init__(self,*args,**kwargs): 
        
        
        resistance = c.resistance(ran.main(27))
        temperature = c.temperature(ran.main(35), 'C')
        temperature2 = c.temperature(0, 'C')
        coefficient = 0.0038
        
        
        self.question = f"""An aluminum cable has a resistance of {resistance.ohms} ohms at a temperature of {temperature.C} degC. Determine its resistance at {temperature2.C} degC. Take the temperature coefficient of resistance at {temperature2.C} degC to be {coefficient} per C"""
        
        resistance2 = c.resistance(resistance.ohms / (1 + coefficient * (temperature.C  - temperature2.C)))
        
        self.answer = f"""Resistance = {resistance2.ohms} ohms"""

class johnbird_3_10:
    def __init__(self):
        resistance = c.resistance(ran.main(1), 'kohms')
        tempcoe = - 0.0005
        temp1 = c.temperature(0, 'C')
        temp2 = c.temperature(ran.main(80), 'C')
        resistance2 = c.resistance(
            1000 * ( 1 + tempcoe * (temp2.C - temp1.C)))


        self.question = f"""A carbon resistor has a resistance of {resistance.kohms} kohms at {temp1.C} degC. Determine its resistance at {temp2.C} degC. Assume that the temperature coefficient of resistance for carbon at {temp1.C} degC is {tempcoe} per degC."""

        self.answer = f"""Resistance = {resistance2.ohms} ohms"""

class johnbird_3_11:
    def __init__(self):

        resistance1 = c.resistance(ran.main(10))
        temp1 = c.temperature(ran.main(20), 'C')
        tempcoe = 0.004
        temp2 = c.temperature(temp1.C + ran.main(80), 'C')
        resistance2 = c.resistance(resistance1.ohms * (1 + (tempcoe * (temp2.C - temp1.C))))


        self.question = f"""A coil of copper wire has a resistance of {resistance1.ohms} ohms at {temp1.C} degC. If the temperature coefficient of resistance of copper at {temp1.C} degC is {tempcoe} per degC determine the resistance of the coil when the temperature rises to {temp2.C} degC."""

        self.answer = f"""Resistance at {temp2.C} degC = {resistance2.ohms} ohms"""

class johnbird_3_12:
    def __init__ (self):

        temp1 = c.temperature(ran.main(18), 'C')
        resistance1 = c.resistance(ran.main(200))
        resistance2 = c.resistance(resistance1.ohms + ran.main(40))
        coe = 0.0039

        equation = sym.Eq(resistance2.ohms, resistance1.ohms * ( 1 + coe * (x - temp1.C) ) )

        solution_set = sym.solveset(equation, x)
        solution_list = list(solution_set)
        temp2 = c.temperature(solution_list[0], 'C')


        self.question = f"""The resistance of a coil of aluminum wire at {temp1.C} degC is {resistance1.ohms} ohms. The temperature of the wire is increased and the resistance rises to {resistance2.ohms} ohms. If the temperature coefficient of resistance of aluminum is {coe} per degC at {temp1.C} degC. Determine the temperature to which the coil has risen."""

        self.answer = f"""Temperature the coil has risen to = {temp2.C} degC"""

class johnbird_3_13:
    def __init__ (self):
        resistance1 = c.resistance(ran.main(200))
        temp1 = c.temperature(ran.main(20), 'C')
        temp2 = c.temperature(temp1.C + ran.main(70), 'C')
        coe = 0.004

        resistance2 = c.resisstance(
            (resistance1.ohms * (1 + coe*temp2.C))/(1 + coe*temp1.C) )

        self.question = f"""Some copper wire has a resistance of {resistance1.ohms} ohms at {temp1.C} degC. A current is passed through the wire and the temperature rises to {temp2.C} degC. Determine the resistance of the wire at {temp2.C} degC, assuming that the temperature coefficient of resistance if {coe} /degC at 0 degC."""

        self.answer = f"""Resistance of the wire at {temp2.C} degC = {resistance2.ohms} ohms"""

class johnbird_3_14:
    def __init__(self):
        resistor1 = c.resistor(band = random.randint(3,4))
        self.question = f"""Determine the value and tolerance of a resistor having a color coding of: {resistor1.color}."""
        self.answer = f"""Value = {resistor1.resistance.ohms} ohms, Tolerance = {resistor1.tolerance}"""

class johnbird_3_16:
    def __init__(self):
        resistor1 = c.resistor(band = random.randint(3,4))
        self.question = f"""Between what two values should a resistor with color coding: {resistor1.color} lie?"""
        self.answer = f"""Resistance range: {resistor1.minresistance.ohms} ohms to {resistor1.maxresistance.ohms} ohms"""

class johnbird_3_17:
    def __init__(self):
        resistor1 = c.resistor()
        self.question = f"""Determine the color coding for a {resistor1.resistance.ohms} ohms having a tolerance of {resistor1.tolerance}"""
        self.answer = f"""Color coding: {resistor1.color} """

class johnbird_3_18:
    def __init__(self):
        resistor1 = c.resistor(band = 5)

        self.question = f"""Determine the value and tolerance of a resistor having a color coding of: {resistor1.color}."""

        self.answer = f"""Resistor value: {resistor1.resistance.ohms} ohms, Tolerance: {resistor1.tolerance} """

class johnbird_3_19:
    def __init__(self):
        D1 = random.randint(1,9)
        D0 = random.randint(1,9)
        i = random.randint(0,4)

        code_list = ['F', 'G', 'J', 'K', 'M']
        tolerance_code = code_list[i]
        tolerance_list = ['1%', '2%', '5%', '10%', '20%']
        tolerance = tolerance_list[i]

        j = random.randint(0,3)
        prefix_list = ['R', 'K', 'M']
        prefix_values = [1, 1000, 1e6]

        resistance1 = c.resistance(
            ((D1 * 10 + D0) / 10) * prefix_values[j] )


        self.question = f"""Determine the value of a resistor marked as {D1}{code}{D0}{tolerance_code}."""

        self.answer = f"""Resistance: {resistance1.ohms} ohms (+/-) {tolerance}"""

class johnbird_5_1:
    def __init__(self):
        v1 = c.voltage(ran.main(5))
        v2 = c.voltage(ran.main(2))
        v3 = c.voltage(ran.main(6))
        it = c.current(4)

        vt = c.voltage(v1.V + v2.V + v3.V)
        rt = c.resistance( vt.V / it.A )

        self.question = f"""For the battery circuit shown https://lesliecaminadecom.files.wordpress.com/2019/09/2019_09_26_13_02_53.png determine the total circuit resistance, given that the p.d's across R1, R2, and R3 are {v1.V} V, {v2.V} V, and {v3.V} V respectively."""
        self.answer = f"""Total resistance = {rt.ohms} ohms"""

class johnbird_5_2:
    def __init__(self):
        rt = c.resistance(ran.main(100))
        v1 = c.voltage(10)
        v2 = c.voltage(4)
        vt = c.voltage(25)
        v3 = c.voltage(25 - 10 - 4)
        it = c.current(vt.V / rt.ohms)
        r2 = c.resistance(v2.V / it.ohms)

        self.question = f"""For the circuit shown https://lesliecaminadecom.files.wordpress.com/2019/09/2019_09_26_14_44_19.png, if the total resistance of the circuit is {rt.ohms} ohms, find the value of the resistance R2."""

        self.answer = f"""Resistance R2 = {r2.ohms} ohms"""

class johnbird_5_3:
    def __init__(self):
        vbat = c.voltage(ran.main(12))
        r1 = c.resistance(ran.main(4))
        r2 = c.resistance(ran.main(9))
        r3 = c.resistance(ran.main(11))

        it = c.current(vbat.V / (r1.ohms + r2.ohms + r3.ohms))
        p3 = c.power(it.A**2 * r3.ohms)

        self.question = f"""A {vbat.V} V battery is connected in a circuit having three series-connected resistors haveing resistance's of {r1.ohms} ohms, {r2.ohms} ohms, and {r3.ohms} ohms. Find the power dissipated by the {r3.ohms}-ohm resistor."""
        self.answer = f"""Power dissipated by the {r3.ohms}-ohm resistor = {p3.W} W"""

class johnbird_5_5:
    def __init__(self):
        vt = c.voltage(ran.main(24))
        it = c.current(ran.main(3))
        r1 = c.resistance(ran.main(2))
        time = c.time(ran.main(2),'hours')

        rt = c.resistance(vt.V / it.A)
        r2 = c.resistance( rt.ohms - r1.ohms )

        energy = c.energy( vt.V * it.A * time.s )

        self.question = f"""Two resistors are connected in series across a {vt.V} V supply and a current of {it.A} A flows in the circuit. One of the resistors has a resistance of {r1.ohms} ohms. If the circuit is connected for {time.hours} hours, how much energy is used?"""
        self.answer = f"""Energy used = {energy.kWh} kWh"""

class johnbird_5_7:
    def __init__(self):
        r1 = c.resistance(ran.main(3))
        r2 = c.resistance(ran.main(6))
        rt = r1.parallel(r2)
        vt = c.voltage(ran.main(12))
        i1 = c.current(vt.V / rt.ohms)


        self.question = f"""Two resistors, of resistance {r1.ohms} ohms and {r2.ohms} ohms, are connected in parallel across a battery having a voltage of {vt.V} V. Determine the current flowing in the {r1.ohms}-ohm resistor."""
        self.answer = f"""Current in the {r1.ohms}-ohm resistance = {i1.A} A"""

class johnbird_5_13:
    def __init__(self):
        r1 = c.resistance(15)
        r2 = c.resistance(10)
        r3 = c.resistance(38)
        r4 = c.resistance(int(ran.main(38)))

        ra = r1.parallel(r2)
        rb = r3.parallel(r4)
        rt = ra.series(rb)

        vt = c.voltage(250)

        pt = c.power(vt.V**2 / rt.ohms)

        self.question = f"""For the circuit shown https://lesliecaminadecom.files.wordpress.com/2019/09/2019_09_26_15_30_02.png calculate the value of resistor Rx such that the total power dissipated in the circuit is {pt.kW} kW"""
        self.answer = f"""Rx = {r4.ohms} ohms"""

class johnbird_5_16:
    def __init__(self):
        rt = c.resistance(ran.main(150))
        r1 = c.resistance(rt.ohms * 3)

        self.question = f"""If three identical lamps are connected in parallel and the combined resistance is {rt.ohms} ohms, find the resistance of one lamp."""
        self.answer = f"""Resistance of one lamp = {r1.ohms} ohms"""

class johnbird_5_17:
    def __init__ (self):
        vt = c.voltage(ran.main(150))
        v1 = c.voltage(vt.V / 3)

        self.question = f"""Three identical lamps A, B and C are connected in series across a {vt.V} V supply. State the voltage of each lamp."""
        self.answer = f"""Voltage of each lamp = {v1.V} V"""

class johnbird_6_1_a:
    def __init__(self):
        c1 = c.capacitance(ran.main(4), 'uF')
        q1 = c.charge(ran.main(5), 'mC')
        v1 = c.voltage( q1.C / c1.F )
        self.question = f"""Determine the potential difference across a {c1.uF} uF capacitor when charged with {q1.mC} mC."""
        self.answer = f"""Potential difference = {v1.V} V"""

class johnbird_6_1_b:
    def __init__(self):
        c1 = c.capacitance(ran.main(50), 'pF')
        v1 = c.voltage(ran.main(2), 'kV')
        q1 = c.charge(c1.F * v1.V)

        self.question = f"""Find the charge on a {c1.pF} pF capacitor when the voltage applied to it is {v1.kV} kV"""
        self.answer = f"""Charge = {q1.uC} uC"""

class johnbird_6_2:
    def __init__(self):
        i1 = c.current(ran.main(4))
        c1 = c.capacitance(ran.main(20), 'uF')
        t1 = c.time(ran.main(3), 'ms')
        q1 = c.charge(i1.A * t1.s)
        v1 = c.voltage(q1.C / c1.F)

        self.question = f"""A direct current of {i1.A} A flows into a previously uncharged {c1.uF} uF capacitor for {t1.ms} ms. Determine the potential difference between the plates."""
        self.answer = f"""Potential difference = {v1.V} V"""


class johnbird_6_3:
    def __init__(self):
        c1 = c.capacitance(ran.main(5), 'uF')
        v1 = c.voltage(ran.main(800), 'V')
        i1 = c.current(ran.main(2), 'mA')
        q1 = c.charge( c1.F * v1.V )
        t1 = c.time( q1.C / i1.A )

        self.question = f"""A {c1.uF} uF capacitor is charged so that the potential difference between its plates is {v1.V} V. Calculate how long the capacitor can provide an average discharge current of {i1.mA} mA."""
        self.answer = f"""Discharge time = {t1.s} s"""

class johnbird_6_4:
    def __init__(self):
        length = c.length(ran.main(20), 'cm')
        width = c.length(ran.main(20), 'cm')
        area = c.area(length.m * width.m)
        charge = c.charge(ran.main(0.2), 'uC')
        spacing = c.length(ran.main(5), 'mm')
        voltage = c.voltage(ran.main(0.25), 'kV')
        fluxdensity = c.electricFluxDensity(charge.C / area.m2)
        electricfield = c.electricField(voltage.V / spacing.m)
        
        self.question = f"""Two parallel rectangular plates measuring {length.cm} cm by {width.cm} cm carry an electric charge of {charge.uC} uC. Calculate the electric flux density. If the plates are spaced {spacing.mm} mm apart and the voltage between them is {voltage.kV} kV, determine the electric field strength."""
        self.answer = f"""Electric Field Strength = {electricfield.kVperm} kV/m"""

class johnbird_6_5:
    def __init__(self):
        er = ran.main(5)
        fluxdensity = c.electricFluxDensity(ran.main(2), 'uCperm2')
        electricfield = c.electricField(fluxdensity.Cperm2 / (c.PERMITTIVITY_OF_FREE_SPACE * er))
        self.question = f"""The flux density between two plates separated by mica of relative permittivity {er} is {fluxdensity.uCperm2} uC/m2. Find the voltage gradient between the plates."""
        self.answer = f"""Voltage Gradient = {electricfield.kVperm} kV/m"""

class johnbird_6_6:
    def __init__(self):
        er = 2.3
        v1 = c.voltage(ran.main(200))
        spacing = c.length(ran.main(0.8), 'mm')
        electricfield = c.electricField(v1.V / spacing.m)
        self.question = f"""Two parallel plates having a potential difference of {v1.V} V between them are spaced {spacing.mm} mm apart. Find the electric flux density when the dielectric between the plates is polyethelyne of relative permittivity {er}."""
        self.answer = f"""Electric Field strength = {electricfield.kVperm} kV/m"""

class johnbird_6_7:
    def __init__(self):
        area = c.area(ran.main(4), 'cm2')
        spacing = c.length(ran.main(0.1),'mm')
        er = 100
        charge = c.charge(ran.main(1.2), 'uC')
        capacitance = c.capacitance(c.PERMITTIVITY_OF_FREE_SPACE * er * area.m2 / spacing.m )
        voltage = c.voltage( charge.C / capacitance.F )

        self.question = f"""A ceramic capacitor has an effective plate area of {area.cm2} cm2 separated by {spacing.mm} mm of ceramic of relative permittivity of {er}. If this capacitor is given a charge of {charge.uC} uC what will be the potential difference between the plates?"""
        self.answer = f"""Potential difference between plates = {voltage.V} V"""

class johnbird_6_8:
    def __init__(self):
        area = c.area(ran.main(800), 'cm2')
        capacitance = c.capacitance(ran.main(4425), 'pF')
        er = 2.5
        spacing = c.length(c.PERMITTIVITY_OF_FREE_SPACE * er * area.m2 / capacitance.F)

        self.question = f"""A waxed paper capacitor has two parallel plates, each of effective area {area.cm2} cm2. If the capacitance of the capacitor is {capacitance.pF} pF determine the effective thickness of the paper if its    relative permittivity is {er}."""
        self.answer = f"""Paper thickness = {spacing.mm} mm"""

class johnbird_6_9:
    def __init__(self):
        length = c.length(ran.main(75), 'mm')
        width = c.length(ran.main(75), 'mm')
        spacing = c.length(ran.main(0.2), 'mm')
        er = 5
        capacitance = c.capacitance(c.PERMITTIVITY_OF_FREE_SPACE * er * area.m2 * 18 / spacing.m)



        self.question = f"""A parallel plate capacitor has nineteen interleaved plates each {length.mm} mm by {width.mm} mm separated by mica sheets {spacing.mm} thick. Assuming the relative permittivity of the mica is {er}, calculate the capacitance of the capacitor."""
        self.answer = f"""Capacitance = {capacitance.nF} nF"""


class johnbird_6_10:
    def __init__(self):
        c1 = c.capacitance(ran.main(6), 'uF')
        c2 = c.capacitance(ran.main(4), 'uF')
        c3 = c1.series(c2)

        self.question = f"""Calculate the equivalent capacitance of two capacitors of {c1.uF} uF and {c2.uF} uF connected in series."""
        self.answer = f"""Equivalent capacitance = {c3.uF} uF"""

class johnbird_6_11:
    def __init__(self):
        c1 = c.capacitance(ran.main(30), 'uF')
        c2 = c.capacitance(ran.main(20), 'uF')
        c3 = c1.series(c2)
        self.question = f"""What capacitance must be connected in series with a {c1.uF} uF capacitor for the equivalent capacitance to be {c3.uF} uF?"""
        self.answer = f"""Capacitance = {c2.uF} uF"""

class johnbird_6_12:
    def __init__(self):
        c1 = c.capacitance(ran.main(1), 'uF')
        c2 = c.capacitance(ran.main(3), 'uF')
        c3 = c.capacitance(ran.main(5), 'uF')
        c4 = c.capacitance(ran.main(6), 'uF')
        ct = c1.parallel(c2).parallel(c3).parallel(c4)
        qt = c.charge(ct.F * vt.V)

        self.question = f"""Capacitances of {c1.uF} uF, {c2.uF} uF, {c3.uF} uF, and {c4.uF} uF are connected in parallel to a direct voltage supply of {vt.V} V. Determine the total charge."""
        self.answer = f"""Total charge = {qt.mC} mC"""

class johnbird_6_13:
    def __init__(self):
        c1 = c.capacitance(ran.main(3), 'uF')
        c2 = c.capacitance(ran.main(6), 'uF')
        c3 = c.capacitance(ran.main(12), 'uF')
        ct = c1.series(c2).series(c3)
        vt = c.voltage(ran.main(350))
        qt = c.charge(ct.F * vt.V)
        v1 = c.voltage(qt.C / c1.F)
        self.question = f"""Capacitance's of {c1.uF} uF, {c2.uF} uF, and {c3.uF} uF are connected in series across a {vt.V} V supply. Calculate the voltage across the {c1.uF}-uF capacitor."""
        self.answer = f"""Voltage across the {c1.uF}-uF capacitor = {v1.V} V"""

class johnbird_6_15:
    def __init__(self):
        c1 = c.capacitance(ran.main(0.2), 'uF')
        v1 = c.voltage(ran.main(1.25), 'kV')
        sf = random.randint(2,4)
        electricfield = c.electricField(ran.main(50), 'MVperm')
        er = 6
        mica_thickness = c.length( v1.V  / electricfield.Vperm)
        area = c.area( c1.F * mica_thickness.m / (c.PERMITTIVITY_OF_FREE_SPACE * er))
        self.question = f"""A capacitor is to be constructed so that its capacitance is {c1.uF} uF and to take a potential difference of {v1.kV} kV across its terminals. The dielectric is to be mica which, after allowing a safety factor of {sf}, has a dielectric strength of {electricfield.MVperm} MV/m. Find the area of the plate assuming a two-plate construction. (Assume er for mica to be {er})"""
        self.answer = f"""Area of the plate = {area.cm2} cm2"""

class johnbird_6_16:
    def __init__(self):
        time = c.time(ran.main(10), 'us')
        c1 = c.capacitance(ran.main(3), 'uF')
        v1 = c.capacitance(ran.main(400))
        energy = c.energy( 0.5 * c1.F * v1.V**2 )
        power = c.power( energy.J / time.s )
        self.question = f"""Determine the average power for a capacitor delivering its energy in a time of {time.us} us, if the capacitor has a capacitance of {c1.uF} uF and charged to {v1.V} V"""
        self.answer = f"""Power = {power.kW} kW"""

class johnbird_6_17:
    def __init__(self):
        capacitance = c.capacitance(ran.main(12),'uF')
        energy = c.energy(ran.main(4))
        voltage = c.voltage( math.sqrt(2 * energy.J / capacitance.C ))

        self.question = f"""A {capacitance.uF} uF capacitor is required to store {energy.J} J of energy. Find the potential difference to which the capacitor must be charged."""
        self.answer = f"""Potential difference = {voltage.V} V"""

class johnbird_6_18:
    def __init__(self):
        charge = c.charge(ran.main(10), 'mC')
        energy = c.energy(ran.main(1.2), 'J')
        voltage = c.voltage( 2 * energy.J / charge.C )
        capacitance = c.capacitance( charge.C / voltage.V )

        self.question = f"""A capacitor is charged with {charge.mC} mC. If the energy stored is {energy.J} J, find the capacitance."""
        self.answer = f"""Capacitance = {capacitance.uF} uF"""

class johnbird_7_1:
    def __init__(self):
        length = c.length(ran.main(200), 'mm')
        width = c.width(ran.main(100), 'mm')
        flux = c.magneticFlux(ran.main(150), 'uWb')
        area = c.area(length.m * width.m)
        fluxdensity = c.magneticFluxDensity(flux.Wb / area.m2)

        self.question = f"""A magnetic pole face has a rectangular section having dimensions {length.mm} mm by {width.mm} mm. If the total flux emerging from the pole is {magneticFlux.uWb} uWb, calculate the flux density."""
        self.answer = f"""Flux density = {fluxdensity.mT} mT"""

class johnbird_7_2:
    def __init__(self):
        magneticfluxdensity = c.magneticFluxDensity(ran.main(1.8))
        flux = c.magneticFlux(ran.main(353), 'mWb')
        area = c.area(flux.Wb / magneticfluxdensity.T )
        radius = c.length(math.sqrt(area.m2 / math.pi))

        self.question = f"""The maximum working flux density of a lifting electromagnet is {magneticfluxdensity.T} and the effective area of the pole face is circular in cross-section. If the total magnetic flux produced is {flux.mWb} mWb, determine the radius of the pole face."""
        self.answer = f"""Radius = {radius.mm} mm"""

class johnbird_7_3:
    def __init__(self):
        H = c.magnetizingForce(ran.main(8000), 'Aperm')
        diameter = c.length(ran.main(30), 'cm')
        turns = int(ran.main(750))
        length = c.length( math.pi * diameter.m )
        current = c.current(H.Aperm * length.m / turns)

        self.question = f"""A magnetising force of {H.Aperm} A/m is applied to a circular magnetic circuit of mean diameter {diameter.cm} cm by passing a curent through a coil wound on the circuit. If the coil is uniformly wound around the circuit and has {turns} turns, find the current in the coil."""
        self.answer = f"""Current = {current.A} A"""

class johnbird_7_4:
    def __init__(self):
        B = c.magneticFluxDensity(ran.main(1.2), 'T')
        H = c.magnetizingForce(ran.main(1250), 'Aperm')
        ur = B.T / (c.PERMEABILITY_OF_FREE_SPACE * H.Aperm)
        self.question = f"""A flux density of {B.T} T is produced in a piece of cast steel by a magnetizing force of {H.Aperm}. Find the relative permeability of the steel under these conditions."""
        self.answer = f"""Relative permeability = {ur}"""

class johnbird_7_5:
    def __init__(self):
        B = c.magneticFieldDensity(ran.main(0.25), 'T')
        airgap = c.length(ran.main(12), 'mm')
        H = c.magnetizingForce(B.T / c.PERMEABILITY_OF_FREE_SPACE)

        self.question = f"""Determine the magnetic field strength and the mmf required to produce a flux density of {B.T} T in an air gap of length {airgap.mm} mm"""
        self.answer = f"""Magnetomotive force = {H.Aperm} A/m"""

class johnbird_7_6:
    def __init__(self):
        turns = ran.main(300)
        circumference = c.length(ran.main(40), 'cm')
        area = c.area(ran.main(4), 'cm2')
        current = c.current(ran.main(5))
        H = c.magnetizingForce( turns * current.A / circumference.m )
        B = c.magneticFluxDensity( c.PERMEABILITY_OF_FREE_SPACE * H.Aperm )
        flux = c.magneticFlux( B.T * area.m2 )

        self.question = f"""A coil of {turns} turns is wound uniformly on a ring of non-magnetic material. The ring has a mean circumference of {circumference.cm} cm and a uniform cross-sectional area of {area.cm2} cm2. If the current in the coil is {current.A} A, calculate the total magnetic flux in the ring."""
        self.answer = f"""Flux = {flux.uWb} uWb"""

class johnbird_7_7:
    def __init__(self):
        diameter = c.length(ran.main(10), 'cm')
        turns = int(ran.main(2000))
        current = c.current(ran.main(0.25))
        fluxdensity = c.magnecticFluxDensity(ran.main(0.4))
        length = c.length( math.pi * diameter.m )
        H = c.magnetizingForce( turns * current.A / length.m )
        ur = fluxdensity.T / (c.PERMEABILITY_OF_FREE_SPACE * H.Aperm)

        self.question = f"""An iron ring of mean diameter {diameter.cm} cm is uniformly wound with {turns} turns of wire. When a current of {current.A} A is passed through a coil a flux density of {fluxdensity.T} T is set up in the iron. Find the relative permeability of the iron under these conditions."""
        self.answer = f"""Relative permeability = {ur}"""

class johnbird_7_8:
    def __init__(self):
        length = c.length(ran.main(150), 'mm')
        area = c.area(ran.main(1800), 'mm2')
        ur = int(ran.main(4000))
        reluctance = c.reluctance(length.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area.m2))

        self.question = f"""Determine the reluctance of a piece of mumetal of length {length.mm} mm and cross-sectional area of {area.mm2} mm2 when the relative permeability is {ur}."""
        self.answer = f"""Reluctance = {reluctance.perH} /H"""

class johnbird_7_9:
    def __init__(self):
        radius = c.length(ran.main(50), 'mm')
        area = c.area(ran.main(400), 'mm2')
        current = c.current(ran.main(0.5))
        flux = c.magneticFlux(ran.main(0.1), 'mWb')
        ur = int(ran.main(200))
        length = c.length( math.pi * 2 * radius.m )
        reluctance = c.reluctance( length.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area.m2))
        turns = reluctance.perH * flux.Wb / current.A

        self.question = f"""A mild steel ring has a radius of {radius.mm} mm and a cross-sectional area of {area.mm2} mm2. A current flows in a coil wound uniformly around the ring and the flux produced is {flux.mWb} mWb. If the relative permeability at this value of current is {ur} find the number of turns in the coil."""
        self.answer = f"""Number of turns = {turns}"""

class johnbird_7_10:
    def __init__(self):
        ur = 750
        length1 = c.length(ran.main(6), 'cm')
        area1 = c.area(ran.main(1), 'cm2')
        length2 = c.length(ran.main(2), 'cm')
        area2 = c.area(ran.main(0.5), 'cm2')
        turns = int(ran.main(200))
        current = c.current(ran.main(0.4))

        reluctance1 = c.reluctance(length1.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area1.m2))
        reluctance2 = c.reluctance(length2.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area2.m2))
        reluctance_total = c.reluctance(reluctance1.perH + reluctance2.perH)
        flux = c.magneticFlux(turns * current.A / reluctance_total.perH)
        fluxdensity = c.magneticFluxDensity(flux.Wb / area.m2)

        self.question = f"""A closed magnetic circuit of cast steel contains a {length1.cm} cm long path of cross sectional area {area1.cm2} cm2 and a {length2.cm} cm path of cross-sectional area {area.cm2} cm2. A coil of {turns} turns is wound around the {length1.cm} cm length of the circuit and a current of {current.A} A flows. Determine the flux density in the {length2.cm} cm path if the relative permeabilty of cast steel is {ur}.""" 
        self.answer = f"""Flux Density = {fluxdensity.T} T"""

class johnbird_7_11:
    def __init__(self):
        radius = c.length(ran.main(50), 'mm')
        length = c.length(2 * math.pi * radius.m)
        area = c.area(ran.main(400), 'mm2')
        current = c.current(ran.main(0.5))
        flux = c.magneticFlux(ran.main(0.1), 'mWb')
        ur = int(ran.main(200))
        reluctance = c.reluctance(length.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area.m2))
        turns = reluctance.perH * flux.Wb / current.A

        self.question = f"""A mild steel ring has a radius of {radius.mm} mm and a cross-sectional area of {area.mm2} mm2. A current of {current.A} A flows in a coil wound uniformly around the ring and the flux produced is {flux.mWb} mWb. If the relative permeability at this value of current is {ur} find the number of turns in the coil."""
        self.answer = f"""Number of turns = {turns} """

class johnbird_7_12:
    def __init__(self):
        length1 = c.length(ran.main(6), 'cm')
        length2 = c.length(ran.main(2), 'cm')
        area1 = c.area(ran.main(1), 'cm2')
        area2 = c.area(ran.main(0.5), 'cm2')
        turns = int(ran.main(200))
        ur = 750
        current = c.current(ran.main(0.4), 'A')

        reluctance1 = c.reluctance(length1.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area1.m2))
        reluctance2 = c.reluctance(length2.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area2.m2))
        reluctance_total = c.reluctance( reluctance1.perH + reluctance2.perH)
        flux = c.magneticFlux( turns * current.A / reluctance_total.perH)
        fluxdensity = c.magneticFluxDensity( flux.Wb / area.m2 )


        self.question = f"""A closed magnetic circuit of cast steel contains a {length1.cm} cm long path of cross-sectional area {area1.cm2} cm2 and a {length2.cm} cm path of cross-sectional area {area2.cm2} cm2. A coil of {turns} is wound around the {length1.cm} cm length of the circuit and a current of {current.A} A flows. Determine the flux density in the {length2.cm} cm path if the relative permeability of cast steel is {ur}."""

        self.answer = f"""Flux density = {fluxdensity.T} T"""

class johnbird_8_2:
    def __init__(self):
        current = c.current(ran.main(20))
        fluxdensity = c.magneticFluxDensity(ran.main(0.9))
        length = c.length(ran.main(30), 'cm')
        
        not_ok = True
        while not_ok:
            angle = c.angle(ran.main(30), 'degrees')
            if 20 < angle.degrees < 40:
                not_ok = False

        force = c.force( fluxdensity.T * current.A * length.m * math.cos(angle.radians))



        self.question = f"""A conductor carries a current of {current.A} A and is in to a magnetic field having a flux density of {fluxdensity.T} T. If the length of the conductor in the field is {length.cm} cm, determine the value of the force if the conductor is inclined at angle of {angle.degrees} degrees."""

        self.answer = f"""Force = {force.N} N"""

class johnbird_8_3:
    def __init__(self):
        length = c.length(ran.main(400), 'mm')
        fluxdensity = c.magneticFluxDensity(ran.main(1.2))
        force = c.force(ran.main(1.92))
        current = c.current(force.N / (fluxdensity.T * length.m))

        self.answer = f"""Current = {current.A} A"""
        self.question = f"""Determine the current required in a {length.mm} mm length of conductor of an electric motor, when the conductor is situated at right-angles to a magnetic field of flux density {fluxdensity.T} T, if a force of {force.N} N is to be exerted on the conductor."""

class johnbird_8_4:
    def __init__(self):
        length = c.length(ran.main(350), 'mm')
        current = c.current(ran.main(10), 'A')
        radius = c.length(ran.main(60), 'mm')
        flux = c.magneticFluxDensity(ran.main(0.5), 'mWb')
        area = c.area(math.pi * radius.m**2)
        force = c.force( flux.Wb * current.A * length.m / area.m2)
        self.question = f"""A conductor {length.mm} mm long carries a current of {current.A} A and is at right-angles to a magnetic field lying between two circular pole faces each of radius {radius.mm} mm. If the total flux between the pole faces is {flux.mWb} mWb, calculate the magnitude of the force exerted on the conductor."""
        self.answer = f"""Force = {force.N} N"""

class johnbird_8_6:
    def __init__(self):
        length = c.length(ran.main(30), 'mm')
        width = c.length(ran.main(24), 'mm')
        fluxdensity = c.magneticFluxDensity(ran.main(0.8))
        current = c.current(ran.main(50), 'mA')
        turns = int(ran.main(300))
        force = c.force( turns * fluxdensity.T * current.A * length.m )
        self.answer = f"""Force = {force.N} N"""
        self.question = f"""A coil is wound on a rectangular former of width {width.mm} mm and length {length.mm} mm. The force is pivoted about an axis passing through the middle of the two shorter sides and is placed in a uniform magnetic field of flux density {fluxdensity.T} T, the axis being perpendicular to the field. If the coil carrier a current of {current.mA} mA, determine the force on each coil side for a coil wound with {turns} turns."""

class johnbird_8_7:
    def __init__(self):
        fluxdensity = c.magneticFluxDensity(ran.main(18.5), 'uT')
        force = c.force(c.CHARGE_ELECTRON * c.SPEED_OF_LIGHT * fluxdensity.T )
        self.answer = f"""Force = {force.N} N"""
        self.question = f"""An electron in a television tube has a charge of {c.CHARGE_ELECTRON} coulombs and travels at {c.SPEED_OF_LIGHT} m/s perpendicular to a field of flux density {fluxdensity.uT} uT. Determine the force exerted on the electron in the field."""

class johnbird_9_1:
    def __init__(self):
        length = c.length(ran.main(300), 'mm')
        speed = c.velocity(ran.main(4), 'mpers')
        fluxdensity = c.magneticFluxDensity(ran.main(1.25), 'T')
        resistance = c.resistance(ran.main(20))
        voltage = c.voltage( fluxdensity.T * length.m * velocity.mpers )
        current = c.current( voltage.V / resistance.ohms )

        self.question = f"""A conductor {length.mm} mm long moves at a uniform speed of {speed.mpers} m/s at right angles to a uniform magnetic field of flux density {fluxdensity.T} T. Determine the current flowing in the conductor when its ends are connected to a load of {resistance.ohms} ohms resistance."""
        self.answer = f"""Current = {current.mA} mA"""

class johnbird_9_2:
    def __init__(self):
        length = c.length(ran.main(75), 'mm')
        fluxdensity = c.magneticFluxDensity(ran.main(0.6))
        voltage = c.voltage(ran.main(9))
        velocity = c.velocity( voltage.V / (fluxdensity.T * length.m))
        self.answer = f"""Velocity = {velocity.mpers} m/s"""
        self.question = f"""At what velocity must a conductor {length.mm} mm long cut a magnetic field of flux density {fluxdensity.T} if an emf of {voltage.V} V is to be induced in it? Assume the conductor, the field and the direction of motion are mutually perpendicular."""

class johnbird_9_3:
    def __init__(self):
        velocity = c.velocity(ran.main(15))
        regen = True
        while regen:
            angle = c.angle(ran.main(60), 'degrees')
            if 20 < angle.degrees < 80:
                regen = False
        flux  = c.magneticFlux(ran.main(5), 'uWb')
        sidelength = c.length(ran.main(2), 'cm')
        area = c.area(sidelength.m**2)
        voltage = c.voltage( flux.Wb * sidelength.m * velocity.mpers * math.sin(angle.radians) / area.m2 )
        self.answer = f"""Voltage = {voltage.mV} mV"""
        self.question = f"""A conductor moves with a velocity of {velocity.mpers} m/s at an angle of {angle.degrees} degrees to a magnetic field produced between two square-faced pole of side length {sidelength.cm} cm. If the flux leaving a pole face is {flux.uWb} uWb, find the magnitude of the induced emf in each case."""

class johnbird_9_4:
    def __init__(self):
        wingspan = c.length(ran.main(36), 'm')
        velocity = c.velocity(ran.main(400), 'kmperh')
        fluxdensity = c.magneticFluxDensity(ran.main(40), 'uT')
        voltage = c.voltage( fluxdensity.T * wingspan.m * velocity.mpers)
        self.answer = f"""Voltage = {voltage.V} V"""
        self.question = f"""The wing span of a metal aeroplane is {wingspan.m} m. If the aeroplane is flying at {velocity.kmperh} km/h, determine the emf induced between its wing tips. Assume the vertical component of the earth's magnetic field is {fluxdensity.uT} uT"""

class johnbird_9_6:
    def __init__(self):
        width = c.length(ran.main(8), 'cm')
        length = c.length(width.cm + ran.main(4), 'cm')
        fluxdensity = c.magneticFluxDensity(ran.main(1.4), 'T')
        turns = int(ran.main(80))
        speed = c.angularVelocity(ran.main(1200), 'revpermin')
        linearspeed = c.velocity( radius.m * speed.radpers)
        voltage = c.voltage(2 * turns * fluxdensity.T * length.m * linearspeed.mpers)
        self.question = f"""A rectangular coil of sides {length.cm} cm and {width.cm} cm is rotated in a magnetic field of flux density {fluxdensity.T} T, the longer side of the coil actually cutting this flux. The coil is made up of {turns}  and rotates at {speed.revpermin} rev/min. Calculate the maximum generated emf."""
        self.answer = f"""Voltage = {voltage.V} V"""

class johnbird_9_7:
    def __init__(self):
        turns = int(ran.main(200))
        flux = c.magneticFlux(ran.main(25), 'mWb')
        time = c.time(ran.main(50), 'ms')
        voltage = c.voltage( - turns * flux.Wb / time.s )
        self.answer = f"""Voltage = {voltage.V} V"""
        self.question = f"""Determine the emf induced in a coil of {turns} turns when there is a change of flux of {flux.mWb} mWb linking with it in {time.ms} ms."""

class johnbird_9_8:
    def __init__(self):
        flux = c.magneticFlux(ran.main(400), 'uWb')
        turns = int(ran.main(150))
        time = c.time(ran.main(40), 'ms')
        voltage = c.voltage( - turns * 2 * flux.Wb / time.s)
        self.answer = f"""Voltage = {voltage.V} V"""
        self.questions = f"""A flux of {flux.uWb} uWb passing through a {turns}-turn coil is reversed in {time.ms} ms. Find the average emf induced."""

class johnbird_9_9:
    def __init__(self):
        inductance = c.inductance(ran.main(12))
        current = c.current(ran.main(4))
        voltage = c.voltage( - inductance.H * current.A )
        self.answer = f"""Voltage = {voltage.V} V"""
        self.question = f"""Calculate the emf induced in a coil of inductance {inductance.H} H by a current changing at the rate of {current.A} A/s."""

class johnbird_9_10:
    def __init__(self):
        voltage = c.voltage(ran.main(1.5), 'kV')
        current = c.current(ran.main(4))
        time = c.time(ran.main(8), 'ms')
        inductance = c.inductance( voltage.V / (current.A / time.s))
        self.answer = f"""Inductance = {inductance.H} H"""
        self.question = f"""An emf of {voltage.kV} kV is induced in a coil when a current of {current.A} A collapses uniformly to zero in {time.ms} ms. Determine the inductance of the coil."""

class johnbird_9_11:
    def __init__(self):
        voltage = c.voltage(ran.main(40))
        inductance = c.inductance(ran.main(150), 'mH')
        current = c.current(ran.main(6))
        time = c.time( inductance.H * current.A / voltage.V )
        self.answer = f"""Time = {time.ms} ms"""
        self.question = f"""An average emf of {voltage.V} V is induced in a coil of inductance {inductance.mH} mH when a current of {current.A} A is reversed. Calculate the time taken for the current to reverse."""

class johnbird_9_12:
    def __init__(self):
        inductance = c.inductance(ran.main(8))
        current = c.current(ran.main(3))
        energy = c.energy( 0.5 * inductance.H * current.A**2 )
        self.answer = f"""Energy = {energy.J} J"""
        self.question = f"""An {inductance.H} H inductor has a current of {current.A} A flowing through it. How much energy is stored in the magnetic field of the inductor?"""

class johnbird_9_13:
    def __init__(self):
        current = c.current(ran.main(4))
        turns = int(ran.main(800))
        flux = c.magneticFlux(ran.main(5), 'mWb')
        inductance = c.inductance( turns * flux.Wb / current.A )
        self.answer = f"""Inductance = {inductance.H} H"""
        self.question = f"""Calculate the coil inductance when a current of {current.A} A in a coil of {turns} turns produces a flux of {flux.mWb} mWb."""

class johnbird_9_14:
    def __init__(self):
        flux = c.magneticFlux(ran.main(25), 'mWb')
        turns = int(ran.main(1500))
        current = c.current(ran.main(3))
        time = c.time(ran.main(150), 'ms')
        inductance = c.inductance( turns * flux.Wb / current.A )
        voltage = c.voltage( - inductance.H * current.A / time.s)
        self.answer = f"""Voltage = {voltage.V} V"""
        self.question = f"""A flux of {flux.mWb} mWb links with a {turns}-turn coil when a current of {current.A} A passes through the coil. Calculate the average emf induced in the current falls to zero in {time.ms} ms"""

class johnbird_9_15:
    def __init__(self):
        current = c.current(ran.main(1.5), 'A')
        flux = c.magneticFlux(ran.main(90), 'uWb')
        inductance = c.inductance(ran.main(0.60), 'H')
        turns = inductance.H * current.A / flux.Wb
        self.answer = f"""Number of turns = {turns}"""
        self.question = f"""When a current of {current.A} A flows in a coil the flux linking with the coil is {flux.uWb} uWb. If the coil inductance is {inductance.H} H, calculate the number of turns of the coil."""

class johnbird_9_16:
    def __init__(self):
        turns = int(ran.main(750))
        inductance = c.inductance(ran.main(3))
        current = c.current(ran.main(2))
        time = c.time(ran.main(20), 'ms')
        flux = c.magneticFlux( inductance.H * current.A / turns )
        voltage = c.voltage( - inductance.H * current.A / time.s )
        self.answer = f"""Voltage = {voltage.V} V"""
        self.question = f"""A {turns} turn coil of inductance {inductance.H} H carries a current of {current.A} A. Calculate the flux linking the coil and the emf induced in the coil when the current collapses to zero in {time.ms} ms"""

class johnbird_9_17:
    def __init__(self):
        turns = int(ran.main(800))
        diameter = c.length(ran.main(120), 'mm')
        area = c.area(ran.main(400), 'mm2')
        current = c.current(ran.main(0.5), 'A')
        ur = int(ran.main(3000))
        time = c.time(ran.main(80), 'ms')
        reluctance = c.reluctance( math.pi * diameter.m / (c.PERMEABILITY_OF_FREE_SPACE * ur * area.m2))
        inductance = c.indutance( turns**2 / reluctance.perH )
        voltage = c.voltage( - inductance.H * current.A / time.s )
        self.answer = f"""Induced emf = {voltage.V} V"""
        self.question = f"""A silicon iron ring is wound with {turns} turns, the ring having a mean diameter of {diameter.mm} mm and a cross sectional area of {area.mm2} mm2. If when carrying a current of {current.A} A the relative permeability is found to be {ur} , calculate the induced emf if the current is reduced to zero in {time.ms} ms."""

class johnbird_9_18:
    def __init__(self):
        current = c.current(ran.main(200))
        voltage = c.voltage(ran.main(1.5))
        M = c.inductance( voltage.V / current.A )
        self.answer = f"""Mutual inductance = {M.mH} mH"""
        self.question = f"""Calculate the mutual inductance between two coils when a current changing at {current.A} A/s in one coil induces an emf of {voltage.V} V in the other."""

class johnbird_9_19:
    def __init__(self):
        inductance = c.inductance(ran.main(18), 'mH')
        voltage = c.voltage(ran.main(0.72))
        didt = c.current( voltage.V / inductance.H )
        self.answer = f"""Rate of change of current = {didt.A} A/s"""
        self.question = f"""The mutual inductance between two coils is {inductance.mH} mH. Calculate the steady rate of change of current in one coil to induce an emf of {voltage.V} V in the other."""

class johnbird_9_20:
    def __init__(self):
        inductance = c.inductance(ran.main(0.2))
        current2 = c.current(ran.main(4))
        current1 = c.current(current2.A + ran.main(6))
        time = c.time(ran.main(10), 'ms')
        turns = int(ran.main(500))
        voltage = c.voltage( - inductance.H * (current1.A - current2.A) / time.s)
        fluxchange = c.magneticFlux( math.abs(voltage.V ) * time.s / turns)
        self.answer = f"""Flux change = {fluxchange.mWb} mWb"""
        self.question = f"""Two coils have a mutual inductance of {inductance.H} H. If the current in one coil is changed from {current1.A} A to {current2.A} A in {time.ms} ms, calculate the change of flux linked with the second coil if it is wound with {turns} turns."""

class johnbird_10_1:
    def __init__(self):
        ia = c.current(ran.main(40), 'mA')
        ra = c.resistance(ran.main(25), 'ohms')
        it = c.current(50)
        rshunt = c.resistance( ia.A * ra.ohms / ( it.A - ia.A))
        self.answer = f"""Shunt resistance = {rshunt.mohms} mohms"""
        self.question = f"""A moving coil instrument gives a fsd when the current is {ia.mA} mA and its resistance is {ra.ohms} ohms. Calculate the value of the shunt to be connected in parallel with the meter to enable it to be used as an ammeter for measuring currents up to {it.A} A"""

class johnbird_10_2:
    def __init__(self):
        vt = c.voltage(100)
        rm = c.resistance(ran.main(10), 'ohms')
        ifsd = c.current(ran.main(8), 'mA')
        rseries = c.resistance( (vt.V - ifsd.A * rm.ohms ) / ifsd.A)
        self.answer = f"""Series resistance = {rseries.kohms} kohms"""
        self.question = f"""A moving-coil instrument having a resistance of {rm.ohms} ohms gives an fsd when the current is {ifsd.mA} mA. Calculate the value of the multiplier to be connected in series with the instrument so that it can be used as a voltmeter for measuring pds up to {vt.V}V"""

class johnbird_10_4:
    def __init__(self):
        regen = True
        while regen:
            ifsd = c.current(ran.main(100), 'mA')
            rm = c.resistance(ran.main(50), 'ohms')
            load_resistance = c.resistance(ran.main(500), 'ohms')
            supply_voltage = c.voltage(int(ran.main(10)))


            meter_reading = c.current( supply_voltage.V / (load_resistance.ohms + rm.ohms))
            if meter_reading.A < ifsd.A:
                regen = False

        self.answer = f"""Meter reading = {meter_reading.mA} mA""" 
        self.question = f"""An ammeter has a fsd of {ifsd.mA} mA and a resistance of {rm.ohms} ohms. The ammeter is used to measure the current in a load of resistance {load_resistance.ohms} ohms when the supply voltage is {supply_voltage.V} V. Calculate the actual current in the circuit."""

class johnbird_10_18:
    def __init__(self):
        rbc = c.resistance( ran.main(100), 'ohms')
        rcd = c.resistance( ran.main(10), 'ohms')
        rda = c.resistance( ran.main(400), 'ohms')
        rx = c.resistance( rbc.ohms * rda.ohms / rcd.ohms )
        self.answer = f"""Unknown resistance = {rx.ohms} ohms"""
        self.question = f"""In a wheatstone bridge ABCD, a galvanometer is connected between A and C, and a battery between B and D. A resistor of unknown value is connected between A and B. When the bridge is balanced, the resistance between B and C is {rbc.ohms} ohms, that between C and D is {rcd.ohms} ohms and that between {rda.ohms} ohms. Calculate the value of the unknown resistance."""

class johnbird_10_19:
    def __init__(self):
        balancelength = c.length(ran.main(400), 'mm')
        vstandard = c.voltage(1.0186)
        length = c.length(balancelength.mm + ran.main(250), 'mm')
        voltage = c.voltage( vstandard.V * (length.mm / balancelength.mm))
        self.answer = f"""Dry cell emf = {voltage.V} V"""
        self.question = f"""In a dc potentiometer, balance is obtained at a length of {length.mm} mm when using a standard cell of {vstandard.V} V. Determine the emf of a dry cell if balance is obtained with length of {balancelength.mm} mm"""

class johnbird_10_20:
    def __init__(self):
        resistance12 = c.resistance(ran.main(400))
        resistance3 = c.resistance(ran.main(5), 'kohms')
        capacitance = c.capacitance(ran.main(7.5), 'uF')
        inductance = c.inductance( resistance12.ohms**2 * capacitance.F )
        resistance = c.resistance( resistance12.ohms**2 / resistance3.ohms )
        self.answer = f"""Inductance and resistance = {inductance.H} H and {resistance.ohms} ohms"""
        self.question = f"""https://lesliecaminadecom.files.wordpress.com/2019/10/2019_10_01_10_10_33.png, For the ac bridge shown in determine the values of the inductance and resistance of the coil when R1 = R2 = {resistance12.ohms} ohms, R3 = {resistance3.kohms} kohms, and C = {capacitance.uF} uF"""

class johnbird_10_21:
    def __init__(self):
        frequency = c.frequency(ran.main(400), 'kHz')
        Q = int(ran.main(100))
        capacitance = c.capacitance(ran.main(400), 'pF')
        inductance = c.inductance( 1 / ( (2 * math.pi * frequency.Hz)**2 * capacitance ))
        resistance = c.resistance( 2 * math.pi * frequency.Hz * inductance.H / Q)

        self.answer = f"""Inductance = {inductance.uH} uH, Resistance = {resistance.ohms} ohms"""
        self.question = f"""When connected to a Q-meter an inductor is made to resonate at {frequency.kHz} kHz. The Q-factor of the circuit is found to be {Q} and the capacitance of the Q-meter capacitor is set to {capacitance.pF} pF. Determine the inductance and the resistance of the inductor."""

class johnbird_10_22:
    def __init__(self):
        resistor = c.resistor( ran.main(5), 'kohms' )
        resistor_tolerance = c.percentage( ran.main(0.4), 'percent')
        current = c.current( ran.main(2.5), 'mA')
        measurement_tolerance = c.percentage( ran.main(0.5), 'percent')
        voltage = c.voltage(resistor.ohms * current.A)
        max_error = c.percentage( resistor_tolerance.percent * measurement_tolerance.percent, 'percent')
        voltage_error = c.voltage( max_error.decimal * voltage.V )
        self.answer  = f"""Voltage = {voltage.V} (+/-) {voltage_error.V} V"""
        self.question = f"""The current flowing through a resistor of {resistor.kohms} kohms (+/-) {resistor_tolerance} % is measured as {current.mA} mA with an accuracy of measurement of (+/-) {measurement_tolerance} %. Determine the nominal value of the voltage across the resistor and its accuracy."""

class johnbird_10_23:
    def __init__(self):
        current = c.current(ran.main(6.25), 'A')
        voltage = c.voltage(ran.main(36.5), 'V')
        error = c.percentage(ran.main(2), 'percent')

        while current.A > 10 or voltage.V > 50:
            current = c.current(ran.main(6.25), 'A')
            voltage = c.voltage(ran.main(36.5), 'V')

        voltage_error = c.voltage( voltage.V * error.decimal )
        current_error = c.current( voltage.V * error.decimal )

        percent_voltage_error = c.percentage( voltage_error.V / voltage.V , 'decimal')
        percent_current_error = c.percentage( current_error.A / current.A , 'decimal')

        percent_resistance_error = c.percentage( percent_voltage_error.percent + percent_current_error.percent, 'percent')
        resistance = c.resistance( voltage.V / current.A)
        resistance_error = c.resistance( resistance.ohms * percent_resistance_error.decimal )

        self.answer = f"""Resistance: {resistance.ohms} (+/-) {resistance_error.ohms} ohms"""
        
        self.question = f"""The current I flowing in a resistor R is measured by a 0-10A ammeter which gives an indication of {current.A} A. The voltage V across the resistor is measured by a 0-50V voltmeter, which gives an indication of {voltage.V} V. Determine the resistance of the resistor, and its accuracy of measurement if both instruments have a limit of error of {error.percent} % of fsd. Neglect any loading effects of the instruments."""

class johnbird_10_24:
    def __init__(self):
        resistance1 = c.resistance(ran.main(1000))
        resistance1_error = c.percentage(ran.main(1), 'percent')
        resistance2 = c.resistance(ran.main(100))
        resistance2_error = c.percentage(ran.main(0.5), 'percent')
        resistance3 = c.resistance(ran.main(432.5))
        resistance3_error = c.percentage(ran.main(0.2), 'percent')

        resistancex = c.resistance(resistance2.ohms * resistance3.ohms / resistance1.ohms )
        max_error = c.percentage(resistance1_error.percent + resistance2_error.percent + resistance3_error.percent )
        resistancex_error = c.resistance( resistancex.ohms * max_error.decimal)

        self.answer = f"""Resistance X  = {resistancex.ohms} (+/-) {resistancex_error.ohms} ohms"""
        self.question = f"""The arms of a Wheatstone bridge ABCD have the following characteristics: AB: R1 = {resistance1.ohms} ohms (+/-) {resistance1_error.percent} %; BC: R2 = {resistance2.ohms} ohms (+/-) {resistance2_error.percent} %; CD: Unknown resistance Rx; DA: R3 = {resistance3.ohms} ohms (+/-) {resistance3_error.percent} %. Determine the value of the unknown resistance and its accuracy of measurement."""
