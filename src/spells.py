from cmath import inf
from distutils.spawn import spawn
from lib2to3.pytree import HUGE
from shutil import which
import colorama
from colorama import Fore, Back, Style
import sys
import os
import math
import time
import copy
import time

from matplotlib.pyplot import bar
class Spells:
    def __init__(self, game):
        self.game = game
    def rage(self):
        for barbarian in self.game.barbarians:
            barbarian.vel *= 2
            barbarian.power *= 2
        self.game.king.vel *= 2
        self.game.king.power *= 2
    def heal(self, max_k_health, max_b_health):
        for barbarian in self.game.barbarians:
            if (math.ceil(barbarian.health * 1.5) <= max_b_health):
                barbarian.health = math.ceil(barbarian.health * 1.5)
            else:
                barbarian.health = max_b_health
                barbarian.color = Back.GREEN
            if (barbarian.health >= 4):
                barbarian.color = Back.GREEN
            if (barbarian.health < 4 and barbarian.health > 2):
                barbarian.color = Back.YELLOW
            if (barbarian.health <= 2 and barbarian.health > 0):
                barbarian.color = Back.RED
            
        if (math.ceil(self.game.king.health * 1.5) <= max_k_health):
            self.game.king.health = math.ceil(self.game.king.health * 1.5)
        else:
            self.game.king.health = max_k_health
            self.game.king.color = Back.GREEN
            return
        if (self.game.king.health >= 38):
            self.game.king.color = Back.GREEN
        if (self.game.king.health < 38 and self.game.king.health > 15):
            self.game.king.color = Back.YELLOW
        if (self.game.king.health <= 15 and self.game.king.health > 0):
            self.game.king.color = Back.RED
    def leviathan(self):
        for cannon in self.game.cannons:
            if ((cannon.x - self.game.king.x)**2 + (cannon.y - self.game.king.y)**2 <= 25):
                i = self.game.which_cannon(cannon.x, cannon.y)
                if (i == None):
                    continue
                if (self.game.cannons[i].health >= 0):
                    self.game.cannons[i].health = self.game.cannons[i].health - self.game.king.power
                    if (self.game.cannons[i].health <= 0):
                        self.game.cannons.pop(i)
                        continue
                if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                    self.game.cannons[i].color = Back.YELLOW
                if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                    self.game.cannons[i].color = Back.RED
        for hut in self.game.huts:
            if ((hut.x - self.game.king.x)**2 + (hut.y - self.game.king.y)**2 <= 25):
                i = self.game.which_hut(hut.x, hut.y)
                if (i == None):
                    continue
                if (self.game.huts[i].health >= 0):
                    self.game.huts[i].health = self.game.huts[i].health - self.game.king.power
                    if (self.game.huts[i].health <= 0):
                        self.game.huts.pop(i)
                        continue
                if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
                    self.game.huts[i].color = Back.YELLOW
                if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
                    self.game.huts[i].color = Back.RED
        for wall in self.game.walls:
            if ((wall.x - self.game.king.x)**2 + (wall.y - self.game.king.y)**2 <= 25):
                i = self.game.which_wall(wall.x, wall.y)
                if (i == None):
                    return
                if (self.game.walls[i].health >= 0):
                    self.game.walls[i].health = self.game.walls[i].health - self.game.king.power
                    if (self.game.walls[i].health <= 0):
                        self.game.walls.pop(i)
                        return
                if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
                    self.game.walls[i].color = Back.YELLOW
                if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
                    self.game.walls[i].color = Back.RED
        if (self.game.town_hall.is_dead == False):
            y = self.game.town_hall.y
            w = self.game.town_hall.width
            b = self.game.town_hall.breadth
            half_breadth = int(b/2)
            half_width  = int(w/2)
            for i in range(self.game.town_hall.x - half_breadth + 1, self.game.town_hall.x+half_breadth + 2):
                for j in range(self.game.town_hall.y - half_width + 1, self.game.town_hall.y+half_width + 1):
                    if ((i - self.game.king.x)**2 + (j - self.game.king.y)**2 <= 25):
                        if (self.game.town_hall.health >= 0):
                            self.game.town_hall.health = self.game.town_hall.health - self.game.king.power
                            if (self.game.town_hall.health <= 0):
                                self.game.town_hall.is_dead = True
                        if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                            self.game.town_hall.color = Back.YELLOW
                        if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                            self.game.town_hall.color = Back.RED
                        return
    def eagle_arrow(self, direction):
        # time.sleep(1)
        if (direction == 2):
            if (self.game.queen.x - 16 >= 0):
                aoe_center_x = self.game.queen.x - 16
                aoe_center_y = self.game.queen.y
            else:
                aoe_center_x = 0
                aoe_center_y = self.game.queen.y
        if (direction == 1):
            if (self.game.queen.x + 16 <= 24):
                aoe_center_x = self.game.queen.x + 16
                aoe_center_y = self.game.queen.y
            else:
                aoe_center_x = 24
                aoe_center_y = self.game.queen.y
        if (direction == 0):
            if (self.game.queen.y - 16 >= 0):
                aoe_center_x = self.game.queen.x
                aoe_center_y = self.game.queen.y - 16
            else:
                aoe_center_x = self.game.queen.x
                aoe_center_y = 0
        if (direction == 3):
            if (self.game.queen.y + 16 <= 24):
                aoe_center_x = self.game.queen.x
                aoe_center_y = self.game.queen.y + 16
            else:
                aoe_center_x = self.game.queen.x
                aoe_center_y = 24
        # print(aoe_center_x)
        # print(aoe_center_y)
        for hut in self.game.huts:
            if (hut.x >= aoe_center_x - 4 and hut.x <= aoe_center_x + 4 and hut.y >= aoe_center_y - 4 and hut.y <= aoe_center_y + 4):
                if (hut.health >= 0):
                    hut.health = hut.health - self.game.queen.power
                    if (hut.health <= 0):
                        self.game.huts.remove(hut)
                        continue
                if (hut.health < 5 and hut.health > 2):
                    hut.color = Back.YELLOW
                if (hut.health <= 2 and hut.health > 0):
                    hut.color = Back.RED
        for cannon in self.game.cannons:
            if (cannon.x >= aoe_center_x - 4 and cannon.x <= aoe_center_x + 4 and cannon.y >= aoe_center_y - 4 and cannon.y <= aoe_center_y + 4):
                if (cannon.health >= 0):
                    cannon.health = cannon.health - self.game.queen.power
                    if (cannon.health <= 0):
                        self.game.cannons.remove(cannon)
                        continue
                if (cannon.health < 5 and cannon.health > 2):
                    cannon.color = Back.YELLOW
                if (cannon.health <= 2 and cannon.health > 0):
                    cannon.color = Back.RED
        for wt in self.game.wizard_towers:
            if (wt.x >= aoe_center_x - 4 and wt.x <= aoe_center_x + 4 and wt.y >= aoe_center_y - 4 and wt.y <= aoe_center_y + 4):
                if (wt.health >= 0):
                    wt.health = wt.health - self.game.queen.power
                    if (wt.health <= 0):
                        self.game.wizard_towers.remove(wt)
                        continue
                if (wt.health < 5 and wt.health > 2):
                    wt.color = Back.YELLOW
                if (wt.health <= 2 and wt.health > 0):
                    wt.color = Back.RED
        for wall in self.game.walls:
            if (wall.x >= aoe_center_x - 4 and wall.x <= aoe_center_x + 4 and wall.y >= aoe_center_y - 4 and wall.y <= aoe_center_y + 4):
                if (wall.health >= 0):
                    wall.health = wall.health - self.game.queen.power
                    if (wall.health <= 0):
                        self.game.walls.remove(wall)
                        continue
                if (wall.health < 5 and wall.health > 2):
                    wall.color = Back.YELLOW
                if (wall.health < 2 and wall.health > 0):
                    wall.color = Back.RED
        w = self.game.town_hall.width
        b = self.game.town_hall.breadth
        half_breadth = int(b/2)
        half_width = int(w/2)
        for i in range(self.game.town_hall.x - half_breadth + 1, self.game.town_hall.x + half_breadth + 2):
                for j in range(self.game.town_hall.y - half_width + 1, self.game.town_hall.y + half_width + 1):
                    if (i >= aoe_center_x - 4 and i <= aoe_center_x + 4 and j >= aoe_center_y - 4 and j <= aoe_center_y + 4):
                        if (self.game.town_hall.health >= 0):
                            self.game.town_hall.health = self.game.town_hall.health - self.game.queen.power
                            if (self.game.town_hall.health <= 0):
                                self.game.town_hall.is_dead = True
                                return
                        if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                            self.game.town_hall.color = Back.YELLOW
                        if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
                            self.game.town_hall.color = Back.RED
                        return