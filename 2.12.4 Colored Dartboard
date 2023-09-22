speed(0)
circle_radius=100
def center_circle():
    right(90)
    forward(-25)
    left(90)
def draw_circle():
    begin_fill()
    color(color_choice)
    circle(circle_radius)
    end_fill()
penup()    
setposition(0,-100)
for i in range(4):
    pendown()
    color_choice = input("What is the color of the circle? ")
    draw_circle()
    penup()
    center_circle()
    circle_radius = circle_radius - 25
