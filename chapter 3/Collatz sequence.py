# Collatz sequence with input validation
# using try and except block


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1 
import sys
print('Input integer:')
try:
    num = int(input())
except ValueError:
    print('must input an integer')
    sys.exit()
    

while True:
    num = collatz(num)
    if num == 1:
        break




