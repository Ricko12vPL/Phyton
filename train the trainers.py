def train_the_trainers():
    # Pobierz liczbę osób w jury
    jury_count = int(input())

    # Inicjalizacja zmiennych
    total_sum_grades = 0
    total_num_grades = 0

    while True:
        # Pobierz nazwę prezentacji
        presentation_name = input()

        # Sprawdź, czy użytkownik chce zakończyć program
        if presentation_name == "Finish":
            break

        # Inicjalizacja zmiennej do sumowania ocen dla danej prezentacji
        sum_grades = 0

        # Pobierz oceny dla danej prezentacji
        for _ in range(jury_count):
            grade = float(input())
            sum_grades += grade

        # Oblicz średnią ocen dla danej prezentacji
        average_grade = sum_grades / jury_count
        print(f"{presentation_name} - {average_grade:.2f}.")

        # Dodaj oceny do ogólnych sum
        total_sum_grades += sum_grades
        total_num_grades += jury_count

    # Oblicz i wypisz ogólną średnią ocenę
    final_assessment = total_sum_grades / total_num_grades
    print(f"Student's final assessment is {final_assessment:.2f}.")


# Przykład użycia
train_the_trainers()
