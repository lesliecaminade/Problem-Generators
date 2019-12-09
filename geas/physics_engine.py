from generator import random_handler
from generator import constants_conversions as c
from mathsub import vectors_engine
import math
import sympy
import random


x, y = sympy.symbols('x y')

gravity = c.acceleration(9.81, 'mpers2')
k_coulomb = 9e9

#----------Schaums------------------------------------------------------------------

class example_2_1:
	def __init__(self,*args,**kwargs):
		velocity = c.velocity(random_handler.main(0.200), 'cmpers')
		
		self.question = f"""Change the speed {velocity.cmpers} cm/s to kilometers per year."""
		
		self.answer = f"""{velocity.kmperyear} kilometers per year."""
		
class example_2_2:
	def __init__(self,*args,**kwargs):
		distance = c.length(  random_handler.main(200),'m' )
		time = c.time(random_handler.main(25),'s')
		
		self.question = f"""A runner makes one lap around a {distance.m} m track in a time of {time.s}s. What were the runner's a) average speed and b) average velocity?"""
		
		aveSpeed = c.velocity( distance.m / time.s)
		aveVelocity = c.velocity(0)
		
		self.answer = f"""Average Speed = {aveSpeed.mpers} m/s
Average Velocity = {aveVelocity.mpers} m/s"""

class example_2_3:
	def __init__(self,*args,**kwargs):
		acceleration = c.acceleration(random_handler.main(8.00),'mpers2')
		time = c.time(random_handler.main(5),'s')
		
		
		self.question = f"""An object starts from rest with a constant acceleration of {acceleration.mpers2} m/s2 along a straight line. a) Find the speed at the end of {time.s} s, b) the average speed for the {time.s}-second interval, and c) the distance traveled in the {time.s} seconds."""
		
		velocity = c.velocity(acceleration.mpers2 * time.s)
		aveVelocity = c.velocity(velocity.mpers / 2)
		distance = c.length( 0.5 * acceleration.mpers2 * time.s**2 )
		
		self.answer = f"""Speed after {time.s}s = {velocity.mpers} m/s
Average Velocity = {aveVelocity.mpers} m/s
Distance Traveled = {distance.m} m"""

class example_2_4:
	def __init__(self,*args,**kwargs):
		velocity1 = c.velocity(random_handler.main(15),'kmperh')
		velocity2 = c.velocity(random_handler.main(60),'kmperh')
		time = c.time(random_handler.main(20),'s')
		
		self.question = f"""A truck's speed increases uniformly from {velocity1.kmperh} km/h to {velocity2.kmperh} km/h in {time.s} s. Determine a) the average speed, b) the average acceleration, c) the distance traveled, all in units of meters and seconds."""
		
		vAverage = c.velocity(0.5*(velocity1.mpers + velocity2.mpers))
		aAverage = c.acceleration((velocity2.mpers - velocity1.mpers)/2)
		distance = c.length(vAverage.mpers * time.s)
		
		self.answer = f"""Average Speed = {vAverage.mpers} m/s
Average Acceleration = {aAverage.mpers2} m/s2
Distance Traveled = {distance.m} m"""

class example_2_8:
	def __init__(self,*args,**kwargs):
		height = c.length(random_handler.main(50),'m')
		
		self.question = f"""A ball is dropped from rest at a height of {height.m} m above the ground. a) What is its speed just before it hits the ground? b) How long does it take to reach the ground?"""
		
		velocityFinal = c.velocity(math.sqrt(2 * gravity.mpers2 * height.m))
		time = c.time(velocityFinal.mpers / gravity.mpers2)
		
		self.answer = f"""Speed before hitting the ground = {velocityFinal.mpers} m/s
Time taken = {time.s} s"""

class example_2_9:
	def __init__(self,*args,**kwargs):
		distance = c.length(random_handler.main(9.0),'m')
		time1 = c.time(random_handler.main(3.0),'s')
		velocity = c.velocity(random_handler.main(24),'mpers')
		
		self.question = f"""A skier starts from rest and slides {distance.m}m down a slope in {time1.s}s. In what time after starting will the skier acquire a speed of {velocity.mpers}m/s? Assume that the acceleration is constant."""
		
		acceleration = c.acceleration((2*distance.m) / time1.s**2)
		time2 = c.time(velocity.mpers / acceleration.mpers2)
		
		self.answer = f"""Time to achieve a velocity of {velocity.mpers}m/s = {time2.s} seconds."""
		
class example_2_10:
	def __init__(self,*args,**kwargs):
		velocity = c.velocity(random_handler.main(20),'mpers')
		deceleration = c.acceleration (random_handler.main(-3.0),'mpers2')
		
		self.question = f"""A bus moving at a speed of {velocity.mpers}m/s begins to slow down at a constant rate of {deceleration.mpers2} m/s each second. Find how far it goes before stopping."""
		
		distance = c.length(-(velocity.mpers**2)/(2*deceleration.mpers2))
		
		self.answer = f"""Distance to stop = {distance.m} m"""
		
class example_2_11:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			velocityInit = c.velocity(random_handler.main(30),'mpers')
			velocityFinal = c.velocity(random_handler.main(10),'mpers')
			timeLarger = c.time(random_handler.main(5), 's')
			timeSmaller = c.time(3, 's')
			
			self.question = f"""A car moving at {velocityInit.mpers} m/s slows uniformly to a speed of {velocityFinal.mpers} m/s in a time of {timeLarger.s}s. Determine a) the acceleration of the car and b) the distance it moves in the third second."""
		
			acceleration = c.acceleration((velocityFinal.mpers - velocityInit.mpers)/timeLarger.s) 
			
			distanceThirdSecond = c.length(velocityInit.mpers * (3 - 2) + 0.5*acceleration.mpers2 * (3**2 - 2**2) )
			
			self.answer = f"""Acceleration = {acceleration.mpers2} m/s2
Distance traveled at the third second = {distanceThirdSecond.m} m"""

			if velocityInit.mpers > velocityFinal.mpers:
				regen = False

class example_2_12:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			velocityInit = c.velocity(random_handler.main(15), 'mpers')
			velocityFinal = c.velocity(random_handler.main(7), 'mpers')
			distance = c.length(random_handler.main(90),'m')
			
			self.question = f"""The speed of a train is reduced uniformly from {velocityInit.mpers} m/s to {velocityFinal.mpers} m/s while traveling a distance of {distance.m} m. a) Compute the acceleration. b) How much farther will the train travel before coming to rest, provided the acceleration remains constant?"""
			
			acceleration = c.acceleration( (velocityFinal.mpers**2 - velocityInit.mpers)**2 / ( 2 * distance.m ))
			restDistance = c.length((0 - velocityInit.mpers**2) / (2 * acceleration.mpers2))
			
			self.answer = f"""Acceleration = {acceleration.mpers2} m/s2
	Distance to stop = {restDistance.m} m"""

			
			if velocityInit.mpers > velocityFinal.mpers:
				regen = False
			
class example_2_13:
	def __init__(self,*args,**kwargs):
		height = c.length(random_handler.main(20),'m')
		
		self.question = f"""A stone is thrown straight upward and it rises to a height of {height.m} m. With what speed was it thrown?"""

		velocityInit = c.velocity(math.sqrt(2 * gravity.mpers2 * height.m))
		self.answer = f"""Initial Velocity  = {velocityInit.mpers} m/s"""
		
class example_2_14:
	def __init__(self,*args,**kwargs):
		velocityInit = c.velocity(random_handler.main(20),'mpers')
		heightCaught = c.length(random_handler.main(5),'m')
		
		self.question = f"""A stone is thrown straight upward with a speed of {velocityInit.mpers} m/s. It is caught on its way down at a point {heightCaught.m} m above where it was thrown. a) How fast was it going when it was caught? b) How long did the trip take?"""
		

		velocityFinal = c.velocity(-math.sqrt(abs(velocityInit.mpers**2 + 2*-gravity.mpers2*heightCaught.m)))
		
		time = c.time((velocityFinal.mpers - velocityInit.mpers)/(-gravity.mpers2))
		
		self.answer = f"""Velocity upon landing = {velocityFinal.mpers} m/s
Trip time = {time.s} s"""
   

			
class example_2_15:
	def __init__(self,*args,**kwargs):
		gravityMoon = c.acceleration(1.60,'mpers2')
		returnTime = c.time(random_handler.main(4),'s')
		
		self.question = f"""A ball that is thrown vertically upward on the Moon returns to its starting point in {returnTime.s} s. Acceleration due to gravity there is {gravityMoon.mpers2} m/s2. Find the ball's original speed."""
		
		velocityInitial = c.velocity((0.5*gravityMoon.mpers2*returnTime.s**2) /(returnTime.s) )
		
		self.answer = f"""Original Speed = {velocityInitial.mpers} m/s"""
			
		
class example_2_16:
	def __init__(self,*args,**kwargs):
		velocityInitial  = c.velocity(random_handler.main(35),'mpers')
		gravityMoon = c.acceleration(1.60,'mpers2')
		time = c.time(random_handler.main(30),'s')
		distanceSpecific = c.length(random_handler.main(100),'m')
		
		self.question = f"""A baseball is thrown straight upward on the Moon with an initial speed of {velocityInitial.mpers} m/s. Compute a) the maximum height reached by the ball, b) the time taken to reach that height, c) its velocity {time.s} s after it is thrown, and d) when the ball's height is {distanceSpecific.m} m."""
	
		maxHeight = c.length(velocityInitial.mpers**2 / (2*gravityMoon.mpers2))
		
		timeMaxHeight = c.time(velocityInitial.mpers / gravityMoon.mpers2)
		
		velocityFinal = c.velocity( velocityInitial.mpers - gravityMoon.mpers2 * time.s)
		
		timeset = sympy.solveset(sympy.Eq(distanceSpecific.m, velocityInitial.mpers*x + 0.5*(-gravityMoon.mpers2)*x**2),x,domain = sympy.Reals)

		timelist = list(timeset)
		
		
		
		self.answer = f"""Max height = {maxHeight.m} m
Time to max height = {timeMaxHeight.s} s
Velocity {time.s} s after throwing = {velocityFinal.mpers} m/s
Time when the ball's height is {distanceSpecific.m} m = {timelist} seconds"""

			
			
class example_2_17:
	def __init__(self,*args,**kwargs):
		height = c.length(random_handler.main(300),'m')
		velocityInitial = c.velocity(random_handler.main(13),'mpers')
		timeSpecific = c.time(random_handler.main(5.0),'s')
		
		self.question = f"""A ballast bag is dropped from a balloon that is {height.m} m above the ground and rising at {velocityInitial.mpers} m/s. For the bag, find a) the maximum height reached, b) its position and velocity {timeSpecific.s}s after it is released, and c) the time at which it hits the ground."""
		
		#upward positive:
		equation = sympy.Eq(0, velocityInitial.mpers**2 + 2*-gravity.mpers2*x)
		maxHeight = c.length(sympy.solveset(equation,x,domain = sympy.Reals).args[0])
		
		positionAtTime = c.length(height.m + velocityInitial.mpers*timeSpecific.s + 0.5*-gravity.mpers2*timeSpecific.s**2)
	
		velocityAtTime = c.velocity(velocityInitial.mpers + -gravity.mpers2 * timeSpecific.s)
		
		equation = sympy.Eq(0, height.m + velocityInitial.mpers*x + 0.5*-gravity.mpers2*x**2)
			
		timeToGround = c.time(max(sympy.solveset(equation,x,domain = sympy.Reals).args[0], sympy.solveset(equation,x,domain = sympy.Reals).args[1]))
	
		self.answer = f"""Max height from the ground = {maxHeight.m} m
Position after {timeSpecific.s}s = {positionAtTime.m} m
Velocity after {timeSpecific.s}s = {velocityAtTime.mpers} m/s
Time to hit the ground = {timeToGround.s} s"""
					
			
class example_2_18:
	def __init__(self,*args,**kwargs):
		velocityInitialX = c.velocity(random_handler.main(30),'mpers')
		velocityInitialY = c.velocity(0)
		heightInitial = c.length(random_handler.main(80),'m')
		
		self.question = f"""A projectile is fired horizontally with a speed of {velocityInitialX.mpers} m/s from the top of a cliff {heightInitial.m} m high. a) How long will it take to strike the level ground at the base of the cliff? b) How far from the foot of the cliff will it strike? c) With what velocity will it strike?"""
		
		
		equation = sympy.Eq(0, heightInitial.m + velocityInitialY.mpers*x + 0.5*-gravity.mpers2*x**2)
		times = sympy.solveset(equation,x,domain = sympy.Reals)
		timeToLand = c.time(max(times.args[0], times.args[1]))

		xDistance = c.length( velocityInitialX.mpers * timeToLand.s)
		
		velocityFinalX = c.velocity(velocityInitialX.mpers)
		velocityFinalY = c.velocity(-gravity.mpers2*timeToLand.s)
		
		velocityFinal = c.velocity(math.sqrt( velocityFinalX.mpers**2 + velocityFinalY.mpers**2))
		
		self.answer = f"""Time to land = {timeToLand.s} s
x - distance of landing point from launch point = {xDistance.m} m
Velocity on landing = {velocityFinal.mpers} m/s"""
		

			
class example_2_19:
	def __init__(self,*args,**kwargs):
		vix = c.velocity(random_handler.main(15),'mpers')
		hi = c.length(random_handler.main(100), 'm')
		viy = c.velocity(0)
		
		self.question = f"""A stunt flier is moving at {vix.mpers} m/s to the flat ground {hi.m} meters below. How large must the distance x from the plane to target be if a sack of flour released from the plane is to strike the target?"""
		
		equation = sympy.Eq(0, hi.m + viy.mpers * x + 0.5 * -gravity.mpers2 * x**2)
		
		t = c.time(max(sympy.solveset(equation,x,domain = sympy.Reals).args[0], sympy.solveset(equation,x,domain = sympy.Reals).args[1]))
		
		xDistance = c.length( vix.mpers * t.s )
		
		self.answer = f"""Distance = {xDistance.m} m"""

		
class example_2_20:
	def __init__(self,*args,**kwargs):
		vi = c.velocity(random_handler.main(100),'mpers')
		angle = c.angle(random_handler.main(30),'deg')
		
		self.question = f"""A baseball is thrown with an initial velocity of {vi.mpers} m/s at an angle of {angle.deg} degrees above the horizontal. How far from the throwing point will the baseball attain its original level?"""
		
		vix = c.velocity( vi.mpers * math.cos(angle.rad))
		viy = c.velocity( vi.mpers * math.sin(angle.rad))
		
		equation = sympy.Eq(0, viy.mpers + 0.5 * -gravity.mpers2 * x )
		
		
		t = c.time(sympy.solveset(equation,x, domain=sympy.Reals).args[0])
		
		xDistance = c.length(vix.mpers*t.s)
		
		self.answer = f"""Horizontal distance = {xDistance.m} m"""
		
class example_2_21:
	def __init__(self,*args,**kwargs): 
		distanceBuilding = c.length(random_handler.main(50),'m')
		vi = c.velocity(random_handler.main(20), 'mpers')
		angle = c.angle(random_handler.main(40), 'deg')
		
		self.question = f"""A ball is thrown from the top of one building toward a tall building {distanceBuilding.m} m away. The initial velocity of the ball is {vi.mpers} m/s, {angle.deg} degrees above horizontal. How far above or below its original level will the ball strike the opposite wall?"""
		
		vix = c.velocity( vi.mpers * math.cos(angle.rad))
		viy = c.velocity( vi.mpers * math.sin(angle.rad))
		
		vfx = c.velocity(vix.mpers)
		t = c.time( distanceBuilding.m / vix.mpers)
		
		yDistance = c.length(viy.mpers * t.s + 0.5*-gravity.mpers2*t.s**2 )
		
		self.answer = f"""For upward positive, the ball will hit {yDistance.m} m from the original level."""
		
class example_3_1:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(3),'kg')
		
		
		self.question = f"""Find the weight on earth of a body whose mass is {mass.kg} kg"""
		
		weight = c.force(mass.kg * gravity.mpers2)
		
		self.answer = f"""Weight = {weight.N} N"""
		
class example_3_2:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(20),'kg')
		force = c.force(random_handler.main(45), 'N')
		
		self.question = f"""A {mass.kg} kg object that can move freely is subjected to a resultant force of {force.N} N in the -x direction. Find the acceleration of the object."""
		
		acceleration = c.acceleration( - force.N / mass.kg) 
		
		self.answer = f"""Acceleration = {acceleration.mpers2} m/s2"""
		
class example_3_3:
	def __init__(self,*args,**kwargs):
		weight = c.force(random_handler.main(50),'N')
		
		self.question = f"""An object is hanging from a ceiling is supported by a cord and its weight is {weight.N} N. Find the tension in the cord"""
		
		self.answer = f"""Tension = {weight.N} N"""
		
class example_3_4:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(5),'kg')
		acceleration = c.acceleration(random_handler.main(0.30),'mpers2')
		
		self.question = f"""A {mass.kg} kg object is to be given an upward acceleration of {acceleration.mpers2} m/s2 by a rope pulling straight upward on it. What must be the tension in the rope?"""
		
		tension = c.force(mass.kg * gravity.mpers2 + mass.kg * acceleration.mpers2)
		
		self.answer = f"""Tension = {tension.N} N"""
		
class example_3_5:
	def __init__(self,*args,**kwargs):
		force = c.force(random_handler.main(140),'N')
		mass = c.mass(random_handler.main(60), 'kg')
		
		self.question = f"""A horizontal force of {force.N} N is needed to pull a {mass.kg} kg box across the horizontal floor at constant speed. What is the coefficient of friction between floor and box?"""
		
		friction = c.force(force.N)
		normal = c.force(mass.kg * gravity.mpers2)
		mu = friction.N / normal.N
		
		self.answer = f"""Coefficient of friction = {mu}"""
		
class example_3_6:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(50),'kg')
		forceX = c.force(random_handler.main(20),'N')
		forceY = c.force(random_handler.main(30),'N')
		
		self.question = f"""The only force acting on a {mass.kg} kg object has components Fx = {forceX.N} N and Fy = {forceY.N} N. Find the acceleration of the object."""
		
		accelX = c.acceleration(forceX.N / mass.kg )
		accelY = c.acceleration(forceY.N / mass.kg )
		
		accelTotal = c.acceleration( math.sqrt(accelX.mpers2**2 + accelY.mpers2**2) )
		
		angle = c.angle(math.atan(accelY.mpers2 / accelX.mpers2 ), 'rad')
		
		self.answer = f"""Acceleration = {accelTotal.mpers2} m/s2 at {angle.deg} degrees"""
		
class example_3_7:
	def __init__(self,*args,**kwargs):
		weight = c.force(random_handler.main(600),'N')
		acceleration = c.acceleration(random_handler.main(0.70),'mpers2')
		
		self.question = f"""A {weight.N} N object is to be given an acceleration of {acceleration.mpers2} m/s2. How large a unbalanced force must act upon it?"""
		
		mass = c.mass(weight.N / gravity.mpers2)
		force = c.force(mass.kg * acceleration.mpers2)
		
		self.answer = f"""Force = {force.N} N"""
		
class example_3_8:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(5), 'kg')
		velocity1 = c.velocity(random_handler.main(7.0),'mpers')
		velocity2 = c.velocity(7 - random_handler.main(4.0),'mpers')
		time = c.time(random_handler.main(3),'s')
		
		self.question = f"""A constant force acts on a {mass.kg} kg object and reduces its velocity from {velocity1.mpers} m/s to {velocity2.mpers} m/s in a time of {time.s} s. Find the force."""
		
		acceleration = c.acceleration((velocity2.mpers - velocity1.mpers) / time.s) 
		force = c.force(mass.kg * acceleration.mpers2)
		
		self.answer = f"""Force = {force.N} N"""
		
class example_3_9:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(400),'g')
		velocity1 = c.velocity(random_handler.main(80),'cmpers')
		friction = c.force(random_handler.main(0.70),'N')
		
		self.question = f"""A {mass.g} g block with an initial speed of {velocity1.cmpers} cm/s slides along a horizontal tabletop against a friction force of {friction.N} N. a) How far will it slide before stopping? b) What is the coefficient of friction between the block and the tabletop?"""
		
		acceleration = c.acceleration( - friction.N / mass.kg )
		xDistance = c.length( ( 0 - velocity1.mpers**2)  / (2 * acceleration.mpers2)  )
		normal = c.force(mass.kg * gravity.mpers2)
		mu = friction.N / normal.N
		
		self.answer = f"""Distance before stopping = {xDistance.m} m
Coefficient of friction = {mu}"""

class example_3_10:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(600),'kg')
		velocity1 = c.velocity(random_handler.main(30),'mpers')
		distanceToStop = c.length(random_handler.main(70),'m')
		
		self.question = f"""A {mass.kg} kg car is moving on a level road at {velocity1.mpers} m/s. a) How large a retarding force (assumed constant) is required to stop it in a distance of {distanceToStop.m} m? b) What is the minimum coefficient of friction between the tires and the roadway if this is to be possible? Assume the wheels are not locked, in which case we are dealing with static friction - there is no sliding."""
		
		acceleration = c.acceleration((0 - velocity1.mpers**2)/( 2 * distanceToStop.m) )
		force = c.force(mass.kg * acceleration.mpers2)
		friction = c.force( force.N)
		normal = c.force(mass.kg * gravity.mpers2)
		mu = friction.N / normal.N
		
		self.answer = f"""Force required = {friction.N} N
Coefficient of friction = {mu}"""

class example_3_11:
	def __init__(self,*args,**kwargs):
		massEngine = c.mass(random_handler.main(8000),'kg')
		massTrain1 = c.mass(random_handler.main(40000),'kg')
		acceleration1 = c.acceleration(random_handler.main(1.20),'mpers2')
		massTrain2 = c.mass(random_handler.main(16000),'kg')
		
		self.question = f"""An {massEngine.kg} kg engine pulls a {massTrain1.kg} kg train along a level track and gives it an acceleration a1 = {acceleration1.mpers2} m/s2. What acceleration a2 would the engine give to a {massTrain2.kg} kg train?"""
		
		massBefore = c.mass(massEngine.kg + massTrain1.kg)
		massAfter = c.mass(massEngine.kg + massTrain2.kg)
		acceleration2 = c.acceleration( (massBefore.kg / massAfter.kg) * acceleration1.mpers2 )
		
		self.answer = f"""Acceleration = {acceleration2.mpers2} m/s2"""
		
class example_3_13:
	def __init__(self,*args,**kwargs):
		tensionLimit = c.force(random_handler.main(1500),'N')
		mass = c.mass(random_handler.main(700),'kg')
		
		self.question = f"""A tow rope will break if the tension in it exceeds {tensionLimit.N} N. It is used to tow a {mass.kg} kg car along level ground. What is the largest acceleration the rope can give to the car?"""
		
		acceleration = c.acceleration(tensionLimit.N / mass.kg)
		
		self.answer = f"""Max Acceleration = {acceleration.mpers2} m/s2"""
		
class example_3_14:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(45), 'kg')
			tensionLimit = c.force(min(random_handler.main(300),mass.kg*gravity.mpers2),'N')
			
			self.question = f"""Compute the least acceleration with which a {mass.kg} kg woman can slide down a rope if the rope can withstand a tension of only {tensionLimit.N}"""
			
			acceleration = c.acceleration( (mass.kg*gravity.mpers2 - tensionLimit.N) / mass.kg  )
			
			if acceleration.mpers2 >= 0:
				regen = False
		
		self.answer = f"""Acceleration = {acceleration.mpers2} m/s2"""
		
class example_3_15:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(70),'kg')
		force = c.force(random_handler.main(400),'N')
		mu = random_handler.u(0.5)
		
		self.question = f"""A {mass.kg} box is slid along the floor by a {force.N} N force. The coefficient of friction between the box and the floor is {mu} when the box is sliding. Find the acceleration of the box."""
		
		normal = c.force(mass.kg * gravity.mpers2)
		friction = c.force( mu * normal.N)
		
		acceleration = c.acceleration( (force.N - friction.N) / mass.kg)
		comment = ''
		if friction.N > force.N:
			#the block wont move
			acceleration = c.acceleration(0)
			comment = 'the block wont move'
		self.answer = f"""Acceleration = {acceleration.mpers2} m/s2, {comment}"""
		
class example_3_16:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(70),'kg')
			force = c.force(random_handler.main(400),'N')
			angle_force = c.angle(random_handler.main(30),'deg')
			mu = random_handler.main(0.5)
			
			self.question = f"""A {mass.kg} kg box is pulled by a {force.N} N force at an angle of {angle_force.deg} degrees to the horizontal (positive towards the +y direction). The coefficient of kinetic friction is {mu}. Find the acceleration of the box."""
			
			forceX = c.force( force.N * math.cos(angle_force.rad))
			forceY = c.force( force.N * math.sin(angle_force.rad))
			weight = c.force( mass.kg * gravity.mpers2)
			normal = c.force( weight.N - forceY.N)
			friction = c.force( mu * normal.N)
			acceleration = c.acceleration( (forceX.N - friction.N) / (mass.kg))
		
			if weight.N > forceY.N and forceX.N > friction.N:
				regen = False
				
			self.answer = f"""Acceleration = {acceleration.mpers2} m/s2"""
			
class example_3_17:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			velocity1 = c.velocity(random_handler.main(20),'mpers')
			velocity2 = c.velocity(0)
			mu = random_handler.u(0.90)
			
			self.question = f"""A car moving at {velocity1.mpers} m/s along a horizontal road has its brakes suddenly applied and eventually comes to rest. What is the shortest distance in which it can be stopped if the friction coefficient between tires and road is {mu}? Assume that all four wheels brake identically. The brakes also dont lock the wheels of the car."""
			
			try:
				acceleration = c.acceleration( - mu * gravity.mpers2)
				xDistance = c.length( (velocity2.mpers**2 - velocity1.mpers**2) / ( acceleration.mpers2 ))
				regen = False
				self.answer = f"""Distance traveled = {xDistance.m} m"""
			except:
				regen = True
				
			
			
			
class example_3_18:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			force = c.force(random_handler.main(400),'N')
			theta_force = c.angle(random_handler.main(50),'deg')
			mass = c.mass(random_handler.main(25),'kg')
			velocity1 = c.velocity(0)
			velocity2 = c.velocity(random_handler.main(2), 'mpers')
			time = c.time(random_handler.main(4), 's')
			
			self.question = f"""A force of {force.N} N pushes down on a {mass.kg} kg box at an angle of {theta_force.deg} degrees with the horizontal. Starting from rest, the box achieves a velocity of {velocity2.mpers} m/s in a time {time.s} s. Find the coefficient of kinetic friction between bix and floor."""
			
			forceX = c.force(force.N * math.cos(theta_force.rad))
			forceY = c.force(force.N * math.sin(theta_force.rad))
			weight = c.force( mass.kg * gravity.mpers2 )
			acceleration = c.acceleration((velocity2.mpers - velocity1.mpers)/time.s)
			friction = c.force( forceX.N - mass.kg*acceleration.mpers2 )
			normal = c.force( forceY.N + weight.N )
			mu = friction.N / normal.N
			
			if forceX.N > mass.kg*gravity.mpers2:
				regen = False
				
			self.answer = f"""Coefficient of friction = {mu}"""

class example_3_19:
	def __init__(self,*args,**kwargs):
		weight = c.force(random_handler.main(200),'N')
		angle = c.angle(random_handler.main(30),'deg')
		
		self.question = f"""A {weight.N} N wagon is to pulled up a {angle.deg}-degree incline at constant speed. How large a force parallel to the incline is needed if friction effects are negligible."""
		
		weightIncline = c.force( weight.N * math.sin(angle.radians) )
		
		self.answer = f"""Force needed = {weightIncline.N} N"""
		
class example_3_20:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(20),'kg')
			mu = random_handler.main(0.30)
			angle = c.angle(random_handler.main(30),'deg')
			
			self.question = f"""A {mass.kg} kg box sits on an incline with an angle of {angle.deg} degrees. The coefficient of friction between box and incline is {mu}. Find the acceleration of the box down the incline."""
			
			weight = c.force(mass.kg*gravity.mpers2)
			weightX = c.force(weight.N * math.sin(angle.rad))
			weightY = c.force(weight.N * math.cos(angle.rad))
			normal = c.force(weightY.N)
			friction = c.force(mu*normal.N)
			
			if weightX.N > friction.N:
				regen = False
				
			acceleration = c.acceleration( ( weightX.N - friction.N) / mass.kg)
			
			self.answer = f"""Accleration = {acceleration.mpers2} m/s2"""
			
