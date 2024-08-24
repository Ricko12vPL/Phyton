# Input: Player names
player1 = input()
player2 = input()

# Initialize points for both players
points_player1 = 0
points_player2 = 0

# Game loop
while True:
    # Input: Card values for each player
    card1 = input()
    if card1 == "End of game":
        break
    card1 = int(card1)

    card2 = int(input())

    # Compare card values
    if card1 > card2:
        points_player1 += card1 - card2
    elif card2 > card1:
        points_player2 += card2 - card1
    else:
        # Number wars situation
        print("Number wars!")
        war_card1 = int(input())
        war_card2 = int(input())

        if war_card1 > war_card2:
            print(f"{player1} is winner with {points_player1} points")
            break
        elif war_card2 > war_card1:
            print(f"{player2} is winner with {points_player2} points")
            break

if card1 == "End of game":
    print(f"{player1} has {points_player1} points")
    print(f"{player2} has {points_player2} points")
