import turtle

def drawEqShape(): 
  "takes a turtle object, num_sides, and side_length as parameters. The function should use the turtle object to draw a shape according to the parameters."

def drawEqShape(jake,num_sides,side_length):
     for i in range(num_sides):
         jake.fd(side_length)
         jake.left(360/num_sides)



jake=turtle.Turtle()
screen=turtle.Screen()
jake.shape("turtle")
jake.color("green")
num_sides=int(input("please enter the number of sides:"))
side_length=int(input("please enter the length of the sides:"))

drawEqShape(jake,num_sides,side_length)
screen.exitonclick()

