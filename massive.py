# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:04:42 2022

@author: uni
"""

from astropy import constants as const
import pygame
import numpy as np
import math


class Massive:
    AU = const.au.value
    G = 6.67428e-11 
    
    scale = 10/AU
    timestep = 3600 * 24
    
    def __init__(self, x, y, radius, color, mass, name="Massive"):
        self.x = x
        self.y = y
        self.radius =  np.log10(mass) * 1/ ( 2 *  np.sqrt(x**2 + y**2)/Massive.AU + 2)
        
        self.color = color
        self.mass = mass
        self.name = name
        
        self.trajectory = []
        
        self.x_vel = 0
        self.y_vel = 0
        
        self.track_points = int(np.sqrt(x**2 + y**2)/Massive.AU * 100 + 10)
        # print(self.track_points)
        
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = np.sqrt(distance_x**2 + distance_y**2) - (self.radius + other.radius) / self.scale

        
        force = self.G * self.mass * other.mass / distance**2
        theta = np.arctan2(distance_y, distance_x)
        force_x = np.cos(theta) * force
        force_y = np.sin(theta) * force 
        
        return force_x, force_y
    
    def draw(self, screen, FONT, FONTCOLOR):
        x = self.x * self.scale + screen.get_width() / 2
        y = self.y * self.scale + screen.get_height() / 2
        
        if len(self.trajectory) > 2 :
            updated_points = []
            for point in self.trajectory:
                x, y = point
                x = x * self.scale + screen.get_width() / 2
                y = y * self.scale + screen.get_height() / 2
                updated_points.append((x,y))
                
                
            pygame.draw.lines(screen, FONTCOLOR, False, updated_points[-self.track_points:], 1)        
        pygame.draw.circle(screen,self.color,(x,y), self.radius)
        
    def update_position(self, objects):
        total_fx = total_fy = 0
        total_fx = total_fy = 0 #total forces exerted on the planet from planet which are not in self
            
        for objec in objects: 
            if self == objec:
                continue
            
            fx, fy = self.attraction(objec)
            total_fx += fx
            total_fy += fy
    

        self.x_vel += total_fx / self.mass * self.timestep 
        self.y_vel += total_fy / self.mass * self.timestep
        
        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        
        if len(self.trajectory) > self.track_points:
            self.trajectory = self.trajectory[-self.track_points:]
            # print(self.name, len(self.trajectory))
        
        self.trajectory.append((self.x, self.y))
        
        
    
    
    
    
    
    
    
    
    
    