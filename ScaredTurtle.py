
from Snappy import *
import random


class ScaredTurtle(Sprite):

    clickCount = 0

    def WhenStarted(self):
        self.Say("Hi!",0.5)

    def WhenIAmClicked(self):
        self.SetPenSize(10)
        self.SetPenColor(random.randrange(200))
        self.clickCount += 1
        if self.clickCount == 3:
            self.clickCount = 0
            self.AskAndWait("Are you stalking me?")
            if TheProject.Answer.lower() != "yes":
                self.Say("Oh, okay.", 1)
                return
        self.PenDown()
        self.Say("Yikes!", 0.5)
        x = random.randrange(-240, 240)
        y = random.randrange(-180, 180)
        self.PointTowards((x, y))
        self.Glide(2, x, y)

    def WhenIAmMouseEntered(self):
        self.Think("Uh oh...", 1)

    def When_space_Pressed(self):
        self.Clear()

    def When_t_Pressed(self):
        self.PlayNote(40, 0.5)

    def WhenKeyPressed(self, key):
        if key != "return":
            self.Say("You pressed %s!" % key, 2)

    def When_d_Pressed(self):
        self.Glide(2,self.Location[0],self.Location[1] - 50)

    def When_0_Pressed(self):
        self.SetRotation(rotation.canRotate)

    def When_1_Pressed(self):
        self.SetRotation(rotation.leftRightOnly)

    def When_2_Pressed(self):
        self.SetRotation(rotation.noRotation)

TheProject.AddSprite(ScaredTurtle())
TheProject.Run()
