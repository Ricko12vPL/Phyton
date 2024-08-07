LENGTH_OF_AQUARIUM = int(input())
WIDTH_OF_AQUARIUM = int(input())
HEIGHT_OF_AQUARIUM = int(input())
PERCENTAGE_OF_OCCUPIED_SPACE_IN_AQUARIUM = float(input())

volume_of_aquarium = LENGTH_OF_AQUARIUM * WIDTH_OF_AQUARIUM * HEIGHT_OF_AQUARIUM  # cm3
volume_in_liters = volume_of_aquarium * 0.001
occupied_space = PERCENTAGE_OF_OCCUPIED_SPACE_IN_AQUARIUM / 100
required_liters = volume_in_liters * (1 - occupied_space)

print(required_liters)
