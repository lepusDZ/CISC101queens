'''
This program consists of 6 function and the main function that runs them. 
1 - reads the url and writes words from there to a file.
2 - creates a dictionary where key is the number of letters in a word and value is the number of words with this amount of letters
3 - counts total amount of words in the given interval
4 - counts how many letters there are in the longest word
5 - returns the length that has the highest number of words of that length
6 - takes a dictionary of length/frequency pairs as a parameter and writes it to a file

Author:  D.Zaichenko
Student Number: 20378257
Date: 17 Nov 2022
'''
import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context


def readWords(url):
    """
    This function reads the url and writes words from there to a file.
    Parameters: url
    Return Value: A list with the words or an empty list if there is an error
    """
    try:
        response = urllib.request.urlopen(url)      #Opens the URL and assigns the data in it to the variable
        data = response.read().decode('utf-8')      #Converts the data to utf-8
        data_list = data.split()                    #Creates a list with the words from the website
        return data_list

    except Exception as err:           #Returns [] if the website was not found or if there was an error and prints the error
        print(err)
        return []


def wordCount(wordList):
    """
    This function creates a dictionary where key is the number of letters in a word
    and value is the number of words with this amount of letters.
    Parameters:  wordList
    Return Value: A dictionary where key - number of letters. Value - number of words with this amount of letters.
    """
    numLet = {}     #Creates an empty dictionary

    for length in range(1, maxWordLength(wordList)+1):      #k is the value from 1 to the number which represents the length of the longest word
        tempList = []           #Creates an empty list every cycle
        
        for index in range(len(wordList)):      #This loop checks every word, if the word length = the length variable it adds the word to the list
            if len(wordList[index]) == length:
                tempList.append(wordList[index])    #Adds the word to the empty list
        
        numLet[length] = len(tempList)      #Here length variable represents the key in the numlet dictionary and assigns the length
                                            #Of the list above to this key
    
    return numLet


def totalWords(numLet, n, m):
    """
    This function counts total amount of words in the given interval
    Parameters:  numLet (lengths dictionary), n - start value of the interval, m - end value of the interval
    Return Value: An integer representing sum of the words in the interval, 0 if n > m
    """
    if n <= m:
        total = 0
        
        for k in range(n,m+1):  #Adds the number of words in the interval to the total
            total += numLet[k]
        return total
    
    else:
        return 0 


def maxWordLength(wordList):
    """
    This function counts how many letters there are in the longest word
    Parameters:  wordList
    Return Value: An integer representing the length of the longest word in the list
    """
    return len(max(wordList, key=len))      #Returns the length of the longest word in the list


def maxFrequency(numLet):
    """
    This function finds the length that has the highest number of words of that length
    Parameters: numLet (lengths dictionary)
    Return Value: An integer representing the length
    """
    b = max(numLet.values())        #Assigns the highest value to b variable
    
    for k in range(1, len(numLet)):
        if numLet[k] == b:  #Checks each key if that value is assigned to it
            key = k         #If yes - assigns it to key variable
    
    return key


def writeToFile(numLet):
    """
    This function writes the data from numLet dictionary to a file
    Parameters: numLet (lengths dictionary)
    Return Value: None
    """
    file = open('statWords.txt', 'w')
    
    for b in range(1, len(numLet)):
        file.write('There are ' + str(numLet[b])+ ' words of length ' + str(b) + '\n')  #Writes the data to a file
    
    file.close()


def main():
    url = 'https://research.cs.queensu.ca/home/cords2/words.txt'        #You can change the URL here

    words = readWords(url)
    
    print('This is the dictionary.\nKey - number of letters. Value - number of words with this amount of letters.')
    listLength = wordCount(words)
    print(listLength)
    
    print('Total words from 1 to 2')
    print(totalWords(listLength, 1, 2))
    print('Total words from 3 to 5')
    print(totalWords(listLength, 3, 5))
    print('Total words from 6 to 2, 6 is greater than 2 => it returns 0')
    print(totalWords(listLength, 6, 2))
    
    print('How many letter there are in the longest word:')
    print(maxWordLength(words))

    print('Here is the length that has the highest number of words:')
    print(maxFrequency(listLength))
    
    print('Now it writes the data to the file called statWords.txt')
    writeToFile(listLength)
    print('.\n.\n.\nDONE')
    

main()