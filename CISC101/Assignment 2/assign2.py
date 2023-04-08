"""
This program is the dice game. There are 4 conditions with 4 different outcomes. It goes on until user wants to stop it.
Author:  D.Zaichenko
Student Number: 20378257
Date: 30 Sept 2022
"""

#Importing random module and assigning the values to key variables
import random
total = 0
play = 'y'

while play == 'y' or play == 'Y':
    
    print('DICE! DICE! DICE!')               #Getting two dice numbers for the next 4 conditions
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print ('You have rolled', die1, die2)
    dice_sum = die1 + die2                   #dice_sum variable for the future usage
    second_cond_helper = (dice_sum%2)        #variable for the second condition (even numbers)
    
    if die1 == die2:                         #1 condition, DOUBLES
        print('DOUBLES! Rolling the second die!')
        roll_num = 1
        while die1 == die2:
            die2 = random.randint(1,6)
            print ('Dice currently are:', die1, die2)
            roll_num += 1
            sum = die1 + die2 + roll_num
            total += sum
        print('Your current score is', total)
        play = input('Wanna play more? Enter "Y" or "y" to continue! Fun is endless!')
    
    elif second_cond_helper == 0:            #2 condition, EVEN NUMBERS
        print('The sum of', die1, die2, 'is even so rolling the dice 4 times')
        for free_spins in range(4):
            die3 = random.randint(1, 6)
            die4 = random.randint(1, 6)
            print ('Dice currently are:', die3, die4)
            sum = die3 + die4
            total += sum
        print('Your current score is', total)
        play = input('Wanna play more? Enter "Y" or "y" to continue! Fun is endless!')
    
    elif die1 == 3 or die2 ==3:              #3 condiiton, 3 - GAME OVER
        print('3!! Unlucky.. Game ends.')
        total += 3
        print('Your final score is', total)
        play = 'n'
    
    elif dice_sum == 7:                      #4 condition, 7 MAGIC NUMBER
        print('Hooray!', die1, '+', die2, '= 7! 10 Free spins and +10 points to your total! Enjoy!')
        for free_spins in range(10):
            die3 = random.randint(1, 6)
            die4 = random.randint(1, 6)
            print ('Dice currently are:', die3, die4)
            sum = die3 + die4
            total += sum
        total += 10
        print('Your current score is', total)
        play = input('Wanna play more? Enter "Y" or "y" to continue! Fun is endless!')
    
    else:
        total += dice_sum                    #no conditions met
        print('Your current score is', total)
        play = input('Wanna play more? Enter "Y" or "y" to continue! Fun is endless!')