# Name: Ruben Sanduleac
# Date: October 20th 2021
# Discription: Write a program that sums numbers obtained from the user.
#              Numbers in the range of -100 to 100 are valid. 
#              A number outside this range indicates that the user is finished with their input.
#              Print the sum of the numbers when complete.

def main():

    # print the title of the program
    print("\nInteractive Loop\n")
    print("Enter a number between -100 and 100 and I will add the integer to the total\n")
    print("Enter any integer outside the range to quit.\n\n")

    #holds the sum of the integers entered
    total  = 0

    while True:
        number = int(input("Enter a number: "))

        if(number < -101) or (number > 101):
            break

        total += number

    print("Total: ", total)
    
main()