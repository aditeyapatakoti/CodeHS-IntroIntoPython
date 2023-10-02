def retrieve_positive_number():
    while True:
        try:
            num = int(input("Enter a positive number: "))
            if num > 0:
                return num
            print("The number must be positive!")
        except ValueError:
            print("That wasn't a number!")

# Call the function and print
print retrieve_positive_number()
