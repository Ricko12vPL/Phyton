def number_pyramid(n):
    current_number = 1  # Numer, który będzie wypisywany
    for row in range(1, n + 1):
        for _ in range(row):
            if current_number > n:
                return  # Zakończenie funkcji, jeśli liczba przekroczy n
            print(current_number, end=" ")
            current_number += 1
        print()  # Przejście do nowej linii po zakończeniu wiersza

# Przykłady użycia:
n = int(input())
number_pyramid(n)
