from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        # self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
    def increase(self):
        self.score+=1
        self.clear()
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
