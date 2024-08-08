import math

record = float(input())
distance = float(input())
seconds_per_metre = float(input())

total_seconds = distance * seconds_per_metre
delay = math.floor(distance / 15) * 12.5

total_time = total_seconds + delay

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record - total_time):.2f} seconds slower.")