class example_3_21:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			force = c.force(random_handler.main(500), 'N')
			mass = c.mass(random_handler.main(25),'kg')
			acceleration = c.acceleration(random_handler.main(0.75),'mpers2')
			angle = c.angle(random_handler.main(40),'deg')
			
			self.question = f"""When a force {force.N} N pushes horizontally on a {mass.kg} kg box on a {angle.deg} degree incline, the acceleration of the box up the incline is {acceleration.mpers2} m/s2. Find the coefficient of kinetic friction between box and incline."""
			
			forceX = c.force(force.N * math.cos(angle.rad))
			forceY = c.force(force.N * math.sin(angle.rad))
			weight = c.force(mass.kg*gravity.mpers2)
			weightX = c.force(weight.N * math.sin(angle.rad))
			weightY = c.force(weight.N * math.cos(angle.rad))
			
			friction = c.force( forceX.N - weightX.N - mass.kg*acceleration.mpers2)
			normal = c.force(forceY.N + weightY.N)
			mu = friction.N / normal.N
			
			if friction.N > 0:
				regen = False
				
			self.answer = f"""Coefficient of kinetic friction = {mu}"""
			
class example_3_22:
	def __init__(self,*args,**kwargs):
		mass1 = c.mass(random_handler.main(300),'g')
		mass2 = c.mass(random_handler.main(500),'g')
		mu = random_handler.main(0.40)
		acceleration = c.acceleration(random_handler.main(200), 'cmpers2')
		
		self.question=f"""Two blocks beside each other on a floor of masses m1 and m2 are pushed by a force F on m1. The coefficient of friction between each block and the table is {mu}. a) What must be the value of F if the blocks are to have an accelerated of {acceleration.cmpers2} cm/s2? How large a force does m1 then exert on m2?"""
		
		force = c.force( mu*gravity.mpers2*(mass1.kg+mass2.kg) + acceleration.mpers2*(mass1.kg+mass2.kg))
		friction2 = c.force(mu*mass2.kg*gravity.mpers2)
		forceMass2 = c.force(friction2.N + mass2.kg*acceleration.mpers2)
		
		self.answer = f"""Force on mass 2 = {forceMass2.N} N"""
		
class example_3_23:
	def __init__(self,*args,**kwargs):
		mass1 = c.mass(random_handler.main(7),'kg')
		mass2 = c.mass(random_handler.main(9),'kg')
		
		if mass2.kg < mass1.kg:
			mass2.kg, mass1.kg = mass1.kg, mass2.kg
			
		self.question = f"""A cord passing over an easily turned pulley (one that is both massless and frictionless) has a {mass1.kg} kg mass hanging from one end and a {mass2.kg} kg mass hanging from the other. Find the acceleration of the masses and the tension of the cord."""
		
		acceleration = c.acceleration ( ((mass2.kg - mass1.kg)*gravity.mpers2) / (mass1.kg + mass2.kg) )
		
		self.answer = f"""Acceleration = {acceleration.mpers2} m/s2"""
		
class example_3_24:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			mu = random_handler.main(0.2)
			massA = c.mass(random_handler.main(25),'kg')
			massB = c.mass(random_handler.main(15),'kg')
			time = c.time(random_handler.main(3.0),'s')
			
			self.question = f"""Mass A with a mass of {massA.kg} kg is a block that is on a table in which has a coefficient of friction of {mu}. Mass A is attached to horizontal rope across a pulley and the other end drops down attached to a freely hanging mass B with a mass of {massB.kg} kg. How far will mass B drop in the first {time.s} s after the system is released?"""
			
			acceleration = c.acceleration ( (massB.kg * gravity.mpers2 - mu * massA.kg * gravity.mpers2) /  (massA.kg + massB.kg) )
			
			distance = c.length(  (1/2) * acceleration.mpers2 * time.s**2 )
			
			self.answer = f"""Distance traveled = {distance.m} m"""
			
			if massA.kg > massB.kg:
				regen = False
				
		
class example_3_25:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			mu = random_handler.main(0.2)
			massA = c.mass(random_handler.main(25),'kg')
			massB = c.mass(random_handler.main(15),'kg')
			acceleration = c.acceleration(random_handler.main(0.75),'mpers2')
			
			self.question = f"""Mass A with a mass of {massA.kg} kg is a block that is on a table in which has a coefficient of friction of {mu}. Mass A is attached to horizontal rope across a pulley and the other end drops down attached to a freely hanging mass B with a mass of {massB.kg} kg. How large horizontal force acting on mass A is required to raise mass B up with an acceleration of {acceleration.mpers2} m/s2?"""
			
			force = c.force( acceleration.mpers2 * (massA.kg + massB.kg)  + mu*massA.kg*gravity.mpers2 + massB.kg*gravity.mpers2 )
			
			self.answer = f"""Force = {force.N} N"""
			
			if massA.kg > massB.kg:
				regen = False
				
class example_3_26:
	def __init__(self,*args,**kwargs):
		mu = random_handler.main(0.60)
		
		self.question =f"""The coefficient of static friction between a box and the flat bed of a truck is {mu}. What is the maximum acceleration the truck can have along level ground if the box is not to slide?"""
		
		acceleration = c.acceleration (mu * gravity.mpers2)
		
		self.answer = f"""Acceleration = {acceleration.mpers2} m/s2"""

#chapter 4
#chapter 5
#---------
class schaums_6_1:
	def __init__(self,*args,**kwargs):
		force = c.force( random_handler.main(75), 'N')
		theta = c.angle( random_handler.main(28), 'deg')
		distance = c.length ( random_handler.main(8), 'm')
		
		self.question = f"""A horizontal block is pulled along the ground by a {force.N} N force direction {theta.deg} degrees. How much work does force do in pulling the object {distance.m} m?"""
		
		work = c.energy( force.N * math.cos(theta.rad) * distance.m )
		
		self.answer = f"""{round(work.J,2)} J"""
		
class schaums_6_2:
	def __init__(self,*args,**kwargs):
		theta = c.angle( random_handler.main(30), 'deg')
		f1 = c.force (random_handler.main (40), 'N')
		f2 = c.force (random_handler.main (20), 'N')
		f3 = c.force (random_handler.main (30), 'N')
		distance  = c.length( random_handler.main(80), 'cm')
		
		self.question = f"""A block moves up a {theta.deg} degree incline under the action of certain force. F1 is horizontal and of magnitude {f1.N} N. F2 is normal to the plane and of magnitude {f2.N} N. F3 is parallel to the plane and of magnitude {f3.N} N. Determine the work done by each force as the block (and the point of application of each force) moves up {round(distance.cm,2)} cm up the incline."""
		
		work1 = c.energy (round(f1.N * math.cos(theta.rad) * distance.m , 2))
		work2 = c.energy (round(0, 2))
		work3 = c.energy (round(f3.N * distance.m, 2))
		
		self.answer = f"""{work1.J} J, {work2.J} J, {work3.J} J"""

class schaums_6_3:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(300),'g')
		distance = c.length(random_handler.main(80),'cm')
		mu = random_handler.main(0.20)
		
		self.question = f"""A {mass.g} g object slides {distance.cm} cm along a horizontal tabletop. How much work is done in overcoming friction between the object and the table if the coefficient of kinetic friction is {mu}?"""
		
		friction = c.force(mu*mass.kg*gravity.mpers2)
		work = c.energy( - friction.N * distance.m)
		
		self.answer = f"""{round(work.J,2 )} J"""
		
class schaums_6_4:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(3), 'kg')
		distance = c.length(random_handler.main(40), 'cm')
		
		self.question  = f"""How much work is done against gravity in lifting a {mass.kg} kg object through a vertical distance of {distance.cm} cm?"""
		
		work = c.energy( mass.kg * gravity.mpers2 * distance.m )
		
		self.answer = f"""{round(work.J, 2)} J"""
		
class schaums_6_6:
	def __init__(self,*args,**kwargs):
		ladderLength = c.length(random_handler.main(3), 'm')
		ladderWeight = c.force(random_handler.main(200),'N')
		ladderCenterOfGravity = c.length(random_handler.main(120),'cm')
		topEndWeight = c.force(random_handler.main(50),'N')
		self.question = f"""A ladder {ladderLength.m} m long and weighing {ladderWeight.N} N has its center of gravity {ladderCenterOfGravity.cm} cm from the bottom. At its top end is a {topEndWeight.N} N weight. Compute the work required to raise the ladder from a horizontal position on the ground to a vertical position."""
		work = c.energy( ladderWeight.N * ladderCenterOfGravity.m + topEndWeight.N * ladderLength.m )
		
		self.answer = f"""{round(work.J,2)} J"""

class schaums_6_7:
	def __init__(self,*args,**kwargs):
		volume = c.volume( random_handler.main(600),'L')
		height = c.length( random_handler.main(20), 'm')
		density = c.density ( 0.82, 'gpercm3')
		
		self.question = f"""Compute the work done againts gravity by a pump that discharges {volume.L} liters of fuel oil into a tank {height.m} m above the pump's intake. One cubic centimeter of fuel oil has a mass of {density.gpercm3} g."""
		
		mass = c.mass ( volume.m3 * density.kgperm3 )
		work = c.energy ( mass.kg * gravity.mpers2 * height.m)
		
		self.answer = f"""{round(work.J,2)} J"""
		
class schaums_6_8:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(2), 'kg')
		height = c.length(random_handler.main(400),'cm')
		
		self.question = f"""A {mass.kg} kg mass falls {height.cm} cm. a) How much work was done on it by the gravitational force? b) How much PE_g did it lose?"""
		
		work = c.energy( mass.kg * gravity.mpers2* height.m )
		
		self.answer = f"""{round(work.J,2)} J, - {round(work.J,2)} J"""


class schaums_6_9:
	def __init__(self,*args,**kwargs):
		force = c.force(random_handler.main(1.50),'N')
		mass = c.mass(random_handler.main(0.20), 'kg')
		distance = c.length(random_handler.main(30),'cm')
		
		self.question = f"""A force of {force.N} N acts on a {mass.kg} kg cart so as to accelerate it along an air track. The track and force are horizontal and in line. How fast is the cart going after acceleration from rest through {distance.cm} cm, if friction is negligible?"""
		
		velocity = c.velocity ( math.sqrt((2 * force.N * distance.m) / mass.kg))
		
		self.answer = f"""{round(velocity.mpers,2)} m/s"""

class schaums_6_10:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(0.50), 'kg')
		velocity1 = c.velocity(random_handler.main(20),'cmpers')
		velocity2 = c.velocity(0)
		distance = c.length(random_handler.main(70),'cm')
		
		self.question = f"""A {mass.kg} kg block slides across a tabletop with an initial velocity of {velocity1.cmpers} cm/s and comes to rest in a distance of {distance.cm} cm. Find the average friction force that retarded the motion"""
		
		friction = c.force ( (0.5 * mass.kg * velocity1.mpers**2) / (distance.m))
		
		self.answer = f"""{round(friction.N,2)} N"""
		
class schaums_6_11:
	def __init__(self,*args,**kwargs):
		velocity = c.velocity ( random_handler.main (15), 'mpers')
		distance = c.length(random_handler.main(2),'m')
		mass = c.mass (random_handler.main(90), 'kg')
		
		self.question = f"""A car going {velocity.mpers} m/s is brought to rest in a distance of {distance.m} m as it strikes a pile of dirt. How large an average force is exerted by seatbelts on a {mass.kg} kg passenger as the car is stopped?"""
		
		force = c.force( (0.5*mass.kg*velocity.mpers**2) / (distance.m) )
		
		self.answer = f"""{round(force.kN,2)} kN"""
		
class schaums_6_12:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			velocity = c.velocity(random_handler.main(20),'mpers')
			velocitySpecific = c.velocity(random_handler.main(12), 'mpers')
			
			self.question = f"""A projectile is shot upward from the earth with speed of {velocity.mpers} m/s. How high is it when its speed is {velocitySpecific.mpers} m/s?"""
			
			height = c.length( - (velocitySpecific.mpers**2 - velocity.mpers**2) / (2*gravity.mpers2))
			
			self.answer = f"""{round(height.m,2)} m"""
			
			if velocity.mpers > velocitySpecific.mpers:
				regen = False
			
class schaums_6_13:
	def __init__(self,*args,**kwargs):
		regen = True
		error = False
		while regen:
			print(type(self))
			mass1 = c.mass(random_handler.main(800),'g')
			mass2 = c.mass(random_handler.main(700),'g')
			distance = c.length(random_handler.main(120),'cm')
			
			self.question = f"""In an Atwood machine, the two masses are {mass1.g}g and {mass2.g}g. The system is released from rest. How fast is the {mass1.g}g mass moving after is has fallen {distance.cm} cm?"""
			
			try:
				velocity = c.velocity ( math.sqrt ((2*gravity.mpers2*distance.m*(mass1.kg - mass2.kg))/(mass1.kg + mass2.kg)))
			except:
				error = True
				
				
			try:
				self.answer = f"""{round(velocity.mpers,2)} m/s"""
			except:
				self.answer = 'error'
				error = True
				
			if mass1.g > mass2.g:
				regen = False
				

class schaums_6_16:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(1200),'kg')
		angle = c.angle(random_handler.main(30),'deg')
		speed = c.velocity(random_handler.main(12),'mpers')
		distance = c.length(random_handler.main(100),'m')
		height = c.length( distance.m * math.sin(angle.rad))
   
		self.question = f"""A {mass.kg} kg car is coasting down a {angle.deg} degree hill. At a time when the car's speed is {speed.mpers} m/s, the driver applies the brakes. What constant force F (parallel to the road) must result if the car is to stop after traveling {distance.m} m"""
		
		friction = c.force ( (-(0.5*mass.kg*speed.mpers**2) - (mass.kg*gravity.mpers2*height.m)) / ( distance.m ) )
		
		self.answer = f"""{round(friction.kN,2)} kN"""
		
class schaums_6_17:
	def __init__(self,*args,**kwargs):
		regen = True
		while regen:
			print(type(self))
			length = c.length( random_handler.main(180), 'cm')
			velocity = c.velocity ( random_handler.main(400), 'cmpers')
			
			self.question = f"""A ball at the end of a {length.cm} cm long string swings as a pendulum. The ball's speed is {velocity.cmpers} cm/s as it passes through its lowest position. a) To what height h above this position will it rise before stopping? b) What angle does the pendulum then make to the vertical?"""
			
			height = c.length( (0.5 * velocity.mpers**2) / gravity.mpers2 )
			angle = c.angle ( math.acos( (length.m - height.m) / (length.m) ), 'rad' )
			
			self.answer = f"""{round(height.m,2)} m, {round(angle.deg,2)} degrees"""
	
			if length.m > height.m:
				regen = False
				

class schaums_6_18:
	def __init__(self,*args,**kwargs):
		mass = c.mass ( random_handler.main(500), 'g')
		angle = c.angle( random_handler.main(25), 'deg')
		velocity = c.velocity ( random_handler.main(200), 'cmpers')
		mu = random_handler.main(0.150)
		
		self.question = f"""A {mass.g}g block is shot up a {angle.deg} degree incline with an initial speed of {velocity.cmpers} cm/s. How far up the incline will it go if the coefficient of friction between it and the incline is {mu}?"""
		
		equation = sympy.Eq(
		0.5 * velocity.mpers**2,
		gravity.mpers2 * x * math.sin(angle.rad) + x * mu * gravity.mpers2 * math.cos(angle.rad)
		)
		
		x_set = sympy.solveset(equation, x)
		x_list = list(x_set)
		
		distance = c.length(x_list[0])
		
		self.answer = f"""{round(distance.m,2)} m"""
		
class schaums_6_19:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(60000), 'kg' )
		percentGrade = c.percentage(random.randint(1,3),'percent')
		force = c.force( random_handler.main(3.0), 'kN' )
		friction = c.force ( random_handler.main(4.0), 'kN' )
		velocity1 = c.velocity( random_handler.main(12), 'mpers' )
		velocity2 = c.velocity( random_handler.main(9), 'mpers' )
		
		self.question = f"""A {mass.kg}kg train is being pulled up a {percentGrade.percent} percent grade (it rises {percentGrade.percent} m for each horizontal 100 m) by a drawbar pull of {force.kN} kN. The friction force opposing the motion of the train is {friction.kN} kN. The train's initial speed is {velocity1.mpers} m/s. Through what horizontal distance s will the train move before its speed is reduced to {velocity2.mpers} m/s?"""
		
		distance = c.length (  (0.5 * mass.kg * (velocity2.mpers**2 - velocity1.mpers**2) / (force.N - friction.N - mass.kg* gravity.mpers2 * percentGrade.whole) ))
		
		self.answer = f"""{round(distance.km,2)} km"""
		
class schaums_6_20:
	def __init__(self,*args,**kwargs):
		mass = c.mass( random_handler.main(1200), 'kg')
		velocity = c.velocity ( random_handler.main(25), 'mpers')
		time = c.time( random_handler.main(8.0), 's')
		
		self.question = f"""An advertisement claims that a certain {mass.kg}kg car can accelerate from rest to a speed of {velocity.mpers} m/s in a time of {time.s}s. What average power must the motor produce to cause this acceleration? Ignore friction losses."""
		
		power = c.power( (0.5*mass.kg*velocity.mpers**2) / (time.s))
		
		self.answer = f"""{round(power.hp,2)} hp"""
		
class schaums_6_21:
	def __init__(self,*args,**kwargs):
		power = c.power ( random_handler.main(0.25), 'hp')
		velocity = c.velocity ( random_handler.main(5.0), 'cmpers')
		
		self.question = f"""A {power.hp} hp motor is used to lift a load at the rate of {velocity.cmpers} cm/s. How great a load can it lift at this constant speed?"""
		
		mass = c.mass ( (power.W) / (gravity.mpers2 * velocity.mpers))
		
		self.answer = f"""{round(mass.kg,2)} kg"""
		
class schaums_6_23:
	def __init__(self,*args,**kwargs):
		distance = c.length( random_handler.main(12), 'm')
		dischargeRate = c.mass(random_handler.main(2), 'kg')
		speed = c.velocity(random_handler.main(3), 'mpers')
		
		self.question = f"""In unloading grain from the hold of a ship, an elevator lifts the grain through a distance of {distance.m}m. Grain is discharged at the top of the elevator at a rate of {dischargeRate.kg} kg each second, and the discharge speed of each grain particle is {speed.mpers} m/s. Find the minimum horsepower motor that can elevate grain in this way."""
		
		power = c.power(dischargeRate.kg * (0.5*speed.mpers**2 + gravity.mpers2*distance.m))
		
		self.answer = f"""{round(power.hp,2)} hp"""
		

class schaums_8_1:
	def __init__(self,*args,**kwargs): 
		
		mass_bullet = c.mass(random_handler.main(8, 'int'), 'g')
		mass_wood = c.mass(random_handler.main(9, 'int'), 'kg')
		velocityprime = c.velocity(random_handler.main(40, 'int'), 'cmpers')
		
		
		self.question = f"""A  {mass_bullet.g} g bullet is fired horizontally into a {mass_wood.kg}kg of wood, which is at rest, and sticks in it. The cube is free to move and has a speed of {velocityprime.cmpers} cm/s after impact. Find the initial velocity of the bullet.""" 

		velocitybullet = c.velocity( ((mass_bullet.kg + mass_wood.kg)*velocityprime.mpers)/ mass_bullet.kg)
		
		self.answer = f"""{round(velocitybullet.kmpers, 2)} km/s"""

#chapter 7     
		
class schaums_8_2:
	def __init__(self,*args,**kwargs): 
		
		mass1 = c.mass(random_handler.main(16,' int'), 'g')
		mass2 = c.mass(random_handler.main(4, 'int'), 'g')
		mass1velocity = c.velocity(random_handler.main(30, 'int'), 'cmpers')
		mass2velocity = c.velocity(random_handler.main(50, 'int'), 'cmpers')


		self.question = f"""A {mass1.g} g mass is moving in the + x direction at {mass1velocity.cmpers} cm/s while a {mass2.g} g mass is moving in the - x direction at {mass2velocity.cmpers} cm/s. They collide and stick 
		together. Find their velocity after the collision."""

		mass2velocity = c.velocity( - mass2velocity.mpers)
		
		velocityprime = c.velocity(
		( mass1.kg * mass1velocity.mpers + mass2.kg * mass2velocity.mpers) / (mass1.kg + mass2.kg)
		)
		
		self.answer = f"""{round(velocityprime.mpers,2)} m/s"""
		
class schaums_8_3:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(2))
		speed = c.velocity(random_handler.main(6))
		time = c.time(random_handler.main(7e-4, 'noround'))
		
		
		self.question = f"""A {mass.kg}kg brick is moving at a speed of {speed.mpers} m/s. How large a force F is needed to stop the brick in a time of {time.s} s ?"""
		
		force = c.force( - (mass.kg * speed.mpers) / (time.s))
		
		self.answer = f"""{round(force.N,2)} N"""
		
class schaums_8_4:
	def __init__(self,*args,**kwargs): 
		regen = True
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(15, 'int'), 'g')
			speedbullet = c.velocity(random_handler.main(300, 'int'), 'mpers')
			speedbullet2 = c.velocity(speedbullet.mpers - random_handler.main(210, 'int'), 'mpers')
			thick = c.length(random_handler.main(2), 'cm')
			
			
			self.question = f"""A {mass.g}g bullet moving at {speedbullet.mpers} m/s passes through a {thick.cm} cm thick sheet of foam plastic and emerges with a speed of {speedbullet2.mpers} m/s. What average force impeded its motion through the plastic?""" 
			
			velocityAverage = c.velocity( 0.5 * (speedbullet.mpers + speedbullet2.mpers))
			time = c.time(  thick.m / velocityAverage.mpers  )
			
			if time.s > 0:
				regen = False
			
		force = c.force(
		(mass.kg*(speedbullet2.mpers - speedbullet.mpers)) / (time.s)
		)
		
		self.answer = f"""{round(force.N,2)} N"""
		
		
class schaums_8_5:
	def __init__(self,*args,**kwargs): 

		massnucleus = c.mass(random_handler.main(3.8e-25 , 'noround')) 
		massparticle = c.mass(random_handler.main(6.6e-27, 'noround'))
		speedparticle = c.velocity(random_handler.main(1.5e7, 'noround'))
		
		
		self.question = f"""The nucleus of an atom has a mass of {massnucleus.kg} kg and is at rest. THe nucleus is radioactive and suddenly ejects a particle of mass {massparticle.kg} kg and speed {speedparticle.mpers} m/s. Find the recoil speed of the nucleus that is left behind."""
		
		# equation = sympy.Eq(
		# 0,
		# (massnucleus.kg - massparticle.kg) * x + massparticle.kg * speedparticle.mpers
		# )
		# print(type(self), 'equation:', equation)
		# x_set = sympy.solveset(equation, x)
		# x_list = list(x_set)
		
		# try:
		# 	speednucleus_after = c.velocity(x_list[0])
		# except:
		# 	print(type(self), 'x_set: ', x_set)
		
		speednucleus_after = c.velocity(- massparticle.kg * speedparticle.mpers / (massnucleus.kg - massparticle.kg))

		
		self.answer = f"""{round(speednucleus_after.mpers,2)} m/s"""
		
class schaums_8_6:
	def __init__(self,*args,**kwargs): 
		
		ballmass = c.mass(random_handler.main(0.25), 'kg')
		ballspeed = c.velocity(random_handler.main(13), 'mpers')
		ballspeed2 = c.velocity(random_handler.main(19), 'mpers')
		time = c.time(random_handler.main(0.010), 's')
		
		
		self.question = f"""A {ballmass.kg} kg ball moving in the + x direction at {ballspeed.mpers} m/s is hit by a bat. Its final velocity is {ballspeed2.mpers} m/s in the - x direction. The bat acts on the ball for {time.s} s. Find the average force F exerted on the ball by the bat."""
		
		ballspeed2 = c.velocity(-ballspeed2.mpers)
		
		force = c.force(    
		(ballmass.kg*(ballspeed2.mpers - ballspeed.mpers )) / (time.s)
		)
		
		self.answer = f"""{round(force.N,2)} N"""
		
		
class schaums_8_8:
	def __init__(self,*args,**kwargs): 
		
		bulletmass = c.mass(random_handler.main(15), 'g')
		blockmass = c.mass(random_handler.main(3), 'kg')
		height = c.length(random_handler.main(10), 'cm')
		
		self.question = f"""A {bulletmass.g} g bullet is fired horizontally into a {blockmass.kg}kg block of wood suspended by a long cord. The bullet sticks in the block. Compute the speed of the bullet if the impact causes the block to swing {height.cm} cm above its initial level."""
		
		velocityprime = c.velocity(
		math.sqrt(
		(gravity.mpers2 * height.m) / (0.5)
		)
		)
		
		bulletvelocity = c.velocity(    
		((bulletmass.kg + blockmass.kg) * velocityprime.mpers)/bulletmass.kg
		)
		
		self.answer = f"""{round(bulletvelocity.kmpers,2)} km/s"""
		
		
class schaums_8_9:
	def __init__(self,*args,**kwargs): 
		
		x1 = c.length(0)
		x2 = c.length(random_handler.main(30,' int'), 'cm')
		x3 = c.length(random_handler.main(70, 'int'), 'cm')
		
		mass1 = c.mass(random_handler.main(200), 'g')
		mass2 = c.mass(random_handler.main(500), 'g')
		mass3 = c.mass(random_handler.main(400), 'g')
		
		
		self.question = f"""Three masses are placed on the x - axis: {mass1.g}g at x = {x1.cm},  {mass2.g}g at x = {x2.cm}cm, and {mass3.g}g at x = {x3.cm}cm. Find their center of mass"""
		
		xbar = c.length(
		(mass1.kg * x1.m + mass2.kg * x2.m + mass3.kg * x3.m) / (mass1.kg + mass2.kg + mass3.kg)
		)
		
		self.answer = f"""{round(xbar.cm,2)} cm"""
		
class schaums_8_10:
	def __init__(self,*args,**kwargs): 
		
		mass1 = c.mass(random_handler.main(4))
		mass2 = c.mass(random_handler.main(7))
		mass3 = c.mass(random_handler.main(5))
		
		x1 = c.length(0)
		y1 = c.length(random_handler.main(5))
		x2 = c.length(random_handler.main(3))
		y2 = c.length(random_handler.main(8))
		x3 = c.length(random_handler.main(-3))
		y3 = c.length(random_handler.main(-6))
		
		self.question = f"""A system consists of the following masses in the xy plane: {mass1.kg} kg at coordinates ( x = {x1.m} m, y = {y1.m} m), {mass2.kg}kg at (x = {x2.m} m, y = {y2.m} m), and {mass3.kg} kg at ( x = {x3.m} m, y = {y3.m} m). Find the position of its center of mass."""
		
		xbar = c.length(
		(x1.m * mass1.kg + x2.m*mass2.kg + x3.m*mass3.kg) / (mass1.kg + mass2.kg + mass3.kg)
		)
		
		ybar = c.length(
		(y1.m*mass1.kg + y2.m*mass2.kg + y3.m*mass3.kg) / (mass1.kg + mass2.kg + mass3.kg)
		)
		
		self.answer = f"""({round(xbar.m,2)} , {round(ybar.m,2)})"""
		
class schaums_8_11:
	def __init__(self,*args,**kwargs): 
		
		speed1y = c.velocity(random_handler.main(2))
		speed2x = c.velocity(random_handler.main(3))
		speed1xprime = c.velocity(random_handler.main(1.2))
		
		
		
		self.question = f"""Two balls of equal mass approach the coordinate origin, one moving downward along the +y-axis at {speed1y.mpers} m/s and the other moving to the right along the - x - axis at {speed2x.mpers} m/s. After they collide, one ball moves out to the right along the + x - axis at {speed1xprime.mpers} m/s. Find the scalar x and y velocity components of the other ball."""
		
		
		speed1y = c.velocity( - speed1y.mpers)
		
		speed2xprime = c.velocity(  speed2x.mpers - speed1xprime.mpers )
		
		speed2yprime = c.velocity( speed1y.mpers )
		
		self.answer = f"""{round(speed2xprime.mpers,2)} m/s, {round(speed2yprime.mpers,2)} m/s"""
		
