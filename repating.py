# EXTRA_NYLON = 2
# EXTRA_PAINT_PERCENTAGE = 1.10
# COSTS_PERCENTAGE = 0.30
# SUM_BAGS = 0.40
#
#
# sum_nylon = (int(input()) + EXTRA_NYLON) * 1.50
# sum_paint = (int(input()) * EXTRA_PAINT_PERCENTAGE) * 14.50
# sum_detergent = int(input()) * 5.00
# hours = int(input())
#
# total_sum_for_materials = sum_nylon + sum_paint + sum_detergent + SUM_BAGS
# total_sum_for_workers = (total_sum_for_materials * COSTS_PERCENTAGE) * hours
# total_sum = total_sum_for_workers + total_sum_for_workers
#
# print(total_sum)

# Constants for extra materials and costs
EXTRA_NYLON = 2
EXTRA_PAINT_PERCENTAGE = 1.10
COSTS_PERCENTAGE = 0.30
SUM_BAGS = 0.40

# Prices
PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_DETERGENT = 5.00

# Reading inputs
required_nylon = int(input())  # Required amount of nylon in square meters
required_paint = int(input())  # Required amount of paint in liters
required_detergent = int(input())  # Quantity of detergent in liters
hours = int(input())  # Hours for which the workers will do the work

# Calculating the costs of materials
sum_nylon = (required_nylon + EXTRA_NYLON) * PRICE_NYLON
sum_paint = (required_paint * EXTRA_PAINT_PERCENTAGE) * PRICE_PAINT
sum_detergent = required_detergent * PRICE_DETERGENT

# Total cost for materials
total_sum_for_materials = sum_nylon + sum_paint + sum_detergent + SUM_BAGS

# Total cost for workers
total_sum_for_workers = (total_sum_for_materials * COSTS_PERCENTAGE) * hours

# Final total cost
total_sum = total_sum_for_materials + total_sum_for_workers

# Output the result
print(total_sum)
