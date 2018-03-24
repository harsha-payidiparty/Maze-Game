import pyglet, physicalobject
from pyglet.window import key

class Block(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        '''
            Initializes a block.
        '''
        # Sets the image for the block
        super(Block, self).__init__(img=pyglet.resource.image("yellowsquare.png"), *args, **kwargs)

        #Event Handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        '''
            Updates the block object.
            
            Where you put what needs to be updated every frame, e.g. movement.
        '''
        super(Block, self).update(dt)

    def collision(self, other):
        '''
            Checks if the block intersected with another object such as the player.
        '''
        super(Block, self).collision(other)

    
