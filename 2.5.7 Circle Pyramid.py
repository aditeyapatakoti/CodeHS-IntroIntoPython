speed(0)
penup()
setposition(0,-30)
def drawcircle():
    pendown()
    circle(50)
    penup()
setposition(-50,-115)
for i in range(2):
    drawcircle()
    forward(100)
setposition(-100,-200)
for i in range(3):
    drawcircle()
    forward(100)
