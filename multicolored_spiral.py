import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
color=("red","yellow","purple","pink","green","blue")
for i in range(300):
    t.pencolor(color [i % 6])
    t.forward (i*2)
    t.right(61)
turtle.done()