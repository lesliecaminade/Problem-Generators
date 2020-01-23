from generator import random_handler as ran
import sympy
import math
import random
from generator import constants_conversions as c
from num2words import num2words
from mathsub.discrete_math_engine import combination as com
from mathsub.discrete_math_engine import permutation as per
import fractions

x, y, z = sympy.symbols('x y z', real = True)#generic variables

NUM_MIN = 1
NUM_MAX = 99

VENN_MIN = 100
VENN_MAX = 500

def rp():
	#random probability
	denom = random.randint(10,50)
	return fractions.Fraction(random.randint(1,denom),denom)

class Probability():
	def __init__(self):
		pass

	def init_random(self):
		total = random.randint(10, 100)
		success = random.randint(1, total - 1)
		p = success / total
		ow = success / (total - success)
		oa = (total - success) / success
		q = 1 - (success / total)

		self.p = fractions.Fraction(p).limit_denominator(100_000_000)
		self.q = fractions.Fraction(q).limit_denominator(100_000_000)
		self.ow = fractions.Fraction(ow).limit_denominator(100_000_000)
		self.oa = fractions.Fraction(oa).limit_denominator(100_000_000)

	def init_define(self, success, total):
		p = success / total
		ow = success / (total - success)
		oa = (total - success) / success
		q = 1 - (success / total)

		self.p = fractions.Fraction(p).limit_denominator(100_000_000)
		self.q = fractions.Fraction(q).limit_denominator(100_000_000)
		self.ow = fractions.Fraction(ow).limit_denominator(100_000_000)
		self.oa = fractions.Fraction(oa).limit_denominator(100_000_000)

	def init_define_float(self, probability):
		p = probability
		q = 1 - probability
		# ow = p / q
		# oa = q / p

		self.p = p
		self.q = q
		# self.ow = ow
		# self.oa = oa

	def intersect(self, probability_object):
		return Probability(self.p * probability_object.p)

	def union(self, probability_object):
		return Probabilty(self.p + probability_object.p)


class Dice_Sum():
	def __init__(self):
		self.DESC = [i for i in range(2, 13)]
		self.universe = set(
			[(i, j) for i in range(1,7) for j in range(1, 7)]
			)

		sums = []
		sums.append(None)
		sums.append(None)
		for a in range(2, 13):
			sums.append(set([(i, j) for i in range(1,7) for j in range(1, 7) if i + j == a]))

		self.sums = sums

		self.doubles = set([(i, i) for i in range(1, 7)])

	def init_dice(self, dice):
		if dice == 3:
			self.universe = set(
				[(i, j, k) for i in range(1,7) for j in range(1, 7) for k in range(1,7)]
				)


			sums = []
			sums.append(None)
			sums.append(None)
			sums.append(None)
			for a in range(3, 19):
				sums.append(set([(i, j, k) for i in range(1,7) for j in range(1, 7) for k in range(1,7) if i + j + k == a]))

			self.sums = sums

			self.triples = set([(i, i, i) for i in range(1, 7)])


		else:
			pass

class Number_Select():
	def __init__(self, divisible_by, **kwargs):

		num_min = random.randint(NUM_MIN, NUM_MAX)
		num_max = random.randint(NUM_MIN, NUM_MAX)


		for key, value in kwargs.items():
			if key == 'min':
				num_min = value
			elif key == 'max':
				num_max = value
			else:
				pass

		if num_min > num_max:
			num_min, num_max = num_max, num_min

		count = 0
		for num in range(num_min, num_max + 1):
			if num % divisible_by == 0:
				count = count  + 1

		p = fractions.Fraction(count , (num_max - num_min + 1))

		self.range = f"""{num_min} to {num_max} inclusive"""
		self.p = p

