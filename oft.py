from random import random

from vec2d import vec2d




class Testicle: # a TESt parTICLE.

    def __init__(self, pos = None):

        #position
        if pos == None:
            self.pos = vec2d(350.0, 250.0)
        else:
            self.pos = vec2d(pos[0], pos[1])

        #direction
        chance = random()
        if chance < 0.5:
            factor = 1
        else:
            factor = -1
        x = random()*factor
        chance = random()
        if chance < 0.5:
            factor = 1
        else:
            factor = -1
        y = random()*factor
        self.dir = vec2d(x, y) #neat randomness, looks hefty but only happens
                               #at creation anyway. 'sides, it's a test.

    def advance(self):
        self.pos += self.dir

    def change_vec(self, new_dir):
        self.dir = new_dir

    def add_vec(self, vec):
        self.dir += vec
