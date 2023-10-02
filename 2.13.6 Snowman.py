speed(0)
first_radius = int(input("How big should the first circle be? " ))




def draw_circle():
    pendown()
    begin_fill()
    color("gray")
    circle(first_radius)
    end_fill()
penup()
setposition(0,-200)
for i in range(3):
    draw_circle()
    left(90)
    forward(first_radius*2)
    right(90)
    first_radius = first_radius/2
