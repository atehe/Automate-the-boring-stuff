import random
from typing import Text

numberOfStreaks = 0

for experimentNumber in range(1000):
    # code that creates a list of 100 heads  or tails values
    test_result = []
    for i in range(100):
        if random.randint(0, 1):
            test_result.append("H")
        else:
            test_result.append("T")

    # code that checks if there is a streak of 6nheads or tails in a row
    for i, flip in enumerate(test_result):
        if i + 6 == len(test_result):
            break
        elif test_result[i : i + 6] == ["H"] * 6 or test_result[i : i + 6] == ["T"] * 6:
            numberOfStreaks += 1

print("Chances of streak: %s%%" % (numberOfStreaks / 100))
