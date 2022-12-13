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

class Building(object):
    def __init__(self, game, x, y, breadth, width):
        self.game = game
        self.x = x
        self.y = y
        self.breadth = breadth
        self.width = width
        self.color = Back.GREEN


class Town_hall(Building):
    def __init__(self, game, x, y, breadth=3, width=4):
        self.health = 20
        self.is_dead = False
        Building.__init__(self, game, x, y, breadth, width)

    def add(self):
        if (self.is_dead == False):
            y = self.y
            w = self.width
            b = self.breadth
            arr = self.game.board
            half_breadth = int(b/2)
            half_width  = int(w/2)
            for i in range(self.x - half_breadth + 1, self.x+half_breadth + 2):
                for j in range(self.y - half_width + 1, self.y+half_width + 1):
                    arr[i][j] = self.color + ' T ' + Style.RESET_ALL
            arr[y][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
            self.game.board = arr


class Huts(Building):
    def __init__(self, game, x, y, breadth=1, width=1):
        self.health = 10
        Building.__init__(self, game, x, y, breadth, width)
    def add(self):
        y = self.y
        w = self.width
        b = self.breadth
        arr = self.game.board
        for i in range(self.x, self.x+b):
            for j in range(self.y, self.y+w):
                arr[i][j] = self.color + ' H ' + Style.RESET_ALL
        arr[y][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
        self.game.board = arr

class Cannons(Building):
    def __init__(self, game, x, y, breadth = 1, width = 1):
        self.health = 9
        self.power = 1
        self.range = 6
        self.attacking = False
        Building.__init__(self, game, x, y, breadth, width)
    def add(self):
        if (self.attacking == True):
            y = self.y
            w = self.width
            b = self.breadth
            arr = self.game.board
            for i in range(self.x, self.x+b):
                for j in range(self.y, self.y+w):
                    arr[i][j] = Back.WHITE + ' C ' + Style.RESET_ALL
            arr[y][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
            self.game.board = arr
        else:
            y = self.y
            w = self.width
            b = self.breadth
            arr = self.game.board
            for i in range(self.x, self.x+b):
                for j in range(self.y, self.y+w):
                    arr[i][j] = self.color + ' C ' + Style.RESET_ALL
            arr[y][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
            self.game.board = arr
    
    def shoot(self, king_or_queen):
        self.attacking = False
        if (king_or_queen == 1):
            if (self.game.king.is_dead == False):
                if ((self.game.king.x - self.x)**2 + (self.game.king.y - self.y)**2 <= (self.range**2)):
                    self.attacking = True
                    if (self.game.king.health >= 0):
                        self.game.king.health = self.game.king.health - self.power
                        if (self.game.king.health <= 0):
                            self.game.king.is_dead = True
                            return
                        if (self.game.king.health < 38 and self.game.king.health > 15):
                            self.game.king.color = Back.YELLOW
                        if (self.game.king.health <= 15 and self.game.king.health > 0):
                            self.game.king.color = Back.RED
                        return
        if (king_or_queen == 2):
            if (self.game.queen.is_dead == False):
                if ((self.game.queen.x - self.x)**2 + (self.game.queen.y - self.y)**2 <= (self.range**2)):
                    self.attacking = True
                    if (self.game.queen.health >= 0):
                        self.game.queen.health = self.game.queen.health - self.power
                        if (self.game.queen.health <= 0):
                            self.game.queen.is_dead = True
                            return
                        if (self.game.queen.health < 38 and self.game.queen.health > 15):
                            self.game.queen.color = Back.YELLOW
                        if (self.game.queen.health <= 15 and self.game.queen.health > 0):
                            self.game.queen.color = Back.RED
                        return
        for barbarian in self.game.barbarians:
            if ((barbarian.x - self.x)**2 + (barbarian.y - self.y)**2 <= (self.range**2)):
                if (self.color == Back.GREEN):
                    self.color = Back.WHITE
                else:
                    self.color = Back.GREEN
                if (barbarian.health >= 0):
                    barbarian.health = barbarian.health - self.power
                    if (barbarian.health <= 0):
                        self.game.barbarians.remove(barbarian)
                        return
                if (barbarian.health < 4 and barbarian.health > 2):
                    barbarian.color = Back.YELLOW
                if (barbarian.health <= 2 and barbarian.health > 0):
                    barbarian.color = Back.RED
                return
        for archer in self.game.archers:
            if ((archer.x - self.x)**2 + (archer.y - self.y)**2 <= (self.range**2)):
                if (self.color == Back.GREEN):
                    self.color = Back.WHITE
                else:
                    self.color = Back.GREEN
                if (archer.health >= 0):
                    archer.health = archer.health - self.power
                    if (archer.health <= 0):
                        self.game.archers.remove(archer)
                        return
                if (archer.health < 4 and archer.health > 2):
                    archer.color = Back.YELLOW
                if (archer.health <= 2 and archer.health > 0):
                    archer.color = Back.RED
                return

class Wizard_Towers(Building):
    def __init__(self, game, x, y, breadth = 1, width = 1):
        self.health = 9
        self.power = 1
        self.range = 6
        self.attacking = False
        Building.__init__(self, game, x, y, breadth, width)
    def add(self):
        y = self.y
        w = self.width
        b = self.breadth
        arr = self.game.board
        for i in range(self.x, self.x+b):
            for j in range(self.y, self.y+w):
                arr[i][j] = self.color + ' 🪄 ' + Style.RESET_ALL
        arr[y][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
        self.game.board = arr
    def shoot(self, x_coord, y_coord, king_or_queen):
        if ((self.x - x_coord)**2 + (self.y - y_coord)**2 > (self.range)**2 + 1):
            return
        else:
            for barbarian in self.game.barbarians:
                if (barbarian.x >= x_coord - 1 and barbarian.x <= x_coord + 1 and barbarian.y >= y_coord - 1 and barbarian.y <= y_coord + 1):
                    if (barbarian.health >= 0):
                        barbarian.health = barbarian.health - self.power
                        if (barbarian.health <= 0):
                            self.game.barbarians.remove(barbarian)
                            continue
                    if (barbarian.health < 4 and barbarian.health > 2):
                        barbarian.color = Back.YELLOW
                    if (barbarian.health <= 2 and barbarian.health > 0):
                        barbarian.color = Back.RED
            for archer in self.game.archers:
                if (archer.x >= x_coord - 1 and archer.x <= x_coord + 1 and archer.y >= y_coord - 1 and archer.y <= y_coord + 1):
                    if (archer.health >= 0):
                        archer.health = archer.health - self.power
                        if (archer.health <= 0):
                            self.game.archers.remove(archer)
                            continue
                    if (archer.health < 3 and archer.health > 2):
                        archer.color = Back.YELLOW
                    if (archer.health <= 2 and archer.health > 0):
                        archer.color = Back.RED
            for balloon in self.game.balloons:
                if (balloon.x >= x_coord - 1 and balloon.x <= x_coord + 1 and balloon.y >= y_coord - 1 and balloon.y <= y_coord + 1):
                    if (balloon.health >= 0):
                        balloon.health = balloon.health - self.power
                        if (balloon.health <= 0):
                            self.game.balloons.remove(balloon)
                            continue
                    if (balloon.health < 4 and balloon.health > 2):
                        balloon.color = Back.YELLOW
                    if (balloon.health <= 2 and balloon.health > 0):
                        balloon.color = Back.RED
            if (king_or_queen == 1):
                if (self.game.king.is_dead == False):
                    if (self.game.king.x >= x_coord - 1 and self.game.king.x <= x_coord + 1 and self.game.king.y >= y_coord - 1 and self.game.king.y <= y_coord + 1):
                        if (self.game.king.health >= 0):
                            self.game.king.health = self.game.king.health - self.power
                            if (self.game.king.health <= 0):
                                self.game.king.is_dead = True
                        if (self.game.king.health < 38 and self.game.king.health > 15):
                            self.game.king.color = Back.YELLOW
                        if (self.game.king.health <= 15 and self.game.king.health > 0):
                            self.game.king.color = Back.RED
            if (king_or_queen == 2):
                if (self.game.queen.is_dead == False):
                    if (self.game.queen.x >= x_coord - 1 and self.game.queen.x <= x_coord + 1 and self.game.queen.y >= y_coord - 1 and self.game.queen.y <= y_coord + 1):
                        if (self.game.queen.health >= 0):
                            self.game.queen.health = self.game.queen.health - self.power
                            if (self.game.queen.health <= 0):
                                self.game.queen.is_dead = True
                        if (self.game.queen.health < 38 and self.game.queen.health > 15):
                            self.game.queen.color = Back.YELLOW
                        if (self.game.queen.health <= 15 and self.game.queen.health > 0):
                            self.game.queen.color = Back.RED
