string = "eggplant"
index = 3
letter = "-"

def replace_at_index(string, index):
    return string[:index] + letter + string[index+1:]

print (replace_at_index(string,index))
