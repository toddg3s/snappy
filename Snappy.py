import pygame
import threading
import os
import math
from time import sleep
from enum import Enum


class StageSprite:

    Costumes = {}
    CurrentCostume = ""
    Costume = None

    Saying = ""
    Thinking = ""

    Hidden = False

    def __init__(self):
        self._updateCostume()
        self.SetUp()

    def SetUp(self):
        pass

# Looks

    def SwitchToCostume(self,name):
        if name in self.Costumes:
            self.CurrentCostume = name
        else:
            self.CurrentCostume = ""
        self._updateCostume()

    def NextCostume(self):
        if len(self.Costumes) == 0:
            self.CurrentCostume = ""
            self._updateCostume()
            return

        keys = sorted(self.Costumes)
        if self.CurrentCostume == "":
            self.CurrentCostume = keys[0]
        else:
            index = keys.index(self.CurrentCostume)
            index += 1
            if(index > len(self.Costumes)):
                index = 0
            self.CurrentCostume = keys[index]
        self._updateCostume()

    def Show(self):
        self.Hidden = False

    def Hide(self):
        self.Hidden = True

# Sensing

    def MouseDown(self):
        return pygame.mouse.get_pressed()[0]

    def KeyPressed(self,key):
        if type(key) is int:
            return pygame.key.get_pressed()[key]
        elif type(key) is str:
            keycheck = key.lower().strip()
            if len(keycheck) == 1:
                return pygame.key.get_pressed()[ord(keycheck)]
            else:
                if keycheck == 'any key':
                    for flag in pygame.key.get_pressed():
                        if flag:
                            return True
                elif keycheck == 'left arrow':
                    return pygame.key.get_pressed()[pygame.K_LEFT]
                elif keycheck == 'right arrow':
                    return pygame.key.get_pressed()[pygame.K_RIGHT]
                elif keycheck == 'up arrow':
                    return pygame.key.get_pressed()[pygame.K_UP]
                elif keycheck == 'down arrow':
                    return pygame.key.get_pressed()[pygame.K_DOWN]
                elif keycheck == 'space':
                    return pygame.key.get_pressed()[pygame.K_SPACE]

        return False

    def AskAndWait(self,prompt):
        return ""

# Pen

    def Clear(self):
        TheProject.PenSurface = pygame.Surface((480,380),pygame.SRCALPHA,32)

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
        threading.Thread(target=TheProject.Stage.WhenIReceive, args=(message,)).start()
        for name in TheProject.Sprites:
            threading.Thread(target=TheProject.Sprites[name].WhenIReceive, args=(message,)).start()

    def BroadcastAndWait(self,message):
        TheProject.Stage.WhenIReceive(message)
        for name in TheProject.Sprites:
            TheProject.Sprites[name].WhenIReceive(message)

    def Wait(self, seconds):
        sleep(seconds)

    # all other control items not implemented

# Sound
    # Not implemented, yet

    def Draw(self,screen):
        if not self.Hidden:
            screen.blit(self.Costume, (0, 20))

    def AddCostume(self, filename, name=""):
        image = pygame.image.load(filename).convert_alpha()
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
            if not hasattr(self, "_mouseover") or self._mouseover:
                threading.Thread(None, self.WhenIAmClicked).start()
        elif event.type == pygame.KEYUP:
            custommethod = "When_%s_Pressed" % pygame.key.name(event.key).replace(" ", "_")
            if hasattr(self, custommethod):
                threading.Thread(None, getattr(self, custommethod)).start()
            else:
                threading.Thread(target=self.WhenKeyPressed, args=[pygame.key.name(event.key)]).start()

    def _updateCostume(self):
        if self.CurrentCostume == "":
            self.Costume = pygame.Surface((480,360),0,32)
            self.Costume.fill(pygame.Color("white"))
        else:
            self.Costume = self.Costumes[self.CurrentCostume]


