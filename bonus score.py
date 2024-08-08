num = int(input())
bonus = 0

if num <= 100:
    bonus = 5
elif num > 100 and num <= 1000:
    bonus = num * 0.2
elif num > 1000:
    bonus = num * 0.1

is_even = num % 2 == 0
num_ends_with_5 = num % 10 == 5

if is_even:
    bonus = bonus + 1
elif num_ends_with_5:
    bonus = bonus + 2

print(bonus)
print(bonus + num)
