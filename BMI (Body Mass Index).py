# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to Calculate BMI (Body Mass Index)
# Last changed: 26-02-2024

# Program to Calculate BMI (Body Mass Index)

# Define a function named calculate_bmi that calculates the Body Mass Index (BMI)
# using the weight (in kilograms) and height (in meters) provided as arguments.
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Program using the calculate_bmi function
# Prompt the user to enter weight and height in kilograms and meters respectively
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# Calculate BMI using the calculate_bmi function
bmi = calculate_bmi(weight, height)

# Display the calculated BMI to the user
print("BMI:", bmi)

# Description:
# This program defines a function called calculate_bmi that calculates the Body Mass Index (BMI) using the weight (in kilograms) and height (in meters) provided as arguments.
# The program then prompts the user to enter their weight and height, and calculates the BMI using the calculate_bmi function.
# Finally, it displays the calculated BMI to the user. This program demonstrates the use of a function to encapsulate a specific calculation task and simplify the BMI calculation process.
# It allows users to quickly determine their BMI by inputting their weight and height, helping them monitor their health and fitness levels.