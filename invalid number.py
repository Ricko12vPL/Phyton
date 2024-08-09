num = int(input())

is_valid = (num >= 100 and num <= 200) or num == 0

if not is_valid:
    print("invalid")
