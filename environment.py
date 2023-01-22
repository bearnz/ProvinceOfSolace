"""
Generate 2d environment for main game.

v0.1: Basic 2d skybox and plane 
"""

import pygame as pg
from img import *

COLOURS = {
    "base": (65, 142, 137)
    ,"safe1": (93, 204, 196)
    ,"safe2": (58, 255, 241)
    ,"ending": (58, 255, 70)
    ,"level1": (6, 21, 44)
    ,"level2": (112, 45, 38)
    ,"level3": (112, 21, 11)
    }

class border:
    def __init__(self, screen):
        sDims = list(screen.get_size())
        wallTxtr, wallRect = loadImg('img/wall.tga', 0.25, 0.25)
        imgDims = [wallRect.width, wallRect.height]
        wallRect = moveImgRelCentre(screen, wallTxtr, wallRect, (-sDims[0] + imgDims[0]) / 2, (-sDims[1] + imgDims[1]) / 2)
        imgDims = [wallRect.width, wallRect.height]
        print()
        imgTess = [(sDims[i] // imgDims[i]) + 1 for i in range(len(sDims))]
        for x in range(imgTess[0]):
            tRect = wallRect.copy().move(imgDims[0] * x, 0)
            screen.blit(wallTxtr, tRect)
            tRect = wallRect.copy().move(imgDims[0] * x, sDims[1] - imgDims[1])
            screen.blit(wallTxtr, tRect)
            if x == 0 or x == (imgTess[0] - 2):
                for y in range(1, imgTess[1]):
                    print(x, y)
                    uRect = wallRect.copy().move(imgDims[0] * x, imgDims[1] * y)
                    screen.blit(wallTxtr, uRect)





class draw:
    def __init__(self, screen, pause, gameLevel):
        if pause != 1:
            bkgCol = COLOURS[gameLevel]
            screen.fill(bkgCol)
            border(screen)
        