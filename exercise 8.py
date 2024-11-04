# Yvone Nicole B. Perlas | ID: 2023-904
# exercise 8: simple search

# This acts as our library of people which is a variable prompt.
namesofpeople = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# This displays the question that asks for the name of the person.
search_term = input("Enter the name you want to search for: ")

# Convert search term to lowercase to allow case-insensitive comparison.
search_term = search_term.lower()

# Initialize a variable to track if the name is found.
found = False

# Create a search loop that iterates through each name in the list inside namesofpeople.
for name in namesofpeople:
    # Convert each name to lowercase and compare with the search term.
    if name.lower() == search_term:
        found = True
        break  # Exit the loop once the name is found.

# Print the result based on whether the name was found or not.
if found:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")
