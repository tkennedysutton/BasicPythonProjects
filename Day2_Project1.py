# Coffee budget calculator
# Define custom exceptions for specific errors
class NoGoodCupsCoffeeError(Exception):
    pass

class NoAverageCupsCoffeeError(Exception):
    pass

class BudgetExceededError(Exception):
    pass

class NoCoffeeTodayError(Exception):
    pass
# Define a class called Calculator
class Calculator:
    """A simple calculator to perform arithmetic operations with error handling."""
    
    # Method to add two numbers
    def add(self, a, b):
        result = a + b
        return result  # Return the sum of a and b
    
    # Method to subtract second number from the first
    def subtract(self, a, b):
        result = a - b
        return result  # Return the difference between a and b
    
    # Method to multiply two numbers
    def multiply(self, a, b):
        result = a * b
        return result  # Return the product of a and b
    
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

# Define the coffee calculation functions with error handling
def good_coffee_is_not_zero(no_coffee, cost_cup):
    try:
        if no_coffee == 0:
            raise NoGoodCupsCoffeeError("Error: No good coffee today! (sad face)")
        result = calc.multiply(no_coffee, cost_cup)
        if result > coffee_budget:
            raise BudgetExceededError("Error: Budget exceeded! You’ve spent too much on good coffee.")
        return result
    except NoGoodCupsCoffeeError as e:
        print(f"Error: {e}")
        return None
    except BudgetExceededError as e:
        print(f"Error: {e}")
        return None

def average_coffee_is_not_zero(no_coffee, cost_cup):
    try:
        if no_coffee == 0:
            raise NoAverageCupsCoffeeError("Error: No average coffee today! (poor choice)")
        result = calc.multiply(no_coffee, cost_cup)
        if result > coffee_budget:
            raise BudgetExceededError("Error: Budget exceeded! You’ve spent too much on average coffee.")
        return result
    except NoAverageCupsCoffeeError as e:
        print(f"Error: {e}")
        return None
    except BudgetExceededError as e:
        print(f"Error: {e}")
        return None
    
def coffee_today_is_not_zero(no_average_cups,no_good_cups):
    try:
        if no_average_cups == 0 or no_good_cups == 0:
            raise NoCoffeeTodayError("Error: No coffee drunk today. You must be a zombie!")
        result = calc.add(no_average_cups,no_good_cups)
        return result
    except NoCoffeeTodayError as e:
        print(f"Error: {e}")

def total_cost_coffee(good_coffee,average_coffee):
    if good_coffee_cost is not 0 or average_coffee_cost is not 0:
        result = calc.add(good_coffee_cost,average_coffee_cost)
        return result
    else: 
        return None
    
# Variables for coffee prices and number of cups
good_coffee_price = 2.99
average_coffee_price = 1.99
no_good_cups = 2
no_average_cups = 1
coffee_budget = 6.00

# Calculate total cost for good coffee
print("Total cost of good coffee:")
result = good_coffee_is_not_zero(no_good_cups, good_coffee_price)
if result is not None:
    print(f"Cost of good coffee today: £{result:.2f}")

# Calculate total cost for average coffee
print("Total cost of average coffee:")
result = average_coffee_is_not_zero(no_average_cups, average_coffee_price)
if result is not None:
    print(f"Cost of average coffee today: £{result:.2f}")

# Calculate cost of coffee (good and average)
good_coffee_cost = good_coffee_is_not_zero(no_good_cups, good_coffee_price)
average_coffee_cost = average_coffee_is_not_zero(no_average_cups, average_coffee_price)
total_no_coffee = coffee_today_is_not_zero(no_average_cups,no_good_cups)
daily_coffee_cost = total_cost_coffee(good_coffee_cost,average_coffee_cost)

# Combine the results and calculate the total daily cost
if good_coffee_cost is not None and average_coffee_cost is not None:
    total_daily_cost = calc.add(good_coffee_cost, average_coffee_cost)
    print(f"Total daily coffee cost: £{total_daily_cost:.2f}")
else:
    print("Error: One of the coffee costs is invalid.")

if total_no_coffee is not None:
    above_or_below_budget = calc.subtract(coffee_budget,daily_coffee_cost)
    print(f"above or below budget: £{above_or_below_budget:.2f}")
else:
    print("Seriously, you need some coffee!")