class schaums_8_12:
	def __init__(self,*args,**kwargs): 
		
		truckmass = c.mass(random_handler.main(7500))
		carmass = c.mass(random_handler.main(1500))
		truckspeed = c.velocity(random_handler.main(5))
		carspeed = c.velocity(random_handler.main(20))
		totalmass = c.mass(truckmass.kg + carmass.kg)
		angle = c.angle(random_handler.main(30, 'int'), 'deg')
		
		self.question = f"""A {truckmass.kg} kg traveling at {truckspeed.mpers} m/s east collides with a {carmass.kg} kg car moving at {carspeed.mpers} m/s in a direction {angle.deg} degrees south of west. After collision, the two vehicles remain tangled together. With what speed and in what direction does the wreckage begin to move?"""
		
		speedxprime = c.velocity(
		(truckmass.kg * truckspeed.mpers - carmass.kg * carspeed.mpers * math.cos(angle.rad) ) / (totalmass.kg)
		)
		
		speedyprime = c.velocity(
		(truckmass.kg * truckspeed.mpers - carmass.kg * carspeed.mpers * math.sin(angle.rad) ) / (totalmass.kg)
		)
		
		speedprime = c.velocity(math.sqrt(speedxprime.mpers**2 + speedyprime.mpers**2))
		
		angle2 = c.angle(math.atan(speedyprime.mpers / speedxprime.mpers), 'rad')
		
		self.answer = f"""{round(speedprime.mpers,2)} m/s, {round(angle2.deg,2)} degrees"""


class schaums_8_13:
	def __init__(self,*args,**kwargs): 
		
		speed1 = c.velocity(random_handler.main(0.75))
		speed2 = c.velocity(random_handler.main(0.43))
		
		self.question = f"""Two identical balls collide head - on. The initial velocity of one is {speed1.mpers} m/s east while that of the other is {speed2.mpers} m/s west. If the collision is perfectly elastic, what is the final velocity of each ball?"""
		
		self.answer = f"""{round(- speed2.mpers,2)} m/s, {round(speed1.mpers,2)} m/s"""


class schaums_8_14():
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(1.0))
		mass2 = c.mass(random_handler.main(2.0))
		speed = c.velocity(random_handler.main(12))
		speed2 = c.velocity(random_handler.main(24))
		
		self.question = f"""A {mass.kg} kg ball moving at {speed.mpers} m/s collides head on with a {mass2.kg} kg ball moving in the opposite direction at {speed2.mpers} m/s. Determine the motion of each after impact if a) e = 2/3, b) the balls stick together and c) the collision is perfectly elastic."""
		
		speed2 = c.velocity(-speed2.mpers)
		
		equation = sympy.Eq(
		mass.kg * speed.mpers + mass2.kg * speed2.mpers , mass.kg * x + mass2.kg * y 
		)
		
		equation2 = sympy.Eq( 
		(2/3) * (speed.mpers - speed2.mpers) , y - x
		)
		
		equation3 = sympy.Eq(
		y, x
		)
		
		equation4 = sympy.Eq(
		1 * (speed.mpers - speed2.mpers) , y - x
		)
		
		
		equations = [equation, equation2]
		set1 = sympy.linsolve(equations, x, y)
		
		equations = [equation, equation3]
		set2 = sympy.linsolve(equations, x, y)
		
		equations = [equation, equation4]
		set3 = sympy.linsolve(equations, x, y)
		

		self.answer = f"""{round(set1.args[0][0],2)}, {round(set1.args[0][1])} m/s; {round(set2.args[0][0],2)}, {round(set2.args[0][1])} m/s; {round(set3.args[0][0],2)}, {round(set3.args[0][1])} m/s """

class schaums_8_15:
	def __init__(self,*args,**kwargs): 
		
		factor = random_handler.main(0.65, sigma = 0.1)
		
		self.question = f"""A ball is dropped from a height h above a tile floor and rebounds to a height of {round(factor,5)} h. Find the coefficient of restitution between the ball and the floor."""
		
		e = math.sqrt(factor)
		
		self.answer = f"""{round(e,5)} """


class schaums_8_16:
	def __init__(self,*args,**kwargs): 
		
		waterspeed = c.velocity(random_handler.main(80), 'cmpers')
		volume = c.volume(random_handler.main(30), 'mL')
		
		self.question = f"""What force is exerted on a stationary flat plate held perpendicular to a jet of water. The horizontal speed of the water is {waterspeed.cmpers} cm/s and {volume.mL} mL of the water hits the plate each second. Assume that the water moves parallel to the plate after striking it."""
		
		masswater = c.mass(volume.mL , 'g')
		force = c.force(masswater.kg*( - waterspeed.mpers))
		
		self.answer = f"""{round(force.N,4)} N"""
		
class schaums_8_17:
	def __init__(self,*args,**kwargs): 
			  
		mass = c.mass(random_handler.main(1500))
		speed = c.velocity(random_handler.main(50), 'kmpers')
		
		self.question = f"""A rocket standing on its launch platform points straight upward. Its jet engines are activated and eject gas at a rate of {mass.kg} kg/s. The molecules are expelled with a speed of {speed.kmpers} km/s. How much mass can the rocket initially have if it is slowly to rise because of the thrust of the engines?"""
		
		force = c.force( speed.mpers * mass.kg)
		mass = c.mass( force.N / gravity.mpers2)
		
		self.answer = f"""{round(mass.kg,2)} kg"""
		
		  
class example_9_1:
	def __init__(self,*args,**kwargs): 
		pass
		
class example_9_2:
	def __init__(self,*args,**kwargs): 
		length = c.length(random_handler.main(90), 'cm')
		arcLength = c.length(random_handler.main(15),'cm')
		
		self.question = f"""The bob of a pendulum {length.cm} cm swings through a {arcLength.cm} cm arc. Find the angle in radians and in degrees through which it swings."""
		
		angle = c.angle(arcLength.m / length.m, 'rad')
		
		self.answer = f"""Angle in degrees = {angle.deg} degrees
Angle in radians = {angle.rad} radians"""

class example_9_3:
	def __init__(self,*args,**kwargs): 
		omega = c.angularVelocity(random_handler.main(900),'rpm')
		distance = c.length(random_handler.main(20),'cm')
		
		self.question = f"""A fan turns at a rate of {omega.rpm} rpm. Find the angular speed of any point on one of the fan blades. b) Find the tangential speed of the tip of a blade if the distance from the center to the tip is {distance.cm} cm."""
		
		tangentialSpeed = c.velocity( omega.radpers * distance.m)

		self.answer = f"""Angular velocity = {omega.radpers} rad/s
Tangential Velocity = {tangentialSpeed.mpers} m/s"""

class example_9_4:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(25),'cm')
		tangentialSpeed = c.velocity(random_handler.main(5.0),'mpers')
		
		self.question = f"""A belt passes over a wheel of radius {radius.cm} cm. If a point on the belt has a speed of {tangentialSpeed.mpers} m/s, how fast is the wheel turning?"""
		
		omega = c.angularVelocity( tangentialSpeed.mpers / radius.m)
		
		self.answer = f"""Angular Velocity = {omega.radpers} rad/s"""
		
class example_9_5:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(40), 'cm')
		omegaF = c.angularVelocity(random_handler.main(900),'rpm')
		time = c.time(random_handler.main(20),'s')
		
		self.question = f"""A wheel of {radius.cm} cm radius rotates on a stationary axle. It is uniformly speeded up from rest to a speed of {omegaF.rpm} rpm in a time of {time.s}s. Find a) the constant angular acceleration of the wheel and b) the tangential acceleration of a point on its rim."""
		
		alpha = c.angularAcceleration((omegaF.radpers)/(time.s))
		tangentialAcceleration = c.acceleration( radius.m * alpha.radpers2)
		
		self.answer = f"""Angular acceleration = {alpha.radpers2} rad/s2
Tangential Acceleration = {tangentialAcceleration.mpers2} m/s2"""

class example_9_6:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(5),'cm')
		omegaI = c.angularVelocity(random_handler.main(30),'revpers')
		omegaF = c.angularVelocity(random_handler.main(20),'revpers')
		time = c.time(random_handler.main(2),'s')
		
		self.question = f"""A pulley of {radius.cm}-cm radius, on a motor, is turning at {omegaI.revpers} rev/s and slows down uniformly to {omegaF.revpers} rev/s in {time.s} s. Calculate a) the angular acceleration of the motor, b) the number of revolutions it makes in this time, and c) the length of belt it winds in this time."""
		
		alpha = c.angularAcceleration((omegaF.radpers - omegaI.radpers)/time.s)
		theta = c.angle( 0.5 * (omegaF.radpers + omegaI.radpers)* time.s, 'radians')
		revolutions = theta.rad / (2*math.pi)
		length = c.length( radius.m * theta.rad)
		
		self.answer =f"""Angular acceleration = {alpha.radpers2} rad/s2
Numer of revolution in this time = {revolutions} revolutions
Length of belt in winds in this time = {length.m} m"""

class example_9_7:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(30),'cm')
		velocityF = c.velocity(random_handler.main(15),'mpers')
		time = c.time(random_handler.main(8), 's')
		
		self.question = f"""A car has wheels of radius {radius.cm} cm. It starts from rest and accelerates uniformly to a speed of {velocityF.mpers} m/s in a time of {time.s} s. Find the angular acceleration of its wheels and the number of rotations one wheel makes in this time."""
		
		tangentialAcceleration = c.acceleration(velocityF.mpers / time.s)
		alpha = c.angularAcceleration(tangentialAcceleration.mpers2 / radius.m)
		theta = c.angle( 0.5*alpha.radpers2*time.s**2, 'radians')
		
		self.answer = f"""Angular acceleration = {alpha.radpers2} rad/s2
Revolutions = {theta.rev} revolutions"""

class example_9_8:
	def __init__(self,*args,**kwargs): 
		omegaI = c.angularVelocity(random_handler.main(900),'rpm')
		omegaF = c.angularVelocity(random_handler.main(300),'rpm')
		theta = c.angle(random_handler.main(50),'rev')
		
		self.question = f"""The spin drier of a washing machine revolving at {omegaI.rpm} rpm slows down uniformly to {omegaF.rpm} rpm while making {theta.rev} revolutions. Find a) the angular acceleration and b) the time required to turn through these {theta.rev} revolutions."""
		
		alpha = c.angularAcceleration((omegaF.radpers**2 - omegaI.radpers**2)/(2*theta.rad))
		omegaAverage = c.angularVelocity(0.5*(omegaI.radpers + omegaF.radpers))
		time = c.time(theta.rad/omegaAverage.radpers)
		
		self.answer = f"""Angular acceleration = {alpha.radpers2} rad/s2
Time = {time.s} s"""

class example_9_9:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(200), 'g')
		radius = c.length(random_handler.main(1.20),'m')
		omega = c.angularVelocity(random_handler.main(3.0), 'revpers')
		
		self.question = f"""A {mass.g}g object is tied to the end of a cord and whirled in a horizontal circle of radius {radius.m} m at a constant {omega.revpers} rev/s. Assume that the cord is horizontal , i.e, that the gravity can be neglected. Determine a) the acceleration of the object and b) the tension in the cord."""
		
		centripetalAcceleration = c.acceleration( radius.m * omega.radpers**2)
		tension = c.force(mass.kg * centripetalAcceleration.mpers2)
		
		self.answer =f"""Acceleration = {centripetalAcceleration.mpers2} m/s2
Tension  = {tension.N} N"""

class example_9_10:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(25), 'm')
		mu = random_handler.main(0.80)
		
		self.question = f"""What is the maximum speed at which a car can round a curve of {radius.m}-m radius on a level road if the coefficient of static friction between the tires and road is {mu}?"""
		
		velocity = c.velocity(math.sqrt(mu*gravity.mpers2*radius.m))
		
		#self.choices = ran2.choice(velocity.mpers, 'm/s')
		self.answer = f"""Maximum speed = {velocity.mpers} m/s"""
		
class example_9_11:
	def __init__(self,*args,**kwargs): 
		height = c.length(random_handler.main(20000), 'm')
		massMoon = c.mass(7.34e22,'kg')
		radiusMoon = c.length(1.738e6,'m')
		
		self.question = f"""A spaceship orbits the Moon at a height of {height.m} m. Assuming it to be subject only to the gravitational pull of the Moon, find its speed and the time it takes for one orbit. For the Moon, mass = {massMoon.kg} kg, and radius = {radiusMoon.m} m."""
		
		velocity = c.velocity(math.sqrt((c.GRAVITATIONAL_CONSTANT * massMoon.kg)/(radiusMoon.m + height.m)))
		
		time = c.time((2*math.pi*radiusMoon.m)/(velocity.mpers))
		
		self.answer = f"""Speed = {velocity.kmpers} km/s
Time for one orbit = {time.min} min"""

class example_9_12:
	def __init__(self,*args,**kwargs): 
		length = c.length(random_handler.main(24), 'cm')
		angle = c.angle(random_handler.main(30),'deg')
		
		self.question = f"""A ball is fastened to one end of a {length.cm} cm string and the other end is held fixed. The ball whirls in a horizontal circle. Find the speed of the ball in its circular path if the string makes an angle of {angle.deg} degrees with the vertical."""
		
		radius = c.length(length.m*math.sin(angle.rad))
		velocity = c.velocity(math.sqrt(radius.m * gravity.mpers2 * math.tan(angle.rad)))
		
		self.answer = f"""Velocity = {velocity.mpers} m/s"""
		
# class example_9_13:
	# def __init__(self,*args,**kwargs): 
		# height = c.length(random_handler.main(25), 'cm')
		# radius = c.length(random_handler.main(5), 'cm')
		
class example_9_14:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(0.90), 'kg')
		radius = c.length(random_handler.main(2.50), 'm')
		
		self.question = f"""A {mass.kg} kg body attached to a cord is whirled in a vertical circle of radius {radius.m} m. a) What minimum speed must it have at the top of the circle so as not to depart from the circular path? 
		b) Under condition a), what speed will the object have at the bottom of the circle? c) Find the tension in the cord when the body is at the bottom of the circle."""
		
		#a
		speedTop = c.velocity(math.sqrt(radius.m * gravity.mpers2))
		
		#b
		equation = sympy.Eq(0.5*x**2, 0.5*speedTop.mpers + gravity.mpers2*2*radius.m)
		speedBottom = c.velocity(max(sympy.solveset(equation,x,domain = sympy.Reals).args[0],sympy.solveset(equation,x,domain = sympy.Reals).args[1]))
		
		#c
		tension = c.force(mass.kg*(gravity.mpers2 + (speedBottom.mpers**2/radius.m)))
		
		self.answer = f"""Speed at top = {speedTop.mpers} m/s
Speed at bottom = {speedBottom.mpers} m/s
Tension at the bottom = {tension.N} N"""

class example_9_15:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(30),'m')
		speed = c.velocity(random_handler.main(13),'mpers')
		
		self.question = f"""A curve of radius {radius.m} m is to be banked so that a car may make a turn at a speed of {speed.mpers} m/s without depending on friction. What must be the slope of the curve?"""
		
		angle = c.angle(math.atan((speed.mpers**2)/(gravity.mpers2*radius.m)),'rad')
		
		self.answer = f"""Angle of banking = {angle.deg} degrees"""
		
class example_9_16:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(150), 'cm')
		mu = random_handler.main(0.30)
		
		self.question = f"""A cylindrical shell of inner radius {radius.m} m rotates at a certain angular speed. A wooden block rests against the inner surface and rotates with it. If the coefficient of static friction between block and surface is {mu}, how fast must the shell be rotating if the block is not to slip and fall? The axis of the cylindrical shell is vertical with respect to the Earth."""
		
		omega = c.angularVelocity(math.sqrt((gravity.mpers2)/(mu*radius.m)))
		
		self.answer = f"""Angular speed required = {omega.revpers} rev/s"""
		
#----CHAPTER 10 SCHAUMS -------------
class schaums_10_1:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(6.0), 'kg')
		radius = c.length(random_handler.main(40), 'cm')
		omega = c.angularVelocity(random_handler.main(300), 'revperm')
		
		
		self.question = f"""A wheel of mass {mass.kg} kg and radius of gyration {radius.cm} cm is rotating at {omega.revperm} rpm. Find its moment of inertia and its rotational KE."""
		
		moi = c.momentOfInertia( mass.kg * radius.m**2)
		
		KEr = c.energy( 0.5 * moi.kgm2 * omega.radpers**2 )
		
		self.answer = f"""Moment of Inertia = {moi.kgm2} kg m2
Rotational Kinetic Energy = {KEr.J} J"""

class schaums_10_2:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(500), 'g')
		radius = c.length(random_handler.main(7.0), 'cm')
		omega = c.angularVelocity(random_handler.main(30), 'revpers')
		
		
		self.question = f"""A {mass.g}-g uniform sphere of {radius.cm}-cm radius spins at {omega.revpers} rev / s on a axis through its center. Find its a) KEr b) angular momentum, and c) radius of gyration."""
		
		moi = c.momentOfInertia( (2/5) * mass.kg * radius.m**2 )
		ker = c.energy(0.5 * moi.kgm2 * omega.radpers**2) 
		L = c.angularMomentum( moi.kgm2 * omega.radpers )
		k = c.length( math.sqrt( moi.kgm2 / mass.kg ))
		
		self.answer = f"""Rotational Kinetic Energy = {ker.J} J
Angular Momentum = {L.kgm2pers} kgm2 / s
Radius of Gyration = {k.cm} cm"""

class schaums_10_3:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(70), 'kg')
		radius = c.length(random_handler.main(75), 'cm')
		alpha = c.angularAcceleration(random_handler.main(4.0), 'revpers2')
		
		self.question = f"""An airplane propeller has a mass of {mass.kg} kg and a radius of gyration of {radius.cm} cm. Find its moment of inertia. How large a torque is needed to give it an angular acceleration of {alpha.revpers2} rev/s2?"""
		
		moi = c.momentOfInertia( mass.kg * radius.m**2 )
		torque = c.torque( moi.kgm2 * alpha.revpers2 )
		
		self.answer = f"""Moment of inertia = {moi.kgm2} kg m2
Torque = {torque.kNm} kNm"""

class schaums_10_4:
	def __init__(self,*args,**kwargs): 
		
		force = c.force(random_handler.main(40), 'N')
		radius = c.length(random_handler.main(20), 'cm')
		moi = c.momentOfInertia(random_handler.main(30), 'kgm2')
		time = c.time(random_handler.main(4.0), 's')
		
		self.question = f"""A constant force of {force.N} N is applied tangentially to the rim of a wheel with {radius.cm} cm radius. The wheel has a moment of inertia of {moi.kgm2} kgm2. Find a) the angular acceleration, b) the angular speed after {time.s} s from rest, and c) the number of revolutions made in that {time.s} seconds. d) Find the work done on the wheel. e) Find the rotational kinetic energy of the wheel after {time.s} s.https://lesliecaminadecom.files.wordpress.com/2019/07/3tm1huii3jd9325mwm3w.png"""
		
		alpha = c.angularAcceleration( (force.N * radius.m) / (moi.kgm2) )
		omega = c.angularVelocity( alpha.radpers2 * time.s )
		theta = c.angle( 0.5 * omega.radpers * time.s )
		torque = c.torque(force.N * radius.m)
		work = c.energy( torque.Nm * theta.rad)
		ker = c.energy( 0.5 * moi.kgm2 * omega.radpers**2)
		
		self.answer = f"""Angular acceleration = {alpha.radpers2} rad/s2
Angular speed after {time.s} s = {omega.radpers} rad/s
Revolutions made after {time.s} s = {theta.rev} revolutions
Work done on the wheel = {work.J} J
Kinetic energy of the wheel after {time.s} s = {ker.J} J"""

class schaums_10_5:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(0.9), 'kg')
		radius = c.length(random_handler.main(8.0), 'cm')
		omega = c.angularVelocity(random_handler.main(1400), 'revperm')
		time = c.time(random_handler.main(35), 's')
		
		self.question = f"""The wheel on a grinder is a uniform {mass.kg}-kg disk of {radius.cm}-cm radius. It coasts uniformly to rest from {omega.revpers} rpm in a time of {time.s} s. How large a friction torque slows its motion?"""
		
		alpha = c.angularAcceleration( - omega.radpers / time.s )
		moi = c.momentOfInertia(0.5 * mass.kg * radius.m**2 )
		torque = c.torque( moi.kgm2 * alpha.radpers2)
		
		self.answer = f"""Angular acceleration = {alpha.radpers2} rad / s2
Moment of inertia = {moi.kgm2} kg m2
Torque = {torque.Nm} Nm"""


		
class schaums_10_7:
	def __init__(self,*args,**kwargs):
		moi = c.momentOfInertia(random_handler.main(3.8), 'kgm2')
		omegai = c.angularVelocity(random_handler.main(2.0), 'revpers')
		omegaf = c.angularVelocity(omegai.revpers + random_handler.main(3), 'revpers')
		theta = c.angle(random_handler.main(6), 'rev')
		
		self.question = f"""A flywheel has a moment of inertia of {moi.kgm2} kgm2. What constant torque is required to increase its frequency from {omegai.revpers} rev/s to {omegaf.revpers} rev/s in {theta.rev} revolutions?"""
		
		torque = c.torque(
		(0.5 * moi.kgm2 * omegaf.radpers**2 - 0.5 * moi.kgm2 * omegai.radpers**2) / (theta.radians)
		)
		
		self.answer = f"""Torque = {torque.Nm} Nm"""
		
class schaums_10_8:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(400), 'g')
		radius = c.length(random_handler.main(15), 'cm')
		height = c.length(random_handler.main(2), 'm')
		time = c.time(random_handler.main(6.5), 's')
		
		self.question = f"""A mass m = {mass.g} g hangs from the rim of a wheel of radius r = {radius.cm} cm. When released from rest, the mass falls {height.m} m in {time.s} s. Find the moment of inertia of the wheel. https://lesliecaminadecom.files.wordpress.com/2019/07/f3c02304q820ekcprt0g.png"""
		
		equation = sympy.Eq( height.m, 0.5 * x * time.s**2)
		accel_set = sympy.solveset(equation,x)
		accel_list = list(accel_set)
		acceleration = c.acceleration(accel_list[0])
		alpha = c.angularAcceleration(acceleration.mpers2)
		
		equation = sympy.Eq(mass.kg * gravity.mpers2 - x, mass.kg * acceleration.mpers2)
		tension_set = sympy.solveset(equation, x)
		tension_list = list(tension_set)
		tension = c.force(tension_list[0])
		
		moi = c.momentOfInertia( (tension.N * radius.m) / (alpha.radpers2) )
		
		self.answer = f"""Moment of inertia of the wheel = {moi.kgm2} kgm2"""
		
class schaums_10_10:
	def __init__(self,*args,**kwargs): 
		moi = c.momentOfInertia(random_handler.main(1.7), 'kgm2')
		radius2 = c.length(random_handler.main(20), 'cm')
		radius1 = c.length(radius2.cm + random_handler.main(30), 'cm')
		mass2 = c.mass(random_handler.main(1.8))
		mass1 = c.mass(mass2.kg + random_handler.main(0.2), 'kg')
		
		self.question = f"""The moment of inertia of the pulley system is I = {moi.kgm2} kgm2, while r1 = {radius1.cm} cm and r2 = {radius2.cm} cm. Find the angular acceleration of the pulley system and the tensions FT1 and FT2. The masses are m1 = {mass1.kg} kg and m2 = {mass2.kg} kg.
		https://lesliecaminadecom.files.wordpress.com/2019/07/qav194zz9ychy8hmf2yv.png"""
		
		equation = sympy.Eq(
		(mass1.kg *gravity.mpers2 - mass1.kg*radius1.m*x)*radius1.m - (mass2.kg*gravity.mpers2+mass2.kg*radius2.m*x)*radius2.m , moi.kgm2*x
		)
		
		alpha_set = sympy.solveset(equation,x)
		alpha_list = list(alpha_set)
		alpha = c.angularAcceleration(alpha_list[0])
		tension1 = c.force( mass1.kg*(gravity.mpers2 - radius1.m*alpha.radpers2))
		tension2 = c.force( mass2.kg*(gravity.mpers2 + radius2.m*alpha.radpers2))
		
		self.answer = f"""Angular acceleration = {alpha.radpers2} rad/s2
Tension FT1 = {tension1.N} N
Tension FT2 = {tension2.N} N"""

class schaums_10_12:
	def __init__(self,*args,**kwargs): 
		omega = c.angularVelocity(random_handler.main(20), 'revpers')
		torque = c.torque(random_handler.main(75), 'Nm')
		
		self.question = f"""A motor runs at {omega.revpers} rev/s and supplies a torque of {torque.Nm} Nm. What horsepower is it delivering?"""
		
		power = c.power( torque.Nm * omega.radpers)
		
		self.answer = f"""Power = {power.hp} hp"""
		
class schaums_10_13:
	def __init__(self,*args,**kwargs): 
		diameter = c.length(random_handler.main(38), 'cm')
		radius = c.length(diameter.cm /2 , 'cm')
		omega = c.angularVelocity(random_handler.main(1200), 'revperm')
		tension_slack = c.force(random_handler.main(130))
		tension_tight = c.force(tension_slack.N + random_handler.main(470))
		
		self.question = f""" The driving wheel of a belt drive attached to an electric motor has a diameter of {diameter.cm} cm and operates at {omega.revperm} rpm. The tension in the belt is {tension_slack.N} N on the slack side and {tension_tight.N} N on the tight side. Find the horsepower transmitted to the wheel by the belt."""
		torque = c.torque( (tension_tight.N - tension_slack.N) * radius.m )
		power = c.power( torque.Nm * omega.radpers )
		self.answer = f"""Power = {power.hp} hp"""
		
class schaums_10_14:
	def __init__(self,*args,**kwargs): 
		power = c.power(random_handler.main(0.75), 'hp')
		time = c.time(random_handler.main(8), 's')
		moi = c.momentOfInertia(random_handler.main(2.0), 'kgm2')
		
		self.question = f"""A {power.hp}-hp motor acts for {time.s} s on an initially nonrotating wheel having a moment of inertia {moi.kgm2} kg m2. Find the angular speed developed in the wheel, assuming no losses."""
		
		omega = c.angularVelocity(
		math.sqrt((power.W * time.s) / (0.5 * moi.kgm2))
		, 'radpers')
		
		self.answer = f"""Angular speed after {time.s} s = {omega.radpers} rad/s"""
		
class schaums_10_15:
	def __init__(self,*args,**kwargs): 
		velocity = c.velocity(random_handler.main(20), 'mpers')
		
		self.question = f"""A uniform solid sphere rolls on a horizontal surface at {velocity.mpers} m/s and then rolls up the incline. If friction losses are negligible, what will be the value of 'h' where the ball stops?
		https://lesliecaminadecom.files.wordpress.com/2019/07/jd3yi24fhv9v6siy9h6t.png"""
		
		equation = sympy.Eq(
		(1/2)*velocity.mpers**2 + (1/5)*velocity.mpers**2, gravity.mpers2 * x
		)
		
		height_set = sympy.solveset(equation, x)
		height_list = list(height_set)
		height = c.length(height_list[0])
		
		self.answer = f"""Height reached = {height.m} m"""
		
class schaums_10_16:
	def __init__(self,*args,**kwargs): 
		radius = c.length(random_handler.main(20), 'cm')
		height = c.length(random_handler.main(5), 'm')
		
		self.question = f"""Starting from rest, a hoop of {radius.cm}-cm radius rolls down a hill to a point {height.m} m below its staring point. How fast is it rotating at that point?"""
		
		omega = c.angularVelocity(
		math.sqrt( (gravity.mpers2 * height.m) / (radius.m**2) )
		)
		
		self.answer = f"""Angular velocity = {omega.radpers} rad/s"""
		
