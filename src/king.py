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
class King:
    def __init__(self, game):
        self.game = game
        self.health = 75
        self.x = 0
        self.y = 0
        self.power = 1
        self.vel = 1
        self.color = Back.GREEN
        self.is_dead = False
    def spawn(self):
        if (self.is_dead == False):
            arr = self.game.board
            arr[self.x][self.y] = self.color + ' K ' + Style.RESET_ALL
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
            if (self.game.board[self.x - 1][self.y] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' H ' + Style.RESET_ALL):
                i = self.game.which_hut(self.x - 1, self.y)
                if (i == None):
                    return
                if (self.game.huts[i].health >= 0):
                    self.game.huts[i].health = self.game.huts[i].health - self.power
                    if (self.game.huts[i].health <= 0):
                        self.game.huts.pop(i)
                        return
                if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
                    self.game.huts[i].color = Back.YELLOW
                if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
                    self.game.huts[i].color = Back.RED
            if (self.game.board[self.x - 1][self.y] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.WHITE + ' C ' + Style.RESET_ALL):
                i = self.game.which_cannon(self.x - 1, self.y)
                if (i == None):
                    return
                if (self.game.cannons[i].health >= 0):
                    self.game.cannons[i].health = self.game.cannons[i].health - self.power
                    if (self.game.cannons[i].health <= 0):
                        self.game.cannons.pop(i)
                        return
                if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                    self.game.cannons[i].color = Back.YELLOW
                if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                    self.game.cannons[i].color = Back.RED
            if (self.game.board[self.x - 1][self.y] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                i = self.game.which_wt(self.x - 1, self.y)
                if (i == None):
                    return
                if (self.game.wizard_towers[i].health >= 0):
                    self.game.wizard_towers[i].health = self.game.wizard_towers[i].health - self.power
                    if (self.game.wizard_towers[i].health <= 0):
                        self.game.wizard_towers.pop(i)
                        return
                if (self.game.wizard_towers[i].health < 5 and self.game.wizard_towers[i].health > 2):
                    self.game.wizard_towers[i].color = Back.YELLOW
                if (self.game.wizard_towers[i].health < 2 and self.game.wizard_towers[i].health > 0):
                    self.game.wizard_towers[i].color = Back.RED
            if (self.game.board[self.x - 1][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
                i = self.game.which_wall(self.x - 1, self.y)
                if (i == None):
                    return
                if (self.game.walls[i].health >= 0):
                    self.game.walls[i].health = self.game.walls[i].health - self.power
                    if (self.game.walls[i].health <= 0):
                        self.game.walls.pop(i)
                        return
                if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
                    self.game.walls[i].color = Back.YELLOW
                if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
                    self.game.walls[i].color = Back.RED
            if (self.game.board[self.x - 1][self.y] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y] == Back.RED + ' T ' + Style.RESET_ALL):
                if (self.game.town_hall.health >= 0):
                    self.game.town_hall.health = self.game.town_hall.health - self.power
                    if (self.game.town_hall.health <= 0):
                        self.game.town_hall.is_dead = True
                if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                    self.game.town_hall.color = Back.YELLOW
                if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                    self.game.town_hall.color = Back.RED

        if (direction == 0):
            if (self.game.board[self.x][self.y - 1] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' H ' + Style.RESET_ALL):
                i = self.game.which_hut(self.x, self.y - 1)
                if (i == None):
                    return
                if (self.game.huts[i].health >= 0):
                    self.game.huts[i].health = self.game.huts[i].health - self.power
                    if (self.game.huts[i].health <= 0):
                        self.game.huts.pop(i)
                        return
                if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
                    self.game.huts[i].color = Back.YELLOW
                if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
                    self.game.huts[i].color = Back.RED
            if (self.game.board[self.x][self.y - 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.WHITE + ' C ' + Style.RESET_ALL):
                i = self.game.which_cannon(self.x, self.y - 1)
                if (i == None):
                    return
                if (self.game.cannons[i].health >= 0):
                    self.game.cannons[i].health = self.game.cannons[i].health - self.power
                    if (self.game.cannons[i].health <= 0):
                        self.game.cannons.pop(i)
                        return
                if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                    self.game.cannons[i].color = Back.YELLOW
                if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                    self.game.cannons[i].color = Back.RED
            if (self.game.board[self.x][self.y - 1] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                i = self.game.which_wt(self.x, self.y - 1)
                if (i == None):
                    return
                if (self.game.wizard_towers[i].health >= 0):
                    self.game.wizard_towers[i].health = self.game.wizard_towers[i].health - self.power
                    if (self.game.wizard_towers[i].health <= 0):
                        self.game.wizard_towers.pop(i)
                        return
                if (self.game.wizard_towers[i].health < 5 and self.game.wizard_towers[i].health > 2):
                    self.game.wizard_towers[i].color = Back.YELLOW
                if (self.game.wizard_towers[i].health < 2 and self.game.wizard_towers[i].health > 0):
                    self.game.wizard_towers[i].color = Back.RED
            if (self.game.board[self.x][self.y - 1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' W ' + Style.RESET_ALL):
                i = self.game.which_wall(self.x, self.y - 1)
                if (i == None):
                    return
                if (self.game.walls[i].health >= 0):
                    self.game.walls[i].health = self.game.walls[i].health - self.power
                    if (self.game.walls[i].health <= 0):
                        self.game.walls.pop(i)
                        return
                if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
                    self.game.walls[i].color = Back.YELLOW
                if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
                    self.game.walls[i].color = Back.RED
            if (self.game.board[self.x][self.y - 1] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y - 1] == Back.RED + ' T ' + Style.RESET_ALL):
                if (self.game.town_hall.health >= 0):
                    self.game.town_hall.health = self.game.town_hall.health - self.power
                    if (self.game.town_hall.health <= 0):
                        self.game.town_hall.is_dead = True
                if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                    self.game.town_hall.color = Back.YELLOW
                if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                    self.game.town_hall.color = Back.RED

        if (direction == 1):
            if (self.game.board[self.x + 1][self.y] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' H ' + Style.RESET_ALL):
                i = self.game.which_hut(self.x + 1, self.y)
                if (i == None):
                    return
                if (self.game.huts[i].health >= 0):
                    self.game.huts[i].health = self.game.huts[i].health - self.power
                    if (self.game.huts[i].health <= 0):
                        self.game.huts.pop(i)
                        return
                if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
                    self.game.huts[i].color = Back.YELLOW
                if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
                    self.game.huts[i].color = Back.RED
            if (self.game.board[self.x + 1][self.y] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.WHITE + ' C ' + Style.RESET_ALL):
                i = self.game.which_cannon(self.x + 1, self.y)
                if (i == None):
                    return
                if (self.game.cannons[i].health >= 0):
                    self.game.cannons[i].health = self.game.cannons[i].health - self.power
                    if (self.game.cannons[i].health <= 0):
                        self.game.cannons.pop(i)
                        return
                if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                    self.game.cannons[i].color = Back.YELLOW
                if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                    self.game.cannons[i].color = Back.RED
            if (self.game.board[self.x + 1][self.y] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                i = self.game.which_wt(self.x + 1, self.y)
                if (i == None):
                    return
                if (self.game.wizard_towers[i].health >= 0):
                    self.game.wizard_towers[i].health = self.game.wizard_towers[i].health - self.power
                    if (self.game.wizard_towers[i].health <= 0):
                        self.game.wizard_towers.pop(i)
                        return
                if (self.game.wizard_towers[i].health < 5 and self.game.wizard_towers[i].health > 2):
                    self.game.wizard_towers[i].color = Back.YELLOW
                if (self.game.wizard_towers[i].health < 2 and self.game.wizard_towers[i].health > 0):
                    self.game.wizard_towers[i].color = Back.RED
            if (self.game.board[self.x + 1][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
                i = self.game.which_wall(self.x + 1, self.y)
                if (i == None):
                    return
                if (self.game.walls[i].health >= 0):
                    self.game.walls[i].health = self.game.walls[i].health - self.power
                    if (self.game.walls[i].health <= 0):
                        self.game.walls.pop(i)
                        return
                if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
                    self.game.walls[i].color = Back.YELLOW
                if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
                    self.game.walls[i].color = Back.RED
            if (self.game.board[self.x + 1][self.y] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y] == Back.RED + ' T ' + Style.RESET_ALL):
                if (self.game.town_hall.health >= 0):
                    self.game.town_hall.health = self.game.town_hall.health - self.power
                    if (self.game.town_hall.health <= 0):
                        self.game.town_hall.is_dead = True
                if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                    self.game.town_hall.color = Back.YELLOW
                if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                    self.game.town_hall.color = Back.RED

        if (direction == 3):
            if (self.game.board[self.x][self.y + 1] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' H ' + Style.RESET_ALL):
                i = self.game.which_hut(self.x, self.y + 1)
                if (i == None):
                    return
                if (self.game.huts[i].health >= 0):
                    self.game.huts[i].health = self.game.huts[i].health - self.power
                    if (self.game.huts[i].health <= 0):
                        self.game.huts.pop(i)
                        return
                if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
                    self.game.huts[i].color = Back.YELLOW
                if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
                    self.game.huts[i].color = Back.RED
            if (self.game.board[self.x][self.y + 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.WHITE + ' C ' + Style.RESET_ALL):
                i = self.game.which_cannon(self.x, self.y + 1)
                if (i == None):
                    return
                if (self.game.cannons[i].health >= 0):
                    self.game.cannons[i].health = self.game.cannons[i].health - self.power
                    if (self.game.cannons[i].health <= 0):
                        self.game.cannons.pop(i)
                        return
                if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                    self.game.cannons[i].color = Back.YELLOW
                if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                    self.game.cannons[i].color = Back.RED
            if (self.game.board[self.x][self.y + 1] == Back.GREEN + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' 🪄 ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' 🪄 ' + Style.RESET_ALL):
                i = self.game.which_wt(self.x, self.y + 1)
                if (i == None):
                    return
                if (self.game.wizard_towers[i].health >= 0):
                    self.game.wizard_towers[i].health = self.game.wizard_towers[i].health - self.power
                    if (self.game.wizard_towers[i].health <= 0):
                        self.game.wizard_towers.pop(i)
                        return
                if (self.game.wizard_towers[i].health < 5 and self.game.wizard_towers[i].health > 2):
                    self.game.wizard_towers[i].color = Back.YELLOW
                if (self.game.wizard_towers[i].health < 2 and self.game.wizard_towers[i].health > 0):
                    self.game.wizard_towers[i].color = Back.RED
            if (self.game.board[self.x][self.y + 1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' W ' + Style.RESET_ALL):
                i = self.game.which_wall(self.x, self.y + 1)
                if (i == None):
                    return
                if (self.game.walls[i].health >= 0):
                    self.game.walls[i].health = self.game.walls[i].health - self.power
                    if (self.game.walls[i].health <= 0):
                        self.game.walls.pop(i)
                        return
                if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
                    self.game.walls[i].color = Back.YELLOW
                if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
                    self.game.walls[i].color = Back.RED
            if (self.game.board[self.x][self.y + 1] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[self.x][self.y + 1] == Back.RED + ' T ' + Style.RESET_ALL):
                if (self.game.town_hall.health >= 0):
                    self.game.town_hall.health = self.game.town_hall.health - self.power
                    if (self.game.town_hall.health <= 0):
                        self.game.town_hall.is_dead = True
                if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                    self.game.town_hall.color = Back.YELLOW
                if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                    self.game.town_hall.color = Back.RED
