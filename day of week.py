day = int(input())

switcher = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
    -1: "Error"
}

print(switcher.get(day, "Error"))
