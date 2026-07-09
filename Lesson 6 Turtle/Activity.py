import turtle 
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

borad=turtle.Turtle()
borad.speed ("fastest")
borad.hideturtle()

colors =["red","orange","yellow","lime","cyan","violet","pink","white"]
for i in range(80):
    borad.color(colors[i%len(colors)])
    borad.width(2)
    borad.forward(i*2)
    borad.right(91)

borad.penup()
borad.goto(0.-60)
borad.setheading(90)
borad.pendown()
borad.color("gold","yellow")
borad.begin_fill()
for i in range(5):
    borad.forward(130)
    borad.right(144)
borad.end_fill

borad.penup()
borad.goto(0,0)
borad.pendown()
petal_colors=["orange","lime","cyan","violet","deeppink",]
for i in range(36):
 borad.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i + 2) % len(petal_colors)])
 borad.begin_fill()
for j in range(4):
        borad.forward(55)
        borad.right(90)
borad.end_fill()
borad.right(10)
turtle.done()