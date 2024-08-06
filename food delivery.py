
PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEG_MENU = 8.15
PRICE_DELIVERY = 2.50
PERCENTAGE_PRICE_DESERT = 0.20


sum_chicken_menus = int(input()) * PRICE_CHICKEN_MENU
sum_fish_menus = int(input()) * PRICE_FISH_MENU
sum_veg_menus = int(input()) * PRICE_VEG_MENU

sum_menus = sum_chicken_menus + sum_fish_menus + sum_veg_menus
price_dessert = sum_menus * PERCENTAGE_PRICE_DESERT
price_delivery = PRICE_DELIVERY

total = sum_menus + price_dessert + PRICE_DELIVERY

print(total)
