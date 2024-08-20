total_amount = 0.0  # Początkowa suma pieniędzy na koncie

while True:
    amount = input()  # Odczytaj kwotę od użytkownika

    if amount == "NoMoreMoney":  # Jeśli użytkownik wpisze "NoMoreMoney", zakończ pętlę
        break

    amount = float(amount)  # Przekonwertuj kwotę na liczbę zmiennoprzecinkową

    if amount < 0:  # Jeśli kwota jest mniejsza niż 0, zakończ program z komunikatem o błędzie
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")  # Wyświetl komunikat o zwiększeniu konta
    total_amount += amount  # Dodaj kwotę do całkowitej sumy na koncie

print(f"Total: {total_amount:.2f}")  # Wyświetl całkowitą sumę pieniędzy na koncie, sformatowaną do dwóch miejsc po przecinku
