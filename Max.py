# Filename: Max.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Find the Maximum of Two Integers
# Last changed: 26-02-2024

# Program to Find the Maximum of Two Integers
# Define a function named max that accepts two integer values as arguments and returns the value that is the greater of the two.
def max(num1, num2):
    return num1 if num1 > num2 else num2

# Program using the max function
# Prompt the user to enter two integer values
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Call the max function to find the greater number and store the result
greater_number = max(num1, num2)

# Display the result to the user
print("The greater number is:", greater_number)

# Description:
# This program defines a function max that takes two integer arguments and returns the greater of the two.
# Then, it prompts the user to input two integers, calls the max function to find the greater number, and displays the result to the user.