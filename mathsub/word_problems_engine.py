from generator import random_handler as ran
import sympy
import math
import random
from generator import constants_conversions as c
from num2words import num2words
import fractions
from mathsub import analytic_geometry_engine
import datetime

x, y, z, t = sympy.symbols('x y z t', real = True)#generic variables
MIN_AGE = 5
MAX_AGE = 30

def clock(hour_init, position, ahead):
    #note that positive position means going clockwise, you encounter the hour hand first before the minute hand.
    omega_hour = -0.5 #degrees per minute
    omega_minute = -6 #degrees per minute
    position = abs(position)

    theta_hour = ( hour_init - 3) * 30 #degrees
    #3pm is 0 degrees
    theta_minute = 90
    #12 o'clock marker is 90 degrees
    
    if ahead == 'hour':
        equation = sym.Eq((theta_minute + omega_minute * t) - (theta_hour + omega_hour * t), position)
    if ahead == 'minute':
        equation = sym.Eq((theta_hour + omega_hour * t) - (theta_minute + omega_minute * t), position)

    solution_set = sym.solveset(equation, t)
    solution_list = list(solution_set)
    return solution_list

def pick_age():
    ages = [random.randint(5, 30) * 2,
    random.randint(4, 20) * 3,
    random.randint(1, 15) * 4,
    random.randint(1, 12) * 5]
    return random.choice(ages)

class Ratio():
    def __init__(self):
        fraction_list = [
        [fractions.Fraction(1,2), 'one-half'],
        [fractions.Fraction(1,3), 'one-third'],
        [fractions.Fraction(2,3), 'two-thirds'],
        [fractions.Fraction(3,4), 'three-fourths']
        ]

        ratio = random.choice(fraction_list)
        self.number = ratio[0]
        self.description = ratio[1]

class Factor():
    def __init__(self):
        factor_list = [[2, 'twice'],
        [3, 'thrice'],
        [4, 'four times'],
        [5, 'five times'],
        [6, 'six times'],
        [7, 'seven times']
        ]

        factor =  random.choice(factor_list)
        self.number = factor[0]
        self.description = factor[1]

class Mixture():
    def __init__(self, volume, quantity, concentration):
        self.volume = volume
        self.quantity = quantity
        self.concentration = concentration

    def mix(self, mixture):
        volume = self.volume + mixture.volume
        quantity = self.quantity + mixture.quantity
        concentration = quantity/volume
        return Mixture(volume, quantity, concentration)


def random_time():
    hour = random.randint(0,23)
    minute = random.randint(0,59)
    return datetime.time(hour = hour, minute = minute)

def hour_convert(hours):
    hours_whole = math.floor(hours)
    fractional = hours - hours_whole
    minutes = int(60 * fractional)
    return hours_whole, minutes

    
class rgs_1:
    def __init__(self):
        num1 = random.randint(2,10)
        num2 = random.randint(2,10)
        
        self.question = f"""Twice the sum of two numbers is {2*(num1 + num2)}. The sum of their squares is {num1**2 + num2**2}. What is the product of the two numbers?"""
        self.answer = f"""{num1 * num2}"""

class rgs_2:
    def __init__(self):
        #pick a random odd integer
        regen = True
        while regen:
            num1 = random.randint(2,20)
            while num1%2 == 0:
                #pick again while the number is still even
                num1 = random.randint(2,20)
            num2 = num1 + 2
            num3 = num1 + 4

            difference = 3*num1 - 2*num3
            if difference > 1:
                regen = False

        self.question = f"""Three times the first of the three consecutive odd integers is {num2words(difference)} more than twice the third. Find the third integer"""
        self.answer = f"""{num3}"""

class rgs_4:
    def __init__(self):
        discount = c.percentage(ran.main(20),'percent')
        retail_price = ran.main(225)
        discounted_retail_price = retail_price * ( 1 - discount.decimal )
        discount_wholesale = c.percentage(ran.main(50), 'percent')
        wholesale_price = retail_price / (1 + discount_wholesale.decimal )

        self.question = f"""A merchant marked a certain product for P{discounted_retail_price:,}, which is {discount.percent}% off the normal retail price. If the retail price is {discount_wholesale.percent}% higher than the wholesale price, what is the wholesale price of the product?"""
        self.answer = f"""{wholesale_price:4.4}"""

