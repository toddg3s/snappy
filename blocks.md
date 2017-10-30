Block | Snappy Equivalent
--- | ---
_Motion_ | 
move _x_ steps | self.Move(_x_)
turn clockwise _x_ degrees | self.TurnClockwise(_x_)
turn counter-clockwise _x_ degrees | self.TurnCounterClockwise(_x_)
point in direction _x_ | self.PointInDirection(_x_)
point towards _x_ | self.PointTowards(_x_)<br/>_x_ can be a sprite, the name of a sprite, or a location tuple (_x_,_y_)
go to x: _x_ y: _y_ | self.GoTo(_item_)<br/>_item_ can be a sprite, the name of a sprite, or a location tuple (_x_,_y_)
glide _n_ secs to x: _x_ y: _y_ | self.Glide(_n_,_x_,_y_)
change x by _x_ | self.ChangeX(_x_)
set x to _x_ | self.SetX(_x_)
change y by _y_ | self.ChangeY(_y_)
set y to _y_ | self.SetY(_y_)
if on edge, bounce | self.IfOnEdgeBounce()
x position | self.Location\[0\]
y position | self.Location\[1\]
direction | self.Direction
&nbsp; | &nbsp;
_Control_ | 
when flag clicked | not implemented
when _key_ key pressed | def self.WhenKeyPressed(self, key): - code should use _key_ to decide what to do<br/>or<br/>def self.When_ _key_ _Pressed(self): for a method that handles a specific key (e.g. def When_r_Pressed(self):)
when I am _clicked_ | def WhenIAmClicked(self):
when I am _pressed_ | not implemented
when I am _dropped_ | not implemented
when I am _mouse-entered_ | def WhenIAmMouseEntered(self):
when I am _mouse-departed_ | def WhenIAmMouseDeparted(self):
when I receive _message_ | def WhenIReceive(self,message): - code should use _message_ to determine what to do
broadcast _message_ | self.Broadcast(_message_)
broadcast _message_ and wait | self.BroadcastAndWait(_message_)
wait _x_ seconds | use python `time.sleep(_x_)`
wait until _expr_ | use python  `while <expr>: time.sleep(0.1)`
forever | use python  `while True:` with inner code
repeat _n_ | use python  `for i in range(_n_):` with inner code
repeat until _expr_ | use python `while not <expr>:` with inner code
if _expr_ | use python `if <expr>:` with inner code
if _expr_ else | use python `if <expr>: else:` with inner code
&nbsp; | &nbsp;
_Looks_ | 
switch to costume _name_ | self.SwitchToCostume(_name_)
next costume | self.NextCostume()
costume # | self.CurrentCostume<br/>This is the _name_ of the costume, not the number
&nbsp; | Note: costumes are added to a sprite by calling its AddCostume(_costume_) method where _costume_ is either a string holding the path to an image file or a pygame.Surface object
say _msg_ for _n_ secs | self.Say(_msg_,_n_)
say _msg_ | self.Say(_msg_) or self.Say(_msg_,0)
think _msg_ for _n_ secs | self.Think(_msg_,_n_)
think _msg_ | self.Think(_msg_) or self.Think(_msg_,0)
change _e_ effect by _x_ | not implemented
set _e_ effect to _x_ | not implemented
clear graphic effects | not implemented
change size by _x_ | self.ChangeSize(_x_)
set size to _x_ % | self.SetSize(_x_)
size | self.Size
show | self.Show()
hide | self.Hide()
go to front | self.GoToFront()
go back _x_ layers | self.GoBack(_x_)
&nbsp; | &nbsp;
_Sensing_ | 
touching _item_ | self.Touching(_item_)<br/>_item_ can be a sprite, the name of a sprite, a location tuple (_x_,_y_) or any one of the following special strings: 'left', 'right', 'top', 'bottom' to check touching a given edge of the screen, or simply 'edge' to see if it's touching any edge
touching _color_ | not implemented
color _x_ touching _color_? | not implemented
ask _prompt_ and wait | self.AskAndWait(_prompt_)
answer | Snappy.Answer
mousex | Snappy.MouseX
mousey | Snappy.MouseY
mousedown | Snappy.MouseDown
key _key_ is pressed | self.KeyPressed(_key_)
distance to _item_ | self.DistanceTo(_item_)<br/>_item_ can be a sprite, the name of a sprite, or a location tuple (_x_,_y_)
reset timer | use python `timeit.default_timer()`
timer | use python `timeit.default_timer()`
_property_ of _sprite_ | TheProject.Sprites\[_name_\]._property_<br/>ex: `TheProject.Sprites['banana'].Size`
my _item_ | not implemented
turbo mode | not implemented
set turbo mode to _turbo_ | not implemented
current _date,year,month..._ | use python date/time functions
&nbsp; | &nbsp;
_Sound_ | 
play sound _sound_ | self.PlaySound(_sound_)<br/>_sound_ can be a string that holds the path to a WAV file to play, a pygame.mixer.Sound object or an array of sample data
play sound _sound_ until done | self.PlaySoundUntilDone(_sound_)<br/>see above for _sound_
stop all sounds | self.StopAllSounds()
rest for _n_ beats | self.Rest(_n_)
play note _x_ for _n_ beats | self.PlayNote(_x_,_n_)
set instrument to _x_ | not implemented
change tempo by _x_ | self.ChangeTempoBy(_x_)
set tempo to _x_ | self.SetTempo(_x_)
tempo | Snappy.Tempo
&nbsp; | &nbsp;
_Operators_ | 
all | All operators are built into python already
&nbsp; | &nbsp;
_Pen_ | 
clear | self.Clear()
pen down | self.PenDown()
pen up | self.PenUp()
set pen color to _color_ | self.SetPenColor(_color_)<br/>_color_ can be a color name (e.g. white, blue, etc.), a color tuple (_r_, _g_, _b_, _a_), an integer indicating a color hue (0 to 200), or a pygame.Color object
change pen color by _x_ | self.ChangePenColor(_x_)
set pen color to _x_ | self.SetPenColor(_x_)
change pen shade by _x_ | self.ChangePenShade(_x_)
set pen shade to _x_ | self.SetPenShade(_x_)
change pen size by _x_ | self.ChangePenSize(_x_)
set pen size to _x_ | self.SetPenSize(_x_)
stamp | not implemented
fill | not implemented
pen trails | not implemented
&nbsp; | &nbsp;
_Variables_ | 
all | all variables blocks are built into python language