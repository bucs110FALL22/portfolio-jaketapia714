from turtle import Turtle, Screen

jake=Turtle()
screen=Screen()
# num_sides=int(input("please enter the number of sides:"))
jake.shape("turtle")
jake.color("purple")
length=50
# angle=360/num_sides
# for i in [angle]*num_sides:
#   jake.fd(length)
#   jake.left(i) 
# screen.exitonclick()

for i in range(4):
  jake.fd(length)
  jake.left(90)

jake.up()
jake.color("red")
jake.fd(length)
jake.down()
for i in range(4):
  jake.fd(length)
  jake.left(90)

screen.exitonclick()
