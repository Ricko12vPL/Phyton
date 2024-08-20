# # Input the money needed for the vacation and the available money
# money_needed = float(input())
# available_money = float(input())
#
# # Initialize variables to keep track of the necessary details
# total_days = 0
# consecutive_spend_days = 0
#
# while True:
#     # Read the action type (either "spend" or "save")
#     action = input()
#
#     # Read the amount to save or spend
#     amount = float(input())
#
#     # Increment the total number of days
#     total_days += 1
#
#     if action == "spend":
#         # Spend the money, ensuring it doesn't go below zero
#         available_money -= amount
#         if available_money < 0:
#             available_money = 0
#
#         # Increment the consecutive spend days counter
#         consecutive_spend_days += 1
#
#         # Check if Jessie has spent money for 5 consecutive days
#         if consecutive_spend_days == 5:
#             print("You can't save the money.")
#             print(total_days)
#             break
#
#     elif action == "save":
#         # Save the money by adding the amount to the available money
#         available_money += amount
#
#         # Reset the consecutive spend days counter
#         consecutive_spend_days = 0
#
#     # Check if Jessie has saved enough money for the vacation
#     if available_money >= money_needed:
#         print(f"You saved the money for {total_days} days.")
#         break

vacation_cost = float(input())
money = float(input())

consecutive_days_spend = 0
total_days = 0

while True:
    action = input()
    amount = float(input())

    total_days += 1

    if action == "spend":
        consecutive_days_spend += 1
        money -= amount
        if money <0:
            money = 0
        if consecutive_days_spend >= 5:
            print("You can't save the money.")
            print(f"{total_days}")
            break
    elif action == "save":
        consecutive_days_spend = 0
        money += amount

        if money >= vacation_cost:
            print(f"You saved the money for {total_days} days.")
            break



