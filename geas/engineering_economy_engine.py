from generator import random_handler as ran
from generator import constants_conversions as c
import sympy
import math
import random
from num2words import num2words
import datetime

YEAR_NOW = 2020
YEAR_MIN = 1980
YEAR_MAX = 2019

x, y, z = sympy.symbols('x y z', real = True)#generic variables

COMPOUNDING_METHODS = ['annually', 'semi-annually', 'quarterly', 'bimonthly', 'monthly', 'semi-monthly']

COMPANY_NAMES = ['SM Investments Corporation', 'BDO Unibank Incorporated', 'JG Summit Holdings Incorporated', 'Ayala Corporation', 'Top Frontier Investment Holdings Incorporated', 'Metropolitan Bank & Trust Company', 'Aboitiz Equity Ventures', 'Manila Electric Company (Meralco)']

RICH_MEN_NAMES = ['Henry Sy', 'Manuel Villar', 'John Gokongwei', 'Enrique K. Razon', 'Jaime Zobel de Ayala', 'Lucio Tan', 'Tony Tan Caktiong', 'Ramon Ang', 'Andrew Tan', 'Inigo Zobel', 'Lucio Co', 'Roberto Ongpin', 'Eduardo Cojuanco', 'Robert Coyuito Jr.']

def compound_method():
	method = random.choice(COMPOUNDING_METHODS)
	if method == 'annually':
		periods_per_year = 1
	elif method == 'semiannually' or method == 'semi-annually':
		periods_per_year = 2
	elif method == 'quarterly':
		periods_per_year = 4
	elif method == 'bimonthly':
		periods_per_year = 6
	elif method == 'monthly':
		periods_per_year = 12
	elif method == 'semimonthly' or method == 'semi-monthly':
		periods_per_year = 24
	else:
		print('compounding method not found.')

	return method, periods_per_year

def is_leap(year):
	if year %4 == 0:
		leap = True
	else:
		leap = False

	if year %100 == 0:
		leap = False

	if year %400 == 0:
		leap = True

	return leap

def compound(amount, interest, years, method, periods = False):
	
	if method == 'annually':
		periods_per_year = 1
	elif method == 'semiannually' or method == 'semi-annually':
		periods_per_year = 2
	elif method == 'quarterly':
		periods_per_year = 4
	elif method == 'bimonthly':
		periods_per_year = 6
	elif method == 'monthly':
		periods_per_year = 12
	elif method == 'semimonthly' or method == 'semi-monthly':
		periods_per_year = 24
	else:
		print('compounding method not found.')

	if periods:
		return c.pesos(amount.pesos * (1 + interest.decimal/periods_per_year)**(periods))
	else:
		return c.pesos(amount.pesos * (1 + interest.decimal/periods_per_year)**(years * periods_per_year))

def eri(interest_rate, method):
	if method == 'annually':
		periods_per_year = 1
	elif method == 'semiannually' or method == 'semi-annually':
		periods_per_year = 2
	elif method == 'quarterly':
		periods_per_year = 4
	elif method == 'bimonthly':
		periods_per_year = 6
	elif method == 'monthly':
		periods_per_year = 12
	elif method == 'semimonthly' or method == 'semi-monthly':
		periods_per_year = 24
	else:
		print('compounding method not found.')	

	return c.percentage((1 + interest_rate.decimal/periods_per_year)**(periods_per_year) - 1, 'decimal')

# def future_annuity(annuity, interest_per_period, periods):
# 	return c.pesos(annuity.pesos * (((1 + interest_per_period.decimal)**(periods) - 1)/(interest_per_period.decimal)))

# def present_ordinary_annuity(annuity, interest_per_period, periods):
# 	return c.pesos(annuity.pesos * (((1 + interest_per_period.decimal)**periods - 1)/(interest_per_period.decimal * (1 + interest_per_period.decimal)**periods)))

def summation(function, start, end):
	sums = 0 * x
	print('summation', start, end)
	#accumulator = 0 * x
	# print(start)
	# print(end)
	if start < end:
		for i in range(start, end + 1):
			moved = function.subs(x, i)
			sums = sums + moved
			print(moved)
	else:

		for i in range(end, start + 1):
			moved = function.subs(x, i)
			sums = sums + moved
			print(moved)


	print('Final value: ', sums)
	return sums
	
def move_payment(amount, interest_per_period, start, destination):
	return c.pesos(amount.pesos * (1 + interest_per_period.decimal)**(destination - start))

def move_payments(uniform_amount, interest_per_period, start, end, destination):
	print('move_payments: ', start, end, destination)
	
	sums = summation(uniform_amount.pesos * ( 1 + interest_per_period.decimal)**(x), destination - start, destination - end)

	#print(c.pesos(float(sums)).pesos_string)
	return c.pesos(float(sums))

def present_to_annuities(present, interest_per_period, periods, **kwargs):
	_type = None
	for key, value in kwargs.items():
		if key == 'type':
			_type = value

	if _type == 'ordinary' or _type == None:
		return c.pesos(
			present.pesos / 
			(((1 + interest_per_period.decimal)**periods  - 1)/
				(interest_per_period.decimal * (1 + interest_per_period.decimal)**periods))
			)

