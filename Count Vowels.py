# Filename: Count Vowels.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Count Vowels in a Text String
# Last changed: 26-02-2024

# Program to Count Vowels in a Text String

# Define a function named count_vowels that takes a text string as an argument and returns a count of all the vowels in the string.
def count_vowels(text):
    # Define a string containing all the vowels, both lowercase and uppercase
    vowels = "aeiouAEIOU"
    count = 0  # Initialize a variable to count the number of vowels
    # Iterate through each character in the text string
    for char in text:
        # Check if the character is a vowel
        if char in vowels:
            count += 1  # Increment the count if the character is a vowel
    return count  # Return the total count of vowels in the text

# Program using the count_vowels function
# Prompt the user to enter a text string
text = input("Enter a text string: ")
# Call the count_vowels function to count the vowels in the entered text
vowel_count = count_vowels(text)
# Display the number of vowels in the entered text to the user
print("Number of vowels:", vowel_count)

# Description:
# This program defines a function count_vowels that takes a text string as input and returns the count of vowels in the string.
# Then, it prompts the user to input a text string, calls the count_vowels function to count the vowels, and displays the count to the user.