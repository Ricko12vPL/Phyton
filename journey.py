# Odczyt danych wejściowych
budget = float(input())
season = input()

# Inicjalizacja zmiennych
destination = ""
type_of_holiday = ""
money_spent = 0.0

# Decyzje o miejscu wypoczynku i wydatkach
if budget <= 100:
    destination = "Serbia"
    if season == "summer":
        type_of_holiday = "Camp"
        money_spent = budget * 0.3
    else:  # winter
        type_of_holiday = "Hotel"
        money_spent = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_holiday = "Camp"
        money_spent = budget * 0.4
    else:  # winter
        type_of_holiday = "Hotel"
        money_spent = budget * 0.8
else:  # budget > 1000
    destination = "Europe"
    type_of_holiday = "Hotel"
    money_spent = budget * 0.9

# Formatowanie wydatków do dwóch miejsc po przecinku
money_spent = round(money_spent, 2)

# Wyświetlenie wyników
print(f"Somewhere in {destination}")
print(f"{type_of_holiday} - {money_spent:.2f}")
