from turtle import Turtle
# CONSTANT Variables start position , dictance of move
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# class snake
class Snake:
    # init where include all inner variables of class.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # this function make snake each time call. ( startin 3 length square )
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # customize snake
            new_segment = Turtle(shape="square")
            new_segment.color("white")
        # pen up
            new_segment.penup()
        # go to right position and adding new one in snake's life LIST
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # move function where first square is HEAD and other ones follow step by step
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # head moving forward 20PX every time while game is on. 
        self.head.forward(MOVE_DISTANCE)


    # Direction function which change it by ARROW key button. 
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