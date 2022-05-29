# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:23:40 2022

@author: uni
"""

from astropy import constants as const
import pygame
import numpy as np
import math
from celestials import Body

class Ship(Body):
    
    def __init__(self, x, y, radius, color, mass, power, name="Ship"):
        Body.__init__(self, x, y, radius, color, mass, name=name)
        self.is_ship = True
        self.power = power
        self.radius = radius
        self.track_points = 100
        
        self.relative_velocities = {}
        self.distant_objects = {}
        self.distant_colors = {}
        
        
    
    
    
    def steering(self, keys_pressed):
        directions = {pygame.K_LEFT:   np.array([-1,  0]),
                      pygame.K_RIGHT:  np.array([ 1,  0]),
                      pygame.K_UP:     np.array([ 0, -1]),
                      pygame.K_DOWN:   np.array([ 0,  1]),
                      pygame.K_a:      np.array([-1,  0]),
                      pygame.K_d:      np.array([ 1,  0]),
                      pygame.K_w:      np.array([ 0, -1]),
                      pygame.K_s:      np.array([ 0,  1])}
        
        acc = np.array([0, 0])
        
        for key in directions:
            if keys_pressed[key]:
                #print(key)
                #print(directions[key])
                acc += directions[key]
            
        acc = self.power * acc
        #print("acc", acc)
        return acc[0], acc[1]
    
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
        
        
        max_speed_x = self.power/self.mass *  screen.get_width() * 10
        max_speed_y = self.power/self.mass *  screen.get_height() * 10
        
        max_vel = np.sqrt(max_speed_y**2 + max_speed_x**2)
        # print("alpha", alpha)
        line_x = - self.x_vel / max_vel / 20
        line_y = - self.y_vel / max_vel / 20
        
        # print("LLINE", line_x)
        #pygame.draw.polygon(screen, FONTCOLOR, ((x-line_x, y-self.radius), (x-line_x-self.radius, y), (x-line_x, y+self.radius))) 
        
        
        arr_scale = 2/4
        
        x_triangle = ( (x - line_x, y - self.radius * arr_scale), 
                       (x -  line_x + np.sign(self.x_vel) * self.radius, y), 
                       (x - line_x, y + self.radius * arr_scale) )      # x vel arrow head
        
        y_triangle = ( (x-self.radius*arr_scale, y-line_y), 
                       (x, y- line_y + np.sign(self.y_vel) * self.radius),
                       (x + self.radius * arr_scale, y - line_y) )      # y vel arrow head
        
        ship_arrow_col = self.WHITE
        ship_col = self.color
        if any(self.is_crashed.values()): 
            ship_arrow_col = self.RED
            ship_col = self.RED
        
        pygame.draw.polygon(screen, ship_arrow_col, x_triangle) # draw x vel arrow head
        pygame.draw.polygon(screen, ship_arrow_col, y_triangle) # draw y vel arrow head
        
        pygame.draw.rect(screen,ship_col,pygame.Rect((x-self.radius,y-self.radius), (self.radius*2, self.radius*2)) ) # draw ship object
        
        ## draw relative velocity errors on other objects
        
        # print(len(self.relative_velocities))
        
        for objec in self.distant_objects:
            
            other_x = self.distant_objects[objec][0] * self.scale + screen.get_width() / 2
            other_y = self.distant_objects[objec][1] * self.scale + screen.get_height() / 2
            relative_x, relative_y = self.relative_velocities[objec]
            color = self.distant_colors[objec]
            
            rel_line_x = - relative_x / max_vel / 20
            rel_line_y = - relative_y / max_vel / 20
            
            # print(other_x, other_y)
            
            # print(rel_line_x, rel_line_y)
            
            rel_x_triangle = ( (other_x - rel_line_x, other_y - self.radius * arr_scale),
                               (other_x - rel_line_x + np.sign(relative_x) * self.radius, other_y),
                               (other_x - rel_line_x, other_y + self.radius * arr_scale) )
            rel_y_triangle = ( (other_x - self.radius * arr_scale, other_y - rel_line_y),
                               (other_x, other_y - rel_line_y + np.sign(relative_y) * self.radius),
                               (other_x + self.radius * arr_scale, other_y - rel_line_y) )
            
            pygame.draw.polygon(screen, color, rel_x_triangle) # draw x vel arrow head
            pygame.draw.polygon(screen, color, rel_y_triangle) # draw y vel arrow head

            
    
    
    def update_position(self, objects, width, height):
        # total_fx = total_fy = 0
        # total_fx = total_fy = 0 
            
        # for objec in objects: 
        #     if self == objec:
        #         continue
            
        #     fx, fy = self.attraction(objec) #total forces exerted on the object from objects which are not itself
        #     total_fx += fx
        #     total_fy += fy
            
        # if self.is_ship:
        #     acc = self.steering(keys_pressed)
        #     #print(acc)
        #     total_fx += acc[0]
        #     total_fy += acc[1]
    

        # self.x_vel += total_fx / self.mass * self.timestep 
        # self.y_vel += total_fy / self.mass * self.timestep
        
        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        
        # print(self.x * self.scale + width/2)
        
        # x boundaries
        if self.x * self.scale + width/2 < 0: 
            self.x = -width/2/self.scale
            self.x_vel *= -.1
         
        if self.x * self.scale + width/2 > width: 
            self.x = width/2/self.scale
            self.x_vel *= -.1
            
        # y boundaries
        if self.y * self.scale + height/2 < 0: 
            self.y = -height/2/self.scale
            self.y_vel *= -.1
         
        if self.y * self.scale + height/2 > height: 
            self.y = height/2/self.scale
            self.y_vel *= -.1
            
        #if self.x > self.x * self.scale - width/2: self.x = -width/2
        #if self.y > height/2: self.y = height/2
        #if self.y < -height/2: self.y = -height/2
        
        # print("post", self.y * self.scale)
        
        if len(self.trajectory) > self.track_points:
            self.trajectory = self.trajectory[-self.track_points:]
            # print(self.name, len(self.trajectory))
        
        self.trajectory.append((self.x, self.y))
        
        
    def update_velocity(self, objects, keys_pressed):
        total_fx = total_fy = 0
        total_fx = total_fy = 0 
            
        for objec in objects: 
            if self == objec:
                continue
            
            fx, fy = self.attraction(objec) #total forces exerted on the object from objects which are not itself
            total_fx += fx
            total_fy += fy
            
            relative_x_vel = self.x_vel - objec.x_vel
            relative_y_vel = self.y_vel - objec.y_vel
            self.relative_velocities[objec.name] = [relative_x_vel, relative_y_vel]
            self.distant_objects[objec.name] = [objec.x, objec.y]
            self.distant_colors[objec.name] = objec.color
            
            
            
            
        #if self.is_ship:
        acc = self.steering(keys_pressed)
            #print(acc)
        total_fx += acc[0]
        total_fy += acc[1]
    

        self.x_vel += total_fx / self.mass * self.timestep 
        self.y_vel += total_fy / self.mass * self.timestep