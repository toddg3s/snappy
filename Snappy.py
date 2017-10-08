import pygame
from pygame import image

import threading
import os
import math

class StageSprite:

    Costumes = { }
    CurrentCostume = ""

    Saying = ""
    Thinking = ""

    Hidden = False

    def __init__(self):
        pass

# Looks

    def SwitchToCostume(self,name):
        if name in self.Costumes:
            CurrentCostume = name
            self.Size = self.Costumes[self.CurrentCostume].get_size()
        else:
            CurrentCostume = ""
            self.Size = (56,40)

    def NextCostume(self):
        keys = sorted(self.Costumes)
        index = keys.index(self.CurrentCostume)
        index += 1
        if(index > len(self.Costumes)):
            index = 0
        CurrentCostume = keys[index]
        self.Size = self.Costumes[self.CurrentCostume].get_size()

    def Show(self):
        self.Hidden = False

    def Hide(self):
        self.Hidden = True

# Sensing

    def MouseDown(self):
        return False

    def KeyPressed(self,key):
        return False

    def DistanceTo(self,item):
        pass

    def Current(self,timeelement="date"):
        pass

    def AskAndWait(self,prompt):
        return ""

# Pen

    def Clear(self):
        pass

# Control

    def WhenKeyPressed(self,key):
        pass

    def WhenIAmClicked(self):
        pass

    def WhenIAmPressed(self):
        pass

    def WhenIAmDropped(self):
        pass

    def WhenIAmMouseEntered(self):
        pass

    def WhenIAmMouseDeparted(self):
        pass

    def WhenIReceive(self,message):
        pass

    def Broadcast(self,message):
        pass

    def BroadcastAndWait(self,message):
        pass

    def Wait(self,seconds):
        pass

    # all other control items not implemented

# Sound
    # Not implemented, yet

    def Draw(self,screen):
        if self.Hidden:
            return
        if self.CurrentCostume == "":
            screen.fill(pygame.Color("white"),pygame.Rect(0,20,480,360))
        else:
            screen.blit(self.Costumes[self.CurrentCostume],(0,20))

    def AddCostume(self,filename,name=""):
        image = pygame.image.load(filename).convert()
        if name == "":
            name = os.path.splitext(os.path.split(filename)[-1])[0]
        if name in self.Costumes:
            i = 2
            newname = name
            while newname in self.Costumes:
                newname = "%s(%d)" % (name, i)
                i += 1
            name = newname
        self.Costumes[name] = image

    def _handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            threading.Thread(None, self.WhenIAmClicked).start()
        elif event.type == pygame.KEYUP:
            pass




