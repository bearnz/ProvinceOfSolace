'''
Menu and element definitions and classes for Province of Solace - v0.1
Developer: Josh Smith
Contact: https://github.com/bearnz

Menus file built using the pyGame module
TBC
'''
import pygame as pg
import engine


def loadImg(path, x=1, y=1):
    '''
    @params:
    path :: string :: image path relative to root folder, drop leading and trailing / chars
    x :: int :: relative width scaling of image
    y :: int :: relative height scaling of image
    '''
    img = pg.image.load(path)
    wTransform = img.get_width() * x
    hTransform = img.get_height() * y
    img = pg.transform.scale(img, (wTransform, hTransform))
    return img, img.get_rect()

def moveImgRelCentre(screen, img, imgRect, x, y):
    '''
    Left = -x | Right = +x
      Up = -y | Down  = +y
    '''
    size = screen.get_size()
    centre = [dim/2 for dim in size]
    imgDim = img.get_width(), img.get_height()
    leftEdge, topEdge = centre[0] - (imgDim[0]/2) + x, centre[1] - (imgDim[1]/2) + y
    outputRect = pg.Rect((leftEdge, topEdge, imgDim[0], imgDim[1]))
    screen.blit(img, outputRect)
    return outputRect


class textBox:
    '''WIP'''
    def __init__(self, text, border, clickable=False):
        sFont = 32
        font = pg.font.Font(None, sFont)
        self.outlineCol = pg.Color('black')
        self.bkgCol = pg.Color('white')
        self.txtCol = pg.Color('black')

        rendText = font.render(text, False, self.txtCol)
        self.textPos = rendText.get_rect(centerx= (sFont*(len(text) + 10))/2, y = rendText.get_height() / 2)
        
        surface = pg.Surface((rendText.get_width() * 2, rendText.get_height() * 2))
        surface.fill(self.outlineCol)
        surface.fill(self.bkgCol, surface.get_rect().inflate(-border, -border))

        self.output = pg.Surface((surface.get_width(), surface.get_height()))
        self.output.blit(surface, (0, 0))
        self.output.blit(rendText, ((surface.get_width() / 2) - (rendText.get_width() / 2), (surface.get_height() / 2) - (rendText.get_height() / 2)))
    
    def updateText(self, newText):
        print("TO IMPLEMENT UPDATE TEXT")

    def updateBkg(self, newColor):
        print("TO IMPLEMENT UPDATE BKG COLOR")

    def updateTextColor(self, newColor):
        print("TO IMPLEMENT UPDATE TEXT COLOR")



class launchScreen:
    def __init__(self, screen):
        '''Currently just a placeholder for future implementation'''
        self.loading = 1

class mainMenu:
    def __init__(self, screen, visible):
        bkgCol = 255, 255, 255, 255 #white
        screen.fill(bkgCol)
        if visible:
            self.buttons = []

            wzImg, wzImgRect = loadImg("img/wazard.png", 0.9, 0.9)
            wzImgRect = moveImgRelCentre(screen, wzImg, wzImgRect, 0, -100)

            playButt = textBox("Play Game", 5, True)
            playButt.textPos = moveImgRelCentre(screen, playButt.output, playButt.textPos, 0, 75)
            self.buttons.append(playButt)

            helpButt = textBox("Help", 5, True)
            helpButt.textPos = moveImgRelCentre(screen, helpButt.output, helpButt.textPos, 0, 125)
            self.buttons.append(helpButt)

            quitButt = textBox("Quit", 5, True)
            quitButt.textPos = moveImgRelCentre(screen, quitButt.output, quitButt.textPos, 0, 175)
            self.buttons.append(quitButt)
        # rectColor = (0.5, 0.1, 0.9)
        # titleElement = pg.Rect(0, 100, 200, 300)
        # pg.draw.rect(screen, rectColor, titleElement)
