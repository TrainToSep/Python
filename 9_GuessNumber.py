logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print (logo)
import random
print ("Welcome to guess number challenge!")
print ("I'm thinking of a number between 1 and 100")
def set_difficult_level ():
    if input ("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
        return 10
    else:
        return 5
number = random.randint (1, 100)

def compare (number, guess):
    if number == guess:
        return 0
    elif number > guess:
        return 1
    else:
        return -1
    
def play ():
    guesses = set_difficult_level ()
    for i in range (guesses):
        print (f" You have {guesses} attempts remain to get the answer. ")
        guess = int (input ("Make a guess: "))
        check = compare (number, guess)
        if check == 0:
            print (f"You got it. {number} is the answer")
            return 
        elif check == 1:
            print ("Too low.")
        else:
            print ("Too high.")
        if guesses > 1:
            print ("Guess again")
        guesses = guesses - 1
    print ("You've ran out of guesses. You lose")

play ()
        
