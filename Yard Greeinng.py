square_meters = float(input())
square_meters_price = square_meters * 7.61
discount = square_meters_price * 0.18
final_price = square_meters_price - discount

print(f"The final price is: {final_price} USD.")
print(f"The discount is: {discount} USD.")