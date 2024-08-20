# Define the goal for daily steps
goal_steps = 10000

# Initialize a counter for the total number of steps taken
total_steps = 0

while True:
    # Input the number of steps taken or the command "Going home"
    command = input()

    if command == "Going home":
        # Input the number of steps taken while going home
        steps_going_home = int(input())
        total_steps += steps_going_home
        break
    else:
        # Convert the command to integer (steps) and add to total steps
        steps = int(command)
        total_steps += steps

    # Check if the goal has been reached
    if total_steps >= goal_steps:
        print("Goal reached! Good job!")
        print(f"{total_steps - goal_steps} steps over the goal!")
        break

# If the loop ends without reaching the goal, check if the total steps are below the goal
if total_steps < goal_steps:
    print(f"{goal_steps - total_steps} more steps to reach the goal.")
