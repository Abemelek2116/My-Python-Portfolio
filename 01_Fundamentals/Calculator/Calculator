"""
🧮 Python Calculator
--------------------
A simple command-line calculator built in Python.

Features:
- Performs basic arithmetic operations: +, -, *, /
- Allows continuous calculations with previous results
- Demonstrates the use of functions, loops, and dictionaries
"""
# --- Operation Functions ---
def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Return the difference of two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Return the division result. Raises an error for division by zero."""
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2


# Mapping of symbols to their corresponding operation functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """Main calculator loop that allows continuous calculations."""
    print(logo)
    print("Welcome to the Python Calculator!\n")

    # Ask the user for the first number
    num1 = float(input("Enter the first number: "))

    # Show available operation symbols
    print("Available operations:")
    for symbol in operations:
        print(symbol)

    should_continue = True

    # Loop for continuous calculations
    while should_continue:
        # Get user’s chosen operation
        operation_symbol = input("Pick an operation: ")

        # Validate operation input
        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue

        # Get the next number
        num2 = float(input("Enter the next number: "))

        # Perform calculation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"\nResult: {num1} {operation_symbol} {num2} = {answer}\n")

        # Ask if the user wants to continue with the result
        next_step = input(
            f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: "
        ).lower()

        if next_step == "y":
            num1 = answer
        else:
            should_continue = False
            print("\nStarting a new calculation...\n")
            calculator()  # Restart calculator recursively


# Entry point of the program
if __name__ == "__main__":
    calculator()