class Sprite(StageSprite):

    Name = "Sprite"
    Drawing = False
    PenColor = [255,255,255]
    PenSize = 1

    Location = (0,0)
    Size = (0,0)
    ScreenPosition = (180,200)
    Direction = 90
    _layer = 0
    _glideTimer = None
    _mouseover = False

    _turtle = None


    def __init__(self):
        super().__init__()
        self.Size = (28,20)
        self._turtle = pygame.image.fromstring(
            b'\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x88\xc9w\x00\x9e\xd1\x82\x00\xca\xe1\x95\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc8\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xcb\xe1\x96\x00\x9f\xd2\x82\x00\x87\xc8w\x00\x8b\xcay?\x8b\xcay\xb2\x8b\xcay\xea\x8b\xcay\xc8\x8b\xcay3\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x1c\x8b\xcay\x87\x8b\xcay\x8d\x8b\xcay6\x88\xc9w\x00\x9e\xd1\x82\x00\xca\xe1\x95\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc9\xe1\x95\x12\xc9\xe1\x95&\xc8\xe1\x95*\xc9\xe1\x95\x1b\xc8\xe0\x94\x05\xcb\xe1\x96\x00\x9e\xd2\x81\x00\x87\xc8wr\x8b\xcay\xf8\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xa2\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\xa7\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xf8\x88\xc9w\x7f\x9c\xd0\x81\x00\xcb\xe1\x95\x11\xcb\xe2\x96l\xc9\xe1\x95\xb7\xc3\xde\x92\xe6\xbf\xdd\x90\xf6\xc1\xde\x92\xf8\xc0\xdd\x91\xef\xc7\xe0\x94\xce\xce\xe2\x97\x84\xa6\xd4\x85\x8f\x85\xc8v\xff\x89\xc9x\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xe6\x8b\xcayD\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcayq\x8b\xcay\xff\x8b\xcay\xff\x8a\xcay\xff\x86\xc9w\xff\xab\xd6\x88\xb1\xc9\xe1\x95\xd5\xaf\xd7\x89\xff\x9a\xcf\x80\xff\x8e\xcbz\xff\x93\xcd}\xff\xa6\xd4\x85\xff\x8b\xcay\xff\x95\xce}\xff\xa7\xd4\x86\xff\xc0\xdd\x91\xff\xb3\xd9\x8b\xff\x8e\xcb{\xf9\x85\xc8w\xc8\x87\xc9wx\x8b\xcay \x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8a\xcay\x00\x88\xc9xA\x87\xc9w\x9e\x8a\xcay\xe4\xac\xd6\x88\xff\xbd\xdc\x90\xff\x95\xce~\xff\x87\xc8w\xff\x88\xc9x\xff\x89\xcax\xff\x91\xcd|\xff\xa4\xd3\x84\xff\x87\xc9w\xff\x89\xc9x\xff\x86\xc8w\xff\x8e\xcbz\xff\xb1\xd8\x8a\xff\xc1\xde\x91\xe6\xad\xd7\x88$\xa7\xd5\x86\x00\x8c\xcaz\x00\x8b\xcax\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8c\xcay\x00\x8f\xcb{\x00\x9b\xd1\x81\x00\xad\xd7\x89\x00\xc3\xde\x92\x7f\xc2\xde\x92\xff\x8d\xcbz\xff\x85\xc8v\xff\x8b\xcay\xff\x8a\xcay\xff\x86\xc9w\xff\x95\xce~\xff\xab\xd6\x87\xff\x86\xc9w\xff\x89\xc9x\xff\x8b\xcay\xff\x88\xc9x\xff\x83\xc7v\xff\xb0\xd8\x89\xff\xd2\xe4\x99\xbe\xc7\xe0\x94\n\x8c\xcaz\x00\x8a\xcax\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8a\xc9y\x00\xb4\xda\x8c\x00\xcb\xe2\x97\x00\xcd\xe3\x97 \xc3\xdf\x92\xe9\xa3\xd3\x83\xff\xa9\xd5\x87\xff\x98\xcf~\xff\x87\xc8w\xff\x89\xc9x\xff\xa0\xd2\x82\xff\xc0\xdd\x91\xff\xc9\xe1\x95\xff\xb3\xd9\x8b\xff\x93\xcd|\xff\x85\xc8w\xff\x8d\xcbz\xff\xa4\xd3\x84\xff\xa5\xd4\x84\xff\xb7\xda\x8d\xff\xbf\xdd\x90w\x8a\xcayL\x8a\xcay\xa4\x8b\xcay\xb6\x8f\xce{\x99\x8c\xcczP\x8b\xcay\x00\x8b\xcay\x00\x87\xc9x\x00\x9a\xcf\x80\x00\xc8\xe1\x94\x00\xcc\xe2\x96\x82\xa8\xd5\x86\xff\x83\xc8u\xff\x91\xcd|\xff\xa8\xd5\x86\xff\xa8\xd5\x86\xff\xb7\xda\x8d\xff\xcb\xe1\x95\xff\xc9\xe1\x95\xff\xc7\xe0\x94\xff\xcb\xe2\x96\xff\xc5\xdf\x93\xff\xab\xd6\x88\xff\xaa\xd6\x87\xff\x9c\xd0\x81\xff\x87\xc9w\xff\x96\xce~\xff\xbf\xdd\x90\xfa\x8e\xcbz\xff\x8a\xcay\xff\x8a\xc9y\xffr\xafn\xff\x81\xc0u\xff\x8d\xccz\xad\x8b\xcay\x11\x8b\xcay:\x87\xc8w\x05\x9d\xd1\x81\x03\xc8\xe0\x94\xc5\x96\xce~\xff\x89\xc9x\xff\x89\xc9x\xff\x85\xc8w\xff\xaf\xd7\x89\xff\xce\xe2\x97\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc9\xe1\x95\xff\xc8\xe0\x94\xff\x92\xcd|\xff\x86\xc8w\xff\x8a\xcay\xff\x8a\xc9y\xff\xbc\xdc\x8f\xff\x9b\xd0\x80\xff\x89\xcax\xff\x89\xc8x\xffU\x8fa\xffu\xb3o\xff\x8e\xcez\xff\x8b\xcay\x90\x8b\xcay\xb4\x8a\xcay\xd5\x8c\xcbz\xcd\xbb\xdc\x8f\xfb\x91\xcc|\xff\x8a\xcax\xff\x8b\xcay\xff\x87\xc9w\xff\xa8\xd5\x86\xff\xcb\xe1\x96\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc8\xe0\x94\xff\xc4\xdf\x92\xff\x90\xcc{\xff\x89\xc9x\xff\x8b\xcay\xff\x88\xc9x\xff\xb5\xd9\x8c\xff\xa4\xd3\x84\xff\x87\xc9w\xff\x8b\xcay\xff\x8b\xc9y\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xe2\x8b\xcay\x13\x8a\xcay{\x8c\xcbz\xc2\xbc\xdc\x8f\xfc\x91\xcc|\xff\x8a\xcax\xff\x8b\xcay\xff\x87\xc9w\xff\xa8\xd5\x86\xff\xcb\xe1\x96\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc8\xe0\x94\xff\xc4\xdf\x92\xff\x8f\xcc{\xff\x89\xc9x\xff\x8b\xcay\xff\x88\xc9x\xff\xb6\xda\x8c\xff\xa4\xd3\x84\xff\x87\xc9w\xff\x8b\xcay\xff\x8d\xccz\xff\x8c\xcbz\xff\x8b\xcay\xff\x8b\xcay\xe5\x8b\xcay\x00\x85\xc8v\x00\x9d\xd1\x81\x01\xc9\xe0\x95\xc5\x97\xcf\x7f\xff\x88\xc9w\xff\x89\xc9x\xff\x85\xc8w\xff\xaf\xd7\x89\xff\xce\xe2\x97\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc9\xe1\x95\xff\xc8\xe0\x94\xff\x92\xcd|\xff\x86\xc8w\xff\x8a\xcay\xff\x8b\xcay\xff\xbd\xdd\x8f\xff\x9b\xd0\x80\xff\x89\xcax\xff\x89\xc8x\xffX\x93b\xffw\xb5p\xff\x8e\xcez\xff\x8b\xcay\xa0\x8a\xc9y\x00\xa9\xd5\x86\x00\xc7\xe0\x94\x00\xcd\xe2\x97\x81\xab\xd5\x87\xff\x84\xc8u\xff\x92\xcd|\xff\xa8\xd5\x86\xff\xa7\xd4\x86\xff\xb4\xd9\x8c\xff\xca\xe1\x95\xff\xc9\xe1\x95\xff\xc8\xe0\x94\xff\xcb\xe2\x96\xff\xc3\xdf\x92\xff\xaa\xd5\x87\xff\xab\xd6\x87\xff\x9d\xd0\x81\xff\x86\xc8w\xff\x99\xcf\x7f\xff\xbf\xdd\x90\xff\x8d\xcbz\xff\x8a\xcay\xff\x8a\xc9x\xffl\xa8k\xff\x7f\xbdt\xff\x8d\xccz\xc6\x8b\xcay\x1b\xa8\xd4\x86\x00\xc6\xe0\x93\x00\xc5\xdf\x93\x00\xc9\xe1\x95 \xc7\xe0\x94\xe9\xa5\xd4\x84\xff\xa9\xd5\x86\xff\x97\xce~\xff\x87\xc8w\xff\x88\xc9x\xff\x9e\xd1\x81\xff\xbe\xdd\x90\xff\xc8\xe0\x94\xff\xb0\xd8\x8a\xff\x91\xcc{\xff\x86\xc8w\xff\x8d\xcbz\xff\xa3\xd3\x84\xff\xa5\xd3\x85\xff\xbb\xdc\x8f\xff\xbd\xdc\x8f|\x89\xcaxb\x8a\xcay\xc1\x8b\xcay\xd5\x8f\xce{\xb6\x8d\xcczm\x8b\xcay\x0b\x8b\xcay\x00\x93\xcd}\x00\x8f\xcb{\x00\x8d\xcaz\x00\x99\xd0\x80\x00\xb7\xda\x8dx\xc6\xe0\x94\xff\x90\xcb{\xff\x84\xc8v\xff\x8b\xcay\xff\x8b\xcay\xff\x86\xc8w\xff\x94\xcd}\xff\xaa\xd5\x87\xff\x86\xc8w\xff\x89\xc9x\xff\x8b\xcay\xff\x87\xc9x\xff\x84\xc7v\xff\xb4\xd9\x8c\xff\xd2\xe4\x99\xbd\xbf\xdd\x90\x08\x8c\xcbz\x00\x8a\xcay\x01\x8b\xcay\x08\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8a\xcay\x00\x8a\xcay\x00\x8a\xcay1\x87\xc9w\x89\x85\xc8w\xd8\xac\xd6\x88\xff\xc1\xde\x92\xff\x9a\xcf\x80\xff\x87\xc9x\xff\x87\xc9w\xff\x88\xc9w\xff\x91\xcc|\xff\xa4\xd3\x84\xff\x87\xc8w\xff\x88\xc9w\xff\x86\xc9w\xff\x91\xcc{\xff\xb7\xda\x8d\xff\xc1\xde\x91\xe7\xaa\xd5\x87&\x90\xcc{\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcayf\x8b\xcay\xf5\x8b\xcay\xff\x8a\xcay\xff\x86\xc9w\xff\xa9\xd4\x87\xbb\xcb\xe1\x96\xd5\xb5\xda\x8c\xff\xa0\xd2\x82\xff\x92\xcc|\xff\x96\xce~\xff\xa7\xd4\x86\xff\x8f\xcbz\xff\x9a\xcf\x7f\xff\xad\xd7\x89\xff\xc3\xde\x92\xff\xb3\xd8\x8b\xff\x8d\xcbz\xf9\x86\xc8w\xcb\x8a\xcax|\x8b\xcay#\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\xaf\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xff\x88\xc9w\x8e\x99\xcf\x7f\x03\xca\xe1\x95\x10\xca\xe1\x96j\xca\xe1\x95\xb6\xc6\xdf\x94\xe4\xc2\xde\x92\xf6\xc4\xdf\x93\xf7\xc4\xdf\x93\xee\xc9\xe1\x95\xcc\xce\xe3\x98\x83\xa6\xd4\x85\x8a\x85\xc8v\xff\x89\xc9x\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xe9\x8b\xcayL\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay&\x8b\xcay\x9b\x8b\xcay\x9c\x8b\xcayF\x88\xc9w\x00\x9b\xd0\x80\x00\xc9\xe1\x95\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc9\xe0\x94\x10\xc8\xe0\x95%\xc8\xe0\x95)\xc8\xe0\x95\x1a\xc7\xe0\x94\x05\xcb\xe1\x96\x00\x9f\xd2\x82\x00\x87\xc8wk\x8b\xcay\xf5\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xac\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x88\xc9w\x00\x9b\xd0\x80\x00\xc9\xe1\x95\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc8\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xcb\xe1\x96\x00\xa0\xd2\x82\x00\x87\xc8w\x00\x8b\xcay:\x8b\xcay\xaf\x8b\xcay\xe9\x8b\xcay\xcc\x8b\xcay:\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00',
            self.Size, "RGBA").convert_alpha()


    # Motion
    def Move(self, steps):
        if self.Direction == 90:
            self._setPosition(self.Location[0] + steps, self.Location[1])
        elif self.Direction == 0:
            self._setPosition(self.Location[0], self.Location[1] - steps)
        elif self.Direction == -90:
            self._setPosition(self.Location[0] - steps, self.Location[1])
        elif self.Direction == 180:
            self._setPosition(self.Location[0], self.Location[1] + steps)
        else:
            pass

    def TurnClockwise(self, degrees):
        if degrees == 0 or degrees == 360:
            return

        while degrees < 0:
            degrees += 360
        while degrees > 360:
            degrees -= 360

        direction = self.Direction + degrees
        if direction > 360:
            direction -= 360

        if direction > 180:
            direction -= 360
        self._rotate(direction)

    def TurnCounterClockwise(self, degrees):
        if degrees == 0 or degrees == 360:
            return

        while degrees < 0:
            degrees += 360
        while degrees > 360:
            degrees -= 360

        direction = self.Direction - degrees
        if direction < -360:
            direction += 360

        if direction < -180:
            direction += 360
        self._rotate(direction)

    def PointInDirection(self, degrees):
        while degrees < -360:
            degrees += 360
        while degrees > 360:
            degrees -= 360

        if degrees > 180:
            degrees -= 360
        if degrees < -180:
            degrees += 360

        self._rotate(degrees)

    def PointTowards(self, item):
        if type(item) is tuple:
            o = self.ScreenPosition
            d = item
            rise = 0.0
            run = 0.0
            offset = 0
            degrees = 0
            multiplier = 1
            if o[0] == d[0]:
                if o[1] < d[1]:
                    self._rotate(0)
                    return
                else:
                    self._rotate(180)
                    return
            elif o[1] == d[1]:
                if o[1] < d[1]:
                    self._rotate(-90)
                    return
                else:
                    self._rotate(90)
                    return
            elif o[0] > d[0] and o[1] > d[1]:
                rise = o[1] - d[1]
                run = o[0] - d[0]
                offset = -90
                multiplier = 1
            elif o[0] < d[0] and o[1] > d[1]:
                rise = o[1] - d[1]
                run = d[0] - o[0]
                offset = 90
                multiplier = -1
            elif o[0] < d[0] and o[1] < d[1]:
                rise = d[1] - o[1]
                run = d[0] - o[0]
                offset = 90
                multiplier = 1
            elif o[0] > d[0] and o[1] < d[1]:
                rise = d[1] - o[1]
                run = o[0] - d[0]
                offset = -90
                multiplier = -1

            degrees = math.degrees(math.atan(rise / run))
            degrees = offset + (multiplier * degrees)
            self._rotate(degrees)
        elif type(item) is Sprite:
            self.PointTowards(item.ScreenPosition)
        elif type(item) is str:
            if item in TheProject.Sprites:
                self.PointTowards(TheProject.Sprites[item].ScreenPosition)

    def GoToPoint(self, x, y):
        self._setPosition(x,y)

    def GoTo(self, item):
        if type(item) is tuple:
            self._setPosition(item[0],item[1])
        elif type(item) is Sprite:
            self._setPosition(item.Location[0],item.Location[1])
        elif type(item) is str:
            if item in TheProject.Sprites:
                self._setPosition(TheProject.Sprites[item].Location[0], TheProject.Sprites[item].Location[1])

    def Glide(self, seconds, x, y):
        pass

    def ChangeX(self, x):
        self._setPosition(self.Location[0] + x, self.Location[1])

    def SetX(self, x):
        self._setPosition(x, self.Location[1])

    def ChangeY(self, y):
        self._setPosition(self.Location[0], self.Location[1] + y)

    def SetY(self, y):
        self._setPosition(self.Location[0],y)

    def IfOnEdgeBounce(self):
        pass

