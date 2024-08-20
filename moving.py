# Input the dimensions of the free space in the apartment
width = int(input())
length = int(input())
height = int(input())

# Calculate the total volume of free space in cubic meters
total_free_space = width * length * height

# Initialize the total volume of boxes moved
total_boxes_volume = 0

while True:
    # Input the number of boxes or the "Done" command
    command = input()

    if command == "Done":
        # If the command is "Done", calculate the remaining free space
        remaining_space = total_free_space - total_boxes_volume
        print(f"{remaining_space} Cubic meters left.")
        break
    else:
        # Convert the command to an integer (number of boxes)
        boxes = int(command)
        total_boxes_volume += boxes

        # Check if the space has run out
        if total_boxes_volume > total_free_space:
            needed_space = total_boxes_volume - total_free_space
            print(f"No more free space! You need {needed_space} Cubic meters more.")
            break
