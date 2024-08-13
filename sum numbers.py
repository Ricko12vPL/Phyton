# Odczyt liczby n
n = int(input())

# Inicjalizacja zmiennej sumy
total_sum = 0

# Pętla iterująca przez n liczb
for i in range(n):
    num = int(input())
    total_sum += num  # Dodawanie bieżącej liczby do sumy

# Wyświetlanie wyniku
print(total_sum)
