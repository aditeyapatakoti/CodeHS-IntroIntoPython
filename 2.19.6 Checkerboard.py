speed(0)
penup()
setposition (-200,-200)
count = 1
def draw_square():
    for i in range(4):
        pendown()
        forward(40)
        left(90)
    penup()
    forward(40)

   
for i in range(10):
    for i in range(10):
        if count % 2 == 0:
            begin_fill()
            color("black")
            draw_square()
            end_fill()
            count = count - 1
        else:
            begin_fill()
            color("red")
            draw_square()
            end_fill()
            count = count + 1
    penup()
    left(90)
    forward(40)
    left(90)
    forward(400)
    right(180)
    count = count + 1
