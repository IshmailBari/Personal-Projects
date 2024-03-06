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
    tokens = re.findall(r'\d*\.?\d+|\S', expression)
    print("Tokens:", tokens)  # Print the tokens for debugging
    return tokens


def shunting_yard(tokens):
    # Convert infix expression to postfix using the Shunting Yard algorithm
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []
    
    print("Input Tokens:", tokens)  # Print the input tokens for debugging
    
    for token in tokens:
        if token.replace('.', '').isdigit():
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
    
    print("Postfix Output:", output)  # Print the postfix output for debugging
    
    return output

def evaluate_postfix(tokens):
    # Evaluate the postfix expression
    stack = []
    
    for token in tokens:
        try:
            # Attempt to convert the token to a float
            number = float(token)
            stack.append(number)
        except ValueError:
            # Token is an operator
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
    print("Expression:", expression)  # Print the expression for debugging
    tokens = tokenize(expression)
    print("Tokens:", tokens)  # Print the tokens for debugging
    postfix = shunting_yard(tokens)
    print("Postfix:", postfix)  # Print the postfix expression for debugging
    try:
        result = evaluate_postfix(postfix)
        label_result.config(text="Result: " + str(result))
    except ValueError as e:
        label_result.config(text="Error: " + str(e))

def add_to_expression(char):
    if char == 'C':
        entry.delete(0, tk.END)  # Clear the entry
    else:
        entry.insert(tk.END, char)

# Create the GUI
root = tk.Tk()
root.title("Calculator")

label = tk.Label(root, text="Enter expression:")
label.grid(row=0, column=0, columnspan=4)

entry = tk.Entry(root, width=30)
entry.grid(row=1, column=0, columnspan=4)

button_texts = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('-', 4, 3),
    ('.', 5, 0), ('0', 5, 1), ('(', 5, 2), (')', 5, 3),
    ('+', 6, 3), ('C', 6, 0)
]

buttons = []
for text, row, column in button_texts:
    button = tk.Button(root, text=text, command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=column)
    buttons.append(button)

calculate_button = tk.Button(root, text="=", command=calculate)
calculate_button.grid(row=5, column=1, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=6, column=0, columnspan=4)

root.mainloop()
