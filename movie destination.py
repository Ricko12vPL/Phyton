# Input
budget = float(input())
destination = input()
season = input()
days = int(input())

# Price determination
if destination == "Dubai":
    if season == "Summer":
        price_per_day = 40000
    else:  # Winter
        price_per_day = 45000
    total_price = days * price_per_day * 0.7
elif destination == "Washington":
    if season == "Summer":
        price_per_day = 12500
    else:  # Winter
        price_per_day = 17000
    total_price = days * price_per_day * 1.25
else:  # London
    if season == "Summer":
        price_per_day = 20250
    else:  # Winter
        price_per_day = 24000
    total_price = days * price_per_day

# Output
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {budget - total_price:.2f} USD left!")
else:
    print(f"The director needs {total_price - budget:.2f} USD more!")
