# Filename: mookwl_P2Q3.py
# Name: Marcus Mook Wei Lun
# Description: Input a score between 0 to 100 inclusive and determine the grade

# Determine grading function
def grade():
    score = float(input("Enter your score: "))
    if score >=70:
        print("Your grade is A.")
    elif score >=60 and score<70:
        print("Your grade is B.")
    elif score >=55 and score<60:
        print("Your grade is C.")
    elif score >=50 and score<55:
        print("Your grade is D.")
    elif score >=45 and score<50:
        print("Your grade is E.")
    elif score >=35 and score<45:
        print("Your grade is S.")
    else:
        print("Your grade is U.")

# Main
grade()

# Exit program
input("Press enter to end the program.")