class schaums_10_17:
	def __init__(self,*args,**kwargs): 
		velocity = c.velocity(random_handler.main(80), 'cmpers')
		height = c.length(random_handler.main(18), 'cm')
		
		self.question = f"""A solid disk rolls over the top of a hill on a track, its speed is {velocity.cmpers} cm/s. If friction losses are negligible, how fast is the disk moving when it is {height.cm} cm below the top?"""
		
		equation = sympy.Eq(
		0.5 * velocity.mpers**2 + 0.25 * velocity.mpers**2 + gravity.mpers2 * height.m , 0.5 * x**2 + 0.25 * x**2
		)
		
		velocity2_set = sympy.solveset(equation, x)
		velocity2_list = list(velocity2_set)
		for i in range(len(velocity2_list)):
			if velocity2_list[i] > 0:
				velocity2 = c.velocity(velocity2_list[i], 'mpers')
				
		self.answer = f"""Final velocity = {velocity2.mpers} m/s"""
		
class schaums_10_18:
	def __init__(self,*args,**kwargs): 
		mass1 = c.mass(random_handler.main(2))
		mass2 = c.mass(random_handler.main(3))
		mass3 = c.mass(random_handler.main(4))
		mass4 = c.mass(random_handler.main(5))
		width = c.length(random_handler.main(120), 'cm')
		length = c.length(width.cm + random_handler.main(130), 'cm')
		
		self.question = f"""Find the moment of inertia of the four masses shown if m1 = {mass1.kg} kg, m2 = {mass2.kg} kg, m3 = {mass3.kg} kg, m4 = {mass4.kg} kg, and the dimensions of the rectangle is {length.cm} cm x {width.cm} cm through a) point A and b) through point B. 
		https://lesliecaminadecom.files.wordpress.com/2019/07/4p1vauikbd5ay6r8ftk1.png"""
		radius = c.length(0.5 * math.sqrt( length.m**2 + width.m**2))
		moi = c.momentOfInertia( (mass1.kg + mass2.kg + mass3.kg + mass4.kg) * radius.m**2)

		
		r_short = c.length(length.m / 2)
		r_long = c.length(math.sqrt(r_short.m**2 + width.m**2))
		moi2 = c.momentOfInertia(
		(mass1.kg + mass2.kg) * r_short.m + (mass3.kg + mass4.kg) * r_long.m
		)
		
		self.answer = f"""Moment of inertia at situation A = {moi.kgm2} kg m2
Moment of inertia at situation B = {moi2.kgm2} kg m2"""
		

class schaums_10_19:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(6), 'kg')
		diameter = c.length(random_handler.main(80), 'cm')
		radius = c.length(diameter.cm/2, 'cm')
		height = c.length((radius.cm/2) + random_handler.main(2), 'cm')
		self.question = f"""The uniform circular disk has mass {mass.kg} kg and diameter {diameter.cm} cm. Compute its moment of inertia about an axis perpendicular to the page a) through G and b) through A.
		https://lesliecaminadecom.files.wordpress.com/2019/07/ml09wrb0uk1k5d99h5ln.png"""
		
		moig = c.momentOfInertia( 0.5 * mass.kg * radius.m**2 )
		
		moia = c.momentOfInertia( moig.kgm2 + mass.kg * height.m**2)
		
		self.answer = f"""Moment of inertia about axis G = {moig.kgm2} kgm2
Moment of inertia about axis A = {moia.kgm2} kgm2"""

class schaums_10_20:
	def __init__(self,*args,**kwargs): 
		diameter = c.length(random_handler.main(1.8), 'm')
		radius = c.length(diameter.m/2, 'm')
		weight = c.force(random_handler.main(10), 'kN')
		velocity = c.velocity(random_handler.main(4.0), 'mpers')
		distance = c.length(random_handler.main(3), 'm')
		
		self.question = f"""A large roller in the form of a uniform cylinder is pulled by a tractor to compact earth; it has a {diameter.m}-m diameter and weighs {weight.kN} kN. If frictional losses can be ignored, what average horsepower must the tractor provide to accelerate it from rest to a speed of {velocity.mpers} m/s in a horizontal distance of {distance.m} m?"""
		
		mass = c.mass(weight.N / gravity.mpers2)
		moi = c.momentOfInertia( 0.5 * mass.kg * radius.m**2)
		omega = c.angularVelocity(velocity.mpers / radius.m, 'radpers')
		work = c.energy( 0.5 * moi.kgm2 * omega.radpers**2 + 0.5 * mass.kg * velocity.mpers**2)
		time = c.time( distance.m / velocity.mpers)
		power = c.power( work.J / time.s)
		
		self.answer = f"""Power required = {power.hp} hp"""
		
class schaums_10_22:
	def __init__(self,*args,**kwargs): 
		omega1 = c.angularVelocity(random_handler.main(0.25), 'revpers')
		omega2 = c.angularVelocity(omega1.revpers + random_handler.main(0.55), 'revpers')
		
		self.question = f"""A man stands on a freely rotating platform. With his arms extended, his rotation frequency is {omega1.revpers} rev/s. But when he draws them in, his frequency is {omega2.revpers} rev/s. Find the ratio of his moment of inertia in the first case to that in the second case."""
		
		ratio = omega2.revpers / omega1.revpers
		
		self.answer = f"""Ratio of moment of inertias = {ratio}"""
		
class schaums_10_25:
	def __init__(self,*args,**kwargs): 
		moi = c.momentOfInertia(random_handler.main(0.0150, 'noround'))
		omega2 = c.angularVelocity(random_handler.main(2), 'revpers')
		omega = c.angularVelocity(omega2.revpers + random_handler.main(1), 'revpers')
		radius = c.length(random_handler.main(20), 'cm')
		
		self.question = f"""A disk like the lower one in the figure has I = {moi.kgm2} kgm2 and is turning at {omega.revpers} rev/s. A trickle of sand falls onto the disk at a distance of {radius.cm} cm from the axis and builds a {radius.cm}-cm radius ring of sand on it. How much sand must fall on the disk for it to slow to {omega2.revpers} rev/s.
		https://lesliecaminadecom.files.wordpress.com/2019/07/9rk4kwqsp7w7s71o9k96.png"""
		
		mass_sand = c.mass(
		(moi.kgm2 * (omega.radpers - omega2.radpers)) / (radius.m**2 * omega2.radpers)
		)
		
		self.answer = f"""Mass of sand = {mass_sand.kg} kg"""
		

		
class schaums_11_2:
	def __init__ (self,*args, **kwargs):
		vibrations = random_handler.main(12,'int')
		time = c.time(random_handler.main(40))
		
		self.question = f"""A spring makes {vibrations} vibrations in {time.s} s. Find the period and the frequency of vibration."""
		
		frequency = c.frequency(vibrations / time.s)
		period = c.time(time.s / vibrations)
		
		self.answer = f"""Period: {period.s} s, Frequency: {frequency.hz} Hz"""
		
class schaums_11_3:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(400),'g')
		ydistance = c.length(random_handler.main(35),'cm')
		additionalMass = c.mass(random_handler.main(400),'g')
		gravity = c.acceleration(9.81)
		
		self.question = f"""When a {mass.g} g mass is hung at the end of a vertical spring, the spring stretches {ydistance.cm} cm. What is the spring constant of the spring, and how much further will it stretch if an additional {additionalMass.g} - g mass is hung from it?"""
		
		springConstant = c.springConstant(mass.kg * gravity.mpers2 / ydistance.m)
		ydistanceWithAdditionalMass = c.length((mass.kg + additionalMass.kg)*gravity.mpers2 / springConstant.Nperm)
		
		self.answer = f"""Spring Constant: {springConstant.Nperm} N/m, Spring Displacement {ydistanceWithAdditionalMass.cm} cm"""
		
class schaums_11_4:
	def __init__(self, *args,**kwargs):
		mass = c.mass(random_handler.main(200),'g')
		k = c.springConstant(random_handler.main(7))
		maxDisplacement = c.length(random_handler.main(5),'cm')
		specificDisplacement = c.length(random.uniform(1,maxDisplacement.cm),'cm')
		
		
		self.question = f"""A {mass.g} - g mass vibrates horizontally without friction at the end of a horizontal spring for which k = {k.Nperm} N/m. The mass is displaced {maxDisplacement.cm} cm from equilibrium and released. Find a) its maximum speed and b) its speed when it is {specificDisplacement.cm} cm from equilibrium. c) What is its acceleration in each of these cases?"""
		
		#maximum speed happens at x = 0
		vMax = c.velocity(maxDisplacement.m * math.sqrt(k.Nperm / mass.kg))
		
		vSpecific = c.velocity((k.Nperm / mass.kg) * (maxDisplacement.m**2 - specificDisplacement.m**2) )
		
		aAtXZero = c.acceleration(0)
		aAtXSpecific = c.acceleration(k.Nperm * specificDisplacement.m / mass.kg)
		
		self.answer = f"""Max speed = {vMax.mpers} m/s, 
Speed at x = {specificDisplacement.cm} cm = {vSpecific.mpers} m/s, 
Acceleration at x=0 = {aAtXZero.mpers2} m/s2, 
Acceleration at x = {specificDisplacement.cm} cm = {aAtXSpecific.mpers2} m/s2."""
		
class schaums_11_5:
	def __init__(self, *args, **kwargs):
		mass = c.mass(random_handler.main(50,'int'),'g')
		A = c.length(random_handler.main(12,'int'),'cm')
		period = c.time(random_handler.main(1.70, round=2), 's')
		xSpecific = c.length(random.randint(0, int(A.cm)), 'cm')
		
		
		self.question = f"""A {mass.g}-g mass  vibrates in SHM at the end of the spring. The amplitude of the motion is {A.cm} cm, and the period is {period.s} s. Find a) the frequency, b) the spring constant, c) the maximum speed of the mass, d) the maximum acceleration of the mass, e) the speed when the displacement is {xSpecific.cm} cm and f) the acceleration when x = {xSpecific.cm} cm."""
		
		frequency = c.frequency(1 / period.s)
		k = c.springConstant( 4 * math.pi**2 * mass.kg / period.s**2  )
		vMax = c.velocity( A.m * math.sqrt(k.Nperm / mass.kg))
		aMax = c.acceleration ( k.Nperm * A.m / mass.kg)
		vSpecific = c.velocity(abs(math.sqrt((k.Nperm / mass.kg))*math.sqrt((A.m**2 - xSpecific.m**2))))
		aSpecific = c.acceleration(-k.Nperm * xSpecific.m / mass.kg)
		
		self.answer = f"""Frequency = {frequency.Hz} Hz
Spring Constant = {k.Nperm} N / m
Velocity Max = {vMax.mpers} m/s
Acceleration Max = {aMax.mpers2} m/s2
Velocity at x:{xSpecific.cm} cm = {vSpecific.mpers} m/s
Acceleration at x:{xSpecific.cm} cm = {aSpecific.mpers2} m/s2"""

class schaums_11_6:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(50),'g')
		massAdd = c.mass(random_handler.main(20),'g')
		xAdd = c.length(random_handler.main(7),'cm')
		gravity = c.acceleration(9.81,'mpers2')
		
		self.question = f"""A {mass.g} g mass hangs at the end of a Hookean spring. When {massAdd.g} g more is added to the end of the spring, it stretches {xAdd.cm} cm more. a) Find the spring constant. b) If the {massAdd.g} g is now removed, what will be the period of the motion?"""

		k = c.springConstant(mass.kg * gravity.mpers2 / xAdd.m)
		period = c.time(math.pi * 2 * math.sqrt(mass.kg / k.Nperm))
		
		self.answer = f"""Spring Constant = {k.Nperm} N/m
Period = {period.s} s"""

class schaums_11_7:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(2),'kg')
		force = c.force(random_handler.main(8),'N')
		A = c.length(random_handler.main(20),'cm')
		
		self.question = f"""A long light piece of spring steel is clamped at its lower end and a {mass.kg} kg ball is fastened to its top end. A horizontal force of {force.N} N is required to displace the ball {A.cm} cm to one side as shown. Assume the system to undergo SHM when released. Find a) the force constant of the spring and b) the period with which the ball will vibrate back and forth."""
		
		k = c.springConstant(force.N / A.m)
		period = c.time(math.pi * 2 * math.sqrt( mass.kg / k.Nperm))
		
		self.answer = f"""Spring Constant = {k.Nperm} N/m
Period = {period.s} s"""

class schaums_11_8:
	def __init__(self,*args,**kwargs):
		A = c.length(random_handler.main(6),'cm')
		gravity = c.acceleration(9.81,'mpers2')
		
		self.question = f"""When a mass m is hung on a spring, the spring stretches {A.cm} cm. Determine its period of vibration if it is pulled down a little and released."""
		
		mass = c.mass(1,'kg')
		k = c.springConstant( mass.kg * gravity.mpers2 / A.m )
		period = c.time(2 * math.pi * math.sqrt( mass.kg / k.Nperm ))
		
		self.answer = f"""Period = {period.s} s"""
		

class schaums_11_10:
	def __init__(self,*args,**kwargs):
		A = c.length(random_handler.main(7),'cm')
		gravity = c.acceleration(9.81, 'mpers2')
		
		self.question = f"""In a certain engine, a piston undergoes vertical SHM with amplitude {A.cm} cm. A washer rests on top of the piston. As the motor speed is slowly increased, at what frequency will the washer no longer stay in contact with the piston?"""
		
		period = c.time(math.pi * 2 * math.sqrt( A.m / gravity.mpers2))
		frequency = c.frequency(1/period.s)
		self.answer =f"""Frequency: {frequency.Hz} Hz"""
		
class schaums_11_11:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(20),'kg')
		kOneSpring = c.springConstant(random_handler.main(30),'Npercm')
		
		self.question = f"""A {mass.kg}kg electric motor is mounted on four vertical springs, each having a spring constant of {kOneSpring.Npercm} N/cm. Find the period with which the motor vibrates vertically."""
		
		period = c.time(2 * math.pi * math.sqrt( mass.kg / (4 * kOneSpring.Nperm)))
		
		self.answer = f"""Period =  {period.s} s"""
		
class schaums_11_13:
	def __init__(self,*args,**kwargs):
		L = c.length(random_handler.main(150.3), 'cm')
		cycles = random_handler.main(100)
		time100Cycles = c.time(random_handler.main(246.7),'s')
		
		self.question = f"""Compute the acceleration due to gravity at a place where a simple pendulum {L.cm} cm long makes {cycles} cycles in {time100Cycles.s} s"""
		
		period = c.time(time100Cycles.s / cycles)
		gravity = c.acceleration((4*math.pi**2*L.m)/(period.s**2))
		
		self.answer = f"""Acceleration = {gravity.mpers2} m/s2"""
		
class schaums_11_14:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(200),'g')
		displacement = c.length(random_handler.main(15),'cm')
		k = c.springConstant(random_handler.main(400),'Nperm')
		
		self.question = f"""The {mass.g} g mass is pushed to the left against the spring and compresses the spring {displacement.cm} cm from its equilibrium position. The system is then released, and the mass shoots to the right. If friction can be ignored, how fast will the mass be moving as it shoots away? Assume the mass of the spring to be very small. Spring constant is {k.Nperm} N/m."""
		
		velocity = c.velocity( math.sqrt(k.Nperm * displacement.m**2 / mass.kg))
		
		self.answer = f"""Velocity = {velocity.mpers} m/s"""
		
class schaums_11_17:
	def __init__(self,*args,**kwargs):
		mass = c.mass(random_handler.main(17),'g')
		A = c.length(random_handler.main(0.75),'cm')
		omega = c.angularVelocity(random_handler.main(63),'radpers')
		
		timeSpecific = c.time(random_handler.main(0.020),'s')
		
		self.question = f"""A {mass.g}g particle at the end of a spring moves according to the equation y = {A.cm} sin ({omega.radpers} t) where y is in cm and t is in seconds. Find the amplitude and frequency of its motion, its position at t = {timeSpecific.s}s, and the spring constant."""
		
		frequency = c.frequency( omega.radpers / (2*math.pi))
		positionSpecific = c.length(A.cm*math.sin(omega.radpers * timeSpecific.s),'cm')
		k = c.springConstant(4*math.pi**2 * frequency.Hz**2 * mass.kg)
		
		self.answer = f"""Amplitude = {A.cm} cm
Frequency = {frequency.Hz} Hz
Position at t = {timeSpecific.s} s = {positionSpecific.cm} cm
Spring Constant = {k.Nperm} N/m"""

#chapter 12 - strength of materials overlap
#chapter 13 - hysrostatics
class schaums_13_1:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(80), 'kg')
		length = c.length(random_handler.main(2), 'm')
		area = c.area(random_handler.main(25), 'cm2')
		
		self.question = f"""An {mass.kg}-kg metal cylinder, {length.m} m long and with each end of area {area.cm2} cm2, stands vertically on one end. What pressure does the cylinder exert on the floor?"""

		pressure = c.pressure( (mass.kg * gravity.mpers2) / (area.m2) )
		
		self.answer = f"""Pressure = {pressure.Pa} Pa"""
		
class schaums_13_2:
	def __init__(self,*args,**kwargs): 
		patm = 101325
		width = c.length(random_handler.main(40), 'cm')
		length = c.length(width.cm + random_handler.main(40), 'cm')
		
		self.question = f"""Atmospheric pressure is about {patm} Pa. How large a force does the still air in a room exert on the inside of a window pane that is {length.cm} cm x {width.cm} cm?"""
		
		force = c.force( patm * length.m * width.m )
		
		self.answer = f"""Force = {force.N} N"""
		
class schaums_13_3:
	def __init__(self,*args,**kwargs): 
		
		depth = c.length(random_handler.main(76), 'cm')
		density_water = c.density(1, 'gpercm3')
		density_mercury = c.density(13.6, 'gpercm3')
		height = c.length(random_handler.main(76), 'cm')
		
		self.question = f"""Find the pressure due to the fluid at a depth of {depth.cm} cm in still a) water ( rho_water = {density_water.gpercm3} ) and b) mercury (rho_mercury = {density_mercury.gpercm3} g/cm3)"""
		
		pressure_water = c.pressure( density_water.kgperm3 * gravity.mpers2 * height.m)
		pressure_mercury = c.pressure( density_mercury.kgperm3 * gravity.mpers2 * height.m)
		
		self.answer = f"""Pressure for water = {pressure_water.kPa} kPa
Pressure for mercury = {pressure_mercury.kPa} kPa"""

class schaums_13_4:
	def __init__(self,*args,**kwargs): 
		depth = c.length(random_handler.main(120), 'm')
		density_sea = c.density(1.03, 'gpercm3')
		
		
		self.question = f"""When a submarine dives to a depth of {depth.m} m, to how large a total pressure is its exterior surface subjected? The density of seawater is about {density_sea.gpercm3} g/cm3."""
		
		pressure_total =  c.pressure( 101325 + density_sea.kgperm3 * gravity.mpers2 * depth.m)
		
		self.answer = f"""Total pressure = {pressure_total.MPa} MPa"""
		
class schaums_13_5:
	def __init__(self,*args,**kwargs): 
		density_water = c.density(1000, 'kgperm3')
		pressure = c.pressure(random_handler.main(270), 'kPa')
		self.question = f"""How high would water rise in the pipes of a building if the water pressure gauge shows the pressure at the ground floor to be {pressure.kPa} kPa?"""
		height = c.length(pressure.Pa / (density_water.kgperm3 * gravity.mpers2))
		self.answer = f"""Height = {height.m} m"""
		
class schaums_13_6:
	def __init__(self,*args,**kwargs): 
		area = c.area(random_handler.main(8), 'km2')
		depth2 = c.length(random_handler.main(3), 'm')
		depth = c.length(depth2.m + random_handler.main(9), 'm')
		density_water = c.density(1000, 'kgperm3')
		
		self.question = f"""A reservoir dam holds an {area.km2} km2 lake behind it. Just behind the dam, the lake is {depth.m} m deep. What is the water pressure a) at the base of the dam and b) at a point {depth2.m} m down from the lake's surface."""
		
		pressure_a = c.pressure( density_water.kgperm3 * gravity.mpers2 * depth.m) 
		pressure_b = c.pressure( density_water.kgperm3 * gravity.mpers2 * depth2.m) 
		
		self.answer = f"""Pressure at base of dam = {pressure_a.kPa} kPa
Pressure at base of dam = {pressure_b.kPa} kPa"""

class schaums_13_7:
	def __init__(self,*args,**kwargs): 
		weight = c.force(random_handler.main(200), 'N')
		area = c.area(random_handler.main(8), 'cm2')
		height = c.length(random_handler.main(25), 'cm')
		density_mercury = c.density(13600, 'kgperm3')
		self.question = f"""A weighted piston confines a fluid density 'rho' in a closed container as shown in the figure. The combined weight of piston and weight is {weight.N} N, and the cross-sectional area of the piston is A = {area.cm2} cm2. Find the total pressure at point B if the fluid is mercury and h = {height.cm} cm (rho_mercury = {density_mercury.kgperm3} kg/m3). What would an ordinary pressure gauge read at B?
		https://lesliecaminadecom.files.wordpress.com/2019/07/6fpqtq2jgau29qsitd0x.png"""
		
		patm = c.pressure(101325, 'Pa')
		pweight = c.pressure( weight.N / area.m2)
		pheight = c.pressure( density_mercury.kgperm3 * gravity.mpers2 * height.m)
		
		ptotal = c.pressure( patm.Pa + pweight.Pa + pheight.Pa)
		
		self.answer= f"""Total pressure = {ptotal.Pa} Pa"""
		
class schaums_13_8:
	def __init__(self,*args,**kwargs): 
		area = c.area(random_handler.main(200), 'cm2')
		area2 = c.area(random_handler.main(5), 'cm2')
		force2 = c.force(random_handler.main(250), 'N')
		
		self.question = f"""In a hydraulic press such as the one in the figure, the large piston has cross-sectional area A1 = {area.cm2} cm2 and the small piston has cross-sectional area A2 = {area2.cm2} cm2. If a force of {force2.N} N is applied to the small piston, find the force F1 on the large piston."""
		
		force = c.force( (area.m2 / area2.m2) * force2.N )
		
		self.answer = f"""Force F1 = {force.kN} kN"""
		
class schaums_13_9:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(600), 'kg')
		area = c.area(random_handler.main(800), 'cm2')
		area2 = c.area(random_handler.main(25), 'cm2')
		density_oil = c.density(0.78, 'gpercm3')
		height = c.length(random_handler.main(8), 'm')
		
		self.question = f"""For the system shown in the following figure, the cylinder on the left,  at L, hass a mass of {mass.kg} kg and a cross-sectional area of {area.cm2} cm2. The piston on the right, at S, has a cross-sectional area of {area2.cm2} cm2 and a negligible weight. If the apparatus is filled with oil ( rho = {density_oil.gpercm3} g/cm3), find the force F required to hold the system in equilibrium as shown. The distance between the pistons is {height.m} m. 
		https://lesliecaminadecom.files.wordpress.com/2019/07/e2uyzh98oj3wltryzpxe.png"""
		
		equation = sympy.Eq(
		(mass.kg * gravity.mpers2) / (area.m2),
		(x / area2.m2) + density_oil.kgperm3 * gravity.mpers2 * height.m
		)
		
		force_set = sympy.solveset(equation, x)
		force_list = list(force_set)
		force = c.force(force_list[0])
		
		self.answer = f"""Force required = {force.N} N"""
		
class schaums_13_10:
	def __init__(self,*args,**kwargs): 
		density_oil = c.density(890, 'kgperm3')
		pressure_limit = c.pressure(random_handler.main(350), 'kPa')
		
		self.question = f"""A barrel will rupture when the gauge pressure within it reaches {pressure_limit.kPa} kPa. It is attached to the lower end of a vertical pipe, with the pipe and barrel filled with oil (rho = {density_oil.kgperm3} kg/m3). How long can the pipe be if the barrel is not to rupture?"""
		
		height = c.length(
		pressure_limit.Pa / (density_oil.kgperm3 * gravity.mpers2)
		)
		
		self.answer = f"""Length of the pipe = {height.m} m"""
		
class schaums_13_11:
	def __init__(self,*args,**kwargs): 
		height_oil = c.length(random_handler.main(2), 'cm')
		height_water = c.length(random_handler.main(8), 'cm')
		density_oil = c.density(0.80, 'gpercm3')
		density_water = c.density(1000, 'kgperm3')
		
		self.question = f"""A vertical test tube has {height_oil.cm} cm of oil (rho = {density_oil.gpercm3} g/cm3) floating on {height_water.cm} cm of water. What is the pressure at the bottom of the tube due to the fluid in it?"""
		
		pressure = c.pressure(
		density_oil.kgperm3 * gravity.mpers2 * height_oil.m + density_water.kgperm3 * gravity.mpers2 * height_water.m
		)
		
		self.answer = f"""Total pressure = {pressure.Pa} Pa"""
		
class schaums_13_12:
	def __init__(self,*args,**kwargs): 
		height2 = c.length(random_handler.main(31), 'cm')
		height = c.length(height2.cm + random_handler.main(9), 'cm')
		density_water = c.density(1000, 'kgperm3')
		
		self.question = f"""A column of water {height.cm} cm high supports a {height2.cm} cm column of an unknown fluid. What is the density of the unknown fluid?
		https://lesliecaminadecom.files.wordpress.com/2019/07/p0b41b0r6bt8nh5uz9im.png"""
		
		density_other = c.density(
		( height.m / height2.m ) * density_water.kgperm3 
		)
		
		self.answer= f"""Density of the unknown fluid = {density_other.kgperm3} kg / m3"""
		
class schaums_13_13:
	def __init__(self,*args,**kwargs): 
		
		height = c.length(random_handler.main(5), 'cm')
		p_atm = c.pressure(76, 'cmHg')
		density_mercury = c.density(13.6, 'gpercm3')
		
		self.question = f"""The U - tube device connected to the tank is called a "manometer". The mercury in the tube stands higher in one side than the other. What is the pressure in the tank if atmospheric pressure is {p_atm.cmHg} cmHg? The density of mercury is {density_mercury.gpercm3} g/cm3, and the height difference of the fluids is {height.cm} cm"""
		
		equation = sympy.Eq(
		x + height.m * density_mercury.kgperm3 * gravity.mpers2,
		p_atm.mHg * density_mercury.kgperm3 * gravity.mpers2
		)
		
		pressure_tank_set = sympy.solveset(equation, x)
		pressure_tank_list = list(pressure_tank_set)
		pressure_tank = c.pressure(pressure_tank_list[0])
		
		self.answer = f"""Pressure in the tank = {pressure_tank.kPa} kPa"""
		
class schaums_13_14:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(25), 'g')
		density_aluminum = c.density(2700, 'kgperm3')
		density_water = c.density(1000, 'kgperm3')
		
		self.question = f"""The mass of a block of aluminum is {mass.g} g. a) What is its volume? b) What will be the tension in a string that suspends the block when the block is totally submerged in water? The density of aluminum is {density_aluminum.kgperm3} kg/m3."""
		
		volume = c.volume(mass.kg / density_aluminum.kgperm3)
		
		fb = c.force( volume.m3 * density_water.kgperm3 * gravity.mpers2)
		
		ft = c.force( mass.kg * gravity.mpers2 - fb.N )
		
		self.answer = f"""Volume of the block = {volume.cm3} cm3
Tension in the string = {ft.N} N"""

class schaums_13_15:
	def __init__(self,*args,**kwargs): 
		mass2 = c.mass(random_handler.main(73), 'g')
		mass = c.mass(mass2.g + random_handler.main(13), 'g')
		density_water = c.density(1000, 'kgperm3')
		self.question = f"""A piece of alloy has a measured mass of {mass.g} g in air and {mass2.g} g when immersed in water. Find its volume and density."""
		
		force_b = c.force(
		mass.kg * gravity.mpers2 - mass2.kg * gravity.mpers2
		)
		
		volume = c.volume( 
		force_b.N / (density_water.kgperm3 * gravity.mpers2)
		)
		
		density = c.density(
		mass.kg / volume.m3
		)
		
		self.answer = f"""Density of alloy = {density.kgperm3} kg/m3"""
		
