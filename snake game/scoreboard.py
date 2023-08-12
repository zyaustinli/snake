from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(r"C:\udemy projects\snake game\data.txt") as data:
            self.high_score = int(data.read())


        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update()
        self.hideturtle()
        


    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, 'normal'))



    def increase_score(self):
        self.score+= 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\udemy projects\snake game\data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update()
