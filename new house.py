Flowers = input()
Number_of_flowers = int(input())
Budget = int(input())

price_roses = 5
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3
price_gladiolus = 2.50

price_total = 0

if Flowers == "Roses:":
    price_total = Flowers * price_roses
    if Flowers > 80:
        price_total *= 0.90
elif Flowers == "Dahlias:":
    price_total = Flowers * price_dahlias
    if Flowers > 90:
        price_total *= 0.85
elif Flowers == "Tulips:":
    price_total = Flowers * price_tulips
    if Flowers > 80:
        price_total *= 0.85
elif Flowers == "Narcissus:":
    price_total = Flowers * price_narcissus
    if Flowers > 120:
        price_total *= 1.15
elif Flowers == "Gladiolus:":
    price_total = Flowers * price_gladiolus
    if Flowers > 120:
        price_total *= 1.20


money_left = Budget - price_total
has_enough_money = money_left >= 0

if has_enough_money:
    print(f"Hey, you have a great garden with {Number_of_flowers} {Flowers} and {money_left:.2f} USD left.")
else:
    print(f"Not enough money, you need {abs(money_left):.2f} USD more.")


# Odczyt danych wejściowych
flower_type = input()
flower_count = int(input())
budget = int(input())

# Inicjalizacja cen dla poszczególnych typów kwiatów
price_per_flower = 0

if flower_type == "Roses":
    price_per_flower = 5
    if flower_count > 80:
        price_per_flower *= 0.9  # 10% zniżki
elif flower_type == "Dahlias":
    price_per_flower = 3.80
    if flower_count > 90:
        price_per_flower *= 0.85  # 15% zniżki
elif flower_type == "Tulips":
    price_per_flower = 2.80
    if flower_count > 80:
        price_per_flower *= 0.85  # 15% zniżki
elif flower_type == "Narcissus":
    price_per_flower = 3
    if flower_count < 120:
        price_per_flower *= 1.15  # 15% podwyżki
elif flower_type == "Gladiolus":
    price_per_flower = 2.50
    if flower_count < 80:
        price_per_flower *= 1.20  # 20% podwyżki

# Obliczenie całkowitego kosztu
total_cost = flower_count * price_per_flower

# Sprawdzenie, czy budżet jest wystarczający
difference = budget - total_cost

# Wyświetlenie wyniku
if difference >= 0:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} USD left.")
else:
    print(f"Not enough money, you need {abs(difference):.2f} USD more.")
