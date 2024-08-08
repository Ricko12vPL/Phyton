price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

input_trip_cost = float(input())
input_puzzle = int(input())
input_doll = int(input())
input_bear = int(input())
input_minion = int(input())
input_truck = int(input())


total_toys = input_puzzle + input_doll + input_bear + input_minion + input_truck
total_price = input_puzzle * price_puzzle + input_doll * price_doll + input_bear * price_bear + input_minion * price_minion + input_truck * price_truck
discount = 0

if total_toys >= 50:
    final_price = total_price * 0.75
else:
    final_price = total_price

profit = final_price * 0.9
money_left = profit - input_trip_cost

if money_left >= 0:
    print(f"Yes! {money_left:.2f} USD left.")
else:
    print(f"Not enough money! {abs(money_left):.2f} USD needed.")




