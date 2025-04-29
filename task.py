firstInput = int(input('Enter the first number: '))
secondInput = int(input("Enter the second number: "))
firstName = str(input('Enter your first name: '))
lastName = str(input("Enter your last name: "))

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def generate_gretting_message(firstname,lastname):
    return f'Hello , {firstname} {lastname}! Welcome to the Python program.'


print('Addition: ',addition(firstInput,secondInput))
print('Subtraction: ',subtraction(firstInput,secondInput))
print ('Multiplication: ',multiplication(firstInput,secondInput))
print('Division: ',division(firstInput,secondInput))
print(generate_gretting_message(firstName,lastName))