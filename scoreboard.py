from turtle import Turtle
# Constants 
ALIGMENT = "center"
FONT = ("Courier", 15, "normal")

# score board class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\Program Files\Installation\VSCodeProjects\SnakeGame\data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.hideturtle()
        self.update_scoreboard

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", align=ALIGMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\Program Files\Installation\VSCodeProjects\SnakeGame\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    # this function update & adding score number to scoreboard    
    def add_score(self):
        self.score += 1
        # clear previous score number
        self.update_scoreboard()