##################################
#Name: Calculator Project
#Author: Ishmail Bari
#
#
#
############################
import tkinter as tk
import re

def tokenize(expression):
    # Tokenize the expression into numbers, operators, and parentheses
    tokens = re.findall(r'\d+\.?\d*|[()+\-*/]', expression)
    return tokens

def shunting_yard(tokens):
    # Convert infix expression to postfix using the Shunting Yard algorithm
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Discard the '('
        elif token in precedence:
            while operators and precedence.get(operators[-1], 0) >= precedence.get(token, 0):
                output.append(operators.pop())
            operators.append(token)
    
    while operators:
        output.append(operators.pop())
    
    return output

def evaluate_postfix(tokens):
    # Evaluate the postfix expression
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        elif token in {'+', '-', '*', '/'}:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                stack.append(a / b)
    
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    
    return stack[0]

def evaluate(expression):
    tokens = tokenize(expression)
    postfix = shunting_yard(tokens)
    result = evaluate_postfix(postfix)
    return result

def calculate():
    expression = entry.get()
    try:
        result = evaluate(expression)
        label_result.config(text="Result: " + str(result))
    except ValueError as e:
        label_result.config(text="Error: " + str(e))

# Create the GUI
root = tk.Tk()
root.title("Calculator")

label = tk.Label(root, text="Enter expression:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
