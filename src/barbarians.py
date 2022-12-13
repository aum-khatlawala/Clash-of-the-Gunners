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

class Barbarians:
    def __init__(self, game, x, y, init_time):
        self.game = game
        self.health = 7
        self.x = x
        self.y = y
        self.power = 1
        self.movement = 1
        self.is_dead = False
        self.color = Back.GREEN
        self.time = init_time
    def spawn(self):
        if (self.is_dead == False):
            arr = self.game.board
            arr[self.x][self.y] = self.color + ' B ' + Style.RESET_ALL
            self.game.board = arr
    def move_and_attack(self, x_coord, y_coord, btype, curr_time):
        if ((curr_time- self.time) % 2 == 0):
            if (self.x == x_coord - 1 and self.y == y_coord - 1):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord - 1 and self.y == y_coord):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord - 1 and self.y == y_coord + 1):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord and self.y == y_coord - 1):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord and self.y == y_coord + 1):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord + 1 and self.y == y_coord - 1):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord + 1 and self.y == y_coord):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            elif (self.x == x_coord + 1 and self.y == y_coord + 1):
                if btype == "C":
                    i = self.game.which_cannon(x_coord, y_coord)
                    
                    if (i == None):
                        print("none")
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
                    return
                elif btype == "W":
                    i = self.game.which_wt(x_coord, y_coord)
                    if (i == None):
                        print("none")
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
                    i = self.game.which_hut(x_coord, y_coord)
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
                    return
                elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
                    if (self.game.town_hall.health >= 0):
                        self.game.town_hall.health = self.game.town_hall.health - self.power
                        if (self.game.town_hall.health <= 0):
                            self.game.town_hall.is_dead = True
                    if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                        self.game.town_hall.color = Back.YELLOW
                    if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
                        self.game.town_hall.color = Back.RED
                    return
            else:
                if (self.x == x_coord or self.y == y_coord):
                    if (self.y == y_coord):
                        diff = self.x - x_coord
                        if (diff > 0):
                            if (self.game.board[self.x - self.movement][y_coord] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.RED + ' W ' + Style.RESET_ALL):
                                i = self.game.which_wall(self.x - self.movement, y_coord)
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
                                return
                            # elif (self.game.board[self.x - self.movement][y_coord] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.WHITE + ' C ' + Style.RESET_ALL):
                            #     i = self.game.which_cannon(self.x - self.movement, y_coord)
                            #     if (i == None):
                            #         return
                            #     if (self.game.cannons[i].health >= 0):
                            #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
                            #         if (self.game.cannons[i].health <= 0):
                            #             self.game.cannons.pop(i)
                            #             return
                            #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                            #         self.game.cannons[i].color = Back.YELLOW
                            #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                            #         self.game.cannons[i].color = Back.RED
                            else:
                                self.x = self.x - self.movement
                        else:
                            if (self.game.board[self.x + self.movement][y_coord] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.RED + ' W ' + Style.RESET_ALL):
                                i = self.game.which_wall(self.x + self.movement, y_coord)
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
                                return
                            # elif (self.game.board[self.x + self.movement][y_coord] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.WHITE + ' C ' + Style.RESET_ALL):
                            #     i = self.game.which_cannon(self.x + self.movement, y_coord)
                            #     if (i == None):
                            #         return
                            #     if (self.game.cannons[i].health >= 0):
                            #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
                            #         if (self.game.cannons[i].health <= 0):
                            #             self.game.cannons.pop(i)
                            #             return
                            #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                            #         self.game.cannons[i].color = Back.YELLOW
                            #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                            #         self.game.cannons[i].color = Back.RED
                            else:
                                self.x = self.x + self.movement
                    else:
                        diff = self.y - y_coord
                        if (diff > 0):
                            if (self.game.board[x_coord][self.y - self.movement] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.RED + ' W ' + Style.RESET_ALL):
                                i = self.game.which_wall(x_coord, self.y - self.movement)
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
                                return
                            # elif (self.game.board[x_coord][self.y - self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
                            #     i = self.game.which_cannon(x_coord, self.y - self.movement)
                            #     if (i == None):
                            #         return
                            #     if (self.game.cannons[i].health >= 0):
                            #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
                            #         if (self.game.cannons[i].health <= 0):
                            #             self.game.cannons.pop(i)
                            #             return
                            #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                            #         self.game.cannons[i].color = Back.YELLOW
                            #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                            #         self.game.cannons[i].color = Back.RED
                            else:
                                self.y = self.y - self.movement
                        else:
                            if (self.game.board[x_coord][self.y + self.movement] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.RED + ' W ' + Style.RESET_ALL):
                                i = self.game.which_wall(x_coord, self.y + self.movement)
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
                                return
                            # elif (self.game.board[x_coord][self.y + self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
                            #     i = self.game.which_cannon(x_coord, self.y + self.movement)
                            #     if (i == None):
                            #         return
                            #     if (self.game.cannons[i].health >= 0):
                            #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
                            #         if (self.game.cannons[i].health <= 0):
                            #             self.game.cannons.pop(i)
                            #             return
                            #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                            #         self.game.cannons[i].color = Back.YELLOW
                            #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                            #         self.game.cannons[i].color = Back.RED
                            else:
                                self.y = self.y + self.movement
                else:
                    x_diff = self.x - x_coord
                    y_diff = self.y - y_coord
                    if (x_diff < 0 and y_diff < 0):
                        if (self.game.board[self.x + self.movement][self.y + self.movement] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.RED + ' W ' + Style.RESET_ALL):
                            i = self.game.which_wall(self.x + self.movement, self.y + self.movement)
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
                            return
                        # elif (self.game.board[self.x + self.movement][self.y + self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
                        #         i = self.game.which_cannon(self.x + self.movement, self.y + self.movement)
                        #         if (i == None):
                        #             return
                        #         if (self.game.cannons[i].health >= 0):
                        #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
                        #             if (self.game.cannons[i].health <= 0):
                        #                 self.game.cannons.pop(i)
                        #                 return
                        #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                        #             self.game.cannons[i].color = Back.YELLOW
                        #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                        #             self.game.cannons[i].color = Back.RED
                        else:
                            self.x = self.x + self.movement
                            self.y = self.y + self.movement
                    elif (x_diff > 0 and y_diff < 0):
                        if (self.game.board[self.x - self.movement][self.y + self.movement] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y + self.movement] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y + self.movement] == Back.RED + ' W ' + Style.RESET_ALL):
                            i = self.game.which_wall(self.x - self.movement, self.y + self.movement)
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
                            return
                        # elif (self.game.board[self.x - self.movement][self.y + self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y + self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y + self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y + self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
                        #         i = self.game.which_cannon(self.x - self.movement, self.y + self.movement)
                        #         if (i == None):
                        #             return
                        #         if (self.game.cannons[i].health >= 0):
                        #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
                        #             if (self.game.cannons[i].health <= 0):
                        #                 self.game.cannons.pop(i)
                        #                 return
                        #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                        #             self.game.cannons[i].color = Back.YELLOW
                        #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                        #             self.game.cannons[i].color = Back.RED
                        else:
                            self.x = self.x - self.movement
                            self.y = self.y + self.movement
                    elif (x_diff < 0 and y_diff > 0):
                        if (self.game.board[self.x + self.movement][self.y - self.movement] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y - self.movement] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y - self.movement] == Back.RED + ' W ' + Style.RESET_ALL):
                            i = self.game.which_wall(self.x + self.movement, self.y - self.movement)
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
                            return
                        # elif (self.game.board[self.x + self.movement][self.y - self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y - self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y - self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y - self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
                        #         i = self.game.which_cannon(self.x + self.movement, self.y - self.movement)
                        #         if (i == None):
                        #             return
                        #         if (self.game.cannons[i].health >= 0):
                        #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
                        #             if (self.game.cannons[i].health <= 0):
                        #                 self.game.cannons.pop(i)
                        #                 return
                        #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                        #             self.game.cannons[i].color = Back.YELLOW
                        #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                        #             self.game.cannons[i].color = Back.RED
                        else:
                            self.x = self.x + self.movement
                            self.y = self.y - self.movement
                    else:
                        if (self.game.board[self.x - self.movement][self.y - self.movement] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y - self.movement] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y - self.movement] == Back.RED + ' W ' + Style.RESET_ALL):
                            i = self.game.which_wall(self.x - self.movement, self.y - self.movement)
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
                            return
                        # elif (self.game.board[self.x - self.movement][self.y - self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y - self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y - self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][self.y - self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
                        #         i = self.game.which_cannon(self.x - self.movement, self.y - self.movement)
                        #         if (i == None):
                        #             return
                        #         if (self.game.cannons[i].health >= 0):
                        #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
                        #             if (self.game.cannons[i].health <= 0):
                        #                 self.game.cannons.pop(i)
                        #                 return
                        #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
                        #             self.game.cannons[i].color = Back.YELLOW
                        #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
                        #             self.game.cannons[i].color = Back.RED
                        else:
                            self.x = self.x - self.movement
                            self.y = self.y - self.movement

















