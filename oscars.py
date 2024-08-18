# Odczyt danych wejściowych
actor_name = input()  # Nazwa aktora/aktorki
academy_points = float(input())  # Początkowe punkty od akademii
n = int(input())  # Liczba asesorów

# Przetwarzanie każdej oceny asesora
for i in range(n):
    assessor_name = input()  # Nazwa asesora
    assessor_score = float(input())  # Ocena asesora

    # Obliczanie punktów przyznanych przez asesora
    points = (len(assessor_name) * assessor_score) / 2
    academy_points += points

    # Sprawdzanie, czy punkty przekroczyły 1250.5
    if academy_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    # Jeśli pętla zakończyła się bez przekroczenia progu 1250.5 punktów
    needed_points = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
