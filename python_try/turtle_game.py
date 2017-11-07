import turtle 

# need randomness 
import random 


my_turtle = turtle.Turtle() 
my_turtle.speed(0) 

#set color list# 
my_colors = ["Black", "Red", "Green", "Blue"] 


def square(length, angle): 
    for i in range (4): 
        my_turtle.forward(length) 
        my_turtle.right(angle) 


for i in range(1000): 

# In Living color!! 
    pcolor = random.choice(my_colors) 

    my_turtle.pencolor(pcolor) 
    square(100, 90) 
    my_turtle.right(11) 







#mine
    print("hello")
import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
def draw(a,b):
   # my_turtle.forward(a)
    #my_turtle.left(b)
    #my_turtle.forward(a)
    #my_turtle.left(b)
    #my_turtle.forward(a)
    #my_turtle.left(b)
    #my_turtle.forward(a)
    for i in range(4):
        my_turtle.forward(a)
        my_turtle.left(b)


#draw(12,90)
#my_turtle.forward(100)
for i in range(400):
     draw(70,90)
     my_turtle.left(11)
