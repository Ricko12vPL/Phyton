
# Odczytanie imienia ucznia
student_name = input()

current_grade = 1  # Aktualna klasa ucznia (zaczyna od 1)
total_grades = 0  # Suma ocen
failed_years = 0  # Liczba niezdanych klas

# Pętla do iteracji przez klasy od 1 do 12
while current_grade <= 12:
    annual_grade = float(input())  # Odczytanie rocznej oceny

    if annual_grade < 4.00:
        failed_years += 1  # Uczeń nie zdał roku
        if failed_years > 1:
            # Uczeń został wykluczony
            print(f"{student_name} has been excluded at {current_grade} grade")
            break
    else:
        total_grades += annual_grade  # Dodanie oceny do sumy
        current_grade += 1  # Przejście do następnej klasy

# Jeśli uczeń ukończył wszystkie klasy bez wykluczenia
if current_grade > 12:
    average_grade = total_grades / 12  # Obliczenie średniej ocen
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
