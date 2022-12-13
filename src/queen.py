from cmath import inf
from distutils.spawn import spawn
from lib2to3.pytree import HUGE
from re import A
from shutil import which
import colorama
from colorama import Fore, Back, Style
import sys
import os
import math
import time
import copy
import time
class Queen:
    def __init__(self, game):
        self.game = game
        self.health = 75
        self.x = 0
        self.y = 0
        self.power = 0.5
        self.vel = 1
        self.color = Back.GREEN
        self.is_dead = False
    def spawn(self):
        if (self.is_dead == False):
            arr = self.game.board
            arr[self.x][self.y] = self.color + ' Q ' + Style.RESET_ALL
            self.game.board = arr

    def move(self, direction):
        # up (w)
        if (direction == 2):
            if (self.vel == 1):
                if (self.x > 0):
                    if (self.game.board[self.x - 1][self.y] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x - 1][self.y] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x - 1][self.y] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                        return
                    self.x = self.x - self.vel
            else:
                if (self.x > self.vel - 1):
                    for i in range(self.vel - 1):
                        if (self.game.board[self.x - (i+1)][self.y] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x - (i+1)][self.y] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x - (i+1)][self.y] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x - (i+1)][self.y] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                            return
                    self.x = self.x - self.vel
        # down (s)
        if (direction == 1):
            if (self.vel == 1):
                if (self.x < 24):
                    if (self.game.board[self.x + 1][self.y] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x + 1][self.y] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x + 1][self.y] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                        return
                    self.x = self.x + self.vel
            else:
                if (self.x <= 24 - self.vel):
                    for i in range(self.vel - 1):
                        if (self.game.board[self.x + (i+1)][self.y] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x + (i+1)][self.y] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x + (i+1)][self.y] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x + (i+1)][self.y] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                            return
                    self.x = self.x + self.vel
        # left (a) 
        if (direction == 0):
            if (self.vel == 1):
                if (self.y > 0):
                    if (self.game.board[self.x][self.y - 1] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x][self.y - 1] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x][self.y - 1] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                        return
                    self.y = self.y - self.vel
            else:
                if (self.y > self.vel - 1):
                    for i in range(self.vel - 1):
                        if (self.game.board[self.x][self.y - (i+1)] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x][self.y - (i+1)] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x][self.y - (i+1)] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - (i+1)] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                            return
                    self.y = self.y - self.vel
        # right (d)
        if (direction == 3):
            if (self.vel == 1):
                if (self.y < 24):
                    if (self.game.board[self.x][self.y + 1] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x][self.y + 1] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                        return
                    if (self.game.board[self.x][self.y + 1] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                        return
                    self.y = self.y + self.vel
            else:
                if (self.y <= 24 - self.vel):
                    for i in range(self.vel - 1):
                        if (self.game.board[self.x][self.y + (i+1)] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x][self.y + (i+1)] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL):
                            return
                        if (self.game.board[self.x][self.y + (i+1)] == Back.RED + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.RED + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.RED + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.WHITE + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + (i+1)] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                            return
                    self.y = self.y + self.vel
    def attack(self, direction):
        if (direction == 2):
            if (self.x - 8 >= 0):
                aoe_center_x = self.x - 8
                aoe_center_y = self.y
            else:
                aoe_center_x = 0
                aoe_center_y = self.y
        if (direction == 1):
            if (self.x + 8 <= 24):
                aoe_center_x = self.x + 8
                aoe_center_y = self.y
            else:
                aoe_center_x = 24
                aoe_center_y = self.y
        if (direction == 0):
            if (self.y - 8 >= 0):
                aoe_center_x = self.x
                aoe_center_y = self.y - 8
            else:
                aoe_center_x = self.x
                aoe_center_y = 0
        if (direction == 3):
            if (self.y + 8 <= 24):
                aoe_center_x = self.x
                aoe_center_y = self.y + 8
            else:
                aoe_center_x = self.x
                aoe_center_y = 24
        # print(aoe_center_x)
        # print(aoe_center_y)
        for hut in self.game.huts:
            if (hut.x >= aoe_center_x - 2 and hut.x <= aoe_center_x + 2 and hut.y >= aoe_center_y - 2 and hut.y <= aoe_center_y + 2):
                if (hut.health >= 0):
                    hut.health = hut.health - self.power
                    if (hut.health <= 0):
                        self.game.huts.remove(hut)
                        continue
                if (hut.health < 5 and hut.health > 2):
                    hut.color = Back.YELLOW
                if (hut.health <= 2 and hut.health > 0):
                    hut.color = Back.RED
        for cannon in self.game.cannons:
            if (cannon.x >= aoe_center_x - 2 and cannon.x <= aoe_center_x + 2 and cannon.y >= aoe_center_y - 2 and cannon.y <= aoe_center_y + 2):
                if (cannon.health >= 0):
                    cannon.health = cannon.health - self.power
                    if (cannon.health <= 0):
                        self.game.cannons.remove(cannon)
                        continue
                if (cannon.health < 5 and cannon.health > 2):
                    cannon.color = Back.YELLOW
                if (cannon.health <= 2 and cannon.health > 0):
                    cannon.color = Back.RED
        for wt in self.game.wizard_towers:
            if (wt.x >= aoe_center_x - 2 and wt.x <= aoe_center_x + 2 and wt.y >= aoe_center_y - 2 and wt.y <= aoe_center_y + 2):
                if (wt.health >= 0):
                    wt.health = wt.health - self.power
                    if (wt.health <= 0):
                        self.game.wizard_towers.remove(wt)
                        continue
                if (wt.health < 5 and wt.health > 2):
                    wt.color = Back.YELLOW
                if (wt.health <= 2 and wt.health > 0):
                    wt.color = Back.RED
        for wall in self.game.walls:
            if (wall.x >= aoe_center_x - 2 and wall.x <= aoe_center_x + 2 and wall.y >= aoe_center_y - 2 and wall.y <= aoe_center_y + 2):
                if (wall.health >= 0):
                    wall.health = wall.health - self.power
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
                    if (i >= aoe_center_x - 2 and i <= aoe_center_x + 2 and j >= aoe_center_y - 2 and j <= aoe_center_y + 2):
                        if (self.game.town_hall.health >= 0):
                            self.game.town_hall.health = self.game.town_hall.health - self.power
                            if (self.game.town_hall.health <= 0):
                                self.game.town_hall.is_dead = True
                                return
                        if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                            self.game.town_hall.color = Back.YELLOW
                        if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
                            self.game.town_hall.color = Back.RED
                        return
