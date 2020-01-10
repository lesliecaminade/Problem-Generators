import random
from electronics import energy_conversion_engine as engine
from num2words import num2words


def ask():
    ask_words = ['Find', 'Determine', 'Calculate', 'Compute', 'Evaluate']
    return random.choice(ask_words)

def parse(string_input):
    string_input = str(string_input)
    return string_input.replace('**', '^').replace('*', ' ')

class Constructor():
    def __init__(self, engine_class_instances):
        #Battery - a single instance of a set of givens, and an answer for a certain problem

        BATTERIES = []
        CHOICES = []
        suffix = ''
        prefix = ''
        for i in range(4):

            #battery = engine.Some_class_from_engine
            battery = engine_class_instances[i]

            #data = battery.Some_attribute_from_battery         
            data =  parse(battery.answer)

            BATTERIES.append(battery)
            CHOICES.append(prefix + str(data) + suffix) 
        main = BATTERIES[0]
        CHOICES[0] = str(CHOICES[0]) + ' #'
        random.shuffle(CHOICES)
        #edit below
        self.question = main.question
        self.answer = f"""A. {CHOICES[0]}
B. {CHOICES[1]}
C. {CHOICES[2]}
D. {CHOICES[3]}"""       
        
class johnbird_4_1():
    def __init__(self):
        instance_list = [
        engine.johnbird_4_1(),        
        engine.johnbird_4_1(),
        engine.johnbird_4_1(),
        engine.johnbird_4_1()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_4_2():
    def __init__(self):
        instance_list = [
        engine.johnbird_4_2(),        
        engine.johnbird_4_2(),
        engine.johnbird_4_2(),
        engine.johnbird_4_2()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_4_3():
    def __init__(self):
        instance_list = [
        engine.johnbird_4_3(),        
        engine.johnbird_4_3(),
        engine.johnbird_4_3(),
        engine.johnbird_4_3()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_4_4():
    def __init__(self):
        instance_list = [
        engine.johnbird_4_4(),        
        engine.johnbird_4_4(),
        engine.johnbird_4_4(),
        engine.johnbird_4_4()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_1():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_1(),        
        engine.johnbird_21_1(),
        engine.johnbird_21_1(),
        engine.johnbird_21_1()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_2():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_2(),        
        engine.johnbird_21_2(),
        engine.johnbird_21_2(),
        engine.johnbird_21_2()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_3():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_3(),        
        engine.johnbird_21_3(),
        engine.johnbird_21_3(),
        engine.johnbird_21_3()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_4():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_4(),        
        engine.johnbird_21_4(),
        engine.johnbird_21_4(),
        engine.johnbird_21_4()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_5():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_5(),        
        engine.johnbird_21_5(),
        engine.johnbird_21_5(),
        engine.johnbird_21_5()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_6():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_6(),        
        engine.johnbird_21_6(),
        engine.johnbird_21_6(),
        engine.johnbird_21_6()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_7():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_7(),        
        engine.johnbird_21_7(),
        engine.johnbird_21_7(),
        engine.johnbird_21_7()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_8():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_8(),        
        engine.johnbird_21_8(),
        engine.johnbird_21_8(),
        engine.johnbird_21_8()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_9():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_9(),        
        engine.johnbird_21_9(),
        engine.johnbird_21_9(),
        engine.johnbird_21_9()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_10():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_10(),        
        engine.johnbird_21_10(),
        engine.johnbird_21_10(),
        engine.johnbird_21_10()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_11():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_11(),        
        engine.johnbird_21_11(),
        engine.johnbird_21_11(),
        engine.johnbird_21_11()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_12():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_12(),        
        engine.johnbird_21_12(),
        engine.johnbird_21_12(),
        engine.johnbird_21_12()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_21_13():
    def __init__(self):
        instance_list = [
        engine.johnbird_21_13(),        
        engine.johnbird_21_13(),
        engine.johnbird_21_13(),
        engine.johnbird_21_13()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_1():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_1(),        
        engine.johnbird_22_1(),
        engine.johnbird_22_1(),
        engine.johnbird_22_1()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_2():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_2(),        
        engine.johnbird_22_2(),
        engine.johnbird_22_2(),
        engine.johnbird_22_2()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_3():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_3(),        
        engine.johnbird_22_3(),
        engine.johnbird_22_3(),
        engine.johnbird_22_3()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_4():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_4(),        
        engine.johnbird_22_4(),
        engine.johnbird_22_4(),
        engine.johnbird_22_4()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_5():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_5(),        
        engine.johnbird_22_5(),
        engine.johnbird_22_5(),
        engine.johnbird_22_5()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_6():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_6(),        
        engine.johnbird_22_6(),
        engine.johnbird_22_6(),
        engine.johnbird_22_6()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_7():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_7(),        
        engine.johnbird_22_7(),
        engine.johnbird_22_7(),
        engine.johnbird_22_7()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_8():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_8(),        
        engine.johnbird_22_8(),
        engine.johnbird_22_8(),
        engine.johnbird_22_8()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_9():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_9(),        
        engine.johnbird_22_9(),
        engine.johnbird_22_9(),
        engine.johnbird_22_9()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_10():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_10(),        
        engine.johnbird_22_10(),
        engine.johnbird_22_10(),
        engine.johnbird_22_10()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_11():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_11(),        
        engine.johnbird_22_11(),
        engine.johnbird_22_11(),
        engine.johnbird_22_11()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_12():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_12(),        
        engine.johnbird_22_12(),
        engine.johnbird_22_12(),
        engine.johnbird_22_12()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_13():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_13(),        
        engine.johnbird_22_13(),
        engine.johnbird_22_13(),
        engine.johnbird_22_13()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_14():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_14(),        
        engine.johnbird_22_14(),
        engine.johnbird_22_14(),
        engine.johnbird_22_14()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_15():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_15(),        
        engine.johnbird_22_15(),
        engine.johnbird_22_15(),
        engine.johnbird_22_15()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_16():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_16(),        
        engine.johnbird_22_16(),
        engine.johnbird_22_16(),
        engine.johnbird_22_16()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_17():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_17(),        
        engine.johnbird_22_17(),
        engine.johnbird_22_17(),
        engine.johnbird_22_17()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_18():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_18(),        
        engine.johnbird_22_18(),
        engine.johnbird_22_18(),
        engine.johnbird_22_18()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_19():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_19(),        
        engine.johnbird_22_19(),
        engine.johnbird_22_19(),
        engine.johnbird_22_19()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_20():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_20(),        
        engine.johnbird_22_20(),
        engine.johnbird_22_20(),
        engine.johnbird_22_20()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_21():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_21(),        
        engine.johnbird_22_21(),
        engine.johnbird_22_21(),
        engine.johnbird_22_21()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_22():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_22(),        
        engine.johnbird_22_22(),
        engine.johnbird_22_22(),
        engine.johnbird_22_22()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_23():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_23(),        
        engine.johnbird_22_23(),
        engine.johnbird_22_23(),
        engine.johnbird_22_23()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_24():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_24(),        
        engine.johnbird_22_24(),
        engine.johnbird_22_24(),
        engine.johnbird_22_24()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_25():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_25(),        
        engine.johnbird_22_25(),
        engine.johnbird_22_25(),
        engine.johnbird_22_25()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_26():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_26(),        
        engine.johnbird_22_26(),
        engine.johnbird_22_26(),
        engine.johnbird_22_26()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class johnbird_22_27():
    def __init__(self):
        instance_list = [
        engine.johnbird_22_27(),        
        engine.johnbird_22_27(),
        engine.johnbird_22_27(),
        engine.johnbird_22_27()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer  
        


        




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        