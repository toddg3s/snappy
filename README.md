# snappy
Python version of UCB's Snap
(see http://snap.berkeley.edu)

Snappy is in an extremely early state at this point.  I've only been using Python for a couple
months, and I've only been working on Snappy for a few days, so if you happen to find this,
please don't think it is even alpha software.  You have been so warned.

This tool is being developed as an supplementary environment for students that are
using Snap! to learn coding.  It provides a basic framework of classes and methods 
that allow the student to create Snap-like projects, but using Python syntax instead
of dragging/dropping graphical blocks.

Snappy is built on top of the PyGame framework (http://pygame.org).  It does all 
of the heavy-lifting of actually drawing the sprites.  Snappy simply provides a 
structured framework to set the state of the sprites that are then drawn by PyGame.

Eventually, I will package this up and check it into a PyPI server, but for now, 
just clone the repo and add a new Python file for your project.  Really, all you need is
Snappy.py.  The other files in this repo are just informational.

# Set Up
Requirements:
* Python 3.6 or above  (http://www.python.org)
* PyGame 1.9.3 or above (python3 -m pip install pygame)

I'd also suggest an actual [Python IDE](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)
for beginners (which face it, is who will actually be using Snappy), but it's not required.

# Caveats

Snappy is currently pre-alpha state.  There are probably lots of bugs, and it hasn't been stress-tested at all.
In particular, there are several bits of Snap functionality that are not yet implemented (see [Blocks](blocks.md)).  
In addition, the functionality to start, pause and stop the program is not implemented, yet.  When the
project is run, it begins processing mouse and keyboard events, sending the appropriate messages
to the sprites.  You cannot pause a project, and the only way to stop it is to close the window.

# Creating a project
Create a new python file in the snappy directory and include this minimal code:

    from Snappy import TheProject
     
    TheProject.Run()

If you run the above code, all you will get is a blank stage that does nothing.
Pretty boring.

To add a little more fun, you can add a "sprite" to the project to actually get
something drawn.

    from Snappy import TheProject
    from Snappy import Sprite
     
    TheProject.AddSprite(Sprite())
    TheProject.Run()

Running this code will get you a lonely little turtle sitting in the middle of  the
screen (I decided to make the default sprite actually look like a turtle instead
of an arrowhead called a turtle).

To make things even more interesting, you will need to add a sprite that has actual 
code within it.  This is done by creating a new class that inherits from the Sprite
class, then adding code to respond to events that will make the sprite perform.

    from Snappy import TheProject
    from Snappy import Sprite
     
    class ScaredTurtle(Sprite):
        def WhenIAmClicked(self):
            self.Move(50)
     
    TheProject.AddSprite(ScaredTurtle())
    TheProject.Run()
    
 See [Blocks](blocks.md) for information about each block type