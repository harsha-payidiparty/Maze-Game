# Maze Game Overview:

This is a very simple pyglet game with two characters that move around trying to get to the finishing point.

This "game" only has movement, rectangle collision, and a way to get from start to finish.
If you reach the end of the level(finish) then the game will exit. The game was created in a code to connect event 
on March 16th, 2018 at the University of Toronto. 

There are 6 python files:
game.py, 
phyicaalobject.py, 
player.py, 
finish.py, 
block.py, 
settings.py, 

The rest are images. 

To start the game, double click on game.py. There, you will see 3 different colored squares
The two green squares are the players, the two red squares are the finish line, and the yellow squares are walls.

Each square has a corresponding file to it. Green corresponds to player.py, red corresponds to finish.py,
and yellow corresponds to block.py.
All three inherit from the file called physicalobject.py.

============GAME.PY============

game.py is the main file where all other objects get initialized, updated, and displayed on the screen.
game.py uses different classes such as the aforementioned players, finish and blocks, which are all physicalobjects.

init()

	This is where everything is initialized. 
	
on_draw()
	
	This is used to clear the window and draw the sprites. 
	
update(dt)
	
	This basically checks for collision. Some optimization to avoid double checking collisions twice.
	Checks if the finish line is reached. Also moves the objects.

============PHYSICALOBJECT.PY============

physicalobject.py is where you get all the functions.

update(self,dt)

	This is the general version of the update which is used by game.py's update.
	This just checks if an object is in bounds and moves the object using its velocity.
	
check_bounds(self)
	
	Keeps the object in the screen so it doesn't run away.
	
collision(self, other)

	Returns if there is a collision or not.
	
handle_collision(self,other)

	This returns what the objects will do if a collision is encountered.
	In general, I put it that it would not overlap with other.
	

============PLAYER.PY============

update(self, dt):
	
	In this update, this is where the movement and the event handling of 
	key presses happen. This is where the velocity is set as well. 
	That's why you can see the square moving around "smoothly."
	
Similarly to player.py, finish.py and block.py inherit from physicalobject.py and 
has the update and collision properties.


============SETTINGS.PY============

All the global variables are stored here



