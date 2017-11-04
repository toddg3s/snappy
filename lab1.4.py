from Snappy import *

class dragon(Sprite):

    def __init__(self):
        super().__init__()
        self.Name = 'dragon'
        self.AddCostume('dragon1-a.png')
        self.AddCostume('dragon1-b.png')
        self.SetRotation(rotation.leftRightOnly)

    def WhenStarted(self):
        self.GoTo((-200,140))
        self.SwitchToCostume('dragon1-a')
        self.PointInDirection(90)

    def When_f_Pressed(self):
        if self.CurrentCostume == 'dragon1-a':
            self.Broadcast('roar')
            self.PointTowards((TheProject.MouseX,TheProject.MouseY))
            self.Glide(1,TheProject.MouseX,TheProject.MouseY)
            self.SwitchToCostume('dragon1-b')
            self.Wait(1)
            self.SwitchToCostume('dragon1-a')


class alonzo(Sprite):

    def __init__(self):
        super().__init__()
        self.Name = 'alonzo'
        self.AddCostume('alonzo.png')
        self.SetRotation(rotation.leftRightOnly)

    def WhenStarted(self):
        self.GoTo((135,43))
        self.PointInDirection(-90)

    def WhenIReceive(self,message):
        if message == 'roar':
            if self.DistanceTo('dragon') < 80:
                self.Say("Yikes!", 0.5)
                self.PointInDirection(TheProject.Sprites['dragon'].Direction * -1)
                self.Glide(1,TheProject.MouseX * -1, TheProject.MouseY * -1)
            else:
                self.Think("Ho hum", 1)


TheProject.AddSprite(dragon())
TheProject.AddSprite(alonzo())
TheProject.Run()