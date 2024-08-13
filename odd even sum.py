# Odczyt liczby elementów
n = int(input())

# Inicjalizacja sum
even_sum = 0
odd_sum = 0

# Pętla iterująca przez wszystkie wprowadzone liczby
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:  # Sprawdzenie, czy pozycja jest parzysta
        even_sum += num
    else:  # Pozycja jest nieparzysta
        odd_sum += num

# Porównanie sum
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {diff}")
