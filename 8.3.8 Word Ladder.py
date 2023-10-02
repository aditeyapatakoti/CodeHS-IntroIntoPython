user_string = input("Enter a string: ")

def get_index():
    while True:
        try:
            user_index = int(input("Enter an Index: "))
            if user_index >= len(user_string):
                print("Invalid Index")
                continue
            if user_index < -1:
                print("Invalid Index")
                continue
        except ValueError:
            print("Invalid Index")
            continue
        return user_index

def get_string():
    while True:
        user_letter = input("Enter letter: ")
        if user_letter.isupper():
            print("Character must be a lowercase letter!")
            continue
        if len(user_letter) > 1:
            print("Must be exactly one character!")
            continue
        return user_letter


while True:
    user_string = list(user_string)
    returned_index = get_index()
    if returned_index == -1:
        break
    returned_string = get_string()
    user_string[returned_index] = returned_string
    print("".join(user_string))
