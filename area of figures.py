import math

figure = input()

if figure == "square":
    side = float(input())
    area = side * side

    print(f"{area:.3f}")

elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2

    print(f"{area:.3f}")

elif figure == "circle":
    radius = float(input())
    area = math.pi * radius * radius

    print(f"{area:.3f}")

elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2

    print(f"{area:.3f}")

else:
    print("Figure not found...")