class Sprite(StageSprite):

    Name = "Sprite"
    Drawing = False
    PenColor = pygame.Color("blue")
    PenSize = 1

    Location = (0, 0)
    Size = (0, 0)
    Scale = 1.0
    LastPosition = (240, 200)
    ScreenPosition = (240, 200)
    Direction = 90
    _layer = 0
    _mouseover = False

    _colors = {}
    _turtle = None

    def __init__(self):
        self._turtle = pygame.image.fromstring(
            b'\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x88\xc9w\x00\x9e\xd1\x82\x00\xca\xe1\x95'
            b'\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc8\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7'
            b'\xe0\x94\x00\xcb\xe1\x96\x00\x9f\xd2\x82\x00\x87\xc8w\x00\x8b\xcay?\x8b\xcay\xb2\x8b\xcay\xea\x8b\xcay'
            b'\xc8\x8b\xcay3\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay'
            b'\x1c\x8b\xcay\x87\x8b\xcay\x8d\x8b\xcay6\x88\xc9w\x00\x9e\xd1\x82\x00\xca\xe1\x95\x00\xc7\xe0\x94\x00'
            b'\xc7\xe0\x94\x00\xc9\xe1\x95\x12\xc9\xe1\x95&\xc8\xe1\x95*\xc9\xe1\x95\x1b\xc8\xe0\x94\x05\xcb\xe1\x96'
            b'\x00\x9e\xd2\x81\x00\x87\xc8wr\x8b\xcay\xf8\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xa2\x8b\xcay'
            b'\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\xa7\x8b\xcay\xff\x8b\xcay'
            b'\xff\x8b\xcay\xf8\x88\xc9w\x7f\x9c\xd0\x81\x00\xcb\xe1\x95\x11\xcb\xe2\x96l\xc9\xe1\x95\xb7\xc3\xde\x92'
            b'\xe6\xbf\xdd\x90\xf6\xc1\xde\x92\xf8\xc0\xdd\x91\xef\xc7\xe0\x94\xce\xce\xe2\x97\x84\xa6\xd4\x85\x8f\x85'
            b'\xc8v\xff\x89\xc9x\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xe6\x8b\xcayD\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay'
            b'\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcayq\x8b\xcay\xff\x8b\xcay\xff\x8a\xcay\xff\x86\xc9w\xff'
            b'\xab\xd6\x88\xb1\xc9\xe1\x95\xd5\xaf\xd7\x89\xff\x9a\xcf\x80\xff\x8e\xcbz\xff\x93\xcd}\xff\xa6\xd4\x85\xff'
            b'\x8b\xcay\xff\x95\xce}\xff\xa7\xd4\x86\xff\xc0\xdd\x91\xff\xb3\xd9\x8b\xff\x8e\xcb{\xf9\x85\xc8w\xc8\x87'
            b'\xc9wx\x8b\xcay \x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay'
            b'\x00\x8a\xcay\x00\x88\xc9xA\x87\xc9w\x9e\x8a\xcay\xe4\xac\xd6\x88\xff\xbd\xdc\x90\xff\x95\xce~\xff\x87'
            b'\xc8w\xff\x88\xc9x\xff\x89\xcax\xff\x91\xcd|\xff\xa4\xd3\x84\xff\x87\xc9w\xff\x89\xc9x\xff\x86\xc8w\xff'
            b'\x8e\xcbz\xff\xb1\xd8\x8a\xff\xc1\xde\x91\xe6\xad\xd7\x88$\xa7\xd5\x86\x00\x8c\xcaz\x00\x8b\xcax\x00\x8b'
            b'\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8c\xcay\x00\x8f\xcb{\x00\x9b\xd1\x81\x00'
            b'\xad\xd7\x89\x00\xc3\xde\x92\x7f\xc2\xde\x92\xff\x8d\xcbz\xff\x85\xc8v\xff\x8b\xcay\xff\x8a\xcay\xff\x86'
            b'\xc9w\xff\x95\xce~\xff\xab\xd6\x87\xff\x86\xc9w\xff\x89\xc9x\xff\x8b\xcay\xff\x88\xc9x\xff\x83\xc7v\xff'
            b'\xb0\xd8\x89\xff\xd2\xe4\x99\xbe\xc7\xe0\x94\n\x8c\xcaz\x00\x8a\xcax\x00\x8b\xcay\x00\x8b\xcay\x00\x8b'
            b'\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8a\xc9y\x00\xb4\xda\x8c\x00\xcb\xe2\x97\x00\xcd\xe3\x97 \xc3\xdf'
            b'\x92\xe9\xa3\xd3\x83\xff\xa9\xd5\x87\xff\x98\xcf~\xff\x87\xc8w\xff\x89\xc9x\xff\xa0\xd2\x82\xff\xc0\xdd'
            b'\x91\xff\xc9\xe1\x95\xff\xb3\xd9\x8b\xff\x93\xcd|\xff\x85\xc8w\xff\x8d\xcbz\xff\xa4\xd3\x84\xff\xa5\xd4'
            b'\x84\xff\xb7\xda\x8d\xff\xbf\xdd\x90w\x8a\xcayL\x8a\xcay\xa4\x8b\xcay\xb6\x8f\xce{\x99\x8c\xcczP\x8b\xcay'
            b'\x00\x8b\xcay\x00\x87\xc9x\x00\x9a\xcf\x80\x00\xc8\xe1\x94\x00\xcc\xe2\x96\x82\xa8\xd5\x86\xff\x83\xc8u'
            b'\xff\x91\xcd|\xff\xa8\xd5\x86\xff\xa8\xd5\x86\xff\xb7\xda\x8d\xff\xcb\xe1\x95\xff\xc9\xe1\x95\xff\xc7\xe0'
            b'\x94\xff\xcb\xe2\x96\xff\xc5\xdf\x93\xff\xab\xd6\x88\xff\xaa\xd6\x87\xff\x9c\xd0\x81\xff\x87\xc9w\xff\x96'
            b'\xce~\xff\xbf\xdd\x90\xfa\x8e\xcbz\xff\x8a\xcay\xff\x8a\xc9y\xffr\xafn\xff\x81\xc0u\xff\x8d\xccz\xad\x8b'
            b'\xcay\x11\x8b\xcay:\x87\xc8w\x05\x9d\xd1\x81\x03\xc8\xe0\x94\xc5\x96\xce~\xff\x89\xc9x\xff\x89\xc9x\xff'
            b'\x85\xc8w\xff\xaf\xd7\x89\xff\xce\xe2\x97\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94'
            b'\xff\xc9\xe1\x95\xff\xc8\xe0\x94\xff\x92\xcd|\xff\x86\xc8w\xff\x8a\xcay\xff\x8a\xc9y\xff\xbc\xdc\x8f\xff'
            b'\x9b\xd0\x80\xff\x89\xcax\xff\x89\xc8x\xffU\x8fa\xffu\xb3o\xff\x8e\xcez\xff\x8b\xcay\x90\x8b\xcay\xb4\x8a'
            b'\xcay\xd5\x8c\xcbz\xcd\xbb\xdc\x8f\xfb\x91\xcc|\xff\x8a\xcax\xff\x8b\xcay\xff\x87\xc9w\xff\xa8\xd5\x86'
            b'\xff\xcb\xe1\x96\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc8\xe0\x94\xff\xc4'
            b'\xdf\x92\xff\x90\xcc{\xff\x89\xc9x\xff\x8b\xcay\xff\x88\xc9x\xff\xb5\xd9\x8c\xff\xa4\xd3\x84\xff\x87\xc9w'
            b'\xff\x8b\xcay\xff\x8b\xc9y\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xe2\x8b\xcay\x13\x8a\xcay{\x8c\xcbz\xc2'
            b'\xbc\xdc\x8f\xfc\x91\xcc|\xff\x8a\xcax\xff\x8b\xcay\xff\x87\xc9w\xff\xa8\xd5\x86\xff\xcb\xe1\x96\xff\xc7'
            b'\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc8\xe0\x94\xff\xc4\xdf\x92\xff\x8f\xcc{\xff'
            b'\x89\xc9x\xff\x8b\xcay\xff\x88\xc9x\xff\xb6\xda\x8c\xff\xa4\xd3\x84\xff\x87\xc9w\xff\x8b\xcay\xff\x8d'
            b'\xccz\xff\x8c\xcbz\xff\x8b\xcay\xff\x8b\xcay\xe5\x8b\xcay\x00\x85\xc8v\x00\x9d\xd1\x81\x01\xc9\xe0\x95'
            b'\xc5\x97\xcf\x7f\xff\x88\xc9w\xff\x89\xc9x\xff\x85\xc8w\xff\xaf\xd7\x89\xff\xce\xe2\x97\xff\xc7\xe0\x94'
            b'\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc7\xe0\x94\xff\xc9\xe1\x95\xff\xc8\xe0\x94\xff\x92\xcd|\xff\x86'
            b'\xc8w\xff\x8a\xcay\xff\x8b\xcay\xff\xbd\xdd\x8f\xff\x9b\xd0\x80\xff\x89\xcax\xff\x89\xc8x\xffX\x93b\xffw'
            b'\xb5p\xff\x8e\xcez\xff\x8b\xcay\xa0\x8a\xc9y\x00\xa9\xd5\x86\x00\xc7\xe0\x94\x00\xcd\xe2\x97\x81\xab\xd5'
            b'\x87\xff\x84\xc8u\xff\x92\xcd|\xff\xa8\xd5\x86\xff\xa7\xd4\x86\xff\xb4\xd9\x8c\xff\xca\xe1\x95\xff\xc9'
            b'\xe1\x95\xff\xc8\xe0\x94\xff\xcb\xe2\x96\xff\xc3\xdf\x92\xff\xaa\xd5\x87\xff\xab\xd6\x87\xff\x9d\xd0\x81'
            b'\xff\x86\xc8w\xff\x99\xcf\x7f\xff\xbf\xdd\x90\xff\x8d\xcbz\xff\x8a\xcay\xff\x8a\xc9x\xffl\xa8k\xff\x7f'
            b'\xbdt\xff\x8d\xccz\xc6\x8b\xcay\x1b\xa8\xd4\x86\x00\xc6\xe0\x93\x00\xc5\xdf\x93\x00\xc9\xe1\x95 \xc7\xe0'
            b'\x94\xe9\xa5\xd4\x84\xff\xa9\xd5\x86\xff\x97\xce~\xff\x87\xc8w\xff\x88\xc9x\xff\x9e\xd1\x81\xff\xbe\xdd'
            b'\x90\xff\xc8\xe0\x94\xff\xb0\xd8\x8a\xff\x91\xcc{\xff\x86\xc8w\xff\x8d\xcbz\xff\xa3\xd3\x84\xff\xa5\xd3'
            b'\x85\xff\xbb\xdc\x8f\xff\xbd\xdc\x8f|\x89\xcaxb\x8a\xcay\xc1\x8b\xcay\xd5\x8f\xce{\xb6\x8d\xcczm\x8b'
            b'\xcay\x0b\x8b\xcay\x00\x93\xcd}\x00\x8f\xcb{\x00\x8d\xcaz\x00\x99\xd0\x80\x00\xb7\xda\x8dx\xc6\xe0\x94'
            b'\xff\x90\xcb{\xff\x84\xc8v\xff\x8b\xcay\xff\x8b\xcay\xff\x86\xc8w\xff\x94\xcd}\xff\xaa\xd5\x87\xff\x86'
            b'\xc8w\xff\x89\xc9x\xff\x8b\xcay\xff\x87\xc9x\xff\x84\xc7v\xff\xb4\xd9\x8c\xff\xd2\xe4\x99\xbd\xbf\xdd'
            b'\x90\x08\x8c\xcbz\x00\x8a\xcay\x01\x8b\xcay\x08\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8a'
            b'\xcay\x00\x8a\xcay\x00\x8a\xcay1\x87\xc9w\x89\x85\xc8w\xd8\xac\xd6\x88\xff\xc1\xde\x92\xff\x9a\xcf\x80'
            b'\xff\x87\xc9x\xff\x87\xc9w\xff\x88\xc9w\xff\x91\xcc|\xff\xa4\xd3\x84\xff\x87\xc8w\xff\x88\xc9w\xff\x86'
            b'\xc9w\xff\x91\xcc{\xff\xb7\xda\x8d\xff\xc1\xde\x91\xe7\xaa\xd5\x87&\x90\xcc{\x00\x8b\xcay\x00\x8b\xcay'
            b'\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcayf\x8b\xcay'
            b'\xf5\x8b\xcay\xff\x8a\xcay\xff\x86\xc9w\xff\xa9\xd4\x87\xbb\xcb\xe1\x96\xd5\xb5\xda\x8c\xff\xa0\xd2\x82'
            b'\xff\x92\xcc|\xff\x96\xce~\xff\xa7\xd4\x86\xff\x8f\xcbz\xff\x9a\xcf\x7f\xff\xad\xd7\x89\xff\xc3\xde\x92'
            b'\xff\xb3\xd8\x8b\xff\x8d\xcbz\xf9\x86\xc8w\xcb\x8a\xcax|\x8b\xcay#\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay'
            b'\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\xaf\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay'
            b'\xff\x88\xc9w\x8e\x99\xcf\x7f\x03\xca\xe1\x95\x10\xca\xe1\x96j\xca\xe1\x95\xb6\xc6\xdf\x94\xe4\xc2\xde'
            b'\x92\xf6\xc4\xdf\x93\xf7\xc4\xdf\x93\xee\xc9\xe1\x95\xcc\xce\xe3\x98\x83\xa6\xd4\x85\x8a\x85\xc8v\xff'
            b'\x89\xc9x\xff\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xe9\x8b\xcayL\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00'
            b'\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay&\x8b\xcay\x9b\x8b\xcay\x9c\x8b\xcayF\x88\xc9w\x00\x9b'
            b'\xd0\x80\x00\xc9\xe1\x95\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc9\xe0\x94\x10\xc8\xe0\x95%\xc8\xe0\x95)'
            b'\xc8\xe0\x95\x1a\xc7\xe0\x94\x05\xcb\xe1\x96\x00\x9f\xd2\x82\x00\x87\xc8wk\x8b\xcay\xf5\x8b\xcay\xff'
            b'\x8b\xcay\xff\x8b\xcay\xff\x8b\xcay\xac\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00'
            b'\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x88\xc9w\x00\x9b\xd0\x80\x00\xc9\xe1'
            b'\x95\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc8\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00\xc7\xe0\x94\x00'
            b'\xc7\xe0\x94\x00\xcb\xe1\x96\x00\xa0\xd2\x82\x00\x87\xc8w\x00\x8b\xcay:\x8b\xcay\xaf\x8b\xcay\xe9\x8b'
            b'\xcay\xcc\x8b\xcay:\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00\x8b\xcay\x00',
            (28, 20), "RGBA").convert_alpha()
        super().__init__()

    # Motion
    def Move(self, steps):
        prefix = "Move: Direction=%d, steps=%d" % (self.Direction, steps)
        if self.Direction == 90:
            TraceInfo(self, "%s, right" % prefix)
            self._setPosition(self.Location[0] + steps, self.Location[1])
        elif self.Direction == 0:
            TraceInfo(self, "%s, up" % prefix)
            self._setPosition(self.Location[0], self.Location[1] - steps)
        elif self.Direction == -90:
            TraceInfo(self, "%s, left" % prefix)
            self._setPosition(self.Location[0] - steps, self.Location[1])
        elif self.Direction == 180:
            TraceInfo(self, "%s, down" % prefix)
            self._setPosition(self.Location[0], self.Location[1] + steps)
        elif 0 < self.Direction < 90:
            x = math.sin(math.radians(self.Direction)) * steps
            y = math.sqrt((steps * steps) - (x * x))
            TraceInfo(self, "%s, quad 2, x=%d, y=%d" % (prefix,x,y))
            self._setPosition(self.Location[0] + x, self.Location[1] + y)
        elif 90 < self.Direction < 180:
            x = math.sin(math.radians(180 - self.Direction)) * steps
            y = math.sqrt((steps * steps) - (x * x))
            TraceInfo(self, "%s, quad 3, x=%d, y=%d" % (prefix,x,y))
            self._setPosition(self.Location[0] + x, self.Location[1] - y)
        elif 0 > self.Direction > -90:
            x = math.sin(math.radians(self.Direction)) * steps
            y = math.sqrt((steps * steps) - (x * x))
            TraceInfo(self, "%s, quad 1, x=%d, y=%d" % (prefix,x,y))
            self._setPosition(self.Location[0] + x, self.Location[1] + y)
        else:
            x = math.sin(math.radians(180 - self.Direction)) * steps
            y = math.sqrt((steps * steps) - (x * x))
            TraceInfo(self, "%s, quad 4, x=%d, y=%d" % (prefix,x,y))
            self._setPosition(self.Location[0] + x, self.Location[1] - y)

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
        TraceInfo(self, "PointInDirection: degrees=%d" % degrees)
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
            o = self.Location
            d = item
            if o[0] == d[0]:
                if o[1] < d[1]:
                    self._rotate(0)
                else:
                    self._rotate(180)
            elif o[1] == d[1]:
                if o[0] < d[0]:
                    self._rotate(90)
                else:
                    self._rotate(-90)
            else:
                rise = abs(d[1] - o[1])
                run = abs(d[0] - o[0])
                degrees = math.degrees(math.atan(rise / run))
                if d[0] > o[0]:
                    offset = 90
                    if d[1] > o[1]:
                        multiplier = -1
                    else:
                        multiplier = 1
                else:
                    offset = -90
                    if d[1] > o[1]:
                        multiplier = 1
                    else:
                        multiplier = -1
                degrees = offset + (multiplier * degrees)
                self._rotate(degrees)

        elif type(item) is Sprite:
            self.PointTowards(item.Location)
        elif type(item) is str:
            if item in TheProject.Sprites:
                self.PointTowards(TheProject.Sprites[item].Location)

    def GoToPoint(self, x, y):
        self._setPosition(x, y)

    def GoTo(self, item):
        if type(item) is tuple:
            self._setPosition(item[0],item[1])
        elif type(item) is Sprite:
            self._setPosition(item.Location[0],item.Location[1])
        elif type(item) is str:
            if item in TheProject.Sprites:
                self._setPosition(TheProject.Sprites[item].Location[0], TheProject.Sprites[item].Location[1])

    def Glide(self, seconds, x, y):
        rise = y - self.Location[1]
        run = x - self.Location[0]
        step = run / (seconds * 24)
        TraceInfo(self, "gliding: run=%d, rise=%d, step=%f" % (run, rise, step))
        start = self.Location
        for i in range(seconds * 24):
            posx = int(round(start[0] + (i * step)))
            posy = int(round(start[1] + (i * step) * (rise / run)))
            self.GoToPoint(posx, posy)
            sleep(0.02)   # I don't like this.  need to find a better way

    def ChangeX(self, x):
        self._setPosition(self.Location[0] + x, self.Location[1])

    def SetX(self, x):
        self._setPosition(x, self.Location[1])

    def ChangeY(self, y):
        self._setPosition(self.Location[0], self.Location[1] + y)

    def SetY(self, y):
        self._setPosition(self.Location[0],y)

    def IfOnEdgeBounce(self):
        if (0 < self.ScreenPosition[0] and self.ScreenPosition[0] + self.Size[0] < 480
           and 20 < self.ScreenPosition[1] and self.ScreenPosition[1] + self.Size[1] < 380):
            return

        TraceInfo(self, "Bouncing: ScreenPosition=%s, Direction=%d" % (self.ScreenPosition, self.Direction))
        if self.ScreenPosition[0] <= 0:
            self.PointInDirection(self.Direction * -1)
            self.SetX(-240 + (self.Size[0] / 2))

        if self.ScreenPosition[0] + self.Size[0] >= 480:
            self.PointInDirection(self.Direction * -1)
            self.SetX(240 - (self.Size[0] / 2))

        if self.ScreenPosition[1] <= 20:
            if self.Direction < 0:
                self.PointInDirection(-90 + self.Direction)
            else:
                self.PointInDirection(90 + self.Direction)
            self.SetY(180 - (self.Size[1] / 2))

        if self.ScreenPosition[1] + self.Size[1] >= 380:
            if self.Direction < 0:
                self.PointInDirection(-180 - self.Direction)
            else:
                self.PointInDirection(180 - self.Direction)
            self.SetY(-180 + (self.Size[1] / 2))


