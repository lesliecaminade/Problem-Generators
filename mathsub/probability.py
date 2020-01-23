import random
from mathsub import probability_engine as engine
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

class rgs_sample_1():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_1(),        
        engine.rgs_sample_1(),
        engine.rgs_sample_1(),
        engine.rgs_sample_1()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_2():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_2(),        
        engine.rgs_sample_2(),
        engine.rgs_sample_2(),
        engine.rgs_sample_2()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_3():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_3(),        
        engine.rgs_sample_3(),
        engine.rgs_sample_3(),
        engine.rgs_sample_3()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_4():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_4(),        
        engine.rgs_sample_4(),
        engine.rgs_sample_4(),
        engine.rgs_sample_4()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_5():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_5(),        
        engine.rgs_sample_5(),
        engine.rgs_sample_5(),
        engine.rgs_sample_5()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_6():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_6(),        
        engine.rgs_sample_6(),
        engine.rgs_sample_6(),
        engine.rgs_sample_6()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_7():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_7(),        
        engine.rgs_sample_7(),
        engine.rgs_sample_7(),
        engine.rgs_sample_7()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_8():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_8(),        
        engine.rgs_sample_8(),
        engine.rgs_sample_8(),
        engine.rgs_sample_8()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_9():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_9(),        
        engine.rgs_sample_9(),
        engine.rgs_sample_9(),
        engine.rgs_sample_9()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
#     
        
class rgs_sample_11():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_11(),        
        engine.rgs_sample_11(),
        engine.rgs_sample_11(),
        engine.rgs_sample_11()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_sample_12():
    def __init__(self):
        instance_list = [
        engine.rgs_sample_12(),        
        engine.rgs_sample_12(),
        engine.rgs_sample_12(),
        engine.rgs_sample_12()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
           
        
class rgs_2():
    def __init__(self):
        instance_list = [
        engine.rgs_2(),        
        engine.rgs_2(),
        engine.rgs_2(),
        engine.rgs_2()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_3():
    def __init__(self):
        instance_list = [
        engine.rgs_3(),        
        engine.rgs_3(),
        engine.rgs_3(),
        engine.rgs_3()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
           
        
class rgs_5():
    def __init__(self):
        instance_list = [
        engine.rgs_5(),        
        engine.rgs_5(),
        engine.rgs_5(),
        engine.rgs_5()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_6():
    def __init__(self):
        instance_list = [
        engine.rgs_6(),        
        engine.rgs_6(),
        engine.rgs_6(),
        engine.rgs_6()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_7():
    def __init__(self):
        instance_list = [
        engine.rgs_7(),        
        engine.rgs_7(),
        engine.rgs_7(),
        engine.rgs_7()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_8():
    def __init__(self):
        instance_list = [
        engine.rgs_8(),        
        engine.rgs_8(),
        engine.rgs_8(),
        engine.rgs_8()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_9():
    def __init__(self):
        instance_list = [
        engine.rgs_9(),        
        engine.rgs_9(),
        engine.rgs_9(),
        engine.rgs_9()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_10():
    def __init__(self):
        instance_list = [
        engine.rgs_10(),        
        engine.rgs_10(),
        engine.rgs_10(),
        engine.rgs_10()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_11():
    def __init__(self):
        instance_list = [
        engine.rgs_11(),        
        engine.rgs_11(),
        engine.rgs_11(),
        engine.rgs_11()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_12():
    def __init__(self):
        instance_list = [
        engine.rgs_12(),        
        engine.rgs_12(),
        engine.rgs_12(),
        engine.rgs_12()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_13():
    def __init__(self):
        instance_list = [
        engine.rgs_13(),        
        engine.rgs_13(),
        engine.rgs_13(),
        engine.rgs_13()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_14():
    def __init__(self):
        instance_list = [
        engine.rgs_14(),        
        engine.rgs_14(),
        engine.rgs_14(),
        engine.rgs_14()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_15():
    def __init__(self):
        instance_list = [
        engine.rgs_15(),        
        engine.rgs_15(),
        engine.rgs_15(),
        engine.rgs_15()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_16():
    def __init__(self):
        instance_list = [
        engine.rgs_16(),        
        engine.rgs_16(),
        engine.rgs_16(),
        engine.rgs_16()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_17():
    def __init__(self):
        instance_list = [
        engine.rgs_17(),        
        engine.rgs_17(),
        engine.rgs_17(),
        engine.rgs_17()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer   


class rgs_18():
    def __init__(self):
        instance_list = [
        engine.rgs_18(),        
        engine.rgs_18(),
        engine.rgs_18(),
        engine.rgs_18()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_19():
    def __init__(self):
        instance_list = [
        engine.rgs_19(),        
        engine.rgs_19(),
        engine.rgs_19(),
        engine.rgs_19()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_20():
    def __init__(self):
        instance_list = [
        engine.rgs_20(),        
        engine.rgs_20(),
        engine.rgs_20(),
        engine.rgs_20()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_21():
    def __init__(self):
        instance_list = [
        engine.rgs_21(),        
        engine.rgs_21(),
        engine.rgs_21(),
        engine.rgs_21()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_22():
    def __init__(self):
        instance_list = [
        engine.rgs_22(),        
        engine.rgs_22(),
        engine.rgs_22(),
        engine.rgs_22()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_23():
    def __init__(self):
        instance_list = [
        engine.rgs_23(),        
        engine.rgs_23(),
        engine.rgs_23(),
        engine.rgs_23()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_24():
    def __init__(self):
        instance_list = [
        engine.rgs_24(),        
        engine.rgs_24(),
        engine.rgs_24(),
        engine.rgs_24()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_25():
    def __init__(self):
        instance_list = [
        engine.rgs_25(),        
        engine.rgs_25(),
        engine.rgs_25(),
        engine.rgs_25()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_26():
    def __init__(self):
        instance_list = [
        engine.rgs_26(),        
        engine.rgs_26(),
        engine.rgs_26(),
        engine.rgs_26()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_27():
    def __init__(self):
        instance_list = [
        engine.rgs_27(),        
        engine.rgs_27(),
        engine.rgs_27(),
        engine.rgs_27()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_28():
    def __init__(self):
        instance_list = [
        engine.rgs_28(),        
        engine.rgs_28(),
        engine.rgs_28(),
        engine.rgs_28()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_29():
    def __init__(self):
        instance_list = [
        engine.rgs_29(),        
        engine.rgs_29(),
        engine.rgs_29(),
        engine.rgs_29()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_30():
    def __init__(self):
        instance_list = [
        engine.rgs_30(),        
        engine.rgs_30(),
        engine.rgs_30(),
        engine.rgs_30()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_31():
    def __init__(self):
        instance_list = [
        engine.rgs_31(),        
        engine.rgs_31(),
        engine.rgs_31(),
        engine.rgs_31()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_32():
    def __init__(self):
        instance_list = [
        engine.rgs_32(),        
        engine.rgs_32(),
        engine.rgs_32(),
        engine.rgs_32()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer    
        
class rgs_33():
    def __init__(self):
        instance_list = [
        engine.rgs_33(),        
        engine.rgs_33(),
        engine.rgs_33(),
        engine.rgs_33()        
        ]
        constructed = Constructor(instance_list)
        self.question = constructed.question
        self.answer = constructed.answer        




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        