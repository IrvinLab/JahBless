# -*- coding: utf-8 -*-
import pygame, sys, random
import pygame.freetype
import threading

genom = [2,12,9,26,5,7,17,46,54,7,0,26,24,0,17,46,2,7,10,29,9,1,57,46,0,13,46,60,40,5,2,36,1,27,23,26,43,5,17,46,2,7,12,1,42,33,17,46,2,11,42,26,8,43,17,46,54,7,22,26,8,4,17,46]

FPS = 60
xGameMap = 16 
yGameMap = 96 
xMap = 0
yMap = 0
xHeroIcon = 0
yHeroIcon = 0
xMagic = 0
yMagic = 0

# Переменные ботов
bot = 1 # Количество ботов
botNumer = [] # Порядковый номер бота в списке ботов
botType = [] # 1 - союзник, 2 - враждебный, 3 - мирный
botStep = [] # Сколько шагов у бота
botLocation = [] # Локация бота
botMap = [] # Карта на которой
botVariant = [] # Номер/вариант бота. т.е. что это именно за бот эльф 2 уровня или скелет 5 уровня
botAlgoritm = [] # Алгоритм бота 1 - псих, 2 - мирный, 3 - добро, 4 - зло
xBot = []
yBot = []
botExpirience = []
botLvl = []
botRasa = []
botZaklinania = []
botVozdeistvie = []
botInventar = []
botIshZdorovie = []
botZdorovie = []
botMana = []
botIshMana = []
botSila = []
botLovkost = []
botYdacha = []
botZachita = []
botHod = []
botAttack = []
botZoloto = []
botSerebro = []
botBronza = []
botUseWeapon = []
botDeistvie = [] # Сколько времени действует заклинание. Пример: botVozdeistvie[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                 #                                                  botDeistvie[n] = [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

pygame.init()
pygame.font.init()   

sc = pygame.display.set_mode((1056, 896))
pygame.display.set_caption("Kings of New World")
clock = pygame.time.Clock()
pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896)) 
print("SAS")


textNameHero = pygame.font.SysFont('Monospace Regular Bold', 23) # Текст отображающий имя игрока               
healt = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Здоровье
manna = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Ману
textSila = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Силу
textLovk = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Ловкость
textYdacha = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Удачу
textZoloto = pygame.font.SysFont('Monospace Regular', 20)
textSerebro = pygame.font.SysFont('Monospace Regular', 20)
textBronza = pygame.font.SysFont('Monospace Regular', 20)
textDescription = pygame.font.SysFont('Monospace Regular', 20) #Описание объекта
textHod = pygame.font.SysFont('Monospace Regular', 20) # Отображает количество оставшегося хода
textExpirience = pygame.font.SysFont('Monospace Regular', 20) # Отображает опыт
textZachita = pygame.font.SysFont('Monospace Regular', 20)  # Отображаем защиту


# Создаём мир
def worldCreate():
    botNumer.clear()
    botType.clear()
    botStep.clear()
    botVariant.clear()
    botAlgoritm.clear()
    xBot.clear()
    yBot.clear()
    botExpirience.clear()
    botLvl.clear()
    botRasa.clear()
    botZaklinania.clear()
    botVozdeistvie.clear()
    botIshZdorovie.clear()
    botZdorovie.clear()
    botMana.clear()
    botIshMana.clear()
    botSila.clear()
    botLovkost.clear()
    botYdacha.clear()
    botZachita.clear()
    botHod.clear()
    botLocation.clear()
    botZoloto.clear()
    botSerebro.clear()
    botBronza.clear()
    botDeistvie.clear()
    botAttack.clear()
    botUseWeapon.clear()
    n = 0 # Создаём массивы для ботов
    for n in range(1000):
        botZoloto.append(n)
        botSerebro.append(n)
        botBronza.append(n)
        botNumer.append(n)
        botType.append(n)
        botStep.append(n)
        botLocation.append(n)
        botMap.append(n)
        xBot.append(n)
        yBot.append(n)
        botExpirience.append(n)
        botLvl.append(n)
        botRasa.append(n)
        botZaklinania.append(n)
        botVozdeistvie.append(n)
        botInventar.append(n)
        botIshZdorovie.append(n)
        botZdorovie.append(n)
        botMana.append(n)
        botIshMana.append(n)
        botSila.append(n)
        botLovkost.append(n)
        botYdacha.append(n)
        botZachita.append(n)
        botHod.append(n)
        botAlgoritm.append(n)
        botVariant.append(n)
        botDeistvie.append(n)
        botAttack.append(n)
        botUseWeapon.append(n)
        
        botZoloto[n] = 0
        botSerebro[n] = 0
        botBronza[n] = 0
        botNumer[n] = 0
        botType[n] = 0
        botStep[n] = 0
        botLocation[n] = 0
        botMap[n] = 0
        xBot[n] = 0
        yBot[n] = 0
        botExpirience[n] = 0
        botLvl[n] = 0
        botRasa[n] = 0
        botZaklinania[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botVozdeistvie[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[n] = 0
        botZdorovie[n] = 0
        botMana[n] = 0
        botIshMana[n] = 0
        botSila[n] = 0
        botLovkost[n] = 0
        botYdacha[n] = 0
        botZachita[n] = 0
        botHod[n] = 0
        botAlgoritm[n] = 0
        botVariant[n] = 0
        botDeistvie[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botAttack[n] = 0
        botUseWeapon[n] = 0
    n = 0  
for yMap in range(14): # Рисуем игровое поле
    
    for xMap in range(32):
        pix = pygame.image.load('Images/weed.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xGameMap,yGameMap))
        xGameMap += 32

    xGameMap = 16
    yGameMap += 32 # Закончили рисовать
    
xGameMap = 16
yGameMap = 548     
while True:
    clock.tick(FPS) 

    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()    
            
    if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896)) 
                
            