def print_depreciation_sched(depreciation_object):
	print('n\t\tBV\t\td\t\tD')
	for i in range(0, depreciation_object.lifespan + 1):
		print(i, '\t\t', depreciation_object.book_values[i].pesos_string, '\t\t', depreciation_object.depreciations[i].pesos_string, '\t\t', depreciation_object.total_depreciations[i].pesos_string)

class Straight_Line_Depreciation():
	def __init__(self, first_cost, salvage_value, lifespan):

		self.first_cost = first_cost
		self.salvage_value = salvage_value
		self.lifespan = lifespan

		book_values = []
		depreciations = []
		total_depreciations = []

		depreciation = c.pesos((first_cost.pesos - salvage_value.pesos) / lifespan)
		book_value_expression = first_cost.pesos - depreciation.pesos * x 
		
		depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			depreciations.append(c.pesos(depreciation.pesos))

		book_values.append(first_cost)
		total_depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			book_values.append(c.pesos(book_value_expression.subs(x, i)))
			total_depreciations.append(c.pesos(first_cost.pesos - book_values[i].pesos))

		self.book_values = book_values
		self.depreciations = depreciations
		self.total_depreciations = total_depreciations

class Sinking_Fund_Depreciation():
	def __init__(self, first_cost, salvage_value, lifespan, interest_rate):

		self.first_cost = first_cost
		self.salvage_value = salvage_value
		self.lifespan = lifespan

		book_values = []
		depreciations = []
		total_depreciations = []

		init_depreciation = c.pesos(
			(first_cost.pesos - salvage_value.pesos) * (interest_rate.decimal) / ( (1 + interest_rate.decimal)**lifespan - 1 )
			)

		depreciations.append(c.pesos(0))
		depreciations.append(init_depreciation)

		for i in range(2, lifespan + 1):
			depreciations.append(
				c.pesos(init_depreciation.pesos * (1 + interest_rate.decimal)**(i - 1))
					)

		total_depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			total_dep = 0
			for j in range(1, i + 1):
				total_dep = total_dep + depreciations[j].pesos 
			total_depreciations.append(
				c.pesos(total_dep)
				)

		book_values.append(first_cost)
		for i in range(1, lifespan + 1):
			book_values.append(
				c.pesos(first_cost.pesos - total_depreciations[i].pesos)
				)

		self.book_values = book_values
		self.depreciations = depreciations
		self.total_depreciations = total_depreciations

class Declining_Balance_Depreciation():
	def __init__(self, first_cost, salvage_value, lifespan):

		k = c.percentage( 1 - (salvage_value.pesos / first_cost.pesos)**(1/lifespan), 'decimal')

		#book_value
		#depreciations
		#total_depreciations
		book_values = []
		depreciations = []
		total_depreciations = []

		for i in range(0, lifespan + 1):
			book_values.append( 
				c.pesos(first_cost.pesos * (1 - k.decimal)**(i))
				)

		depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			depreciations.append(
				c.pesos(book_values[i - 1].pesos - book_values[i].pesos)
				)

		total_depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			#add all depreciations from dn down to d1
			total_dep = 0
			for j in range(0, i + 1):
				total_dep = total_dep + depreciations[j].pesos 
			
			total_depreciations.append(
				c.pesos(total_dep)
				)

		self.first_cost = first_cost
		self.salvage_value = salvage_value
		self.lifespan = lifespan
		self.book_values = book_values
		self.depreciations = depreciations
		self.total_depreciations = total_depreciations

class Double_Declining_Balance_Depreciation():
	def __init__(self, first_cost, salvage_value, lifespan):

		k = c.percentage( 2/lifespan, 'decimal')

		#book_value
		#depreciations
		#total_depreciations
		book_values = []
		depreciations = []
		total_depreciations = []

		for i in range(0, lifespan + 1):
			book_values.append( 
				c.pesos(first_cost.pesos * (1 - k.decimal)**(i))
				)

		depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			depreciations.append(
				c.pesos(book_values[i - 1].pesos - book_values[i].pesos)
				)

		total_depreciations.append(c.pesos(0))
		for i in range(1, lifespan + 1):
			#add all depreciations from dn down to d1
			total_dep = 0
			for j in range(0, i + 1):
				total_dep = total_dep + depreciations[j].pesos 
			
			total_depreciations.append(
				c.pesos(total_dep)
				)

		self.first_cost = first_cost
		self.salvage_value = salvage_value
		self.lifespan = lifespan
		self.book_values = book_values
		self.depreciations = depreciations
		self.total_depreciations = total_depreciations

class Sum_Of_The_Years_Depreciation():
	def __init__(self, first_cost, salvage_value, lifespan):

		book_values = []
		depreciations = []
		total_depreciations = []

		syd = (lifespan / 2) * (lifespan + 1)

		depreciations.append(c.pesos(0))
		total_depreciations.append(c.pesos(0))
		book_values.append(first_cost)

		for i in range(1 , lifespan + 1):
			depreciations.append(
				c.pesos(
					(first_cost.pesos - salvage_value.pesos) * (lifespan - i + 1) / (syd)
					)
				)

			total_depreciations.append(
				c.pesos(
					(first_cost.pesos - salvage_value.pesos) * ( i * (2 * lifespan - i + 1) ) / (2 * syd)
					)
				)

			book_values.append(
				c.pesos(
					first_cost.pesos - total_depreciations[i].pesos
					)
				)

		self.first_cost = first_cost
		self.salvage_value = salvage_value
		self.lifespan = lifespan
		self.book_values = book_values
		self.depreciations = depreciations
		self.total_depreciations = total_depreciations