class rgs_5:
    def __init__(self):
        watch_discounted = ran.main(3500)
        discount = c.percentage(ran.main(30), 'percent')
        original_price = watch_discounted / (1 - discount.decimal)
        selling_price = ran.main(5050)

        if selling_price > original_price:
            desc = "Gain"
            ratio = c.percentage(selling_price / original_price, 'decimal')
        else:
            desc = "Loss"
            ratio = c.percentage((original_price - selling_price)/original_price, 'decimal')

        self.question = f"""A man sold a watch for P{watch_discounted} at a loss of {discount.percent}% on the cost price. Find the corresponding loss or gain if he sold it for P{selling_price}."""
        self.answer = f"""{ratio.percent:4.4}% {desc}"""

# class rgs_6:
#     def __init__(self):
#         hour = random.randint(0, 11)

#         if hour == 0:
#             display_hour = 12
#             next_hour = 1
#         else:
#             display_hour = hour
#             next_hour = display_hour + 1

#         #for the first time
#         if hour <= 3:
#             minute = clock(hour, 90, 'minute')
#         if hour > 3:
#             minute = clock(hour, 90, 'hour')

#         self.question = f"""At what time between {display_hour} and {next_hour} o'clock will the hands of the clock be at right angles for the first time?"""
#         self.answer = f"""Time for first right angle: {display_hour}:{minute}"""

class rgs_8:
    def __init__(self):
        smaller = int(ran.main(19))
        larger = smaller + int(ran.main(5))

        self.question = f"""The difference of the cubes of two positive numbers is {larger**3 - smaller**3} and the cube of their difference is {(larger - smaller)**3}. Find the smaller number."""

        self.answer = f"""{smaller}"""

class rgs_9:
    def __init__(self):
        cats = random.randint(3,5)
        rats = random.randint(3,5)
        minutes = random.randint(3,5)

        cat_rate = (rats/minutes) / cats

        cats_next = int(ran.main(100))
        rats_next = int(ran.main(100))

        time_minutes = (rats_next / (cat_rate * cats_next))

        self.question = f"""{num2words(cats).capitalize()} cats can kill {rats} rats in {minutes} minutes. How many minutes will it take for {cats_next} cats to kill {rats_next}?"""
        self.answer = f"""{time_minutes:4.4} minutes"""

class rgs_10:
    def __init__(self):
        k = random.randint(2,9)
        x = random.randint(2,9)
        y = random.randint(2,9)
        z = random.randint(2,9)
        w = k * x * y / z**2

        x2 = random.randint(2,9)
        y2 = random.randint(2,9)
        z2 = random.randint(2,9)
        w2 = k * x2 * y2 / z2**2

        self.question = f"""If w varies directly as the product of x and y and inversely as the square of z and that w = {w} when x = {x}, y = {y}, and z = {z}. Find w when x = {x2}, y = {y2}, and z = {z2}."""

        self.answer = f"""{w2:4.4}"""

class rgs_11:
    def __init__(self):
        water_speed = int(ran.main(8))
        boat_speed = int(ran.main(40))

        downstream = water_speed + boat_speed
        upstream = boat_speed - water_speed
        speed_ratio = sympy.simplify(sympy.Rational(downstream, upstream))
        time_ratio = sympy.simplify(sympy.Rational(upstream, downstream))

        self.question = f"""A boat takes {time_ratio} as much time to travel downstream than to travel upstream. If the rate of the water current is {water_speed} kph, what is the rate of the of the boat in still water?"""

        self.answer = f"""{boat_speed} kph"""

# class rgs_12:
#     def __init__(self):
#         hour = random.randint(0,11)
#         if hour == 0:
#             display_hour = 12
#         else:
#             display_hour = hour

#         if hour <= 6:
#             minutes = clock(hour, 180, 'minutes')
#         if hour > 6:
#             minutes = clock(hour, 180, 'hour')

