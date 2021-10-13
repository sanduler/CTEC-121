# Task 1: Simple Pay Program
# Author: Ruben Sanduleac
# Date: October 9th 2021
# Discription: This program calculates the pay for an employee based 
#              on the info provided. 


# Define a function called main
def main():
    
    # prints the title of the program
    print("\nSimple Pay Program\n")
    hoursWorked = float(input("Enter the number of hours worked: "))
    rate = float(25.00)
    pay = hoursWorked * rate
    tax = float(12.5)
    netPay = pay - (0.125 * pay)
    print("\nPay Stub")
    print("         Hours:        ", hoursWorked)
    print("         Rate:        $", rate)
    print("         Pay:         $", pay)
    print("         Tax:         $", tax)
    print("     Net Pay:         $", netPay)
    print("\n")
# Call the main function to start program
main()