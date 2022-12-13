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

class Archers:
    def __init__(self, game, x, y, init_time):
        self.game = game
        self.health = 4
        self.x = x
        self.y = y
        self.movement = 1
        self.power = 0.5
        self.range = 8
        self.is_dead = False
        self.color = Back.GREEN
        self.time = init_time
    def spawn(self):
        if (self.is_dead == False):
            arr = self.game.board
            arr[self.x][self.y] = self.color + ' A ' + Style.RESET_ALL
            self.game.board = arr
    def move(self, x_coord, y_coord, curr_time):
        if ((curr_time- self.time) % 1 == 0):
            # if (self.x - 1 >= 0 and self.y -1 >= 0):
            #     if (self.game.board[self.x-1][self.y-1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x-1][self.y-1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x-1][self.y-1] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x - 1, self.y - 1)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            # if (self.x - 1 >= 0):
            #     if(self.game.board[self.x-1][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x-1][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x-1][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x - 1, self.y)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            # if (self.x - 1 >= 0 and self.y + 1 <= 24):
            #     if(self.game.board[self.x-1][self.y+1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x-1][self.y+1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x-1][self.y+1] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x - 1, self.y + 1)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            # if (self.y - 1 >= 0):
            #     if(self.game.board[self.x][self.y-1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y-1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y-1] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x, self.y - 1)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            # if (self.y + 1 <= 24):
            #     if(self.game.board[self.x][self.y+1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y+1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y+1] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x, self.y + 1)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            # if (self.x + 1 <= 24 and self.y - 1 >= 0):
            #     if(self.game.board[self.x+1][self.y-1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x+1][self.y-1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x+1][self.y-1] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x + 1, self.y - 1)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            # if (self.x + 1 <= 24):
            #     if(self.game.board[self.x+1][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x+1][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x+1][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x + 1, self.y)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
                    
            # if (self.x + 1 <= 24 and self.y + 1 <= 24):
            #     if(self.game.board[self.x+1][self.y+1] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x+1][self.y+1] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x+1][self.y+1] == Back.RED + ' W ' + Style.RESET_ALL):
            #         i = self.game.which_wall(self.x + 1, self.y + 1)
            #         if (i == None):
            #             return
            #         if (self.game.walls[i].health >= 0):
            #             self.game.walls[i].health = self.game.walls[i].health - self.power
            #             if (self.game.walls[i].health <= 0):
            #                 self.game.walls.pop(i)
            #                 return
            #         if (self.game.walls[i].health < 5 and self.game.walls[i].health > 2):
            #             self.game.walls[i].color = Back.YELLOW
            #         if (self.game.walls[i].health < 2 and self.game.walls[i].health > 0):
            #             self.game.walls[i].color = Back.RED
            #         return
            if (self.x == x_coord - 1 and self.y == y_coord - 1):
                return
            elif (self.x == x_coord - 1 and self.y == y_coord):
                return
            elif (self.x == x_coord - 1 and self.y == y_coord + 1):
                return
            elif (self.x == x_coord and self.y == y_coord - 1):
                return
            elif (self.x == x_coord and self.y == y_coord + 1):
                return
            elif (self.x == x_coord + 1 and self.y == y_coord - 1):
                return
            elif (self.x == x_coord + 1 and self.y == y_coord):
                return
            elif (self.x == x_coord + 1 and self.y == y_coord + 1):
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
    def attack(self):
        x, y, bldg = self.game.closest_building(self.x, self.y)
        if (x != math.inf and y != math.inf and bldg != " "):
            if (bldg == "H"):
                for hut in self.game.huts:
                    if (hut.x == x and hut.y == y and (hut.x - self.x)**2 + (hut.y - self.y)**2 <= (self.range**2)):
                        if (hut.health >= 0):
                            hut.health = hut.health - self.power
                            if (hut.health <= 0):
                                self.game.huts.remove(hut)
                                return
                        if (hut.health < 5 and hut.health > 2):
                            hut.color = Back.YELLOW
                        if (hut.health <= 2 and hut.health > 0):
                            hut.color = Back.RED
                        return
                # for cannon in self.game.cannons:
                #      if ((cannon.x - self.x)**2 + (cannon.y - self.y)**2 <= (self.range**2)):
                #         if (cannon.health >= 0):
                #             cannon.health = cannon.health - self.power
                #             if (cannon.health <= 0):
                #                 self.game.cannons.remove(cannon)
                #                 return
                #         if (cannon.health < 5 and cannon.health > 2):
                #             cannon.color = Back.YELLOW
                #         if (cannon.health <= 2 and cannon.health > 0):
                #             cannon.color = Back.RED
                #          return
                # if ((self.game.town_hall.x - self.x)**2 + (self.game.town_hall.y - self.y)**2 <= (self.range**2)):
                #     if (self.game.town_hall.health >= 0):
                #         self.game.town_hall.health = self.game.town_hall.health - self.power
                #         if (self.game.town_hall.health <= 0):
                #             self.game.town_hall.is_dead = True
                #             return
                #     if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                #         self.game.town_hall.color = Back.YELLOW
                #     if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
                #         self.game.town_hall.color = Back.RED
                #     return
            if (bldg == "C"):
                for cannon in self.game.cannons:
                    if (cannon.x == x and cannon.y == y and (cannon.x - self.x)**2 + (cannon.y - self.y)**2 <= (self.range**2)):
                        if (cannon.health >= 0):
                            cannon.health = cannon.health - self.power
                            if (cannon.health <= 0):
                                self.game.cannons.remove(cannon)
                                return
                        if (cannon.health < 5 and cannon.health > 2):
                            cannon.color = Back.YELLOW
                        if (cannon.health <= 2 and cannon.health > 0):
                            cannon.color = Back.RED
                        return
            if (bldg == "W"):
                for wt in self.game.wizard_towers:
                    if (wt.x == x and wt.y == y and (wt.x - self.x)**2 + (wt.y - self.y)**2 <= (self.range**2)):
                        if (wt.health >= 0):
                            wt.health = wt.health - self.power
                            if (wt.health <= 0):
                                self.game.wizard_towers.remove(wt)
                                return
                        if (wt.health < 5 and wt.health > 2):
                            wt.color = Back.YELLOW
                        if (wt.health <= 2 and wt.health > 0):
                            wt.color = Back.RED
                        return
                # if ((self.game.town_hall.x - self.x)**2 + (self.game.town_hall.y - self.y)**2 <= (self.range**2)):
                #         if (self.game.town_hall.health >= 0):
                #             self.game.town_hall.health = self.game.town_hall.health - self.power
                #             if (self.game.town_hall.health <= 0):
                #                 self.game.town_hall.is_dead = True
                #                 return
                #         if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
                #             self.game.town_hall.color = Back.YELLOW
                #         if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
                #             self.game.town_hall.color = Back.RED
                #         return
                # for hut in self.game.huts:
                #     if ((hut.x - self.x)**2 + (hut.y - self.y)**2 <= (self.range**2)):
                #         if (hut.health >= 0):
                #             hut.health = hut.health - self.power
                #             if (hut.health <= 0):
                #                 self.game.huts.remove(hut)
                #                 return
                #         if (hut.health < 5 and hut.health > 2):
                #             hut.color = Back.YELLOW
                #         if (hut.health <= 2 and hut.health > 0):
                #             hut.color = Back.RED
                #         return
            if (bldg == "T"):
                if ((self.game.town_hall.x - self.x)**2 + (self.game.town_hall.y - self.y)**2 <= (self.range**2)):
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
                # for cannon in self.game.cannons:
                #     if ((cannon.x - self.x)**2 + (cannon.y - self.y)**2 <= (self.range**2)):
                #         if (cannon.health >= 0):
                #             cannon.health = cannon.health - self.power
                #             if (cannon.health <= 0):
                #                 self.game.cannons.remove(cannon)
                #                 return
                #         if (cannon.health < 5 and cannon.health > 2):
                #             cannon.color = Back.YELLOW
                #         if (cannon.health <= 2 and cannon.health > 0):
                #             cannon.color = Back.RED
                #         return
                # for hut in self.game.huts:
                #     if ((hut.x - self.x)**2 + (hut.y - self.y)**2 <= (self.range**2)):
                #         if (hut.health >= 0):
                #             hut.health = hut.health - self.power
                #             if (hut.health <= 0):
                #                 self.game.huts.remove(hut)
                #                 return
                #         if (hut.health < 5 and hut.health > 2):
                #             hut.color = Back.YELLOW
                #         if (hut.health <= 2 and hut.health > 0):
                #             hut.color = Back.RED
                #         return







    # def move(self, x_coord, y_coord):
    #     #  for i in range (1, self.vel + 1):
    #     #     if (self.x - i < 0 or self.x + i > 24 or self.y - i < 0 or self.y + i > 24):
    #     #         continue
    #     #     else:
    #     #         if (self.game.board[self.x - i][self.y - i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y - i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y - i] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x - i, self.y - i)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #          elif (self.game.board[self.x - i][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #              num = self.game.which_wall(self.x - i, self.y)
    #     #              if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #         elif (self.game.board[self.x - i][self.y + i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y + i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y + i] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x - i, self.y + i)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #         elif (self.game.board[self.x][self.y - i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - i] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x, self.y - i)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #         elif (self.game.board[self.x][self.y + i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + i] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x, self.y + i)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #         elif (self.game.board[self.x + i][self.y - i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y - i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y - i] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x + i, self.y - i)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #         elif (self.game.board[self.x + i][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x + i, self.y)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     #         elif (self.game.board[self.x + i][self.y + i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y + i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y + i] == Back.RED + ' W ' + Style.RESET_ALL):
    #     #             num = self.game.which_wall(self.x + i, self.y + i)
    #     #             if (self.game.walls[num].health >= 0):
    #     #                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #     #                 if (self.game.walls[num].health <= 0):
    #     #                     self.game.walls.remove(self.game.walls[num])
    #     #                     return
    #     #             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #     #                 self.game.walls[num].color = Back.YELLOW
    #     #             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #     #                 self.game.walls[num].color = Back.RED
    #     #             return
    #     for i in range (1, self.vel + 1):
    #         if (self.x == x_coord - i and self.y == y_coord - i):
    #             # self.x = x_coord - 1
    #             # self.y = y_coord - 1
    #             return
    #         elif (self.x == x_coord - i and self.y == y_coord):
    #             # self.x = x_coord - 1
    #             # self.y = y_coord
    #             return
    #         elif (self.x == x_coord - i and self.y == y_coord + i):
    #             # self.x = x_coord - 1
    #             # self.y = y_coord + 1
    #             return
    #         elif (self.x == x_coord and self.y == y_coord - i):
    #             # self.x = x_coord
    #             # self.y = y_coord - 1
    #             return
    #         elif (self.x == x_coord and self.y == y_coord + i):
    #             # self.x = x_coord
    #             # self.y = y_coord + 1
    #             return
    #         elif (self.x == x_coord + i and self.y == y_coord - i):
    #             # self.x = x_coord + 1
    #             # self.y = y_coord - 1
    #             return
    #         elif (self.x == x_coord + i and self.y == y_coord):
    #             # self.x = x_coord + 1
    #             # self.y = y_coord
    #             return
    #         elif (self.x == x_coord + i and self.y == y_coord + i):
    #             # self.x = x_coord + 1
    #             # self.y = y_coord + 1
    #             return
    #     else:
    #         if (self.x == x_coord or self.y == y_coord):
    #             if (self.y == y_coord):
    #                 diff = self.x - x_coord
    #                 if (diff > 1):
    #                     for i in range(1, self.vel + 1):
    #                         if (self.x - i < 0):
    #                             continue
    #                         else:
    #                             if (self.game.board[self.x - i][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
    #                                 num = self.game.which_wall(self.x - i, self.y)
    #                                 if (self.game.walls[num].health >= 0):
    #                                     self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                     if (self.game.walls[num].health <= 0):
    #                                         self.game.walls.remove(self.game.walls[num])
    #                                         return
    #                                 if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                     self.game.walls[num].color = Back.YELLOW
    #                                 if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):
    #                                     self.game.walls[num].color = Back.RED
    #                                 return
    #                     self.x = self.x - self.vel
    #                 else:
    #                     for i in range(1, self.vel + 1):
    #                         if (self.x + i > 24):
    #                             continue
    #                         else:
    #                             if (self.game.board[self.x + i][self.y] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y] == Back.RED + ' W ' + Style.RESET_ALL):
    #                                 num = self.game.which_wall(self.x + i, self.y)
    #                                 if (self.game.walls[num].health >= 0):
    #                                     self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                     if (self.game.walls[num].health <= 0):
    #                                         self.game.walls.remove(self.game.walls[num])
    #                                         return
    #                                 if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                     self.game.walls[num].color = Back.YELLOW
    #                                 if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #                                     self.game.walls[num].color = Back.RED
    #                                 return
    #                     self.x = self.x + self.vel
    #             else:
    #                 diff = self.y - y_coord
    #                 if (diff > 1):
    #                     for i in range(1, self.vel + 1):
    #                         if (self.y - i < 0):
    #                             continue
    #                         else:
    #                             if (self.game.board[self.x][self.y - i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y - i] == Back.RED + ' W ' + Style.RESET_ALL):
    #                                 num = self.game.which_wall(self.x, self.y - i)
    #                                 if (self.game.walls[num].health >= 0):
    #                                     self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                     if (self.game.walls[num].health <= 0):
    #                                         self.game.walls.remove(self.game.walls[num])
    #                                         return
    #                                 if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                     self.game.walls[num].color = Back.YELLOW
    #                                 if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #                                     self.game.walls[num].color = Back.RED
    #                                 return
    #                     self.y = self.y - self.vel
    #                 else:
    #                     for i in range(1, self.vel + 1):
    #                         if (self.y + i > 24):
    #                             continue
    #                         else:
    #                             if (self.game.board[self.x][self.y + i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x][self.y + i] == Back.RED + ' W ' + Style.RESET_ALL):
    #                                 num = self.game.which_wall(self.x, self.y + i)
    #                                 if (self.game.walls[num].health >= 0):
    #                                     self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                     if (self.game.walls[num].health <= 0):
    #                                         self.game.walls.remove(self.game.walls[num])
    #                                         return
    #                                 if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                     self.game.walls[num].color = Back.YELLOW
    #                                 if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #                                     self.game.walls[num].color = Back.RED
    #                                 return
    #                     self.y = self.y + self.vel
    #         else:
    #             x_diff = self.x - x_coord
    #             y_diff = self.y - y_coord
    #             if (x_diff < -1 and y_diff < -1):
    #                 for i in range(1, self.vel + 1):
    #                     if (self.x + i > 24 or self.y + i > 24):
    #                         continue
    #                     else:
    #                         if (self.game.board[self.x + i][self.y + i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y + i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y + i] == Back.RED + ' W ' + Style.RESET_ALL):
    #                             num = self.game.which_wall(self.x + i, self.y + i)
    #                             if (self.game.walls[num].health >= 0):
    #                                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                 if (self.game.walls[num].health <= 0):
    #                                     self.game.walls.remove(self.game.walls[num])
    #                                     return
    #                             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                 self.game.walls[num].color = Back.YELLOW
    #                             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #                                 self.game.walls[num].color = Back.RED
    #                             return
    #                 self.x = self.x + self.vel
    #                 self.y = self.y + self.vel
    #             elif (x_diff > 1 and y_diff < -1):
    #                 for i in range(1, self.vel + 1):
    #                     if (self.x - i < 0 or self.y + i > 24):
    #                         continue
    #                     else:
    #                         if (self.game.board[self.x - i][self.y + i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y + i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y + i] == Back.RED + ' W ' + Style.RESET_ALL):
    #                             num = self.game.which_wall(self.x - i, self.y + i)
    #                             if (self.game.walls[num].health >= 0):
    #                                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                 if (self.game.walls[num].health <= 0):
    #                                     self.game.walls.remove(self.game.walls[num])
    #                                     return
    #                             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                 self.game.walls[num].color = Back.YELLOW
    #                             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #                                 self.game.walls[num].color = Back.RED
    #                             return
    #                 self.x = self.x - self.vel
    #                 self.y = self.y + self.vel
    #             elif (x_diff < -1 and y_diff > 1):
    #                 for i in range(1, self.vel + 1):
    #                     if (self.x + i > 24 or self.y - i < 0):
    #                         continue
    #                     else:
    #                         if (self.game.board[self.x + i][self.y - i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y - i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x + i][self.y - i] == Back.RED + ' W ' + Style.RESET_ALL):
    #                             num = self.game.which_wall(self.x + i, self.y - i)
    #                             if (self.game.walls[num].health >= 0):
    #                                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                 if (self.game.walls[num].health <= 0):
    #                                     self.game.walls.remove(self.game.walls[num])
    #                                     return
    #                             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                 self.game.walls[num].color = Back.YELLOW
    #                             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):
    #                                 self.game.walls[num].color = Back.RED
    #                             return
    #                 self.x = self.x + self.vel
    #                 self.y = self.y - self.vel
    #             else:
    #                 for i in range(1, self.vel + 1):
    #                     if (self.x - i < 0 or self.y - i < 0):
    #                         continue
    #                     else:
    #                         if (self.game.board[self.x - i][self.y - i] == Back.GREEN + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y - i] == Back.YELLOW + ' W ' + Style.RESET_ALL or self.game.board[self.x - i][self.y - i] == Back.RED + ' W ' + Style.RESET_ALL):
    #                             num = self.game.which_wall(self.x - i, self.y - i)
    #                             if (self.game.walls[num].health >= 0):
    #                                 self.game.walls[num].health = self.game.walls[num].health - self.power
    #                                 if (self.game.walls[num].health <= 0):
    #                                     self.game.walls.remove(self.game.walls[num])
    #                                     return
    #                             if (self.game.walls[num].health < 5 and self.game.walls[num].health > 2):
    #                                 self.game.walls[num].color = Back.YELLOW
    #                             if (self.game.walls[num].health <= 2 and self.game.walls[num].health > 0):\
    #                                 self.game.walls[num].color = Back.RED
    #                             return
    #                 self.x = self.x - self.vel
    #                 self.y = self.y - self.vel
    # def attack(self):
    #     # for wall in self.game.walls:
    #     #     if ((wall.x - self.x)**2 + (wall.y - self.y)**2 <= (self.range**2)):
    #     #         if (wall.health >= 0):
    #     #             wall.health = wall.health - self.power
    #     #             if (wall.health <= 0):
    #     #                 self.game.walls.remove(wall)
    #     #                 return
    #     #         if (wall.health < 5 and wall.health > 2):
    #     #             wall.color = Back.YELLOW
    #     #         if (wall.health <= 2 and wall.health > 0):
    #     #             wall.color = Back.RED
    #     #         return

        # x, y, bldg = self.game.closest_building(self.x, self.y)
        # if (x != math.inf and y != math.inf and bldg != " "):
        #     if (bldg == "H"):
        #         for hut in self.game.huts:
        #             if ((hut.x - self.x)**2 + (hut.y - self.y)**2 <= (self.range**2)):
        #                 if (hut.health >= 0):
        #                     hut.health = hut.health - self.power
        #                     if (hut.health <= 0):
        #                         self.game.huts.remove(hut)
        #                         return
        #                 if (hut.health < 5 and hut.health > 2):
        #                     hut.color = Back.YELLOW
        #                 if (hut.health <= 2 and hut.health > 0):
        #                     hut.color = Back.RED
        #                 return
        #         # for cannon in self.game.cannons:
        #         #      if ((cannon.x - self.x)**2 + (cannon.y - self.y)**2 <= (self.range**2)):
        #         #         if (cannon.health >= 0):
        #         #             cannon.health = cannon.health - self.power
        #         #             if (cannon.health <= 0):
        #         #                 self.game.cannons.remove(cannon)
        #         #                 return
        #         #         if (cannon.health < 5 and cannon.health > 2):
        #         #             cannon.color = Back.YELLOW
        #         #         if (cannon.health <= 2 and cannon.health > 0):
        #         #             cannon.color = Back.RED
        #         #          return
        #         # if ((self.game.town_hall.x - self.x)**2 + (self.game.town_hall.y - self.y)**2 <= (self.range**2)):
        #         #     if (self.game.town_hall.health >= 0):
        #         #         self.game.town_hall.health = self.game.town_hall.health - self.power
        #         #         if (self.game.town_hall.health <= 0):
        #         #             self.game.town_hall.is_dead = True
        #         #             return
        #         #     if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
        #         #         self.game.town_hall.color = Back.YELLOW
        #         #     if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
        #         #         self.game.town_hall.color = Back.RED
        #         #     return
        #     if (bldg == "C"):
        #         for cannon in self.game.cannons:
        #             if ((cannon.x - self.x)**2 + (cannon.y - self.y)**2 <= (self.range**2)):
        #                 if (cannon.health >= 0):
        #                     cannon.health = cannon.health - self.power
        #                     if (cannon.health <= 0):
        #                         self.game.cannons.remove(cannon)
        #                         return
        #                 if (cannon.health < 5 and cannon.health > 2):
        #                     cannon.color = Back.YELLOW
        #                 if (cannon.health <= 2 and cannon.health > 0):
        #                     cannon.color = Back.RED
        #                 return
        #         # if ((self.game.town_hall.x - self.x)**2 + (self.game.town_hall.y - self.y)**2 <= (self.range**2)):
        #         #         if (self.game.town_hall.health >= 0):
        #         #             self.game.town_hall.health = self.game.town_hall.health - self.power
        #         #             if (self.game.town_hall.health <= 0):
        #         #                 self.game.town_hall.is_dead = True
        #         #                 return
        #         #         if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
        #         #             self.game.town_hall.color = Back.YELLOW
        #         #         if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
        #         #             self.game.town_hall.color = Back.RED
        #         #         return
        #         # for hut in self.game.huts:
        #         #     if ((hut.x - self.x)**2 + (hut.y - self.y)**2 <= (self.range**2)):
        #         #         if (hut.health >= 0):
        #         #             hut.health = hut.health - self.power
        #         #             if (hut.health <= 0):
        #         #                 self.game.huts.remove(hut)
        #         #                 return
        #         #         if (hut.health < 5 and hut.health > 2):
        #         #             hut.color = Back.YELLOW
        #         #         if (hut.health <= 2 and hut.health > 0):
        #         #             hut.color = Back.RED
        #         #         return
        #     if (bldg == "T"):
        #         if ((self.game.town_hall.x - self.x)**2 + (self.game.town_hall.y - self.y)**2 <= (self.range**2)):
        #                 if (self.game.town_hall.health >= 0):
        #                     self.game.town_hall.health = self.game.town_hall.health - self.power
        #                     if (self.game.town_hall.health <= 0):
        #                         self.game.town_hall.is_dead = True
        #                         return
        #                 if (self.game.town_hall.health < 10 and self.game.town_hall.health > 4):
        #                     self.game.town_hall.color = Back.YELLOW
        #                 if (self.game.town_hall.health <= 4 and self.game.town_hall.health > 0):
        #                     self.game.town_hall.color = Back.RED
        #                 return
        #         # for cannon in self.game.cannons:
        #         #     if ((cannon.x - self.x)**2 + (cannon.y - self.y)**2 <= (self.range**2)):
        #         #         if (cannon.health >= 0):
        #         #             cannon.health = cannon.health - self.power
        #         #             if (cannon.health <= 0):
        #         #                 self.game.cannons.remove(cannon)
        #         #                 return
        #         #         if (cannon.health < 5 and cannon.health > 2):
        #         #             cannon.color = Back.YELLOW
        #         #         if (cannon.health <= 2 and cannon.health > 0):
        #         #             cannon.color = Back.RED
        #         #         return
        #         # for hut in self.game.huts:
        #         #     if ((hut.x - self.x)**2 + (hut.y - self.y)**2 <= (self.range**2)):
        #         #         if (hut.health >= 0):
        #         #             hut.health = hut.health - self.power
        #         #             if (hut.health <= 0):
        #         #                 self.game.huts.remove(hut)
        #         #                 return
        #         #         if (hut.health < 5 and hut.health > 2):
        #         #             hut.color = Back.YELLOW
        #         #         if (hut.health <= 2 and hut.health > 0):
        #         #             hut.color = Back.RED
        #         #         return