#         self.question = f"""How many minutes after {display_hour}:00 o'clock will the hands of the clock be opposite each other for the first time?"""
#         self.answer = f"""Minutes: {minutes}"""

class rgs_13:
    def __init__(self):
        area1 = c.area(ran.main(5), 'mm2')
        resistance1 = c.resistance(ran.main(7.02), 'ohms')
        k = resistance1.ohms * area1.m2

        area2 = c.area(ran.main(9), 'mm2')
        resistance2 = c.resistance( k/ area2.m2, 'ohms')

        self.question = f"""The electrical resistance of a piece of wire is inversely proportional to the cross sectional area. When the cross sectional area is {area1.mm2} mm2 its resistance is {resistance1.ohms} ohms. Compute the resistance when the cross-sectional area is {area2.mm2} mm2."""
        self.answer = f"""{resistance2.ohms:4.4} ohms"""

class rgs_14:
    def __init__(self):
        weight1 = ran.main(180)
        RADIUS_EARTH = 4000
        altitude = ran.main(1000)
        k = weight1 * RADIUS_EARTH**2

        weight2 = k / (RADIUS_EARTH + altitude)**2

        self.question = f"""The weight of an object above the earth varies inversely as the square of the distance from the center of the earth. If a man weight {weight1} pounds on the surface of the earth, what would his weight be at an altitude {altitude} miles? Assume that the radius of the earth to be {RADIUS_EARTH} miles."""
        self.answer = f"""{weight2:4.4} lbs."""

class rgs_15:
    def __init__(self):
        force1 = ran.main(18.6)
        disp1 = ran.main(1.27)
        k = force1 / disp1

        self.question = f"""According to Hooke's law, the length of a spring S, varies directly as the force F, applied on the spring. If a spring to which Hooke's law applies, a force of {force1} lb stretches the spring by {disp1} in, find k, the constant of proportionality."""
        self.answer = f"""{k:4.4}"""

class rgs_16:
    def __init__(self):
        height1 = ran.main(100)
        velocity1 = ran.main(80)

        k = velocity1 / math.sqrt(height1)

        height2 = ran.main(height1 + ran.main(450))
        velocity2 = k * math.sqrt(height2)

        self.question = f"""A falling body strikes the ground with a velocity v which varies directly as the square root of the distance it falls. If a bodt that falls {height1} feet strikes the ground with a velocity of {velocity1} feet per second, with what velocity will a ball dropped from a monument of height {height2} feet strike the ground?"""
        self.answer = f"""{velocity2:4.4} ft/s."""

class rgs_17():
    def __init__(self):
        harry_ron_ratio = Ratio()
        harry = pick_age()
        ron = int(harry * (1/harry_ron_ratio.number))
        hermione  = int(ran.main(8)) + harry

        self.question = f"""Harry is {harry_ron_ratio.description} as old as Ron and {hermione - harry} years younger than Hermione. If Harry is {harry} years old, what is the sum of their ages?"""
        self.answer = f"""{harry + ron + hermione} years"""

class rgs_18:
    def __init__(self):
        quarters = random.randint(1,10)
        dime_quarter_ratio = random.randint(2,4)
        dimes = dime_quarter_ratio * quarters
        nickel_dime_ratio  = random.randint(2,4)
        nickels = nickel_dime_ratio * dimes
        pennies = dimes

        money = 0.01*pennies + 0.05*nickels + 0.1*dimes + 0.25*quarters

        self.question = f"""Bobbie has ${money:4.2} in quarters, dimes, nickels, and pennies. He has {num2words(dime_quarter_ratio)} times as many dimes as quarters and {num2words(nickel_dime_ratio)} times as many nickels as dimes. The number of pennies is the same as the number of dimes. How many of each coin does he have?"""

        self.answer = f"""P: {pennies}, N: {nickels}, D: {dimes}, Q: {quarters}"""

