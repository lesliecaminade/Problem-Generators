from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
import num2words

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables
            
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

class rgs_1:
    def __init__(self):
        num1 = random.randint(2,10)
        num2 = random.randint(2,10)
        
        self.question = f"""Twice the sum of two numbers is {2*(num1 + num2)}. The sum of their squares is {num1**2 + num2**2}. What is the product of the two numbers?"""
        self.answer = f"""Product of the two numbers: {num1 * num2}"""

class rgs_2:
    def __init__(self):
        #pick a random odd integer
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

        self.question = f"""Three times the first of the three consecutive odd integers is {num2words.num2words(difference)} more than twice the third. Find the third integer"""
        self.answer = f"""Third integer: {num3}"""

class rgs_4:
    def __init__(self):
        discount = c.percentage(ran.main(20),'percent')
        retail_price = ran.main(225)
        discounted_retail_price = retail_price * ( 1 - discount.decimal )
        discount_wholesale = c.percentage(ran.main(50), 'percent')
        wholesale_price = retail_price / (1 + discount_wholesale.decimal )

        self.question = f"""A merchant marked a certain product for P{discounted_retail_price}, which is {discount.percent}% off the normal retail price. If the retail price is {discount_wholesale.percent}% higher than the wholesale price, what is the wholesale price of the product?"""
        self.answer = f"""Wholesale price: {wholesale_price}"""

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
        self.answer = f"""Profit: {ratio.percent}% {desc}"""

class rgs_6:
    def __init__(self):
        hour = random.randint(0, 11)

        if hour == 0:
            display_hour = 12
            next_hour = 1
        else:
            display_hour = hour
            next_hour = display_hour + 1

        #for the first time
        if hour <= 3:
            minute = clock(hour, 90, 'minute')
        if hour > 3:
            minute = clock(hour, 90, 'hour')

        self.question = f"""At what time between {display_hour} and {next_hour} o'clock will the hands of the clock be at right angles for the first time?"""
        self.answer = f"""Time for first right angle: {display_hour}:{minute}"""

class rgs_8:
    def __init__(self):
        smaller = int(ran.main(19))
        larger = smaller + int(ran.main(5))

        self.question = f"""The difference of the cubes of two positive numbers is {larger**3 - smaller**3} and the cube of their difference is {(larger - smaller)**3}. Find the smaller number."""

        self.answer = f"""Smaller number: {smaller}"""

class rgs_9:
    def __init__(self):
        cats = random.randint(3,5)
        rats = random.randint(3,5)
        minutes = random.randint(3,5)

        cat_rate = (rats/minutes) / cats

        cats_next = int(ran.main(100))
        rats_next = int(ran.main(100))

        time_minutes = (rats_next / (cat_rate * cats_next))

        self.question = f"""{num2words.num2words(cats)} cats can kill {rats} rats in {minutes} minutes. How many minutes will it take for {cats_next} cats to kill {rats_next}?"""
        self.answer = f"""Time in minutes: {time_minutes}"""

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

        self.answer = f"""w = {w2}"""

class rgs_11:
    def __init__(self):
        water_speed = int(ran.main(8))
        boat_speed = int(ran.main(40))

        downstream = water_speed + boat_speed
        upstream = boat_speed - water_speed
        speed_ratio = sym.simplify(sym.Rational(downstream, upstream))
        time_ratio = sym.simplify(sym.Rational(upstream, downstream))

        self.question = f"""A boat takes {time_ratio} as much time to travel downstream than to travel upstream. If the rate of the water current is {water_speed} kph, what is the rate of the of the boat in still water?"""

        self.answer = f"""Boat speed in still water: {boat_speed} kph"""

class rgs_12:
    def __init__(self):
        hour = random.randint(0,11)
        if hour == 0:
            display_hour = 12
        else:
            display_hour = hour

        if hour <= 6:
            minutes = clock(hour, 180, 'minutes')
        if hour > 6:
            minutes = clock(hour, 180, 'hour')

        self.question = f"""How many minutes after {display_hour}:00 o'clock will the hands of the clock be opposite each other for the first time?"""
        self.answer = f"""Minutes: {minutes}"""

class rgs_13:
    def __init__(self):
        area1 = c.area(ran.main(5), 'mm2')
        resistance1 = c.resistance(ran.main(7.02), 'ohms')
        k = resistance1.ohms * area1.m2

        area2 = c.area(ran.main(9), 'mm2')
        resistance2 = c.resistance( k/ area2.m2, 'ohms')

        self.question = f"""The electrical resistance of a piece of wire is inversely proportional to the cross sectional area. When the cross sectional area is {area1.mm2} mm2 its resistance is {resistance1.ohms} ohms. Compute the resistance when the cross-sectional area is {area2.mm2} mm2."""
        self.answer = f"""Resistance at {area2.mm2} mm2: {resistance2.ohms} ohms"""

class rgs_14:
    def __init__(self):
        weight1 = ran.main(180)
        RADIUS_EARTH = 4000
        altitude = ran.main(1000)
        k = weight1 * RADIUS_EARTH**2

        weight2 = k / (RADIUS_EARTH + altitude)**2

        self.question = f"""The weight of an object above the earth varies inversely as the square of the distance from the center of the earth. If a man weight {weight1} pounds on the surface of the earth, what would his weight be at an altitude {altitude} miles? Assume that the radius of the earth to be {RADIUS_EARTH} miles."""
        self.answer = f"""Weight at {altitude} miles above earth: {weight2} pounds."""

