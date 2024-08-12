# Dane wejściowe
days = int(input())
room_type = input()
grade = input()

# Ceny za noc
price_per_night = 0
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

# Obliczenie całkowitej ceny za pobyt
total_price = price_per_night * (days - 1)  # Liczba nocy = liczba dni - 1

# Zastosowanie rabatów w zależności od liczby dni
if room_type == "apartment":
    if days < 10:
        total_price *= 0.70  # 30% zniżki
    elif 10 <= days <= 15:
        total_price *= 0.65  # 35% zniżki
    else:
        total_price *= 0.50  # 50% zniżki
elif room_type == "president apartment":
    if days < 10:
        total_price *= 0.90  # 10% zniżki
    elif 10 <= days <= 15:
        total_price *= 0.85  # 15% zniżki
    else:
        total_price *= 0.80  # 20% zniżki

# Ocena pobytu
if grade == "positive":
    total_price *= 1.25  # Dodaj 25%
elif grade == "negative":
    total_price *= 0.90  # Odejmij 10%

# Wynik końcowy
print(f"{total_price:.2f}")
