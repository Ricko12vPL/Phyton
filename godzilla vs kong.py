budget = float(input())
extras = int(input())
extras_clothing = float(input())

sum_decor = budget * 0.10
sum_clothing = extras * extras_clothing

if extras > 150:
    sum_clothing = sum_clothing * 0.90

sum_movie = sum_decor + sum_clothing
money_left = budget - sum_movie

if money_left >= 0:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} USD left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} USD more.")
