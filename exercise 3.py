# Yvone Nicole B. Perlas | ID: 2023-904
# exercise 3: biography

# To be able to get the inputs of the user we will be using 'input'.
# Within the variable, we use the 'input' function to prompt the user for their data.
firstname = input("First name: ")    # Asks for the user's first name.
surname = input("Surname: ")         # Asks for the user's surname.
hometown = input("Hometown: ")       # Asks for the user's hometown.


while True:
    age = input("Age: ")  
    try:
        age = int(age)  
        break 
    except ValueError:
        print("Invalid, please enter a numeric value.")  

userdata = { 
    "First name": firstname,
    "Surname": surname,
    "Hometown": hometown,
    "Age": age,
}

print(f"First Name: {userdata['First name']}")
print(f"Surname: {userdata['Surname']}")  
print(f"Hometown: {userdata['Hometown']}")  
print(f"Age: {userdata['Age']}")  


