##################################
#Name: Calculator Project
#Author: Ishmail Bari
#
#
#
############################

calculatorOn = True
savedOperation = False
operation = None
while calculatorOn:
    test = True
    if 'temp' in locals():
        choice = input("what will your first input be? (number, /, X, +, -)")
    else:
        choice = "number"
    if choice == "number":
        test = True
        while test:
            number = input("Please input an integer")
            try:
                number = int(number)
                test = False
            except ValueError:
                print("That was not an integer")
        if savedOperation:
            if operation == "/":
                temp = temp/number
            elif operation == "X":
                temp = temp * number
            elif operation == "+":
                temp = temp + number
            elif operation == "-":
                temp = temp - number
        else:
            temp = number
    elif choice == "/":
        savedOperation = True
        operation = "/"
    elif choice =="X":
        savedOperation = True
        operation = "X"
    elif choice == "+":
        savedOperation = True
        operation = "+"
    elif choice == "-":
        savedOperation = True
        operation = "-"
    print(temp)
        
