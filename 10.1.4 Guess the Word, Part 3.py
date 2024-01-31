secret_word = "eggplants"
dashes = "---------"
# NOTE: Change the amount of dashes according to how many letters are in the variable
# NOTE CONTINUED: secret word. Make sure to change both top and bottom.
arr = ['-','-','-','-','-','-','-','-','-']
guesses_left = 10
# NOTE: You can change the number of guesses left according to the number above.
def get_guess():
    while True:
        print(''.join(arr))
        print(str(guesses_left) + " incorrect guesses left.")
        guess = input("Guess: ")
        if len(guess) > 1:
            print("Your guess must have exactly one character!")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Your guess must be a lowercase letter!")
        else:
            return guess


while guesses_left > 0 and '-' in arr:
    a = get_guess()
    for i in range(len(secret_word)):
        if secret_word[i] == a:
            arr[i] = a
    if a not in secret_word:
        print("That letter is not in the word!")
        guesses_left -= 1
    else:
        print("That letter is in the word!")

if '-' not in arr:
    print("Congrats you win! The word was: "+ secret_word)
else:
    print("You lose, The word was: " + secret_word)

def update_dashes():
    pass
