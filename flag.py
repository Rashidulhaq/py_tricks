import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()



def draw_bangladeshi_flag():
    turtle.speed(3)
    
    # Drawing the flagpole/stick (black color)
    turtle.penup()
    turtle.goto(-300, -310)  # Adjust the starting position for the flagpole
    turtle.pendown()
    turtle.color("orange")
    turtle.pensize(4)
    turtle.left(90)
    turtle.forward(400)
    turtle.backward(200)


    
    # Drawing the green rectangle
    draw_rectangle("#006A4E", 300, 400)
    
    # Drawing the red circle
    draw_circle("#F42A41", 80, -20, 40)
    
    # Hiding the turtle after drawing
    turtle.hideturtle()
    
    # Keep the window open
    turtle.done()

if __name__ == "__main__":
    draw_bangladeshi_flag()
