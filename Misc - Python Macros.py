import math
import random

import pyperclip


title_string = """Choice Randomizer
Code by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com"""


    print(choice_template)
    print()
    pyperclip.copy(choice_template)
    
def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1
    
while True:
    command = input()
    
    randomize(command)
    


       
