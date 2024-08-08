# hours = int(input())
# minutes = int(input())
#
# minutes += 15
# if hours >= 60:
#     minutes -= 60
#     hours += 1
#
# if hours >= 24:
#     hours = 0
#
# if minutes < 10:
#     print(f'{hours}:0{minutes}')
# else:
#     print(f'{hours}:{minutes}')

hours = int(input())
minutes = int(input())

if minutes + 15 > 59:
    hours = hours + 1
    minutes = (minutes + 15) % 60
else:
    hours = hours
    minutes = minutes + 15

if hours == 24:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
