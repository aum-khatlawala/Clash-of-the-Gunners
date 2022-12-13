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

class Walls:
    def __init__(self, game, x, y):
        self.game = game
        self.health = 10
        self.x = x
        self.y = y
        self.is_dead = False
        self.color = Back.GREEN
    def add(self):
        if (self.is_dead == False):
            arr = self.game.board
            arr[self.x][self.y] = self.color + ' W ' + Style.RESET_ALL
            self.game.board = arr