class Numbers():
	def __init__(self):
		num_min = random.randint(NUM_MIN, NUM_MAX)
		num_max = random.randint(NUM_MIN, NUM_MAX)
		if num_min > num_max:
			num_min, num_max = num_max, num_min
		PRIME_MAX = NUM_MAX
		self.descriptions = ['even', 'odd', 'prime']
		self.universe = set([i for i in range(num_min, num_max + 1)])
		self.even = set([i for i in range(num_min, num_max + 1) if i%2 == 0])
		self.odd = set([i for i in range(num_min, num_max + 1) if i%2 == 1])
		self.prime = set([p for p in range(num_min,num_max + 1) if 0 not in [p%d for d in range(2,p)]])
		self.min = num_min
		self.max = num_max

		self.sets = {'even':self.even, 'odd':self.odd, 'prime':self.prime}

	def multiple(self, num):
		return set([i for i in range(self.min, self.max + 1) if i%num == 0])


	
def pick_two_divisors():
	numbers_possible = [i for i in range(1, 11)]
	divisor_1 = numbers_possible.pop(random.randint(0, len(numbers_possible) - 1))
	divisor_2 = numbers_possible.pop(random.randint(0, len(numbers_possible) - 1))
	return divisor_1, divisor_2

class Multinomial():
	def __init__(self):
		pass

	def init_2(self, trials, success, p, *args):
		#this is technically a binomial distribution
		return com(trials, success) * p**success * (1 - p)**(trials - success)

	def init_3(self, s1, s2, s3, p1, p2, p3, *args):
		#this is a 3 variable normal distribution
		trials = s1 + s2 + s3
		return (math.factorial(trials)/(math.factorial(s1) * math.factorial(s2) * math.factorial(s3))) * p1**s1 * p2**s2 * p3**s3

class Hypergeometric():
	def __init__(self):
		pass

	def init_2 (self, n1, n2, r1, r2):
		p = fractions.Fraction((com(n1, r1) * com(n2, r2)),( com (n1 + n2, r1 + r2)))
		return p

	def init_3 (self, n1, n2, n3, r1, r2, r3):
		p = fractions.Fraction(com(n1, r1) * com(n2, r2) * com(n3, r3) , com(n1 + n2 + n3, r1 + r2 + r3))
		return p

class Expectation():
	def __init__(self):
		pass

	def init_2(self, fake_win, pwin, plose):
		#this function solves for the fair price of the lottery ticket (or any equivalent)
		net_win = fake_win.pesos - net_lose.pesos
		equation = sympy.Eq(
			(net_win * pwin), 
			x * plose
			)

		net_lose = sympy.solveset(equation, x).args[0]
		return c.pesos(net_lose)

	def init_3(self, fake_win_1, fake_win_2, pwin_1, pwin_2,  plose):
		#this function solves for the fair price of the lottery ticket (or any equivalent)

		equation = sympy.Eq(
			((fake_win_1.pesos - x) * pwin_1) + ((fake_win_2.pesos - x) * pwin_2),
			x * plose
			)

		net_lose = sympy.solveset(equation, x).args[0]
		return c.pesos(net_lose)

