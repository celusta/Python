# Filename: mookwl_P2Q5.py
# Name: Marcus Mook Wei Lun
# Description: Find number of days in a month

# Prompt user for month in number
n = int(input("Enter a month in number:"))
y = int(input("Enter a year:"))
# Month listing
m = ['January', 'February', 'March', 'April', 'May', 'June',
     'July', 'August', 'September', 'October', 'November', 'December']
# Display result
if n in range(1,12,2) :
    print(m[n-1], y, "has 31 days.")
elif n in range(4,12,2) :
    print(m[n-1], y, "has 30 days.")
elif n == 2 and y%4 == 0 and y%100 != 0 :
    print(m[n-1], y, "has 29 days.")
else :
    print(m[n-1], y, "has 28 days.")
