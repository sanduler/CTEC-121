# Name: Ruben Sanduleac
# Date: October 20th 2021
# Discription: This program uses the range function to skip every third
#              number starting from 11 and ending in 23;

# 11 is the starting number, 26 is the ending number, 
# 26 is never reached as the last iteration stops at 23.
# end = is used to create place holders between numbers and
# place them on one line.
x = range(11, 26, 3)
for n in x:
  print(n, end= " ")