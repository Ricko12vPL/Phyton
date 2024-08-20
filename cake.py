# Input the dimensions of the cake
width = int(input())
length = int(input())

# Calculate the total number of pieces of the cake
total_pieces = width * length

# Initialize the number of pieces taken
pieces_taken = 0

while True:
    # Input the number of pieces taken or the "STOP" command
    command = input()

    if command == "STOP":
        # If the command is STOP, calculate the remaining pieces
        print(f"{total_pieces - pieces_taken} pieces are left.")
        break
    else:
        # Convert the command to an integer (number of pieces taken)
        pieces_taken += int(command)

        # Check if all pieces have been taken
        if pieces_taken >= total_pieces:
            print(f"No more cake left! You need {pieces_taken - total_pieces} pieces more.")
            break
