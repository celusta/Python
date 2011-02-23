# Filename: mookwl_P2Q2.py
# Name: Marcus Mook Wei Lun
# Description: Input lengths of a triangle and determine if the triangle is valid.

#Prompt user for triangle lengths
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
#Determines if the triangle is valid and displays result
if a+b>c and a+c>b and b+c>a:
    print("Perimeter =", (a+b+c))
else:
    print("Invalid triangle!")
#Exit program
input("Press enter to end the program.")
