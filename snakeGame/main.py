import turtle, time, random

delay = 0.1
score = 0
high_score = 0

# Creates a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# Setting width and height of the screen
wn.setup(width=600, height=600)
wn.tracer(0)

# Creating head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food in the game
food = turtle.Turtle()
colors = random.choice(["red", "green", "yellow"])
shapes = random.choice(["circle", "square", "triangle"])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center", font=("candria", 24, 'bold'))

# Assigning key directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")

segments = []

while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['circle', 'square'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score : {score} High score: {high_score}", align="center", font=("candara", 24, "bold"))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

        # Adding segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")  # Color of tail
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001

