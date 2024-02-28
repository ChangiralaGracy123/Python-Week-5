# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Determine if a Number is Even
# Last changed: 26-02-2024

# Program to Determine if a Number is Even

# Define a function named is_even that accepts an integer as an argument and returns True if the integer is even and False otherwise.
def is_even(number):
    return number % 2 == 0

# Program using the is_even function
# Prompt the user to enter an integer
number = int(input("Enter an integer: "))

# Check if the entered number is even using the is_even function
if is_even(number):
    print("Even")
else:
    print("Odd")

# Description:
# This program defines a function called is_even that determines whether an integer is even or odd.
# It then prompts the user to input an integer and uses the is_even function to check if the entered number is even or odd.
# Finally, it displays the result to the user, indicating whether the number is even or odd.
# This program demonstrates the use of a function to encapsulate a specific task and improve code readability and reusability.