class hipolito_2_1():
	def __init__(self):
		interest = c.pesos(ran.main(265))
		months = int(ran.main(4))
		principal = c.pesos(ran.main(15_000))

		self.question = f"""What is the annual rate of interest if {interest.pesos_string} is earned in {num2words(months)} months on an investment of {principal.pesos_string}?"""

		n = months / 12
		i = c.percentage(interest.pesos / (principal.pesos * n), 'decimal')

		self.answer = f"""{i.percent:4.4} %"""

class hipolito_2_2():
	def __init__(self):
		principal = c.pesos(ran.main(2000))
		months = int(ran.main(13))   
		interest_rate = c.percentage(ran.main(20), 'percent')

		future = c.pesos(principal.pesos * ( 1 + (months/12) * interest_rate.decimal))

		self.question = f"""A loan of {principal.pesos_string} is made for a period of {months} months, at a simple interest of {interest_rate.percent:4.4} %. What is the future amount is due at the end of the loan period?"""
		self.answer = f"""{future.pesos_string}"""

class hipolito_2_3():
	def __init__(self):
		interest_rate = c.percentage(ran.main(12), 'percent')
		future = c.pesos(ran.main(20_000))
		months = int(ran.main(9))

		present = c.pesos( future.pesos / ( 1 + (months / 12) * interest_rate.decimal))

		self.question = f"""If you borrow money from your friend with simple interest of {interest_rate.percent:4.4} %, find the present worth of {future.pesos_string}, which is due at the end of {num2words(months)} months."""

		self.answer = f"""{present.pesos_string}"""

class hipolito_2_4():
	def __init__(self):
		present = c.pesos(ran.main(5000))
		year = int(ran.main(2019))
		date_initial, date_final = ran.dates(year)
		interest_rate = c.percentage(ran.main(22), 'percent')

		delta = date_final - date_initial

		if is_leap(year) == False:
			days_per_year = 365
		else:
			days_per_year = 366

		interest = c.pesos(present.pesos * interest_rate.decimal * delta.days / days_per_year)

		self.question = f"""Determine the exact simple interest on {present.pesos_string} for the period from {date_initial.strftime('%B %d')} to {date_final.strftime('%B %d, %Y')}, if the rate of interest is {interest_rate.percent:4.4} %."""
		self.answer = f"""{interest.pesos_string}"""

class hipolito_2_5():
	def __init__(self):
		future = c.pesos(ran.main(200_000))
		method_1 = random.choice(COMPOUNDING_METHODS)
		interest_rate_1 = c.percentage(ran.main(10), 'percent')
		years_1 = int(ran.main(5))

		method_2 = random.choice(COMPOUNDING_METHODS)
		interest_rate_2 = c.percentage(ran.main(12), 'percent')
		years_2 = int(ran.main(5))

		principal_2 = compound(future, interest_rate_1, -years_1, method_1)
		principal_1 = compound(principal_2, interest_rate_2, -years_2, method_2)

		self.question = f"""A man wishes his son to receive {future.pesos_string} {num2words(years_1 + years_2)} years from now. What amount should he invest if it will earn interest of {interest_rate_1.percent:4.4} % compounded {method_1} during the first {years_1} years and {interest_rate_2.percent:4.4} % compounded {method_2} during the next {years_2} years?"""
		self.answer = f"""{principal_1.pesos_string}"""

class hipolito_2_6():
	def __init__(self):
		present = c.pesos(ran.main(25_000))
		years = round(ran.main(7.42),2)
		interest_rate = c.percentage(ran.main(8), 'percent')
		method, periods_per_year = compound_method()
		future = compound(present, interest_rate, years, method)

		self.question = f"""By the condition of a will, the sum of {present.pesos_string} is left to be held in trust be her guradian until it amounts to {future.pesos_string}. When will the girl receive the money if the fund is invested at {interest_rate.percent:4.4} % compounded {method}?"""
		self.answer = f"""{years} years"""

class hipolito_2_7():
	def __init__(self):
		method = random.choice(COMPOUNDING_METHODS)
		present = c.pesos(ran.main(5000))
		years_1 = int(ran.main(10))
		interest_rate = c.percentage(ran.main(14.35), 'percent')
		years_2 = int(years_1 + ran.main(5))
		future_1 = compound(present, interest_rate, years_1, method)
		future_2 = compound(present, interest_rate, years_2, method)

		self.question = f"""At a certain interest rate compounded {method}, {present.pesos_string} will amount to {future_1.pesos_string} after {num2words(years_1)} years. What is the amount at the end of {num2words(years_2)} years?"""
		self.answer = f"""{future_2.pesos_string}"""


