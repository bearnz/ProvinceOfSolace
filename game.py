'''
-------------PRIMARY EXECUTABLE-------------
Province of Solace
Version: v0.0 VERY EARLY DEVELOPMENT
Developer: Josh Smith
Contact: https://github.com/raebeht

TODO: EVERYTHING LOL

Currently coding the game engine and
basic menu functionality

This is the primary file to run to launch
the game, the aim of this project is to
teach myself game design, and keep me
busy. There should be no expectations of
quality digging into this source code.
This is my first attempt at making a game.
--------------------------------------------
'''
import pygame as pg
import sys
import engine
import menu
import os
import random

DEBUG = True

def main():
    #Global variables to control core game functionality
    PAUSE = 1
    GAMESPEED = 0
    #Engine init, launch game into main menu
    game = engine.gameEngine()
    pg.display.set_caption("Province of Solace v0.01")
    mainScreen = game.screen
    launching = menu.launchScreen(mainScreen)
    mMenu = menu.mainMenu(mainScreen)
    if DEBUG:
        print("DEBUG MODE ON")
        print("Diagnostic info below")
        print('Video driver: {0}'.format(pg.display.get_driver()))
        print(pg.display.Info())
    while True:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.draw.rect(mainScreen, pg.Color('red'), [100, 100, 100, 100])
            else:
                currentFrame =  pg.display.get_surface()
                #if DEBUG:
                    #os.system('cls')
                    #print(event)
        pg.display.flip()
        
    

if __name__ == "__main__":
    main()