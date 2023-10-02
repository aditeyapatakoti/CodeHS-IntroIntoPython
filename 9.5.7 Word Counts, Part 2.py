text = input("Enter some text: ")

text_list = text.split()

dictionary = {}
def update_counts(count_dictionary, word):
    if word in count_dictionary:
        count_dictionary[word] = count_dictionary[word] + 1
    else:
        count_dictionary[word] = 1
    
for word in text_list:
    update_counts(dictionary, word)

print(dictionary)
