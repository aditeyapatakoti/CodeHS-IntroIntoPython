speed(0)
radius = int(input("What is the circle's radius?: "))
square_color_choice = input("What is the color of the square? ")

circle_color_choice = input("What is the color of the circle? ")

def draw_square():
    for i in range(4):
        pendown()
        begin_fill()
        color(square_color_choice)
        forward(radius*2)
        end_fill()
        right(90)

def draw_circle():
    pendown()
    begin_fill()
    color(circle_color_choice)
    circle(radius)
    end_fill()

penup()
setposition(-radius, radius)
draw_square()
penup()
setposition(0, - radius)
draw_circle()
