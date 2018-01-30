import pygame, math, random
from math import cos, sin
from pygame.locals import *
from pygame.draw import *
from newvector import Vec2

###############################################################################

class Game:
    def __init__(self, size=512, gsize=640):
        pygame.init()
        self.size = size
        self.gsize = gsize
        self.surface = pygame.display.set_mode((size, size))
        self.clock = pygame.time.Clock()
        self.player = Player(self.surface, self.gsize)
        self.stations = {}

    def calcFrame(self):

        # Get keys active on this frame
        keys = pygame.key.get_pressed()

        # Limit framerate to ~60fps
        self.clock.tick(60)

        # Quitting on ESC
        if keys[K_ESCAPE]:
            return False

        # No uses yet for events
        # Keeping this here in case i forget the syntax
        for event in pygame.event.get():
            pass

        # Do a physics update on the ship
        self.player.physUpdate(keys)

        # Preserving the loop
        return True

    def drawFrame(self):
        self.surface.fill(0x000000)

        # Drawing 4 square regions
        for gx in range(2):
            for gy in range(2):

                # Deterministic seed for each region
                random.seed(seed2(self.player.pos.x // 1 - gx, self.player.pos.y // 1 - gy))

                # Drawing n random stars per region
                ofs = Vec2([self.gsize * (gx + (self.player.pos.x % 1) - 1), self.gsize * (gy + (self.player.pos.y % 1) - 1)])
                for _ in range(200):

                    # Position of star
                    x_ = random.randint(0, self.gsize) - ofs.x
                    y_ = random.randint(0, self.gsize) - ofs.y

                    # Drawing stars either all white or random colors
                    line(self.surface, random.randint(0, 2**24), (x_, y_), (x_, y_))

                # Condition for the station to appear
                if random.randint(0, 256) > 245:

                    # Draw position of the station
                    x_ = random.randint(0, self.gsize) - ofs.x
                    y_ = random.randint(0, self.gsize) - ofs.y

                    # Working out global position and id of the station
                    spos = Vec2([self.player.pos.x+x_/self.gsize, self.player.pos.y+y_/self.gsize])
                    i_ = '{0}:{1}'.format(int(spos.x), int(spos.y))

                    # Making sure the station doesn't already exist
                    if not i_ in self.stations.keys():
                        # If it doesn't, create a new one
                        self.stations[i_] = Station(spos.x, spos.y)

                    # Placeholder image
                    circle(self.surface, 0xFFFFFF, (int(x_), int(y_)), 50)


        # Drawing the ship
        self.player.draw()
        pygame.display.update()

    def loop(self, v=True):
        running = True
        while running:
            running = self.calcFrame()
            self.drawFrame()

            # If i want runtime details
            if v:
                print('\n\n\n\n\n\n\n\n\n\n\n\n')
                print(self.player.vel)
                print(self.player.pos)
                print(self.stations)
                print(round(self.clock.get_fps(), 2))


class Player:

    # Tuning parameters
    velmult = 0.0001
    rotmult = 0.0125

    def __init__(self, surface, gsize):
        self.surface = surface
        self.hed = 0
        self.pos = Vec2([0, 0])
        self.vhd = 0
        self.vel = Vec2([0, 0])
        self.gsize = gsize

    def physUpdate(self, keys):

        # Changing speed of rotation
        if keys[K_a]: # Accelerating left
            self.vhd = max(self.vhd - self.rotmult, -self.rotmult*10)
        if keys[K_d]: # Accelerating right
            self.vhd = min(self.vhd + self.rotmult, self.rotmult*10)
        if not(keys[K_a] or keys[K_d]): # Rotation velocity decay
            self.vhd = math.copysign(max(abs(self.vhd) - self.rotmult, 0), self.vhd)
        
        # Changing rotation angle
        self.hed = (self.hed + self.vhd) % (2*math.pi)

        # Changing velocity
        if keys[K_w]: # Moving forward
            self.vel += Vec2.fromAngle(self.hed) * self.velmult
        if keys[K_s]: # Moving backward
            self.vel -= Vec2.fromAngle(self.hed) * self.velmult
        if keys[K_x]: # Killing velocity
            self.vel = self.vel.withMag(max(self.vel.mag() - self.velmult, 0))

        # Adding velocity to position
        self.pos += self.vel

        # DEBUG KEY TO TELEPORT TO STATION
        if keys[K_q]:
            self.pos.set([19, 8])

    def draw(self):

        # Screen center
        x_ = self.surface.get_width()//2
        y_ = self.surface.get_height()//2

        # Drawing ship
        h = self.hed
        l_ = [[cos(h)*10, sin(h)*10],
              [cos(h+0.6)*6, sin(h+0.6)*6],
              [cos(h+(math.pi-0.6))*6, sin(h+(math.pi-0.6))*6], 
              [cos(h+(math.pi-0.4))*5, sin(h+(math.pi-0.4))*5], 
              [cos(h+(math.pi-0.4))*9, sin(h+(math.pi-0.4))*9], 
              [cos(h+math.pi)*8, sin(h+math.pi)*8], 
              [cos(h-(math.pi-0.4))*9, sin(h-(math.pi-0.4))*9], 
              [cos(h-(math.pi-0.4))*5, sin(h-(math.pi-0.4))*5], 
              [cos(h-(math.pi-0.6))*6, sin(h-(math.pi-0.6))*6],
              [cos(h-0.6)*6, sin(h-0.6)*6]]
        l_ = [[l[0]+x_, l[1]+y_] for l in l_]
        lines(self.surface, 0xFFFFFF, True, l_)


class Station:
    lazspd = 0.001

    def __init__(self, x, y):
        self.typ = random.choice(['Hostile', 'Trade', 'Derelict'])
        self.cls = random.randint(1, 5)

        self.pos = Vec2([x, y])

    def attack(self):
        fvec = game.player.pos - self.pos
        fvec /= fvec.mag()
        fvec *= self.lazspd
        
        pass

    def __repr__(self):
        return '{} V{} Station'.format(self.typ, self.cls)

# Combine two integers into one, unique integer
seed2 = lambda x,y:int(((x+y)**2+3*x+y)/2)

###############################################################################



###############################################################################

game = Game()
game.loop()