def generate_fibonacci(n):
    # Handle cases where n is 0 or negative
    if n <= 0:
        return []
    # If only 1 term is needed, return just [0]
    if n == 1:
        return [0]

    # Start the sequence with the first two numbers
    sequence = [0, 1]
    
    # Loop to calculate the rest of the terms up to n
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence


def is_fibonacci(num):
    # Negative numbers are not in the sequence
    if num < 0:
        return False

    # Keep generating terms until we reach or pass the number
    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    # If 'a' equals 'num', it's part of the Fibonacci sequence
    return a == num


def print_first_n_terms():
    # Get user input for Part A
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: Please enter a positive integer greater than zero.")
            return

        # Generate and print the terms separated by spaces
        seq = generate_fibonacci(n)
        formatted_seq = " ".join(str(x) for x in seq)
        print(f"Fibonacci sequence: {formatted_seq}")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


def check_fibonacci_number():
    # Get user input for Part B
    try:
        num = int(input("Enter a number to check: "))
        if is_fibonacci(num):
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


def main():
    # Run Part A
    print("=== PART A: First N Terms ===")
    print_first_n_terms()

    # Run Part B
    print("\n=== PART B: Check Sequence Membership ===")
    check_fibonacci_number()


if __name__ == "__main__":
    main()