class hipolito_2_8():
	def __init__(self):
		companies = COMPANY_NAMES
		company_a = companies.pop(random.randint(0, len(companies) -1))
		company_b = companies.pop(random.randint(0, len(companies)-1))

		#company_a perspective
		borrow_1 = c.pesos(ran.main(9000))
		borrow_2 = c.pesos(ran.main(12_000))
		payment_1 = c.pesos(ran.main(7000))
		#payment_2 = x
		payment_percentage = c.percentage(ran.main(50), 'percent')
		#payment_3 = percentage *  x  + x
		interest_rate = c.percentage(ran.main(12), 'percent')

		borrow_1_year = int(random.randint(YEAR_MIN, YEAR_MAX))
		borrow_2_year = borrow_1_year + random.randint(1,3)
		payment_1_year = borrow_2_year + random.randint(1,3)
		payment_2_year = payment_1_year + random.randint(1,3)
		payment_3_year = payment_2_year + random.randint(1,3)

		equation = sympy.Eq((1 + payment_percentage.decimal) * x + x * (1 + interest_rate.decimal)**(payment_3_year - payment_2_year) + payment_1.pesos * (1 + interest_rate.decimal)**(payment_1_year - payment_3_year) , borrow_2.pesos * ( 1 + interest_rate.decimal)**(payment_3_year - borrow_2_year) + borrow_1.pesos * (1 + interest_rate.decimal)**(payment_3_year - borrow_1_year))
		payment_1 = c.pesos(
			sympy.solveset(
				equation, x
				).args[0]
			)
		payment_2 = c.pesos(
			payment_1.pesos * (1 + payment_percentage.decimal)
			)

		self.question = f"""{company_a} borrowed {borrow_1.pesos_string} from {company_b} on Jan. 1, {borrow_1_year} and {borrow_2.pesos_string} on Jan. 1, {borrow_2_year}. {company_a} made a partial payment of {payment_1.pesos_string} on Jan. 1, {payment_1_year}. It was agreed that the balance of the loan would be amortized by two payments on of Jan. 1, {payment_2_year} and the other on Jan. 1, {payment_3_year}, the second being {payment_percentage.percent:4.4} % larger than the first. If the interest rate is {interest_rate.percent:4.4}%, what is the amount of each payment?"""
		self.answer = f"""{payment_1.pesos_string}, {payment_2.pesos_string}"""

class hipolito_2_9():
	def __init__(self):
		borrow_1 = c.pesos(ran.main(3000))
		due_1 = random.randint(1,5)
		interest_rate_1 = c.percentage(ran.main(12), 'percent')
		method_1 = random.choice(COMPOUNDING_METHODS)

		borrow_2 = c.pesos(ran.main(5000))
		due_2 = random.randint(1,5)
		interest_rate_2 = c.percentage(ran.main(12), 'percent')
		method_2 = random.choice(COMPOUNDING_METHODS)

		due_3 = due_2 + random.randint(1,5)
		interest_rate_3 = c.percentage(ran.main(16), 'percent')
		method_3 = random.choice(COMPOUNDING_METHODS)

		future_1 = compound(borrow_1, interest_rate_1, due_1, method_1)
		future_2 = compound(borrow_2, interest_rate_2, due_2, method_2)
		future_3 = c.pesos(
			compound(future_1, interest_rate_3, due_3 - due_1, method_3).pesos + compound(future_2, interest_rate_3, due_3 - due_2, method_3).pesos
			)

		self.question = f"""A woman borrowed {borrow_1.pesos_string} to be paid after {due_1} years with interest at {interest_rate_1.percent:4.4} % compounded {method_1} and {borrow_2.pesos_string} to be paid after {due_2} years at {interest_rate_2.percent:4.4} % compounded {method_2}. What single payment must she pay after {due_3} years at an interest rate of {interest_rate_3.percent:4.4} % compounded {method_3} to settle the two obligations?"""
		self.answer = f"""{future_3.pesos_string}"""

class hipolito_2_10():
	def __init__(self):
		borrow = c.pesos(ran.main(1342))
		payment = c.pesos(borrow.pesos + ran.main(158))
		discount_rate = c.percentage(
			(payment.pesos - borrow.pesos) / payment.pesos, 'decimal'
			)
		interest_rate = c.percentage( discount_rate.decimal / (1 - discount_rate.decimal), 'decimal')
		months = int(ran.main(9))
		rich_man = random.choice(RICH_MEN_NAMES)
		self.question = f"""Mr. {rich_man} borrowed money from a bank. He received from the bank {borrow.pesos_string} and promises to repay {payment.pesos_string} at the end of {months} months. Determine the simple interest rate and the corresponding discount rate or often referred to as the "Banker's Discount"."""
		self.answer = f"""{discount_rate.percent:4.4}%, {interest_rate.percent:4.4}%"""

