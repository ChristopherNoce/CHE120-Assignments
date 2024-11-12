#Christopher Noce | 21143999

#modification: single letter hangman

import random

letters = 'abcdefghijklmnopqrstuvwxyz'

def getRandomLetter(letterList):
    #this function returns a random letter from the list of letters.
    letterIndex = random.randint(0, len(letterList) - 1)
    return letterList[letterIndex]

def getGuess():
    guess = input('Guess the letter:')
    return guess

def playAgain():
    return input('Do you want to play again? (yes or no) ') == 'yes' #true or false

print('S I N G L E  L E T T E R  G A M E')
print('''
  +---+
      |
      |
      |
     ===''')

while True:
    secretLetter = getRandomLetter(letters)
    
    # Player has one guess
    guess = getGuess()
    
    if guess == secretLetter:
        print(f'Congratulations! You guessed the letter "{secretLetter}" correctly!')
    else:
        print(f'Sorry, the correct letter was "{secretLetter}". Better luck next time!')
        print('''
  +---+
  O   |
 /|\  |
 / \  |
     ===''')
    
    if not playAgain():
        break
