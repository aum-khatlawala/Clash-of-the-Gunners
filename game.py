from cgi import test
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
import json
from playsound import playsound

from matplotlib.pyplot import bar
from src.input import Get, input_to
from src.king import King
from src.buildings import Building, Town_hall, Huts, Cannons
from src.barbarians import Barbarians
from src.walls import Walls
from src.gameclass import Game
from src.spells import Spells
from src.archers import Archers
from src.balloons import Balloons

blank_board = []
m = 25
n = 25
for i in range(m):
    row = [' X ']*n
    row.append('\n')
    blank_board.append(row)
centerx = 0
centery = 0
if m % 2 == 1:
    centerx = (m-1)/2 - 1
if m % 2 == 0:
    centerx = (m-2)/2 - 1
if n % 2 == 1:
    centery = (n-1)/2 - 1
if n % 2 == 0:
    centery = (n-2)/2 - 1
game = Game(int(centerx), int(centery))
value = True
facing = "d"
for i in range(10, 15):
    game.walls.append(Walls(game, i, 9))
    game.walls.append(Walls(game, i, 14))
for j in range (10, 14):
    game.walls.append(Walls(game, 10, j))
    game.walls.append(Walls(game, 14, j))
replay_dict = {}
timer = 1
total_king_health = game.king.health
total_queen_health = game.queen.health
test_barbarian = Barbarians(game, 24, 0, 0)
total_barbarian_health = test_barbarian.health
choice = int(input("1. King or 2. Archer Queen? "))
if choice == 1:
    replay_dict[0] = "1"
if choice == 2:
    replay_dict[0] = "2"