# from cmath import inf
# from distutils.spawn import spawn
# from lib2to3.pytree import HUGE
# from shutil import which
# import colorama
# from colorama import Fore, Back, Style
# import sys
# import os
# import math
# import time
# import copy
# import time

# class Barbarians:
#     def __init__(self, game, x, y):
#         self.game = game
#         self.health = 7
#         self.x = x
#         self.y = y
#         self.power = 1
#         self.movement = 0.5
#         self.is_dead = False
#         self.color = Back.GREEN
#     def spawn(self):
#         if (self.is_dead == False):
#             arr = self.game.board
#             arr[math.floor(self.x)][math.floor(self.y)] = self.color + ' B ' + Style.RESET_ALL
#             self.game.board = arr
#     def move_and_attack(self, x_coord, y_coord, btype):
#         if (self.x == x_coord - 0.5 and self.y == y_coord - 0.5):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         elif (self.x == x_coord - 0.5 and self.y == y_coord):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         elif (self.x == x_coord - 0.5 and self.y == y_coord + 0.5):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         elif (self.x == x_coord and self.y == y_coord - 0.5):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         elif (self.x == x_coord + 0.5 and self.y == y_coord - 0.5):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         elif (self.x == x_coord + 0.5 and self.y == y_coord):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         elif (self.x == x_coord + 0.5 and self.y == y_coord + 0.5):
#             if btype == "C":
#                 i = self.game.which_cannon(x_coord, y_coord)
                 
