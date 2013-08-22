from random import random, randrange #I usually use these two.

import pygame  #this thing ain't gonna work without good ol' pygame.
from pygame.locals import *

from vec2d import vec2d #definitely gonna need vectors. Mhm, no doubt.

##### OBJECTS FOR TESTING #####
from oft import *
##### ------------------- #####

def displayGrid():
    global screen
    for x in range(700, None, 50):
        pass
        

def main():

    objects = [] #instantiating some objects from the OTest class to play with
    for i in range(2000):
        objects.append(OTest())

    
    

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((700,500), DOUBLEBUF)

    frames = 0
            
    try:
        while True:
            frames += 1
            time_passed = clock.tick(60)
            
            pygame.event.pump()

            #UPDATE ENTITIES! BWAHAHA
            buckets = [] #making the initial buckets
            for x in range(700/10):
                buckets.append([])
                for y in range(500/10):
                    buckets[x].append([])
            #placing references to the correct object in the buckets
            for obj in objects:
                posx = int(obj.pos.x/10)
                posy = int(obj.pos.y/10)
                buckets[posx][posy].append(obj)

            #FOR TESTING
            for x in range(len(buckets)):
                for y in range(len(buckets[x])):
                    for ref in buckets[x][y]:
                        ref.advance()
                        for other in buckets[x][y]:
                            if other == ref:
                                continue
                            else:
                                if ref.pos == other.pos:
                                    print "direct collision."
            #END TESTING STUFF

            pygame.display.set_caption("Frames: " + str(frames))
            screen.fill((0,0,0))
##            displayGrid()
            for obj in objects:
                posx = int(round(obj.pos.x))
                posy = int(round(obj.pos.y))
                pygame.draw.circle(screen, (255,255,255), (posx, posy), 2)
            pygame.display.update()
    except(KeyboardInterrupt):
        pygame.quit()


#begin!
main()
