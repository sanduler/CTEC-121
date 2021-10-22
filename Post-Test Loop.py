# Name: Ruben Sanduleac
# Date: October 20th 2021
# Discription: Ask the user for a number between 1 and 7. 
#              Repeat the input request if the number entered is outside the range.


def main():

    # print the title of the program
    print("\nPost-Test Loop\n")
    print("Enter a number between 1 and 7\n")
    print("Enter any integer outside the range to quit.\n\n")

    while True:
        number = int(input("Enter a number: "))

        if(number < 1) or (number > 7):
            break
    
main()