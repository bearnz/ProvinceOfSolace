'''
Province of Solace
Developer: Josh Smith
Contact: https://github.com/raebeht

Game engine file built using the pyGame module
TBC
'''
import pygame as pg
import json
import sys
import time


class gameEngine:
    def __init__(self):
        #Environmental Variable Setting and Initialisation
        pg.init()
        pg.version.ver = '0.1'
        configFile = json.load(open('config.json', 'r'))
        screen_width = configFile['pxWidth']
        screen_height = configFile['pxHeight']
        screen_mode = configFile['windowType']
        flags = pg.OPENGL | pg.SHOWN

        #Allocate to Class variables
        self.version = pg.version.ver       
        self.screen = pg.display.set_mode((screen_width, screen_height))
        self.refreshRate = 100