class rgs_19:
    def __init__(self):
        length1 = ran.main(100)
        diameter1 = ran.main(1.25)
        resistance1 = ran.main(30)

        k = resistance1 * diameter1**2 / length1

        resistance2 = ran.main(25)
        diameter2 = ran.main(0.75)
        length2 = resistance2 * diameter2**2 / k

        self.question = f"""The electrical resistance of a wire varies as its length and inversely as the square of the diameter. If a wire {length1} m long and {diameter1} mm in diameter has a resistance of {resistance1} ohms, find the length of the wire of the same material whose resistance and diameter are {resistance2} ohms and {diameter2} mm, respectively?"""
        self.answer = f"""{length2:4.4} m"""

class rgs_20:
    def __init__(self):
        doll_price = int(ran.main(7))
        train_price = int(ran.main(18))
        doll_quantity = int(ran.main(22))
        train_quantity = int(ran.main(3))

        money = doll_price * doll_quantity + train_price * train_quantity

        self.question = f"""Suppose that dolls sell for {doll_price} dollars each and toy train sell for {train_price} dollars. A store sells only dolls and train sets, and the total amount received is {money} dollars. How many toy trains were sold?"""

        self.answer = f"""{train_quantity}"""

class rgs_21:
    def __init__(self):
        x1 = random.randint(2,10)
        y1 = random.randint(2,10)
        z1 = random.randint(2,10)
        k = z1 * y1**2 / x1

        x2 = random.randint(2,10)
        y2 = random.randint(2,10)
        z2 = k * x2 / y2**2

        self.question = f"""Given that z varies directly as x and inversely as y^2. If x = {x1}, and y = {y1}, then z = {z1}. Find z if x = {x2} and y = {y2}."""
        self.answer = f"""{z2:4.4}"""

class rgs_22:
    def __init__(self):
        percentage_hike = c.percentage(ran.main(10), 'percent')
        percentage_consumption_reduction = c.percentage(ran.main(10), 'percent')

        bill_percentage = c.percentage( percentage_hike.decimal * percentage_consumption_reduction.decimal, 'decimal' )
        delta = c.percentage(abs(1 - bill_percentage.decimal), 'decimal')

        self.question = f"""After the price of petroleum oil went up by {percentage_hike.percent:4.4} %, a consumer reduced his oil consumption by {percentage_consumption_reduction} %. By what percent would his petroleum bill be changed?"""
        self.answer = f"""{delta.percent:4.4} %"""

class rgs_23():
    def __init__(self):
        repeat = True
        while repeat:
            beth = pick_age()
            ana = beth + random.randint(5,10)
            factor = Factor()

            equation = sympy.Eq(
                factor.number * (beth*ana),
                (beth + x)*(ana + x)
                )
            
            i = 0
            solution_positive = False
            while not(solution_positive):
                f = sympy.solveset(equation, x).args[i]
                i = i + 1
                if f > 0:
                    solution_positive = True

            if f.is_integer:
                repeat = False
            

        self.question = f"""Ana is {ana - beth} years older than Beth. In {f} years, the product of their ages is {factor.description} the product of their present ages. How old is Beth now?"""
        self.answer = f"""{beth} years"""

# class rgs_24():
#     def __init__(self):


class rgs_25():
    def __init__(self):
        son_portion = random.randint(2,9)
        daughter_portion = random.randint(2, 9)
        wife_factor = Factor()
        wife_portion = son_portion * wife_factor.number
        bodyguard_portion = random.randint(2, 9)
        total = son_portion + daughter_portion + wife_portion + bodyguard_portion
        money = c.pesos(ran.main(5_000_000))
        bodyguard_money = c.pesos( 
            (bodyguard_portion / total) * money.pesos
            )


        self.question = f"""A multimillionaire left his entire estate to his wife, son, daughter, and bodyguard. His daughter and son got {fractions.Fraction(son_portion + daughter_portion, total)} of the total value of the estate sharing in the ratio of {fractions.Fraction(son_portion, daughter_portion)}. His wife got {wife_factor.description} value as much as the share of the son. If the bodyguard received {bodyguard_money.pesos_string} pesos, what is the total value of the estate?"""
        self.answer = f"""{money.pesos_string}"""

