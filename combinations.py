def count_combinations(n):
    count = 0
    for x1 in range(n + 1):       # Iterate x1 from 0 to n
        for x2 in range(n + 1):   # Iterate x2 from 0 to n
            x3 = n - x1 - x2      # Calculate x3 as the difference needed to reach n
            if x3 >= 0:           # Ensure x3 is non-negative
                count += 1        # Valid combination found, increment count
    print(count)

# Example usage:
n = int(input())
count_combinations(n)
