'''
This program is the BINGO game. It consists of 5 functions. 
It creates a 9-line card and asks user if they want to continue.
With each 'yes' response from the user it picks the random line from the website.
If this line is on the card - it changes it to "SEEN". Win conditions are horizontal "SEEN" lines and corners.

Author:  D.Zaichenko
Student Number: 20378257
Date: 23 Nov 2022
'''
import ssl
import urllib.request
import random
ssl._create_default_https_context = ssl._create_unverified_context

def readUrl(url):
    """
    This function opens the url and copies the lines from the wwebsite to a list.
    Parameters: url
    Return Value: WordList (list with lines)
    """
    try:
        WordList = []       #Creates an empty list
        response = urllib.request.urlopen(url)      #Opens the URL and assigns the data in it to the variable
        data = response.readline().decode('utf-8')      #Converts the data to utf-8
        
        while len(data) != 0:
            WordList.append(data.replace("\n", ""))
            data = response.readline().decode('utf-8')  
            
        return WordList

    except Exception as err:           #Prints the error if it was there
        print(err)

def theCard(list):
    """
    This function creates the BINGO card with 9 lines
    Parameters: list (list with lines)
    Return Value: tempList (9 lines card for BINGO game)
    """
    tempList = []       #Creates an empty list
    
    while len(tempList) < 9:                        #Loop goes on until there are 9 lines in the card
        item = list[random.randrange(len(list))]        #Assigns a random line from the list to the item variable
        
        if item not in tempList:        #No duplicates in the list
            tempList.append(item)
            
    return tempList

def display(card):
    """
    This function prints the card.
    Parameters: card (list with 9 lines)
    Return Value: None
    """
    print(card[0], card[1], card[2], sep=' || ')
    print(card[3], card[4], card[5], sep=' || ')
    print(card[6], card[7], card[8], sep=' || ')

def seenCheck(ItemsList,card):
    """
    This function puts "SEEN" instead of a line if it = the random line from url list
    Parameters: ItemsList (url list), card (9 line list)
    Return Value: None
    """
    for b in range(len(card)):
            if ItemsList[random.randrange(len(ItemsList))] == card[b]:      #Check if every line from the card = the random line from the url list
                card[b] = "SEEN"            #If yes - changes it to "SEEN"

def winCheck(card):
    """
    This function checks the card for the win conditions
    Parameters: card (9 line list)
    Return Value: True if win
    """
    if card[3] == "SEEN" and card[4] == "SEEN" and card[5] == "SEEN":       #2 row
        print('YOU WON!!!')
        return True
    elif card[0] == "SEEN" and card[1] == "SEEN" and card[2] == "SEEN":     #1 row
        print('YOU WON!!!')
        return True
    elif card[6] == "SEEN" and card[7] == "SEEN" and card[8] == "SEEN":     #3 row
        print('YOU WON!!!')
        return True
    elif card[0] == "SEEN" and card[2] == "SEEN" and card[6] == "SEEN" and card[8] == "SEEN":   #corners
        print('YOU WON!!!')
        return True



def main():
    url = 'https://research.cs.queensu.ca/home/cords2/zoombingo.txt'       #You can change the URL here
    choice = 'Y'
    ItemsList = readUrl(url)        #Assigns the url list to ItemsList variable
    card = (theCard(ItemsList))     #Assigns the card list to card variable
    
    print('Welcome to the BINGO!!!\n')

    while choice == 'y' or choice == 'Y':
        display(card)
        choice = input('Is it the time to choose a new item? (Y or y for yes): ')
        
        seenCheck(ItemsList,card)

        if winCheck(card) == True:
            choice == 'n'


main()