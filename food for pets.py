# Initialize variables
best_player = ""
most_goals = 0

# Input loop
while True:
    player_name = input()
    if player_name == "END":
        break

    goals = int(input())

    if goals > most_goals:
        most_goals = goals
        best_player = player_name

    # If a player scores 10 or more goals, we end the loop
    if goals >= 10:
        break

# Output
print(f"{best_player} is the best player!")
if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
