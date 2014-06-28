#!/usr/bin/python

import random
from collections import Counter

choice = None
rolls = None    
result = []

def numcheck(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def userInput():
    global choice
    global rolls
    global result
    #resets result value
    result = []

    choice = input('How many sides do you wish to use?(up to 100) ')
    print('-'*10)
    rolls = input('How many times would you like to roll the dice? ')
    print('-'*10)

    while numcheck(choice) == False or int(choice) < 0 or int(choice) > 100:
        choice = input('Please choose a number more than 0 and up to 100 sides. ') 
        print('Thank You')

    while numcheck(rolls) == False or int(rolls) < 0:
        rolls = input('Please choose a number of rolls  greater than 0 ')

    rolldice(int(rolls))

def rolldice(times):
    while times > 0:
        result.append(random.randint(0, int(choice) - 1))
        times -= 1

    post(result)

def replay():
    i = input('Would you like to roll a new set of dice(y/n). No will close the program.')
    if i == 'y':
        userInput()
        replay()
    else:
        exit(0) 

def post(x):
    perpost = []
    count = Counter(x)
    xlist = []
    
    print('Results: ', result)
    
    for key in count.keys():
        perpost.append((count[key], key))
    print('-'*10)
    print('Most often occurences....')
    
    perpost.sort(reverse=True)
    
    if perpost[2][0] > 2:
        x = 3
    else:
        x = 1

    for tally, num in perpost[0:x]:
        percent = int(tally) / int(rolls) * 100
        print('The number ', num, 'was rolled',  "%.2f" % round(percent,2), '% of the time(', tally, ')')
    
    return None


userInput()
replay()
