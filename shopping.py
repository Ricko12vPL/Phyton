# budget = float(input())
# num_video_cards = int(input())
# num_cpu = int(input())
# num_ram = int(input())
# discount = 0.15
#
# price_video_cards = 250
# price_cpu = (num_video_cards * price_video_cards) * 0.35
# price_ram = (num_video_cards * price_video_cards) * 0.10
#
# cost_of_video_cards = num_video_cards * price_video_cards
# cost_of_cpu = num_cpu * price_cpu
# cost_of_ram = num_ram * price_ram
#
# total_sum = cost_of_video_cards + cost_of_cpu + cost_of_ram
# budget_left = total_sum - (total_sum * discount)
# money_left = budget - budget_left
#
# if num_video_cards <= num_cpu:
#     budget_left = total_sum - (total_sum * discount)
#
# if total_sum <= budget:
#     print(f"You have {money_left:.2f} USD left!")
# elif total_sum > budget:
#     print(f"Not enough money! You need {abs(money_left):.2f} USD more!")


budget = float(input())
num_video_cards = int(input())
num_cpu = int(input())
num_ram = int(input())

# Ceny poszczególnych komponentów
price_video_cards = 250
price_cpu = (num_video_cards * price_video_cards) * 0.35
price_ram = (num_video_cards * price_video_cards) * 0.10

# Koszty wszystkich komponentów
cost_of_video_cards = num_video_cards * price_video_cards
cost_of_cpu = num_cpu * price_cpu
cost_of_ram = num_ram * price_ram

# Suma całkowita przed zniżką
total_sum = cost_of_video_cards + cost_of_cpu + cost_of_ram

# Zastosowanie zniżki, jeśli liczba kart graficznych jest większa niż liczba procesorów
if num_video_cards > num_cpu:
    total_sum *= 0.85  # Rabat 15%

# Obliczenie pozostałego budżetu
money_left = budget - total_sum

# Wyświetlenie odpowiedniego komunikatu
if money_left >= 0:
    print(f"You have {money_left:.2f} USD left!")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} USD more!")
