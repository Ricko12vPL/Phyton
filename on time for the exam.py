# Dane wejściowe
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Konwersja czasu na minuty od początku dnia
exam_total_minutes = exam_hour * 60 + exam_minute
arrival_total_minutes = arrival_hour * 60 + arrival_minute

# Różnica czasu między przybyciem a egzaminem
time_difference = arrival_total_minutes - exam_total_minutes

# Analiza przybycia
if time_difference > 0:
    print("Late")
    if time_difference >= 60:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{time_difference} minutes after the start")
elif -30 <= time_difference <= 0:
    print("On time")
    if time_difference != 0:
        print(f"{abs(time_difference)} minutes before the start")
else:
    print("Early")
    if abs(time_difference) >= 60:
        hours = abs(time_difference) // 60
        minutes = abs(time_difference) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{abs(time_difference)} minutes before the start")
