speed(0)
penup()
row_value=0
radius = 25

  
def move_to_row(num_blocks):
    x_value = -((num_blocks*50)/2) + radius
    y_value = -200+(50*row_value)
    setposition(x_value,y_value)


def draw_block_row(num_blocks):
    for i in range(num_blocks):
        pendown()
        circle(radius)
        penup()
        forward(50)


num_blocks=int(input("How many blocks on the bottom row? (8 or less): "))


for i in range(num_blocks):
    move_to_row(num_blocks)
    row_value=row_value+1
    draw_block_row(num_blocks)
    num_blocks=num_blocks-1
