user_name = input("Hello, what name is the reservation under? ")
#Change the reservation name from "." to your name (or any name)
reservation_name = "."

if user_name == reservation_name:
    print("Right this way!")
else:
    print("Name:", user_name)
    print("Sorry, we dont have a reservation under that name.")