# Looks

    def Say(self, message="Hello", seconds=0):
        if message == "":
            self.Saying = ""
        self.Saying = message
        if seconds > 0:
            sleep(seconds)
            self.Saying = ""

    def Think(self,message="Hmmm...",seconds=0):
        if message == "":
            self.Thinking = ""
        self.Thinking = message
        if seconds > 0:
            sleep(seconds)
            self.Thinking = ""

    # Graphic effects not implemented

    def ChangeSize(self,size):
        self.Scale += (size / 100.0)
        self._updateCostume()

    def SetSize(self,percent):
        self.Scale = (percent / 100.0)
        self._updateCostume()

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
        if type(color) is tuple:
            self.PenColor.rgba =  (color[0], color[1], color[3], color[4])
        elif type(color) is str:
            self.PenColor = pygame.Color(color)
        elif type(color) is int:
            self.PenColor.hsva = (color, 100, 100, 100)
        elif type(color) is pygame.Color:
            self.PenColor = color

    def ChangePenColor(self,amount):
        hsva = self.PenColor.hsva
        self.PenColor.hsva = (hsva[0] + amount, hsva[1], hsva[2], hsva[3])

    def ChangePenShade(self,amount):
        hsva = self.PenColor.hsva
        self.PenColor.hsva = (hsva[0], hsva[1] + amount, hsva[2], hsva[3])

    def SetPenShade(self,percent):
        hsva = self.PenColor.hsva
        self.PenColor.hsva = (hsva[0], percent, hsva[2], hsva[3])

    def ChangePenSize(self,amount):
        self.PenSize += amount

    def SetPenSize(self,size):
        self.PenSize = size

