import turtle
import random
jake=turtle.Turtle()
jake.color("blue")
jake.shape("turtle")
jake.setpos(0,0)
window=turtle.Screen()
turtle.screensize(width=1000,height=1000)
width= turtle.window_width()
height= turtle.window_height()

while abs(jake.xcor())<(width/2) and abs(jake.ycor())<(height/2):
  result=random.randrange(2)
  if result ==1:
    jake.left(90)
    jake.forward(50)
    print("heads")
  else:
    jake.right(90)
    jake.forward(50)
    print("tails")
