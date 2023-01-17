import sys, pygame

pygame.init()
size = width, height = 1920, 1080
speed = [2, 2]
white = 1, 1, 1
screen = pygame.display.set_mode(size)
ball = pygame.image.load("img/wazard.png")
ballrect = ball.get_rect()
text = "lol ur gey"
sFont = 32
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((170, 238, 187))
font = pygame.font.Font(None, sFont)
rText = font.render(text, True, (10, 10, 10))
textPos = rText.get_rect(centerx=background.get_width() / 2, y=10)
pygame.draw.rect(screen, "white", [75, 10, 50, 20], 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    font = pygame.font.Font(None, sFont)
    rText = font.render(text, True, (10, 10, 10))
    textPos = rText.get_rect(centerx= (sFont*(len(text) + 2))/2, y = 10)
    pygame.draw.rect(screen, "black", [75, 10, 50, 20], 2)
    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(rText, textPos)
    pygame.display.flip()
    