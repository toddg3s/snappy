from Snappy import *
import socket


class BTTraceListener:
    @staticmethod
    def write(source, level, message):
        if level == TraceLevel.Call and isinstance(source, Sprite):
            if source.Name in TheProject.Sprites:
                sprite = TheProject.Sprites[source.Name]
                if hasattr(sprite, 'socket'):
                    sprite.socket.send(bytes(message, 'UTF-8'))


class DebugSocket:
    name = ""

    def __init__(self, name):
        self.name = name

    def send(self, barray):
        print("%s: %s" % (self.name, barray))


def get_sprite(target):
    sprite = None
    if isinstance(target, Sprite):
        sprite = target
    elif type(target) is str and target in TheProject.Sprites:
        sprite = TheProject.Sprites[target]
    return sprite


def set_sprite_socket(target, mac_address, channel=1):
    sprite = get_sprite(target)
    if sprite is None:
        return

    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((mac_address, channel))
    sprite.socket = s


def set_sprite_debug_socket(target):
    sprite = get_sprite(target)
    if sprite is None:
        return

    sprite.socket = DebugSocket(sprite.Name)


def select_device(prompt, channel=None):
    devices = [('00:1f:e1:dd:08:3d', 'test1'), ('3d:08:dd:e1:15:00', 'test2')]

    if len(devices) == 0:
        return

    for i in range(len(devices)):
        print("%d) %s - %s" % (i, devices[i][1], devices[i][0]))
    select = input(prompt)
    if len(select) == 0:
        return
    index = -1
    try:
        index = int(select)
    except ValueError:
        pass

    if index == -1:
        return

    c = input('Channel #:') if channel is None else channel

    ch_num = -1
    try:
        ch_num = int(c)
    except ValueError:
        pass

    if ch_num == -1:
        return

    return devices[index][0], ch_num
