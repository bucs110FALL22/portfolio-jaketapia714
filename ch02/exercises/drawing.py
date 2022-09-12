import turtle
length=int(input("please enter the length of the sides:"))
sides=int(input("please enter the number of sides:"))
mt=turtle.Turtle()
mt.shape("turtle")
screen=turtle.Screen()
mt.color("red")
for i in range(sides):
  mt.fd(length)
  mt.left(360/sides)
screen.exitonclick()