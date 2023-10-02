user_age = int(input("What is your age?"))
requirement_age = 18

if user_age >= requirement_age:
    print("Age:", str(user_age))
    print("You are old enough to vote!")
else:
    print("Age:", str(user_age))
    print("You are not old enough to vote.")
