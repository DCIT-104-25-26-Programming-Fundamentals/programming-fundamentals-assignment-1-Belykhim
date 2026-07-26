def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")
        