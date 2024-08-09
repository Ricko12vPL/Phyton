# fruit = input()
# day_of_week = input()
# quantity = float(input())
# price = 0
# days = ["Monday" "Tuesday" "Wednesday" "Thursday" "Friday"]
#
# if day_of_week == days:
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#
#     print(f"{abs(quantity * price):.2f}, Error")
#
# elif day_of_week != "Saturday" or "Sunday":
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#
#     print(f"{abs(quantity * price):.2f}, Error")



fruit = input()
day = input()
quantity = float(input())


switcher_weekdays = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

switcher_weekends = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

total = -1

if (day == "Monday" or
    day == "Tuesday" or
    day == "Wednesday" or
    day == "Thursday" or
    day == "Friday"):
        total = switcher_weekdays.get(fruit, 0) * quantity

elif (day == "Saturday" or
      day == "Sunday"):
        total = switcher_weekends.get(fruit, 0) * quantity
else:
    print("error")

if total == 0:
    print("error")
elif total >0:
    print(f"{total:.2f}")