class hipolito_2_11():
	def __init__(self):
		deposit = c.pesos(ran.main(50_000))
		interest_rate = c.percentage(ran.main(6), 'percent')
		method = random.choice(COMPOUNDING_METHODS)
		years = int(ran.main(5))
		inflation_rate = c.percentage(ran.main(6.5), 'percent')

		effective = eri(interest_rate, method)
		future = c.pesos(
			deposit.pesos * ((1 + effective.decimal)/(1 + inflation_rate.decimal))**(years)
			)

		self.question = f"""A man deposits {deposit.pesos_string} in a bank at {interest_rate.percent:4.4}% compounded {method} for {years} years. If the inflation rate of {inflation_rate.percent:4.4}% per year continues for this period, what is purchasing power of the original principal?"""
		self.answer = f"""{future.pesos_string}"""

class hipolito_2_12():
	def __init__(self):
		deposit = c.pesos(ran.main(600))
		methods = COMPOUNDING_METHODS
		method_1 = 'monthly'
		periods_per_year_1 = 12
		method_2, periods_per_year_2 = compound_method()
		years = int(ran.main(4))
		interest_rate = c.percentage(ran.main(12), 'percent')

		equation = sympy.Eq(
			(1 + x)**12 - 1 ,
			(1 + interest_rate.decimal/periods_per_year_2)**periods_per_year_2 - 1
			)
		print(sympy.solveset(equation, x, domain = sympy.S.Reals))

		positive_real = False
		i = 0
		while not positive_real:
			if sympy.solveset(equation, x, domain = sympy.S.Reals).args[i] >= 0:
				interest_rate_monthly = c.percentage(
					sympy.solveset(equation, x, domain = sympy.S.Reals).args[i]
				)
				positive_real = True
			i = i + 1


		future = move_payments(deposit, interest_rate_monthly, 1, years * 12, years * 12)

		self.question = f"""What is the future worth of {deposit.pesos_string} deposited at the end of every month for {years} years if the interest rate is {interest_rate.percent:4.4}% compounded {method_2}."""
		self.answer = f"""{future.pesos_string}"""

class hipolito_2_14():
	def __init__(self):
		annuity = c.pesos(ran.main(88_094.54))
		years = int(ran.main(15))
		interest_rate = c.percentage(ran.main(12), 'percent')
		present = move_payments(annuity, interest_rate, 1, years, 0)
		years_in_question = random.randint(1, years-1)
		present_in_question = move_payments(annuity, interest_rate, years_in_question + 1, years, 0)

		self.question = f"""{random.choice(RICH_MEN_NAMES)} borrows {present.pesos_string} at {interest_rate.percent:4.4}% compounded annually, agreeing to repay the loan in {years} equal annual payments. How much of the original principal is still unpaid after he has made the {num2words(years_in_question, to = 'ordinal')} payment?"""
		self.answer = f"""{present_in_question.pesos_string}"""



#this class is subject to review: 
#RECOMMENDATION: function reorganization
class hipolito_2_15():
	def __init__(self):

		person = random.choice(RICH_MEN_NAMES)

		downpayment = c.pesos(ran.main(200_000))
		annuity = c.pesos(ran.main(15_000))
		method, payments_per_year = compound_method()
		interest_per_year = c.percentage(ran.main(12), 'percent')
		interest_per_period = c.percentage(interest_per_year.percent/payments_per_year, 'percent')
		years = int(ran.main(10))
		total_payments = years * payments_per_year

		#what is the cash price of the lot?
		first_question = move_payments(annuity, interest_per_period, 1, total_payments, 0)

		#If person missed the first (1 < x < years * payments_per_year) payments,  what must he pay at the time the (x + 1)th is due to bring hum up to date?
		temp_2 = random.randint(2, total_payments - 2)
		second_question  = move_payments(annuity, interest_per_period, 1, temp_2 + 1, temp_2 + 1)

		#After making (1 < x < total_payments), person wished to discharge his remaining indebtness by a single payment at the time when the (x + 1) th regular payment was due what must he pay in addition to the regular payment then due?
		temp_3 = random.randint(2, total_payments - 2)
		third_question = move_payments(annuity, interest_per_period, temp_3 + 1, total_payments, temp_3 + 1)

		#If person missed the first X payments, what must he pay when the (X + 1)th payment is due to discharge his entire indebtness?
		temp_4 = random.randint(2, total_payments - 2)
		fourth_question = move_payments(annuity, interest_per_period, 1, total_payments, temp_4 + 1)

		self.question = f"""{person} purchased a small lot in a subdivision, paying {downpayment.pesos_string} down and promising to pay {annuity.pesos_string} every {12/payments_per_year} months for the next {years} years. THe seller figured interest at {interest_per_year.percent:4.4} % compounded {method}. a) What was the cash price of the lot? b) If {person} missed the first {temp_2} payments, what must he pay at the time the {num2words(temp_2 + 1, to = 'ordinal')} is due to bring him up to date? c) After making {temp_3} payments, {person} wished to discharge his remaining indebtness by a single payment at the time when the {num2words(temp_3 + 1, to = 'ordinal')} regular payment was due, what must he pay in addition to the regular payment then due? d) If {person} missed the first {temp_4} payments, what must he pay when the {num2words(temp_4 + 1, to = 'ordinal')} payment is due to discharge his entire indebtness?"""
		self.answer = f"""{first_question.pesos_string}, {second_question.pesos_string}, {third_question.pesos_string}, {fourth_question.pesos_string}"""


