speed(0)
secret_number = 5
pensize(10)

def green_check():
    color("green")
    penup()
    backward(25)
    right(45)
    pendown()
    forward(35)
    left(90)
    forward(75)
    
def draw_arrow():
    color("red")
    left(90)
    forward(50)
    left(45)
    backward(25)
    forward(25)
    right(90)
    backward(25)
    forward(25)
    left(45)
    backward(100)
    forward(50)
    right(90)
    
user_number = int(input("Guess a number between 1 and 10: "))

while user_number != secret_number:
    if user_number < secret_number:
        draw_arrow()
    else:
        left(180)
        draw_arrow()
        right(180)
    user_number = int(input("Guess a number between 1 and 10: "))
    clear()
    
green_check()
