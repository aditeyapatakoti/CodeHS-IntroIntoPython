def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must be a lowercase letter!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess

def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result


secret_word = "grasswayz"
dashes = "-"*len(secret_word)
while True:
    guess = get_guess()
    if guess in secret_word:
        print("The letter is in the word.")
        dashes = update_dashes(secret_word, dashes, guess)
    else:
        print("That letter is not in the word.")
        print(dashes)
