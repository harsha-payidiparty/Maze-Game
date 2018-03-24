import pyglet
import os, platform

#Import globals
import settings

#Import other objects too 
import player, finish, block

#Size of the window screen
window = pyglet.window.Window(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)

#Collection of sprites to be populated and drawn later
main_batch = pyglet.graphics.Batch()

key = pyglet.window.key

#Initializing the event stack size
event_stack_size = 0


def init():
    '''
        Initializes global variables.
    '''
    # pl, fin, blo are the player, finishing point and blocks
    global p1, p2, fin1, fin2, blo, game_objects, event_stack_size
    
    # Iterates through the stack size and makes sure there aren't any handlers leftover
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    # Where objects get initiated
    p1 = player.Player(x=50, y=250, batch=main_batch, p=1)
    p2 = player.Player(x=200, y=250, batch=main_batch, p=2)
    fin1 = finish.Finish(x=50, y=0, batch=main_batch)
    fin2 = finish.Finish(x=500, y=250, batch=main_batch)

  
    game_objects = [p1,p2,fin1,fin2]
    
    # Build vertical walls

    for i in range(16):
        for j in range(12):
            if (settings.GAME_SCREEN[j][i] == 1):
                blo = block.Block(x = (i * 50), y = (550 - (j * 50)), batch=main_batch)
                game_objects.append(blo)
    
    for obj in game_objects:
        for handler in obj.event_handlers:
            window.push_handlers(handler)
            event_stack_size += 1


@window.event
def on_draw():
    '''
        Clears the window of previous drawn sprites and then redraws them depending on the update.
    '''
    window.clear()  
    main_batch.draw()

def update(dt):
    '''
        Checks if it collides, with the object and then further calls each objects own updates.
        
        Special object called finish.Finish that upon being collided with would execute a command
        that would close the current level and go to the next level.
        
        game_objects - a list of all the objects
        dt - delay time in seconds
        player.Player, finsih.Finish - The object type that was imported
    '''
    success = 0
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if obj_1.collision(obj_2):
                if((type(obj_1) == finish.Finish or type(obj_2) == finish.Finish) and
                   (type(obj_1) == player.Player or type(obj_2) == player.Player)):
                    success += 1
                    
                    if (success == 2):
                        window.close()
                        if platform.system() == "Windows":
                            os.system("py ../" + NEXT_GROUP + "/game.py")
                        else:
                            os.system("python ../" + NEXT_GROUP + "/game.py")
                obj_1.handle_collision(obj_2)
    
    #Updates every object from the initialized list
    for obj in game_objects:
        obj.update(dt)
  
if __name__ == "__main__":
    # Initializing Player and other objects
    init()
    # Update the game 120 times per second (fps)
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    # Tell pyglet to do its thing
    pyglet.app.run()




