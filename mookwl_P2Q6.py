# Filename: mookwl_P2Q6
# Name: Marcus Mook Wei Lun
# Description: Sorts 3 integers from largest to smallest

# Prompt user to enter 3 integers
a = int(input("Enter 1st integer:"))
b = int(input("Enter 2nd integer:"))
c = int(input("Enter 3rd integer:"))
# Display result
if a>b>c :
    print(a, b, c)
elif a>c>b :
    print(a, c, b)
elif b>a>c :
    print(b, a, c)
elif b>c>a :
    print(b, c, a)
elif c>a>b :
    print(c, a, b)
else :
    print(c, b, a)
