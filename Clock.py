import turtle
import datetime
from datetime import datetime as e

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(0, 0)
screen.bgcolor('#17BEBB')
face = turtle.Turtle()
hand = turtle.Turtle()
face.hideturtle()
hand.hideturtle()


def draw_face():
    face.clear()
    face.penup()
    face.goto(0, -700)
    face.pensize(5)
    face.pendown()
    face.fillcolor('white')
    face.begin_fill()
    face.circle(700)
    face.end_fill()
    face.penup()
    face.goto(0, 0)
    face.dot(10)
    face.pensize(2)
    for angle in range(0, 360, 6):
        face.penup()
        face.goto(0, 0)
        face.setheading(90 - angle)
        face.forward(620)
        face.pendown()
        face.forward(30)
    face.pensize(4)
    for angle in range(0, 360, 30):
        face.penup()
        face.goto(0, 0)
        face.setheading(90 - angle)
        face.forward(600)
        face.pendown()
        face.forward(50)


def draw_hand():
    hand.clear()
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90 - ((hour % 12 * 30)+((30*minute)//60)))
    hand.pendown()
    hand.color('black')
    hand.pensize(6)
    hand.forward(375)

    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90 - ((minute * 6)+((6*(second))//60)))
    hand.pendown()
    hand.color('black')
    hand.pensize(4)
    hand.forward(550)

    hand.penup()
    hand.color('red')
    hand.goto(0, 0)
    hand.dot(5)
    hand.setheading(90-((second * 6)+((6*millisecond)//100000)))
    hand.pendown()
    hand.pensize(2)
    hand.forward(600)


def animate():
    global c, hour, minute, second, millisecond
    d = datetime.datetime.now()
    hour = d.hour
    minute = d.minute
    second = d.second
    millisecond = int(e.now().strftime('%f')[:-1])


    draw_hand()
    screen.update()
    screen.ontimer(animate, 1)


draw_face()
animate()
turtle.Screen().exitonclick()
