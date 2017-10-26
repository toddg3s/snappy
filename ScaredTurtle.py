
import Snappy
import random


class ScaredTurtle(Snappy.Sprite):

    clickCount = 0

    def WhenIAmClicked(self):
        self.clickCount += 1
        if self.clickCount == 3:
            self.clickCount = 0
            self.AskAndWait("Are you stalking me?")
            if Snappy.TheProject.Answer.lower() != "yes":
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

    def WhenKeyPressed(self, key):
        self.Say("You pressed %s!" % key, 2)


Snappy.TheProject.AddSprite(ScaredTurtle())
Snappy.TraceLevel = Snappy.tracelevel.Info
Snappy.TheProject.Run()
