from turtle import *
from random import randint as r

"""
CLASS AND FUNCTION DEFINITIONS
"""
def box(turtle, x,y,color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    
def checkerboard():
    count=0
    t = Turtle()
    t.speed(0)
    t.ht()
    t.penup()
    t.goto(-200,200)
    for y in range(200,-200,-40):
        for x in range(-200,200,40):
            if count%2==0:
                box(t,x,y, ("light green"))
            else:
                box(t,x,y,("light blue"))
            count+=1
        count+=1

class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.ht()
        self.shape("apple.gif")
        self.speed(0)
        self.penup()
        self.goto(r(-180,180),r(-180,180))
        self.st()

    def move(self):
        self.ht()
        self.goto(r(-180,180),r(-180,180))
        self.st()

class Head(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.speed(0)
        self.ht()
        self.penup()
        self.color('dark red')
        self.shape("square")
        self.direction = 0
        self.velocity = 20
        self.goto(-175,0)
        self.st()
        self.score = 0
        self.screen = screen
        self.speed(1)
        self.screen.onkey(self.north, "Up")
        self.screen.onkey(self.south, "Down")
        self.screen.onkey(self.west, "Left")
        self.screen.onkey(self.east, "Right")

    def move(self, snake):
        if self.check_for_death(snake):
            self.die(snake)
        self.speed(0)
        self.setheading(self.direction)
        self.speed(1)
        # self.speed(self.velocity)
        self.forward(self.velocity)
        
    def die(self, caterpillar):
        for j in range(len(caterpillar)-1,-1,-1):
            caterpillar[j].ht()
            caterpillar.pop(j)

    def check_for_death(self,snake):
        if self.xcor()>190 or self.xcor()<-190 or self.ycor()<-190 or self.ycor()>190:
            return True
        for i in range(7, len(snake)):
            if self.distance(snake[i])<15:
                return True
        return False
        
    def north(self):
        if self.direction != -90:
            self.direction = 90

    def south(self):
        if self.direction != 90:
            self.direction = -90

    def east(self):
        if self.direction != 180:
            self.direction = 0

    def west(self):
        if self.direction != 0:
            self.direction = 180

class Segment(Turtle):
    def __init__(self,color):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color(color)
        self.shape("square")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0,230)

    def display(self, text):
        self.clear()
        self.write("Score: "+str(text), align = "center", font=("Times New Roman",40))

    def game_over(self):
        self.clear()
        self.color("red")
        self.write("GAME OVER!", align = "center", font=("Times New Roman",40))


class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.ht()
        self.pu()
        self.index = 0
        self.shape("square")
        self.goto(r(-180,180),r(-180,180))
        self.st()

def update():
    global speed
    if play:
        if len(snake)>0:
            snake[0].move(snake)
            if snake[0].distance(apple)<20:
                    apple.move()
                    snake[0].score += 1
                    score.display(snake[0].score)
                    snake[0].velocity += 1
                    if snake[0].velocity % 10 == 0:
                        speed += 0.2
                        screen.tracer(speed)
                    snake.append(Segment("orange"))
                    snake.append(Segment("red"))
                    if len(snake)%10==0:
                        snake[0].velocity +=1
            for i in range(len(snake)-1, 0, -1):
                snake[i].goto(snake[i-1].xcor(), snake[i-1].ycor())
        else:
            score.game_over()
    screen.ontimer(update,50)

def start():
    global play
    play = True
"""
SCREEN
"""
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.register_shape('apple.gif')
screen.listen()
screen.onkey(start,"space")
checkerboard()
speed = 1
screen.tracer(speed)
score = ScoreBoard()
play = False
"""
TURTLE AND OBJECT INSTANTIATION
"""
apple = Apple()
snake = [Head(screen)]
obstacles = [Obstacle(),Obstacle(),Obstacle()]
score.display(snake[0].score)
"""
GAME LOOP
"""
speed = 2
update()

screen.mainloop()      
    


