import random

import time

#list of words being picked from (14)
aWordList = ["duck", "cat", "dog", "giraffe",
 "fish", "eagle", "frog", "snake", "spider",
  "horse", "bee", "hippopotamus", "scorpion", "chimpanzee"]

#"randomly" select word from list
iWordSelection = (random.randrange(1,14))

stWORD = aWordList[iWordSelection]

#define amount of turns left 
iTurns = int(5)

while iTurns > 0:

    stUserSelection = input("please input your guess: ")

    iFails = 0

    for stWORD in stUserSelection:

        print(stWORD)

    else:
        print("*")
        iFails += 1

 if stUserSelection in stWORD:
        iTurns -= 1
        print ("wrong")
        time.sleep(2)
        
        print ("you have " + str(iTurns) + " turns left")

        if iTurns == 0:
            print("you loose")
            time.sleep(5)
            break
        
    if iFails == 0:
        print("you won!!")
        time.sleep(10)
        break


   

        
        