class rgs_26():
    def __init__(self):
        #profit is a linear function of units sold
        units_1 = int(ran.main(80))
        profit_1 = c.pesos(ran.main(80))
        units_2 = int(units_1 + ran.main(30))
        profit_2 = c.pesos(profit_1.pesos + ran.main(60))
        point_1 = analytic_geometry_engine.Point()
        point_1.init_define(units_1, profit_1.pesos)
        point_2 = analytic_geometry_engine.Point()
        point_2.init_define(units_2, profit_2.pesos)

        line = analytic_geometry_engine.Line()
        line.init_two_points(point_1, point_2)

        units_3 = int(units_2 + ran.main(140))
        profit_equation = line.y_in_terms_of_x()
        profit_3 = c.pesos(
            profit_equation.subs(x, units_3)
            )

        profit_per_unit = c.pesos(
            profit_3.pesos / units_3
            )

        self.question = f"""A company sells {units_1} units and makes {profit_1.pesos_string} profit. It sells {units_2} units and makes {profit_2.pesos_string} profit. If the profit is a linear function of the number of units sold, what is the average profit per unit if the company sells {units_3} units?"""
        self.answer = f"""{profit_per_unit.pesos_string}"""

class rgs_27():
    def __init__(self):
        repeat = True
        while repeat:
            #past_ages
            maria_past = pick_age()
            anna_past = pick_age()
            
            #present ages
            maria_ratio = Ratio()
            anna_ratio = Ratio()
            maria = float(maria_past * (1/maria_ratio.number))
            anna = float(anna_past * (1/anna_ratio.number))

            self.question = f"""The sum of the ages of Maria and Anna is {int(maria + anna)}. When Maria was {maria_ratio.description} her present age and Anna was {anna_ratio.description} of her present age, the sum of their ages was {maria_past + anna_past}. How old is Maria now?"""
            self.answer = f"""{int(maria)} years"""

            if maria.is_integer and anna.is_integer:
                repeat = False


class rgs_28():
    def __init__(self):
        past_to_now = random.randint(5,10)
        a_age_past = pick_age()
        b_age_past = pick_age()
        a_age = a_age_past + past_to_now
        b_age = b_age_past + past_to_now

        now_to_future = random.randint(5,10)
        a_age_future = a_age + now_to_future
        b_age_future = b_age + now_to_future

        self.question = f"""{num2words(now_to_future).capitalize()} years from now the sum of the ages of A and B is equal to {a_age_future + b_age_future}. {num2words(past_to_now).capitalize()} years ago, the difference of their ages is equal to {abs(a_age_past - b_age_past)}. How old is A and B?"""
        self.answer = f"""{a_age} years, {b_age} years"""

class rgs_29():
    def __init__(self):

        alice = random.randint(2,10)
        peter = random.randint(2,10)

        if alice > peter:
            alice , peter = peter, alice

        john_factor = Factor()
        # print(john_factor.number)
        # print(john_factor.description)
        
        john = peter * john_factor.number

        #solve for future
        alice_factor = Factor()        
        f = random.randint(5,10)
        print(alice, john, peter)

        self.question = f"""John is {john_factor.description} as old as his friend Peter. Peter is {peter - alice} years older than Alice. In {f} years, John will be {fractions.Fraction(john + f,alice + f)} times as old as Alice. How old is Peter now?"""
        self.answer = f"""{peter} years"""

class rgs_30():
    def __init__(self):
        alice = random.randint(2,10)
        john_factor = Factor()
        father_factor = Factor()

        john = alice * john_factor.number
        father = john * father_factor.number

        f = random.randint(5,10)

        self.question = f"""John's father is {father_factor.description} older than John and John is {john_factor.description} as old as his sister Alice. In {f} years time, the sum of their ages will be {alice + john + father + 3 * f}. How old is John now?"""
        self.answer = f"""{john} years"""

