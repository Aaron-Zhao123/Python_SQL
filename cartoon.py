picture1_filename='parking_taken.jpg'
picture2_filename='parking_empty.jpg'
#declare pic names

import pygame
#use pygame library
import sys
from pygame.locals import *
#use some funcs and varaibals from pygame

#input=raw_input("Enter input:");


pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Repono testing software")

pic1=pygame.image.load(picture1_filename).convert()
pic2=pygame.image.load(picture2_filename).convert()
input=0

while True:
    if input==0:
        screen.blit(pic2,(0,0))
    if input==1:
        screen.blit(pic1,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()





