from Snappy import TheProject
from Snappy import Sprite

import random

class ScaredTurtle(Sprite):

    def WhenIAmClicked(self):
        self.PenDown()
        self.TurnClockwise(random.randrange(-179,180))
        self.Move(50)



TheProject.AddSprite(ScaredTurtle())

TheProject.Run()
