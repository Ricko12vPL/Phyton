def is_special_number(n, num):
    """
    Check if n is divisible by each digit of num.
    """
    num_str = str(num)
    for digit in num_str:
        if digit == '0' or n % int(digit) != 0:
            return False
    return True


def find_special_numbers(n):
    special_numbers = []
    for num in range(1111, 10000):
        if is_special_number(n, num):
            special_numbers.append(num)
    return special_numbers


def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    special_numbers = find_special_numbers(n)

    # Print the result as space-separated values
    print(" ".join(map(str, special_numbers)))


if __name__ == "__main__":
    main()
