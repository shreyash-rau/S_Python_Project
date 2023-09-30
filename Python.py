# method to get random numbers
import random 

name = input("Enter your Name : ")
 
print("Good Luck ! ", name)
 
words = ['angular', 'anglescript', 'bash', 'beta', 
         'charm', 'chapel','dart','darwin', 'ease', 'ecmascript','flex','go!','gdscript','hermes','haskell'
         ,'icon','javascript','java','kotlin','livescript','microcode',' mangoose','dotnet','neko','oracle'
         ,'peral','psql','qalb','ruby'
         ,'sql','typescript','unicon','winbatch','xquery','zonnon']
 
# chose the random word form words of list
word = random.choice(words)
print("Guess the characters")
 
guesses = '' 
turns = 10           # numbers of turne to b alloted to guess the words
while turns > 0:
    failed = 0           # counts the number of times a user fails
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
 
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")
    guesses += guess         # every input character will be stored in guesses
  
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")
