import Snappy
import pygame

class Moveable(Snappy.Sprite):
    def When_f_Pressed(self):
        self.GoToFront()

    def When_b_Pressed(self):
        self.GoBack(1)

for i in range(10):
    s = Snappy.Sprite()
    s.Name = "Layer%d" % i
    s.GoToPoint(i * 10, i * 10)
    Snappy.TheProject.AddSprite(s)

m = Moveable()
img = pygame.Surface((100, 100), 0, 32)
img.fill(pygame.Color("blue"))
m.AddCostume(img)
m.NextCostume()
m.GoToPoint(50,50)
Snappy.TheProject.AddSprite(m)
Snappy.TraceLevel = Snappy.tracelevel.Debug

Snappy.TheProject.Run()