#                 if (i == None):
#                     print("none")
#                     return
#                 if (self.game.cannons[i].health >= 0):
#                     self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     if (self.game.cannons[i].health <= 0):
#                         self.game.cannons.pop(i)
#                         return
#                 if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     self.game.cannons[i].color = Back.YELLOW
#                 if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     self.game.cannons[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' H ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' H ' + Style.RESET_ALL):
#                 i = self.game.which_hut(x_coord, y_coord)
#                 if (i == None):
#                     return
#                 if (self.game.huts[i].health >= 0):
#                     self.game.huts[i].health = self.game.huts[i].health - self.power
#                     if (self.game.huts[i].health <= 0):
#                         self.game.huts.pop(i)
#                         return
#                 if (self.game.huts[i].health < 5 and self.game.huts[i].health > 2):
#                     self.game.huts[i].color = Back.YELLOW
#                 if (self.game.huts[i].health < 2 and self.game.huts[i].health > 0):
#                     self.game.huts[i].color = Back.RED
#                 return
#             elif (self.game.board[x_coord][y_coord] == Back.GREEN + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.YELLOW + ' T ' + Style.RESET_ALL or self.game.board[x_coord][y_coord] == Back.RED + ' T ' + Style.RESET_ALL):
#                 if (self.game.town_hall.health >= 0):
#                     self.game.town_hall.health = self.game.town_hall.health - self.power
#                     if (self.game.town_hall.health <= 0):
#                         self.game.town_hall.is_dead = True
#                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
#                     self.game.town_hall.color = Back.YELLOW
#                 if (self.game.town_hall.health < 4 and self.game.town_hall.health > 0):
#                     self.game.town_hall.color = Back.RED
#                 return
#         else:
#             if (self.x == x_coord or self.y == y_coord):
#                 if (self.y == y_coord):
#                     diff = self.x - x_coord
#                     if (diff > 0):
#                         if (self.game.board[math.floor(self.x - self.movement)][y_coord] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[math.floor(self.x - self.movement)][y_coord] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[math.floor(self.x - self.movement)][y_coord] == Back.RED + ' W ' + Style.RESET_ALL):
#                             i = self.game.which_wall(math.floor(self.x - self.movement), y_coord)
#                             if (i == None):
#                                 return
#                             if (self.game.walls[i].health >= 0):
#                                 self.game.walls[i].health = self.game.walls[i].health - self.power
#                                 if (self.game.walls[i].health <= 0):
#                                     self.game.walls.pop(i)
#                                     return
#                             if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                                 self.game.walls[i].color = Back.YELLOW
#                             if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                                 self.game.walls[i].color = Back.RED
#                             return
#                         # elif (self.game.board[self.x - self.movement][y_coord] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - self.movement][y_coord] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                         #     i = self.game.which_cannon(self.x - self.movement, y_coord)
#                         #     if (i == None):
#                         #         return
#                         #     if (self.game.cannons[i].health >= 0):
#                         #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                         #         if (self.game.cannons[i].health <= 0):
#                         #             self.game.cannons.pop(i)
#                         #             return
#                         #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                         #         self.game.cannons[i].color = Back.YELLOW
#                         #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                         #         self.game.cannons[i].color = Back.RED
#                         else:
#                             self.x = self.x - self.movement
#                     else:
#                         if (self.game.board[math.ceil(self.x + self.movement)][y_coord] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[math.ceil(self.x + self.movement)][y_coord] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[math.ceil(self.x + self.movement)][y_coord] == Back.RED + ' W ' + Style.RESET_ALL):
#                             i = self.game.which_wall(math.ceil(self.x + self.movement), y_coord)
#                             if (i == None):
#                                 return
#                             if (self.game.walls[i].health >= 0):
#                                 self.game.walls[i].health = self.game.walls[i].health - self.power
#                                 if (self.game.walls[i].health <= 0):
#                                     self.game.walls.pop(i)
#                                     return
#                             if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                                 self.game.walls[i].color = Back.YELLOW
#                             if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                                 self.game.walls[i].color = Back.RED
#                             return
#                         # elif (self.game.board[self.x + self.movement][y_coord] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][y_coord] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                         #     i = self.game.which_cannon(self.x + self.movement, y_coord)
#                         #     if (i == None):
#                         #         return
#                         #     if (self.game.cannons[i].health >= 0):
#                         #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                         #         if (self.game.cannons[i].health <= 0):
#                         #             self.game.cannons.pop(i)
#                         #             return
#                         #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                         #         self.game.cannons[i].color = Back.YELLOW
#                         #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                         #         self.game.cannons[i].color = Back.RED
#                         else:
#                             self.x = self.x + self.movement
#                 else:
#                     diff = self.y - y_coord
#                     if (diff > 0):
#                         if (self.game.board[x_coord][math.floor(self.y - self.movement)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[x_coord][math.floor(self.y - self.movement)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[x_coord][math.floor(self.y - self.movement)] == Back.RED + ' W ' + Style.RESET_ALL):
#                             i = self.game.which_wall(x_coord, math.floor(self.y - self.movement))
#                             if (i == None):
#                                 return
#                             if (self.game.walls[i].health >= 0):
#                                 self.game.walls[i].health = self.game.walls[i].health - self.power
#                                 if (self.game.walls[i].health <= 0):
#                                     self.game.walls.pop(i)
#                                     return
#                             if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                                 self.game.walls[i].color = Back.YELLOW
#                             if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                                 self.game.walls[i].color = Back.RED
#                             return
#                         # elif (self.game.board[x_coord][self.y - self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y - self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                         #     i = self.game.which_cannon(x_coord, self.y - self.movement)
#                         #     if (i == None):
#                         #         return
#                         #     if (self.game.cannons[i].health >= 0):
#                         #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                         #         if (self.game.cannons[i].health <= 0):
#                         #             self.game.cannons.pop(i)
#                         #             return
#                         #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                         #         self.game.cannons[i].color = Back.YELLOW
#                         #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                         #         self.game.cannons[i].color = Back.RED
#                         else:
#                             self.y = self.y - self.movement
#                     else:
#                         if (self.game.board[x_coord][math.ceil(self.y + self.movement)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[x_coord][math.ceil(self.y + self.movement)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[x_coord][math.ceil(self.y + self.movement)] == Back.RED + ' W ' + Style.RESET_ALL):
#                             i = self.game.which_wall(x_coord, math.ceil(self.y + self.movement))
#                             if (i == None):
#                                 return
#                             if (self.game.walls[i].health >= 0):
#                                 self.game.walls[i].health = self.game.walls[i].health - self.power
#                                 if (self.game.walls[i].health <= 0):
#                                     self.game.walls.pop(i)
#                                     return
#                             if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                                 self.game.walls[i].color = Back.YELLOW
#                             if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                                 self.game.walls[i].color = Back.RED
#                             return
#                         # elif (self.game.board[x_coord][self.y + self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[x_coord][self.y + self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                         #     i = self.game.which_cannon(x_coord, self.y + self.movement)
#                         #     if (i == None):
#                         #         return
#                         #     if (self.game.cannons[i].health >= 0):
#                         #         self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                         #         if (self.game.cannons[i].health <= 0):
#                         #             self.game.cannons.pop(i)
#                         #             return
#                         #     if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                         #         self.game.cannons[i].color = Back.YELLOW
#                         #     if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                         #         self.game.cannons[i].color = Back.RED
#                         else:
#                             self.y = self.y + self.movement
#             else:
#                 x_diff = self.x - x_coord
#                 y_diff = self.y - y_coord
#                 if (x_diff < 0 and y_diff < 0):
#                     if (self.game.board[math.ceil(self.x + self.movement)][math.ceil(self.y + self.movement)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[math.ceil(self.x + self.movement)][math.ceil(self.y + self.movement)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[math.ceil(self.x + self.movement)][math.ceil(self.y + self.movement)] == Back.RED + ' W ' + Style.RESET_ALL):
#                         i = self.game.which_wall(math.ceil(self.x + self.movement), math.ceil(self.y + self.movement))
#                         if (i == None):
#                             return
#                         if (self.game.walls[i].health >= 0):
#                             self.game.walls[i].health = self.game.walls[i].health - self.power
#                             if (self.game.walls[i].health <= 0):
#                                 self.game.walls.pop(i)
#                                 return
#                         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                             self.game.walls[i].color = Back.YELLOW
#                         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                             self.game.walls[i].color = Back.RED
#                         return
#                     # elif (self.game.board[self.x + self.movement][self.y + self.movement] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + self.movement][self.y + self.movement] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                     #         i = self.game.which_cannon(self.x + self.movement, self.y + self.movement)
#                     #         if (i == None):
#                     #             return
#                     #         if (self.game.cannons[i].health >= 0):
#                     #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     #             if (self.game.cannons[i].health <= 0):
#                     #                 self.game.cannons.pop(i)
#                     #                 return
#                     #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     #             self.game.cannons[i].color = Back.YELLOW
#                     #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     #             self.game.cannons[i].color = Back.RED
#                     else:
#                         self.x = self.x + self.movement
#                         self.y = self.y + self.movement
#                 elif (x_diff > 0 and y_diff < 0):
#                     if (self.game.board[math.floor(self.x - self.movement)][math.ceil(self.y + self.movement)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[math.floor(self.x - self.movement)][math.ceil(self.y + self.movement)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[math.floor(self.x - self.movement)][math.ceil(self.y + self.movement)] == Back.RED + ' W ' + Style.RESET_ALL):
#                         i = self.game.which_wall(math.floor(self.x - self.movement), math.ceil(self.y + self.movement))
#                         if (i == None):
#                             return
#                         if (self.game.walls[i].health >= 0):
#                             self.game.walls[i].health = self.game.walls[i].health - self.power
#                             if (self.game.walls[i].health <= 0):
#                                 self.game.walls.pop(i)
#                                 return
#                         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                             self.game.walls[i].color = Back.YELLOW
#                         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                             self.game.walls[i].color = Back.RED
#                         return
#                     # elif (self.game.board[self.x - 1][self.y + 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y + 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y + 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y + 1] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                     #         i = self.game.which_cannon(self.x - 1, self.y + 1)
#                     #         if (i == None):
#                     #             return
#                     #         if (self.game.cannons[i].health >= 0):
#                     #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     #             if (self.game.cannons[i].health <= 0):
#                     #                 self.game.cannons.pop(i)
#                     #                 return
#                     #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     #             self.game.cannons[i].color = Back.YELLOW
#                     #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     #             self.game.cannons[i].color = Back.RED
#                     else:
#                         self.x = self.x - self.movement
#                         self.y = self.y + self.movement
#                 elif (x_diff < 0 and y_diff > 0):
#                     if (self.game.board[math.ceil(self.x + self.movement)][math.floor(self.y - self.movement)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[math.ceil(self.x + self.movement)][math.floor(self.y - self.movement)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[math.ceil(self.x + self.movement)][math.floor(self.y - self.movement)] == Back.RED + ' W ' + Style.RESET_ALL):
#                         i = self.game.which_wall(math.ceil(self.x + self.movement), math.floor(self.y - self.movement))
#                         if (i == None):
#                             return
#                         if (self.game.walls[i].health >= 0):
#                             self.game.walls[i].health = self.game.walls[i].health - self.power
#                             if (self.game.walls[i].health <= 0):
#                                 self.game.walls.pop(i)
#                                 return
#                         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                             self.game.walls[i].color = Back.YELLOW
#                         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                             self.game.walls[i].color = Back.RED
#                         return
#                     # elif (self.game.board[self.x + 1][self.y - 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y - 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y - 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x + 1][self.y - 1] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                     #         i = self.game.which_cannon(self.x + 1, self.y - 1)
#                     #         if (i == None):
#                     #             return
#                     #         if (self.game.cannons[i].health >= 0):
#                     #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     #             if (self.game.cannons[i].health <= 0):
#                     #                 self.game.cannons.pop(i)
#                     #                 return
#                     #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     #             self.game.cannons[i].color = Back.YELLOW
#                     #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     #             self.game.cannons[i].color = Back.RED
#                     else:
#                         self.x = self.x + self.movement
#                         self.y = self.y - self.movement
#                 else:
#                     if (self.game.board[math.floor(self.x - self.movement)][math.floor(self.y - self.movement)] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[math.floor(self.x - self.movement)][math.floor(self.y - self.movement)] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[math.floor(self.x - self.movement)][math.floor(self.y - self.movement)] == Back.RED + ' W ' + Style.RESET_ALL):
#                         i = self.game.which_wall(math.floor(self.x - self.movement), math.floor(self.y - self.movement))
#                         if (i == None):
#                             return
#                         if (self.game.walls[i].health >= 0):
#                             self.game.walls[i].health = self.game.walls[i].health - self.power
#                             if (self.game.walls[i].health <= 0):
#                                 self.game.walls.pop(i)
#                                 return
#                         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
#                             self.game.walls[i].color = Back.YELLOW
#                         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
#                             self.game.walls[i].color = Back.RED
#                         return
#                     # elif (self.game.board[self.x - 1][self.y - 1] == Back.GREEN + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y - 1] == Back.YELLOW + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y - 1] == Back.RED + ' C ' + Style.RESET_ALL or self.game.board[self.x - 1][self.y - 1] == Back.WHITE + ' C ' + Style.RESET_ALL):
#                     #         i = self.game.which_cannon(self.x - 1, self.y - 1)
#                     #         if (i == None):
#                     #             return
#                     #         if (self.game.cannons[i].health >= 0):
#                     #             self.game.cannons[i].health = self.game.cannons[i].health - self.power
#                     #             if (self.game.cannons[i].health <= 0):
#                     #                 self.game.cannons.pop(i)
#                     #                 return
#                     #         if (self.game.cannons[i].health < 5 and self.game.cannons[i].health > 2):
#                     #             self.game.cannons[i].color = Back.YELLOW
#                     #         if (self.game.cannons[i].health < 2 and self.game.cannons[i].health > 0):
#                     #             self.game.cannons[i].color = Back.RED
#                     else:
#                         self.x = self.x - self.movement
#                         self.y = self.y - self.movement
