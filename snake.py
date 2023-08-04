from turtle import Turtle, Screen

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.list_of_turtles = []
        self.create_turtle()
        self.head = self.list_of_turtles[0]

    def create_turtle(self):
        for turtle in POSITION:
            self.increase_size(turtle)

    def increase_size(self, position_a):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()

        new_turtle.goto(position_a)
        self.list_of_turtles.append(new_turtle)

    def extend(self):
        self.list_of_turtles[-1].speed("fastest")
        self.increase_size(self.list_of_turtles[-1].position())

    def move(self):
        for turtle in range(len(self.list_of_turtles) - 1, 0, -1):
            new_x = self.list_of_turtles[turtle - 1].xcor()
            new_y = self.list_of_turtles[turtle - 1].ycor()
            self.list_of_turtles[turtle].goto(new_x, new_y)

        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