class schaums_13_16:
	def __init__(self,*args,**kwargs): 
		
		density_aluminum = c.density(2700, 'kgperm3')
		mass2 = c.mass(random_handler.main(45), 'g')
		mass = c.mass(mass2.g + random_handler.main(22), 'g')
		
		self.question = f"""A solid aluminum cylinder with rho = {density_aluminum.kgperm3} kg/m3 has a measured mass of {mass.g} g in air and {mass2.g} g when immersed in turpentine. Determine the density of turpentine."""
		
		force_b = c.force(
		(mass.kg - mass2.kg) * gravity.mpers2
		)
		
		volume = c.volume( 
		mass.kg / density_aluminum.kgperm3
		)
		
		density_turpentine = c.density(
		(mass.kg - mass2.kg) / volume.m3 
		)
		
		self.answer = f"""Density of turpentine = {density_turpentine.kgperm3} kg/m3"""
		
class schaums_13_17:
	def __init__(self,*args,**kwargs): 
		mass3 = c.mass(random_handler.main(0.70), 'g')
		mass2 = c.mass(mass3.g + random_handler.main(0.8), 'g')
		mass = c.mass(mass2.g + random_handler.main(1), 'g')
		density_water = c.density(1000, 'kgperm3')
		self.question = f"""A glass stopper has a mass of {mass.g} g when measured in air, {mass2.g} g when measured in water and {mass3.g} g in sulfuric acid. What is the density of the acid? Its specific gravity?"""
		
		fb = c.force(
		(mass.kg - mass2.kg) * gravity.mpers2
		)
		
		volume = c.volume(
		fb.N / ( density_water.kgperm3 *  gravity.mpers2 )
		)
		
		fb2 = c.force(
		(mass.kg - mass3.kg) * gravity.mpers2
		)
		
		density_acid = c.density(
		(mass.kg - mass3.kg) / (volume.m3)
		)
		
		spgr = density_acid.kgperm3 / density_water.kgperm3
		
		self.answer = f"""Density of the acid = {density_acid.kgperm3} kg/m3
Specific gravity of the acid = {spgr}"""

class schaums_13_18:
	def __init__(self,*args,**kwargs): 
		density_ice = c.density(917, 'kgperm3')
		self.question = f"""The density of ice is {density_ice.kgperm3} kg/m3. What fraction of the volume of a piece of ice will be above water when floating in fresh water?"""
		frac = 1 - (density_ice.kgperm3 / 100)
		self.answer = f"""Fraction of volume that is above water = {frac}"""
		
class schaums_13_19:
	def __init__(self,*args,**kwargs): 
		regen = 1
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(60), 'kg')
			width = c.length(random_handler.main(0.80), 'm')
			length = c.length(width.m + random_handler.main(0.2), 'm')
			height = c.length(random_handler.main(0.5), 'm')
			depth = c.length(random_handler.main(30), 'cm')
			density_water = c.density(1000, 'kgperm3')
			
			self.question = f"""A {mass.kg}-kg rectangular box, open at the top, has base dimensions {length.m} m by {width.m} m and depth {height.m} m. a) How deep will it sink in fresh water? b) What weight Fwb of ballast will cause it to sink to a depth of {depth.cm} cm?"""
			
			equation = sympy.Eq(
			density_water.kgperm3 * gravity.mpers2 * length.m * width.m * x, 
			mass.kg * gravity.mpers2
			)
			
			height_sink_set = sympy.solveset(equation, x)
			height_sink_list = list(height_sink_set)
			height_sink = c.length(height_sink_list[0])
			
			if height_sink.cm < height.cm and height.cm > depth.cm:
				regen = 0
				
		equation = sympy.Eq(
		density_water.kgperm3 * gravity.mpers2 * length.m * width.m * depth.m,
		mass.kg * gravity.mpers2 + x
		)
		
		force_b_set = sympy.solveset(equation, x)
		force_b_list = list(force_b_set)
		force_b = c.force(force_b_list[0])
		
		mass_ballast = c.mass(
		force_b.N / gravity.mpers2
		)

		self.answer = f"""The box floats, and the required ballast mass to sink it to a depth of {depth.cm} cm is {mass_ballast.kg} kg"""
		
class schaums_13_20:
	def __init__(self,*args,**kwargs): 
		density_foam = c.density(0.58, 'gpercm3')
		floating = c.percentage(random_handler.main(20), 'percent')
		sinking = c.percentage(1 - floating.decimal, 'decimal')
		mass = c.mass(random_handler.main(80), 'kg')
		density_man = c.density(1.04, 'gpercm3')
		density_water = c.density(1000, 'kgperm3')
		
		self.question = f"""A plastic foam (rho = {density_foam.gpercm3} g/cm3) is to be used as a life preserver. What volume of foam must be used if it is to keep {floating.percent} percent (by volume) of a {mass.kg}-kg man above water in a lake? The average density of a man is {density_man.gpercm3} kg /m3"""
		
		volume_man = c.volume(mass.kg / density_man.kgperm3)
		#x is the volume of foam
		equation = sympy.Eq(
		density_water.kgperm3 * (sinking.decimal * volume_man.m3) *gravity.mpers2 + density_water.kgperm3 * x * gravity.mpers2,
		density_man.kgperm3 * volume_man.m3 * gravity.mpers2  + density_foam.kgperm3 * x * gravity.mpers2
		)
		
		volume_foam_set = sympy.solveset(equation, x)
		volume_foam_list = list(volume_foam_set)
		volume_foam = c.volume(volume_foam_list[0])
		
		self.answer = f"""Volume of the foam foam = {volume_foam.m3} m3"""
		
class schaums_13_21:
	def __init__(self,*args,**kwargs):
		weight = c.force(random_handler.main(2.30), 'N')
		weight2 = c.force(weight.N + random_handler.main(0.45), 'N')
		density_water = c.density(1000, 'kgperm3')
		self.question = f"""A partly filled beaker of water sits on a scale, and its weight is {weight.N} N. When a piece of metal suspended from a thread is totally immersed in the beaker (but not touching the bottom),  the scale reads {weight2.N} N. What is the volume of the metal?"""
		
		volume = c.volume(
		(weight2.N - weight.N) / (density_water.kgperm3 * gravity.mpers2)
		)
		
		self.answer = f"""Volume of the metal piece = {volume.cm3} cm3"""
		
class schaums_13_22:
	def __init__(self,*args,**kwargs): 
		
		regen = 1
		density_gold = c.density(19.3, 'gpercm3')
		density_water = c.density(1000, 'kgperm3')
		while regen:
			print(type(self))
			mass2 = c.mass(random_handler.main(36.22), 'g')
			mass = c.mass(mass2.g + random_handler.main(2.03), 'g')
			
			self.question = f"""A piece of pure gold (rho = {density_gold.gpercm3} g/cm3) is suspected to have a hollow center. It has a mass of {mass.g} g when measured in air and {mass2.g} g in water. What is the volume of the central hole in the gold?"""
			
			volume_gold = c.volume(
			mass.kg / density_gold.kgperm3
			)
			
			volume_water = c.volume(
			(mass.kg - mass2.kg) / density_water.kgperm3
			)
			
			volume_hole = c.volume(
			volume_gold.m3 - volume_water.m3
			)
			
			if volume_hole.m3 > 0:
				regen = 0
		
		self.answer = f"""Volume of hole = {volume_hole.cm3} cm3"""
		
class schaums_13_24:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(5), 'kg')
		load = c.mass(random_handler.main(30), 'kg')
		density_helium = c.density(0.178, 'kgperm3')
		density_air = c.density(1.29, 'kgperm3')
		
		self.question = f"""What must be the volume V of a {mass.kg}-kg balloon filled with helium (rho = {density_helium.kgperm3} kg/m3) if it is to lift a {load.kg}-kg load? Use (rho_air = {density_air.kgperm3} kg/m3)."""
		
		volume = c.volume(
		(mass.kg + load.kg) / (density_air.kgperm3 - density_helium.kgperm3)
		)
		
		self.answer = f"""Volume of balloon = {volume.m3} m3"""
		
#chapter 14 - hydrodynamics

class schaums_15_1:
	def __init__(self,*args,**kwargs): 
		
		l = random.randint(50,90)
		ti = random.randint(10,20)
		tf = random.randint(30,45)
		alpha = 1.7*10**-5
		dL = alpha*(l*c.CENTI)*(tf-ti)
		self.answer = """{dL:e} m""".format(dL = dL)
		
		solution = """
dL = (alpha) Lo dT
dL = (1.7E-5)({l:g}/100)({tf:g} - {ti:g})
dL = {dL:g}""".format(l=l,tf=tf,ti=ti,dL=dL)

		self.question = """A copper bar is {l:g}-cm long at {ti:g}°C. What is the increase in length when it is heated to {tf:g}°C? The linear expansion coefficient for copper is 1.7 x 10^(-5) C^-1.""".format(l=l,ti=ti,tf=tf)
			
class schaums_15_2:
	def __init__(self,*args,**kwargs): 
		dc = random.randint(80000,150000)/100000
		dh = dc - random.randint(20,100)/100000
		
		dT = (dc - dh)/(1.1E-5 * dh)
		ti = random.randint(20,40)
		self.answer = """{dT:g} °C""".format(dT = dT)
		solution = """
dL = d_cylinder - d_hole
dL = alpha L dT
dT = dL/(alpha L)
dT = (d_cylinder - d_hole)/(alpha L)
dT = ({dc:g} - {dh:g})/((1.1E-5)({dh:g}))
dT = {dT:g}""".format(dc=dc,dh=dh,dT=dT)
		self.question = """A cylinder of diameter {dc:g} cm at {ti:g} °C is to be slid into a hold in a steel plate. The hole has a diameter of {dh:g} cm at {ti:g} °C. To what temperature must the plate be heated? For steel, alpha = 1.1 x 10^-5 °C^-1.""".format(dc=dc,ti=ti,dh=dh)
		
class schaums_15_3:
	def __init__(self,*args,**kwargs): 
		ti = random.randint(15,35)
		tf = ti - random.randint(15,35)            
		dLL = (1.1E-5)*(tf - ti)*100          
		self.answer = """{dLL:g} %""".format(dLL=dLL)

		solution = """
dL/L = alpha (dT)
dL/L = (1.1E-5)({tf:g} - {ti:g})
dL/L = {dLL:g}%""".format(ti=ti,tf=tf,dLL=dLL)
		
		self.question = """A steel tape is calibrated at {ti:g}°C. On a cold day when the temperature is {tf:g}°C, what will be the percent error in the tape? alpha = 1.1 x 10^-5 °C^-1.""".format(ti=ti,tf=tf)
		
class schaums_15_4:
	def __init__(self,*args,**kwargs): 
		diff = random.randint(5,35)
		alphacu = 1.7E-5
		alphaal = 2.2E-5
		Lcu = (-alphaal*(diff*c.CENTI))/(alphacu - alphaal)
		self.answer = """{Lcu:g} m""".format(Lcu=Lcu)
		solution = """
dLcu = dLal
alphacu Lcu dT = alphaal Lal dT
alphacu Lcu dT = alphaal (Lcu - diff) dT
alphacu Lcu = alphaal*Lcu - alphaal*diff
Lcu (alphacu - alphaal) = -alphaal*diff
Lcu = (-alphaal*diff)/(alphacu - alphaal)
Lcu = (-({alphaal:g})({diff:g}/100))/({alphacu:g} - {alphaal:g})
Lcu = {Lcu:g}""".format(diff=diff,alphaal=alphaal,alphacu=alphacu,Lcu=Lcu)
		
		self.question = """A copper rod (alpha = 1.7E-5 °C-1) is {diff:g} cm longer than an aluminum rod (alpha = 2.20E-5 °C-1). How long should the copper rod be if the difference in their lengths is to be independent of the temperature?""".format(diff=diff)
		
class schaums_15_5:
	def __init__(self,*args,**kwargs): 
		
		ti = random.randint(10,30)
		alphast = 1.1E-5
		alphaal = 2.2E-5
		db = random.randint(8000,11000)/10000
		dh = db - random.randint(10,15)/10000
		
		dT = (dh-db)/(db*alphast - dh*alphaal)
		tf = ti + dT
		self.answer = """{tf:g} °C""".format(tf=tf)
		
		solution = """
Db + Db alphast dT = Dh + Dh alphaal dT
dT (Db alphast - Dh alphaal) = Dh - Db
dT = (Dh - Db)/(Db alphast - Dh alphaal)
dT = ({dh:g} - {db:g})/({db:g}*{alphast:g} - {dh:g}*{alphaal:g})
dT = {dT:g}
Tf = Ti + dT
Tf = {ti:g} + {dT:g}
Tf = {tf:g}""".format(dh=dh,db=db,alphaal=alphaal,alphast=alphast,dT=dT,ti=ti,tf=tf)

		self.question  = """At {ti:g}°C a steel ball (alpha = 1.1E-5 °C-1) has a diameter of {db:g} cm, while the diameter of a hold in an aluminum plate (alpha = 2.2E-5 °C-1) is {dh:g} cm. At what temperature (the same for both) will the ball just pass through the hole?""".format(dh=dh,db=db,ti=ti)
		
class schaums_15_6:
	def __init__(self,*args,**kwargs): 
		
		l = random.randint(50,100)
		ti = random.randint(5,15)
		tf = random.randint(25,40)
		
		alphacu = 1.7E-5
		alphast = 1.1E-5
		
		cms = ( l * ( 1 + alphacu*(tf-ti)))/(1 + alphast*(tf-ti))
		self.answer = """{cms:g} cm""".format(cms=cms)
		
		
		solution = """
copper length at {tf:g}°C:
Lcuf = Lcui(1 + alphacu dT)
centimeter marks on tape length at {tf:g}°C:
Lcm = (1)(1 + alphast dT)
number of "centimeters" read on the tape:
cms = (Lcui(1 + alphacu dT)) / (1 + alphast dT)
cms = ({l:g}*(1 + {alphacu:g}*({tf:g} - {ti:g})))/(1 + {alphast:g}*({tf:g} - {ti:g}))
cms = {cms:g}""".format(l=l,alphacu=alphacu,tf=tf,ti=ti,alphast=alphast,cms=cms)
		
		self.question = """A steel tape measures the length of a copper rod as {l:g} cm when both are at {ti:g}°C, the calibration temperature for the tape. What would the tape read for the length of the rod when both are at {tf:g}°C? alphast = 1.1E-5 °C-1, alphacu = 1.7E-5°C-1""".format(l=l,ti=ti,tf=tf)
		
class schaums_15_7:
	def __init__(self,*args,**kwargs): 
		alphaglass = 9E-6
		betaglass = 3*alphaglass
		betamercury = 182E-6
		v = random.randint(25,90)
		ti = random.randint(10,20)
		tf = ti + random.randint(10,20)
		
		vext = (betamercury - betaglass)*v*(tf -ti)
		
		self.answer = """{vext:g} cm^3""".format(vext=vext)
		
		solution = """
Vextra = dV_mercury - dV_glass
Vextra = (betamercury*Vo*dT) - (betaglass*Vo*dT)
Vextra = (betamercury - betaglass)*Vo*dT
Vextra = ({betamercury:g} - {betaglass:g})*{v:g}*({tf:g} - {ti:g})
Vextra = {vext:g}""".format(betamercury=betamercury,betaglass=betaglass,v=v,tf=tf,ti=ti,vext=vext)

		self.question = """A glass flask is filled "to the mark" with {v:g} cm^3 of mercury at {ti:g}°C. If the flask and its contents are heated to {tf:g}°C, how much mercury will be above the mark? alphaglass = 9E-6 °C-1, and betamercury = 182E-6 °C-1""".format(ti=ti,v=v,tf=tf)
		
		
class schaums_15_8:
	def __init__(self,*args,**kwargs): 
		tf = random.randint(25,80)
		beta = 1.82E-4
		rho0 = 13600
		dVv0 = beta*tf
		rho1 = rho0 * (1/(1+dVv0))
		self.answer = """{rho1:g} kg/m3""".format(rho1=rho1)
		solution = """
m = rho0 v0 = rho1 v1
rho1 = rho0*v0/v1
rho1 = rho0*v0/(v0 + dV)
rho1 = rho0 * (1/(1 + (dV/v0)))
dV/v0 = beta dT
dV/v0 = {beta:g}*{tf:g}
dV/v0 = {dVv0:g}
rho1 = {rho0:g}*(1/(1 + {dVv0:g}))
rho1 = {rho1:g}""".format(beta=beta,tf=tf,rho1=rho1,rho0=rho0,dVv0 = dVv0)

		self.question = """The density of mercury at exactly 0°C is 13600 kg/m3, and its volume expansion coefficient is 1.82E-4 °C-1. Calculate the density of mercury at {tf:g}°C""".format(tf=tf)
		
class schaums_15_9:
	def __init__(self,*args,**kwargs): 
		a = random.randint(10,30)/10
		l = random.randint(10,30)/10
		ti = random.randint(10,30)
		tf = ti - random.randint(10,30)
		E = 2E11
		alpha = 1.1E-5
		
		F = abs((tf-ti)*alpha*E*(a*c.MILLI**2))
		self.answer = """{F:g} N""".format(F=F)
		solution = """
dL = alpha L dT
stress = F/A = E strain = E dL/L
F/A = dT alpha E
F = dT alpha E A
F = abs(({tf:g} - {ti:g})*{alpha:g}*{E:g}*({a:g}/1000^2))
F = {F:g}""".format(tf=tf,ti=ti,alpha=alpha,E=E,a=a,F=F)

		self.question = """A steel wire of {a:g} mm^2 cross-section is held straight (but under no tension) by attaching it firmly to two points a distance {l:g} m apart at {ti:g}°C. If the temperature now decreases to {tf:g}°C, and if the two tie points remain fixed, what will be the tension in the wire? For steel, alphast = 1.1E-5 °C-1 and E = 2.0E11 Pa.""".format(a=a,l=l,ti=ti,tf=tf)
		
class schaums_15_10:
	def __init__(self,*args,**kwargs): 
		a = random.randint(20,60) 
		ti = random.randint(-20,-5)
		tf = ti + random.randint(20,40)
		alpha = 1.1E-5
		E = 2E11
		F = abs((tf-ti)*alpha*E*(a*c.CENTI**2))
		self.answer = """{F:g} N""".format(F=F)            
		solution = """
dL = alpha L dT
stress = F/A = E strain = E dL/L
F/A = dT alpha E
F = dT alpha E A
F = abs(({tf:g} - {ti:g})*{alpha:g}*{E:g}*({a:g}/100^2))
F = {F:g}""".format(tf=tf,ti=ti,alpha=alpha,E=E,a=a,F=F)
		
		self.question = """When a building is constructed at {ti:g}°C, a steel beam (cross-sectional area {a:g} cm^2) is put in place with its ends cemented in pillars. If the sealed ends cannot move, what will be the compressional force in the beam when the temperature if {tf:g}°C? For this kind of steel, alphast = 1.1E-5 °C-1 and E = 2E11 Pa.""".format(ti=ti,a=a,tf=tf)
		



class schaums_16_1:
	def __init__(self,*args,**kwargs): 
		v1 = random.randint(100,300)/10000
		p1 = 101*KILO
		t1 = 5
		
		p2 = p1 + random.randint(1,10)*KILO
		t2 = random.randint(10,50)
		v2 = (v1*p1*(t2+273))/(p2*(t1+273))
		self.answer = """{v2:g} m^3""".format(v2=v2)
		solution = """
p1v1/t1 = p2v2/t2
v2 = (v1*p1*t2)/(p2*t1)
v2 = ({v1:g}*{p1:g}*({t2:g} + 273))/({p2:g}*({t1:g} + 273))
v2 = {v2:g}""".format(v1=v1,v2=v2,t1=t1,t2=t2,p1=p1,p2=p2)
		
		
		self.question = """A mass of oxygen occupies {v1:g} m^3 at atmospheric pressure, 101 kPa, and {t1:g}°C. Determine its volume if its pressure is increased to {p2:g} kPa while its temperature is changed to {t2:g}°C.""".format(v1=v1,t1=t1/1000,p2=p2,t2=t2)
		
class schaums_16_2:
	def __init__(self,*args,**kwargs): 
		patm = 76
		p1g = random.randint(300,500)
		t1 = random.randint(2,15)
		t2 = t1 + random.randint(15,25)
		
		
		p1 = p1g + patm
		p2 = (p1*(t2+273))/((t1+273))
		p2g = p2 - patm
		self.answer = """{p2g:g} cmHg""".format(p2g=p2g)
		
		solution = """
p1/t1 = p2/t2
p2 = (p1*t2*)/(t1*)
p2 = ((patm + p1g)*t2*v1)/(t1*v2)
p2 = (({patm:g} + {p1g:g})*({t2:g} + 273)/(({t1:g} + 273))
p2 = {p2:g}
p2g = p2 - patm
p2g = {p2:g} - {patm:g}
p2g = {p2g:g}""".format(patm = patm, p1g=p1g,p2g=p2g,t2=t2,t1=t1,p2=p2)
		self.question = """On a day when atmospheric pressure is {patm:g} cmHg, the pressure gauge on a tank reads the pressure inside to be {p1g:g} cmHg. The gas in the tank has a temperature of {t1:g}°C. If the tank is heated to {t2:g}°C by the Sun, and if no gas exits from it, what will the pressure gauge read?""".format(patm=patm,p1g=p1g,t1=t1,t2=t2)
		
class schaums_16_3:
	def __init__(self,*args,**kwargs): 
		p1g = random.randint(300,310)
		p2g = p1g + random.randint(30,100)
		patm = 101
		t1 = random.randint(5,25)
		t2 = ((t1+273)*(p2g+patm))/(p1g+patm)
		t2c = t2 - 273
		
		self.answer = """{t2c:g} °C""".format(t2c=t2c) 
		solution ="""
p1/t1 = p2/t2
t2 = t1p2/p1
t2 = (({t1:g} + 273)*({p2g:g} + {patm:g}))/({p1g:g} + {patm:g})
t2 = {t2:g}
t2c = {t2:g} - 273
t2c = {t2c:g}""".format(t1=t1,p2g=p2g,patm=patm,p1g=p1g,t2=t2,t2c=t2c)
		self.question = """The gauge pressure in a car tire is {p1g:g} kPa when its temperature is {t1:g}°C. After running at high speed, the tire has heated up and its pressure is {p2g:g} kPa. What is then the temperature of the gas in the tire? Assume atmospheric pressure to be 101 kPa.""".format(p1g = p1g, t1=t1,p2g=p2g)
		
class schaums_16_4:
	def __init__(self,*args,**kwargs): 
		ratio = random.randint(2,9)
		patm = 740
		p1 = patm
		p2 = p1*ratio
		p2g = p2 - patm
		p2gkpa = p2g * 101/760
		self.answer = """{p2gkpa:g} kPa""".format(p2gkpa=p2gkpa)
		solution = """
p1v1 = p2v2
p2 = p1v1/v2
p2 = {p1:g}*{ratio:g}
p2g = p2 - patm
p2g = {p2:g} - {patm:g}
p2g = {p2g:g}
conversion:
kPa = mmHg * 101/760
p2g = {p2gkpa:g}""".format(p1=p1,ratio=ratio,p2=p2,patm=patm,p2g=p2g,p2gkpa=p2gkpa)
		
		self.question = """Gas at room temperature and pressure is confined to a cylinder by a piston. The piston is now pushed in so as to reduce the volume of 1/{ratio:g} of its original value. After the gas temperature has returned to room temperature, what is the gauge pressure of the gas in kPa? Local atmospheric pressure is {patm:g} mm of mercury.""".format(ratio=ratio,patm=patm)
		
class schaums_16_5:
	def __init__(self,*args,**kwargs): 
		v1 = random.randint(50,150)/100
		v2 = v1 - random.randint(20,60)/100
		p1 = random.randint(50,150)/100
		t1 = random.randint(-40,-10)
		t2 = random.randint(20,60)
		p2 = (p1*v1*(t2+273))/(v2*(t1+273))
		self.answer = """{p2:g} atm""".format(p2=p2)
		solution = """
p1v1/t1 = p2v2/t2 
p2 = p1v1t2/v2t1
p2 = ({p1:g}*{v1:g}*({t2:g} + 273)/({v2:g}*({t1:g} + 273))
p2 = {p2:g}""".format(p2=p2,v1=v1,t2=t2,v2=v2,t1=t1,p1=p1)
		
		self.question = """An ideal gas has a volume of {v1:g} liter at {p1:g} atm and {t1:g} °C. To how many atmospheres pressure must it be subjected to be compressed to {v2:g} liter when the temperature is {t2:g}°C?""".format(v1=v1,p1=p1,t1=t1,v2=v2,t2=t2)
		
class schaums_16_6:
	def __init__(self,*args,**kwargs): 
		v1 = random.randint(300,400)
		t1 = random.randint(10,20)
		p1 = random.randint(100,200)
		t2 = t1 - random.randint(10,50)
		p2 = p1 + random.randint(100,200)
		
		v2 = (v1*p1*(t2+273))/(p2*(t1+273))
		self.answer = """{v2:g} mL""".format(v2=v2)
		
		solution = """
p1v1/t1 = p2v2/t2
v2 = v1p1t2/p2t1
v2 = ({v1:g}*{p1:g}*({t2:g} + 273))/({p2:g}*({t1:g} + 273))
v2 = {v2:g}""".format(v1=v1,p1=p1,t2=t2,p2=p2,t1=t1,v2=v2)
		self.question = """A certain mass of hydrogen gas occupies {v1:g} mL at {t1:g} °C and {p1:g} kPa. Find its volume at {t2:g}°C and {p2:g} kPa.""".format(v1=v1,t1=t1,p1=p1,t2=t2,p2=p2)
		
class schaums_16_7:
	def __init__(self,*args,**kwargs): 
		t1 = 0
		p1 = 760
		rho1 = 1.25
		
		t2 = random.randint(20,50)
		p2 = random.randint(720,780)
		rho2 = (rho1*p2*(t1+273))/(p1*(t2+273))
		self.answer = """{rho2:g} kg/m^3""".format(rho2=rho2)
		
		solution = """
p1v1/t1 = p2v2/t2
p1/(rho1 t1) = p2/(rho2 t2)
rho2 = (rho1p2t1)/(p1t2)
rho2 = ({rho1:g}*{p2:g}*({t1:g} +273))/({p1:g}*({t2:g} +273))
rho2 = {rho2:g}""".format(rho1=rho1,p2=p2,t1=t1,p1=p1,t2=t2,rho2=rho2)

		self.question = """The density of nitrogen is {rho1:g} kg/m^3 at S.T.P. Determine the density of nitrogen at {t2:g}°C and {p2:g} mm of mercury.""".format(rho1=rho1,t2=t2,p2=p2)
		
class schaums_16_8:
	def __init__(self,*args,**kwargs): 
		v1 = random.randint(1,5)
		t1 = random.randint(10,30)
		p1g = random.randint(10,30)
		patm = 1
		
		p1 = (p1g + patm)*10**5
		M = 32/1000
		R = UNIVERSALGASCONSTANT
		
		m = (p1*v1*LITERS_M3*M)/(R*(t1+273))
		self.answer = """{m:g} kg""".format(m=m)
		
		solution = """
p = patm + pg
pV = nRT
pV = (m/M)*RT
m = pVM / RT
m = (patm + pg)VM / RT
m = (({patm:g} + {p1g:g})*{v1:g}*{M:g}) / ({R:g}*({t1:g}))
m = {m:g}""".format(patm = patm, p1g = p1g, v1 = v1/1000, M = M/1000, R = R, t1 = t1+273, m = m)
		
		self.question = """A {v1:g}-liter tank contains oxygen at {t1:g}°C and a gauge pressure of {p1g:g} x 10^5 Pa. What mass of oxygen is in the tank? The molecular mass of oxygen is 32 kg/kmol. Assume atmospheric pressure to be 1 x 10^5 Pa.""".format(v1=v1,t1=t1,p1g=p1g)
		
		
class schaums_16_9:
	def __init__(self,*args,**kwargs): 
		#STP 
		t1 = 0
		p1 = 101325
		m = random.randint(1,9)
		M = 32
		
		v = (m*UNIVERSALGASCONSTANT*(t1+273))/(p1*M*KGKMOL)
		self.answer = """{v:g} m3""".format(v=v)
		
		solution = """
pV = (m/M)RT
V = (mRT)/(pM)
V = ({m:g}*{R:g}*{t1:g})/({p1:g}*{M:g})
V = {v:g}""".format(m=m,R=UNIVERSALGASCONSTANT,t1=t1+273,p1=p1,M=M*KGKMOL,v=v)
		self.question = """Determine the volume occupied by {m:g}g of oxygen (M = 32 kg/kmol) at STP.""".format(m=m)
		
		
