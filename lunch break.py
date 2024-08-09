import math

serial_name = str(input())
duration_episode = int(input())
duration_break = int(input())

time_for_lunch = duration_break / 4
time_for_rest = duration_break / 8

remaining_time = duration_break - time_for_lunch - time_for_rest

if remaining_time >= duration_episode:
    print(f"You have enough time to watch {serial_name} and left with {abs(remaining_time - duration_episode):.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(abs(remaining_time - duration_episode)):.0f} more minutes.")
