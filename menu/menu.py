from pygame.sprite import *
from pygame import*
import pygame



pygame.init()
pygame.display.set_caption("Ludo")
screen = pygame.display.set_mode((1100, 750))


class MainMenu:
    def __init__(self):
        self.image = pygame.image.load("wallpaper.jpg")
        self.image = pygame.transform.scale(self.image, (1100, 750))
        screen.blit(self.image, (0, 0))

    def title(self):
        self.image = pygame.image.load("newtitle.png")
        self.image = pygame.transform.scale(self.image, (850, 250))
        screen.blit(self.image, (350, 0))

    def pawn(self):
        self.image = pygame.image.load("pawn2.png")
        screen.blit(self.image, (0, 0))

    def dice(self):
        self.image = pygame.image.load("dice.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        screen.blit(self.image, (150, 170))

class MainButton(MainMenu):
    def __init__(self):
        super().__init__()

    def start(self):
        self.image = pygame.image.load('start.png')
        screen.blit(self.image, (0, 400))

    def start1(self):
        self.image = pygame.image.load('start.png')
        self.image = pygame.transform.scale(self.image, (410, 210))
        screen.blit(self.image, (0, 375))

    def exit(self):
        self.image = pygame.image.load("exit.png")
        screen.blit(self.image, (0, 550))

    def exit1(self):
        self.image = pygame.image.load("exit.png")
        self.image = pygame.transform.scale(self.image, (570, 260))
        screen.blit(self.image, (0, 525))

menu = MainMenu()
a = MainButton()

while True:
    MainMenu()
    menu.title()
    menu.pawn()
    menu.dice()
    a.start()
    a.exit()
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()

    if mouse_x >= 0 and mouse_x <= 390 and mouse_y >= 400 and mouse_y <= 570:
        a.start1()
        if pressed1 == 1:
            from fproject import fp
            fp.main()

    if mouse_x >= 50 and mouse_x <= 520 and mouse_y >= 550 and mouse_y <= 770:
        a.exit1()
        if pressed1 == 1:
            pygame.quit()
            quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
