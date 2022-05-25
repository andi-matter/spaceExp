# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:27:44 2022

@author: uni
"""

import pygame
from pygame.locals import *
import numpy as np

from celestials import Planet

#------------------------------------
#Color Section
GREY = (128,128,128) #mercury
YELLOWISH = (165,124,27) #venus
BLUE = (0,0,225) #for earth
RED = (198, 123, 92) #mars
BROWN = (144, 97, 77) #jupiter
CARMEL = (195, 161, 113) #saturn
URANUS_BLUE = (79, 208, 231) #uranus
NEPTUNE = (62, 84, 232) #neptune
WHITE = (255, 255, 255) #for text
YELLOW = (255, 255, 0) #for sun
DARK_GREY = (80,78,81) #orbit

#print(pygame.font.get_fonts())

#-------------------------------------

sun = Planet(0,0,20, YELLOW, 1.98892 * 10**30, name="Sun")
sun.sun = True

mercury = Planet(0.387 * Planet.AU, 0, 8, GREY, 3.30 * 10**24, name="Mercury")
mercury.y_vel = 47.4 * 1000 #Kilometer * 1000 = meter

venus = Planet(0.723 * Planet.AU, 0, 14, YELLOWISH, 4.8685 * 10**24, name="Venus")
venus.y_vel = -35.02 * 1000 #Kilometer * 1000 = meter

earth = Planet(-1*Planet.AU, 0, 16, BLUE, 5.9742*10**24, name="Earth")
earth.y_vel = 29.783 * 1000 #Kilometer * 1000 = meter

mars = Planet(-1.524*Planet.AU, 0, 12, RED, 6.39 * 10**23, name="Mars")
mars.y_vel = 24.077 * 1000 #Kilometer * 1000 = meter

jupiter = Planet(3.203 * Planet.AU, 0, 16, BROWN, 1000.13 * 10**24, name="Jupiter")
jupiter.y_vel = 15.06 * 1000 #Kilometer * 1000 = meter

saturn = Planet(9.537 * Planet.AU, 0, 16, CARMEL, 568.32 * 10**24, name="Saturn")
saturn.y_vel = 9.68 * 1000 #Kilometer * 1000 = meter

uranus = Planet(19.191 * Planet.AU, 0, 16, URANUS_BLUE, 86.811 * 10**24, name="Uranus")
uranus.y_vel = 6.80 * 1000 #Kilometer * 1000 = meter

neptune = Planet(30.068 * Planet.AU, 0, 16, NEPTUNE, 102.409 * 10**24, name="Neptune")
neptune.y_vel = 5.43 * 1000 #Kilometer * 1000 = meter

pluto = Planet(39.481 * Planet.AU, 0, 16, BROWN, 0.01303 * 10**24, name="Pluto")
pluto.y_vel = 4.67 * 1000 #Kilometer * 1000 = meter


interloper = Planet(-2*Planet.AU, -0.4*Planet.AU, 5, DARK_GREY, 10**10, name="Comet")
interloper.y_vel = 10 * 1000

planets = [interloper, sun, earth, mars, mercury, venus, jupiter,]# saturn, uranus, neptune, pluto]


mass = 5.9742*10**29
velo = 10 * 1000

body1 = Planet(-0.7*Planet.AU, 0, 6, BLUE, mass/1000, name="Body 1")
body1.y_vel = velo*1.237

body0 = Planet(.7*Planet.AU, 0, 6, YELLOW, mass/1000, name="Body 0")
body0.y_vel = -velo*1.237

body2 = Planet(0, 0, 16, GREY, mass, name="Body 2")
body2.y_vel = 0
body2.sun = True

body3 = Planet(3*Planet.AU, 0, 6, URANUS_BLUE, mass/900, name="Body 3")
body3.y_vel = -velo*1.0

body3_moon = Planet(3.11*Planet.AU, 0, 6, DARK_GREY, mass/1000/300, name="Body 3 Moon")
body3_moon.y_vel = -velo*1.5
#body3_moon.x_vel = -1.0*1000

interloper = Planet(-2*Planet.AU, -0.4*Planet.AU, 5, DARK_GREY, mass/100000, name="Comet")
interloper.y_vel = 9 * 1000
interloper.x_vel = 5 * 1000

bodies = [body0, body1, body2, body3, interloper]# body3_moon]


#-------------------------------------
pygame.init()
clock = pygame.time.Clock() #to keep running the simulation on specified time

width, height = 800, 800

Planet.scale *= 10

FONT = pygame.font.SysFont('couriernew', 18)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Planet Simulation")

print(screen.get_width())

print(type(screen))

running = True

while running:
    clock.tick(500) #Changes will occur at 60 tick rate
    screen.fill((0,0,0)) #Window Bg
    
    time_text = FONT.render(f"{pygame.time.get_ticks()//1000}", 1, WHITE)
    screen.blit(time_text, (width/2, 0))
    
    
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
         
    objects = bodies        
    
    for obj in objects:
        #print("here")
        # planet.update_position(objects)
        obj.update_position(objects)
        
        obj.draw(screen, FONT, WHITE)
            
    pygame.display.update()

pygame.quit()


