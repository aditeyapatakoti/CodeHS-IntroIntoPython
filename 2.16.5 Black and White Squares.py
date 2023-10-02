penup()
setposition (-50,0)
count = 1
def draw_square():
    for i in range(4):
        pendown()
        forward(25)
        left(90)
    penup()
    forward(35)

for i in range(6):
    if count % 2 == 0:
       draw_square()
       count = count - 1
    else:
        begin_fill()
        color("black")
        draw_square()
        end_fill()
        count = count + 1
