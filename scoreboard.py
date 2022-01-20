FONT = ("Courier", 24, "normal")
class Scoreboard():
    def __init__(self):
        self.level=1
        self.speed=10

    def increaseLevel(self):
        self.speed+=5
        self.level+=1

