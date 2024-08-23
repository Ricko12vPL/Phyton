def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_prime_non_prime():
    prime_sum = 0
    non_prime_sum = 0

    while True:
        command = input()

        if command == "stop":
            break

        number = int(command)

        if number < 0:
            print("Number is negative.")
            continue

        if is_prime(number):
            prime_sum += number
        else:
            non_prime_sum += number

    print(f"Sum of all prime numbers is: {prime_sum}")
    print(f"Sum of all non prime numbers is: {non_prime_sum}")


# Przykład użycia
sum_prime_non_prime()