class rgs_31():
    def __init__(self):

        repeat = True
        while repeat:
            try:
                mary = pick_age()
                father_factor = Factor()
                father = int(mary * father_factor.number)
                p = random.randint(5,10)

                if mary - p > 0 and father < 60:
                    repeat = False
                self.question = f"""Mary's father is {father_factor.description} as old as Mary. {num2words(p).capitalize()} years ago he was {fractions.Fraction(father - p, mary - p)} times as old. How old is Mary now?"""
                self.answer = f"""{mary}"""
            except:
                repeat = True

class rgs_32():
    def __init__(self):
        repeat = True
        while repeat:
            son = pick_age()
            factor = Factor()
            man = son * factor.number

            f = random.randint(5,10)

            self.question = f"""A man is {factor.description} as old as his son. In {f} years time, the father will be {fractions.Fraction(man + f, son + f)} as old as his son. How old is the son?"""
            self.answer  = f"""{son} years"""

            if (man - son) > 20 and (man - son) < 40:
                repeat = False

class rgs_33():
    def __init__(self):
        repeat = True
        while repeat:
            cynthia_past = pick_age()
            abigail_factor = Factor()
            abigail_past = abigail_factor.number * cynthia_past

            f = random.randint(5,20)

            abigail = abigail_past + f
            cynthia = cynthia_past + f

            self.question = f"""Abigail is {abigail - cynthia} years older than Cynthia. {num2words(f).capitalize()} years ago, Abigail was {abigail_factor.description} as old as Cynthia. How old is Abigail now?"""
            self.answer = f"""{abigail} years"""

            if abigail_past > 0 and abigail < 60:
                repeat = False

class rgs_34():
    def __init__(self):
        repeat = True
        while repeat:
            cassandra = pick_age()
            factor = Factor()
            seymour = factor.number * cassandra

            equation = sympy.Eq(
                cassandra + x, 
                seymour - x
                )

            f = sympy.solveset(equation, x).args[0]

            self.question = f"""Seymour is {factor.description} as old as Cassandra. If {f} is added to Cassandra's age and {f} is subtracted to Seymour's age, their ages will then be equal. How old is Seymour now?"""
            self.answer = f"""{seymour} years"""

            if cassandra > 0 and seymour < 60 and f.is_integer:
                repeat = False

class rgs_35():
    def __init__(self):
        #resistance = k length / area

        resistance_1 = c.resistance(ran.main(100))
        length_1  = c.length(ran.main(10))
        diameter_1 = c.length(ran.main(0.1), 'cm')
        area_1 = c.area( math.pi * diameter_1.m**2/ 4)

        volume = c.volume( area_1.m2 * length_1.m)

        k = resistance_1.ohms * area_1.m2 / length_1.m

        length_2 = c.length(length_1.m + ran.main(2))
        area_2 = c.area(volume.m3 / length_2.m)
        resistance_2 = c.resistance(k * length_2.m / area_2.m2)

        self.question = f"""The resistance of a wire varies directly with its length and inversely with its area. If a certain piece of wire {length_1.m} meters long and {diameter_1.cm} cm in diameter has a resistance of {resistance_1.ohms} ohms, what will its resistance be if its is uniformly stretched so that its length becomes {length_2.m:4.4} meters?"""
        self.answer = f"""{resistance_2.ohms:4.4} ohms"""

class rgs_36():
    def __init__(self):
        #assume a length of 1
        a_time = ran.main(8)
        b_time = ran.main(4)

        equation = sympy.Eq(
            1 - (1/a_time) * x, 
            (1 - (1/b_time) * x) * 2
            )

        time = sympy.solveset(equation, x).args[0]

        self.question = f"""Candle A and Candle B of equal length are lighted at the same time and burning until Candle A is twice as long as Candle B. Candle A is designed to fully burn in {a_time} hours while Candle B for {b_time} hours. How long will they be lighted?"""
        self.answer = f"""{time:4.4} hours"""

