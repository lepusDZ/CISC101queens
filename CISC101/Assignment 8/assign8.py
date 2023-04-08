'''
This program works with "Tim Hortons order database". It does 5 things, you can choose between them:
1 - prints meal name and the price when you enter order's number
2 - changes the food name to the name entered by user
3 - removes an order
4 - finds and prints list with donut order IDs
5 - calculates the total cost of no-donut orders

Author:  D.Zaichenko
Student Number: 20378257
Date: 01 Dec 2022
'''

import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context


def readUrl(url):
    """
    This function opens the url and copies the lines from the wwebsite to a list.
    Parameters: url
    Return Value: menu (dictionary with orders)
    """
    try:
        keys = []   #Creates an empty list
        menu = {}   #Creates an empty dictionary
        
        response = urllib.request.urlopen(url)      #Opens the URL and assigns the data in it to the variable
        data = response.readline().decode('utf-8')      #Converts the data to utf-8
        
        while len(data) != 0:
            keys.append(data.split(" "))
            data = response.readline().decode('utf-8')      #Adds lists with data to the keys list

        for k in range(len(keys)):
            menu[keys[k][0]] = [" ".join(keys[k][1:-1]),keys[k][-1].replace("\n","")]       #Adds keys and values to the dictionary. key - order. value - [name, price]

        return menu

    except Exception as err:           #Prints the error if it was there
        print(err)


def printMenu():
    """
    This function just outputs the menu
    """

    print('Welcome to the menu! You have 5 function to run! Choose one.',
            '1. Look up an order', '2. Change the food item', '3. Find a donut order', "4. Remove an order", "5. Calculate total price without donut orders", '', sep='\n')


def findOrder(data):
    """
    This function prints meal name and the price when you enter order's number
    Parameters: data (dictionary with order IDs, namings, prices)
    Return Value: string with order naming and price || 'there is no such an order' if there is no such an order
    """
    choice = input("Order number: ")
    
    if choice in data.keys():       #If entered number exists as a key in a dictionary
        return (data[choice][:])    #Returns naming and price
    
    else:
        return 'There is no such an order.'


def changeFood(data):
    """
    This function changes the food name to the name entered by user.
    Parameters: data (dictionary with order IDs, namings, prices)
    Return Value: None
    """
    choice = input("Order number: ")
    
    if choice in data.keys():       #If entered number exists as a key in a dictionary
        data[choice][0] = input("Enter the new food name: ")        #Changes the name of food
        print('New food name and price:')
        print(data[choice][:])
    
    else:
        print("There is no such an order")


def findDonut(data):
    """
    This function finds and prints list with donut order IDs
    Parameters: data (dictionary with order IDs, namings, prices)
    Return Value: keys (list with donut order IDs)
    """
    keys = []
    
    for k in data.keys():                       #Check each order, if there is "donut" or "Donut" in the food name
        if ("Donut" or "donut") in data[k][0]:  #Adds the key to the list
            keys.append(k)
    
    return keys


def removeOrder(data):
    """
    This function removes an order.
    Parameters: data (dictionary with order IDs, namings, prices)
    Return Value: None
    """
    choice = input("Order number: ")
    
    if choice in data.keys():
        del data[choice]        #Deletes an order with a key entered by a user
        print("Order removed")
    
    else:
        print("There is no such an order")


def calculateTotal(data):
    """
    This function calculates the total cost of no-donut orders.
    Parameters: data (dictionary with order IDs, namings, prices)
    Return Value: total (integer representing the total cost of no-donut orders)
    """
    total = 0
    
    for key in data.keys():             #Check every key in the list
        if key not in findDonut(data):  #If it is not in the donut order list
            total += float(data[key][-1])   #Adds the price to the total
    
    return format(total, ',.2f')


def main():
    data = readUrl("https://research.cs.queensu.ca/home/cords2/timHortons.txt")     #You can change the URL here
    
    printMenu()     #Prints the menu
    
    check = True
    
    while check == True:        #With that the menu outputs until 0 is entered
        decision = int(input('Enter the number from 1 to 5 to choose the function. Enter 0 to exit, 6 to show menu: '))     #Choose the function or exit
        
        if decision<=5 and decision>=1:
            if decision==1:     #1 OPTION, find order function
                print(findOrder(data))

            elif decision==2:   #2 OPTION, change food name function
                changeFood(data)

            elif decision==3:   #3 OPTION, print keys of donut orders function
                print("Donut orders IDs:")
                print(findDonut(data))
            
            elif decision==4:
                removeOrder(data)   #4 OPTION, remove order function
                print('Here is the new order list after your removal:')
                print(data)
            
            elif decision==5:
                print('Total price of no-donut orders is:')
                print(calculateTotal(data))    #5 OPTION, calculate total without donut orders function
                
        elif decision==6:
            printMenu()  

        elif decision==0:
            check = False
        
        else:
            print('You entered the invalid number. Please, ')



main()