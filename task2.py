# Task-1
numberInput=int(input('Enter a number: '))
if(numberInput % 2 == 0):
    print(f'{numberInput} is an even number.')
else:
    print(f'{numberInput} is an odd number.')
    
    
# Task-2
sumOfIntegers=0
for i in range(1,51):
    sumOfIntegers=sumOfIntegers+i
    
    
print(f'The sum of numbers from 1 to 50 is: ',sumOfIntegers)