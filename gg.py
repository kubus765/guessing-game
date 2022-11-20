import random
def guessing_game():
    number = random.randint(1,10)
    print("Guess the number (1-10):")
    guess = int(input())
    if guess == number:
        return "You guessed it! Congratulations!"
    else:
        return "Sorry, you didn't guess it, the number was "+str(number)
while 1:
    print(guessing_game())
