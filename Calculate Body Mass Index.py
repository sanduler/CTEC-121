# Task 1: Simple Pay Program
# Author: Ruben Sanduleac
# Date: October 9th 2021
# Discription: This program calculates the BMI


# Define a function called main
def main():
    
    #variables
    factorWeight = 0.45359237
    heightFactor = 0.0254

    # prints the title of the program
    print("\nCalculate BMI\n")
    Weight = float(input("Enter your weight in pounds: "))
    Height = float(input("Enter your height in inches: "))

    #calculatioons
    kiloWeight = Weight * factorWeight
    heightMeters = Height * heightFactor
    BMI = kiloWeight / (heightMeters * heightMeters)


    print("\nDetails")
    print("         Weight:        ", Weight, "         ", kiloWeight, "Kg")
    print("         Height:        ", Height, "          ", heightMeters, "m")
    print("         BMI:           ", BMI)
    print("\n")
    
# Call the main function to start program
main()