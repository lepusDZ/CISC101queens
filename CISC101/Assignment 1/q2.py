"""
This program asks the user to input their Numerical Course Average, converts it to a numeric mark and outputs it.
Author:  D.Zaichenko
Student Number: 20378257
Date: 19 Sept 2022
"""

mark = int(input('Please enter your numeric mark: '))   #Numeric mark input
if mark < 0 or mark > 100:
    print('Your number is out of range. Try again.')    #If input is out of range, the program stops.
elif mark >= 90:        #Converting the number to a numeric mark + numeric mark output
    print("A+")
elif mark >= 85:
    print("A")
elif mark >= 80:
    print("A-")
elif mark >= 77:
    print("B+")
elif mark >= 73:
    print("B")
elif mark >= 70:
    print("B-")
elif mark >= 67:
    print("C+")
elif mark >= 63:
    print("C")
elif mark >= 60:
    print("C-")
elif mark >= 57:
    print("D+")
elif mark >= 53:
    print("D")
elif mark >= 50:
    print("D-")
else:
    print("F :(")