import random_handler as ran
import numpy_handler as num
import sympy as sym
# from sympy import init_printing
import math
import random
# import algebra
# import analytic_geometry
import constants_conversions as c
# import randomizer_2 as ran2

x, y, z = sym.symbols('x y z', real = True)#generic variables
            
#init_printing(use_unicode=False)
# gravity = c.acceleration(9.81, 'mpers2')  
class interest:
    def __init__(self,*args,**kwargs):
        self.percent = args[0]
        self.decimal = self.percent / 100
        for arg in args:
            if arg == 'decimal':
                self.decimal = args[0]
                self.percent = args[0] * 100
                
    def eri(self,m):
        eff = (1 + self.decimal / m)**m - 1
        return interest(eff*100)
        
                
class money:
    def __init__(self,*args,**kwargs): 
        self.money = args[0]
        
    def add(self,money_object):
        new_money = self.money + money_object.money
        return money(new_money)
    
    def compound(self,interest_object,periods,*args):
        
        #args0 is interest per period
        try:
            interest_per_period = args[0]
        except:
            interest_per_period = 1
            
        new_money = self.money * (1 + interest_object.decimal/interest_per_period)**(periods)

        return money(new_money) 
        
    def whenCompound(self,future_object, interest_object):
        #this finds the number of periods required to go from principal to future values
        periods = math.log(future_object.money/self.money) / math.log(1 + interest_object.decimal)
        return periods
        
    def findInterestCompound(self,future_object,periods):
        #find the interest rate
        interestrate = (future_object.money / self.money)**(1/periods) - 1
        return interest(interestrate*100)
        

class hipolito_2_1:
    def __init__(self,*args,**kwargs): 
        interest = ran.main(265)
        principal = ran.main(15000)
        
        self.question = f"""What is the annual rate of interest if P {interest} is earned in four months on an investment of P {principal}?"""
        
        n = 4/12
        
        i = interest / (principal * n) 
        ipercentage = i * 100
        
        self.answer = f"""Annual rate of interest = {ipercentage} %"""
        
class hipolito_2_2:
    def __init__(self,*args,**kwargs): 
        
        principal = ran.main(2000)
        i = interest(ran.main(20, 'int'))
        
        self.question = f"""A loan of P {principal:,} is made for a period of 13 months, from January 1 to January 31 the following year, at a simple interest of {i.percent} %. What is the future amount is due at the end of the loan period?"""
        
        future = principal * ( 1 + (13/12) * i.decimal)
        
        self.answer = f"""Future Amount = P {future:,}"""
        
class hipolito_2_3:
    def __init__(self,*args,**kwargs): 
        
        i = interest(ran.main(12,'int'))
        future = money(ran.main(20000))
        
        self.question = f"""If you borrow money from your friend with simple interest of {i.percent}%, find the present worth of P{future.money:,}, which is due at the end of nine months."""
        
        n = 9/12
        
        present = money(future.money /  ( 1 + n * i.decimal ))
        
        self.answer = f"""Present Worth = {present.money:,}"""
        
        
class hipolito_2_5:
    def __init__(self,*args,**kwargs): 
        
        future = money(ran.main(200000))
        rate1 = interest(ran.main(10, 'int'))
        rate2 = interest(ran.main(12, 'int'))
        
        years1 = ran.main(5, 'int')
        years2 = ran.main(5, 'int')
        
        self.question = f"""A man wishes his son to receive P{future.money:,} ten years from now. What amount should he invest if it will earn interest of {rate1.percent} % compounded annually during the first {years1} years and {rate2.percent} % compounded quarterly during the next {years2} years?"""
        
        int1 = interest(rate1.percent / 1)
        int2 = interest(rate2.percent / 4)
        
        p2 = future.compound(int2,-4*years2)
        p1 = p2.compound(int1, -years1)
        
        self.answer = f"""Amount to be invested = P {p1.money:,}""" 
        
class hipolito_2_6:
    def __init__(self,*args,**kwargs): 
        principal = money(ran.main(25000))
        future = money(ran.main(45000))
        rate = interest(ran.main(8, 'int'))
        int = interest(rate.percent / 4)
        
        self.question = f"""By the condition of a will the sum of P {principal.money:,} is left to be held in trust by her guardian until it amounts to P{future.money:,}. When will the girl receive the money if the fund is invested at {rate.percent}% compounded quarterly?"""
        
        periods = principal.whenCompound(future, int)
        years = periods / 4
        
        self.answer = f"""Time required = {years} years"""
        
