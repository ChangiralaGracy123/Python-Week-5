# Filename: Count Vowels.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Check Palindrome
# Last changed: 26-02-2024

# Program to Check Palindrome

# Define a function named is_palindrome that accepts a text string as input and determines whether or not the text string is a palindrome.
def is_palindrome(text):
    text = text.lower()  # Convert text to lowercase
    reverse_text = text[::-1]  # Reverse the text string
    # Check if the original text string is equal to its reverse
    return text == reverse_text

# Program using the is_palindrome function
# Prompt the user to enter a word or phrase
word = input("Enter a word or phrase: ")
# Call the is_palindrome function to check if the entered text is a palindrome
if is_palindrome(word):
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome.")

# Description:
# This program defines a function is_palindrome that checks whether a given text string is a palindrome (reads the same forwards and backwards).
# It then prompts the user to input a word or phrase, calls the is_palindrome function to check if the entered text is a palindrome, and displays the result to the user.