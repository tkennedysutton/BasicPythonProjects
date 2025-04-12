
"""1. Building a Simple Calculator with Robust Error Handling
Personal Perspective
Tristan’s World:
Think of your Calculator as a tool for everyday decisions—whether calculating the best coffee price or quickly figuring out if you should budget in extra time for a rock climbing session. It handles errors gracefully, much like deciding to leave a coffee shop if the brew isn’t up to par.
"""
# Define a class called Calculator


class Calculator:
    """A simple calculator to perform arithmetic operations with error handling."""
    
    # Method to add two numbers
    def add(self, a, b):
        return a + b  # Return the sum of a and b
    
    # Method to subtract second number from the first
    def subtract(self, a, b):
        return a - b  # Return the difference between a and b
    
    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b  # Return the product of a and b
    
    # Method to divide the first number by the second
    def divide(self, a, b):
        try:
            result = a / b  # Try to perform division
        except ZeroDivisionError:
            # If division by zero is attempted, print an error message
            print("Error: Division by zero is not allowed.")
            return None  # Return None to indicate an invalid result
        return result  # If no error, return the division result

# Create an instance (object) of the Calculator class
calc = Calculator()

# Call the 'add' method from the Calculator instance and print the result
print("Tristan's Addition:", calc.add(10, 5))  # Expected output: 15

# Call the 'divide' method with valid numbers and print the result
print("Tristan's Division (valid):", calc.divide(10, 2))  # Expected output: 5.0

# Call the 'divide' method with division by zero to see error handling in action
print("Tristan's Division (error):", calc.divide(10, 0))  # Expected: Error message + None
#What’s happening? Error Handling: The divide method uses a try-except block to catch a division-by-zero error. This mechanism is much like deciding not to trust a coffee shop with a “bad brew.”