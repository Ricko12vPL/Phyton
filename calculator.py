deposit_amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

annual_interest_rate_percentage = annual_interest_rate / 100
interest_total = deposit_amount * annual_interest_rate_percentage
interest_one_month = interest_total / 12

amount = deposit_amount + deposit_term * interest_one_month

print(amount)