class rgs_37():
    def __init__(self):
        apples = random.randint(1,20)
        oranges = random.randint(1,20)
        if apples < oranges:
            apples, oranges = oranges, apples

        price_discrepancy = c.pesos(ran.main(3))
        orange_price = c.pesos(ran.main(10))
        apple_price = c.pesos(orange_price.pesos + price_discrepancy.pesos)

        cost = c.pesos(
            apples * apple_price.pesos + oranges * orange_price.pesos
            )

        self.question = f"""A customer bought some apples and some oranges, {oranges + apples} of fruit in total, and they cost him {cost.pesos_string}. If an apple costs {price_discrepancy.pesos_string} more than an orange, and if more apples than oranges were purchased, how many pieces of apple were bought?"""
        self.answer = f"""{apples}"""

class rgs_38():
    def __init__(self):
        bar_length = c.length(ran.main(4))
        weight_1 = c.force(ran.main(300), 'lb')
        weight_2 = c.force(ran.main(200), 'lb')

        equation = sympy.Eq(
            weight_1.lb * x, weight_2.lb * (bar_length.m - x)
            )

        distance = c.length(
            sympy.solveset(equation, x).args[0]
            )

        self.question = f"""An iron bar {bar_length.m:4.4} meters long has a {weight_1.lb:4.4} -lb weight hung on one end and a {weight_2.lb:4.4}-lb weight hung at the opposite end. How far from the {weight_1.lb:4.4}-lb weight should the fulcrum be located to balance the bar?"""
        self.answer = f"""{distance.m:4.4} meters"""

# class rgs_39():
#     def __init__(self):

class rgs_40():
    def __init__(self):
        volume_result = ran.main(5)
        concentration_result = c.percentage(ran.main(10), 'percent')
        concentration_b = c.percentage(concentration_result.percent + ran.main(2), 'percent')
        concentration_a = c.percentage(concentration_result.percent - ran.main(3), 'percent')

        mix_a = Mixture(x, concentration_a.decimal * x, concentration_a.decimal)
        mix_b = Mixture(volume_result - x, concentration_b.decimal * (volume_result - x), concentration_b.decimal)
        mix_c = mix_a.mix(mix_b)

        equation = sympy.Eq(mix_c.concentration, concentration_result.decimal)

        volume_a = sympy.solveset(equation, x).args[0]

        self.question = f"""For a particular experiment, you need {volume_result} liters of {concentration_result.percent:4.4} %. You find {concentration_a.percent:4.4}% and {concentration_b.percent:4.4}%. How much of the {concentration_a.percent:4.4}% solution do you mix with the appropriate amount of the {concentration_b.percent:4.4} % solution to get {volume_result} liters of {concentration_result.percent:4.4} % solution?"""
        self.answer = f"""{volume_a:4.4} liters"""

class rgs_41():
    def __init__(self):
        horse_price = int(ran.main(31))
        ox_price = int(ran.main(21))
        ox = random.randint(11, 51)
        horse = random.randint(11, 51)
        cost = horse_price * horse + ox_price * ox

        self.question = f"""A farmer lays out the sum of {cost} crowns in purchasing horses and oxen. He pays {horse_price} for each horse and {ox_price} for each ox. How many oxen did the farmer buy?"""
        self.answer = f"""{ox}"""

class rgs_42():
    def __init__(self):
        milk_1 = random.randint(1,10)
        water_1 = random.randint(1,10)
        frac_1 = fractions.Fraction(milk_1, water_1)
        c1 = milk_1 / (milk_1 + water_1)
        milk_2 = random.randint(1,10)
        water_2 = random.randint(1,10)
        frac_2 = fractions.Fraction(milk_2, water_2)
        c2 = milk_2 / (milk_2 + water_1)


        a = Mixture(1, milk_1, c1)
        b = Mixture(1, milk_2, c2)
        c = a.mix(b)

        self.question = f"""The ratios of pure milk and water in two vessels are {frac_1.numerator} : {frac_1.denominator} and {frac_2.numerator} : {frac_2.denominator} respectively. If equal quantities of the mixtures of the vessels are mixed together, the ratio of pure milk and water in the new vessel is"""
        frac_c = fractions.Fraction(c.concentration)
        self.answer = f"""{frac_c.numerator} : {frac_c.denominator}"""

