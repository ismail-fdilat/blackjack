# coding: utf-8
import pygame

# Intialize the pygame
from cards.project import Deck, Gamer

pygame.init()

black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)
# create the screen
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('arial', 15)
hitTxt = font.render('Hit', 1, black)
standTxt = font.render('Stand', 1, black)
restartTxt = font.render('Restart', 1, black)
#  making a Deck
myDeck = Deck()
myDeck.shuffle()
# create the bank
bank = Gamer("bank")
bank.currentplayer()
bank.draw(myDeck, 2)
print(bank.somme())
bank.hidesecondecarte()
# create the player
bob = Gamer("you")
bob.currentplayer()
bob.draw(myDeck, 2)
bob.showHand()
print(bob.somme())
for c in bob.hand:
    print(c +".png")
police = pygame.font.SysFont("impact", 128)
lost = police.render(bob.name + "  lost", True, (0, 0, 0))
win = police.render(bob.name + "  win", True, (0, 0, 0))
imagebob = []
for i in bob.hand:
    imagebob.append(pygame.image.load(i + ".png").convert_alpha())
imagebank =[]
for i in bank.hand:
    imagebank.append(pygame.image.load(i +".png").convert_alpha())
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((86, 125, 70))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x=100
    for i in imagebank:
        screen.blit(i, (x, 50))
        x+=110
    x=100
    for i in imagebob:
        screen.blit(i, (x, 400))
        x+=110


    pygame.draw.rect(screen,(255,255,0),((550, 550, 75, 25)))
    pygame.draw.rect(screen, (255, 0, 0), ((470, 550, 75, 25)))
    if bank.somme() == 21:
        screen.blit(lost, (200, 300))
    elif bob.somme() == 21:
        screen.blit(win, (200, 300))
    elif bob.lost() == True:
        screen.blit(lost, (200, 300))
    elif bob.somme() < bank.somme():
        screen.blit(lost, (200, 300))
    else:
        screen.blit(win, (200, 300))
    restartB = pygame.draw.rect(screen, (80, 150, 15), (350, 225, 75, 25))
    pygame.display.flip()



