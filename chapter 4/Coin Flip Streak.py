import random
from typing import Text

numberOfStreaks = 0

for experimentNumber in range(1000):
    #code that creates a list of 100 heads  or tails values
    test_result = []
    for i in range(100):
        if random.randint(0, 1):
            test_result.append('H')
        else:
            test_result.append('T')
        print(test_result)
    #code that checks if there is a streak of 6nheads or tails in a row
    for i in range(len(test_result)):
        

print(numberOfStreaks)
                
        


print('Chances of streak: %s%%' % (numberOfStreaks / 100))