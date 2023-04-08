"""
This program shows the pricelist, asks the user to choose a meal, asks for a tip, calculates the final price.
Author:  D.Zaichenko
Student Number: 20378257
Date: 19 Sept 2022
"""

tax = 1.05
print("Items available for purchase:\n1. Chicken Wrap $4.50\n2. Wings (10) $16.99\n3. Fries $4.59\n4. Meatball Sub $8.39\n5. Soup $2.95\n")
item_num = int(input("Enter the number corresponding to the item that you would like to purchase: "))

if item_num < 1 or item_num > 5:    #If user enters the wrong number, the program will stop
    print('You entered the invalid number. Choose another one.')
else:                               #Assigning the correct price to the variable after the user's number input
    if item_num == 1:
        food_price = 4.50
    elif item_num == 2:
        food_price = 16.99
    elif item_num == 3:
        food_price = 4.59
    elif item_num == 4:
        food_price = 8.39
    else:
        food_price = 2.95
    
    tip = input('Would you like to give a tip? (Enter "Yes" if yes): ')     #Asking for a tip
    if tip == 'Yes':
        print('How do you want to leave a tip?\n1. Percentage %\n2. Dollars $\n')
        tip_type = int((input('Enter the number corresponding to your choice: ')))  #Tip type
        if tip_type < 1 or tip_type > 2:            #If user enters the wrong number, the program will stop
            print('You entered the invalid number. Try again.')
        elif tip_type == 1:     
            tip = int(input('Enter the percentage: '))
            total = format(food_price * tax + (food_price * (tip / 100)), ',.2f')   #Calculations if tip is a percentage
            print('Your total is $', total, sep='')       
        elif tip_type == 2:
            tip = int(input('Enter the tip: '))
            total = format(food_price * tax + tip, ',.2f')      #Calculations if tip is an amount
            print('Your total is $', total, sep='')
    else:
        total = format(food_price * tax, ',.2f')    #Calculations if there is no tip
        print('Your total is $', total, sep='')     