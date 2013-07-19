#!/usr/bin/env python

"""A simple starfield example. Note you can move the 'center' of
the starfield by leftclicking in the window. This example show
the basics of creating a window, simple pixel plotting, and input
event management"""


import random, math, pygame
from pygame.locals import *

#constants
WINSIZE = [740, 580] # initial 640 x 480
WINCENTER = [370, 290]
NUMSTARS = 15000 #initial value 150


def init_star():
    "creates new star values"
    dir = random.randrange(100000)
    velmult = random.random()*.6+.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]


def initialize_stars():
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        vel, pos = star
        steps = random.randint(0, WINCENTER[0])
        pos[0] = pos[0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * .02) #initial steps * .09
        vel[1] = vel[1] * (steps * .02) #initial steps * .09
        stars.append(star)
    move_stars(stars)
    return stars
  

def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)


def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            vel[:], pos[:] = init_star()
        else:
            vel[0] = vel[0] * 1.05
            vel[1] = vel[1] * 1.05
  

def main():
    "This is the starfield code"
    #create our starfield
    random.seed()
    stars = initialize_stars()
    clock = pygame.time.Clock()
    #initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('pygame Stars Example')
    white = 255, 240, 200
    black = 0, 0, 0		# originally 20, 20, 40
    yellow = 255, 255, 0
    red = 255, 0, 0
    screen.fill(black)
    
    #Color	Red	Green	Blue	Hexadecimal
	#Black 	0 	0 	0 	#000000
	#White 	255 255	255	#FFFFFF
	#Red 	255	0 	0 	#FF0000
	#Green 	0 	192 0 	#00C000
	#Blue 	0 	0 	255 #0000FF
	#Yellow 255 255 0 	#FFFF00

    #main game loop
    done = 0
    while not done:
        draw_stars(screen, stars, black)
        move_stars(stars)
        some_colors = [white, yellow, red, white, yellow, white]
        g = random.randint(0, 5)
        draw_stars(screen, stars, some_colors[g])#  white)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
        clock.tick(50)


# if python says run, then we should run
if __name__ == '__main__':
    main()


