max_points = -1
best_movie = ""

for i in range(7):
    title = input().strip()  # Strips any leading/trailing spaces

    if title == "STOP":
        break

    points = 0
    length = len(title)

    for char in title:
        points += ord(char)
        if char.islower():
            points -= 2 * length
        elif char.isupper():
            points -= length

    if points > max_points:
        max_points = points
        best_movie = title

if i == 6 and title != "STOP":  # Checks if the loop ended because of the limit
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")