class schaums_16_10:
	def __init__(self,*args,**kwargs): 
		m = random.randint(1,9)
		v = random.randint(20,40)
		t = random.randint(10,30)
		M = 28
		p = (m*MILLIGRAMS*UNIVERSALGASCONSTANT*(t+273))/(M*KGKMOL*v*MILLILITERS_M3)
		p_atm = p * (1/101325)
		self.answer = """{p_atm:g} atm""".format(p_atm=p_atm)
		solution = """
p = (mRT) / (MV)
p = ({m:g}*{R:g}*{t:g})/({M:g}*{v:g})
p = {p:g} Pa
p_atm = p_Pa * (1/101325)
p_atm = {p:g} * (1/101325)
p_atm = {p_atm:g}""".format(m=m*MILLIGRAMS, R = UNIVERSALGASCONSTANT, t=t+273, M= M*KGKMOL, v = v*MILLILITERS_M3, p=p, p_atm = p_atm)

		self.question = """A {m:g}-mg droplet of liquid nitrogen is present in a {v:g} mL tube as it is sealed off at a very low temperature. What will be the nitrogen pressure in the tube when it is warmed to {t:g}°C? Express your answer in atmospheres ( M for nitrogen is 28 kg/kmol)""".format(v=v,m=m,t=t)
		
class schaums_16_11:
	def __init__(self,*args,**kwargs): 
		v = random.randint(500,600)
		t = random.randint(10,30)
		p = random.randint(3,7)
		M = 32
		m = ((p*ATM_PA)*(v*LITERS_M3)*(M*KGKMOL))/(UNIVERSALGASCONSTANT*(t+273))
		self.answer = """{m:g} kg""".format(m=m)
		solution = """
pV = (m/M)RT
m = pVM / RT
m = ({p:g}*{v:g}*{M:g})/({R:g}*{t:g})
m = {m:g} kg""".format(p=p*ATM_PA,v=v*LITERS_M3,M=M*KGKMOL,R=UNIVERSALGASCONSTANT,t=t+273,m=m)
		self.question = """A tank of volume {v:g} liters contains oxygen at {t:g}°C at {p:g} atm pressure. Calculate the mass of the oxygen in the tank. M = 32 kg/kmol for oxygen.""".format(v=v,t=t,p=p)
		
class schaums_16_12:
	def __init__(self,*args,**kwargs): 
		t = random.randint(8,28)
		p = random.randint(750,780)
		v = random.randint(100,200)/100
		m = random.randint(200,300)/100
		
		M = ((m*GRAMS)*(UNIVERSALGASCONSTANT)*(t + 273))/((p*MMHG_PA)*(v*LITERS_M3))
		self.answer = """{M:g} kg/kmol""".format(M = M*KGMOL_KGKMOL)
		solution = """
pV = (m/M)RT
M = (mRT)/(PV)
M = ({m:g}*{R:g}*{t:g})/({p:g}*{v:g})
M = {M:g} kg/mol
M_kgkmol = {M2:g} kg/kmol""".format(m=m*GRAMS, R = UNIVERSALGASCONSTANT, t = t + 273, p = p*MMHG_PA, v = v*LITERS_M3, M = M, M2 = M*KGMOL_KGKMOL)
		self.question = """At {t:g}°C and {p:g} mmHg, {v:g} liters of an ideal gas has a mass of {m:g}g. Compute the molecular mass of the gas.""".format(t=t,p=p,v=v,m=m)
		
class schaums_16_13:
	def __init__(self,*args,**kwargs): 
		
		m = random.randint(2,9)
		t = random.randint(10,30)
		p = random.randint(300,400)
		M = 4
		v = ((m*GRAMS)*(UNIVERSALGASCONSTANT)*(t+273))/((M*KGKMOL)*(p*MMHG_PA))
		self.answer = """{v:g} liters""".format(v = v*M3_LITERS)
		solution = """
pv = (m/M)RT
v = mRT / MP"""

		self.question = """Compute the volume of {m:g}g of helium ( M = 4.0 kg/kmol ) at {t:g}°C and {p:g} mmHg.""".format(m=m,t=t,p=p)
		
		
class schaums_16_14:
	def __init__(self,*args,**kwargs): 
		M = 16
		t = random.randint(10,30)
		p = random.randint(2,7)
		rho = ((p*ATM_PA)*(M*KGKMOL))/((UNIVERSALGASCONSTANT)*(t+273))
		self.answer = """{rho:g} kg/m^3""".format(rho=rho)
		solution = """
pV = (m/M)RT
rho = m/V = pM / RT"""
		self.question = """Find the density of methane ( M = 16 kg/kmol ) at {t:g}°C and {p:g} atm.""".format(t=t,p=p)
		
class schaums_16_15:
	def __init__(self,*args,**kwargs): 
		v1 = random.randint(10,30)/10
		h = random.randint(10,20)
		rho = DENSITY_WATER
		g = 9.81
		patm = STP_PRESSURE
		p2 = patm
		p1 = rho*g*h + patm
		v2 = (v1*p1) / (p2)
		self.answer = """{v2:g} mm^3""".format(v2=v2)
		solution = """
p = po + rho g h
p1 v1 = p2 v2"""
		self.question = """A fish emits a {v1:g} mm^3 bubble at a depth of {h:g} m in a lake. Find the volume of the bubble as it reaches the surface. Assume its temperature does not change.""".format(v1=v1,h=h)
		
		
class schaums_16_16:
	def __init__(self,*args,**kwargs): 
		ratio = random.randint(2,4)
		l = random.randint(10,20)
		p1 = STP_PRESSURE
		g = 9.81
		patm = STP_PRESSURE
		rho = DENSITY_WATER
		v1v2_ratio = 1/(1-(1/ratio))
		p2 = p1*(v1v2_ratio)
		h = (p2 - patm) / (rho*g)
		self.answer = """{h:g} m""".format(h=h)
		solution = """
p2 = po + rho g h
p1 v1 = p2 v2"""
		self.question = """A {l:g} cm long test tube of uniform bore is lowered, open end down, into a fresh water lake. How far below the surface of the lake must the water level be in the tube if 1/{ratio:g} of the tube is to be filled with water?""".format(l=l,ratio=ratio)
		
		
class schaums_16_17:
	def __init__(self,*args,**kwargs): 
		mn = random.randint(10,20)
		pn = random.randint(30,60)/10
		ph = pn - random.randint(10,20)/10
		Mn = 28 
		Mh = 2
		
		nn = mn / Mn
		nh = nn * (ph/pn)
		mh = nh * Mh
		self.answer = """{mh:g} kg""".format(mh=mh)
		solution = """
pn v = nn RT , ph v = nh RT
n = m/M"""
		self.question = """A tank contains {mn:g} kg of N2 gas ( M = 28 kg/kmol )  at a pressure of {pn:g} atm. How much H2 has ( M = 2 kg/kmol ) at {ph:g} atm would the same tank contain?""".format(mn=mn,pn=pn,ph=ph)
		
class schaums_16_18:
	def __init__(self,*args,**kwargs): 
		t = random.randint(10,30)
		ph = random.randint(100,350)
		pc = random.randint(100,350)
		pme = random.randint(100,350)
		pet = random.randint(100,350)
		Mh = 2
		Mco2 = 44
		Mch4 = 16
		Mc2h4 = 30
		
		p = ph + pc + pme + pet
		mh = (Mh*ph) #V/RT
		m = Mh*ph + Mco2*pc + Mch4*pme + Mc2h4*pet #V/RT
		m_frac = mh/m
		self.answer = """{m_frac:g}""".format(m_frac=m_frac)
		solution = """
p = p1 + p2 + p3 + ... - daltons law of partial pressures
m = M n
n = PV / RT
m = M (PV / RT)
m_frac = m / m_total"""
		self.question = """In a gaseous mixture at {t:g}°C the partial pressures of the components are as follows: hydrogen, {ph:g}mmHg; carbon dioxide, {pc:g}mmHg; methane, {pme:g}mmHg; ethylene, {pet:g}mmHg. What is the total pressure of the mixture? What is the mass fraction of hydrogen? (MH = 2 kg/kmol, MCO2 = 44 kg/kmol, MCH4 = 16 kg/kmol, MC2H4 = 30 kg/kmol )""".format(t=t,ph=ph,pc=pc,pme=pme,pet=pet)
		
		
class schaums_17_1:
	def __init__(self,*args,**kwargs): 
		
		self.answer = """4.7 x 10^-26 kg"""
		solution = """
mo = M / Na"""
		self.question = """Ordinary nitrogen gas consists of molecules of N2. Find the mass of one such molecule. The molecular mass is 28 kg/kmol."""
		
class schaums_17_2:
	def __init__(self,*args,**kwargs): 
		m = random.randint(1,9)
		M = 4
		
		n = (m*GRAMS) / (M*KGKMOL_KGMOL)
		N = n * AVOGADROS_NUMBER
		self.answer = """{N:g} atoms""".format(N = N)
		solution = """
n = m / M
N = n * Na"""
		self.question = """Helium gas consists of separate He atoms rather than molecules. How many helium atoms are there in {m:g}g of helium? M = 4.0 kg/kmol for He.""".format(m=m)
		
class schaums_17_3:
	def __init__(self,*args,**kwargs): 
		r = random.randint(20,80)
		rho = 13600
		M = 202
		V = (4/3) * math.pi * (r*MILLI)**3
		m = rho * V
		mo = ( M*KGKMOL_KGMOL)/AVOGADROS_NUMBER
		N = m / mo
		self.answer = """{N:g} atoms""".format(N = N)
		solution = """
V = (4/3) pi r^3
m = rho V
mo = M / Na
N = m / mo"""
		self.question = """A droplet of mercury has a radius of {r:g} mm. How many mercury atoms are in the droplet? For Hg, M = 202 kg/kmol and rho = 13600 kg/m^3""".format(r=r)
		
class schaums_17_4:
	def __init__(self,*args,**kwargs): 
		v = random.randint(10,100)
		rho = 0.88
		M = 78
		m = (rho*GCM3_KGM3)*(v*MILLILITERS_M3)
		mo = (M*KGKMOL_KGMOL)/AVOGADROS_NUMBER
		N = m / mo
		self.answer = """{N:g} atoms""".format(N=N)
		solution = """
rho = 0.88
M = 78
m = (rho*GCM3_KGM3)(v*MILLILITERS_M3)
mo = (M*KGKMOL_KGMOL)/AVOGADROS_NUMBER
N = m / mo"""
		self.question = """How many molecules are there in {v:g} mL of benzene? For benzene, rho = 0.88 g/cm^3 and M = 78 kg/kmol.""".format(v=v)
		
class schaums_17_5:
	def __init__(self,*args,**kwargs): 
		t = random.randint(-10,10)
		M = 28
		mo = (M*KGKMOL_KGMOL) / AVOGADROS_NUMBER
		vrms = math.sqrt((3*BOLTZMANNS_CONSTANT*(t+273))/mo)
		self.answer = """{v:g} km/s""".format(v = vrms/1000)
		solution = """
M = 28
mo = (M*KGKMOL_KGMOL) / AVOGADROS_NUMBER
vrms = math.sqrt((3*BOLTZMANNS_CONSTANT*(t+273))/mo)"""
		self.question = """Find the RMS speed of a nitrogen molecule ( M = 28 kg/kmol ) in air at {t:g}°C""".format(t=t)
		
		
class schaums_17_6:
	def __init__(self,*args,**kwargs): 
		
		t = random.randint(-10,10)
		M = 28
		g = 9.81
		mo = (M*KGKMOL_KGMOL) / AVOGADROS_NUMBER
		h = (1/mo)*((3*BOLTZMANNS_CONSTANT*(t+273))/(2*g))
		self.answer = """{h:g} km""".format(h = h/1000)
		solution = """            
M = 28
g = 9.81
mo = (M*KGKMOL_KGMOL) / AVOGADROS_NUMBER
KE = PE
(3/2) BOLTZMANNS_CONSTANT T = mgh
h = (1/mo)*((3*BOLTZMANNS_CONSTANT*(t+273))/(2*g))"""

		self.question = """A gas molecule at the surface of the Earth happens to have the RMS speed for that has at {t:g}°C. If it were to go straight up without colliding with other molecules, how high would it rise? ( M = 28 kg/kmol )""".format(t=t)
		
class schaums_17_7:
	def __init__(self,*args,**kwargs): 
		
		rho = 1.29
		patm = 100
		vrms = math.sqrt((3*patm*KILO)/(rho))
		self.answer = """{v:g} m/s""".format(v=vrms)
		solution = """
P = (1/3) rho vrms^2
vrms = sqrt((3 P) / rho )"""

		self.question = """Air at room temperature has a density of about 1.29 kg/m^3. Assuming it to be entirely one gas, find vrms for its molecules"""
		
class schaums_17_8:
	def __init__(self,*args,**kwargs): 
		
		t = random.randint(-20,20)
		KE_total = AVOGADROS_NUMBER * (1/1000) * (3/2) * BOLTZMANNS_CONSTANT * (t + 273)
		self.answer = """{KE:g} J""".format(KE = KE_total)
		solution = """
KE_total = AVOGADROS_NUMBER * (1/1000) * (3/2) * BOLTZMANNS_CONSTANT * (t + 273)"""
		self.question = """Find the translational kinetic energy of one gram mole of any ideal gas at {t:g}°C""".format(t=t)
		
class schaums_17_9:
	def __init__(self,*args,**kwargs): 
		t = 3.5
		M = 1
		mo = (M*KGKMOL_KGMOL) / AVOGADROS_NUMBER
		vrms = math.sqrt((3*BOLTZMANNS_CONSTANT*t)/(mo))
		rho = 10**6 / AVOGADROS_NUMBER
		p = (1/3) *rho*vrms**2
		self.answer = """{v:g} km/s, {p:g} Pa""".format(v = vrms/1000, p = p)
		
		self.question = """There is about one hydrogen atom per cm^3 in outer space, where the temperature (in the shade) is about 3.5 K. Find the rms speed of these atoms and the pressure they exert. ( M = 1 kg/kmol )"""
		
class schaums_17_10:
	def __init__(self,*args,**kwargs): 
		
		MH = 2
		MN = 28
		KE_ratio = 1
		vrms_ratio = math.sqrt(MN / MH)
		self.answer = """{KE:g}, {v:g}""".format(KE = KE_ratio,v = vrms_ratio)
		solution = """
KE = (3/2) kb T,  which is independent of M. so KE_ratio = 1
vrms = sqrt(3kbT / mo)
mo = M / Na""" 
		self.question = """Find the following ratios for hydrogen ( M = 2 kg/kmol ) and nitrogen ( M = 28 kg/kmol ) gases at the same temperature: KEH / KEN and vrmsH / vrmsN."""
		
class schaums_17_11:
	def __init__(self,*args,**kwargs): 
		
		r = random.randint(1,9)
		V = 22.4
		N = AVOGADROS_NUMBER
		
		mfp = 1 / ( 4*math.pi*math.sqrt(2)*(r*10**(-10))**2*(N/(V*LITERS_M3)))
		self.answer = """{mfp:g} m""".format(mfp = mfp)
		solution = """
V = 22.4
N = AVOGADROS_NUMBER

mfp = 1 / ( 4*math.pi*math.sqrt(2)*(r*10**(-10))**2*(N/(V*LITERS_M3)))"""

		self.question = """Certain ideal gas molecules behave like spheres of radius {r:g} x 10^(-10) m. Find the mean free path of these molecules at STP.""".format(r=r)
		
		
class schaums_17_12:
	def __init__(self,*args,**kwargs): 
		mfp = random.randint(30,80)
		r = random.randint(1,9)
		t = random.randint(10,30)
		NoverV = 1/(math.pi*4*math.sqrt(2)*(r*10**(-10))**2*(mfp*CENTI))
		p = NoverV*BOLTZMANNS_CONSTANT*(t+273)
		self.answer = """{p:g} mPa""".format(p = p*1000)
		solution = """
(N/V) = 1 / (4*pi*sqrt(2)*r^2*mfp)
pV = Nkb T
p = (N/V) kb T"""
		self.question = """At what pressure will the mean free path be {mfp:g} cm for spherical molecules of radius {r:g} x 10^(-10) m? Assume an ideal gas at {t:g}°C""".format(mfp = mfp, r=r, t=t)
		
		
class schaums_18_1:
	def __init__(self,*args,**kwargs): 
		
		v = random.randint(10,30)
		t1 = random.randint(10,30)
		t2 = t1 + random.randint(10,20)
		dT = t2 - t1
		c = SPECIFIC_HEAT_WATER_JKGK
		m = v*GRAMS_KG
		dQ = m * c * dT
		self.answer = """{dQ:g} kJ, -{dQ:g} kJ""".format(dQ = dQ/1000)
		solution = """
Q = mcdT 
cw = 4186 J/kgk"""
		self.question = """How much heat is required to raise the temperature of {v:g} mL of water from {t1:g}°C to {t2:g}°C? How much heat is lost by the water as it cools back down to {t1:g}°C?""".format(v = v, t1 = t1, t2 = t2)
		
class schaums_18_2:
	def __init__(self,*args,**kwargs): 
		
		m = random.randint(10,40) #grams
		t1 = random.randint(80,120) #degC
		t2 = t1 - random.randint(40,70) #degC
		dT = t2 - t1
		c = 880
		dQ = m*GRAMS_KG * c * dT
		self.answer = """{dQ:g} J""".format(dQ = dQ)
		solution = """
dQ = mc dT
c = 880 J/kgK"""
		self.question = """How much heat does {m:g} g of aluminum give off as it cools from {t1:g}°C to {t2:g}°C? For aluminum, c = 880 J/kgK.""".format(m=m, t1 =t1, t2 = t2)
		
class schaums_18_3:
	def __init__(self,*args,**kwargs): 
		cal = 0.21
		ccu = 0.093
		dTal = random.randint(40,70)
		dTcu = (cal/ccu)*dTal
		self.answer = """{dTcu:g}°C""".format(dTcu = dTcu)
		solution = """
dQal = dQcu
mcal dT = m ccu dT
dTcu = (cal/ccu) dTal"""
		self.question = """A certain amount of heat is added to a mass of aluminum ( c = 0.21 cal/gC ), and its temperature is raised {dT:g}°C. Suppose that the same amount of heat is added to the same mass of copper ( c = 0.093 cal/gC ). How much the temperature of the copper rise?""".format(dT = dTal)
		
class schaums_18_4:
	def __init__(self,*args,**kwargs): 
		
		t1 = random.randint ( 10,30)
		t2 = t1 + random.randint(60,80)
		tf = (t1 + t2)/2
		self.answer = """{tf:g} °C""".format(tf=tf)
		solution = """dQ = mcdT"""
		self.question = """Two identical metal plates ( mass = m, specific heat = c ) have different  temperatures; one is at {t1:g}°C and the other is at {t2:g}°C. They are placed in good thermal contact. What is their final temperature?""".format(t1=t1,t2=t2)
		
class schaums_18_5:
	def __init__(self,*args,**kwargs): 
		
		mcoffee = random.randint(200,300)
		tcoffee = random.randint(80,100)
		mmilk = random.randint(10,30)
		tmilk = random.randint(0,10)
		c = SPECIFIC_HEAT_WATER_CALGC
		tfinal_set = sympy.solveset(mcoffee * (x - tcoffee) + mmilk*(x - tmilk),x)
		tfinal_list = list(tfinal_set)
		tfinal = tfinal_list[0]
		self.answer = """{tf:s}°C""".format(tf = str(tfinal))
		solution = """
dQ1 = dQ2
dQ = mc dT
c = c_water = c_milk = c_coffee = 4186 J/kgK"""

		self.question = """A thermos bottle contains {mcoffee:g}g of coffee at {tcoffee:g}°C. To this is added {mmilk:g}g of milk at {tmilk:g}°C. After equilibrium is established, what is the temperature of the liquid? Assume no heat loss to the thermos bottle.""".format(mcoffee = mcoffee, tcoffee = tcoffee, mmilk = mmilk, tmilk = tmilk)
		
		
class schaums_18_6:
	def __init__(self,*args,**kwargs): 
		mwater = random.randint(100,200)
		twater = random.randint(1,10)
		mmetal = random.randint(70,110)
		tmetal = random.randint(80,120)
		tf = random.randint(twater,tmetal)
		
		cwater = SPECIFIC_HEAT_WATER_CALGC
		cmetal = -(cwater*mwater*(tf - twater))/(mmetal*(tf - tmetal))
		self.answer = """{cmetal:g} cal/gC""".format(cmetal = cmetal)
		solution = """
dQwater + dQmetal = 0
dQ = mc dT"""
		self.question = """A thermos bottle contains {mwater:g}g of water at {twater:g}°C. Into this is placed {mmetal:g}g of metal at {tmetal:g}°C. After equilibrium is established, the temperature of the water and the metal is {tf:g}°C. What is the specific heat of the metal? Assume no heat loss to the thermos bottle.""".format(mwater=mwater,twater=twater,mmetal=mmetal,tmetal=tmetal,tf = tf)
		
class schaums_18_7:
	def __init__(self,*args,**kwargs): 
		mcu = random_handler.ten(200)
		moil = random_handler.ten(150)
		toil = random_handler.ten(20)
		tcu = toil
		mal = random_handler.ten(80)
		tal = random_handler.ten(300)
		ccu = 0.093
		cal = 0.21
		coil = 0.37
	   
		tf = sympy.solveset(sympy.Eq(cal*mal*(x - tal) + ccu*mcu*(x-tcu) + coil*moil*(x - toil),0) , x).args[0]
		tf = sympy.N(tf)
		self.answer = """{tf:g}°C""".format(tf = tf)
		solution = """sum(dQn) = 0
		dQ = mc dT"""
		
		self.question = """A {mcu:g}g copper calorimeter can contains {moil:g}g of oil at {toil:g}°C. To the oil is added {mal:g}g of aluminum at {tal:g}°C. What will be the temperature of the system after equilibrium is established? ccu = 0.093 cal/gC, cal = 0.21 cal/gC, and coil = 0.37 cal/gC""".format(mcu = mcu, moil = moil, toil=toil, mal = mal, tal=tal)
		
class schaums_18_8:
	def __init__(self,*args,**kwargs): 
		ccu = 0.093
		cwater = SPECIFIC_HEAT_WATER_CALGC
		mc = random.randint(1,9)
		mcal = random_handler.hundred(1500)
		mw = random_handler.hundred(2000)
		t1 = random_handler.ten(20)
		t2 = t1 + random.randint(5,20)
		dT = t2 - t1
		Qcarbon = sympy.solveset(x + ccu*mcal*dT + cwater*mw*dT,x).args[0]
		Qcarbon = sympy.N(Qcarbon)
		QcarbonPerGram = -Qcarbon/mc
		self.answer = """{q:g} cal/g""".format(q = QcarbonPerGram)
		
		self.question = """Exactly {mc:g}g of carbon was burned to CO2 in a copper calorimeter. The mass of the calorimeter is {mcal:g}g, and there is {mw:g}g of water in the calorimeter. The initial temperature was {t1:g}°C, and the final temperature is {t2:g}°C. Calculate the heat given off per gram of carbon. ccu = 0.093 cal/gC. Neglect the small heat capacity of the carbon and carbon dioxide.""".format(mc=mc,mcal=mcal,mw=mw,t1=t1,t2=t2)
		
class schaums_18_9:
	def __init__(self,*args,**kwargs): 
		retry = True
		while retry == True:
			print(type(self))
			mwater = random_handler.ten(300)
			mice = random_handler.ten(150)
			twater = random_handler.ten(50)
			Hice = LATENT_HEAT_FUSION_WATER_CALG
			cwater = SPECIFIC_HEAT_WATER_CALGC
			tf = sympy.solveset(mice*Hice + cwater*mice*(x - 0) + cwater*mwater*(x - twater),x).args[0]
			tf = sympy.N(tf)
			if tf > 0:
				retry = False
		
		
		self.answer = """{tf:g} °C""".format(tf = tf)
		solution = """dQ = mc dT, dQ = m H"""
		self.question = """Determine the temperature Tf that results when {mice:g}g of ice at 0°C is mixed with {mwater:g}g of water at {twater:g}°C.""".format(mice = mice, mwater= mwater, twater = twater)
		
class schaums_18_10:
	def __init__(self,*args,**kwargs): 
		tf = random_handler.ten(20)
		msteam = random_handler.ten(20)
		Lv = LATENT_HEAT_VAPORIZATION_WATER_CALG
		cw = SPECIFIC_HEAT_WATER_CALGC
		dQ = msteam*(-Lv) + cw*msteam*(tf - 100)
		self.answer = """{dQ:g} cal""".format(dQ = dQ)
		
		self.question = """How much heat is given up when {msteam:g}g of steam at 100°C is condensed and cooled to {tf:g}°C?""".format(msteam = msteam, tf = tf)
		
class schaums_18_11:
	def __init__(self,*args,**kwargs): 
		
		mal = random_handler.ten(20)
		cal = 0.21
		Lfice = LATENT_HEAT_FUSION_WATER_CALG
		ti = random_handler.ten(90)
		
		retry = True
		while retry: 
			print(type(self))
			mice = sympy.solveset(mal*cal*(0 - ti) + Lfice*x,x).args[0]
			mice = sympy.N(mice)
			
			if mice > 0:
				retry = False
		
		self.answer = """{mice:g} g""".format(mice = mice)
		
		self.question = """A {mal:g}g piece of aluminum (c = 0.21 cal/gC ) at {ti:g}°C is dropped into a cavity in a large block of ice at 0°C. How much ice does the aluminum melt?""".format(mal = mal, ti = ti)
		
class schaums_18_12:
	def __init__(self,*args,**kwargs): 
		
		mcal = random_handler.ten(40)
		mwater1 = random_handler.ten(200)
		mice = random_handler.ten(50)
		mwater2 = random_handler.ten(30)
		twater2 = random.randint(80,95)
		cwater = SPECIFIC_HEAT_WATER_CALGC
		Lice = LATENT_HEAT_FUSION_ICE_CALG
		#assuming that the final temperature is greater than zero
		
		tf = sympy.solveset(mwater2*cwater*(x - twater2) + mice*Lice + (mwater1 + mice)*cwater*x + mcal*cwater*x,x).args[0]
		tf = sympy.N(tf)
		
		#if tf is found to be less than zero, then this means not all ice is melted.
		if tf < 0:
			tf = 0
			mice_melt = (mwater2*cwater*twater2)/Lice
			self.answer = """{tf:g}°C, {m:g} g melted ice""".format(tf = tf, m = mice_melt)
			
		else:
			self.answer = """{tf:g}°C""".format(tf=tf)
		
		
		self.question = """In a calorimeter can (which behaves thermally as if it were equivalent to {mcal:g}g of water) are {mwater1:g}g of water and {mice:g}g of ice, all at exactly 0°C. Into this is poured {mwater2:g}g of water at {twater2:g}°C. What will be the final condition of the system?""".format(mwater1 = mwater1, mcal=mcal,mice=mice,mwater2=mwater2, twater2 = twater2)
		
class schaums_18_13:
	def __init__(self,*args,**kwargs): 
		solution = """P = Q/t, dQ = m Lv"""
		
		P = random_handler.hundred(900)
		t = random.randint(1,9)
		Lv = LATENT_HEAT_VAPORIZATION_WATER_JKG
		
		m = sympy.solveset(x*Lv - (P*t*MIN_SEC), x).args[0]
		m = sympy.N(m)
		self.answer = """{m:g} g""".format(m=m*1000)
		
		self.question = """An electric heater that produces {P:g}W of power is used to vaporize water. How much water at 100°C can be changed to steam in {t:g} minutes by the heater? For water at 100°C, Lv = 2.26 x 10^6 J/kgK.""".format(P = P, t=t)
		
class schaums_18_14:
	def __init__(self,*args,**kwargs): 
		solution = """dQ = m c dT, KE = (1/2) m v^2"""
		mbullet = random.randint(1,9)
		vbullet = random_handler.ten(180)
		cbullet = 128
		KE = 0.5 * mbullet*GRAMS_KG * (vbullet**2)
		dT = KE / (mbullet*GRAMS_KG * cbullet)
		self.answer = """{dT:g} °C""".format(dT = dT)
		
		self.question = """A {mbullet:g}g bullet (c = 0.0305 cal/gC = 128 J/kgK) moving at {vbullet:g} m/s enters a bag of sand and stops. By what amount does the temperature of the bullet change if all its kinetic energy becomes thermal energy that is added to the bullet?""".format(vbullet = vbullet, mbullet = mbullet)
		
