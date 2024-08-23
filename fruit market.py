# Input
price_strawberries = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

# Calculations
price_raspberries = price_strawberries / 2
price_oranges = price_raspberries - 0.4 * price_raspberries
price_bananas = price_raspberries - 0.8 * price_raspberries

total_cost = (price_strawberries * strawberries_kg) + (price_raspberries * raspberries_kg) + (price_oranges * oranges_kg) + (price_bananas * bananas_kg)

# Output
print(f"{total_cost:.2f}")