# Looks
    def Say(self,message="Hello",seconds=-1):
        if seconds == 0:
            self._shutup()
        self.Saying = message
        if seconds > 0:
            t = threading.Timer(seconds,self._shutup)
            t.start()

    def Think(self,message="Hmmm...",seconds=-1):
        if seconds == 0:
            self._clearmind()
        self.Thinking = message
        if seconds > 0:
            t = threading.Timer(seconds,self._clearmind)
            t.start()

    # Graphic effects not implemented

    def ChangeSize(self,size):
        pass

    def SetSize(self,percent):
        pass

    def GoToFront(self):
        TheProject.MoveToFront(self)

    def GoBack(self,layers):
        TheProject.MoveBack(self)

# Pen

    def PenDown(self):
        self.Drawing = True

    def PenUp(self):
        self.Drawing = False

    def SetPenColor(self,color):
        pass

    def ChangePenColor(self,amount):
        pass

    def ChangePenShade(self,amount):
        pass

    def SetPenShade(self,percent):
        pass

    def ChangePenSize(self,amount):
        self.PenSize += amount

    def SetPenSize(self,size):
        self.PenSize = size

# Sensing

    def Touching(self,item):
        pass

    # color-touching not implemented


    def Draw(self,screen):
        if(self.CurrentCostume==""):
            screen.blit(self._turtle,self.ScreenPosition)
        else:
            screen.blit(self.Costumes[self.CurrentCostume], self.ScreenPosition)

    def _setPosition(self, x, y):
        self.Location = (x,y)
        self.ScreenPosition = (x + 240, y + 180)

    def _rotate(self,direction):
        dir = self.Direction
        newdir = direction
        if dir < 0:
            dir = 360 + dir
        if newdir < 0:
            newdir = 360 + newdir

        angle = dir - newdir

        pygame.transform.rotate(self._turtle,angle)
        for c in self.Costumes:
            pygame.transform.rotate(self.Costumes[c], angle)

    def _shutup(self):
        self.Saying = ""
    def _clearmind(self):
        self.Thinking = ""

    def _handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP and self._mouseover:
            threading.Thread(None, self.WhenIAmClicked).start()
        elif event.type == pygame.MOUSEMOTION:
            inbounds = (event.pos[0] >= self.ScreenPosition[0] and event.pos[0] <= self.ScreenPosition[0] + self.Size[0]) and (event.pos[1] >= self.ScreenPosition[1] and event.pos[1] <= self.ScreenPosition[1] + self.Size[1])
            if self._mouseover and not inbounds:
                self._mouseover = False
                threading.Thread(None,self.WhenIAmMouseDeparted).start()
            if inbounds and not self._mouseover:
                self._mouseover = True
                threading.Thread(None,self.WhenIAmMouseEntered).start()
        elif event.type == pygame.KEYUP:
            pass


