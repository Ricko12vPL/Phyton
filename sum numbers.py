# Odczytanie liczby początkowej
target_sum = int(input())

# Inicjalizacja zmiennej do przechowywania sumy
current_sum = 0

# Pętla do odczytu liczb i sumowania ich
while current_sum < target_sum:
    number = int(input())  # Odczytanie liczby od użytkownika
    current_sum += number  # Dodanie liczby do sumy

# Wyświetlenie końcowej sumy
print(current_sum)
