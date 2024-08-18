# Odczyt danych wejściowych
n = int(input())  # Liczba otwartych kart
salary = int(input())  # Pensja

# Przetwarzanie każdej karty
for _ in range(n):
    website = input()  # Nazwa strony internetowej

    # Sprawdzanie nazwy strony i odejmowanie odpowiedniej kary
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    # Sprawdzanie, czy pensja spadła do zera lub poniżej
    if salary <= 0:
        print("You have lost your salary.")
        break

# Jeśli pensja jest większa niż 0, wyświetl pozostałą kwotę
if salary > 0:
    print(salary)
