from Snappy import *

class stage(StageSprite):
    def When_space_Pressed(self):
        self.Clear()


class sprite1(Sprite):
    def WhenStarted(self):
        self.PenDown()
        self.SetPenColor('blue')
        self.Hide()
        while True:
            self.GoTo((TheProject.MouseX * -1, TheProject.MouseY))

class sprite2(Sprite):
    def WhenStarted(self):
        self.PenDown()
        self.SetPenColor('red')
        self.Hide()
        while True:
            self.GoTo((TheProject.MouseX * -1, TheProject.MouseY * -1))

class sprite3(Sprite):
    def WhenStarted(self):
        self.PenDown()
        self.SetPenColor('green')
        self.Hide()
        while True:
            self.GoTo((TheProject.MouseX, TheProject.MouseY * -1))

class sprite4(Sprite):
    def WhenStarted(self):
        self.PenDown()
        self.SetPenColor('purple')
        self.Hide()
        while True:
            self.GoTo((TheProject.MouseX, TheProject.MouseY))

TheProject.SetTheStage(stage())
TheProject.AddSprite(sprite1())
TheProject.AddSprite(sprite2())
TheProject.AddSprite(sprite3())
TheProject.AddSprite(sprite4())

TheProject.Run()