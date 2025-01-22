def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation!"
num1 = 10 
num2 = 5  
operation = '*'  
result = calculator(num1, num2, operation)
print(result)
