from random import random, randrange #I usually use these two.

import pygame  #this thing ain't gonna work without good ol' pygame.
from pygame.locals import *

from vec2d import vec2d #definitely gonna need vectors. Mhm, no doubt.

##### OBJECTS FOR TESTING #####
from oft import *
##### ------------------- #####



def main():

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((768,512), DOUBLEBUF)

    frames = 0
            
    try:
        while True:
            frames += 1
            time_passed = clock.tick(60)
            
            pygame.event.pump()

            #UPDATE ENTITIES! BWAHAHA

            pygame.display.set_caption("Frames: " + str(frames))
            screen.fill((0,0,0))
            pygame.display.update()
    except(KeyboardInterrupt):
        pygame.quit()


#begin!
main()