# Sensing

    def Touching(self,item):
        selfrect = pygame.Rect(self.ScreenPosition, self.Size )
        if type(item) is Sprite:
            # the current implementation simply checks whether the two sprites' rectangles intersect.  Perhaps in the
            # future we can check if a non-transparent pixel in this sprite is intersecting a non-transparent pixel in the other
            otherrect = pygame.Rect(item.ScreenPosition, item.Size)
            return selfrect.colliderect(otherrect)
        elif type(item) is tuple:
            if len(item) == 2:  # point
                return selfrect.collidepoint(item[0], item[1])
            elif len(item) == 4: # rect
                otherrect = pygame.Rect(item[0], item[1], item[2], item[3])
                return selfrect.colliderect(otherrect)
        elif type(item) is str:
            side = item.lower().strip()
            if side == 'left':
                return self.ScreenPosition[0] <= 0
            elif side == 'right':
                return self.ScreenPosition[0] + self.Size[0] >= 480
            elif side == 'top':
                return self.ScreenPosition[1] <= 0
            elif side == 'bottom':
                return self.ScreenPosition[1] + self.Size[1] >= 380

        return False

    def DistanceTo(self,item):
        run = 0
        rise = 0
        if type(item) is Sprite:
            run = abs(item.Location[0] - self.Location[0])
            rise = abs(item.Location[1] - self.Location[1])
        elif type(item) is tuple:
            run = abs(item[0] - self.Location[0])
            rise = abs(item[1] - self.Location[1])

        return math.sqrt((run * run) + (rise * rise))


    # color-touching not implemented


    def Draw(self,screen):
        while self.Costume.get_locked():
            sleep(0.1)
        screen.blit(self.Costume, self.ScreenPosition)

        textimage = None
        if len(self.Thinking) > 0:
            textimage = self._rendertext(self.Thinking, pygame.Color("gray"))
        if len(self.Saying) > 0:
            textimage = self._rendertext(self.Saying, pygame.Color("black"))

        if textimage is not None:
            # TODO: Draw speech or thought bubble
            size = textimage.get_size()
            x = 0
            y = 0
            if self.ScreenPosition[0] + self.Size[0] + size[0] > 480:
                x = self.ScreenPosition[0] - size[0]
            else:
                x = self.ScreenPosition[0] + self.Size[0]
            if self.ScreenPosition[1] - size[1] > 20:
                y = self.ScreenPosition[1] - size[1]
            else:
                y = self.ScreenPosition[1] + self.Size[1]
            screen.blit(textimage, (x,y))

    def _rendertext(self, message, color):
        if message == "":
            return pygame.Surface((1,1), pygame.SRCALPHA,32)
        font = pygame.font.Font(None, 24)
        lines = message.split('\n')
        renderlines = []
        for line in lines:
            words = line.split(' ')
            renderline = ''
            for word in words:
                if len(renderline) < 25:
                    renderline += word + ' '
                else:
                    renderlines.append(renderline)
                    renderline = word + ' '
            if len(renderline) > 0:
                renderlines.append(renderline)
        lineimages = []
        totalheight = 0
        totalwidth = 0
        for line in renderlines:
            image = font.render(line, True, color)
            lineimages.append(image)
            size = image.get_size()
            totalheight += size[1] + 4
            totalwidth = size[0] if size[0] > totalwidth else totalwidth
        textsurface = pygame.Surface((totalwidth, totalheight),pygame.SRCALPHA, 32)
        y = 0
        for lineimage in lineimages:
            textsurface.blit(lineimage, (0,y))
            y += lineimage.get_size()[1] + 4

        return textsurface

    def _setPosition(self, x, y):
        oldLocation = self.Location
        self.Location = (x,y)

        screenx = x + 240 - (self.Size[0] / 2)
        screeny = 180 - y - (self.Size[1] / 2) + 20

        self.ScreenPosition = (screenx, screeny)

        if self.Drawing:
            pygame.draw.line(TheProject.PenSurface,self.PenColor, (oldLocation[0] + 240, 180 - oldLocation[1]),
                             (self.Location[0] + 240, 180 - self.Location[1]), self.PenSize)

        TraceDebug(self,"%s._setPosition: oldLocation=(%d,%d), Location=(%d,%d), ScreenPosition=(%d,%d) Drawing=%s" %
               (self.Name, oldLocation[0], oldLocation[1], self.Location[0], self.Location[1], self.ScreenPosition[0],
                self.ScreenPosition[1], self.Drawing))

    def _rotate(self, direction):
        TraceDebug(self, "_rotate: %d" % direction)
        self.Direction = direction
        self._updateCostume()

    def _angleTo(self, location):
        run = abs(self.Location[0] - location[0])
        rise = abs(self.Location[1] - location[1])
        return math.degrees(math.atan(rise / run))

    def _updateCostume(self):
        if self.CurrentCostume == "":
            baseCostume = self._turtle
        else:
            baseCostume = self.Costumes[self.CurrentCostume]

        angle = self.Direction if self.Direction > 0 else 360 + self.Direction

        self.Costume = pygame.transform.rotozoom(baseCostume, 90 - angle, self.Scale)
        self.Size = self.Costume.get_size()

        TraceDebug(self,"%s._updateCostume: CurrentCostume=%s, Direction=%d, Scale=%f, Size=(%d,%d)" %
              (self.Name, self.CurrentCostume, self.Direction, self.Scale, self.Size[0], self.Size[1]))

        self._setPosition(self.Location[0], self.Location[1])

    def _handleEvent(self,event):
        if event.type == pygame.MOUSEMOTION:
            inbounds = (self.ScreenPosition[0] <= event.pos[0] <= self.ScreenPosition[0] + self.Size[0]) and (
            self.ScreenPosition[1] <= event.pos[1] <= self.ScreenPosition[1] + self.Size[1])
            if self._mouseover and not inbounds:
                self._mouseover = False
                threading.Thread(None,self.WhenIAmMouseDeparted).start()
            if inbounds and not self._mouseover:
                self._mouseover = True
                threading.Thread(None,self.WhenIAmMouseEntered).start()
        else:
            super()._handleEvent(event)


