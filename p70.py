from itertools import permutations

# Input 3 or 4 characters
input_string = input("Enter 3 or 4 characters: ")

# Generate all permutations of the input string
combinations = permutations(input_string)

# Print all combinations
for combo in combinations:
    print(''.join(combo))
