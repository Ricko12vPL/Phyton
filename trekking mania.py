# Odczyt liczby grup wspinaczy
number_of_groups = int(input())

# Inicjalizacja liczników wspinaczy na poszczególne szczyty
climbers_makalu = 0
climbers_mont_blanc = 0
climbers_kilimanjaro = 0
climbers_k2 = 0
climbers_everest = 0

# Całkowita liczba wspinaczy
total_climbers = 0

# Przetwarzanie każdej grupy wspinaczy
for _ in range(number_of_groups):
    group_size = int(input())
    total_climbers += group_size

    if group_size <= 5:
        climbers_makalu += group_size
    elif group_size <= 12:
        climbers_mont_blanc += group_size
    elif group_size <= 25:
        climbers_kilimanjaro += group_size
    elif group_size <= 40:
        climbers_k2 += group_size
    else:
        climbers_everest += group_size

# Obliczanie procentowego udziału wspinaczy na każdym szczycie
p1 = (climbers_makalu / total_climbers) * 100
p2 = (climbers_mont_blanc / total_climbers) * 100
p3 = (climbers_kilimanjaro / total_climbers) * 100
p4 = (climbers_k2 / total_climbers) * 100
p5 = (climbers_everest / total_climbers) * 100

# Wyświetlanie wyników, sformatowanych do dwóch miejsc po przecinku
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
