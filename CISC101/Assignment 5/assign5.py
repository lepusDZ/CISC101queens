'''
This program is a Wordle game. It chooses a word from the given list, prints it, then asks user to
guess it. Program will output information for each letter regarding whether the letter is in the correct 
position, not in the word, or is in the word but in the wrong position. User has only 6 attempts. Program
stops running if the user wins or runs out of attempts.

Author:  D.Zaichenko
Student Number: 20378257
Date: 03 Nov 2022
'''
import random


def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the secret word
    """

    validWords = ["could", "smile", "ultra", "extra",
                  "beacon", "hearts", "cap", "wordle",
                  "computing", "python"]

    # Generates a random integer in order to use it as an index
    wordPosition = random.randint(0, len(validWords)-1)

    # Uses the generated integer as an index to pick a random word from the list
    return validWords[wordPosition]


def checkLetters(secretWord, userWord):
    """
    This function checks the letters guessed by the user against the secret
    word and informs the user as to which letters are in the correct location,
    which letters are in the word but not in the correct location and which
    letters are not in the word.
    Paramters:   secretWord, userWord - strings
    Returns:  None
    """

    for k in range(len(userWord)):  # Loop checks every letter of userWord one by one
        if userWord[k] == secretWord[k]:
            print(userWord[k], '- in correct place')        # Prints, if a letter in userWord is the same as a letter in secretWord
        elif userWord[k] in secretWord:
            print(userWord[k], '- not in correct place')    # Prints, if a letter in userWord is in secretWord, but in incorrect place
        else:
            print(userWord[k], '- not in the word')         # Prints, if a letter in userWord is not in secretWord


def checkForDuplicates(userWord):
    """
    This function checks the user's word for duplicate letters.
    If there are duplicate letters, the function returns True, otherwise, False.
    Parameters:  userWord - string
    Return:  Boolean
    """
    check = 0

    for k in userWord:          # Checks if letter k repeats in the userWord more than 1 time.
        for b in range(len(userWord)):      # If it doesn't, then after every [for b in range] loop variable check adds only 1
            if k == userWord[b]:
                check += 1  

    if check > len(userWord):       #If there're duplicate letters check > len(userWord)
        return True
    else:
        return False                #check = len(userWord) - no duplicate letters


def play(secretWord):
    """
    This function allows the user to play the game, entering up to 6 words to
    try to guess the secret word. When the correct word is guessed, the play
    stops and the user is congratulated.
    Parameters: string representing the secretWord
    Return Value:  None
    """

    attempt = 0
    while attempt < 6:         #6 given attempts
        print('Please, guess a', len(secretWord), 'letter word: ', end='')      # User guesses the word
        userWord = input('')
        
        if checkForDuplicates(userWord) == False:       #No duplicate letters
            attempt += 1                            # +1 attempt to total attempts
            checkLetters(secretWord, userWord)
            
            if userWord == secretWord:          #User guessed the word
                print('You won!')
                break
        
        else:
            print('Sorry, your word has duplicated letters. Try another one.')     #If checkForDuplicates returned True (duplicate letters)


def main():
    """
    This implements the user interface for the program.
    """

    secretWord = chooseWord()       #Assigns the secret Word to a variable
    print('The secret word is', secretWord)     #Prints the secret word

    play(secretWord)        #Starts the game


main()
