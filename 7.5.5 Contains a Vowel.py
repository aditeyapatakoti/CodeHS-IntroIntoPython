word = "abcdefghijklmnopqrstuvwxyz"
def contains_vowel(word):
    vowels = ["a", "e", "i","o", "u"]
    for vowel in vowels:
        if vowel in word:
            return True
    return False
print (contains_vowel(word))
