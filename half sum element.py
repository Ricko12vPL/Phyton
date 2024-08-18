# n = int(input())
#
# sum_nums = 0
# highest = 0
#
#
# for i in range(n):
#     num_input = int(input())
#     sum_nums += num_input
#     if sum_nums > highest:
#         highest = num_input
#
# sum_nums -= highest
#
# if highest == sum_nums:
#     print("Yes")
#     print(f"Sum = {sum_nums}")
# else:
#     diff = abs(highest - sum_nums)
#     print("No")
#     print(f"Diff = {diff}")

# Odczyt liczby n
n = int(input())

# Inicjalizacja zmiennych
max_num = None
total_sum = 0

# Pętla iterująca przez n liczb
for i in range(n):
    num = int(input())
    total_sum += num

    # Znajdowanie największej liczby
    if max_num is None or num > max_num:
        max_num = num

# Obliczenie sumy wszystkich liczb poza największą
sum_without_max = total_sum - max_num

# Sprawdzenie warunków
if max_num == sum_without_max:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - sum_without_max)
    print("No")
    print(f"Diff = {diff}")
