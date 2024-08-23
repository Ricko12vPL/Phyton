# Input
budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_costs_percentage = int(input())

# Discount if more than 7 nights
if nights > 7:
    price_per_night *= 0.95

total_cost = (nights * price_per_night) + (budget * additional_costs_percentage / 100)

# Output
if budget >= total_cost:
    print(f"Smiths will be left with {budget - total_cost:.2f} USD after vacation.")
else:
    print(f"{total_cost - budget:.2f} USD needed.")
