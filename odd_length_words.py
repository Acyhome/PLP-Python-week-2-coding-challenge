# Program to filter words with an odd number of characters

# Step 1: Create a list of words
words = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Step 2: Use list comprehension to filter words with odd lengths
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Step 3: Display the result
print(f"Words with an odd number of characters: {odd_length_words}")
