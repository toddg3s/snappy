
import Snappy

import random

class ScaredTurtle(Snappy.Sprite):

    def WhenIAmClicked(self):
        self.PenDown()
        self.Say("Yikes!",0.5)
        x = random.randrange(-240,240)
        y = random.randrange(-180,180)
        print("heading to %d,%d" % (x,y))
        self.PointTowards((x,y))
        self.Glide(2,x,y)

    def WhenIAmMouseEntered(self):
        self.Think("Uh oh...", 1)

    def When_space_Pressed(self):
        self.Clear()

    def WhenKeyPressed(self,key):
        self.Say("You pressed %s!" % key, 2)

Snappy.TheProject.AddSprite(ScaredTurtle())
Snappy.TraceLevel = Snappy.tracelevel.Info
Snappy.TheProject.Run()
