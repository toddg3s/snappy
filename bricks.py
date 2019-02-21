import Snappy

class BrickLayer(Snappy.Sprite):

    offset = 0

    def When_r_Pressed(self):
        self.drawrow()

    def When_w_Pressed(self):
        for i in range(5):
            self.drawrow()

    def When_space_Pressed(self):
        self.Clear()
        self.GoTo((-240,-160))
        self.Hide()

    def When_s_Pressed(self):
        self.PenDown()
        self.SetPenSize(15)
        for i in range(4):
            self.Move(50)
            self.TurnCounterClockwise(90)
        self.SetPenSize(1)

    def When_t_Pressed(self):
        self.PenDown()
        for i in range(4):
            self.Move(50)
            self.TurnClockwise(90)


    def drawrow(self):
        while self.Location[0] < 240:
            self.drawbrick()
            self.PointInDirection(90)
            self.Move(20)
        self.offset = 10 if self.offset == 0 else 0
        self.GoTo((-240 - self.offset, self.Location[1] + 10))

    def drawbrick(self):
        self.SetPenColor('red')
        self.PenDown()
        self.PointInDirection(90)
        self.Move(20)
        self.PointInDirection(0)
        self.Move(10)
        self.PointInDirection(-90)
        self.Move(20)
        self.PointInDirection(180)
        self.Move(10)
        self.PenUp()

Snappy.TheProject.AddSprite(BrickLayer())
Snappy.TraceLevel = Snappy.tracelevel.Debug
Snappy.TheProject.Run()