class hipolito_2_7:
    def __init__(self,*args,**kwargs): 
        
        principal = money(ran.main(5_000))
        future = money(ran.main(20_000))
        years1 = ran.main(10, 'int')
        years2 = years1 + ran.main(5, 'int')
        
        
        self.question = f"""At a certain interest rate compounded semiannually P{principal.money:,} will amount to P{future.money:,} after {years1} years. What is the amount at the end of {years2} years?"""
        
        int = principal.findInterestCompound(future, years1 * 2)
        future2 = principal.compound(int, years2 * 2)
        
        self.answer = f"""Amount after {years2} years = P {future2.money:,}"""
        
class hipolito_2_8:
    def __init__(self,*args,**kwargs): 
        p1 = money(ran.main(9000))
        p2 = money(ran.main(12000))
        
        p3 = money(p1.money - ran.main(2000))
        int = interest(ran.main(12, 'int'))
        
        self.question = f"""Jones Corporation borrowed P{p1.money:,} from Brown Corporation on Jan. 1, 1978 and P{p2.money:,} on Jan. 1, 1980. Jones Corporation made a partial payment of P{p3.money:,} on Jan. 1, 1981. It was agreed that the balance of the loan would be amortizes by two payments one of Jan. 1, 1982 and the other on Jan. 1, 1983, the second being 50%larger than the first. If the interest rate is {int.percent}%. What is the amount of each payment?"""
        
        p1 = p1.compound(int,5)
        p2 = p2.compound(int,3)
        p3 = p3.compound(int,2)
        
        equation = sym.Eq(
        p1.money + p2.money,
        p3.money + x*(1 + int.decimal)**2 + (3/2)*x
        )
        
        temp = sym.solveset(equation,x,domain = sym.Reals)
        temp2 = temp.args[0]
        
        self.answer = f"""First Payment = P{temp2:,} 
Second Payment = P{(3/2)*temp2:,}"""

class hipolito_2_9:
    def __init__(self,*args,**kwargs): 
        principal1 = money(ran.main(3000))
        years1 = 1.5
        principal2 = money(ran.main(5000))
        years2 = 3
        rate1 = interest(ran.main(12,'int'))
        rate2 = interest(rate1.percent,'int')
        years3 = 3.5
        rate3 = interest(rate1.percent + ran.main(4,'int'))
        
        self.question = f"""A woman borrowed P{principal1.money:,} to be paid after 1 and  1/2 years with interest at {rate1.percent}% compounded semiannually and P{principal2.money:,} to be paid after 3 years at {rate2.percent}% compounded monthly. What single payment must she pay after 3 and 1/2 years at an interest rate of {rate3.percent}% compounded quarterly to settle the two obligations?"""
        
        future1 = principal1.compound(rate1, 2*years1, 2)
        future2 = principal2.compound(rate2, 12*years2, 12)
        
        future3 = future1.compound(rate3,4*(years3 - years1), 4)
        future3 = future3.add(future2.compound(rate3,4*(years3 - years1),4))
        
        self.answer = f"""Single Payment after 3.5 years = P{future3.money:,}"""
        
class hipolito_2_10:
    def __init__(self,*args,**kwargs): 
        principal = money(ran.main(1342, 'int'))
        future = money(principal.money + ran.main(158, 'int'))
        months = ran.main(9, 'int')
        
        self.question = f"""Mr. J. de la Cruz borrowed money from a bank. He received from the bank P{principal.money:,} and promises to repay P{future.money:,} at the end of {months} months. Determine the simple interest rate and the corresponding discount rate or often referred to as the “Banker’s discount.”"""
        
        discount = interest((future.money - principal.money)/principal.money, 'decimal')
        interestrate = interest(discount.decimal / (1 - discount.decimal), 'decimal')
        
        self.answer = f"""Rate of discount = {discount.percent}%
Simple interest rate = {interestrate.percent}%"""

class hipolito_2_11:
    def __init__(self,*args,**kwargs): 
        principal = money(ran.main(50_000, 'int'))
        rate1 = interest(ran.main(6,'int'))
        inflation1 = interest(rate1.percent+0.5)
        years = ran.main(5,'int')
        
        self.question = f"""A man deposits P{principal.money:,} in a bank account at {rate1.percent}% compounded monthly for {years} years. If the inflation rate of {inflation1.percent}% per year continues for this period, will this effectively protect the purchasing power of the original principal? How much is the purchasing power after {years} years?"""
        
        eri = rate1.eri(12)
        
        future = principal.compound(eri, 5)
        future = future.compound(inflation1, -5)
        
        self.answer = f"""Purchasing power after {years} years = P {future.money:,}"""
        
        
        
        
        
        
        