class Deck():
	def __init__(self):
		self.cards = 52
		self.SUITS = ['spade', 'clubs', 'hearts', 'diamonds']
		self.SUITS_PLUS = ['spade', 'clubs', 'hearts', 'diamonds', 'face']
		self.RANKS = [i for i in range(1, 14)]
		#spades, clubs, hearts, diamonds
		self.suits = {'spade':13, 'clubs':13, 'hearts':13, 'diamonds':13, 'face':12}
		#none aces, two, three,...,king
		self.ranks = [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
		self.face = 12

		# print(self.suits)
		# print(self.ranks)
		# print(self.face)

	def probability(self, desc):
		
		if type(desc) == str:
			p = fractions.Fraction(self.suits[desc], self.cards)
		else:
			p = fractions.Fraction(self.ranks[desc], self.cards)
		return p

	def draw(self, desc):
		self.cards = self.cards - 1
		for key in self.SUITS_PLUS:
			if desc == key:
				self.suits[key] = self.suits[key] - 1
				# print(self.suits)
		if type(desc) == int:
			self.ranks[desc] = self.ranks[desc] - 1
			# print(self.ranks)

			if desc > 10:
				self.face = self.face - 1
				# print(self.face)

class Die():
	def __init__(self):
		self.DESC = ['odd number', 'even number', 1, 2, 3, 4, 5, 6, 'prime number', 'composite number']

	def probability(self, desc):
		if desc == 'odd number' or desc == 'even number':
			return fractions.Fraction(1,2)
		
		elif desc == 1 or desc == 2 or desc == 3 or desc == 4 or desc == 5 or desc == 6:
			return fractions.Fraction(1,6)

		elif desc == 'prime number':
			return fractions.Fraction(1,2)

		elif desc == 'composite number':
			return fractions.Fraction(1,2)

		else:
			pass

class Coin():
	def __init__(self):
		self.DESC = ['heads', 'tails']

	def probability(self, desc):
		if desc == 'heads' or desc == 'tails':
			return fractions.Fraction(1,2)

class Venn_Diagram():
	def __init__(self):
		pass

	def init_random(self, sets ,others = False):
		def pick():
			return random.randint(VENN_MIN, VENN_MAX)

		def pick_lower():
			return random.randint(VENN_MIN, int(VENN_MAX/3))


		a = pick()
		b = pick()

		if sets == 3:
			c = pick()
		else:
			c = 0

		abnotc = pick_lower()

		if sets == 3:
			acnotb = pick_lower()
			bcnota = pick_lower()
			abc = pick_lower()
		else:
			acnotb = 0
			bcnota = 0
			abc = 0

		if others:
			outside = pick_lower()



		A = a + abnotc + acnotb
		B = b + abnotc + bcnota
		C = c + acnotb + bcnota

		self.A = A
		self.B = B
		self.C = C
		self.U = a + b + c + abnotc + acnotb + bcnota + outside

		self.AB = abnotc + abc
		self.AC = acnotb + abc
		self.BC = bcnota + abc
		self.ABC = abc

		self.others = outside
		self.other = outside


class rgs_sample_1():
	def __init__(self):
		dice = Dice_Sum()
		e1 = random.choice(dice.DESC)
		events = dice.sums[e1]
		samples = dice.universe
		p = fractions.Fraction(len(events), len(samples))

		self.question = f"""Roll a pair of dice one time. What is the probability of getting a sum of {e1}?"""
		self.answer = f"""{p}"""

class rgs_sample_2():
	def __init__(self):
		numbers_possible = [i for i in range(1, 11)]
		num_min = random.randint(NUM_MIN, NUM_MAX)
		num_max = random.randint(NUM_MIN, NUM_MAX)
		if num_min > num_max:
			num_min, num_max = num_max, num_min

		divisor_1, divisor_2 = pick_two_divisors()
		number_select_1 = Number_Select(divisor_1, min = num_min, max = num_max)
		number_select_2 = Number_Select(divisor_2, min = num_min, max = num_max)


		self.question = f"""A number from {number_select_1.range} is randomly selected. What is the probability that it will be divisible by {divisor_1} and {divisor_2}?"""
		self.answer = f"""{number_select_1.p * number_select_2.p}"""

class rgs_sample_2b():
	def __init__(self):
		numbers_possible = [i for i in range(1, 11)]
		num_min = random.randint(NUM_MIN, NUM_MAX)
		num_max = random.randint(NUM_MIN, NUM_MAX)
		if num_min > num_max:
			num_min, num_max = num_max, num_min

		divisor_1, divisor_2 = pick_two_divisors()
		number_select_1 = Number_Select(divisor_1, min = num_min, max = num_max)
		number_select_2 = Number_Select(divisor_2, min = num_min, max = num_max)


		self.question = f"""A number from {number_select_1.range} is randomly selected. What is the probability that it will be divisible by {divisor_1} and {divisor_2}?"""
		self.answer = f"""{number_select_1.probability + number_select_2.probability - (number_select_1.probability * number_select_2.probability):4.4}"""


class rgs_sample_3():
	def __init__(self):
		committee = Hypergeometric()
		men = random.randint(10, 15)
		women = random.randint(10, 15)
		men_select = random.randint(1,10)
		women_select = random.randint(1,10)
		p = committee.init_2(men, women, men_select, women_select)

		self.question = f"""A committee of {men_select + women_select} is to be selected from a group of {men} men and {women} women. If the selection is made randomly, what is the probability that the committee consists of {men_select} men and {women_select} women?"""
		self.answer = f"""{p}"""

class rgs_sample_4():
	def __init__(self):
		probability = Probability()
		probability.init_random()
		self.question = f"""If the odds against event E are {probability.oa}, find the probability of success."""
		self.answer = f"""{probability.p}"""

class rgs_sample_5():
	def __init__(self):
		second_prize = c.pesos(ran.main(2000))
		first_prize = c.pesos(second_prize.pesos + ran.main(3000))

		probability_1st = 0.001
		probability_2nd = 0.003
		plose = 1 - probability_1st - probability_2nd

		expectation = Expectation()
		ticket_price = expectation.init_3(first_prize, second_prize, probability_1st, probability_2nd, plose)

		self.question = f"""A man purchases a raffle ticket, he can win a first prize of {first_prize.pesos_string} or a second prize of {second_prize.pesos_string} with probabilities {probability_1st:4.8} and {probability_2nd:4.8}. What should be the fair price to pay for the ticket?"""
		self.answer = f"""{ticket_price.pesos_string}"""

class rgs_sample_6():
	def __init__(self):
		deck = Deck()
		suit = random.choice(deck.SUITS)
		rank = random.randint(1,13)
		p1 = deck.probability(suit)
		p2 = deck.probability(rank)
		p = p1 + p2 - p1 * p2
		self.question = f"""One card is drawn from a standard deck of 52 playing cards. What is the probability that the card drawn is either a {suit} card or a {num2words(rank)} card?"""
		self.answer = f"""{p}"""

class rgs_sample_6b():
	def __init__(self):
		deck = Deck()
		suit = random.choice(deck.SUITS)
		rank = random.randint(1,13)
		p1 = deck.probability(suit)
		p2 = deck.probability(rank)
		p = p1 * p2
		self.question = f"""One card is drawn from a standard deck of 52 playing cards. What is the probability that the card drawn is a {suit} card and a(n) {num2words(rank)} card?"""
		self.answer = f"""{p}"""

class rgs_sample_7():
	def __init__(self):
		deck = Deck()
		ranks = deck.RANKS
		rank_1 = ranks.pop(random.randint(0, len(ranks) - 1))
		rank_2 = ranks.pop(random.randint(0, len(ranks) - 1))
		suit = random.choice(deck.SUITS)

		p1 = deck.probability(rank_1)
		p2 = deck.probability(rank_2)
		p3 = deck.probability(suit)

		p = p1 + p2 + p3 - (p1*p3 + p2*p3)
		#p1p2 is not present since ranks have no intersection

		self.question = f"""A single card is drawn from a standard 52-card deck. Determine the probability that the single card drawn is a(n) {num2words(rank_1)}, a(n) {num2words(rank_2)}, or a {suit}."""
		self.answer = f"""{p}"""

class rgs_sample_8():
	def __init__(self):
		#hyper = Hypergeometric()
		deck = Deck()

		draw_consecutive_suit = random.choice(deck.SUITS_PLUS)
		p1 = deck.probability(draw_consecutive_suit)
		deck.draw(draw_consecutive_suit)
		p2 = deck.probability(draw_consecutive_suit)

		p = p1 * p2

		self.question = f"""John draws two cards from a pack of playing cards (jokers excluded). If John will not replace the first drawn card back to the pack before drawing the second card, what is the probability that both cards are {draw_consecutive_suit} cards?"""
		self.answer = f"""{p}"""

class rgs_sample_9():
	def __init__(self):
		hyper = Hypergeometric()
		black_balls = random.randint(5,15)
		white_balls = random.randint(5,15)
		black_select = random.randint(1, black_balls)
		white_select = random.randint(1, white_balls)

		p = hyper.init_2(black_balls, white_balls, black_select, white_select)

		self.question = f"""A bag contains {black_balls} black balls and {white_balls} white balls. If {white_select + black_select} balls are drawn in succession without replacement, what is the probability that there are {black_select} black balls and {white_select} white balls?"""
		self.answer = f"""{p}""" 

#rgs sample_10_is just a duplicate of rgs_9 with different set of given values

class rgs_sample_11():
	def __init__(self):
		multinomial = Multinomial()
		p_pass = fractions.Fraction(random.randint(1,9), 10)
		trials = random.randint(5,15)
		passers = random.randint(1, trials - 1)

		p = 0
		for i in range(passers, trials + 1):
			p = p + multinomial.init_2(trials, i, p_pass)

		self.question = f"""If the probability that the average freshman will not complete 5 years of engineering course is {1 - p_pass}, what is the probability that in every {trials} freshmen at least {passers} will complete the 5-year course?"""
		self.answer = f"""{p}"""

class rgs_sample_12():
	def __init__(self):
		average = random.randint(1,10)
		p_faulty = fractions.Fraction(average,1000)
		trials = int(ran.main(200))
		faulties = random.randint(1, 10)
		
		multi = Multinomial()
		p = 0
		for i in range(faulties, trials + 1):
			p = p + multi.init_2(trials, i, p_faulty)

		self.question = f"""A manufacturer has determined that a certain machine averages {num2words(average)} faulty resistor for every 1000 it produces. What is the probability that an order of {trials} resistors will have {faulties} or more faulty resistors?"""
		self.answer = f"""{float(p):4.4}"""

class rgs_2():
	def __init__(self):
		greater_than = random.randint(2,5)
		count = 0
		for i in range(greater_than + 1, 7):
			count = count + 1

		p = count * fractions.Fraction(1,6)
		self.question = f"""When a die is rolled, the probability of getting a number greater than {greater_than}"""
		self.answer = f"""{p}"""

class rgs_3():
	def __init__(self):
		coins_tossed = random.randint(2, 10)
		heads = random.randint(1, coins_tossed)
		tails = coins_tossed - heads

		multinomial = Multinomial()
		p = multinomial.init_2(coins_tossed, heads, fractions.Fraction(1,2))
		self.question = f"""When {coins_tossed} coins are tossed, the probability of getting {heads} heads is"""
		self.answer = f"""{p}"""

class rgs_5():
	def __init__(self):
		die = Die()
		coin = Coin()
		die_desc = random.choice(die.DESC)
		coin_desc = random.choice(coin.DESC)
		p1 = die.probability(die_desc)
		p2 = coin.probability(coin_desc)
		p = p1 * p2
		self.question = f"""When a coin is tossed and a die is rolled, the probability of getting a {coin_desc} on the coin and {die_desc} on the die is"""
		self.answer = f"""{p}"""

class rgs_6():
	def __init__(self):
		die = Dice_Sum()
		descriptions = die.DESC
		e1 = descriptions.pop(random.randint(0, len(descriptions) - 1))
		e2 = descriptions.pop(random.randint(0, len(descriptions) - 1))
		results_1 = die.sums[e1]
		results_2 = die.sums[e2]

		#print('results_1 ', results_1)
		results = results_1.union(results_2)

		p = fractions.Fraction(len(results),len(die.universe))

		self.question = f"""If two dice are tossed, find the probability of rolling a sum of either {e1} or {e2}."""
		self.answer = f"""{p}"""

class rgs_7():
	def __init__(self):
		die = Dice_Sum()
		e = random.choice(die.DESC)
		events = die.sums[e]
		samples = die.universe
		p = fractions.Fraction(len(events), len(samples))

		self.question = f"""Roll a pair of fair dice one time. What is the probability that the sum of the two numbers is {e}?"""

		self.answer = f"""{p}"""

class rgs_8():
	def __init__(self):
		similar_cards = random.randint(1,4)
		deck = Deck()
		ranks = deck.RANKS
		rank = ranks.pop(random.randint(0, len(ranks) - 1))

		p = 1
		for i in range(similar_cards):
			p = p * deck.probability(rank)
			deck.draw(rank)

		for i in range(similar_cards + 1, 5 + 1):
			p = p * (1 - deck.probability(rank))
			deck.draw(random.choice(ranks))

		self.question = f"""What is the probability of obtaining a poker hand (5 cards) containing {similar_cards} {num2words(rank)}s?"""
		self.answer = f"""{p}"""

class rgs_9():
	def __init__(self):
		multi = Multinomial()
		p_boy = fractions.Fraction(1,2)

		children = random.randint(3,12)
		a = random.randint(1, children - 1)
		b = children - a

		p1 = multi.init_2(children, a, p_boy)
		p2 = multi.init_2(children, b, p_boy)
		p = p1 + p2

		self.question = f"""In a family of {num2words(children)}, what is the probability of having a set of {num2words(a)} and {num2words(b)}. ({num2words(a)} son(s) and {num2words(b)} daughter(s) or {num2words(b)} son(s) and {num2words(a)} daughter(s) )."""
		self.answer = f"""{p}"""

class rgs_10():
	def __init__(self):
		hyper = Hypergeometric()
		blacks = random.randint(5, 20)
		whites = random.randint(5, 20)
		select_black = random.randint(1,blacks)
		select_white = random.randint(1,whites)

		p = hyper.init_2(blacks, whites, select_black, select_white)

		self.question = f"""An urn contains {blacks} black balls and {whites} white balls. What is the probability of getting {select_black} black ball(s) and {select_white} white ball(s) in {select_black + select_white} consecutive draws from the urn?"""
		self.answer = f"""{p}"""

class rgs_11():
	def __init__(self):
		multi = Multinomial()
		blacks = random.randint(5, 20)
		whites = random.randint(5, 20)
		select_black = random.randint(1,blacks)
		select_white = random.randint(1,whites)
		p = multi.init_2(blacks + whites, select_black, fractions.Fraction(blacks, blacks + whites))

		self.question = f"""From a bag containing {blacks} black balls and {whites} white balls, {num2words(select_black + select_white)} balls are drawn one at a time. Find the probability that {num2words(select_black)} balls are black and {num2words(select_white)} balls are white. Assume that all balls are returned before the next ball is taken."""
		self.answer = f"""{float(p):4.4}"""

class rgs_12():
	def __init__(self):
		ave_hits = random.randint(1,9)
		p_hit = fractions.Fraction(ave_hits, 10)

		trials = random.randint(5,15)
		hits = random.randint(1, trials - 1)

		multi = Multinomial()
		p = multi.init_2(trials, hits, p_hit)

		self.question = f"""If probability that a missile will hit the target is {p_hit}, find the probability of exactly {hits} hits out of {trials} tries."""
		self.answer = f"""{float(p):4.4}"""

class rgs_13():
	def __init__(self):
		p = fractions.Fraction(random.randint(1,11), 12)
		q = fractions.Fraction(random.randint(1,11), 12)

		self.question = f"""In a shooting game, the probabilities that Roger and Joel will hit a target are {p} and {q} respectively. What is the probability that the target is hit when both shoot at it?"""
		self.answer = f"""{p + q - p * q}"""

class rgs_14():
	def __init__(self):
		repeat = True
		while repeat:
			p = rp()
			q = rp()
			r = rp()
			s = rp()
			if float(p + q + r + s) < 1:
				repeat = False

		proba = p + q + r + s 

		self.question = f"""In a race for mayor, four candidates A, B, C, and D, have probabilities of {p}, {q}, {r}, and {s} of winning respectively. What is the probability that A, B, C, or D will win?"""
		self.answer = f"""{proba}"""

class rgs_15():
	def __init__(self):
		p_credit = rp()

		multi = Multinomial()
		trials = random.randint(5,15)
		at_least = random.randint(1, trials - 1)

		p = 0
		for i in range(at_least, trials + 1):
			p = p + multi.init_2(trials, i, p_credit)

		self.question = f"""The probability of getting a credit in an examination is {p_credit}. If three students are selected at random, what is the probability that at least {num2words(at_least)} of them got a credit?"""
		self.answer = f"""{float(p):4.8}"""

class rgs_16():
	def __init__(self):
		p_girl = fractions.Fraction(1,2)

		children = random.randint(3,12)
		at_least = random.randint(1, children - 1)

		multi = Multinomial()
		p = 0
		for i in range(at_least, children + 1):
			p = p + multi.init_2(children, i, p_girl)

		self.question =f"""Find the probability that a couple having {children} children will have at least {num2words(at_least)} girl(s)."""
		self.answer = f"""{p}"""

class rgs_17():
	def __init__(self):
		p_win = fractions.Fraction(2,6)
		p_lose = fractions.Fraction(4,6)

		dice = [i for i in range(6)]
		d1 = dice.pop(random.randint(0, len(dice) - 1))
		d2 = dice.pop(random.randint(0, len(dice) - 1))

		ticket_price = c.pesos(ran.main(5))
		fake_win = c.pesos(ticket_price.pesos + ran.main(10))

		winning = c.pesos((fake_win.pesos - ticket_price.pesos) * p_win - ticket_price.pesos * p_lose)

		self.question = f"""In a dice game, one fair die is used. The player wins {fake_win.pesos_string} if he rolls either a {d1} or a {d2}. He loses {ticket_price.pesos_string} if he turns up any other face. What is the expected winning for one roll of the die?"""
		self.answer = f"""{winning.pesos_string}"""

class rgs_18():
	def __init__(self):
		trials = random.randint(10, 50)
		corrects = random.randint(1, trials - 1)
		p_correct = fractions.Fraction(1,2)
		multi = Multinomial()
		p = multi.init_2(trials, corrects, p_correct)

		self.question = f"""Find the probability of getting exactly {corrects} correct answers out of {trials} questions on true or false questions."""

		self.answer = f"""{p}"""

class rgs_19():
	def __init__(self):
		deck = Deck()
		rank = random.choice(deck.RANKS)
		suit = random.choice(deck.SUITS)

		pr = deck.probability(rank)
		ps = deck.probability(suit)

		p = pr + ps - (pr * ps)

		self.question = f"""If a single card is selected from a deck of 52 cards, find the probability that the card is either a {rank} or a {suit}."""

		self.answer = f"""{p}"""

class rgs_20():
	def __init__(self):
		tossed = random.randint(3,10)
		at_least_tails = random.randint(1, tossed - 1)

		multi = Multinomial()

		p = 0
		for i in range(at_least_tails, tossed + 1):
			p = p + multi.init_2(tossed, i, fractions.Fraction(1,2))

		self.question = f"""When {num2words(tossed)} coins are tossed, the probability of getting at least {num2words(at_least_tails)} tail(s)."""
		self.answer = f"""{p}"""

class rgs_21():
	def __init__(self):
		reds = random.randint(3,6)
		greens = random.randint(3, 6)
		blues = random.randint(3, 6)
		draws = min(reds, greens, blues)
		total = reds + greens + blues
		PR = fractions.Fraction(reds, total)
		PG = fractions.Fraction(greens, total)
		PB = fractions.Fraction(blues, total)
		multi = Multinomial()
		pr = multi.init_3(draws, 0, 0, PR, PG, PB)
		pg = multi.init_3(0, draws, 0, PR, PG, PB)
		pb = multi.init_3(0, 0, draws, PR, PG, PB)
		p = pr + pg + pb

		self.question = f"""A bag contains {reds} red beads, {greens} green beads, and {blues} blue beads. If a bead is selected and its color noted, and then it is replaced and another bead is selected, the probability that in {draws} draws, the beads will be of the same color is"""
		self.answer = f"""{p}"""


class rgs_22():
	def __init__(self):
		vd = Venn_Diagram()
		vd.init_random(2, True)
		sports = ['basketball', 'volleyball', 'baseball', 'billiards', 'tennis', 'badminton']
		sport_1 = sports.pop(random.randint(0, len(sports) - 1))
		sport_2 = sports.pop(random.randint(0, len(sports) - 1))
		probability = fractions.Fraction(vd.U - vd.others, vd.U)
		self.question = f"""At a high school with {vd.U} students, {vd.A} play {sport_1}, {vd.B} play {sport_2}, and {vd.AB} play both sports. If a student is selected at random, find the probability that the student plays {sport_1} or {sport_2}."""
		self.answer = f"""{probability}"""


class rgs_23():
	def __init__(self):
		ds = Dice_Sum()
		sum_of = random.choice(ds.DESC)

		results_1 = ds.sums[sum_of]
		results_2 = ds.doubles
		results = results_1.union(results_2)

		print(results_1)
		print(results_2)
		print(results)
		p = fractions.Fraction(len(results), len(ds.universe))

		self.question = f"""Two dice are rolled. What is the probability of getting doubles or a sum of {sum_of}?"""
		self.answer = f"""{p}"""

class rgs_24():
	def __init__(self):
		vd = Venn_Diagram()
		vd.init_random(2, True)

		self.question = f"""The probability that a family visits Safari Zoo is {round(vd.A/vd.U, 2)}, and the probability that a family rides on the Mt. Pleasant Tourist Railroad is {round(vd.B / vd.U, 2)}. The probability that a family does both is {round(vd.AB/vd.U,2)}. Find the probability that the family visits the zoo or the railroad."""
		self.answer = f"""{round((vd.U - vd.others) / vd.U , 2)}"""

class rgs_25():
	def __init__(self):
		m = Multinomial()
		trials = random.randint(3,9)
		p = m.init_2(trials, trials, fractions.Fraction(1,6))

		self.question = f"""{num2words(trials).capitalize()} dice are rolled. What is the probability of getting {num2words(trials)} {random.randint(1,6)}s?"""
		self.answer = f"""{p}"""

class rgs_27():
	def __init__(self):
		percentage = c.percentage(ran.main(25), 'percent')

		m = Multinomial()
		trials = random.randint(3,9)
		p = m.init_2(trials, trials, 1 - percentage.decimal)

		self.question = f"""If {round(percentage.percent,4)} % of US prison inmates are not US citizens, what is the probability of randomly selecting {num2words(trials)} inmates who will not be US citizens?"""
		self.answer = f"""{round(p, 4)} """

class rgs_29():
	def __init__(self):
		samples = random.randint(10,30)
		defective_all = random.randint(int(0.25 * samples), int(0.75 * samples))
		trials = random.randint(2, int(0.25 * samples))
		defectives = random.randint(1, trials - 1)

		h = Hypergeometric()
		p = h.init_2(defective_all, samples - defective_all, defectives, trials - defectives)

		self.question = f"""In a sample of {samples} telephones, {defective_all} are defective. If {trials} are selected at random and tested, what is the probability that {defectives} of them are defective?"""
		self.answer=  f"""{p}"""

class rgs_30():
	def __init__(self):
		blues = random.randint(5,20)
		reds = random.randint(5,20)

		trials = min(blues, reds)
		blue = random.randint(1, trials)

		h = Hypergeometric()
		p = h.init_2(blues, reds, blue, trials - blue)

		self.question = f"""A bag contains {blues} blue marbles and {reds} red marbles. If {trials} marbles are selected at random without replacement, what is the probability that {blue} of the marbles are blue?"""
		self.answer = f"""{p} """

class rgs_32():
	def __init__(self):
		n = Numbers()
		multiple_of = random.randint(2,10)
		desc = random.choice(n.descriptions)
		samples = n.sets[desc]
		print(samples)
		kind = n.multiple(multiple_of)
		p = fractions.Fraction(len(samples.intersection(kind)), len(samples))

		self.question = f"""The numbers {n.min} to {n.max} are placed in a hat and a number is selected. What is the probability that the number is a multiple of {multiple_of} given that it is known to be a(n) {desc} number?"""
		self.answer = f"""{p}"""

class rgs_33():
	def __init__(self):
		ds = Dice_Sum()
		sum_1 = random.randint(2,12)
		samples = ds.sums[sum_1]
		events = ds.doubles.intersection(samples)

		p = fractions.Fraction(len(events), len(samples))


		self.question = f"""Two dice are tossed; what is the probability that the numbers are the same on both dice if it is known that the sum of the spots is {sum_1}?"""
		self.answer = f"""{p}"""
























