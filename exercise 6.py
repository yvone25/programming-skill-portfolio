# Yvone Nicole B. Perlas | ID: 2023-904
# exercise 6: correct password

# This is the variable that holds the correct password.
correct_password = "_nicole0306_"

# The while True function loops until the correct password is inputted.
while True:
    # Ask the user to input the password
    password_input = input("Enter the password: ")
    
    # Check if the input corresponds to the correct password
    if password_input == correct_password:
        print("Correct password!")
        break  # Exit the loop once the correct password has been inputted
    else:
        print("Incorrect password. Please try again.")

