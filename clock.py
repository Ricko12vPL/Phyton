def print_clock():
    for hour in range(24):       # Loop through each hour from 0 to 23
        for minute in range(60): # Loop through each minute from 0 to 59
            print(f"{hour}:{minute}")  # Print in "hours:minutes" format

# Call the function to print the clock
print_clock()
