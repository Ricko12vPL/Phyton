# Pobieramy dane wejściowe
start = int(input())
end = int(input())

# Konwertujemy liczby na stringi, aby łatwiej iterować przez każdą cyfrę
start_str = str(start)
end_str = str(end)

# Iterujemy przez wszystkie liczby w podanym zakresie
for i in range(int(start_str[0]), int(end_str[0]) + 1):
    for j in range(int(start_str[1]), int(end_str[1]) + 1):
        for k in range(int(start_str[2]), int(end_str[2]) + 1):
            for l in range(int(start_str[3]), int(end_str[3]) + 1):
                # Sprawdzamy, czy wszystkie cyfry są nieparzyste
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    # Jeśli tak, tworzymy i wypisujemy kod kreskowy
                    print(f"{i}{j}{k}{l}", end=" ")
