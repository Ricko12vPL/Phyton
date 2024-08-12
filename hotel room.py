# Odczyt danych wejściowych
month = input()
nights = int(input())

# Ustalanie cen za noc w zależności od miesiąca
if month in ["May", "October"]:
    studio_price = 50
    apartment_price = 65
elif month in ["June", "September"]:
    studio_price = 75.20
    apartment_price = 68.70
elif month in ["July", "August"]:
    studio_price = 76
    apartment_price = 77

# Zastosowanie zniżek dla studio
if month in ["May", "October"]:
    if nights > 14:
        studio_price *= 0.70
    elif nights > 7:
        studio_price *= 0.95
elif month in ["June", "September"] and nights > 14:
    studio_price *= 0.80

# Zastosowanie zniżki dla apartamentu
if nights > 14:
    apartment_price *= 0.90

# Obliczenie całkowitej ceny za pobyt
studio_total = studio_price * nights
apartment_total = apartment_price * nights

# Wyświetlenie wyników
print(f"Apartment: {apartment_total:.2f} USD.")
print(f"Studio: {studio_total:.2f} USD.")