class rgs_15:
    def __init__(self):
        force1 = ran.main(18.6)
        disp1 = ran.main(1.27)
        k = force1 / disp1

        self.question = f"""According to Hooke's law, the length of a spring S, varies directly as the force F, applied on the spring. If a spring to which Hooke's law applies, a force of {force1} lb stretches the spring by {disp1} in, find k, the constant of proportionality."""
        self.answer = f"""Constant of proportionality: {k}"""

class rgs_16:
    def __init__(self):
        height1 = ran.main(100)
        velocity1 = ran.main(80)

        k = velocity1 / math.sqrt(height1)

        height2 = ran.main(height1 + ran.main(450))
        velocity2 = k * math.sqrt(height2)

        self.question = f"""A falling body strikes the ground with a velocity v which varies directly as the square root of the distance it falls. If a bodt that falls {height1} feet strikes the ground with a velocity of {velocity1} feet per second, with what velocity will a ball dropped from a monument of height {height2} feet strike the ground?"""
        self.answer = f"""Velocity: {velocity2} feet per second."""

class rgs_17:
    def __init__(self):
        harry = int(ran.main(8))
        
        hermione = int(harry + ran.main(8))
        ron = int(hermione + ran.main(8))

        ratio_1 = sym.Rational(harry, hermione)
        diff = hermione - harry

        self.question = f"""Harry is {ratio_1} as old as Ron and {diff} years younger than Hermione. If Harry is {harry} years old, what is the sum of their ages?"""
        self.answer = f"""Sum of their ages: {harry + ron + hermione}"""

class rgs_18:
    def __init__(self):
        quarters = random.randint(1,10)
        dime_quarter_ratio = random.randint(2,4)
        dimes = dime_quarter_ratio * quarters
        nickel_dime_ratio  = random.randint(2,4)
        nickels = nickel_dime_ratio * dimes
        pennies = dimes

        money = 0.01*pennies + 0.05*nickels + 0.1*dimes + 0.25*quarters

        self.question = f"""Bobbie has ${money} in quarters, dimes, nickels, and pennies. He has {num2words.num2words(dime_quarter_ratio)} times as many dimes as quarters and {num2words.num2words(nickel_dime_ratio)} times as many nickels as dimes. The number of pennies is the same as the number of dimes. How many of each coin does he have?"""

        self.answer = f"""Pennies: {pennies}, Nickels: {nickels}, Dimes: {dimes}, Quarters: {quarters}"""

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
        self.answer = f"""Length: {length2} m"""

class rgs_20:
    def __init__(self):
        doll_price = int(ran.main(7))
        train_price = int(ran.main(18))
        doll_quantity = int(ran.main(22))
        train_quantity = int(ran.main(3))

        money = doll_price * doll_quantity + train_price * train_quantity

        self.question = f"""Suppose that dolls sell for {doll_price} dollars each and toy train sell for {train_price} dollars. A store sells only dolls and train sets, and the total amount received is {money} dollars. How many toy trains were sold?"""

        self.answer = f"""Trains: {train_quantity}"""

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
        self.answer = f"""Z value: {z2}"""

class rgs_22:
    def __init__(self):
        percentage_hike = c.percentage(ran.main(10), 'percent')
        percentage_consumption_reduction = c.percentage(ran.main(10), 'percent')

        bill_percentage = c.percentage( percentage_hike.decimal * percentage_consumption_reduction.decimal, 'decimal' )
        delta = c.percentage(abs(1 - bill_percentage.decimal), 'decimal')

        self.question = f"""After the price of petroleum oil went up by {percentage_hike.percent} %, a consumer reduced his oil consumption by {percentage_consumption_reduction} %. By what percent would his petroleum bill be changed?"""
        self.answer = f"""Percentage bill change: {delta.percent} %"""

class rgs_23:
    def __init__(self):
        anna = random.randint(1,10)
        diff = random.randint(1,10)
        beth = anna + diff

        plus = random.randint(1,10)
        anna_plus = anna + plus
        beth_plus = beth + plus

        future_product_ages = anna_plus * beth_plus
        product_ages = anna * beth

        ratio = sym.simplify(sym.Rational(future_product_ages, product_ages))

        self.question = f"""Ana is {diff} years older than Beth. In {plus} years the product of their ages is {ratio} times the product of their present ages. How old is Beth now?"""

        self.answer = f"""Beth's age now: {beth}"""

class rgs_24:
    def __init__(self):
        peter = random.randint(1,10)
        paul = peter  + random.randint(1,10)

        plus = random.randint(1,10)

        peter_plus = peter + plus
        paul_plus = paul + plus

        ratio = sym.simplify(sym.Rational(peter_plus, paul_plus))
        self.question =f"""The sum of the ages of Peter and Paul is {peter + paul}. Peter will be {ratio} times as sold as Paul {plus} years from now. What is the present age of Peter?"""
        self.answer = f"""Peter's present age: {peter}"""

        












