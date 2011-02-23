# Filename: mookwl_P2Q4.py
# Name: Marcus Mook Wei Lun
# Description: Determine whether the input year is a leap year

# Prompt user for year
year = int(input("Enter year:"))
# Display result
if year%4 == 0 and year%100 != 0 or year%400 == 0 :
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")