class rgs_43():
    def __init__(self):
        total_money = c.pesos(ran.main(3000))
        r1 = random.randint(1,20)
        r2 = random.randint(1,20)
        frac = fractions.Fraction(r1, r2)
        money_a = c.pesos(
            (r1 / (r1 + r2)) * total_money.pesos
            )
        money_b = c.pesos(
            (r2 / (r1 + r2)) * total_money.pesos
            )
        if money_a.pesos > money_b.pesos:
            money_a, money_b = money_b, money_a

        self.question = f"""A certain sum of money is distributed among two friends in the ratio of {frac.numerator}:{frac.denominator}. If one of them got {c.pesos(money_b.pesos - money_a.pesos).pesos_string} more than the other, the total sum was"""
        self.answer = f"""{total_money.pesos_string}"""

class rgs_44():
    def __init__(self):
        total_money = c.pesos(ran.main(5000))
        r1 = random.randint(1,20)
        r2 = random.randint(1,20)
        r3 = random.randint(1,20)
        if r2 > r3:
            r2, r3 = r3, r2
        total_r = r1 + r2 + r3
        p_a = c.percentage(ran.main(40), 'percent')

        money_a = c.pesos(
            (r1 / total_r) * total_money.pesos
            )
        money_b = c.pesos(
            (r2 / total_r) * total_money.pesos
            )
        money_c = c.pesos(
            (r3 / total_r) * total_money.pesos
            )

        money_a_portion = c.pesos(
            money_a.pesos * p_a.decimal
            )

        GCD = math.gcd(math.gcd(r1, r2), r3)
        self.question= f"""An amount is divided among A, B, and C in the ratio of {int(r1/GCD)}:{int(r2/GCD)}:{int(r3/GCD)} respectively. If {p_a.percent:4.4} % of the amount A received is {money_a_portion.pesos_string}, what is the difference between the amounts received by B and C?"""
        self.answer = f"""{c.pesos(money_c.pesos - money_b.pesos).pesos_string}"""

# class rgs_45():
#     def __init__(self):

class rgs_46():
    def __init__(self):
        repeat = True
        while repeat:

            a_time = int(ran.main(24))
            b_time = int(ran.main(32))

            time_in_question = int(ran.main(16))

            equation = sympy.Eq(
                1, 
                ((1/a_time) + (1/b_time)) * x + (1/b_time) * (16 - x)
                )

            time_to_close_a = sympy.solveset(equation, x).args[0]

            self.question = f"""Two pipes A and B fill a cistern in {a_time} minutes and {b_time} minutes respectively. Assuming that both pipes are opened simultaneously, when must the first tap be turned off so that the cistern may be filled in {time_in_question} minutes?"""
            self.answer = f"""{time_to_close_a:4.4} minutes"""

            if 0 < time_to_close_a < time_in_question:
                repeat = False

# class rgs_47():
#     def __init__(self):

#         steal_time = random_time()
#         speed_1 = c.velocity(ran.main(45), 'kmperh')
#         discover_delta = ran.main(1)
#         discover_h, discover_m = hour_convert(discover_delta)
#         discover_time = datetime.time(hour = steal_time.hour + discover_h, minute = steal_time.minute + discover_m)
#         speed_2 = c.velocity(speed_1.kmperh + ran.main(9), 'kmperh')

#         equation = sympy.Eq(
#             (speed_1.kmperh * x),
#             (speed_2.kmperh * (x - discover_delta))
#             )

#         solution_positive = False
#         i = 0
#         while not(solution_positive):
#             hours_chase = sympy.solveset(equation, x).args[i]
#             i = i + 1
#             if hours_chase > 0:
#                 solution_positive = True

#         chase_h, chase_m = hour_convert(hours_chase)
#         chase_time = steal_time.

#         self.question = f"""A theif steals a scooter at {steal_time.strftime('%I:%M:%p')} and drives at the speed of {speed_1.kmperh} km/h. The theft is discovered at {discover_time.strftime('%I:%M:%p')} and the owner chases him at {speed_2.kmperh} km/h. He will be caught at"""
#         self.answer = f"""{chased_time.strftime('%I:%M:%p')}"""











        


        

        












