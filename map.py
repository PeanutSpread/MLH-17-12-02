from pygame import*
from math import*
from random import*

## The map class for running the map randomizer and getting the location of walls
class gameMap(object):
    
    ## setting up the variables used between all of the methods
    def __init__(self,x,y,maxX,maxY,wall_percent):
        self.wallist = [] # The location of all of the wall blocks
        self.percent = wall_percent # The percentage of wall spawns
        self.maxx = maxX # The length of the window
        self.maxy = maxY # The height of the Window
    
    ## The main function called to make the map
    def map(self,x,y):
        self.background(x,y,(randint(50,125),randint(50,125),randint(50,125)))
        self.wall(x,y)
        
    ## The tiled background used to show spaces
    def background(self,x,y,borders):
        draw.rect(screen,(randint(50,125),randint(50,125),randint(50,125)),(x,y,self.maxx,self.maxy)) # The actual background colour
        # The border of each tile
        for x in range(0,self.maxx,square):
            for y in range (0,self.maxy,square):
                draw.rect(screen,borders,(x,y,square,square),2)
    
    ## The actual wall locations and the drawing of them
    def wall(self,x,y):
        for i in range (64,self.maxx-64,64):
                    for j in range (64,self.maxy-64,64):
                        if randint(0,self.percent) == 0:
                            self.wallist += [(i,j)] # List storing locations
                            draw.rect(screen,(0,0,0),(i,j,square,square))# Drawing the walls
    
    
    ## Returning the wall's locations
    def get_wallist(self):
        return self.wallist