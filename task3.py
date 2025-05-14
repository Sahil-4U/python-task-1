import math

# Factorial of a number:-
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


factorialInput=int(input('Enter a number: '))
print(f'Factorial of {factorialInput} is: {factorial(factorialInput)}')

# Math module operation:-
mathOperationInput=int(input('Enter a number: '))
print(f'square root: {math.sqrt(mathOperationInput)}')
print(f'Logarithm: {math.log(mathOperationInput)}')
print(f'Sine: {math.sin(mathOperationInput)}')
