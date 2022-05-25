# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:12:39 2022

@author: uni
"""

from astropy import constants as const
import pygame
import numpy as np
import math
from massive import Massive

class Body(Massive):
 
    def __init__(self, x, y, radius, color, mass, name="Body"):
       
        Massive.__init__(self, x, y, radius, color, mass, name=name) 
        self.sun = False
        self.distance_to_sun = 0
        
    def draw(self, screen, FONT, FONTCOLOR):
        
        Massive.draw(self, screen, FONT, FONTCOLOR)
        
        if not self.sun:
            # print("not sun")
            distance_text = FONT.render(f"{round(self.distance_to_sun/self.AU, 1)}AU", 1, FONTCOLOR)
            #print(distance_text)
            screen.blit(distance_text, (self.x * self.scale + screen.get_width()/2, self.y * self.scale + screen.get_height()/2 + 20) )
            name_text = FONT.render(f"{self.name}", 1, FONTCOLOR)
            screen.blit(name_text, (self.x * self.scale + screen.get_width()/2, self.y * self.scale + screen.get_height()/2) )
    
      
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = np.sqrt(distance_x**2 + distance_y**2) #- (self.radius + other.radius) / self.scale
        
        if other.sun:
            # print("other sun")
            self.distance_to_sun = distance
            
        # print(distance)
        if distance < (self.radius + other.radius) / self.scale:
            print( "CRASH" )
            #self.x_vel *= -1
            #self.y_vel *= -1
            return 0, 0
        
        force = self.G * self.mass * other.mass / distance**2
        theta = np.arctan2(distance_y, distance_x)
        force_x = np.cos(theta) * force
        force_y = np.sin(theta) * force 
        
        return force_x, force_y
    

      

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        