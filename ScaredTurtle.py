from Snappy import TheProject
from Snappy import Sprite

class ScaredTurtle(Sprite):

    def WhenIAmClicked(self):
        self.Move(50)


TheProject.AddSprite(ScaredTurtle())

TheProject.Run()