class Project:
    Name = ""
    Running = True
    Screen = None
    Stage = None
    Sprites = {}

    PenSurface = None

    BackgroundThread = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snappy")
        self.Screen = pygame.display.set_mode((480, 380), 0, 32)
        self.Stage = StageSprite()
        self.PenSurface = pygame.Surface((480, 360), pygame.SRCALPHA, 32)

    def SetTheStage(self, stage):
        if type(stage) is not StageSprite:
            raise Exception("Cannot set the stage to a sprite.  It must be subclassed from StageSprite")
        self.Stage = stage

    def AddSprite(self, sprite):
        if sprite.Name in self.Sprites:
            i = 2
            newname = sprite.Name
            while newname in self.Sprites:
                newname = "%s(%d)" % (sprite.Name, i)
                i += 1
            sprite.Name = newname

        self.Sprites[sprite.Name] = sprite

    def RemoveSprite(self,sprite):
        if type(sprite) is str:
            if sprite in self.Sprites:
                del self.Sprites[sprite]
        elif type(sprite) is Sprite:
            index = list(self.Sprites.values()).index(sprite)
            if index >= 0:
                key = list(self.Sprites.keys())[index]
                del self.Sprites[key]

    # def MoveToFront(self,sprite):
    #
    # def MoveBack(self,sprite,layers):
    #     index = self.Sprites.index(sprite)
    #     self.Sprites.remove(sprite)
    #     if (index + layers) > len(self.Sprites):
    #         self.Sprites.append(sprite)
    #     else:
    #         self.Sprites.insert(index + 1, sprite)

    def Go(self):
        self.Running = True

    def Pause(self):
        self.Running = not self.Running

    def Stop(self):
        self.Running = False

    def Load(self, filename):
        pass

    def Save(self, filename):
        pass

    def Run(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if self.Running:
                    self.Stage._handleEvent(i)
                    for k in self.Sprites:
                        self.Sprites[k]._handleEvent(i)

            if self.Running:
                self.Stage.Draw(self.Screen)
                self.Screen.blit(self.PenSurface,(0,20))
                for k in self.Sprites:
                    if not self.Sprites[k].Hidden:
                        self.Sprites[k].Draw(self.Screen)

                pygame.display.update()


TheProject = Project()


class tracelevel(Enum):
    Error = 1
    Warn  = 2
    Info  = 3
    Debug = 4


TraceLevel = tracelevel.Error


def Trace(source, level, message):
    if level.value <= TraceLevel.value:
        if hasattr(source,"Name"):
            prefix = "Sprite[%s]" % source.Name
        elif type(source) is Project:
            prefix = "Project "
        elif type(source) is str:
            prefix = source + " "
        else:
            prefix = "%s[%s]" % (type(source), source) + " "
        print(prefix + message)


def TraceError(source, message):
    Trace(source,tracelevel.Error, message)


def TraceWarn(source, message):
    Trace(source,tracelevel.Warn, message)


def TraceInfo(source, message):
    Trace(source,tracelevel.Info, message)


def TraceDebug(source, message):
    Trace(source,tracelevel.Debug, message)