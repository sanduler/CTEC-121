# Name: Ruben Sanduleac
# Date: October 12th 2021
# Discription: Write a This problem illustrates the 
#              types of calculations made for a store 
#              that has multiple locations in multiple states.

def main():

    # Title of the program 
    print("\nLunch Purchase Receipt \n")

    # Location based table 
    print("1. Long Beach, California") 
    print("2. Portland, Oregon") 
    print("3. Vancouver, WA\n")

    # get an input from the user to select any of the above locations
    shop = int(input("Please enter the shop location by entering 1, 2 or 3: "))

    # Check if the user selected correct state based on the user input
    while (shop > 3) or (shop < 1):
        shop = int(input("Please enter the shop location by entering 1, 2 or 3: "))

    # use a logical if statment to correspunts the inputs based on the state
    if shop == 1:
         print("\nShop Location: CA\n")
         numSlices = int(input("How many slices would you like: "))
         numDrinks = int(input("How many drinks would you like: "))
         numDonuts = int(input("How many donuts would you like: "))

         # tax for California
         tax = 0.1025

    elif shop == 2:
         print("\nShop Location: OR\n")  
         numSlices = int(input("How many slices would you like: "))
         numDrinks = int(input("How many drinks would you like: "))
         numDonuts = int(input("How many donuts would you like: "))

         # tax for Oregon
         tax = 0.00

    elif shop == 3:
         print("\nShop Location: WA\n")  
         numSlices = int(input("How many slices would you like: "))
         numDrinks = int(input("How many drinks would you like: "))
         numDonuts = int(input("How many donuts would you like: "))

         # tax for Washington
         tax = 0.084
     
    # calcualte the costs of pizza, drink and donut
    costPizza = float(numSlices * 2.00)
    costDrink = float(numDrinks * 1.50)
    costDonut = float(numDonuts * 0.56)

    # calculate the subtotal
    subtotal = costPizza + costDrink + costDonut

    # calcualte the tax from the if statement based on the state
    taxTotal = subtotal * tax

    # calculate the total by subtracting the tax
    total = subtotal - tax

    #print the amount on reciept
    print("\n")
    print("Pizza x ",numSlices, ":       $","{0:.2f}".format(costPizza))
    print("Drink x ",numDrinks, ":       $","{0:.2f}".format(costDrink))
    print("Donut x ",numDonuts, ":       $","{0:.2f}".format(costDonut))
    print("---------------------------------------")
    print("Subtotal:         ", "$","{0:.2f}".format(subtotal))
    print("Tax:              ", "$","{0:.2f}".format(taxTotal))
    print("\n")
    print("Total:            ", "$","{0:.2f}".format(total))
    print("\n")

    amount = float(input("Please enter an amount: "))

    # use a while loop to compare the amount entered to be bigger than the total
    while (amount <= total):
         amount = float(input("Please enter a larger amount to cover the expenses: "))

    # print the amount entered
    print("Tendered:              ", "$","{0:.2f}".format(amount))

    # calculate the change
    change = amount - total
    
    # print the change
    print("Change:                ", "$","{0:.2f}".format(change))
    print("\n")

main()