import turtle

turtle.Screen().bgcolor("red")

sc=turtle.Screen()
sc.setup(400,300)

t1=turtle.Turtle()
for i in range(4):
    t1.forward(100)
    t1.right(90)
    i=i+1

turtle.done()