class hipolito_2_18():
	def __init__(self):
		payments_phase_1 = int(ran.main(2))
		phase_1 = c.pesos(ran.main(60_000))

		payments_phase_2 = int(ran.main(5))
		phase_2 = c.pesos(ran.main(90_000))

		payments_phase_3 = int(ran.main(5))
		phase_3 = c.pesos(ran.main(120_000))

		total_payments = payments_phase_1 + payments_phase_2 + payments_phase_3

		interest_per_year = c.percentage(ran.main(14), 'percent')
		method, periods_per_year = compound_method()
		interest_per_period = c.percentage(interest_per_year.percent/periods_per_year, 'percent')

		years = int(ran.main(12))
		total_periods = years * periods_per_year

		factor = (1 + interest_per_period.decimal)
		
		phase_1_present = move_payments(phase_1, interest_per_period, 1, payments_phase_1, 0)

		phase_2_present = move_payments(phase_2, interest_per_period, payments_phase_1 + 1, payments_phase_1 + payments_phase_2, 0)

		phase_3_present = move_payments(phase_3, interest_per_period, payments_phase_1 + payments_phase_2 + 1, payments_phase_1 + payments_phase_2 + payments_phase_3, 0 )

		present = c.pesos(phase_1_present.pesos + phase_2_present.pesos + phase_3_present.pesos)

		equivalent_uniform_annuity = c.pesos(
			present.pesos / (((1 + interest_per_period.decimal)**total_payments - 1)/(interest_per_period.decimal * (1 + interest_per_period.decimal)**(total_payments))) ) 

		self.question = f"""An asphalt road requires no upkeep until the end of {payments_phase_1} years when {phase_1.pesos_string} will be needed for repairs. After this, {phase_2.pesos_string} will be needed for repairs at the end of each year for the next {payments_phase_2} years, then {phase_3.pesos_string} at the end of each year for the next {payments_phase_3} years. If money is worth {interest_per_year.percent:4.4}% compounded {method},  what was the equivalent uniform annual cost for the {total_payments}-year period?"""

		self.answer = f"""{equivalent_uniform_annuity.pesos_string}"""

class hipolito_2_19():
	def __init__(self):


		withdraw_annuity = c.pesos(ran.main(18_000))

		deposit_year_start = int(ran.main(41))
		deposit_year_end = deposit_year_start + int(ran.main(10))

		withdraw_year_start = deposit_year_end + int(ran.main(10))
		withdraw_year_end = withdraw_year_start + int(ran.main(10))

		deposits = deposit_year_end - deposit_year_start + 1
		interest_per_year = c.percentage(ran.main(10), 'percent')

		withdraw_to_present = move_payments(withdraw_annuity, interest_per_year, withdraw_year_start, withdraw_year_end, deposit_year_start - 1)

		deposit_per_year = present_to_annuities(withdraw_to_present, interest_per_year, deposits)

		self.question = f"""A man wishes to provide a fund for his retirement such that from his {num2words(withdraw_year_start, to = 'ordinal')} to {num2words(withdraw_year_end, to = 'ordinal')} birthdays he will be able to withdraw equal sums of {withdraw_annuity.pesos_string} for his yearly expenses. He invests equal amount for his {num2words(deposit_year_start, to = 'ordinal')} to {num2words(deposit_year_end, to = 'ordinal')} birthdays in a fund earning {interest_per_year.percent:4.4} % compounded annually. How much should each of these amounts be?"""

		self.answer = f"""{deposit_per_year.pesos_string}"""


class hipolito_2_21():
	def __init__(self):
		payments = int(ran.main(6))
		annuity = c.pesos(ran.main(120_000))
		interest_per_year = c.percentage(ran.main(15), 'percent')

		present = move_payments(annuity, interest_per_year, 0, payments - 1, 0)

		future = move_payments(annuity, interest_per_year, 0, payments - 1, payments - 1)

		self.question = f"""Determine the present worth and the accumulated amount of an annuity consisting of {payments} payments of {annuity.pesos_string} each, the payments are made at the beggining of each year. Money is worth {interest_per_year.percent:4.4} % compounded annually."""
		self.answer = f"""{present.pesos_string}, {future.pesos_string}"""