class schaums_18_15:
	def __init__(self,*args,**kwargs): 
		solution = """dQ = m c dT"""
		mperson = random_handler.ten(60)
		cbody = 0.83
		energy = random_handler.hundred(2500)
		dt = (energy*BIGCAL_CAL)/(mperson*KG_GRAMS*cbody)
		self.answer = """{dt:g}°C""".format(dt = dt)
		
		self.question = """Suppose a {mperson:g}kg person consumes {energy:g} Cal of food in one day. If the entire heat equivalent of this food were retained by the person's body, how large a temperature change would it cause? (For the body, c = 0.83 cal/gC). Remember that 1 Cal = 1 kcal = 1000 cal.""".format(mperson = mperson, energy = energy)
		
class schaums_18_16:
	def __init__(self,*args,**kwargs): 
		solution = """RH = mass_water_conc / mass_water_saturated_conc"""
		rh = random_handler.ten(35)
		l = random.randint(5,12)
		w = random.randint(5,12)
		h = random.randint(5,12)
		saturated = 19.33 / 1000
		m_water_conc = rh*PERCENT * saturated
		mwater = m_water_conc * (l*w*h)
		self.answer = """{mwater:g} kg""".format(mwater=mwater)
		self.question = """A thermometer in a {l:g} m x {w:g} m x {h:g} m room reads 22°C and a humidistat reads the R.H. to be {rh:g} percent. What mass of water vapor is in the room? Saturated air at 22°C contains 19.33 g H2O/m^3""".format(l=l,w=w,h=h,rh=rh)
		
class schaums_18_17:
	def __init__(self,*args,**kwargs): 
		solution = """RH = mass_water_conc / mass_water_saturated_conc"""
		tinit = random.randint(20,30)
		tdew = random.randint(10,19)
		tinitcon = random.uniform(25,28)
		tinitcon = round(tinitcon,2)
		tdewcon = random.uniform(12,15)
		tdewcon = round(tdewcon,2)
		
		rh = tdewcon / tinitcon
		rh = rh *100
		self.answer = """{rh:g}%""".format(rh = rh)
		
		self.question = """On a certain day when the temperature is {tinit:g}°C, moisture forms on the outside of a glass of cold drink if the glass is at a temperature of {tdew:g}°C or lower. What is the RH on the day? Saturated air at {tinit:g}°C contains {tinitcon:g} g/m3 of water, while at {tdew:g}°C, it contains {tdewcon:g} g/m^3.""".format(tinit = tinit, tdew = tdew, tinitcon = tinitcon, tdewcon = tdewcon)
		
class schaums_18_18:
	def __init__(self,*args,**kwargs): 
		tout = random.randint(1,10)
		rhout = random.randint(10,30)
		tin = tout + random.randint(10,20)
		rhin = rhout + random.randint(10,30)
		conout = random.uniform(4,8)
		conout = round(conout,2)
		conin = random.uniform(15,19)
		conin = round(conin,2)
		
		mass_wv_tout = rhin*PERCENT *conin
		mass_wv_tin_comf = rhout*PERCENT *conout
		onem3_at_tin = (c.CELSIUS_KELVIN(tin) / c.CELSIUS_KELVIN(tout))
		mass_wv_tin_expanded = onem3_at_tin * mass_wv_tin_comf
		tobeadded_per_m3 = (mass_wv_tin_expanded - mass_wv_tout)
		self.answer = """{a:g} g""".format(a = tobeadded_per_m3)
		
		solution = f"""
mass_wv_tout = {rhin}*PERCENT *{conin}
mass_wv_tin_comf = {rhout}*PERCENT *{conout}
onem3_at_tin = (c.CELSIUS_KELVIN({tin}) / c.CELSIUS_KELVIN({tout}))
mass_wv_tin_expanded = {onem3_at_tin} * {mass_wv_tin_comf}
tobeadded_per_m3 = ({mass_wv_tin_expanded} - {mass_wv_tout})"""

		self.question = """Outside air at {tout:g}°C and {rhout:g} percent relative humidity is introduced into a heating and airconditioning plant where it is heated to {tin:g}°C and its relative humidity is increased to a comfortable {rhin:g} percent. How many grams of water must be evaporated into a cubic meter of outside air to accomplish this? Saturated air at {tout:g}°C contains {conout:g} g/m^3 of water, and at {tin:g}°C it contains {conin:g} g/m^3.""".format(tout=tout,rhout = rhout, rhin = rhin,tin = tin, conout=conout,conin = conin)
		
class schaums_19_1:
	def __init__(self,*args,**kwargs): 
		thick_cm = random.randint(2,5)
		area_cm2 = random_handler.hundred(5000)
		temp1 = random_handler.ten(150)
		temp2 = temp1 - random.randint(5,20)
		kt = 80
		
		power = kt * (area_cm2*CM2_M2)* ((temp1 - temp2)/(thick_cm*CENTI))
		self.answer = f'{power} W'
		solution = f"""
power = kt * (area*CM2_M2) ((temp1 - temp2)/(thick_cm*CENTI)
power = {kt} * ({area_cm2}*CM2_M2)* (({temp1} - {temp2})/({thick_cm}*CENTI)
power = {power}"""
		
		self.question = f"""An iron plate {thick_cm} cm thick has a cross-sectional area of {area_cm2} cm^2. One face is at {temp1}°C and the other is at {temp2}°C. How much heat passes through the plate each second? For iron, kt = 80 W/mK"""
		
class schaums_19_2:
	def __init__(self,*args,**kwargs): 
		thickness = random_handler.ten(4)
		dt = random_handler.ten(32)
		power = random_handler.ten(200)
		area = random_handler.ten(5)
		
		kt = (power*KCALHR_WATTS) * ((thickness*MILLI)/(area*CM2_M2*dt))
		self.answer = f'{kt} W/mK'
		solution = f"""
kt = (power*KCALHR_WATTS) * ((thickness*MILLI)/(area*CM2_M2*dt))
kt = ({power}*KCALHR_WATTS) * (({thickness}*MILLI)/({area}*CM2_M2*{dt}))
kt = {kt}"""
		
		self.question = f"""A metal plate {thickness} mm thick has a temperature difference of {dt}°C betweeen its faces. It transmits {power} kcal/h through an area of {area} cm^2. Calculate the thermal conductivity of this metal in W/mK."""
		
class schaums_19_3:
	def __init__(self,*args,**kwargs): 
		area = random_handler.ten(80)
		thick = random_handler.ten(3)
		temp1 = random_handler.ten(100)
		temp2 = random_handler.ten(0)
		kt1 = random.uniform(46,50)
		kt1 = round(kt1,2)
		kt2 = random.uniform(65,70)
		kt2 = round(kt2,2)
		
		tjunc = sympy.solveset((kt1*(temp1 - x)) - (kt2*(x - temp2)),x,domain=sympy.Reals).args[0]
		tjunc = sympy.N(tjunc)
		
		power = kt1 * (area*CM2_M2) * (temp1 - tjunc) / (thick*MILLI)
		self.answer = f'{tjunc}°C , {power} W'
		solution = f"""
{kt1}*({temp1} - tjunc) = ({kt2}*(tjunc - {temp2})
tjunc = {tjunc}
power = kt1 * (area*CM2_M2) * (temp1 - tjunc) / (thick*MILLI)
power = {kt1} * ({area}*CM2_M2) * ({temp1} - {tjunc}) / ({thick}*MILLI)
power = {power}"""
		
		self.question = f"""Two metal plates are soldered together. It is known that A = {area} cm^2, L1 = L2 = {thick} mm, T1 = {temp1}°C, T2 = {temp2}°C. For the plate on the left, kt1 = {kt1} W/mK; for the plate on the right kt2 = {kt2} W/mK. Find the heat flow rate through the plates and the temperature T of the soldered junction. 
		https://lesliecaminadecom.files.wordpress.com/2019/05/6vh8mi1b5nd3391frev0.png"""
		
class schaums_19_4:
	def __init__(self,*args,**kwargs): 
		edge = random_handler.ten(42)
		thick = random_handler.ten(3)
		kt = 0.050
		tout = random_handler.ten(20)
		
		area = 6*(edge**2)
		power = kt * (area*CM2_M2) * (tout) / (thick*CENTI)
		mass_melted = (power * 3600) / (LATENT_HEAT_FUSION_ICE_JKG)
		self.answer = f'{mass_melted} kg'
		solution = f"""
area = 6*(edge**2)
area = 6*({edge}**2)
area = {area} 
power = kt * (area*CM2_M2) * (tout - 0) / (thick*CENTI)
power = {kt} * ({area}*CM2_M2) * ({tout} - 0) / ({thick}*CENTI)
power = {power}
mass_melted = (power * 3600) / (LATENT_HEAT_FUSION_ICE_JKG)
mass_melted = ({power} * 3600) / ({LATENT_HEAT_FUSION_ICE_JKG})
mass_melted = {mass_melted}"""

		
		
		self.question = f"""A beverage cooler is in the shape of a cube, {edge}cm on each inside edge. Its {thick} cm thick walls are made of plastic (kt = 0.050 W/mK). When the outside temperature is {tout}°C, how much ice will melt inside the cooler each hour?"""
		
class schaums_19_5:
	def __init__(self,*args,**kwargs): 
		kt = 1
		length = random_handler.ten(3)
		dia_in = random_handler.ten(1)
		dia_out = dia_in + 0.2
		tempwater = random_handler.ten(20)
		tempsteam = random.randint(100,120)
		
		area_in = math.pi * dia_in * length #CM2
		area_out = math.pi * dia_out * length #CM2
		area = (1/2) * (area_in + area_out) #averaging the two areas
		thickness = (dia_out - dia_in) / 2
		power = kt * area * (tempsteam - tempwater) / (thickness) #the cms will cancel so the units are fine
		
		self.answer = f'{power} cals/ s'
		solution = f"""
	area_in = math.pi * dia_in * length 
	area_in = math.pi * {dia_in} * {length}
	area_in = {area_in}
	area_out = math.pi * dia_out * length
	area_out = math.pi * {dia_out} * {length}
	area_out = {area_out}
	area = (1/2) * (area_in + area_out)
	area = (1/2) * ({area_in} + {area_out})
	area = {area}
	thickness = (dia_out - dia_in) / 2
	thickness = ({dia_out} - {dia_in}) / 2
	thickness = {thickness}
	power = kt * area * (tempsteam - tempwater) / (thickness)
	power = {kt} * {area} * ({tempsteam} - {tempwater}) / ({thickness})
	power = {power} """
		
		self.question = f"""A copper tube (length, {length} m; inner diameter, {dia_in} cm; outer diameter, {dia_out} cm) passes through a vat of rapidly circulating water maintained at {tempwater}°C. Live steam at {tempsteam}°C passes through the tube. What is the heat flow rate from the steam into the vat? How much steam is condensed each minute? For copper, kt = 1.0 cal/(s cm C)""" 
		
class schaums_19_6:
	def __init__(self,*args,**kwargs): 
		r1 = 1.93
		r2 = 4.3
		r3 = 0.45
		rtotal = r1 + r2 + r3
		rtotal = rtotal * USCUSTOMARYUNIT_KELVINPERWATT
		area = random_handler.ten(15)
		dt = random_handler.ten(20)
		time = 3600
		dQ = area*dt*time / rtotal
		self.answer = f'{rtotal} K/W, {dQ} J'
		solution = f"""
rtotal = (r1 + r2 + r3) * USCUSTOMARYUNIT_KELVINPERWATT
rtotal = {r1} + {r2} + {r3}*{USCUSTOMARYUNIT_KELVINPERWATT}
rtotal = {rtotal}
time = 3600
dQ = area*dt*time / rtotal
dQ = {area}*{dt}*{time} / {rtotal}
dQ = {dQ}"""
		self.question = f"""Calculate the R value for a wall consisting of the following layers: concrete block ( R = 1.93 ), 1 inch of insulating board (R = 4.3), and 0.50 inch of drywall (R=0.45), all in US Customary Units. If the wall has an area of {area} m^2, find the heat flow per hour through it when the temperature just outside is {dt} °C lower than inside."""
		
class schaums_19_7:
	def __init__(self,*args,**kwargs): 
		diameter = random_handler.r(2)
		temperature = random_handler.r(600)
		area = 4*math.pi*(diameter*CENTI/2)**2
		power = area*STEFAN_BOLTZMANNS_CONSTANT*((c.CELSIUS_KELVIN(temperature))**4)
		self.answer = f'{power} W'
		solution = f"""
area = 4*math.pi*(diameter*CENTI/2)**2
area = 4*math.pi*({diameter}*CENTI/2)**2
area = {area}
power = area*STEFAN_BOLTZMANNS_CONSTANT*c.CELSIUS_KELVIN(temperature)**4
power = {area}*{STEFAN_BOLTZMANNS_CONSTANT}*c.CELSIUS_KELVIN({temperature})**4
power = {power}"""
		self.question = f"""A spherical body of {diameter} cm diameter is maintained at {temperature}°C. Assuming that it radiates as if it were a blackbody, at what rate (in watts) is energy radiated from the sphere?"""
		
class schaums_19_8:
	def __init__(self,*args,**kwargs): 
		area = random_handler.r(140)/100
		emissivity = random_handler.u(0.5)
		temperature_body = 37
		time = 60
		temperature_room = temperature_body - random.randint(10,20)
		power = area * STEFAN_BOLTZMANNS_CONSTANT * emissivity * (c.CELSIUS_KELVIN(temperature_body)**4 - c.CELSIUS_KELVIN(temperature_room)**4)*time
		power_kcal = power * JOULE_KCAL
		
		self.answer = f'{power} J, {power_kcal} kcal'
		solution = f"""
power = area * STEFAN_BOLTZMANNS_CONSTANT * emissivity * (c.CELSIUS_KELVIN(temperature_body)**4 - c.CELSIUS_KELVIN(temperature_room)**4)*time
power = {area} * {STEFAN_BOLTZMANNS_CONSTANT} * {emissivity} * (c.CELSIUS_KELVIN({temperature_body})**4 - c.CELSIUS_KELVIN({temperature_room})**4)*{time}
power = {power}
power_kcal = {power} * JOULE_KCAL
power_kcal = {power_kcal}"""

		self.question = f"""An unclothed person whose body has a surface area of {area} m^2 with an emissivity of {emissivity} has a skin temperature of {temperature_body}°C and stands in a {temperature_room}°C room. How much energy does the person lose per minute?"""
		
class schaums_20_1:
	def __init__(self,*args,**kwargs): 
		dQ = random_handler.r(8)
		dW = random_handler.r(6)
		
		self.question = f"""In certain process, {dQ} kcal of heat is furnished to the system while the system does {dW} kJ of work. By how much does the internal energy of the system change during the process?""" 
		
		dQ = dQ * KCAL_JOULE 
		dW = dW * KILO
		dU = dQ - dW
		
		self.answer = f'{dU} J'
		solution = f"""
dQ = dQ * KCAL_JOULE
dW = dW * KILO
dU = dQ - dW
dU = {dQ} - {dW}
dU = {dU}"""

class schaums_20_2:
	def __init__(self,*args,**kwargs): 
		mass = random_handler.r(50)
		temp1 = random_handler.r(21)
		temp2 = temp1 + random_handler.r(37-21)
		dQ = mass * GRAMS * SPECIFIC_HEAT_WATER_JKGK * (temp2 - temp1)
		dW = 0 #practically zero expansion of water
		dU = dQ - dW 
		self.answer = f'{dU} J'
		solution = f"""
dQ = mass * GRAMS * SPECIFIC_HEAT_WATER_JKGK * (temp2 - temp1)
dQ = {mass} * {GRAMS} * {SPECIFIC_HEAT_WATER_JKGK} *({temp2} - {temp1})
dQ = {dW}
dW = 0
dU = dQ - dW
dU = {dQ} - {dW}
dU = {dU} """
		self.question = f"""The specific heat of water is {SPECIFIC_HEAT_WATER_JKGK} J/kgK. By how many joules does the internal energy of {mass} g of water change as it is heated from {temp1}°C to {temp2}°C?"""
		
class schaums_20_3:
	def __init__(self,*args,**kwargs): 
		mass = random_handler.r(5)
		dQ = mass * LATENT_HEAT_FUSION_ICE_CALG 
		dW = 0 
		dU = dQ - dW
		dU_J = dU * CAL_JOULE
		self.answer = f'{dU} cal, {dU_J} J'
		solution = f"""
dQ = mass * LATENT_HEAT_FUSION_ICE_CALG 
dQ = {mass} * {LATENT_HEAT_FUSION_ICE_CALG} 
dW = 0 
dU = dQ - dW
dU = {dQ} - {dW}
dU = {dU} cal, {dU_J} J"""
		
		self.question = f"""How much does the internal energy of {mass} g of ice at precisely 0°C increase as it is changed to water at 0°C? Neglect the changed in volume."""
		
class schaums_20_4:
	def __init__(self,*args,**kwargs): 
		spring_const = random_handler.r(500)
		mass_block = random_handler.r(400)
		mass_water = random_handler.r(900)
		specific_heat_block = random_handler.r(450)
		dx = random_handler.r(15)
		PE = (1/2)* spring_const * (dx*CENTI)**2
		dT = sympy.solveset(mass_block*GRAMS*specific_heat_block*x + mass_water*GRAMS*SPECIFIC_HEAT_WATER_JKGK*x - PE,x,domain = sympy.Reals).args[0]
		dT = sympy.N(dT)
		self.answer = f'{dT} K'
		solution = f"""
PE = (1/2)* spring_const * (dx*CENTI)**2
PE = (1/2)* {spring_const} * ({dx}*CENTI)**2
PE = {PE}
mass_block*specific_heat_block*dT + mass_water*SPECIFIC_HEAT_WATER_JKGK*dT =  PE
{mass_block}*GRAMS*{specific_heat_block}*dT + {mass_water}*GRAMS*{SPECIFIC_HEAT_WATER_JKGK}*dT =  {PE}
dT = {dT}"""
		
		self.question = f"""A spring (k = {spring_const} N/m) supports a {mass_block} g mass which is immersed in {mass_water}g of water. The specific heat of the mass is {specific_heat_block} J/kgK. The spring is now stretched {dx} cm and, after thermal equilibrium is reached, the mass is released so it vibrates up and down. By how much has the temperature of the water changed when the vibration has stopped?"""
		
class schaums_20_5:
	def __init__(self,*args,**kwargs): 
		edge = random_handler.r(6)
		temp1 = random_handler.r(20)
		temp2 = random_handler.r(300)
		ciron = 0.11
		mass = random_handler.r(1700)
		beta = 3.6E-5
		p = STP_PRESSURE
		volume = (edge*CENTI)**3
		dQ = ciron * mass * (temp2 - temp1)
		dQJ = dQ * CAL_JOULE
		dV = volume * beta * (temp2 - temp1)
		dW = p * dV
		dU = dQJ - dW
		self.answer = f'Internal Energy Change = {dU} J,  Work = {dW} J'
		solution = f"""
volume = (edge*CENTI)**3
volume = ({edge}*CENTI)**3
volume = {volume}
dQ = ciron * mass * (temp2 - temp1)
dQ = {ciron} * {mass} * ({temp2} - {temp1})
dQ = {dQ} cal
dQ = {dQJ} J
dV = volume * beta * (temp2 - temp1)
dV = {volume} * {beta} * ({temp2} - {temp1})
dV = {dV}
dW = p * dV
dW = {p} * {dV}
dW = {dW}
dU = dQ - dW
dU = {dQJ} - {dW}
dU = {dU}"""

		self.question = f"""Find ΔW and ΔU for a {edge}-cm cube of iron as it is heated from {temp1}°C to {temp2}°C at atmospheric pressure. For iron, c = 0.11 cal/gC, and the volume coefficient of thermal expansion is 3.6 x 10^-5 °C^-1. The mass of the cube is {mass}g."""

class schaums_20_6:
	def __init__(self,*args,**kwargs): 
		power_hp = random_handler.r(4)/10
		masswater = random_handler.r(5)
		tempinc = random_handler.r(6)
		
		power = power_hp * HORSEPOWER_WATTS
		dQ = masswater * SPECIFIC_HEAT_WATER_JKGK * tempinc
		time = dQ / power
		time_min = time/60
		self.answer = f'{time_min} min'
		solution = f"""            
power = power_hp * HORSEPOWER_WATTS
power = {power_hp} * {HORSEPOWER_WATTS}
power = {power} W
dQ = masswater * SPECIFIC_HEAT_WATER_JKGK * tempinc
dQ = {masswater} * {SPECIFIC_HEAT_WATER_JKGK} * {tempinc}
dQ = {dQ} J
time = dQ / power
time = {dQ} / {power}
time = {time} s, {time_min} min"""
		
		self.question = f"""A motor supplies {power_hp} hp to stir {masswater} kg of water. Assuming that all the work goes into heating the water by friction losses, how long will it take to increase the temperature of the water {tempinc}°C"""
		
class schaums_20_7:
	def __init__(self,*args,**kwargs): 
		heat1_cal = random_handler.r(500)
		work1_J = random_handler.r(400)
		heat2_cal = random_handler.r(300)
		work2_J = random_handler.r(420)
		heat3_cal = random_handler.r(1200)
		
		dU1 = heat1_cal*CAL_JOULE - work1_J 
		dU2 = heat2_cal*CAL_JOULE - (-work2_J)
		dU3 = -heat3_cal*CAL_JOULE
		
		self.answer = f'{dU1} J, {dU2} J, {dU3} J'
		solution = f"""
dU1 = heat1_cal*CAL_JOULE - work1_J 
dU1 = {heat1_cal}*{CAL_JOULE} - {work1_J}
dU1 = {dU1} J
dU2 = heat2_cal*CAL_JOULE - (-work2_J)
dU2 = {heat2_cal}*{CAL_JOULE} - (-{work2_J})
dU2 = {dU2} J
dU3 = -heat3_cal*CAL_JOULE
dU3 = -{heat3_cal}*{CAL_JOULE}
dU3 = {dU3} J
"""
		
		self.question = f"""In each of the following situations, find the change in internal energy of the system. a) A system absorbs {heat1_cal} cal of heat and at the same time does {work1_J} J of work. b) A system absorbs {heat2_cal} cal and at the same time {work2_J} of work is done on it. c) {heat3_cal} calories is removed from a gas held at constant volume. Give your answer in kiljoules."""
		
class schaums_20_8:
	def __init__(self,*args,**kwargs): 
		work1_J = random_handler.r(5)
		work2_J = random_handler.r(80)
		dQ1 = 0
		dQ2 = 0
		dU1 = - (work1_J)
		dU2 = - (-work2_J)
		self.answer = f'{dU1} J, {dU2} J'
		solution = f"""
dQ1 = 0
dQ2 = 0
dU1 = - (work1_J)
dU1 = - ({work1_J})
dU1 = {dU1} J
dU2 = - (-work2_J)
dU2 = - (-{work2_J})
dU2 = {dU2} J"""
		
		self.question = f"""For each of the following adiabatic processes, find the change in internal energy. a) A gas does {work1_J} J of work while expanding adiabatically. b) During an adiabatic compression, {work2_J} J of work is done on a gas."""
		
class schaums_20_9:
	def __init__(self,*args,**kwargs): 
		cv = 0.177
		cp = 0.248
		mass = random_handler.r(5)
		temp1 = random_handler.r(10)
		temp2 = random_handler.r(130)
		
		dW = 0
		dQv = cv * mass*KG_GRAMS *(temp2 - temp1)
		dQv_J = dQv * CAL_JOULE
		
		dU = dQv_J
		
		dQp = cp * mass *KG_GRAMS *(temp2 - temp1)
		dQp_J = dQp * CAL_JOULE
		dW = dQp_J - dU
		
		self.answer = f'Work = {dW} J,Internal Energy = {dU} J'
		solution = f"""
dW = 0
dQv = cv * mass*KG_GRAMS *(temp2 - temp1)
dQv = {cv} * {mass}*{KG_GRAMS} *({temp2} - {temp1})
dQv = {dQv} cal
dQv_J = dQv * CAL_JOULE
dQv_J = {dQv} * {CAL_JOULE}
dQv_J = {dQv_J} J
dU = dQv_J
dU = {dQv_J} J
dQp = cp * mass *KG_GRAMS *(temp2 - temp1)
dQp = {cp} * {mass} *{KG_GRAMS} *({temp2} - {temp1})
dQp = {dQp} cal
dQp_J = dQp * CAL_JOULE
dQp_J = {dQp} * {CAL_JOULE}
dQp_J = {dQp_J} J
dW = dQp_J - dU
dW = {dQp_J} - {dU}
dW = {dW} J"""
		
		self.question = f"""The temperature of {mass} kg of N2 gas is raised from {temp1}°C to {temp2}°C. If this is done at constant pressure, find the increase in internal energy ΔU and the external work ΔW done by the gas. For N2 gas, cv = 0.177  cal/g°C and cp = 0.248 cal/g°C."""
		
class schaums_20_10:
	def __init__(self,*args,**kwargs): 
		mass = 1
		dV = 1.68 - 0.001
		p = 101E3
		Lv = LATENT_HEAT_VAPORIZATION_STEAM_JKG
		dQ = mass * Lv
		dW = p * dV
		fraction = dW / (mass*Lv)
		dU = dQ - dW
		self.answer = f'{fraction}, {dU} J'
		solution = f"""
Lv = LATENT_HEAT_VAPORIZATION_STEAM_JKG
Lv = {LATENT_HEAT_VAPORIZATION_STEAM_JKG}
dQ = mass * Lv
dQ = {mass} * {Lv}
dQ = {dQ}
dW = p * dV
dW = {p} * {dV}
dW = {dW}
fraction = dW / (mass*Lv)
fraction = {dW} / ({mass}*{Lv})
fraction = {fraction}
dU = dQ - dW
dU = {dQ} - {dW}
dU = {dU}"""
		self.question = f"""One kilogram of steam at 100°C and 101 kPa occupies 1.68 m^3. a) What fraction of the observed heat of vaporization of water is accounted for by the expansion of water into steam? b) Determine the increase in internal energy of {mass} kg of water as it is vaporized at 100°C"""
		
class schaums_20_11:
	def __init__(self,*args,**kwargs): 
		cv = 740
		M = 28
		cp = cv + (UNIVERSAL_GAS_CONSTANT / (M*KGKMOL_KGMOL))
		self.answer = f'{cp} J/kgK'
		solution = f"""
cp = cv + (UNIVERSAL_GAS_CONSTANT / (M*KGKMOL_KGMOL))
cp = {cv} + ({UNIVERSAL_GAS_CONSTANT}) / ({M}*{KGKMOL_KGMOL}))
cp = {cp}"""
		self.question = f"""For nitrogen gas, cv = 740 J/kgK. Find its specific heat at constant pressure. ( The molecular mass of nitrogen gas is 28 kg/kmol)"""
		
class schaums_20_12:
	def __init__(self,*args,**kwargs): 
		volume_initial = random_handler.r(3)
		volume_final = volume_initial + random_handler.r(21)
		pressure_initial = random_handler.r(20)
		
		dW_iso = (pressure_initial*ATM_PA) * (volume_initial*LITERS_M3) * math.log(volume_final / volume_initial, math.exp(1))
		
		self.answer = f'{dW_iso} J'
		solution = f"""
dW_iso = (pressure_initial*ATM_PA) * (volume_initial*LITERS_M3) * math.log(volume_final / volume_initial, math.exp(1))
dW_iso = ({pressure_initial}*{ATM_PA}) * ({volume_initial}*{LITERS_M3}) * math.log({volume_final} / {volume_initial}, math.exp(1))
dW_iso = {dW_iso}"""
		
		self.question = f"""How much work is done by an ideal gas in expaning isothermally from an initial volume of {volume_initial} liters at {pressure_initial} atm to a final volume of {volume_final} liters?"""
		
