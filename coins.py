# Input the change amount
change = float(input())

# Convert the change to cents to avoid floating-point precision issues
cents = round(change * 100)

# Define the coin denominations in cents
coins = [200, 100, 50, 20, 10, 5, 2, 1]

# Initialize the counter for the number of coins used
coin_count = 0

# Iterate over each coin denomination
for coin in coins:
    # Determine how many coins of this denomination can be used
    if cents >= coin:
        coin_count += cents // coin
        cents %= coin

# Output the number of coins used
print(coin_count)
