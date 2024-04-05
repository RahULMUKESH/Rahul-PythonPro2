import random 
import time

def intro():
    global name
    print("May I ask you for your name?")
    name = input() 
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(number):
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter) 

            if guess <= 200 and guess >= 1:
                guessesTaken += 1 
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(0.5)
                        print("Try Again!")
                if guess == number:
                    break 
            if guess > 200 or guess < 1: 
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:
            print("I don't think that "+enter+" is a number. Sorry")
            
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

def play_game():
    name = intro()
    playagain = "yes"
    while playagain.lower() in ["yes", "y"]:
        number = random.randint(1, 200)
        pick(number)
        print("Do you want to play again? (yes/no)")
        playagain = input()

play_game()
