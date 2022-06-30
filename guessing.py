# simple guessing game
answer = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
canGuess = True

while guess != answer and canGuess == True:
    # update the guess_count
    if guess_count < guess_limit:
        guess_count += 1
        
        # Ask for the guess and store the input in var guess
        guess = input("Please guess the secret word. ")
        print("You have "+ str(guess_limit - guess_count) + " tries left.")

            
    else:
        canGuess = False
        print("You have run out of guesses.")
    

if canGuess == True:
    print("You win.  You solved the mystery in "+str(guess_count)+" tries.")
else:
    print("You lose.")