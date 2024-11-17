# Program to compute the sum of integers in a list

# Step 1: Accept user input for a list of integers
user_input = input("Enter a list of integers separated by spaces: ")

# Step 2: Convert the input string into a list of integers
numbers = [int(num) for num in user_input.split()]

# Step 3: Compute the sum of all integers in the list
total_sum = sum(numbers)

# Step 4: Display the result
print(f"The sum of the integers in the list is: {total_sum}")
