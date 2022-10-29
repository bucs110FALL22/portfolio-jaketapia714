import turtle

height=800
width=600

screen=turtle.Screen()
screen.screensize(height,width)

leonardo=turtle.Turtle()
leonardo.color("black")
leonardo.shape("turtle")
leonardo.speed(0)

def fill_in(x="color"):
  '''
    makes turtle color
    turtle object starts to draw
    turtle fills in polygons
    '''
  leonardo.fillcolor(x)
  leonardo.begin_fill()

def move_turtle(x):
  '''
  moving the turtle without lines
  turtle object is lifted up, moved, then put down
  turtle moves from point a to point b without lines
  '''
  leonardo.penup()
  leonardo.goto(x)
  leonardo.pendown()
  return

def feathers(r = 100, angle=90, n=7):
  '''
   makes the feathers of a native american hat
   makes half a feather, then the other half, colors it brown
   makes 7 feathers behind the head
  '''
  for i in range(n):
    for i in range(2):
      leonardo.fillcolor("brown")
      leonardo.begin_fill()
      leonardo.circle(r,angle)
      leonardo.left(180-angle)
      leonardo.end_fill()
    leonardo.left(15)
  return  

def head(x="color", y=0):
  '''
  makes the turtle draw the outline of a head
  input the color and radius of a circle so turtle can draw one
  filled in circle with color and radius of choice
  '''
  fill_in(x)
  leonardo.circle(y)
  leonardo.end_fill()

move_turtle((0,50))
feathers()
leonardo.right(105)

move_turtle((0,0))
head("beige",50)

eye_coords = ((-25,50),(25,50))
leonardo.fillcolor("white")
for i in eye_coords:
  move_turtle(i)
  leonardo.begin_fill()
  leonardo.circle(10)
  leonardo.end_fill()

eye_coords = ((-25,50),(25,50))
leonardo.fillcolor("black")
for i in eye_coords:
  move_turtle(i)
  leonardo.begin_fill()
  leonardo.circle(2.5)
  leonardo.end_fill()


mouth_coords = ((-20,30))
move_turtle(mouth_coords)
leonardo.forward(40)

screen.exitonclick()