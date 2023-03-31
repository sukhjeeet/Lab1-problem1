def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+,-,*,/): ")
    return num1, num2, operator

def displayResult(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == '/':
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operator")

num1, num2, operator = takeInput()
displayResult(num1, num2, operator)
