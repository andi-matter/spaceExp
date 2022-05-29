# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:46:03 2022

@author: uni
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:27:44 2022

@author: uni
"""

import pygame
from pygame.locals import *
import numpy as np

from celestials import Body
from ship import Ship

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


mass = 5.9742*10**29
velo = 10 * 1000


body1 = Body(-0.7*Body.AU, 0, 6, BLUE, mass/1000, name="Body 1")
body1.y_vel = velo*1.237

body0 = Body(.85*Body.AU, 0, 6, YELLOW, mass/1000, name="Body 0")
body0.y_vel = -velo*1.237

body2 = Body(0, 0, 16, GREY, mass, name="Body 2")
body2.y_vel = 0
body2.sun = True
# body2.mass = 0.1

body3 = Body(3*Body.AU, 0, 6, URANUS_BLUE, mass/100, name="Body 3")
body3.y_vel = -velo*1.0

body4 = Body(-3*Body.AU, 0, 6, URANUS_BLUE, mass/100, name="Body 3 too")
body4.y_vel = velo*1.0

body3_moon = Body(3.11*Body.AU, 0, 6, DARK_GREY, mass/1000/300, name="Body 3 Moon")
body3_moon.y_vel = -velo*1.5
#body3_moon.x_vel = -1.0*1000

interloper = Body(-2*Body.AU, -0.4*Body.AU, 5, DARK_GREY, mass/100000, name="Comet")
interloper.y_vel = 9 * 1000
interloper.x_vel = 5 * 1000

ship = Ship(2*Body.AU, 2*Body.AU, 5, RED, 1000, 1.5, name="Ship")

objects = [ ship , body2,  body0,  body3, body4, interloper]

# objects = objects[0, 2]

#-------------------------------------
pygame.init()
clock = pygame.time.Clock() #to keep running the simulation on specified time

width, height = 800, 800

Body.scale *= 10

FONT = pygame.font.SysFont('couriernew', 18)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Planet Simulation")



running = True

while running:
    clock.tick(90) #Changes will occur at 60 tick rate
    screen.fill((0,0,0)) #Window Bg
    
    time_text = FONT.render(f"{pygame.time.get_ticks()//1000}", 1, WHITE)
    screen.blit(time_text, (width/2, 0))
    
    keys_pressed = pygame.key.get_pressed()
    
    #print(keys_pressed)
    
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
              
    
    for i, obj in enumerate(objects):
        #print("here")
        # planet.update_position(objects)
        
        # print(obj.name)
        
        if type(obj) == Ship:
            obj.update_velocity(objects, keys_pressed)
        else:
            obj.update_velocity(objects)
    
        crashed_text = FONT.render(f"{obj.name} is crashed? {any(obj.is_crashed.values())}", 1, WHITE)
        screen.blit(crashed_text, (width/2-crashed_text.get_width(), height -20 - i * 20))
    
    for obj in objects:
        #print("here")
        # planet.update_position(objects)
        
        if type(obj) == Ship:
            obj.update_position(objects, width, height)
        else:
            obj.update_position(objects)
            
        obj.draw(screen, FONT, WHITE)
            
    pygame.display.update()

pygame.quit()


