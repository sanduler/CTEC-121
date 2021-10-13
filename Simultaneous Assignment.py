# Name: Ruben Sanduleac
# Date: October 12th 2021
# Discription: Write a program that gets three values, an int, a float, 
#              and a single word, from the user. Use simultaneous 
#              assignment to assign the three values to three variables. 
#              Use the split method to separate the input string into three 
#              values. There's a helpful video in this Module regarding 
#              simultaneous assignment.


def main():
    number, decimal, word = input("Enter an int, a floar and a word: ").split()
    print("\n")
    
    print ((number), (decimal), (word))
    print(type(number), type(decimal), type(word))
    
    number = int(number)
    decimal = float(decimal)

    print(number, type(number))
    print (decimal, type(decimal))


# Call the main function to start program
main()