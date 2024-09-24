""" 
circle pyramids are pretty cool
"""
#Will draw a pyramid made of circles with three rows
#Resets da code too make it as fast as possible
speed(0)
penup()
#Creates da first circle for the first row of da circle pyramid and moves it in da first position
setposition(0,-30)
pendown()
circle(50)
penup()
#Creates da second row of circles for da circle pyramid and uses a for loop
setposition(-50,-115)
for i in range(2):
  pendown()
  circle(50)
  penup()
  forward(100)
#Creates da final row for da circle pyramid and also uses a for loop
setposition(-100,-200)
for i in range(3):
  pendown()
  circle(50)
  penup()
  forward(100)

