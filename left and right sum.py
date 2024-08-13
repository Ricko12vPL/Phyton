# Odczyt liczby n
n = int(input())

# Inicjalizacja sum
left_sum = 0
right_sum = 0

# Pętla iterująca przez pierwsze n liczb (lewa suma)
for i in range(n):
    num = int(input())
    left_sum += num

# Pętla iterująca przez drugie n liczb (prawa suma)
for i in range(n):
    num = int(input())
    right_sum += num

# Porównanie sum
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
