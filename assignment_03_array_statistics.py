def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def main():
    try:
        count_input = input("How many numbers? ")
        count = int(count_input)

        if count <= 0:
            print("Error: Please enter a positive integer greater than zero.")
            return

        numbers = []
        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        total = calculate_sum(numbers)
        avg = calculate_average(numbers)
        maximum = find_maximum(numbers)
        minimum = find_minimum(numbers)

        print("\nResults:")
        print(f"Sum:     {total:g}")
        print(f"Average: {avg:g}")
        print(f"Maximum: {maximum:g}")
        print(f"Minimum: {minimum:g}")

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()