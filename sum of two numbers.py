def find_magic_combination(start, end, magic_number):
    combination_count = 0

    # Iterate over all possible pairs of numbers in the interval [start, end]
    for first_num in range(start, end + 1):
        for second_num in range(start, end + 1):
            combination_count += 1
            if first_num + second_num == magic_number:
                # Print the first combination that meets the criteria
                print(f"Combination N:{combination_count} ({first_num} + {second_num} = {magic_number})")
                return

    # If no valid combination is found, print the total combinations checked
    print(f"{combination_count} combinations - neither equals {magic_number}")


# Example usage:
start = int(input())
end = int(input())
magic_number = int(input())

find_magic_combination(start, end, magic_number)
