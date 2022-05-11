import turtle
import random

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.setworldcoordinates(-500,-500,500,500)
screen.bgcolor('blue')
screen.tracer(0, 0)
turtle.hideturtle()
turtle.up()
turtle.color('red')
score_turtle = turtle.Turtle()
score_turtle.color('red')
score_turtle.up()
score_turtle.hideturtle()


min_speed = 5
max_speed = 10
letters = []
speeds = []
pos = []
lts = []
n = 10

score = 0


def increase_difficulty():
    global min_speed, max_speed
    min_speed += 1
    max_speed += 1
    screen.ontimer(increase_difficulty, 3500)


def draw_game_over():
    turtle.goto(0, 0)
    turtle.color('red')
    turtle.write('GAME OVER', align='center', font=('Courier', 50, 'normal'))
    turtle.goto(0, -150)
    turtle.color('orange')
    turtle.write('Your Score is '+str(score), align='center', font=('Courier', 40, 'normal'))
    screen.update()



def draw_score():
    score_turtle.clear()
    score_turtle.goto(350, 400)
    score_turtle.write('Score : '+str(score), align='center', font=('Courier', 25, 'normal'))
    screen.update()


def draw_letters():
   
    for i in range(len(letters)):
        lts[i].clear()
        lts[i].goto(pos[i])
        lts[i].write(letters[i], align='center', font=('courier', 20, 'normal'))
        pos[i][1] -= speeds[i]
        if pos[i][1] < -500:
            draw_game_over()
            return
    screen.update()
    screen.ontimer(draw_letters, 10)


def f(c):
    global score
    if c in letters:
        score += 1
        k = letters.index(c)
        while True:
            l = chr(ord('a') + random.randrange(1,26))
            if l not in letters:
                letters[k] = l
                break
        pos[k] = [random.randint(-450, 450), 500]
        speeds[k] = random.randint(min_speed, max_speed)
    else:
        score -= 1
    draw_score()


for _ in range(n):
    lts.append(turtle.Turtle())
    while True:
        l = chr(ord('a') + random.randrange(26))
        if l not in letters:
            letters.append(l)
            break
    speeds.append(random.randint(min_speed, max_speed))
    pos.append([random.randint(-450, 450), 500])

for i in range(n):
    lts[i].speed(0)
    lts[i].hideturtle()
    lts[i].up()
    lts[i].color('yellow')

draw_letters()
increase_difficulty()



screen.onkey(lambda: f('a'), 'a')
screen.onkey(lambda: f('b'), 'b')
screen.onkey(lambda: f('c'), 'c')
screen.onkey(lambda: f('d'), 'd')
screen.onkey(lambda: f('e'), 'e')
screen.onkey(lambda: f('f'), 'f')
screen.onkey(lambda: f('g'), 'g')
screen.onkey(lambda: f('h'), 'h')
screen.onkey(lambda: f('i'), 'i')
screen.onkey(lambda: f('j'), 'j')
screen.onkey(lambda: f('k'), 'k')
screen.onkey(lambda: f('l'), 'l')
screen.onkey(lambda: f('m'), 'm')
screen.onkey(lambda: f('n'), 'n')
screen.onkey(lambda: f('o'), 'o')
screen.onkey(lambda: f('p'), 'p')
screen.onkey(lambda: f('q'), 'q')
screen.onkey(lambda: f('r'), 'r')
screen.onkey(lambda: f('s'), 's')
screen.onkey(lambda: f('t'), 't')
screen.onkey(lambda: f('u'), 'u')
screen.onkey(lambda: f('v'), 'v')
screen.onkey(lambda: f('w'), 'w')
screen.onkey(lambda: f('x'), 'x')
screen.onkey(lambda: f('y'), 'y')
screen.onkey(lambda: f('z'), 'z')
screen.listen()


screen.mainloop()
