# Program to store information about a person in a dictionary

# Step 1: Create an empty dictionary to store the information
person_info = {}

# Step 2: Ask the user for input and store it in the dictionary
person_info["name"] = input("Enter your name: ")
person_info["age"] = int(input("Enter your age: "))
person_info["favorite_color"] = input("Enter your favorite color: ")

# Step 3: Print the dictionary to the console
print("\nPerson Information:")
print(person_info)
