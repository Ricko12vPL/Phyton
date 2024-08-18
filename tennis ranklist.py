import math

# Odczyt liczby turniejów i początkowej liczby punktów
number_of_tournaments = int(input())
initial_points = int(input())

# Inicjalizacja zmiennych
total_points = initial_points
points_earned = 0
wins = 0

# Przetwarzanie wyników każdego turnieju
for _ in range(number_of_tournaments):
    result = input()

    if result == "W":
        points_earned += 2000
        wins += 1
    elif result == "F":
        points_earned += 1200
    elif result == "SF":
        points_earned += 720

# Obliczanie końcowej liczby punktów
total_points += points_earned

# Obliczanie średniej liczby punktów na turniej
average_points = points_earned / number_of_tournaments

# Obliczanie procentu wygranych turniejów
win_percentage = (wins / number_of_tournaments) * 100

# Wyświetlanie wyników
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{win_percentage:.2f}%")
