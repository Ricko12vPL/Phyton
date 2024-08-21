def main():
    while True:
        destination = input()  # Read the destination or 'End'
        if destination == "End":
            break

        # Read the minimum budget required for the destination
        budget = float(input())
        saved_amount = 0

        # Loop to accumulate savings until the budget is met
        while saved_amount < budget:
            saving = float(input())
            saved_amount += saving

        # Print the result once the budget is met
        print(f"Going to {destination}!")


# Run the program
main()
