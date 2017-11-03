import Snappy
import random

class lab04(Snappy.Sprite):
    def When_space_Pressed(self):
        self.Say('My name is Snappy', 1)
        self.GoTo((random.randrange(-100,100),random.randrange(-100,100)))
        self.Say("I'm only a few weeks old",1)
        self.GoTo((random.randrange(-100,100),random.randrange(-100,100)))
        self.TurnClockwise(20)
        self.Say("I've never attended school",1)
        self.Glide(random.randrange(-100,100),random.randrange(-100,100),1)
        self.Say("I hope to become part of TEALS curriculum")

Snappy.TheProject.AddSprite(lab04())
Snappy.TheProject.Run()
