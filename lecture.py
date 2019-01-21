import pyglet
import time

class lecture:
    
    def play(self, video):
        
        self.video = video
        
        window = pyglet.window.Window(fullscreen = True)
        #window = pyglet.window.Window(300,300)
        player = pyglet.media.Player() 
        MediaLoad = pyglet.media.load(self.video)  
        player.queue(MediaLoad) 
        player.play()
         
        @window.event
        def on_draw():
            time.sleep(6)
            window.clear()
            player.get_texture().blit(0,0)
        
        pyglet.app.run()
        
