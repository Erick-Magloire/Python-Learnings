###Building a Guessing Game
#Creating a game where a user keeps typing in guesses until they correctly guess the "secret word"
secret_word = "giraffe"
guess = ""
guess_count = 0 #Added variable where user has limited tries to guess the secret_word
guess_limit = 5 #attempts
out_of_guesses = False
                        #Added condition for message when user is out of guesses
while guess != secret_word and not(out_of_guesses): #Keep looping while guess is not equal to secret_word
    if guess_count < guess_limit: #If guess count is less than guess limit, keep executing loop
        guess = input("Enter new guess:")
        guess_count += 1
    else: #if guess count is not less than guess limit, out_of_guesses becomes True
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, no more attempts.")
else:
    print ("You got it champ!")

##Process Logic Breakdown
#1.Created variable for the user's guess, "secret_word", starting guess count, guess limit, and out of guesses condition
#2.while loop condition is guess is not secret_word
#3.Specify as long as guess_count is less than guess_limit, continue doing the below
    #a.when loop is ran, increase guess_count by 1 and provide new input line
#4.Specified condition for when guess_count = guess_limit
    #a. using boolean value, and not(out_of_guesses)
#5.If statement to give response when the user has won or ran out of guesses