archer_count = 0
barbarian_count = 0
balloon_count = 0
flag = 0
while (value):
    if (flag == 1):
            if (facing == "w"):
                spell = Spells(game)
                spell.eagle_arrow(2)
                replay_dict[timer] = "e"
            if (facing == "a"):
                spell = Spells(game)
                spell.eagle_arrow(0)
                replay_dict[timer] = "e"
            if (facing == "s"):
                spell = Spells(game)
                spell.eagle_arrow(1)
                replay_dict[timer] = "e"
            if (facing == "d"):
                spell = Spells(game)
                spell.eagle_arrow(3)
                replay_dict[timer] = "e"
            flag = 0
    # if (len(game.barbarians) == 0 and game.king.is_dead == True):
    #     print('\033[1;1H', end="")
    #     print("Game Over. You Lose")
    #     value = False
    # if (len(game.cannons) == 0 and len(game.huts) == 0 and game.town_hall.is_dead == True):
    #     print('\033[1;1H', end="")
    #     print("You Win")
    #     value = False
    key = input_to()
    game.board = copy.deepcopy(blank_board)
    print('\033[1;1H', end="")
    if (choice == 1):
        game.king.spawn()
    if (choice == 2):
        game.queen.spawn()
    game.town_hall.add()
    for wall in game.walls:
        wall.add()
    for hut in game.huts:
        hut.add()
    for barbarian in game.barbarians:
        barbarian.spawn()
        x, y, bldg = game.closest_building(barbarian.x, barbarian.y)
        if (x != math.inf and y != math.inf and bldg != " "):
            barbarian.move_and_attack(x, y, bldg, timer)
    for archer in game.archers:
        archer.spawn()
        x, y, bldg = game.closest_building(archer.x, archer.y)
        if (x != math.inf and y != math.inf and bldg != " "):
            archer.move(x, y, timer)
            archer.attack()
    for balloon in game.balloons:
        balloon.spawn()
        x, y, bldg = game.closest_to_balloon(balloon.x, balloon.y)
        if (x != math.inf and y != math.inf and bldg != " "):
            balloon.move_and_attack(x, y, bldg, timer)
    for cannon in game.cannons:
        cannon.add()
        cannon.shoot(choice)
    for wt in game.wizard_towers:
        wt.add()
        x, y, trooptype = game.closest_troop(wt.x, wt.y, choice)
        if (x != math.inf and y != math.inf and trooptype != " "):
            wt.shoot(x, y, choice)
    if (key == "1"):
        if (barbarian_count < 6):
            game.barbarians.append(Barbarians(game, 24, 0, timer))
            replay_dict[timer] = "1"
            barbarian_count += 1
    if (key == "2"):
        if (barbarian_count < 6):
            game.barbarians.append(Barbarians(game, 0, 24, timer))
            replay_dict[timer] = "2"
            barbarian_count += 1
    if (key == "3"):
        if (barbarian_count < 6):
            game.barbarians.append(Barbarians(game, 24, 24, timer))
            replay_dict[timer] = "3"
            barbarian_count += 1
    if (key == "4"):
        if (archer_count < 6):
            game.archers.append(Archers(game, 24, 0, timer))
            replay_dict[timer] = "4"
            archer_count += 1
    if (key == "5"):
        if (archer_count < 6):
            game.archers.append(Archers(game, 0, 24, timer))
            replay_dict[timer] = "5"
            archer_count += 1
    if (key == "6"):
        if (archer_count < 6):
            game.archers.append(Archers(game, 24, 24, timer))
            replay_dict[timer] = "6"
            archer_count += 1
    if (key == "7"):
        if (balloon_count < 3):
            game.balloons.append(Balloons(game, 24, 0, timer))
            replay_dict[timer] = "7"
            balloon_count += 1
    if (key == "8"):
        if (balloon_count < 3):
            game.balloons.append(Balloons(game, 0, 24, timer))
            replay_dict[timer] = "8"
            balloon_count += 1
    if (key == "9"):
        if (balloon_count < 3):
            game.balloons.append(Balloons(game, 24, 24, timer))
            replay_dict[timer] = "9"
            balloon_count += 1
    if (choice == 1):
        if (key == "a"):
            game.king.move(0)
            facing = "a"
            replay_dict[timer] = "a"
        if (key == "s"):
            game.king.move(1)
            facing = "s"
            replay_dict[timer] = "s"
        if (key == "w"):
            game.king.move(2)
            facing = "w"
            replay_dict[timer] = "w"
        if (key == "d"):
            game.king.move(3)
            facing = "d"
            replay_dict[timer] = "d"
        if (key == "q"):
            value = False
            replay_dict[timer] = "q"
        if (key == " "):
            if (facing == "w"):
                game.king.attack(2)
                replay_dict[timer] = " "
            if (facing == "a"):
                game.king.attack(0)
                replay_dict[timer] = " "
            if (facing == "s"):
                game.king.attack(1)
                replay_dict[timer] = " "
            if (facing == "d"):
                game.king.attack(3)
                replay_dict[timer] = " "
        if (key == "r"):
            spell = Spells(game)
            spell.rage()
            replay_dict[timer] = "r"
        if (key == "h"):
            spell = Spells(game)
            spell.heal(total_king_health, total_barbarian_health)
            replay_dict[timer] = "h"
        if (key == "l"):
            spell = Spells(game)
            spell.leviathan()
            replay_dict[timer] = "l"
    if (choice == 2):
        if (key == "a"):
            game.queen.move(0)
            facing = "a"
            replay_dict[timer] = "a"
        if (key == "s"):
            game.queen.move(1)
            facing = "s"
            replay_dict[timer] = "s"
        if (key == "w"):
            game.queen.move(2)
            facing = "w"
            replay_dict[timer] = "w"
        if (key == "d"):
            game.queen.move(3)
            facing = "d"
            replay_dict[timer] = "d"
        if (key == "q"):
            value = False
            replay_dict[timer] = "q"
        if (key == " "):
            if (facing == "w"):
                game.queen.attack(2)
                replay_dict[timer] = " "
            if (facing == "a"):
                game.queen.attack(0)
                replay_dict[timer] = " "
            if (facing == "s"):
                game.queen.attack(1)
                replay_dict[timer] = " "
            if (facing == "d"):
                game.queen.attack(3)
                replay_dict[timer] = " "
        if (key == "e"):
            flag = 1
            # if (facing == "w"):
            #     spell = Spells(game)
            #     spell.eagle_arrow(2)
            #     replay_dict[timer] = "e"
            # if (facing == "a"):
            #     spell = Spells(game)
            #     spell.eagle_arrow(0)
            #     replay_dict[timer] = "e"
            # if (facing == "s"):
            #     spell = Spells(game)
            #     spell.eagle_arrow(1)
            #     replay_dict[timer] = "e"
            # if (facing == "d"):
            #     spell = Spells(game)
            #     spell.eagle_arrow(3)
            #     replay_dict[timer] = "e"
    game.display()
    # print("\n Time: " + str(int(time.time()-game.time)) + " seconds")
    # print(game.king.health)
    if (choice == 1):
        if (game.king.health >= 0):
            healthbar = "\n King's Health: " + '★'*game.king.health + '☆'*(total_king_health-game.king.health)
            print(healthbar)
            # print(game.king.health)
        else:
            # if all barbarians' health is also 0, print game over
            lifecard = "\n King's Health: " + '☆'*total_king_health
            print(lifecard)
    if (choice == 2):
        if (game.queen.health >= 0):
            healthbar = "\n Queen's Health: " + '★'*game.queen.health + '☆'*(total_queen_health-game.queen.health)
            print(healthbar)
        else:
            # if all barbarians' health is also 0, print game over
            lifecard = "\n Queen's Health: " + '☆'*total_queen_health
            print(lifecard)
    print("\n Press q to quit")
    print("\n")
    # for wall in game.walls:
    #     print(wall.health)
    # for cannon in game.cannons:
    #     print(cannon.health)
    #     print("\n")
    # for i in replay_array:
    #     print(i)
    # print(len(game.barbarians))
    # for i in game.cannons:
    #     print(i.health)
    if (choice == 1):
        if (len(game.barbarians) == 0 and game.king.is_dead == True and len(game.archers) == 0 and len(game.balloons) == 0):
            print(r'''
     _____                        _____                _  __   __            _                    
    |  __ \                      |  _  |              | | \ \ / /           | |                   
    | |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __| |  \ V /___  _   _  | |     ___  ___  ___ 
    | | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |   \ // _ \| | | | | |    / _ \/ __|/ _ \
    | |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |  |_|   | | (_) | |_| | | |___| (_) \__ \  __/
     \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)   \_/\___/ \__,_| \_____/\___/|___/\___|
                                                                                                                                                                                            
            ''')
            playsound("src/sfx-defeat3.mp3")
            value = False
    if (choice == 2):
        if (len(game.barbarians) == 0 and game.queen.is_dead == True and len(game.archers) == 0 and len(game.balloons) == 0):
            print(r'''
     _____                        _____                _  __   __            _                    
    |  __ \                      |  _  |              | | \ \ / /           | |                   
    | |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __| |  \ V /___  _   _  | |     ___  ___  ___ 
    | | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |   \ // _ \| | | | | |    / _ \/ __|/ _ \
    | |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |  |_|   | | (_) | |_| | | |___| (_) \__ \  __/
     \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)   \_/\___/ \__,_| \_____/\___/|___/\___|
                                                                                                                                                                                            
            ''')
            playsound("src/sfx-defeat3.mp3")
            value = False 
    if (len(game.cannons) == 0 and len(game.huts) == 0 and len(game.wizard_towers) == 0 and game.town_hall.is_dead == True):
        if (game.level == 1):
            game.level += 1
            game.level_up(game.level, int(centerx), int(centery))
            archer_count = 0
            barbarian_count = 0
            balloon_count = 0
        elif(game.level == 2):
            game.level += 1
            game.level_up(game.level, int(centerx), int(centery))
            archer_count = 0
            barbarian_count = 0
            balloon_count = 0
        elif(game.level == 3):
            print(r'''
     _____ _____ _  __   __            _    _ _       
    |  __ \  __ \ | \ \ / /           | |  | (_)      
    | |  \/ |  \/ |  \ V /___  _   _  | |  | |_ _ __  
    | | __| | __| |   \ // _ \| | | | | |/\| | | '_ \ 
    | |_\ \ |_\ \_|   | | (_) | |_| | \  /\  / | | | |
    \____/ \____(_)   \_/\___/ \__,_|  \/  \/|_|_| |_|
                                                    
                                                    
            ''')
            playsound("src/sfx-victory6.mp3")
            value = False
    timer = timer + 1
    # print(game.which_hut(3, 20))
    # for hut in game.huts:
    #     print(hut.health)
    # print(game.town_hall.health)
    # for barbarian in game.barbarians:
    #     print(barbarian.health)
with open("replays/replay.txt", "a") as outfile:
    outfile.write(str(replay_dict))
    outfile.write("\n")