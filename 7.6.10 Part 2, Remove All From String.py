word = "bananas"
letter = "na"

def remove_all_from_string(word, letter):
    while True:
        index = word.find(letter)
        if index == -1:
            return word
        word = word[:index] + word[index+len(letter):]

print (remove_all_from_string(word, letter))
