fruit = input()
set_size = input()
number_of_orders = int(input())

small_set_size = number_of_orders * 2
big_set_size = number_of_orders * 5

price_set = 0

if set_size == "big":
    if fruit == "Watermelon":
        price_set = big_set_size * 28.70 #Watermelon price big for pc.
    elif fruit == "Mango":
        price_set = big_set_size * 19.60 #Mango price big for pc.
    elif fruit == "Pineapple":
        price_set = big_set_size * 24.80 #Pineapple price bigfor pc.
    elif fruit == "Raspberry":
        price_set = big_set_size * 15.20 #Raspberry price big for pc.

elif set_size == "small":
    if fruit == "Watermelon":
        price_set = small_set_size * 56 #Watermelon price small for pc.
    elif fruit == "Mango":
        price_set = small_set_size * 36.66 #Mango price small for pc.
    elif fruit == "Pineapple":
        price_set = small_set_size * 42.10 #Pineapple price small for pc.
    elif fruit == "Raspberry":
        price_set = small_set_size * 20 #Raspberry price small for pc.


if 400 <= price_set <= 1000:  #discount
    price_set *= 0.85
elif price_set >= 1000:  # discount
    price_set *= 0.50

print(f"{price_set:.2f} USD.")

