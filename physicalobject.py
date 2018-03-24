import pyglet
import settings

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        '''
            Initializes a physical object, e.g. player, wall, etc...
        '''
        # Inherits self.x, self.y: coordinate on screen
        super(PhysicalObject, self).__init__(*args, **kwargs)
        
        # Velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Keeps track of the previous (x,y)
        self.prev_x, self.prev_y = 0.0, 0.0
    
    def update(self,dt):
        '''
            Updates the physical object's location, given it's diretion.
        '''
        # Updates position from velocity
        self.prev_x = self.x
        self.x += self.velocity_x * dt
        
        self.prev_y = self.y
        self.y += self.velocity_y * dt
        
        self.check_bounds()

    def check_bounds(self):
        '''
            Ensures the physical object stays within the bounds of the window.
        '''
        min_x = 0
        min_y = 0
        max_x = settings.WINDOW_WIDTH - self.image.width 
        max_y = settings.WINDOW_HEIGHT - self.image.height 
        
        if self.x < min_x:
            self.velocity_x = 0
            self.x = min_x
        if self.y < min_y:
            self.velocity_y = 0
            self.y = min_y
        if self.x > max_x:
            self.velocity_x = 0
            self.x = max_x
        if self.y > max_y:
            self.velocity_y = 0
            self.y = max_y

    def collision(self, other):
        '''
            Checks if there is a collision between the physical object and other.
            Returns a boolean.
        '''

        if (self.x < other.x + other.image.width and
            self.x + self.image.width > other.x and
            self.y < other.y + other.image.height and
            self.y + self.image.height > other.y):
                self.velocity_x, self.velocity_y = 0.0, 0.0
                return True
        return False
        
    def handle_collision(self,other):
        '''
            Prevents two physical objects from colliding.
            
            By using the Kinkowski sum we figure out which side is hit in the rectangle.
            Changes in complexity depending on the shape.
        '''
        
        wy = (self.image.width + other.image.width) * (self.y - other.y)
        hx = (self.image.height + self.image.height) * (self.x - other.x)

        if (wy > hx):
            if (wy > -hx):
                # top
                self.y = other.y + other.image.height
            else:
                # left
                self.x = other.x - self.image.width
        else:
            if (wy > -hx):
                # right
                self.x = other.x + other.image.width
            else:
                # bottom
                self.y = other.y - self.image.width
        

