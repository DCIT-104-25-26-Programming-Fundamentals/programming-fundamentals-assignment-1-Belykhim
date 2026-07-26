def add(a, b):
    # Returns the sum of two numbers
    return a + b


def subtract(a, b):
    # Returns the difference between two numbers
    return a - b


def multiply(a, b):
    # Returns the product of two numbers
    return a * b


def divide(a, b):
    # Returns division result rounded to 2 decimal places, or an error if dividing by zero
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)


def modulus(a, b):
    # Returns the remainder after division, or an error if dividing by zero
    if b == 0:
        return "Error: Cannot perform modulus by zero."
    return a % b


def power(a, b):
    # Returns a raised to the power of b
    return a ** b


def display_menu():
    # Print the calculator menu options
    print("\n============================")
    print("      SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    # Helper function to safely read two numbers from the user
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid number input.")
        return None, None


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue

            if choice == "1":
                res = add(num1, num2)
                print(f"Result: {num1:g} + {num2:g} = {res:g}")
            elif choice == "2":
                res = subtract(num1, num2)
                print(f"Result: {num1:g} - {num2:g} = {res:g}")
            elif choice == "3":
                res = multiply(num1, num2)
                print(f"Result: {num1:g} * {num2:g} = {res:g}")
            elif choice == "4":
                res = divide(num1, num2)
                if isinstance(res, str):
                    print(res)
                else:
                    print(f"Result: {num1:g} / {num2:g} = {res}")
            elif choice == "5":
                res = modulus(num1, num2)
                if isinstance(res, str):
                    print(res)
                else:
                    print(f"Result: {num1:g} % {num2:g} = {res:g}")
            elif choice == "6":
                res = power(num1, num2)
                print(f"Result: {num1:g} ** {num2:g} = {res:g}")
        else:
            print("Invalid choice. Please select an option from 1 to 7.")


if __name__ == "__main__":
    main()