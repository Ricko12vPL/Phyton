def sum_digits_even_odd_positions(num):
    num_str = str(num)
    even_sum = 0
    odd_sum = 0

    for i in range(len(num_str)):
        digit = int(num_str[i])
        if i % 2 == 0:  # Nieparzysta pozycja (indeks 0, 2, 4...)
            odd_sum += digit
        else:  # Parzysta pozycja (indeks 1, 3, 5...)
            even_sum += digit

    return even_sum, odd_sum


def equal_sums_even_odd_position(start, end):
    result = []
    for num in range(start, end + 1):
        even_sum, odd_sum = sum_digits_even_odd_positions(num)
        if even_sum == odd_sum:
            result.append(num)

    if result:
        print(" ".join(map(str, result)))


# Przykłady użycia:
start = int(input())
end = int(input())
equal_sums_even_odd_position(start, end)
