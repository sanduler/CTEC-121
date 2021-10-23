# Name: Ruben Sanduleac
# Date: October 20th 2021
# Discription: This program sums every number from 1 - 142


def main():

    # print the title of the program
    print("\nAccumulator Pattern Program\n")

    # accumilator starting at 0
    total = 0

    # set the range from 1 -142 , one digit lower bcs starting digit is 0
    x = range(1, 143)
    for n in x:

        # increment the total by adding n 
        total = total + n

    # print the total
    print("The total sums for numbers 1 through 142 is: ", total,"\n")

main() 