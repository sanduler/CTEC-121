# Name: Ruben Sanduleac
# Date: October 12th 2021
# Discription: Write a program for pay that can:
#              - calculates the mean and standard 
#                deviation of a set of random numbers.

import random
import math

def main():
    print("Fun With Stats \n")
    
    total = 0
    totalSquared = 0

    for count in range(1, 101):
        randomNumber = random.randint(1,100)
        total = total + randomNumber
        totalSquared = totalSquared + randomNumber ** 2
        # print("Number: ", count, "Random Number: ", randomNumber, "Total: ", total, "Total Squared: ", totalSquared)

    mean = total / 100
    variance = (totalSquared) - (((total)**2)/100)
    diviation = math.sqrt(variance)

    print("        mean:",              mean)
    print("        std deviation:",     diviation)

main()