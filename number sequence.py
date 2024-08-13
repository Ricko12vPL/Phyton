# Odczyt liczby n
n = int(input())

# Inicjalizacja zmiennych do przechowywania największej i najmniejszej liczby
max_num = None
min_num = None

# Pętla iterująca przez n liczb
for i in range(n):
    num = int(input())

    # Aktualizacja największej liczby
    if max_num is None or num > max_num:
        max_num = num

    # Aktualizacja najmniejszej liczby
    if min_num is None or num < min_num:
        min_num = num

# Wyświetlanie wyników
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
