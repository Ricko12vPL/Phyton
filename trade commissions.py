city = str(input())
sales = float(input())

if city == "London":
    commission = 0

    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        print("error")

    print(f"{commission:.2f}")
elif city == "Paris":
    commission = 0

    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
    else:
        print("error")

    print(f"{commission:.2f}")
elif city == "Rome":
    commission = 0

    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        print("error")

    if not (commission <= 0):
        print(f"{commission:.2f}")
else:
    print("error")

