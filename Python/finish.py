import pyglet
import os
from pyglet.window import key
import physicalobject

class Finish(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        '''
            Initializes a finishing point that transfers to the next level.
        '''
        # Sets the finish object's image.
        super(Finish, self).__init__(img=pyglet.resource.image("redsquare.png"), *args, **kwargs)

        #Event Handlers.
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
    
    def update(self, dt):
        '''
            Updates the block object.

            Where you put what needs to be updated every frame, e.g as movement.
        '''
        super(Finish, self).update(dt)

    
    def collision(self, other):
        '''
            Checks if the finish intersected with another object such as the player.
        '''
        super(Finish, self).collision(other)
