# Day 2: Basic math operations - Add, Sub, Mul, Div

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Print results
print("\nResults:")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
