# Odczyt tekstu od użytkownika
text = input()

# Inicjalizacja zmiennej sumy
vowel_sum = 0

# Przypisanie wartości do poszczególnych samogłosek
vowel_values = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

# Iteracja przez każdy znak w tekście
for char in text:
    if char in vowel_values:
        vowel_sum += vowel_values[char]  # Dodanie wartości samogłoski do sumy

# Wyświetlenie wyniku
print(vowel_sum)
