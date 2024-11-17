# Program to find common elements between two sets

# Step 1: Accept user input for two sets of integers
set1_input = input("Enter the first set of integers separated by spaces: ")
set2_input = input("Enter the second set of integers separated by spaces: ")

# Step 2: Convert the input strings into sets of integers
set1 = set(int(num) for num in set1_input.split())
set2 = set(int(num) for num in set2_input.split())

# Step 3: Find the intersection (common elements) between the two sets
common_elements = set1 & set2  # You can also use set1.intersection(set2)

# Step 4: Display the result
print(f"The common elements between the two sets are: {common_elements}")
