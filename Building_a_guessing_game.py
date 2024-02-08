secrete_word="welcome"
guess=""
guess_count=0
guess_limit = 3
out_of_guesses = False
while guess != secrete_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Please enter the guess word: ")
        guess_count += 1
    else:
        out_of_guesses=True
if(out_of_guesses):
    print("ohhh out of Guesses, You lose the game!")
else:
    print("Yeah, You win the game!")