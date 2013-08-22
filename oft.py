from random import random

from vec2d import vec2d




class OTest:

    def __init__(self, pos = None):

        #position
        if pos == None:
            self.pos = vec2d(random()*700.0, random()*500.0)
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
        if self.pos.x < 0:
            self.pos.x += 700.0
        elif self.pos.x > 700:
            self.pos.x -= 700.0
        if self.pos.y < 0:
            self.pos.y += 500.0
        elif self.pos.y > 500:
            self.pos.y -= 500.0

    def change_vec(self, new_dir):
        self.dir = new_dir

    def add_vec(self, vec):
        self.dir += vec
