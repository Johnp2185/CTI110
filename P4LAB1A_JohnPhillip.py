#Phillip John
#28 Mar 24
#P4LAB1A
#A program that uses turtle graphics to draw a triangle and square.

import turtle
# Set up the window and its attributes
wn = turtle.Screen()                    
wn.bgcolor("red")
wn.title("Triangle & Square")
t = turtle.Turtle()
for i in range(4):
    
# Pen attributes
    triangle = turtle.Turtle()              
    triangle.color("yellow")                # set pencolor
    triangle.pensize(8)                     # set pensize
    triangle.shape("turtle")                # set penshape

    square = turtle.Turtle()                
    square.color("green")                   # set pencolor
    square.pensize(7)                       # set pensize
    square.shape("turtle")                  # set penshape

# Make triangle draw triangle
    triangle.forward(80)                   
    triangle.left(120)
    triangle.forward(80)
    triangle.left(120)
    triangle.forward(80)
    triangle.left(120)                      # Complete the triangle
     
# Make square draw a square
    square.forward(50)                      
    square.left(90)
    square.forward(50)
    square.left(90)
    square.forward(50)
    square.left(90)
    square.forward(50)
    square.left(90)

wn.mainloop()                               # Wait for user to close window
