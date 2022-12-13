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
from src.input import Get, input_to
from src.king import King
from src.buildings import Building, Town_hall, Huts, Cannons, Wizard_Towers
from src.barbarians import Barbarians
from src.walls import Walls
from src.spells import Spells
from src.queen import Queen
class Game:
    def __init__(self, center_x, center_y):
        self.run = True
        self.town_hall = Town_hall(self, center_x, center_y)
        self.king = King(self)
        self.queen = Queen(self)
        self.board = []
        self.huts = [Huts(self, 2, 3), Huts(self, 5, 6), Huts(self, 20, 22), Huts(self, 10, 3), Huts(self, 3, 20)]
        self.time = time.time()
        self.barbarians = []
        self.archers = []
        self.balloons = []
        self.walls = []
        # self.total_wts = [Wizard_Towers(self, 24, 22), Wizard_Towers(self, 20, 23), Wizard_Towers(self, 9, 4), Wizard_Towers(self, 24, 3)]
        self.wizard_towers = [Wizard_Towers(self, 24, 22), Wizard_Towers(self, 20, 23)]
        self.level = 1
        # self.total_cannons = [Cannons(self, 12, 8), Cannons(self, 12, 15), Cannons(self, 9, 12), Cannons(self, 15, 12)]
        self.cannons = [Cannons(self, 12, 8), Cannons(self, 12, 15)]
    def level_up(self, level, center_x, center_y):
        # if level == 1:
        #     self.cannons = [Cannons(self, 12, 8), Cannons(self, 12, 15)]
        #     self.wizard_towers = [Wizard_Towers(self, 24, 22), Wizard_Towers(self, 20, 23)]
        if level == 2:
            self.cannons = [Cannons(self, 12, 8), Cannons(self, 12, 15), Cannons(self, 9, 12)]
            self.wizard_towers = [Wizard_Towers(self, 24, 22), Wizard_Towers(self, 20, 23), Wizard_Towers(self, 9, 4)]
            self.balloons = []
            self.archers = []
            self.barbarians = []
            self.huts = [Huts(self, 2, 3), Huts(self, 5, 6), Huts(self, 20, 22), Huts(self, 10, 3), Huts(self, 3, 20)]
            self.town_hall = Town_hall(self, center_x, center_y)
            self.walls = []
            for i in range(10, 15):
                self.walls.append(Walls(self, i, 9))
                self.walls.append(Walls(self, i, 14))
            for j in range (10, 14):
                self.walls.append(Walls(self, 10, j))
                self.walls.append(Walls(self, 14, j))
            self.king.x = 0
            self.king.y = 0
            self.queen.x = 0
            self.queen.y = 0
        elif level == 3:
            self.cannons = [Cannons(self, 12, 8), Cannons(self, 12, 15), Cannons(self, 9, 12), Cannons(self, 15, 12)]
            self.wizard_towers = [Wizard_Towers(self, 24, 22), Wizard_Towers(self, 20, 23), Wizard_Towers(self, 9, 4), Wizard_Towers(self, 24, 3)]
            self.balloons = []
            self.archers = []
            self.barbarians = []
            self.huts = [Huts(self, 2, 3), Huts(self, 5, 6), Huts(self, 20, 22), Huts(self, 10, 3), Huts(self, 3, 20)]
            self.town_hall = Town_hall(self, center_x, center_y)
            self.walls = []
            for i in range(10, 15):
                self.walls.append(Walls(self, i, 9))
                self.walls.append(Walls(self, i, 14))
            for j in range (10, 14):
                self.walls.append(Walls(self, 10, j))
                self.walls.append(Walls(self, 14, j))
            self.king.x = 0
            self.king.y = 0
            self.queen.x = 0
            self.queen.y = 0
    def display(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end='')
    def which_hut(self, x, y):
        i = 0
        for hut in self.huts:
            if (hut.x == x and hut.y == y):
                return i
            i+=1
    def which_wall(self, x, y):
        i = 0
        for wall in self.walls:
            if (wall.x == x and wall.y == y):
                return i
            i+=1
    def which_cannon(self, x, y):
        i = 0
        for cannon in self.cannons:
            if (cannon.x == x and cannon.y == y):
                return i
            i+=1
    def which_wt(self, x, y):
        i = 0
        for wt in self.wizard_towers:
            if (wt.x == x and wt.y == y):
                return i
            i+=1
    def closest_building(self, barbarian_x, barbarian_y):
        bldgtype = " "
        coord_x = math.inf
        coord_y = math.inf
        min_dist = 5000 # arbitrary large number greater than (24**2) + (24**2)
        for hut in self.huts:
            if ((hut.x - barbarian_x)**2 + (hut.y - barbarian_y)**2 < min_dist):
                coord_x = hut.x
                coord_y = hut.y
                min_dist = (hut.x - barbarian_x)**2 + (hut.y - barbarian_y)**2
                bldgtype = "H"
        # for wall in self.walls:
        #     if ((wall.x - barbarian_x)**2 + (wall.y - barbarian_y)**2 < min_dist):
        #         coord_x = wall.x
        #         coord_y = wall.y
        #         min_dist = (wall.x - barbarian_x)**2 + (wall.y - barbarian_y)**2
        for cannon in self.cannons:
            if ((cannon.x - barbarian_x)**2 + (cannon.y - barbarian_y)**2 < min_dist):
                coord_x = cannon.x
                coord_y = cannon.y
                min_dist = (cannon.x - barbarian_x)**2 + (cannon.y - barbarian_y)**2
                bldgtype = "C"
        for wt in self.wizard_towers:
            if ((wt.x - barbarian_x)**2 + (wt.y - barbarian_y)**2 < min_dist):
                coord_x = wt.x
                coord_y = wt.y
                min_dist = (wt.x - barbarian_x)**2 + (wt.y - barbarian_y)**2
                bldgtype = "W"
        if (self.town_hall.is_dead == False):
            y = self.town_hall.y
            w = self.town_hall.width
            b = self.town_hall.breadth
            half_breadth = int(b/2)
            half_width  = int(w/2)
            for i in range(self.town_hall.x - half_breadth + 1, self.town_hall.x+half_breadth + 2):
                for j in range(self.town_hall.y - half_width + 1, self.town_hall.y+half_width + 1):
                    if ((i - barbarian_x)**2 + (j - barbarian_y)**2 < min_dist):
                      coord_x = i
                      coord_y = j
                      min_dist = (i - barbarian_x)**2 + (j - barbarian_y)**2
                      bldgtype = "T"
        return coord_x, coord_y, bldgtype
    def closest_to_balloon(self, balloon_x, balloon_y):
        bldgtype = " "
        coord_x = math.inf
        coord_y = math.inf
        min_dist = 5000 # arbitrary large number greater than (24**2) + (24**2)
        if (len(self.cannons) == 0 and len(self.wizard_towers) == 0):
            for hut in self.huts:
                if ((hut.x - balloon_x)**2 + (hut.y - balloon_y)**2 < min_dist):
                    coord_x = hut.x
                    coord_y = hut.y
                    min_dist = (hut.x - balloon_x)**2 + (hut.y - balloon_y)**2
                    bldgtype = "H"
            # for wall in self.walls:
            #     if ((wall.x - balloon_x)**2 + (wall.y - balloon_y)**2 < min_dist):
            #         coord_x = wall.x
            #         coord_y = wall.y
            #         min_dist = (wall.x - balloon_x)**2 + (wall.y - balloon_y)**2
            if (self.town_hall.is_dead == False):
                y = self.town_hall.y
                w = self.town_hall.width
                b = self.town_hall.breadth
                half_breadth = int(b/2)
                half_width  = int(w/2)
                for i in range(self.town_hall.x - half_breadth + 1, self.town_hall.x+half_breadth + 2):
                    for j in range(self.town_hall.y - half_width + 1, self.town_hall.y+half_width + 1):
                        if ((i - balloon_x)**2 + (j - balloon_y)**2 < min_dist):
                            coord_x = i
                            coord_y = j
                            min_dist = (i - balloon_x)**2 + (j - balloon_y)**2
                            bldgtype = "T"
            return coord_x, coord_y, bldgtype
        else:
            for cannon in self.cannons:
                if ((cannon.x - balloon_x)**2 + (cannon.y - balloon_y)**2 < min_dist):
                    coord_x = cannon.x
                    coord_y = cannon.y
                    min_dist = (cannon.x - balloon_x)**2 + (cannon.y - balloon_y)**2
                    bldgtype = "C"
            for wt in self.wizard_towers:
                if ((wt.x - balloon_x)**2 + (wt.y - balloon_y)**2 < min_dist):
                    coord_x = wt.x
                    coord_y = wt.y
                    min_dist = (wt.x - balloon_x)**2 + (wt.y - balloon_y)**2
                    bldgtype = "W"
            return coord_x, coord_y, bldgtype
    def closest_troop(self, wt_x, wt_y, king_or_queen):
        trooptype = " "
        coord_x = math.inf
        coord_y = math.inf
        min_dist = 5000 # arbitrary large number greater than (24**2) + (24**2)
        for barbarian in self.barbarians:
            if ((barbarian.x - wt_x)**2 + (barbarian.y - wt_y)**2 < min_dist):
                coord_x = barbarian.x
                coord_y = barbarian.y
                min_dist = (barbarian.x - wt_x)**2 + (barbarian.y - wt_y)**2
                trooptype = "B"
        # for wall in self.walls:
        #     if ((wall.x - wt_x)**2 + (wall.y - wt_y)**2 < min_dist):
        #         coord_x = wall.x
        #         coord_y = wall.y
        #         min_dist = (wall.x - wt_x)**2 + (wall.y - wt_y)**2
        for archer in self.archers:
            if ((archer.x - wt_x)**2 + (archer.y - wt_y)**2 < min_dist):
                coord_x = archer.x
                coord_y = archer.y
                min_dist = (archer.x - wt_x)**2 + (archer.y - wt_y)**2
                trooptype = "A"
        for balloon in self.balloons:
            if ((balloon.x - wt_x)**2 + (balloon.y - wt_y)**2 < min_dist):
                coord_x = balloon.x
                coord_y = balloon.y
                min_dist = (balloon.x - wt_x)**2 + (balloon.y - wt_y)**2
                trooptype = "B"
        if (king_or_queen == 1):
            if (self.king.is_dead == False):
                if ((self.king.x - wt_x)**2 + (self.king.y - wt_y)**2 < min_dist):
                    coord_x = self.king.x
                    coord_y = self.king.y
                    min_dist = (self.king.x - wt_x)**2 + (self.king.y - wt_y)**2
                    trooptype = "K"
        if(king_or_queen == 2):
            if (self.queen.is_dead == False):
                if ((self.queen.x - wt_x)**2 + (self.queen.y - wt_y)**2 < min_dist):
                    coord_x = self.queen.x
                    coord_y = self.queen.y
                    min_dist = (self.queen.x - wt_x)**2 + (self.queen.y - wt_y)**2
                    trooptype = "Q"
        return coord_x, coord_y, trooptype