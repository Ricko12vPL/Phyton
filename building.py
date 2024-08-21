def print_room_numbers(floors, rooms_per_floor):
    for floor in range(floors, 0, -1):  # Pętla po piętrach od najwyższego do najniższego
        for room in range(rooms_per_floor):  # Pętla po pokojach na danym piętrze
            if floor == floors:  # Jeśli to najwyższe piętro
                print(f"L{floor}{room}", end=" ")
            elif floor % 2 == 0:  # Jeśli piętro jest parzyste (biura)
                print(f"O{floor}{room}", end=" ")
            else:  # Jeśli piętro jest nieparzyste (apartamenty)
                print(f"A{floor}{room}", end=" ")
        print()  # Nowa linia po zakończeniu wypisywania wszystkich pokoi na danym piętrze

# Przykłady użycia:
floors = int(input())
rooms_per_floor = int(input())
print_room_numbers(floors, rooms_per_floor)