class hipolito_2_22():
	def __init__(self):
		#capitalized cost

		initial_cost = c.pesos(ran.main(3_000_000))
		additional_cost = c.pesos(ran.main(100_000))
		additional_cost_interval = int(ran.main(10))
		initial_annual_operating_cost = c.pesos(ran.main(100_000))
		initial_duration = int(ran.main(4))
		thereafter_annual_operating_cost = c.pesos(ran.main(160_000))
		major_rework_cost = c.pesos(ran.main(300_000))
		major_rework_interval = int(ran.main(13))
		interest_per_year = c.percentage(ran.main(15), 'percent')


		first_cost = c.pesos(initial_cost.pesos + additional_cost.pesos / ((1 + interest_per_year.decimal)**additional_cost_interval - 1))

		present_worth_maintainance_cost = c.pesos(
			move_payments(initial_annual_operating_cost, interest_per_year, 1, initial_duration, 0).pesos + (thereafter_annual_operating_cost.pesos/interest_per_year.decimal)*(1 + interest_per_year.decimal)**(-initial_duration)
			)

		rework_cost = c.pesos(
			major_rework_cost.pesos / 
			((1 + interest_per_year.decimal)**major_rework_interval - 1)
			)

		capitalized_cost = c.pesos(
			first_cost.pesos + present_worth_maintainance_cost.pesos + rework_cost.pesos
			)

		self.question = f"""Calculate the capitalized cost of a project that has an initial cost of {initial_cost.pesos_string} and an additional cost of {additional_cost.pesos_string} at the end of every {additional_cost_interval} years. The annual operating costs will be {initial_annual_operating_cost.pesos_string} at the end of every year for {initial_duration} years and {thereafter_annual_operating_cost.pesos_string} thereafter. In addition, there is expected to be recurring major rework cost of {major_rework_cost.pesos_string} every {major_rework_interval} years. Assume i = {interest_per_year.percent:4.4}%"""
		self.answer = f"""{capitalized_cost.pesos_string}"""

class hipolito_2_23():
	def __init__(self):
		philantropist_money = c.pesos(ran.main(5_000_000))
		facilities_cost = c.pesos(ran.main(1_200_000))
		capital_replacement = c.pesos(ran.main(100_000))
		capital_replacement_interval = int(ran.main(5))
		interest_per_year = c.percentage(ran.main(12), 'percent')

		annuity = c.pesos(
			philantropist_money.pesos * interest_per_year.decimal
			)

		total_cost = c.pesos(
			facilities_cost.pesos + capital_replacement.pesos/((1 + interest_per_year.decimal)**capital_replacement_interval - 1)
			)

		total_cost_annuity = c.pesos(
			total_cost.pesos * interest_per_year.decimal
			)

		year_end_amount = c.pesos(annuity.pesos - total_cost_annuity.pesos)

		self.question = f"""The will of a wealthy philantropist left {philantropist_money.pesos_string} to establish a perpetual charitable foundation. The foundation trustees decided to spend {facilities_cost.pesos_string} to provide facilities immediately and to provide {capital_replacement.pesos_string} of capital replacement at the end of each {capital_replacement_interval} year period. If the invested funds earned {interest_per_year.percent:4.4}% per annum, what would be the year end amount available in perpetuity from the endowment for charitable purposes?"""
		self.answer = f"""{year_end_amount.pesos_string}"""


class hipolito_3_1():
	def __init__(self):
		lifespan = int(ran.main(20))
		now = random.randint(1, lifespan - 1)
		first_cost = c.pesos(ran.main(60_000))
		salvage_value = c.pesos(ran.main(20_000))
		cost_of_alternative = c.pesos(first_cost.pesos + ran.main(40_000))
		
		machine_shop = Straight_Line_Depreciation(first_cost, salvage_value, lifespan)

		book_value_now = machine_shop.book_values[now]
		new_capital_required = c.pesos(cost_of_alternative.pesos - book_value_now.pesos)

		self.question = f"""A machine shop purchased {now} years ago a milling machine for {first_cost.pesos_string}. A straight line depreciation reserve had been provided based on a {lifespan}-year of the machine. THe owner of the machine shop desires to replace the old milling machine with a modern unit having many advantages costing {cost_of_alternative.pesos_string}. It can sell the old unit for {salvage_value.pesos_string}. How much new capital will be required for the purchase?"""
		self.answer = f"""{new_capital_required.pesos_string}"""

class hipolito_3_2():
	def __init__(self):
		power = c.power(ran.main(30), 'hp')
		tax_and_importation_cost = c.pesos(ran.main(360_000))
		bank_charge_cost = c.pesos(ran.main(5_000))
		installation_cost = c.pesos(ran.main(25_000))
		incidental_cost = c.pesos(ran.main(20_000))
		salvage_value = c.pesos(ran.main(60_000))
		lifespan = int(ran.main(20))
		years_in_question = random.randint(1, lifespan - 1)

		first_cost = c.pesos(tax_and_importation_cost.pesos + bank_charge_cost.pesos + installation_cost.pesos + incidental_cost.pesos )
		sand_mill = Straight_Line_Depreciation(first_cost, salvage_value, lifespan)

		self.question = f"""A tax and duty free importation of a {power.hp:4.4} horsepower sand mill for paint manufacturing costs {tax_and_importation_cost.pesos_string}. Bank charges, arrester and brokerage cost {bank_charge_cost.pesos_string}. Foundation and installation costs were {installation_cost.pesos_string}. Other incidental expenses amount to {incidental_cost.pesos_string}. Salvage value of the mill is estimated to be {salvage_value.pesos_string} after {lifespan} years. Find the appraisal value of the mill using straight-line depreciation of the end of {years_in_question} years."""
		self.answer = f"""{sand_mill.book_values[years_in_question].pesos_string}"""

