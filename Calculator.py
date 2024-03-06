##################################
#Name: Calculator Project
#Author: Ishmail Bari
#
#
#
############################
calculator_on = True
temp = 0
operation = None

while True:
    number = input("Please input a number or type 'quit' to exit: ")
    if number.lower() == 'quit':
        calculator_on = False
        break
    try:
        temp = float(number)  # Accept floating-point numbers as well
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while calculator_on:
    while True:
        number = input("Please input a number or type an operation (+, -, X, /): ")
        if number.lower() in ['+', '-', 'x', '/']:
            operation = number
            break
        elif number.lower() == 'quit':
            calculator_on = False
            break
        try:
            number = float(number)
            if operation == '+':
                temp += number
            elif operation == '-':
                temp -= number
            elif operation.lower() == 'x':
                temp *= number
            elif operation == '/':
                if number == 0:
                    print("Error: Division by zero")
                    continue
                temp /= number
            print("Result:", temp)  # Print the intermediate result
            break
        except ValueError:
            print("Invalid input. Please enter a number or an operation.")

print("Calculator is turned off.")