class Project:
    Name = ""
    Running = True
    Screen = None
    Stage = None
    Sprites = {}

    BackgroundThread = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snappy")
        self.Screen = pygame.display.set_mode((480,380),0,24)
        self.Stage = StageSprite()

    def SetTheStage(self,stage):
        if type(stage) is Sprite:
            raise Exception("Cannot set the stage to a sprite.  It must be subclassed from StageSprite")
        self.Stage = stage

    def AddSprite(self,sprite):
        if sprite.Name in self.Sprites:
            i = 2
            newname = sprite.Name
            while newname in self.Sprites:
                newname = "%s(%d)" % (sprite.Name,i)
                i += 1
            sprite.Name = newname

        self.Sprites[sprite.Name] = sprite

    def RemoveSprite(self,sprite):
        if type(sprite) is int:
            self.Sprites.remove(self.Sprites[sprite])
        elif type(sprite) is str:
            for s in self.Sprites:
                if s.Name == sprite:
                    break
            else:
                return
            self.Sprites.remove(s)
        elif type(sprite) is Sprite:
            self.Sprites.remove(sprite)

    def MoveToFront(self,sprite):
        self.Sprites.remove(sprite)
        self.Sprites.insert(0,sprite)

    def MoveBack(self,sprite,layers):
        index = self.Sprites.index(sprite)
        self.Sprites.remove(sprite)
        if (index + layers) > len(self.Sprites):
            self.Sprites.append(sprite)
        else:
            self.Sprites.insert(index + 1, sprite)

    def Go(self):
        Running = True

    def Pause(self):
        self.Running = not self.Running

    def Stop(self):
        Running = False

    def Load(self,filename):
        pass

    def Save(self,filename):
        pass

    def Run(self):
        while True:
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exit()
                self.Stage._handleEvent(i)
                for k in self.Sprites:
                    self.Sprites[k]._handleEvent(i)


            self.Stage.Draw(self.Screen)
            for k in self.Sprites:
                self.Sprites[k].Draw(self.Screen)
            pygame.display.update()

TheProject = Project()