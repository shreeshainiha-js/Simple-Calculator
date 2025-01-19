# Function for a simple calculator
def calculator(a, b, operation):
    # Perform the desired operation based on user input
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        # Check to avoid division by zero
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation!"

# Example usage
num1 = 10  # First number
num2 = 5   # Second number
operation = '*'  # Operation to perform (e.g., '+', '-', '*', '/')

# Call the calculator function and store the result
result = calculator(num1, num2, operation)

# Display the result
print(f"Result of {num1} {operation} {num2} = {result}")
