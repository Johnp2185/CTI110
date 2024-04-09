#Phillip John
#28 Mar 24
#P4LAB1B
#A program that uses turtle graphics to draw my initials.

import turtle
wn = turtle.Screen()                        # Set up the window and its attributes
wn.bgcolor("green")
wn.title("PJ")
for i in range(99):

    
# set attributes
    p = turtle.Turtle()                     
    p.color("red")                          # set pencolor
    p.pensize(10)                           # set pensize
    p.shape("turtle")                       # set penshape

# create J
    j = turtle.Turtle()               
    j.color("yellow")                       # set pencolor
    j.pensize(10)                           # set pensize
    j.shape("turtle")                       # set penshape

# Draw P
    p.circle(80,180)                     
    p.left(90)
    p.forward(250)                          # Complete the P

#Draw J
    j.penup()
    j.forward(200)
    j.pendown()
    j.forward(100)                      
    j.backward(200)
    j.forward(100)
    j.right(90)                              
    j.forward(120)
    j.circle(-60,200)                       # Complete the J

wn.mainloop()                               # Wait for user to close window
