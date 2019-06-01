# -*- coding: utf-8 -*-
import pygame
 
FPS = 60
xMapGame = 64 # Игровое поле состоит из квадратов 22х14
yMapGame = 100 
xMap = 0
yMap = 0
n = 0

pygame.init()
sc = pygame.display.set_mode((1056, 896))
clock = pygame.time.Clock()
pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896)) 

for yMap in range(14): # Рисуем игровое поле
    
    for xMap in range(22):
        pix = pygame.image.load('Images/weed.jpg')
        pixRect = pix.get_rect(bottomright=(xMapGame, yMapGame))
        sc.blit(pix, pixRect)
        xMapGame += 32

    xMapGame = 64
    yMapGame += 32 # Закончили рисовать
    



pygame.display.update()
 

while True:
 
    
    clock.tick(FPS) 
 
   
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()


 
    
    pygame.display.update()
