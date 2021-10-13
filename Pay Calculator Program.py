# Name: Ruben Sanduleac
# Date: October 12th 2021
# Discription: Write a program for pay that can:
#              - regular hours worked overtime hours worked regular pay
#              - overtime pay
#              - gross pay (total pay)
#              - tax withheld at a rate of 12.5%
#              - other deductions at a rate of 5% of the total pay only over $500.00 net pay received
def main():

    print("Pay Program")

    hours = int(input("Enter the number of hours worked this week: "))
    print("\n")

    rate = float(15.00)
    overtimeRate = float(22.5)
    tax = float(12.5)
    deduction = float(0.05)

    if hours > 40:
        overTime = hours - 40
        regularHours = hours - overTime
        pay = regularHours * rate
        overtimePay = overtimeRate * overTime
    else:
        regularHours = hours
        pay = regularHours * rate    


    grossPay = pay + overtimePay

    taxPay = 0.125 * grossPay
    
    if grossPay > 500:
         deductionsTax = grossPay * deduction
    else:
        deductionsTax = 0

    netPay = grossPay - taxPay - deductionsTax


    print("Pay Stub")
    print("                 Regular     Overtime")
    print("         Hours:  ", regularHours, "       ", overTime)
    print("         Pay:    ",pay, "    ", overtimePay)  
    print("\n")
    print("         Gross Pay:", "                ", grossPay)
    print("         Tax:", "                      ", taxPay)
    print("         Other Deductions:", "         ", deductionsTax)
    print("         Net Pay:", "                  ", netPay)

    print("\n")

main()
