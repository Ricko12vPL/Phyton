max_num = None  # Zmienna do przechowywania największej liczby

while True:
    user_input = input()  # Odczytaj dane wejściowe od użytkownika

    if user_input == "Stop":  # Sprawdź, czy wpisano "Stop"
        break

    num = int(user_input)  # Przekonwertuj dane wejściowe na liczbę całkowitą

    if max_num is None or num > max_num:  # Zaktualizuj największą liczbę, jeśli to konieczne
        max_num = num

# Po zakończeniu pętli wyświetl największą liczbę
print(max_num)