class schaums_20_13:
	def __init__(self,*args,**kwargs): 
		volume1 = random_handler.r(22)
		temp1 = random_handler.r(12)
		pressure1 = random_handler.r(100)
		volume2 = volume1 - random.randint(5,volume1 - 1)
		gamma = 1.67
		pressure2 = pressure1 * (volume1 / volume2)**gamma
		temp2 = (c.CELSIUS_KELVIN(temp1)) * (volume1 / volume2)**(gamma - 1)
		self.answer = f'{pressure2} kPa, {temp2} K'
		solution = f"""
gamma = 1.67
pressure2 = pressure1 * (volume1 / volume2)**gamma
pressure2 = {pressure1} * ({volume1} / {volume2})**{gamma}
pressure2 = {pressure2} kPa
temp2 = (c.CELSIUS_KELVIN(temp1)) * (volume1 / volume2)**(gamma - 1)
temp2 = (c.CELSIUS_KELVIN({temp1})) * ({volume1} / {volume2})**({gamma} - 1)
temp2 = {temp2} K"""

		self.question = f"""Some {volume1} cubic centimeters of monoatomic gas at {temp1}°C and {pressure1} kPa is suddenly (and adiabaticallly) compressed to {volume2} cm^3. What are its new pressure and temperature?""" 
		
class schaums_20_14:
	def __init__(self,*args,**kwargs): 
		tempc = random_handler.r(100)
		temph = random_handler.r(400)
		efficiency = 1 - (c.CELSIUS_KELVIN(tempc)/c.CELSIUS_KELVIN(temph))
		efficiency_percentage = efficiency * 100
		
		self.answer = f'{efficiency_percentage} %'
		solution = f"""
efficiency = 1 - (c.CELSIUS_KELVIN(tempc)/c.CELSIUS_KELVIN(temph))
efficiency = 1 - (c.CELSIUS_KELVIN({tempc})/c.CELSIUS_KELVIN({temph}))
efficiency = {efficiency}
efficiency_percentage = efficiency * 100
efficiency_percentage = {efficiency} * 100
efficiency_percentage = {efficiency_percentage} %"""

		self.question = f"""Compute the maximum possible efficiency of a heat engine operating between the temperature limits of {tempc}°C and {temph}°C"""
		
class schaums_20_15:
	def __init__(self,*args,**kwargs): 
		eff_comp_carnot_show = random_handler.r(30)
		eff_comp_carnot = eff_comp_carnot_show / 100
		
		tempc = random_handler.r(35)
		temph = random_handler.r(220)
		power_hp = random_handler.r(8)
		
		carnot_eff = 1 - (c.CELSIUS_KELVIN(tempc) / c.CELSIUS_KELVIN(temph))
		actual_eff = eff_comp_carnot * carnot_eff
		output_work = power_hp * HORSEPOWER_WATTS * WATTS_CALS
		
		input_heat = output_work / actual_eff
		rejected_energy = input_heat *(1 - actual_eff)
		
		self.answer = f'{input_heat} cal/s, {rejected_energy} cal/s'
		solution = f"""
carnot_eff = 1 - (c.CELSIUS_KELVIN(tempc) / c.CELSIUS_KELVIN(temph))
carnot_eff = 1 - (c.CELSIUS_KELVIN({tempc}) / c.CELSIUS_KELVIN({temph}))
carnot_eff = {carnot_eff}
actual_eff = eff_comp_carnot * carnot_eff
actual_eff = {eff_comp_carnot} * {carnot_eff}
actual_eff = {actual_eff}
output_work = power_hp * HORSEPOWER_WATTS * WATTS_CALS
output_work = {power_hp} * {HORSEPOWER_WATTS} * {WATTS_CALS}
input_heat = output_work / actual_eff
input_heat = {output_work} / {actual_eff}
input_heat = {input_heat}
rejected_energy = input_heat *(1 - actual_eff)
rejected_energy = {input_heat} *(1 - {actual_eff})
rejected_energy = {rejected_energy}"""
		self.question = f"""A steam engine operating between a boiler temperature of {temph}°C and a condenser temperature of {tempc}°C delivers {power_hp} hp. If its efficiency is {eff_comp_carnot_show}% of that for a Carnot engine operating between this temperature limits, how many calories are absorbed each second by the boiler? How many calories are exhausted to the condenser each second?"""
		
		
class schaums_20_16:
	def __init__(self,*args,**kwargs): 
		kmoles = random_handler.r(3)
		moles = kmoles * KILO
		mass = kmoles * 2
		temp1 = STP_TEMPERATURE
		pressure1 = STP_PRESSURE
		cv = 10 
		volume1 = 22.4 * kmoles
		volume2 = 2 * volume1
		vol2_vol1_ratio = 2
		
		temp2 = c.CELSIUS_KELVIN(temp1) * vol2_vol1_ratio
		
		work = pressure1 * (volume2 - volume1)
		
		heatv = cv * mass * (temp2 - temp1) 
		internal_energy = heatv
		
		heatp = internal_energy + work
		heatp_mega = heatp / MEGA
		self.answer = f'{heatp_mega} MJ'
		solution = f"""
temp2 = c.CELSIUS_KELVIN(temp1) * vol2_vol1_ratio
temp2 = c.CELSIUS_KELVIN({temp1}) * {vol2_vol1_ratio}

work = pressure1 * (volume2 - volume1)
work = {pressure1} * ({volume2} - {volume1})
work = {work}

heatv = cv * mass * (temp2 - temp1)
heatv = {cv} * {mass} *({temp2} - {temp1})
heatv = {heatv}
internal_energy = heatv
internal_energy = {internal_energy}

heatp = internal_energy + work
heatp = {internal_energy} + {work}
heatp = {heatp}
heatp_mega = heatp / MEGA
heatp_mega = {heatp} / {MEGA}
heatp_mega = {heatp_mega}"""

		self.question = f"""{kmoles} kmoles ({mass} kg) of hydrogen gas at STP expands isobarically to precisely twice its volume. a) What is the final temperature of the gas? b) What is the expansion work done by the gas? c) By how much does the internal energy of the gas change? d) How much heat enters the gas during the expansion? For H2, cv = 10 kJ / kgK
		"""
class schaums_20_17:
	def __init__(self,*args,**kwargs): 
		mass = r.r(8)
		area = r.r(60)
		pressure_atmosphere = 100
		temp1 = r.r(30)
		temp2 = temp1 + random.randint(50,90)
		distance = r.r(20)
		
		piston_pressure = (mass*9.81) / (area *CM2_M2)
		gas_pressure = piston_pressure + pressure_atmosphere*KILO
		dV = (distance * CENTI) * (area * CM2_M2)
		difference = gas_pressure * dV
		self.answer = f'{difference} J'
		solution = f"""            
piston_pressure = (mass*9.81) / (area *CM2_M2)
piston_pressure = ({mass}*9.81) / ({area} *{CM2_M2})
piston_pressure = {piston_pressure}
gas_pressure = piston_pressure + pressure_atmosphere*KILO
gas_pressure = {piston_pressure} + {pressure_atmosphere}*{KILO}
gas_pressure = {gas_pressure}
dV = (distance * CENTI) * (area * CM2_M2)
dV = ({distance} * {CENTI}) * ({area} * {CM2_M2})
dV = {dV}
heating:
dQ1 = dU1 + dW1 = dU1 + p *dV = dU1 + {gas_pressure} * {dV}
dQ1 = dU1 + {difference}
cooling:
- dQ2 = dU2
returning to original temperature:
dU1 = dU2
therefore:
dQ1 - dQ2 = dW
dQ1 - dQ2 = {difference}"""
		
		self.question = f"""A cylinder of ideal gas is closed by an {mass}kg movable piston (area = {area} cm^2). Atmospheric pressure is {pressure_atmosphere} kPa. When the gas is heated from {temp1}°C to {temp2}°C, the piston rises {distance} cm. The piston is then fastened in place, and the gas is cooled back to {temp1}°C. Calling ΔQ1 the heat added to the gas in the heating process, and ΔQ2 the heat lost during cooling, find the difference between ΔQ1 and ΔQ2.https://lesliecaminadecom.files.wordpress.com/2019/05/il11ly75q87l0l0fs4f2.png"""


#chapter 21 - entropy and the second law

class example_22_2:
	def __init__(self,*args,**kwargs):
		wavelength = c.length( random_handler.main(18.0),'cm')
		frequency = c.frequency ( random_handler.main(1900),'Hz')
		
		self.question = f"""Measurements show that the wavelength of sound wave in certain material is {wavelength.cm}cm. The frequency of the wave is {frequency.Hz}Hz. What is the speed of the sound wave?"""
		
		speed = c.speed( wavelength.m * frequency.Hz )
		
		self.answer = f"""Velocity = {speed.mpers} m/s"""
		
class example_22_3:
	def __init__(self,*args,**kwargs):
		length = c.length(random_handler.main(5), 'm')
		mass = c.mass(random_handler.main(1.45),'g')
		frequency = c.frequency( random_handler.main(120), 'Hz')
		wavelength = c.length( random_handler.main(60.0), 'cm')
		
		self.question = f"""A horizontal cord {length.m}m long has a mass {mass.g}g. What must be the tension in the cord if the wavelength of a {frequency.Hz}Hz wave on it is to be {wavelength.cm}cm? How large a mass must be hung from its end (say, over a pulley) to give it this tension?"""
		
		velocity = c.velocity( wavelength.m * frequency.Hz )
		tension = c.force( (mass.kg / length.m)*velocity.mpers )
		mass = c.mass (  tension.N / gravity.mpers2 )
		
		self.answer = f"""Mass = {mass.kg} kg"""
		
class example_22_4:
	def __init__(self,*args,**kwargs):
		length = c.length( random_handler.main(20),'m')
		mass = c.mass (random_handler.main(5),'kg')
		frequency = c.frequency ( random_handler.main(7.0), 'Hz')
		
		self.question = f"""A uniform flexible cable is {length.m} m long and has a mass of {mass.kg}kg. It hangs vertically under its own weight and is vibrated from its upper end with a frequency of {frequency.Hz}Hz. a) Find the speed of a tranverse wave on the midpoint. b) What are the frequency and wavelength at the midpoint."""
		
		tension = c.force( 0.5 * mass.kg * gravity.mpers2 )
		mu = c.mass( mass.kg / length.m )
		velocity = c.velocity( math.sqrt( tension.N / mu.kg ) )
		wavelength = c.length( velocity.mpers / frequency.Hz )
		
		self.answer = f"""Velocity of wave = {velocity.mpers} m/s
Wavelength = {wavelength.m} m"""

# class example_22_5:
	# def __init__(self,*args,**kwargs):
		# tension = c.force(random_handler.main(88),'N')
		# length = c.length(random_handler.main(50.0),'cm')
		# mass = c.mass(random_handler.main(0.50),'g')
		
		# self.question = f"""Shows a metalyrsa
		
#chapter 22 not finished yet

# chapter 23 - sound
# chapter 24 - electrostatics
class schaums_24_1:
	def __init__(self,*args,**kwargs): 
		distance = c.length(random_handler.main(1.5))
		force = c.force(random_handler.main(2))
		
		self.question = f"""Two coins lie {distance.m} m apart on a table. They carry identical charges. Approximately how large is the charge on each coin if a coin experiences a force of {force.N} N?"""
		
		charge = c.charge(
		math.sqrt( 
		force.N * distance.m**2 / k_coulomb
		)
		)
		
		self.answer = f"""Charge on each coin = {charge.uC} uC"""
		
class schaums_24_2:
	def __init__(self,*args,**kwargs): 
		er_water = 80
		distance = c.length(random_handler.main(1.5))
		force = c.force(random_handler.main(2))
		
		self.question = f"""Two coins lie {distance.m} m apart underwater ( er_water = {er_water} ). They carry identical charges. Approximately how large is the charge on each coin if a coin experiences a force of {force.N} N?"""
		
		charge = c.charge(
		math.sqrt(
		force.N * distance.m**2 * er_water / k_coulomb
		)
		)
		
		self.answer = f"""Charge on each coin = {charge.uC} uC"""
		
class schaums_24_3:
	def __init__(self,*args,**kwargs): 
		charge_He = 2
		charge_Ne = 10
		charge_He_C = c.charge(2 * c.CHARGE_ELECTRON)
		charge_Ne_C = c.charge(10 * c.CHARGE_ELECTRON)
		distance = c.length( random_handler.main(3), 'nm')
		
		self.question = f"""A helium nucleus has charge +{charge_He}e, and a neon nucleus +{charge_Ne}e, where "e" is the quantum of charge, {c.CHARGE_ELECTRON} C. Find the repulsive force exerted on one by the other when they are {distance.nm} nm apart. Assume the system to be in a vacuum."""
		
		force = c.force(
		k_coulomb * charge_He_C.C * charge_Ne_C.C / distance.m**2
		)
		
		self.answer = f"""Force between the two nuclei = {force.nN} nN"""

class schaums_24_4:
	def __init__(self,*args,**kwargs):
		distance = c.length(random_handler.main(5.3) * 1e-11)
		electron_mass = c.mass(9.1e-31)
		
		self.question = f"""In the Bohr model of the hydrogen atom, an electron ( q = - e ) circles a proton ( q' = e ) in an orbit of radius {distance.pm} pm. The attraction of the proton for the electron furnishes the centripetal force needed to hold the electron in orbit. Find a) the force of electrical attraction between the particles and b) the electron's speed. The electron mass is {electron_mass.kg} kg."""
		
		force = c.force(
		k_coulomb * c.CHARGE_ELECTRON**2 / distance.m**2
		)
		
		velocity = c.velocity(
		math.sqrt(
		force.N * distance.m / electron_mass.kg
		)
		)
		
		self.answer = f"""Force of attraction = {force.nN} nN
Speed of the electron = {velocity.mpers} m/s"""
#chapter 24 not finished yet



# chapter 25 - potential and capacitance
# chapter 26 - current,  resistance and ohm's law
# chapter 27 - electrical power
# chapter 28 - equivalent resistance, simple circuits
# chapter 29 - kirchoff's laws
# chapter 30 - forces in magnetic fields
# chapter 31 - sources of magnetic fields
# chapter 32 - induced emf and magnetic flux
# chapter 33 - electric generators and motors
# chapter 34 - inductance, rc and rl time constants
# chapter 35 - alternating current
# chapter 36 - reflection of light

# chapter 37 - refraction of light
# chapter 38 - thin lenses
# chapter 39 - optical instruments
# chapter 40 - interference and diffraction of light
# chapter 41 - relativity
# chapter 42 - quantum physics and wave mechanics
# chapter 43 - the hydrogen atom
# chapter 44 - multielectron atoms
# chapter 45 - nuclei and radioactivity
# chapter 46 - applied nuclear physics




#SERWAY AND JEWETT --------------------------------------------------------------------------

class serway_7_1:
	def __init__(self,*args,**kwargs): 
		
		force1 = c.force(random_handler.main(50))
		angle1 = c.angle(random_handler.main(30), 'degrees')
		displacement1 = c.length(random_handler.main(3))
		
		self.question = f"""A man cleaning a floor pulls a vacuum cleaner with a force of magnitude F = {force1.N} N at an angle of {angle1.deg} degrees with the horizontal. Calculate the work done by the force on the vacuum cleaner as the vacuum cleaner is displaced {displacement1.m} m to the right."""
		
		work1 = c.energy(force1.N * displacement1.m * math.cos(angle1.rad))
		
		self.answer = f"""{round(work1.J,2)} J"""
		
class serway_7_3:
	def __init__(self,*args,**kwargs): 
		
		deltar = vectors_engine.vector(x_comp = random_handler.main(2), y_comp = random_handler.main(3))
		force = vectors_engine.vector(x_comp = random_handler.main(5), y_comp = random_handler.main(2))
		
		self.question = f"""A particle moving in the xy plane undergoes a displacement given by deltar = {deltar.vector} m as a constant force F = {force.vector} N acts on the particle. Calculate the work done by F on the particle."""
		
		work = c.energy(force.dot(deltar))
		
		self.answer = f"""{round(work.J,2)} J"""
		
class serway_7_5:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(550), 'g')
		displacement = c.length(random_handler.main(2), 'cm')
		
		self.question = f"""A common technique used to measure the force constant of a spring is demonstrated by the setup. The spring is hung vertically and an object of mass m is attached to its lower end. Under the action of the load 'mg', the spring stretches a distance d from its equilibrium position. a) If a spring is stretched {displacement.cm} cm by a suspended object having a mass of {mass.kg} kg, what is the force constant of the spring.? b) How much work is done by the spring on the object as it stretches through this distance?"""
		
		
		k = c.springConstant(
		(mass.kg * gravity.mpers2) / displacement.m
		)
		
		work = c.energy( - 0.5 * k.Nperm * displacement.m**2)
		
		self.answer = f"""{round(k.Nperm, 2)} N/m, {round(work.J, 2)} J"""

class serway_7_6:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(6))
		force = c.force(random_handler.main(12))
		disp = c.length(random_handler.main(3))
		
		self.question = f"""A {mass.kg} kg block initially at rest is pulled to the right along a frictionless, horizontal surface by a constant horizontal force of magnitude {force.N} N. Find the block's speed after it has moved through a horizontal distance of {disp.m} m."""

		velocityf = c.velocity(
		math.sqrt(
		(2 * force.N * disp.m) / (mass.kg)
		)
		)

		self.answer = f"""{round(velocityf.mpers,2)} m/s"""
		
		
class serway_8_3:
	def __init__(self,*args,**kwargs): 
		mass = c.mass(random_handler.main(35), 'g')
		ya = c.length(random_handler.main(-120), 'cm')
		yc = c.length(random_handler.main(20), 'm')
		
		
		self.question = f"""The launching mechanism of a popgun consists of a trigger-released spring. The spring is compressed to a position ya and the trigger is fired. The projectile of mass m rises to a position yc above the position at which it leaves the spring, indicated as position yb = 0. Consider a firing of the gun for which m = {mass.g}g, ya = {ya.m} m, and yc = {yc.m} m. a) Neglecting all resistive forces, determine the spring constant. b) Find the speed of the projectile as it moves through the equilibrium position b of the spring."""
		
		k = c.springConstant(
		(2*mass.kg*gravity.mpers2*(yc.m - ya.m)) / (ya.m**2)
		)
		
		velocityb = c.velocity(
		math.sqrt(
		(k.Nperm*ya.m**2 / mass.kg) + 2 * gravity.mpers2 * ya.m
		)
		)
		
		self.answer = f"""{round(k.Nperm,2)} N/m, {round(velocityb.mpers,2)} m/s"""

class serway_8_4:
	def __init__(self,*args,**kwargs): 
		regen = True
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(6))
			force = c.force(random_handler.main(12))
			disp = c.length(random_handler.main(3))
			mu = random_handler.main(0.15)
			
			self.question = f"""A {mass.kg} kg block initially at rest is pulled to the right along a horizontal surface by a constant horizontal force of {force.N} N. a) Find the speed of the block after it has moved {disp.m} m if the surfaces in contact have a coefficient of kinetic friction of {mu}. b) Suppose the force F is applied at an angle theta. At what angle should the force be to achieve the largest possible speed after the block has moved {disp.m} m to the right?"""
			
			fk = c.force( mu * mass.kg * gravity.mpers2)
			
			try:
				velocityfinal = c.velocity(
				math.sqrt(
				(2/mass.kg) * ( - fk.N * disp.m + force.N * disp.m )
				)
				)
				regen = False
			except:
				regen = True
		
		theta = c.angle(math.atan(mu), 'radians')
		
		self.answer = f"""{round(velocityfinal.mpers,2)} m/s, {round(theta.degrees,2)} degrees."""

class serway_8_6:
	def __init__(self,*args,**kwargs): 
		regen = True
		while regen:
			print(type(self))
			mass = c.mass(random_handler.main(1.6))
			k = c.springConstant(random_handler.main(1000))
			disp = c.length(random_handler.main(2), 'cm')
			friction = c.force(random_handler.main(4))
			
			self.question = f"""A block of mass {mass.kg}kg is attached to a horizontal spring that has a force constant of {k.Nperm} N/m. The spring is compressed {disp.cm} cm and is then released from rest. a) Calculate the speed of the block as it passes through the equilibrium position x = 0 if the surface is frictionless. b) Calculate the speed of the block as it passes through the equilibrium position if a constant friction force of {friction.N} N retards its motion from the moment is released."""
			try:
				velocityf = c.velocity(
				math.sqrt(
				(2 / mass.kg) * ( 0.5 * k.Nperm * disp.m**2 )
				)
				)
				
				velocityf2 = c.velocity(
				math.sqrt(
				(2/mass.kg) * (0.5 * k.Nperm * disp.m**2 - friction.N * disp.m)
				)
				)
				
				regen = False
			except:
				regen = True
		
		self.answer = f"""{round(velocityf.mpers,2)} m/s, {round(velocityf2.mpers,2)} m/s"""

class serway_8_7:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(3))
		length = c.length(random_handler.main(1))
		angle = c.angle(random_handler.main(30), 'degrees')
		friction = c.force(random_handler.main(5))
		
		self.question = f"""A {mass.kg} kg crate slides down a ramp. The ramp is {length.m} m length and inclined at an angle of {angle.degrees} degrees. The crate starts from rest at the top, experiences a constant friction force of magnitude {friction.N} N, and continues to move a short distance on the horizontal floor after it leaves the ramp. a) Determine the speed of the crate at the bottom of the ramp. b) How far does the crate slide on the horizontal floor if it continues to experience a friction force of magnitude {friction.N} N?"""
		height = c.length(length.m * math.sin(angle.radians))
		
		velocityf = c.velocity(
		(2/mass.kg) * (mass.kg *gravity.mpers2 * height.m  - friction.N * length.m)
		)
		
		distance = c.length( 
		(mass.kg * velocityf.mpers**2) / (2 * friction.N)
		)
		
		self.answer = f"""{round(velocityf.mpers,2)} m/s, {round(distance.m,2)} m"""

class serway_8_8:
	def __init__(self,*args,**kwargs): 
		
		mass = c.mass(random_handler.main(800), 'g')
		va = c.velocity(random_handler.main(1.2))
		k = c.springConstant(random_handler.main(50), 'Nperm')
		mu = random_handler.main(0.5)
		
		self.question = f"""A block having a mass of {mass.kg} kg is given an initial velocity va = {va.mpers} m/s to the right and collides with a spring whose mass is negligible and whose force constant is k = {k.Nperm} N/m. a) Assuming the surface to be frictionless, calculate the maximum compression of the spring after the collision. b) Suppose a constant force of kinetic friction acts between the block and the surface, with us = {mu}. If the speed of the block at the moment it collides with the spring is va = {va.mpers} m/s, what is the maximum compression xc in the spring?"""
		
		xmax = c.length(
		math.sqrt(mass.kg / k.Nperm) * va.mpers
		)
		
		equation = sympy.Eq(
		k.Nperm * x**2 + 2*mu*mass.kg*gravity.mpers2*x - mass.kg*va.mpers**2,
		0
		)
		
		solution_set = sympy.solveset(equation, x)
		solution_list = list(solution_set)
		
		for i in range(len(solution_list)):
			if solution_list[i] > 0:
				x2 = c.length(solution_list[i])
				
		self.answer =f"""{round(xmax.m,2)} m, {round(x2.m,2)} m"""

class serway_8_11:
	def __init__(self,*args,**kwargs): 
		
		elevatormass = c.mass(random_handler.main(1600), 'kg')
		loadmass = c.mass(random_handler.main(200), 'kg')
		friction = c.force(random_handler.main(4000), 'N')
		velocity = c.velocity(random_handler.main(3), 'mpers')
		accel = c.acceleration(random_handler.main(1),'mpers2')
		
		
		self.question = f"""An elevator car has a mass of {elevatormass.kg} kg and is carrying passengers having a combined mass of {loadmass.kg} kg. A constant friction force of {friction.N} N retards its motion. a) How much power must a motor deiver to lift the elevator car and its passengers at a constant speed of {velocity.mpers} m/s? b) What power must the motor deliver at the instant the speed of the elevator is "v" if the motor is designed to provide the elevator car with an upward acceleration of {accel.mpers2} m/s2?"""
		
		mass = c.mass(elevatormass.kg + loadmass.kg)
		
		power = c.power(
		(mass.kg * gravity.mpers2 + friction.N ) * velocity.mpers
		)
		
		power2 = c.power(
		(mass.kg*(accel.mpers2 + gravity.mpers2) + friction.N ) 
		)
		
		self.answer = f"""{round(power.W,2)} W, {round(power2.W,2)} W"""

class serway_36_3:
	def __init__(self,*args,**kwargs): 
		
		temp = random.randint(0,2)
		do_list = [25, 10, 5]
		do = c.length(random_handler.main(do_list[temp]), 'cm')
		f = c.length(random_handler.main(10), 'cm')
		
		self.question = f"""A spherical mirror has a focal length of {f.cm} cm. Locate the describe the image for an object distance of {do.cm} cm."""
		
		equation = sympy.Eq(
		1/f.cm,
		(1/x) + (1/do.cm)
		)
		
		di_set = sympy.solveset(equation, x)
		#print(di_set)
		di_list = list(di_set)
		
		for i in range(len(di_list)):
			if di_list[i] >= 0:
				di = c.length(di_list[i], 'cm')
				
		magnification = - di.cm / do.cm
		
		self.answer = f"""Image Distance = {di.cm} cm
Magnification = {magnification}"""

class serway_36_4:
	def __init__(self,*args,**kwargs): 
		
		do = c.length(random_handler.main(10))
		f = c.length(random_handler.main(-0.6))
		
		self.question = f"""An automobile rearview mirror shows an image of a truck located {do.m} m from the mirror. The focal length of the mirror is {f.m} m. a) Find the position of the image of the truck. b) Find the magnification of the image."""
		
		equation = sympy.Eq(
		1/f.m , 
		1/do.m + 1/x
		)
		
		di_set = sympy.solveset(equation, x)
		di_list = list(di_set)
		di = c.length(di_list[0])
		
		magnification = - di.m / do.m
		
		self.answer = f"""Image distance = {di.m} m
Magnification = {magnification} """

class serway_36_6:
	def __init__(self,*args,**kwargs): 
		regen = True
		while regen:
			print(type(self))
			radius = c.length(random_handler.main(3), 'cm')
			nplastic = 1.50
			nair = 1.0
			do = c.length(random_handler.main(2), 'cm')
			
			self.question = f"""A set of coins is embedded in a spherical plastic paperweight having a radius of {radius.cm} cm. The index of refraction of the plastic is n1 = {nplastic}. One coin is located {do.cm} from the edge of the sphere. Find the position of the image of the coin."""
			
			if radius.m > do.m:
				regen = False
				
		equation = sympy.Eq(
		nair/x, 
		((nair - nplastic)/-radius.cm) - (nplastic/do.cm)
		)
		
		di_set = sympy.solveset(equation, x)
		di_list = list(di_set)
		di = c.length(di_list[0], 'cm')
		
		self.answer = f"""Image distance = {di.cm}"""
		
class serway_36_7:
	def __init__(self,*args,**kwargs): 
		
		
		
		self.question = f"""A small fish is swimming at a depth "d" below the surface of a pond. a) What is the apparent depth of the fish as viewed from directly overhead? b) If your face is at a distance "d" above the water surface, What apparent distance above the surface does the fish see your face?"""
		
		self.answer = f"""Situation A = - {-1.00 / 1.33} d
Situation B = - {1.33/1.00} d"""


class serway_36_8:
	def __init__(self,*args,**kwargs): 
		
		lenstype_i = random.randint(0,1)
		lenstypes = ['converging', 'diverging']
		f = c.length(random_handler.main(10), 'cm')
		do_list = [30,10,5]
		temp = random.randint(0,2)
		do = c.length(random_handler.main(do_list[temp]), 'cm')
		
		if lenstype_i == 1:
			f = c.length(-f.cm , 'cm')
		
		
		self.question = f"""A {lenstypes[lenstype_i]} lens has a focal length of {f.cm} cm. a) An object is placed {do.cm} cm from the lens. Find the image distance."""
		
		equation = sympy.Eq(
		1/f.cm, 
		1/x + 1/do.cm
		)
		
		di_set = sympy.solveset(equation, x)
		di_list = list(di_set)
		di = c.length(di_list[0], 'cm')
		
		self.answer = f"""Image distance = {di.cm} cm"""


		

		
		
		
		
		
		
		
		
		
		

		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		