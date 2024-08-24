budget = float(input())
n = int(input())

discounts = {
    "Thrones": 0.5,
    "Lucifer": 0.4,
    "Protector": 0.3,
    "TotalDrama": 0.2,
    "Area": 0.1
}

total_price = 0

for _ in range(n):
    name = input()
    price = float(input())

    if name in discounts:
        price -= price * discounts[name]

    total_price += price

if budget >= total_price:
    print(f"You bought all the series and left with {budget - total_price:.2f} USD.")
else:
    print(f"You need {total_price - budget:.2f} USD. more to buy the series!")
