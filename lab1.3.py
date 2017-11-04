from Snappy import *

class shapes(Sprite):

    def When_space_Pressed(self):
        self.Clear()

    def When_1_Pressed(self):
        self.PenDown()
        self.SetPenColor('blue')
        self.SetPenSize(10)
        for i in range(4):
            self.Move(50)
            self.TurnCounterClockwise(90)
        self.PenUp()

    def When_2_Pressed(self):
        self.PenDown()
        self.SetPenColor('red')
        self.SetPenSize(5)
        for i in range(3):
            self.Move(50)
            self.TurnCounterClockwise(120)
        self.PenUp()

    def When_3_Pressed(self):
        self.PenDown()
        self.SetPenColor('green')
        self.SetPenSize(3)
        self.TurnCounterClockwise(45)
        for i in range(4):
            self.Move(50)
            self.TurnCounterClockwise(90)
        self.PenUp()
        self.TurnClockwise(45)

    def When_4_Pressed(self):
        self.PenDown()
        self.SetPenColor('purple')
        self.SetPenSize(12)
        for i in range(5):
            self.Move(50)
            self.TurnCounterClockwise(72)
        self.PenUp()

    def When_5_Pressed(self):
        self.PenDown()
        self.SetPenColor('orange')
        self.SetPenSize(10)
        self.Move(50)
        self.TurnCounterClockwise(45)
        self.Move(30)
        self.TurnCounterClockwise(135)
        self.Move(50)
        self.TurnCounterClockwise(45)
        self.Move(30)
        self.TurnCounterClockwise(135)
        self.PenUp()

    def When_6_Pressed(self):
        self.PenDown()
        self.SetPenColor('black')
        self.SetPenSize(2)
        for i in range(5):
            self.Move(50)
            self.TurnCounterClockwise(145)
        self.PenUp()

    def When_up_Pressed(self):
        self.ChangeY(10)

    def When_down_Pressed(self):
        self.ChangeY(-10)

    def When_left_Pressed(self):
        self.ChangeX(-10)

    def When_right_Pressed(self):
        self.ChangeX(10)

TheProject.AddSprite(shapes())
TheProject.Run()
