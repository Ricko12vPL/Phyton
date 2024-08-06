sum_pens = int(input()) * 5.80
sum_markers = int(input()) * 7.20
sum_detergents = int(input()) * 1.20
discount = int(input())

amount = sum_pens + sum_markers + sum_detergents
amount_after_discount = amount - (amount * (discount / 100))


print(amount_after_discount)
