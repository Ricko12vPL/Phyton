def multiplication_table():
    for i in range(1, 11):        # Loop through the first multiplier from 1 to 10
        for j in range(1, 11):    # Loop through the second multiplier from 1 to 10
            result = i * j        # Calculate the result of the multiplication
            print(f"{i} * {j} = {result}")  # Print the multiplication in the format "i * j = result"

# Call the function to print the multiplication table
multiplication_table()
