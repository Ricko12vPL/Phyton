
PRICE_OF_TRAINING = int(input())
PRICE_OF_SNEAKERS = PRICE_OF_TRAINING - (PRICE_OF_TRAINING * 0.40) # -40% LESS  365 - (365 * 0.40)
PRICE_OF_OUTFIT = PRICE_OF_SNEAKERS - (PRICE_OF_SNEAKERS * 0.20)   # -20% LESS
PRICE_OF_BALL = PRICE_OF_OUTFIT * 0.25       # 1/4 LESS
PRICE_OF_ACCESSORIES = PRICE_OF_BALL * 0.20  # 1/5 LESS

total_cost = PRICE_OF_TRAINING + PRICE_OF_SNEAKERS + PRICE_OF_OUTFIT + PRICE_OF_BALL + PRICE_OF_ACCESSORIES


print(total_cost)
