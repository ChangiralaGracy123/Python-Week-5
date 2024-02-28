# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Calculate Hamming Distance
# Last changed: 26-02-2024

# Program to Calculate Hamming Distance

# Define a function named hamming_distance that calculates the Hamming distance between two strings, which is the number of corresponding characters or symbols that differ in the two strings.
def hamming_distance(str1, str2):
    # Check if the lengths of the strings are not equal
    if len(str1) != len(str2):
        return "Error: Strings are not of equal length"

    distance = 0  # Initialize the Hamming distance counter

    # Iterate through each character in the strings using enumerate
    for i, ch in enumerate(str1):
        # Compare corresponding characters in the two strings
        if ch != str2[i]:
            distance += 1  # Increment the distance if characters are different

    return distance  # Return the Hamming distance


# Program using the hamming_distance function
# Prompt the user to enter two strings of equal length
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Calculate and display the Hamming distance between the two strings
print("Hamming distance:", hamming_distance(str1, str2))

# Description:
# This program defines a function called hamming_distance that calculates the Hamming distance between two strings.
# The Hamming distance is the number of corresponding characters or symbols that differ in the two strings.
# The program prompts the user to enter two strings of equal length and then calculates and displays the Hamming distance between them using the hamming_distance function.
# If the entered strings are not of equal length, the program returns an error message indicating that the strings are not comparable.
# This program demonstrates how to implement a function to perform a specific task and use it in a program to analyze and compare strings.
