# This is a guess the number game.
import random

guessesTaken = 0

print('Hello Player 1! What is your name?')
playerOne = input()

print('Go ahead and choose your low and high number')

lower = int(input("Enter your low number: ")) 

upper = int(input("Enter your high number: ")) 

print('Hello Player 2! what is your name?')
playerTwo = input()

number = random.randint(lower, upper)

print('Well, ' + playerTwo + ', I am thinking of a number between',  lower, 'and', upper)

while guessesTaken < 4:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    
    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
    print("\tBetter Luck Next time!")