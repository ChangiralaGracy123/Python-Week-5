# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Validate Password
# Last changed: 26-02-2024

# Program to Validate Password

# Define a function named validate_password that accepts a password as input and validates it according to specific rules:
# - At least eight characters long
# - Includes at least one uppercase and one lowercase letter
# - Includes at least one digit
def validate_password(password):
    # Check if the password length is less than 8 characters
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    has_upper = any(char.isupper() for char in password)

    # Check if the password contains at least one lowercase letter
    has_lower = any(char.islower() for char in password)

    # Check if the password contains at least one digit
    has_digit = any(char.isdigit() for char in password)

    # Return True if all conditions are met, False otherwise
    return has_upper and has_lower and has_digit


# Program to check password validity
while True:
    password = input("Enter a password: ")  # Prompt the user to enter a password
    # Check if the entered password is valid using the validate_password function
    if validate_password(password):
        print("Password is valid!")  # Display a message indicating a valid password
        break  # Exit the loop if a valid password is entered
    else:
        print("Password is invalid. Please try again.")  # Prompt the user to try again if the password is invalid

# Description:
# This program defines a function called validate_password that validates a password based on specific criteria:
# it must be at least eight characters long and contain at least one uppercase letter, one lowercase letter, and one digit.
# The program continuously prompts the user to enter a password and checks its validity using the validate_password function.
# If the entered password meets all the criteria, the program displays a message indicating that it is valid and exits the loop.
# If the password is invalid, the program prompts the user to try again until a valid password is entered.
# This program demonstrates how to enforce password security by validating passwords against specific requirements.