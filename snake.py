from turtle import Turtle
STARTING_POSITIONS = [(-5, 5), (-25, 5), (-45, 5)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.red = 255
        self.green = 255
        self.blue = 255
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        if self.red < 1 or self.green < 1:
            self.blue -= 5
        else:
            self.red -= 5
            self.green -= 5
        new_segment.color(self.red, self.green, self.blue)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.tail.pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_segment = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setpos(next_segment)
        self.head.forward(MOVE_DISTANCE)

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
