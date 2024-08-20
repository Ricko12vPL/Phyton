# Odczytanie liczby n
n = int(input())

# Inicjalizacja pierwszej liczby w sekwencji
k = 1

# Pętla do generowania i wyświetlania kolejnych liczb w sekwencji
while k <= n:
    print(k)   # Wyświetlenie aktualnej wartości k
    k = 2 * k + 1  # Obliczenie następnej liczby w sekwencji