class hipolito_3_3():
	def __init__(self):
			original_cost = c.pesos(ran.main(65_000))
			shipping_cost = c.pesos(ran.main(2_000))
			installation_cost = c.pesos(ran.main(3_000))

			#1
			lifespan = int(ran.main(10))
			salvage_value = c.pesos(ran.main(5_000))

			#2
			interest_rate = c.percentage(ran.main(5), 'percent')

			first_cost = c.pesos(original_cost.pesos + shipping_cost.pesos + installation_cost.pesos)

			depreciation_straight_line = c.pesos(
				first_cost.pesos - salvage_value.pesos / lifespan 
				)

			depreciation_sinking_fund = c.pesos(
				(first_cost.pesos - salvage_value.pesos) * (interest_rate.decimal) / ((1 + interest_rate.decimal)**lifespan - 1)
				)

			self.question = f"""Power to a remote transmitting station is provided by a Diesel-generator unit. The original cost of the unit is {original_cost.pesos_string}. It costs {shipping_cost.pesos_string} to ship the unit to the job site. An additional cost of {installation_cost.pesos_string} was incurred for installation. 
a) Determine the annual depreciation cost by the straight-line depreciation method, if the unit has an expected life of {lifespan} years. The salvage value of the unit at the end of its life was estimated to be {salvage_value.pesos_string}.
b) Determine the annual depreciation cost by the sinking fund method. Assume that the annual charge for depreciation was deposited in a fund drawing compound interest at the rate of {interest_rate.percent:4.4}%. """

			self.answer = f"""{depreciation_straight_line.pesos_string}, {depreciation_sinking_fund.pesos_string}"""

class hipolito_3_5():
	def __init__(self):
		generator_cost = c.pesos(ran.main(90_000))
		installation_cost = c.pesos(ran.main(10_000))
		generator_lifespan = int(ran.main(17))
		lifespan = generator_lifespan
		salvage_value = c.pesos(ran.main(5_000))

		first_cost = c.pesos(generator_cost.pesos + installation_cost.pesos)

		year_in_question = random.randint(2, generator_lifespan - 1)

		declining_balance = Declining_Balance_Depreciation(first_cost, salvage_value, lifespan)

		double_declining_balance = Double_Declining_Balance_Depreciation(first_cost, salvage_value, lifespan)

		interest_rate = c.percentage(ran.main(12), 'percent')
		sinking_fund = Sinking_Fund_Depreciation(first_cost, salvage_value, lifespan, interest_rate)

		sum_of_the_years = Sum_Of_The_Years_Depreciation(first_cost, salvage_value, lifespan)

		print_depreciation_sched(declining_balance)
		print()
		print_depreciation_sched(double_declining_balance)
		print()
		print_depreciation_sched(sinking_fund)
		print()
		print_depreciation_sched(sum_of_the_years)
		print()

		self.question = f"""An industrial plant bought a generator set for {generator_cost.pesos_string}. Other expenses including installation amounted to {installation_cost.pesos_string}. The generator set is to have a life of {lifespan} years with a salvage value at the end of life of {salvage_value.pesos_string}. Determine the depreciation charge during the {num2words(year_in_question, to = 'ordinal')} year and the book value at the end of {year_in_question} years by the 
i) declining balance method
ii) double declining balance method
iii) sinking fund method at {interest_rate.percent:4.4} %
iv) SYD method."""
		self.answer = f"""i) {declining_balance.depreciations[year_in_question].pesos_string}, {declining_balance.book_values[year_in_question].pesos_string}
ii) {double_declining_balance.depreciations[year_in_question].pesos_string}, {double_declining_balance.book_values[year_in_question].pesos_string}
iii) {sinking_fund.depreciations[year_in_question].pesos_string}, {sinking_fund.book_values[year_in_question].pesos_string}
iv) {sum_of_the_years.depreciations[year_in_question].pesos_string}, {sum_of_the_years.book_values[year_in_question].pesos_string}"""

class hipolito_3_6():
	def __init__(self):
		original_cost = c.pesos(ran.main(6_000_000))
		installation_cost_percentage = c.percentage(ran.main(3), 'percent')
		lifespan = int(ran.main(8))
		salvage_value_percentage = c.percentage(ran.main(5), 'percent')
		installation_cost = c.pesos(original_cost.pesos * installation_cost_percentage.decimal )
		first_cost = c.pesos(original_cost.pesos + installation_cost.pesos)
		salvage_value = c.pesos(first_cost.pesos * salvage_value_percentage.decimal)

		straight_line = Straight_Line_Depreciation(first_cost, salvage_value, lifespan)

		syd = Sum_Of_The_Years_Depreciation(first_cost, salvage_value, lifespan)
		year_in_question = random.randint(2, lifespan - 2)

		print_depreciation_sched(straight_line)
		print()
		print_depreciation_sched(syd)
		print()

		self.question = f"""A telephone company purchased a microwave radio equipment for {original_cost.pesos_string}. Freight and installation charges amounted to {installation_cost_percentage.percent:4.4}% of the purchased price. If the equipment shall be depreciated over a period of {lifespan} years  with a salvage value of {salvage_value_percentage.percent:4.4}%, determine the following:
a) Annual depreciation charge using the straight line method.
b) Depreciation charge during the {num2words(year_in_question, to = 'ordinal')} year using the sum-of-the year's digits method."""
		self.answer = f"""{straight_line.depreciations[1].pesos_string}, {syd.depreciations[year_in_question].pesos_string}"""









		














