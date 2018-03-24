import pyglet
from pyglet.window import key
import physicalobject

class Player(physicalobject.PhysicalObject):

    def __init__(self, p, *args, **kwargs):
        '''
            Initializes a Player object.
        '''
        # Sets the image for the player
        super(Player, self).__init__(img=pyglet.resource.image("greensquare.jpg"), *args, **kwargs)
        
        # Event Handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.p = p

    def update(self, dt):
        '''
            Updates the player object.

            Where you put what needs to be updated every frame, such as movement
            or a sprite change(implement this yourself).
        '''
        # Player movement
        if self.key_handler[key.LEFT]:
            self.x += -10

        if self.key_handler[key.RIGHT]:
            self.x += 10

        if self.key_handler[key.UP]:
            self.y += 10

        if self.key_handler[key.DOWN]:
            self.y += -10

        super(Player, self).update(dt)
