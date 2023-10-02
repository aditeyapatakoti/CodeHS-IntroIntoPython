user_weather = input("What is the weather? (sunny, rainy, snowy):")

# Case sensitive
def rainy():
    print("On a rainy day, galoshes are appropriate footwear.")
def sunny():
    print("Put on some sandals!!!!!!!!!!!!!!")
def snowy():
    print("Put on some boots!!!!!!!!!!!!!!!")

if user_weather == "rainy":
    rainy()
elif user_weather == "sunny":
    sunny()
elif user_weather == "snowy":
    snowy()
else:
    print("Not valid")
