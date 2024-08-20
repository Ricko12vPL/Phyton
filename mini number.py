min_num = None  # Zmienna do przechowywania najmniejszej liczby

while True:
    user_input = input()  # Odczytaj dane wejściowe od użytkownika

    if user_input == "Stop":  # Sprawdź, czy wpisano "Stop"
        break

    num = int(user_input)  # Przekonwertuj dane wejściowe na liczbę całkowitą

    if min_num is None or num < min_num:  # Zaktualizuj najmniejszą liczbę, jeśli to konieczne
        min_num = num

# Po zakończeniu pętli wyświetl najmniejszą liczbę
print(min_num)
