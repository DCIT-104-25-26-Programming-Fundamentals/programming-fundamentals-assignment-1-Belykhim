def print_single_table(n):
    # Print the multiplication table for a given number from 1 to 12
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 13):
        print(f"  {n:<2} x  {i:<2} =  {n * i}")


def print_tables_up_to_n(n):
    # Print multiplication tables for every number from 1 up to n
    for number in range(1, n + 1):
        print_single_table(number)
        if number < n:
            print("  ---------------------------")


def main():
    # Part A - Single Table
    print("=== PART A: Single Table ===")
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Error: Please enter a positive integer greater than zero.")
            return
        print_single_table(num)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return

    # Part B - Tables from 1 to N
    print("\n=== PART B: Tables from 1 to N ===")
    try:
        limit = int(input("Enter a number N: "))
        if limit <= 0:
            print("Error: Please enter a positive integer greater than zero.")
            return
        print_tables_up_to_n(limit)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()