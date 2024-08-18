# Odczyt danych wejściowych
age = int(input())  # Wiek Lily
washing_machine_price = float(input())  # Cena pralki
toy_price = int(input())  # Cena jednej zabawki

# Inicjalizacja zmiennych
money_saved = 0  # Suma zaoszczędzonych pieniędzy
toys_count = 0  # Liczba otrzymanych zabawek
money_received = 0  # Kwota otrzymana na poszczególne urodziny

# Przetwarzanie danych
for i in range(1, age + 1):
    if i % 2 == 0:  # Jeżeli urodziny są parzyste, Lily otrzymuje pieniądze
        money_received += 10
        money_saved += money_received - 1  # Otrzymuje pieniądze minus 1 USD dla brata
    else:  # Jeżeli urodziny są nieparzyste, Lily otrzymuje zabawkę
        toys_count += 1

# Suma pieniędzy za sprzedane zabawki
money_saved += toys_count * toy_price

# Sprawdzanie, czy Lily ma wystarczająco dużo pieniędzy na pralkę
if money_saved >= washing_machine_price:
    print(f"Yes! {money_saved - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money_saved:.2f}")

