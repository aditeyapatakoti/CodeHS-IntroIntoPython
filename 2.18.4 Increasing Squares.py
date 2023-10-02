length = 25
speed(0)


penup()
backward(10)
def draw_square():
    pendown()
    for i in range(4):
        forward(length)
        left(90)
    forward(length/2)
    penup()
    right(90)
    forward(12.5)
    left(90)
    

while length<= 350:
    draw_square()
    length=length+25
    backward(length/2)

    
draw_square()
