# Odczyt liczby n
n = int(input())

# Inicjalizacja liczników dla każdego przedziału
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

# Pętla iterująca przez n liczb
for i in range(n):
    num = int(input())

    # Sprawdzanie do którego przedziału należy liczba
    if num < 200:
        count_p1 += 1
    elif num < 400:
        count_p2 += 1
    elif num < 600:
        count_p3 += 1
    elif num < 800:
        count_p4 += 1
    else:
        count_p5 += 1

# Obliczanie procentów dla każdego przedziału
p1 = (count_p1 / n) * 100
p2 = (count_p2 / n) * 100
p3 = (count_p3 / n) * 100
p4 = (count_p4 / n) * 100
p5 = (count_p5 / n) * 100

# Wyświetlanie wyników
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
