# Task 1: Simple Pay Program
# Author: Ruben Sanduleac
# Date: October 9th 2021
# Discription: This program calculates the travel time between two locations


# Define a function called main
def main():
    
    #variables


    # prints the title of the program
    print("\nCalculate trip duration\n")
    startLocation = input("Enter the starting location: ")
    endLocation = input("Enter the ending location: ")
    distanceBetween = float(input("Enter the distance between locations: "))

    #calculatioons  
    distance = distanceBetween / 60


    print("\nDetails")
    print("         Start:             ", startLocation)
    print("         End:               ", endLocation)
    print("         Distance:          ", distanceBetween, "miles")
    print("         Duration:          ", distance, "hours")
    print("\n")
# Call the main function to start program
main()