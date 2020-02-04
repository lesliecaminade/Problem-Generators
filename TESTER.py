from mathsub import differential_equation_engine as engine

def main():
	object = engine.DE_2()

	#for objects that are non-questions
	#object.init_random()

	print(object.question)
	print()
	print(object.answer)
	print()
	print()
	print()

for i in range(10):
	main()


