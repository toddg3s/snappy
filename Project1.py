from Snappy import *

class Line:
    Text = ""
    Length = 1.0

    def __init__(self,text,length):
        self.Text = text
        self.Length = length

class Actor(Sprite):

    Lines = []
    Linenumber = 0
    Responder = False

    def __init__(self):
        super().__init__()
        with open('whosonfirst.txt') as script:
            for line in script:
                parts = line.split(':')
                if parts[0] == self.Name:
                    words = parts[1].split(' ')
                    self.Lines.append(Line(parts[1], len(words) * 0.5))

    def WhenIReceive(self,message):
        if message.startswith(self.Name):
            return
        self.Linenumber = int(message.split('.')[1])
        self.SpeakLine()

    def SpeakLine(self):
        self.Say(self.Lines[self.Linenumber].Text, self.Lines[self.Linenumber].Length)
        self.Broadcast("%s.%d" % (self.Name,self.Linenumber + int(self.Responder)))


class Abbott(Actor):

    def __init__(self):
        self.Name = "Abbott"
        super().__init__()
        self.Responder = True
        self.GoTo((-100,80))
        # set costumes, etc.

    def WhenStarted(self):
        pass
        #initial animations

    def WhenIReceive(self,message):
        super().WhenIReceive(message)
        if self.Linenumber == 1:
            pass  # animations

class Costello(Actor):

    def __init__(self):
        self.Name = "Costello"
        super().__init__()
        self.GoTo((100,-80))
        # set costumes, etc.

    def WhenStarted(self):
        #inifial animation
        self.SpeakLine()


    def WhenIReceive(self,message):
        super().WhenIReceive(message)
        if self.Linenumber == 1:
            pass


TheProject.AddSprite(Abbott())
TheProject.AddSprite(Costello())
TheProject.Run()