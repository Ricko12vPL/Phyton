walk_duration = int(input())
walk_days = int(input())
cat_calories_taken = int(input())

cat_calories_burn = 5 # for every minutes
calories_enough = cat_calories_taken / 2

total_walk_time = walk_duration * walk_days # in minutes
total_burned_calories_per_day = total_walk_time * cat_calories_burn

if total_burned_calories_per_day >= calories_enough:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories_per_day}.")

