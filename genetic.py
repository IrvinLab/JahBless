# -*- coding: utf-8 -*-
import pygame, sys, random
import pygame.freetype
import threading
import random

n = 0 
m = 0
myGen = 1

if myGen == 1:
    genom = [25, 46, 52, 36, 39, 18, 57, 18, 54, 63, 54, 35, 24, 39, 43, 30, 40, 14, 47, 49, 14, 58, 4, 5, 48, 5, 6, 24, 24, 36, 2, 19, 41, 3, 6, 61, 56, 62, 54, 62, 18, 26, 45, 39, 9, 8, 31, 36, 34, 4, 31, 12, 2, 20, 3, 62, 5, 15, 55, 26, 21, 63, 60, 31, 3, 32, 34, 61, 22, 39, 8, 23, 5, 41, 28, 8, 6, 31, 3, 30, 1, 51, 42, 40, 29, 36, 16, 47, 2, 21, 20, 33, 56, 2, 43, 0, 38, 24, 33, 20, 39, 60, 4, 8, 1, 1, 13, 48, 55, 47, 25, 31, 34, 59, 33, 46, 41, 59, 24, 3, 17, 37, 30, 35, 19, 43, 40, 39]



elif myGen == 2:
    genom = []
    for n in range(64):
        genom.append(n)
        createGen = int(random.random() * 64)
        genom[n] = createGen

print(genom)


iteration = 1
FPS = 60
xGameMap = 16 
yGameMap = 96 
xMap = 0
yMap = 0
xHeroIcon = 0
yHeroIcon = 0
xMagic = 0
yMagic = 0
world = []
lifeTime = 0 # Здесь измеряем время жизни ботов
sobitie = 0 # Здесь мы отсчитываем ходы ботов для того чтобы вызывать события

# Переменные ботов
bot = 1 # Количество ботов
botNumer = [] # Порядковый номер бота в списке ботов
botType = [] # 1 - союзник, 2 - враждебный, 3 - мирный
botStep = [] # Позиция для выбора поведения согласно геному
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
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto    
    global world, xMap, yMap
    
    xMap = 16 
    yMap = 96 
    n = 0
    for n in range(480): # Забиваем мир нулями
        world.append(n)
        world[n] = 0
        
    n = 0
    for n in range(448):  # рандомно размещаем горы и воду
        tmp = int(random.random()*22)
        if n == 30 or n == 62 or n == 63 or n == 384 or n == 385 or n == 417:
            pass
        else:
            if tmp == 5:
                world[n] = 1
                pix = pygame.image.load('Images/mount.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xMap,yMap))
            elif tmp == 6:
                world[n] = 2
                pix = pygame.image.load('Images/water.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xMap,yMap)) 
        xMap += 32    
        if xMap >= 1040:
            xMap = 16
            yMap += 32  
    
    world[145] = 8  # А затем расставляем объекты
    world[298] = 5
    world[416] = 10
    world[31] = 15        
    
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
    worldUpdate()    
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

def markLocation(numberMark, iconka): # Определяем кординаты пиктограммы 32х32
    if numberMark <= 31 and numberMark >= 0: yMap = 96; xMap = 16 + (32*numberMark)
    if numberMark <= 63 and numberMark >= 32: yMap = 128; xMap = 16 + (32*(numberMark-32)) 
    if numberMark <= 95 and numberMark >= 64: yMap = 160; xMap = 16 + (32*(numberMark-64))
    if numberMark <= 127 and numberMark >= 96: yMap = 192; xMap = 16 + (32*(numberMark-96))
    if numberMark <= 159 and numberMark >= 128: yMap = 224; xMap = 16 + (32*(numberMark-128))   
    if numberMark <= 191 and numberMark >= 160: yMap = 256; xMap = 16 + (32*(numberMark-160)) 
    if numberMark <= 223 and numberMark >= 192: yMap = 288; xMap = 16 + (32*(numberMark-192)) 
    if numberMark <= 255 and numberMark >= 224: yMap = 320; xMap = 16 + (32*(numberMark-224)) 
    if numberMark <= 287 and numberMark >= 256: yMap = 352; xMap = 16 + (32*(numberMark-256)) 
    if numberMark <= 319 and numberMark >= 288: yMap = 384; xMap = 16 + (32*(numberMark-288)) 
    if numberMark <= 351 and numberMark >= 320: yMap = 416; xMap = 16 + (32*(numberMark-320)) 
    if numberMark <= 383 and numberMark >= 352: yMap = 448; xMap = 16 + (32*(numberMark-352)) 
    if numberMark <= 415 and numberMark >= 384: yMap = 480; xMap = 16 + (32*(numberMark-384)) 
    if numberMark <= 447 and numberMark >= 416: yMap = 512; xMap = 16 + (32*(numberMark-416))                         
                     
    if iconka == 0: pix = pygame.image.load('Images/weed.jpg'); x_len = pix.get_width(); y_len = pix.get_height();sc.blit(pix, (xMap,yMap))
    if iconka == 1: pix = pygame.image.load('Images/mount.jpg'); x_len = pix.get_width(); y_len = pix.get_height();sc.blit(pix, (xMap,yMap))
    if iconka == 2: pix = pygame.image.load('Images/water.jpg'); x_len = pix.get_width(); y_len = pix.get_height();sc.blit(pix, (xMap,yMap))
    if iconka == 3: pix = pygame.image.load('Images/jilZelievara_32.png'); x_len = pix.get_width(); y_len = pix.get_height();sc.blit(pix, (xMap,yMap))               
    if iconka == 4: pix = pygame.image.load('Images/lachugaShamana_32.png'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 5: pix = pygame.image.load('Images/hijinaMaga_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
    if iconka == 6: pix = pygame.image.load('Images/kuznica_32.png'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
    if iconka == 8: pix = pygame.image.load('Images/market_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))      
    if iconka == 10: pix = pygame.image.load('Images/portal_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 14: pix = pygame.image.load('Images/sunduk_32.png'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))       
    if iconka == 15: pix = pygame.image.load('Images/city_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))   
    if iconka == 16: pix = pygame.image.load('Images/taverna_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))     
    if iconka == 17: pix = pygame.image.load('Images/portal_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))   
    if iconka == 50: pix = pygame.image.load('Images/akami_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 51: pix = pygame.image.load('Images/artes_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
    if iconka == 52: pix = pygame.image.load('Images/deathOwner_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 53: pix = pygame.image.load('Images/deterok_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 54: pix = pygame.image.load('Images/djepotai_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 55: pix = pygame.image.load('Images/farion_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 56: pix = pygame.image.load('Images/garitos_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 57: pix = pygame.image.load('Images/gendalf_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 58: pix = pygame.image.load('Images/illidan_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 59: pix = pygame.image.load('Images/jaina_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 60: pix = pygame.image.load('Images/kell_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 61: pix = pygame.image.load('Images/kelTuZed_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
    if iconka == 62: pix = pygame.image.load('Images/magerion_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 63: pix = pygame.image.load('Images/mefistofor_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))   
    if iconka == 64: pix = pygame.image.load('Images/paladin_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))         
    if iconka == 65: pix = pygame.image.load('Images/pradmur_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 66: pix = pygame.image.load('Images/sargaras_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 67: pix = pygame.image.load('Images/sauron_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 68: pix = pygame.image.load('Images/silvana_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
    if iconka == 69: pix = pygame.image.load('Images/trall_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 70: pix = pygame.image.load('Images/uter_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 71: pix = pygame.image.load('Images/varomir_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))   
    if iconka == 72: pix = pygame.image.load('Images/vulDjin_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 73: pix = pygame.image.load('Images/zadira_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 100: pix = pygame.image.load('Images/elf1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 101: pix = pygame.image.load('Images/elf2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 102: pix = pygame.image.load('Images/elf3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 103: pix = pygame.image.load('Images/gnoll1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 104: pix = pygame.image.load('Images/gnoll2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 105: pix = pygame.image.load('Images/gnoll3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 106: pix = pygame.image.load('Images/gnom1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 107: pix = pygame.image.load('Images/gnom2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 108: pix = pygame.image.load('Images/gnom3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 109: pix = pygame.image.load('Images/gnom4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 110: pix = pygame.image.load('Images/goblin_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 111: pix = pygame.image.load('Images/goblin1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 112: pix = pygame.image.load('Images/goblin2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 113: pix = pygame.image.load('Images/goblin3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 114: pix = pygame.image.load('Images/hermit1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 115: pix = pygame.image.load('Images/hermit2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 116: pix = pygame.image.load('Images/hermit3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 117: pix = pygame.image.load('Images/headHunter_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 118: pix = pygame.image.load('Images/human_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 119: pix = pygame.image.load('Images/monster1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 120: pix = pygame.image.load('Images/monster2_32.png'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 121: pix = pygame.image.load('Images/monster3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 122: pix = pygame.image.load('Images/monster4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 123: pix = pygame.image.load('Images/morlok1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 124: pix = pygame.image.load('Images/morlok2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 125: pix = pygame.image.load('Images/morlok3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 126: pix = pygame.image.load('Images/naemnik1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 127: pix = pygame.image.load('Images/naemnik2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 128: pix = pygame.image.load('Images/naemnik3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 129: pix = pygame.image.load('Images/naemnik4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 130: pix = pygame.image.load('Images/nekromant_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 131: pix = pygame.image.load('Images/nepobedimii_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 132: pix = pygame.image.load('Images/nepobedimii1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 133: pix = pygame.image.load('Images/ogr1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 134: pix = pygame.image.load('Images/ogr2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 135: pix = pygame.image.load('Images/okylt_32.png'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 136: pix = pygame.image.load('Images/ork1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 137: pix = pygame.image.load('Images/ork2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 138: pix = pygame.image.load('Images/ork3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 139: pix = pygame.image.load('Images/ork4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 140: pix = pygame.image.load('Images/ork5_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 141: pix = pygame.image.load('Images/ork6_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 142: pix = pygame.image.load('Images/ork7_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 143: pix = pygame.image.load('Images/ork-shaman_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 144: pix = pygame.image.load('Images/otstupnik_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 145: pix = pygame.image.load('Images/razboinik_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 146: pix = pygame.image.load('Images/grabitel_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 147: pix = pygame.image.load('Images/redFireHolem_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 148: pix = pygame.image.load('Images/skelet1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 149: pix = pygame.image.load('Images/skelet2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 150: pix = pygame.image.load('Images/skelet3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 151: pix = pygame.image.load('Images/skelet4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 152: pix = pygame.image.load('Images/skelet5_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 153: pix = pygame.image.load('Images/skelet6_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 154: pix = pygame.image.load('Images/skelet7_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 155: pix = pygame.image.load('Images/skelet8_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 156: pix = pygame.image.load('Images/soulCatcher_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 157: pix = pygame.image.load('Images/strannik_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 158: pix = pygame.image.load('Images/troll1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 159: pix = pygame.image.load('Images/troll2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 160: pix = pygame.image.load('Images/troll3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 161: pix = pygame.image.load('Images/troll4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 162: pix = pygame.image.load('Images/troll5_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 163: pix = pygame.image.load('Images/troll6_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 164: pix = pygame.image.load('Images/vampir_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 165: pix = pygame.image.load('Images/wizard_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 166: pix = pygame.image.load('Images/womanElf1_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 167: pix = pygame.image.load('Images/womanElf2_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 168: pix = pygame.image.load('Images/womanElf3_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 169: pix = pygame.image.load('Images/womanElf4_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 170: pix = pygame.image.load('Images/womanElf5_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))  
    if iconka == 171: pix = pygame.image.load('Images/womanElf6_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
    if iconka == 172: pix = pygame.image.load('Images/womanElf7_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))     
    #pygame.display.update()   

def worldUpdate():   # Отправляем данные об объекте
    n = 0
    for n in range(448):
        if world[n] == 0: markLocation(n, world[n])
        if world[n] == 1: markLocation(n, world[n])
        if world[n] == 2: markLocation(n, world[n])
        if world[n] == 3: markLocation(n, world[n])
        if world[n] == 4: markLocation(n, world[n])   
        if world[n] == 5: markLocation(n, world[n])
        if world[n] == 6: markLocation(n, world[n])
        if world[n] == 7: markLocation(n, world[n])              
        if world[n] == 8: markLocation(n, world[n]) 
        if world[n] == 9: markLocation(n, world[n])
        if world[n] == 10: markLocation(n, world[n])   
        if world[n] == 11: markLocation(n, world[n])
        if world[n] == 12: markLocation(n, world[n])
        if world[n] == 13: markLocation(n, world[n])              
        if world[n] == 14: markLocation(n, world[n]) 
        if world[n] == 15: markLocation(n, world[n])
        if world[n] == 16: markLocation(n, world[n])   
        if world[n] == 17: markLocation(n, world[n])
        if world[n] == 18: markLocation(n, world[n])
        if world[n] == 19: markLocation(n, world[n])              
        if world[n] == 20: markLocation(n, world[n]) 
        if world[n] == 21: markLocation(n, world[n])
        if world[n] == 22: markLocation(n, world[n])   
        if world[n] == 23: markLocation(n, world[n])
        if world[n] == 24: markLocation(n, world[n])
        if world[n] == 25: markLocation(n, world[n])              
        if world[n] == 26: markLocation(n, world[n])
        if world[n] == 27: markLocation(n, world[n])
        if world[n] == 28: markLocation(n, world[n])   
        if world[n] == 29: markLocation(n, world[n])
        if world[n] == 30: markLocation(n, world[n])
        if world[n] == 31: markLocation(n, world[n])              
        if world[n] == 32: markLocation(n, world[n]) 
        if world[n] == 33: markLocation(n, world[n])
        if world[n] == 34: markLocation(n, world[n])   
        if world[n] == 35: markLocation(n, world[n])
        if world[n] == 36: markLocation(n, world[n])
        if world[n] == 37: markLocation(n, world[n])              
        if world[n] == 38: markLocation(n, world[n]) 
        if world[n] == 39: markLocation(n, world[n])
        if world[n] == 40: markLocation(n, world[n])   
        if world[n] == 41: markLocation(n, world[n])
        if world[n] == 42: markLocation(n, world[n])
        if world[n] == 43: markLocation(n, world[n])              
        if world[n] == 44: markLocation(n, world[n]) 
        if world[n] == 45: markLocation(n, world[n])
        if world[n] == 46: markLocation(n, world[n])   
        if world[n] == 47: markLocation(n, world[n])
        if world[n] == 48: markLocation(n, world[n])
        if world[n] == 49: markLocation(n, world[n])              
        if world[n] == 50: markLocation(n, world[n])
        if world[n] == 51: markLocation(n, world[n])
        if world[n] == 52: markLocation(n, world[n])   
        if world[n] == 53: markLocation(n, world[n])
        if world[n] == 54: markLocation(n, world[n])
        if world[n] == 55: markLocation(n, world[n])              
        if world[n] == 56: markLocation(n, world[n]) 
        if world[n] == 57: markLocation(n, world[n])
        if world[n] == 58: markLocation(n, world[n])   
        if world[n] == 59: markLocation(n, world[n])
        if world[n] == 60: markLocation(n, world[n])
        if world[n] == 61: markLocation(n, world[n])              
        if world[n] == 62: markLocation(n, world[n]) 
        if world[n] == 63: markLocation(n, world[n])
        if world[n] == 64: markLocation(n, world[n])   
        if world[n] == 65: markLocation(n, world[n])
        if world[n] == 66: markLocation(n, world[n])
        if world[n] == 67: markLocation(n, world[n])              
        if world[n] == 68: markLocation(n, world[n]) 
        if world[n] == 69: markLocation(n, world[n])
        if world[n] == 70: markLocation(n, world[n])   
        if world[n] == 71: markLocation(n, world[n])
        if world[n] == 72: markLocation(n, world[n])
        if world[n] == 73: markLocation(n, world[n])              
        if world[n] == 74: markLocation(n, world[n])   
        if world[n] == 75: markLocation(n, world[n])   
        if world[n] == 76: markLocation(n, world[n])
        if world[n] == 77: markLocation(n, world[n])
        if world[n] == 78: markLocation(n, world[n])              
        if world[n] == 79: markLocation(n, world[n]) 
        if world[n] == 80: markLocation(n, world[n])
        if world[n] == 81: markLocation(n, world[n])   
        if world[n] == 82: markLocation(n, world[n])
        if world[n] == 83: markLocation(n, world[n])
        if world[n] == 84: markLocation(n, world[n])              
        if world[n] == 85: markLocation(n, world[n]) 
        if world[n] == 86: markLocation(n, world[n])
        if world[n] == 87: markLocation(n, world[n])   
        if world[n] == 88: markLocation(n, world[n])
        if world[n] == 89: markLocation(n, world[n])
        if world[n] == 90: markLocation(n, world[n])              
        if world[n] == 91: markLocation(n, world[n])
        if world[n] == 92: markLocation(n, world[n])
        if world[n] == 93: markLocation(n, world[n])   
        if world[n] == 94: markLocation(n, world[n])
        if world[n] == 95: markLocation(n, world[n])
        if world[n] == 96: markLocation(n, world[n])              
        if world[n] == 97: markLocation(n, world[n]) 
        if world[n] == 98: markLocation(n, world[n])
        if world[n] == 99: markLocation(n, world[n])   
        if world[n] == 100: markLocation(n, world[n])
        if world[n] == 101: markLocation(n, world[n])
        if world[n] == 102: markLocation(n, world[n])              
        if world[n] == 103: markLocation(n, world[n]) 
        if world[n] == 104: markLocation(n, world[n])
        if world[n] == 105: markLocation(n, world[n])   
        if world[n] == 106: markLocation(n, world[n])
        if world[n] == 107: markLocation(n, world[n])
        if world[n] == 108: markLocation(n, world[n])              
        if world[n] == 109: markLocation(n, world[n]) 
        if world[n] == 110: markLocation(n, world[n])
        if world[n] == 111: markLocation(n, world[n])   
        if world[n] == 112: markLocation(n, world[n])
        if world[n] == 113: markLocation(n, world[n])
        if world[n] == 114: markLocation(n, world[n])              
        if world[n] == 115: markLocation(n, world[n])
        if world[n] == 116: markLocation(n, world[n])
        if world[n] == 117: markLocation(n, world[n])   
        if world[n] == 118: markLocation(n, world[n])
        if world[n] == 119: markLocation(n, world[n])
        if world[n] == 120: markLocation(n, world[n])              
        if world[n] == 121: markLocation(n, world[n]) 
        if world[n] == 122: markLocation(n, world[n])
        if world[n] == 123: markLocation(n, world[n])   
        if world[n] == 124: markLocation(n, world[n])
        if world[n] == 125: markLocation(n, world[n])
        if world[n] == 126: markLocation(n, world[n])              
        if world[n] == 127: markLocation(n, world[n]) 
        if world[n] == 128: markLocation(n, world[n])
        if world[n] == 129: markLocation(n, world[n])   
        if world[n] == 130: markLocation(n, world[n])
        if world[n] == 131: markLocation(n, world[n])
        if world[n] == 132: markLocation(n, world[n])              
        if world[n] == 133: markLocation(n, world[n]) 
        if world[n] == 134: markLocation(n, world[n])
        if world[n] == 135: markLocation(n, world[n])   
        if world[n] == 136: markLocation(n, world[n])
        if world[n] == 137: markLocation(n, world[n])
        if world[n] == 138: markLocation(n, world[n])              
        if world[n] == 139: markLocation(n, world[n])
        if world[n] == 140: markLocation(n, world[n])
        if world[n] == 141: markLocation(n, world[n])
        if world[n] == 142: markLocation(n, world[n])              
        if world[n] == 143: markLocation(n, world[n]) 
        if world[n] == 144: markLocation(n, world[n])
        if world[n] == 145: markLocation(n, world[n])   
        if world[n] == 146: markLocation(n, world[n])
        if world[n] == 147: markLocation(n, world[n])
        if world[n] == 148: markLocation(n, world[n])              
        if world[n] == 149: markLocation(n, world[n]) 
        if world[n] == 150: markLocation(n, world[n])
        if world[n] == 151: markLocation(n, world[n])   
        if world[n] == 152: markLocation(n, world[n])
        if world[n] == 153: markLocation(n, world[n])
        if world[n] == 154: markLocation(n, world[n])              
        if world[n] == 155: markLocation(n, world[n])
        if world[n] == 156: markLocation(n, world[n])
        if world[n] == 157: markLocation(n, world[n])   
        if world[n] == 158: markLocation(n, world[n])
        if world[n] == 159: markLocation(n, world[n])
        if world[n] == 160: markLocation(n, world[n])              
        if world[n] == 161: markLocation(n, world[n]) 
        if world[n] == 162: markLocation(n, world[n])
        if world[n] == 163: markLocation(n, world[n])   
        if world[n] == 164: markLocation(n, world[n])
        if world[n] == 165: markLocation(n, world[n])
        if world[n] == 166: markLocation(n, world[n])              
        if world[n] == 167: markLocation(n, world[n]) 
        if world[n] == 168: markLocation(n, world[n])
        if world[n] == 169: markLocation(n, world[n])   
        if world[n] == 170: markLocation(n, world[n])
        if world[n] == 171: markLocation(n, world[n])
        if world[n] == 172: markLocation(n, world[n])              
        if world[n] == 173: markLocation(n, world[n]) 
        if world[n] == 174: markLocation(n, world[n])
        if world[n] == 175: markLocation(n, world[n])   
        if world[n] == 176: markLocation(n, world[n])
        if world[n] == 177: markLocation(n, world[n])
        if world[n] == 178: markLocation(n, world[n])              
        if world[n] == 179: markLocation(n, world[n])
        if world[n] == 180: markLocation(n, world[n])
        if world[n] == 181: markLocation(n, world[n])
        if world[n] == 182: markLocation(n, world[n])              
        if world[n] == 183: markLocation(n, world[n]) 
        if world[n] == 184: markLocation(n, world[n])
        if world[n] == 185: markLocation(n, world[n])   
        if world[n] == 186: markLocation(n, world[n])
        if world[n] == 187: markLocation(n, world[n])
        if world[n] == 188: markLocation(n, world[n])              
        if world[n] == 189: markLocation(n, world[n]) 
        if world[n] == 190: markLocation(n, world[n])
        if world[n] == 191: markLocation(n, world[n])   
        if world[n] == 192: markLocation(n, world[n])
        if world[n] == 193: markLocation(n, world[n])
        if world[n] == 194: markLocation(n, world[n])              
        if world[n] == 195: markLocation(n, world[n])
        if world[n] == 196: markLocation(n, world[n])
        if world[n] == 197: markLocation(n, world[n])   
        if world[n] == 198: markLocation(n, world[n])
        if world[n] == 199: markLocation(n, world[n])
        if world[n] == 200: markLocation(n, world[n])              
        if world[n] == 201: markLocation(n, world[n]) 
        if world[n] == 202: markLocation(n, world[n])
        if world[n] == 203: markLocation(n, world[n])   
        if world[n] == 204: markLocation(n, world[n])
        if world[n] == 205: markLocation(n, world[n])
        if world[n] == 206: markLocation(n, world[n])              
        if world[n] == 207: markLocation(n, world[n]) 
        if world[n] == 208: markLocation(n, world[n])
        if world[n] == 209: markLocation(n, world[n])   
        if world[n] == 200: markLocation(n, world[n])
        if world[n] == 201: markLocation(n, world[n])
        if world[n] == 202: markLocation(n, world[n])              
        if world[n] == 203: markLocation(n, world[n]) 
        if world[n] == 204: markLocation(n, world[n])
        if world[n] == 205: markLocation(n, world[n])   
        if world[n] == 206: markLocation(n, world[n])
        if world[n] == 207: markLocation(n, world[n])
        if world[n] == 208: markLocation(n, world[n])              
        if world[n] == 209: markLocation(n, world[n])         

def ubiraemTrup(trup):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto    
    
    if xBot[trup] != 0 and yBot[trup] != 0:
        pix = pygame.image.load('Images/weed.jpg'); x_len = pix.get_width(); y_len = pix.get_height();sc.blit(pix, (xBot[trup],yBot[trup]))
    botType[trup] = 0
    botStep[trup] = 0
    xBot[trup] = 0
    yBot[trup] = 0
    botExpirience[trup] = 0
    botLvl[trup] = 0
    botRasa[trup] = 0
    botZaklinania[trup] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botVozdeistvie[trup] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botInventar[trup] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botIshZdorovie[trup] = 0
    botZdorovie[trup] = 0
    botMana[trup] = 0
    botIshMana[trup] = 0
    botSila[trup] = 0
    botLovkost[trup] = 0
    botYdacha[trup] = 0
    botZachita[trup] = 0
    botHod[trup] = 0
    world[botLocation[trup]] = 0
    botNumer[trup] = 0
    botVariant[trup] = 0
    botAlgoritm[trup] = 0
    botLocation[trup] = 0

def mutation(): # Изменяем геном. Меняем случайный ген случайным образом
    global genom, iteration, lifeTime
    
    genMutant = int(random.random() * 128)
    iteration += 1
    lifeTime = 0
    #worldCreate()
    numerMutant = int(random.random() * 64)
    
    genom[genMutant] = numerMutant
    
    #for n in range(10):
    #    botLocation[n] = locations[n]
    #    botMana[n] = 200
    #    botIshMana[n] = 200
    #    botIshZdorovie[n] = 100
    #    botZdorovie[n] = 100
    #    botVariant[n] = 151+n
    #    botZaklinania[n] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #    if n<5: botRasa[n] = 1
    #    else: botRasa[n] = 2
    #    botSila[n] = 10
    #    world[locations[n]] = 151+n
    print("===================================================================")    
    print("Iteration #", str(iteration), "gene - ", str(genMutant), " changed - ", str(numerMutant), ". Event =",str(sobitie))
    print("Genom:", str(genom))
def bornBot(numerBurnBota, typeBurnBota):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, world 
    
    if typeBurnBota == 100 or typeBurnBota == 101 or typeBurnBota == 102 or typeBurnBota == 106 or typeBurnBota == 107 or typeBurnBota == 108 or typeBurnBota == 109 or typeBurnBota == 110 or typeBurnBota == 111 or typeBurnBota == 112 or typeBurnBota == 113 or typeBurnBota == 114 or typeBurnBota == 115 or typeBurnBota == 116 or typeBurnBota == 117 or typeBurnBota == 118 or typeBurnBota == 126 or typeBurnBota == 127 or typeBurnBota == 128 or typeBurnBota == 129 or typeBurnBota == 145 or typeBurnBota == 146 or typeBurnBota == 157 or typeBurnBota == 165 or typeBurnBota == 166 or typeBurnBota == 167 or typeBurnBota == 168 or typeBurnBota == 169 or typeBurnBota == 170 or typeBurnBota == 171 or typeBurnBota == 172:
        if world[30] == 0:
            xBot[numerBurnBota] = 976
            yBot[numerBurnBota] = 96
            world[30] = typeBurnBota
            botLocation[numerBurnBota] = 30
        elif world[63] == 0:
            xBot[numerBurnBota] = 976
            yBot[numerBurnBota] = 128
            world[63] = typeBurnBota
            botLocation[numerBurnBota] = 63 
        elif world[62] == 0:
            xBot[numerBurnBota] = 1008
            yBot[numerBurnBota] = 128
            world[62] = typeBurnBota  
            botLocation[numerBurnBota] = 62
        elif world[146] == 0:
            xBot[numerBurnBota] = 592
            yBot[numerBurnBota] = 224
            world[146] = typeBurnBota
            botLocation[numerBurnBota] = 146
        elif world[144] == 0:
            xBot[numerBurnBota] = 528
            yBot[numerBurnBota] = 224
            world[144] = typeBurnBota
            botLocation[numerBurnBota] = 144
        elif world[113] == 0:
            xBot[numerBurnBota] = 560
            yBot[numerBurnBota] = 192
            world[113] = typeBurnBota
            botLocation[numerBurnBota] = 113
        elif world[177] == 0:
            xBot[numerBurnBota] = 560
            yBot[numerBurnBota] = 256
            world[177] = typeBurnBota
            botLocation[numerBurnBota] = 177
            
    else:
        if world[384] == 0:
            xBot[numerBurnBota] = 16
            yBot[numerBurnBota] = 480
            world[384] = typeBurnBota
            botLocation[numerBurnBota] = 384 
        elif world[385] == 0:
            xBot[numerBurnBota] = 48
            yBot[numerBurnBota] = 480
            world[385] = typeBurnBota
            botLocation[numerBurnBota] = 385 
        elif world[417] == 0:
            xBot[numerBurnBota] = 48
            yBot[numerBurnBota] = 512
            world[417] = typeBurnBota
            botLocation[numerBurnBota] = 417
        elif world[146] == 0:
            xBot[numerBurnBota] = 592
            yBot[numerBurnBota] = 224
            world[146] = typeBurnBota
            botLocation[numerBurnBota] = 146
        elif world[144] == 0:
            xBot[numerBurnBota] = 528
            yBot[numerBurnBota] = 224
            world[144] = typeBurnBota
            botLocation[numerBurnBota] = 144
        elif world[113] == 0:
            xBot[numerBurnBota] = 560
            yBot[numerBurnBota] = 192
            world[113] = typeBurnBota
            botLocation[numerBurnBota] = 113
        elif world[177] == 0:
            xBot[numerBurnBota] = 560
            yBot[numerBurnBota] = 256
            world[177] = typeBurnBota
            botLocation[numerBurnBota] = 177     
        

def botActivity(nomerBota):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations  
    
    #print("botActivity", str(sobitie))
    if sobitie % 597 == 0: mutation()
    
    if sobitie % 1537 == 0: # Рожаем бота
        for n in range(1000):
            if botZdorovie[n] <= 0: #Если бот номер N мёртв, то занимаем его ID
                tmp = int(random.random()*72)+100 # Генеруем вид бота
                botRandom = int(random.random()*100) # Переменная для случайного распределения артефактов
                print("BORN bot #",str(n)," variant -",str(tmp))
                if tmp == 100: # Эльф 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 110
                    botIshZdorovie[n] = 110
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 10
                    botLovkost[n] = 6
                    botYdacha[n] = 5
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 60
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 150
                    if botRandom == 10:
                        botInventar[n] = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    bornBot(n, tmp)           
                            
                            
                
                if tmp == 101: # Эльф 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 125
                    botIshZdorovie[n] = 125
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 12
                    botLovkost[n] = 7
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 90
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 400       
                    bornBot(n, tmp)
                        
                if tmp == 102: # Эльф 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 150
                    botIshZdorovie[n] = 150
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 15
                    botLovkost[n] = 8
                    botYdacha[n] = 8
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 1
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 250
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 350 
                    if botRandom == 10:
                        botInventar[n] = [4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2
                        botBronza[n] = 450       
                    bornBot(n, tmp)
                        
                if tmp == 103: # Гнолл 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 110
                    botIshZdorovie[n] = 110
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 10
                    botLovkost[n] = 5
                    botYdacha[n] = 3
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 100
                    bornBot(n, tmp) 
                        
                if tmp == 104: # Гнолл 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 125
                    botIshZdorovie[n] = 125
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 12
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 60
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 120
                    bornBot(n, tmp)  
                        
                if tmp == 105: # Гнолл 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 150
                    botIshZdorovie[n] = 150
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 15
                    botLovkost[n] = 7
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 40
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 180
                    bornBot(n, tmp)    
                        
                if tmp == 106: # Гном 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 140
                    botIshZdorovie[n] = 140
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 18
                    botLovkost[n] = 7
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 180
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 280
                    if botRandom == 10:
                        botInventar[n] = [67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1       
                        botBronza[n] = 400
                    bornBot(n, tmp)
                        
                if tmp == 107: # Гном 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 195
                    botIshZdorovie[n] = 195
                    botMana[n] = 60
                    botIshMana[n] = 60
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 21
                    botLovkost[n] = 9
                    botYdacha[n] = 12
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 200
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 300
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [68,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [69,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 108: # Гном 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 275
                    botIshZdorovie[n] = 275
                    botMana[n] = 120
                    botIshMana[n] = 120
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 25
                    botLovkost[n] = 9
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 300
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [68,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 400
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [69,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2 
                        botBronza[n] = 500
                    if botRandom == 10:
                        botInventar[n] = [70,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3       
                        botBronza[n] = 650
                    bornBot(n, tmp)
                        
                if tmp == 109: # Гном 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 375
                    botIshZdorovie[n] = 375
                    botMana[n] = 180
                    botIshMana[n] = 180
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 31
                    botLovkost[n] = 12
                    botYdacha[n] = 19
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [68,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 1
                    botBronza[n] = 500
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [69,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2
                        botBronza[n] = 500
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [70,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2 
                        botBronza[n] = 600
                    if botRandom == 10:
                        botInventar[n] = [70,5,3,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3       
                        botBronza[n] = 800
                    bornBot(n, tmp)
                        
                if tmp == 110: # Гоблин 0 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 0
                    botZdorovie[n] = 50
                    botIshZdorovie[n] = 50
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 3
                    botLovkost[n] = 5
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 10
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 30
                    if botRandom == 10:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botBronza[n] = 90
                    bornBot(n, tmp)
                        
                if tmp == 111: # Гоблин 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 100
                    botIshZdorovie[n] = 100
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 10
                    botLovkost[n] = 8
                    botYdacha[n] = 11
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 30
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 80
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 120
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botBronza[n] = 150
                    bornBot(n, tmp)
                        
                if tmp == 112: # Гоблин 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 120
                    botIshZdorovie[n] = 120
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 13
                    botLovkost[n] = 8
                    botYdacha[n] = 12
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 80
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 120
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 160
                    if botRandom == 10:
                        botInventar[n] = [3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botBronza[n] = 210
                    bornBot(n, tmp)
                        
                if tmp == 113: # Гоблин 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 145
                    botIshZdorovie[n] = 145
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 16
                    botLovkost[n] = 8
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 120
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 160
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 210
                    if botRandom == 10:
                        botInventar[n] = [3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botSerebro[n] = 1
                        botBronza[n] = 290
                    bornBot(n, tmp)
                        
                if tmp == 114: # Отшельник 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 125
                    botIshZdorovie[n] = 125
                    botMana[n] = 90
                    botIshMana[n] = 90
                    botZaklinania[n]=[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 11
                    botLovkost[n] = 6
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 60
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botSerebro[n] = 1
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 115: # Отшельник 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 165
                    botIshZdorovie[n] = 165
                    botMana[n] = 160
                    botIshMana[n] = 160
                    botZaklinania[n]=[6,22,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 14
                    botLovkost[n] = 6
                    botYdacha[n] = 12
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [7,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 60
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botSerebro[n] = 1
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 116: # Отшельник 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 225
                    botIshZdorovie[n] = 225
                    botMana[n] = 250
                    botIshMana[n] = 250
                    botZaklinania[n]=[6,22,7,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 18
                    botLovkost[n] = 6
                    botYdacha[n] = 19
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [8,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 250
                    if botRandom == 10:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botSerebro[n] = 1
                        botBronza[n] = 250
                    bornBot(n, tmp)
                        
                if tmp == 117: # Охотник за головами 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 265
                    botIshZdorovie[n] = 265
                    botMana[n] = 60
                    botIshMana[n] = 60
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 21
                    botLovkost[n] = 7
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [6,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [61,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 250
                    if botRandom == 10:
                        botInventar[n] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botSerebro[n] = 1
                        botBronza[n] = 250
                    bornBot(n, tmp)
                        
                if tmp == 118: # Человке 0 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 0
                    botZdorovie[n] = 50
                    botIshZdorovie[n] = 50
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 4
                    botLovkost[n] = 5
                    botYdacha[n] = 3
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 15
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 20
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 40
                    if botRandom == 10:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botBronza[n] = 90
                    bornBot(n, tmp)
                        
                if tmp == 119: # Монстр 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 140
                    botIshZdorovie[n] = 140
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 15
                    botLovkost[n] = 7
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 20
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 40
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 80
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 180
                    bornBot(n, tmp)
                        
                if tmp == 120: # Монстр 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 190
                    botIshZdorovie[n] = 190
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 18
                    botLovkost[n] = 7
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 20
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 40
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 80
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 180
                    bornBot(n, tmp)
                        
                if tmp == 121: # Монстр 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 300
                    botIshZdorovie[n] = 300
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 30
                    botLovkost[n] = 9
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2       
                        botBronza[n] = 450
                    bornBot(n, tmp) 
                        
                if tmp == 122: # Монстр 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 570
                    botIshZdorovie[n] = 570
                    botMana[n] = 400
                    botIshMana[n] = 400
                    botZaklinania[n]=[12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 45
                    botLovkost[n] = 9
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 500
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 600
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 750
                    if botRandom == 10:
                        botInventar[n] = [51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 4       
                        botBronza[n] = 900
                    bornBot(n, tmp)
                        
                if tmp == 123: # Морлок 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 125
                    botIshZdorovie[n] = 125
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 12
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 60
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 120
                    bornBot(n, tmp)
                        
                if tmp == 124: # Морлок 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 165
                    botIshZdorovie[n] = 165
                    botMana[n] = 30
                    botIshMana[n] = 30
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 15
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 150
                    bornBot(n, tmp)
                        
                if tmp == 125: # Морлок 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 200
                    botIshZdorovie[n] = 200
                    botMana[n] = 90
                    botIshMana[n] = 90
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 20
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 160
                    if botRandom == 10:
                        botInventar[n] = [4,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 250
                    bornBot(n, tmp)
                        
                if tmp == 126: # Наёмник 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 130
                    botIshZdorovie[n] = 130
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 13
                    botLovkost[n] = 7
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 90
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [60,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [61,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 250       
                    bornBot(n, tmp)
                        
                if tmp == 127: # Наёмник 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 165
                    botIshZdorovie[n] = 165
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 16
                    botLovkost[n] = 7
                    botYdacha[n] = 10
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [60,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [61,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [62,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 450       
                    bornBot(n, tmp)
                        
                if tmp == 128: # Наёмник 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 210
                    botIshZdorovie[n] = 210
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 20
                    botLovkost[n] = 7
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 350
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [61,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 300
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [62,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [63,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 550       
                    bornBot(n, tmp)
                        
                if tmp == 129: # Наёмник 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 310
                    botIshZdorovie[n] = 310
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 29
                    botLovkost[n] = 7
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 450
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [62,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 500
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [63,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 600
                    if botRandom == 10:
                        botInventar[n] = [65,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 750       
                    bornBot(n, tmp)
                        
                if tmp == 130: # Некромант 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 350
                    botIshZdorovie[n] = 350
                    botMana[n] = 400
                    botIshMana[n] = 400
                    botZaklinania[n]=[12,22,6,5,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 20
                    botLovkost[n] = 7
                    botYdacha[n] = 25
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 450       
                    bornBot(n, tmp)
                        
                if tmp == 131: # Непобедимый 6 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 6
                    botZdorovie[n] = 490
                    botIshZdorovie[n] = 490
                    botMana[n] = 350
                    botIshMana[n] = 350
                    botZaklinania[n]=[12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 39
                    botLovkost[n] = 7
                    botYdacha[n] = 25
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [8,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 400
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 500
                    if botRandom == 10:
                        botInventar[n] = [65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 650       
                    bornBot(n, tmp)
                        
                if tmp == 132: # Непобедимый 7 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 7
                    botZdorovie[n] = 600
                    botIshZdorovie[n] = 600
                    botMana[n] = 490
                    botIshMana[n] = 490
                    botZaklinania[n]=[12,6,13,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 50
                    botLovkost[n] = 7
                    botYdacha[n] = 25
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [59,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 450
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 500
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 700
                    if botRandom == 10:
                        botInventar[n] = [51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 950       
                    bornBot(n, tmp)
                        
                if tmp == 133: # Огр 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 200
                    botIshZdorovie[n] = 200
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 25
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 20
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 50
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 100
                    bornBot(n, tmp)
                        
                if tmp == 134: # Огр 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 270
                    botIshZdorovie[n] = 270
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 31
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 5
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 50
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 150
                    bornBot(n, tmp)
                        
                if tmp == 135: # Оккультист 6 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 450
                    botIshZdorovie[n] = 450
                    botMana[n] = 550
                    botIshMana[n] = 550
                    botZaklinania[n]=[12,22,6,5,4,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 25
                    botLovkost[n] = 7
                    botYdacha[n] = 35
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,53,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 300
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [10,54,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 400
                    if botRandom == 12:
                        botInventar[n] = [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 650
                    if botRandom == 11:
                        botInventar[n] = [57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 650
                    if botRandom == 10:
                        botInventar[n] = [66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 650       
                    bornBot(n, tmp)
                        
                if tmp == 136: # Орк 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 135
                    botIshZdorovie[n] = 135
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 14
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 30
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 60
                    if botRandom == 10:
                        botInventar[n] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 120
                    bornBot(n, tmp)
                        
                if tmp == 137: # Орк 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 165
                    botIshZdorovie[n] = 165
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 17
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 300
                    bornBot(n, tmp)
                        
                if tmp == 138: # Орк 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 235
                    botIshZdorovie[n] = 235
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 23
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 300
                    bornBot(n, tmp)
                        
                if tmp == 139: # Орк 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 300
                    botIshZdorovie[n] = 300
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 30
                    botLovkost[n] = 6
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 140: # Орк 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 475
                    botIshZdorovie[n] = 475
                    botMana[n] = 200
                    botIshMana[n] = 200
                    botZaklinania[n]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 40
                    botLovkost[n] = 6
                    botYdacha[n] = 17
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [5,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 141: # Орк 6 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 6
                    botZdorovie[n] = 600
                    botIshZdorovie[n] = 600
                    botMana[n] = 300
                    botIshMana[n] = 300
                    botZaklinania[n]=[22,16,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 55
                    botLovkost[n] = 6
                    botYdacha[n] = 17
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [6,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 142: # Орк 7 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 7
                    botZdorovie[n] = 870
                    botIshZdorovie[n] = 870
                    botMana[n] = 400
                    botIshMana[n] = 400
                    botZaklinania[n]=[22,16,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 75
                    botLovkost[n] = 6
                    botYdacha[n] = 27
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [6,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 4
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [32,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 5
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 143: # Орк-шаман 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 300
                    botIshZdorovie[n] = 300
                    botMana[n] = 230
                    botIshMana[n] = 230
                    botZaklinania[n]=[12,7,4,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 30
                    botLovkost[n] = 6
                    botYdacha[n] = 15
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [73,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 144: # Оккультист 7 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 7
                    botZdorovie[n] = 590
                    botIshZdorovie[n] = 590
                    botMana[n] = 750
                    botIshMana[n] = 750
                    botZaklinania[n]=[12,22,6,5,4,7,14,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 35
                    botLovkost[n] = 7
                    botYdacha[n] = 35
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [59,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 350
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [73,53,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 400
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [10,58,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 500
                    if botRandom == 12:
                        botInventar[n] = [56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 950
                    if botRandom == 11:
                        botInventar[n] = [66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 950
                    if botRandom == 10:
                        botInventar[n] = [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 950       
                    bornBot(n, tmp)
                        
                if tmp == 145: # Разбойник 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 165
                    botIshZdorovie[n] = 165
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 17
                    botLovkost[n] = 6
                    botYdacha[n] = 6
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 300
                    bornBot(n, tmp)
                        
                if tmp == 146: # Разбойник 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 185
                    botIshZdorovie[n] = 185
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 20
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 200
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 250
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 147: # Красный огненный голем 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 500
                    botIshZdorovie[n] = 500
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 49
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 148: # Скелет 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 50
                    botIshZdorovie[n] = 50
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 5
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 149: # Скелет 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 75
                    botIshZdorovie[n] = 75
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 9
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 150: # Скелет 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 110
                    botIshZdorovie[n] = 110
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 12
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 151: # Скелет 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 155
                    botIshZdorovie[n] = 155
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 17
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 152: # Скелет 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 200
                    botIshZdorovie[n] = 200
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 27
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 153: # Скелет 6 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 6
                    botZdorovie[n] = 295
                    botIshZdorovie[n] = 295
                    botMana[n] = 170
                    botIshMana[n] = 170
                    botZaklinania[n]=[12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 40
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 154: # Скелет 7 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 7
                    botZdorovie[n] = 430
                    botIshZdorovie[n] = 430
                    botMana[n] = 200
                    botIshMana[n] = 200
                    botZaklinania[n]=[12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 53
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 155: # Скелет 8 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 8
                    botZdorovie[n] = 590
                    botIshZdorovie[n] = 590
                    botMana[n] = 300
                    botIshMana[n] = 300
                    botZaklinania[n]=[11,15,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 70
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 0
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 0
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 0
                    bornBot(n, tmp)
                        
                if tmp == 156: # Душекрад 10 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 10
                    botZdorovie[n] = 1350
                    botIshZdorovie[n] = 1350
                    botMana[n] = 1200
                    botIshMana[n] = 1200
                    botZaklinania[n]=[15,16,1,19,23,13,7,4,0,0,0,0,0,0,0,100]
                    botSila[n] = 120
                    botLovkost[n] = 6
                    botYdacha[n] = 47
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [10,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 350
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [31,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 4
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 5
                        botBronza[n] = 500
                    bornBot(n, tmp)
                        
                if tmp == 157: # Странник 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 240
                    botIshZdorovie[n] = 240
                    botMana[n] = 300
                    botIshMana[n] = 300
                    botZaklinania[n]=[22,6,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 20
                    botLovkost[n] = 7
                    botYdacha[n] = 25
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 450       
                    bornBot(n, tmp)
                        
                if tmp == 158: # Тролль 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 115
                    botIshZdorovie[n] = 115
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 11
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 350
                    bornBot(n, tmp)
                        
                if tmp == 159: # Тролль 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 135
                    botIshZdorovie[n] = 135
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 14
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 70
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 400
                    bornBot(n, tmp)
                        
                if tmp == 160: # Тролль 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 185
                    botIshZdorovie[n] = 185
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 19
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 250
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 400
                    if botRandom == 10:
                        botInventar[n] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 600
                    bornBot(n, tmp)
                        
                if tmp == 161: # Тролль 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 245
                    botIshZdorovie[n] = 245
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 27
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 130
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 230
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 380
                    if botRandom == 10:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 700
                    bornBot(n, tmp)
                        
                if tmp == 162: # Тролль 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 345
                    botIshZdorovie[n] = 345
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 39
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 200
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 30
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 60
                    if botRandom == 10:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 120
                    bornBot(n, tmp)
                        
                if tmp == 163: # Тролль 6 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 6
                    botZdorovie[n] = 495
                    botIshZdorovie[n] = 495
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 53
                    botLovkost[n] = 6
                    botYdacha[n] = 4
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 300
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [11,12,48,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 450
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [31,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 600
                    if botRandom == 10:
                        botInventar[n] = [31,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 900
                    bornBot(n, tmp)
                        
                if tmp == 164: # Вампир 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 245
                    botIshZdorovie[n] = 245
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 30
                    botLovkost[n] = 6
                    botYdacha[n] = 20
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [12,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 1
                    if botRandom == 10:
                        botInventar[n] = [53,11,12,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 3
                    bornBot(n, tmp)
                        
                if tmp == 165: # Колдун 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 350
                    botIshZdorovie[n] = 350
                    botMana[n] = 450
                    botIshMana[n] = 450
                    botZaklinania[n]=[22,6,12,1,9,19,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 20
                    botLovkost[n] = 7
                    botYdacha[n] = 25
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [8,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 250
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 400
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 500
                    if botRandom == 10:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 750       
                    bornBot(n, tmp)
                        
                if tmp == 166: # Женщина-эльф 1 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 1
                    botZdorovie[n] = 100
                    botIshZdorovie[n] = 100
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 9
                    botLovkost[n] = 6
                    botYdacha[n] = 7
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 60
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 150
                    if botRandom == 10:
                        botInventar[n] = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200       
                    bornBot(n, tmp)
                        
                if tmp == 167: # Женщина-эльф 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 130
                    botIshZdorovie[n] = 130
                    botMana[n] = 0
                    botIshMana[n] = 0
                    botZaklinania[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 13
                    botLovkost[n] = 6
                    botYdacha[n] = 13
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 120
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 350
                    if botRandom == 10:
                        botInventar[n] = [5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 500       
                    bornBot(n, tmp)
                        
                if tmp == 168: # Женщина-эльф 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 175
                    botIshZdorovie[n] = 175
                    botMana[n] = 80
                    botIshMana[n] = 80
                    botZaklinania[n]=[9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 19
                    botLovkost[n] = 6
                    botYdacha[n] = 18
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 170
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 270
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 370
                    if botRandom == 10:
                        botInventar[n] = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 570       
                    bornBot(n, tmp)
                        
                if tmp == 169: # Женщина-эльф 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 235
                    botIshZdorovie[n] = 235
                    botMana[n] = 180
                    botIshMana[n] = 180
                    botZaklinania[n]=[9,6,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 27
                    botLovkost[n] = 6
                    botYdacha[n] = 13
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 270
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 370
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [7,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 500
                    if botRandom == 10:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 700       
                    bornBot(n, tmp)
                        
                if tmp == 170: # Женщина-эльф 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 310
                    botIshZdorovie[n] = 310
                    botMana[n] = 300
                    botIshMana[n] = 300
                    botZaklinania[n]=[9,6,12,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 39
                    botLovkost[n] = 6
                    botYdacha[n] = 18
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 370
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 470
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [11,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 600
                    if botRandom == 10:
                        botInventar[n] = [72,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 900       
                    bornBot(n, tmp)
                        
                if tmp == 171: # Женщина-эльф 6 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 6
                    botZdorovie[n] = 440
                    botIshZdorovie[n] = 440
                    botMana[n] = 400
                    botIshMana[n] = 400
                    botZaklinania[n]=[9,6,12,23,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 52
                    botLovkost[n] = 6
                    botYdacha[n] = 18
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 480
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 580
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [11,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 800
                    if botRandom == 10:
                        botInventar[n] = [56,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 1000       
                    bornBot(n, tmp)
                        
                if tmp == 172: # Женщина-эльф 7 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 7
                    botZdorovie[n] = 640
                    botIshZdorovie[n] = 640
                    botMana[n] = 550
                    botIshMana[n] = 550
                    botZaklinania[n]=[9,6,12,23,19,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 69
                    botLovkost[n] = 6
                    botYdacha[n] = 18
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 680
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 780
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [11,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 900
                    if botRandom == 10:
                        botInventar[n] = [58,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 1500       
                    bornBot(n, tmp)                 
                        
                break   
                 
    
    if botZdorovie[0] <= 0 and botZdorovie[1] <= 0 and botZdorovie[2] <= 0 and botZdorovie[3]<= 0 and botZdorovie[4] <= 0 and botZdorovie[5] <= 0 and botZdorovie[6] <= 0 and botZdorovie[7] <= 0 and botZdorovie[8] <= 0 and  botZdorovie[9] <= 0:
        print(genom)
        print("Life time: ", lifeTime)
        mutation()        
    
    # Обрабатываем геном
    if botStep[nomerBota] > 127: botStep[nomerBota] = 0
    if botZdorovie[nomerBota] > 0: # Если бот жив
        if genom[botStep[nomerBota]] == 0: pass # Если равен нулю, то ничего не делаем
        
        elif genom[botStep[nomerBota]] == 1: # Идём вверх
            if botLocation[nomerBota]>=32:
                if world[botLocation[nomerBota]-32] == 0:
                    yBot[nomerBota] -= 32
                    world[botLocation[nomerBota]] = 0
                    world[botLocation[nomerBota]-32] = botVariant[nomerBota]
                    botLocation[nomerBota] -= 32
                    worldUpdate()
                    pygame.display.update()                    
        
        elif genom[botStep[nomerBota]] == 2: # Идём вниз
            if botLocation[nomerBota] <= 416:
                if world[botLocation[nomerBota]+32] == 0:
                    yBot[nomerBota] += 32
                    world[botLocation[nomerBota]] = 0
                    world[botLocation[nomerBota]+32] = botVariant[nomerBota]
                    botLocation[nomerBota] += 32
                    worldUpdate()
                    pygame.display.update()                    
                    
        elif genom[botStep[nomerBota]] == 3: # Идём влево
            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                if world[botLocation[nomerBota]-1] == 0:
                    xBot[nomerBota] -= 32
                    world[botLocation[nomerBota]] = 0
                    world[botLocation[nomerBota]-1] = botVariant[nomerBota]
                    botLocation[nomerBota] -= 1                
                    worldUpdate()
                    pygame.display.update()                                        
        
        elif genom[botStep[nomerBota]] == 4: # Идём вправо
            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                if world[botLocation[nomerBota]+1] == 0:
                    xBot[nomerBota] += 32
                    world[botLocation[nomerBota]] = 0
                    world[botLocation[nomerBota]+1] = botVariant[nomerBota]
                    botLocation[nomerBota] += 1
                    worldUpdate()
                    pygame.display.update()
        
        elif genom[botStep[nomerBota]] == 5: # Бьём врага вверх 
            if botLocation[nomerBota]>=32:
                if world[botLocation[nomerBota]-32] >= 50: # Если сверху кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+32 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot up. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                            break                    
                    
        elif genom[botStep[nomerBota]] == 6: # Бьём врага вниз 
            if botLocation[nomerBota] <= 416:
                if world[botLocation[nomerBota]+32] >= 50: # Если снизу кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-32 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot down. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])  
                            break
        
        elif genom[botStep[nomerBota]] == 7: # Бьём врага слева
            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                if world[botLocation[nomerBota]-1] >= 50: # Если слева кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+1 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                            break
        
        elif genom[botStep[nomerBota]] == 8: # Бьём врага справа
            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                if world[botLocation[nomerBota]+1] >= 50: # Если справа кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-1 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                            break

        elif genom[botStep[nomerBota]] == 9: # Бьём врага сверху-справа
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                    if world[botLocation[nomerBota]-31] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                                break
        
        elif genom[botStep[nomerBota]] == 10: # Бьём врага сверху-слева
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]-33] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])  
                                break
                            
        elif genom[botStep[nomerBota]] == 11: # Бьём врага снизу-справа
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                    if world[botLocation[nomerBota]+33] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                break
        
        elif genom[botStep[nomerBota]] == 12: # Бьём врага снизу-слева
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]+31] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                break
                            
        elif genom[botStep[nomerBota]] == 13:  # Применяем заклинание "Пронзающая смерть"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 1:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        break
                                    else: print("Less that 200 mana")
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        break
                                    else: print("Less that 200 mana")
    
                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        break
                                    else: print("Less that 200 mana")
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        break
                                    else: print("Less that 200 mana")                             
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    break
                                else: print("Less that 200 mana")

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                print("Bot is right, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    break
                                else: print("Less that 200 mana")

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    break
                                else: print("Less that 200 mana")
     
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    break
                                else: print("Less that 200 mana")  
                        
                        
        elif genom[botStep[nomerBota]] == 14:  # Применяем заклинание "Fair Ball"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 1:
                    for n in range(15):
                        if botZaklinania[n] == 6:
                            for n in range(1000):
                                if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                                    if botLocation[nomerBota]>=32:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            print("Bot is left, Im - ", str(nomerBota), "kast - Fair Ball")
                                            if botMana[nomerBota] >= 30:
                                                print("Excellent, bot ", str(n), "took damage")
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                break
                                            else: print("Less that 30 mana")
                            
                                if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                                    if botLocation[nomerBota]>=32:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            print("Bot is left, Im - ", str(nomerBota), "kast - Fair Ball")
                                            if botMana[nomerBota] >= 30:
                                                print("Excellent, bot ", str(n), "took damage")
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                break
                                            else: print("Less that 30 mana")

                                if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                                    if botLocation[nomerBota]<=416:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            print("Bot is left, Im - ", str(nomerBota), "kast - Fair Ball")
                                            if botMana[nomerBota] >= 30:
                                                print("Excellent, bot ", str(n), "took damage")
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                break
                                            else: print("Less that 30 mana")
                            
                                if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                                    if botLocation[nomerBota]<=416:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            print("Bot is left, Im - ", str(nomerBota), "kast - Fair Ball")
                                            if botMana[nomerBota] >= 30:
                                                print("Excellent, bot ", str(n), "took damage")
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                break
                                            else: print("Less that 30 mana")   
                
                                if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                                    if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                        print("Bot is left, Im - ", str(nomerBota), "kast - Fair Ball")
                                        if botMana[nomerBota] >= 30:
                                            print("Excellent, bot ", str(n), "took damage")
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            break
                                        else: print("Less that 30 mana")

                                if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                                    if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                        print("Bot is right, Im - ", str(nomerBota), "kast - Fair Ball")
                                        if botMana[nomerBota] >= 30:
                                            print("Excellent, bot ", str(n), "took damage")
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            break
                                        else: print("Less that 30 mana")

                                if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                                    if botLocation[nomerBota] >= 32:
                                        print("Bot is up, Im - ", str(nomerBota), "kast - Fair Ball")
                                        if botMana[nomerBota] >= 30:
                                            print("Excellent, bot ", str(n), "took damage")
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            break
                                        else: print("Less that 30 mana")
 
                                if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                                    if botLocation[nomerBota] <= 416:
                                        print("Bot is up, Im - ", str(nomerBota), "kast - Fair Ball")
                                        if botMana[nomerBota] >= 30:
                                            print("Excellent, bot ", str(n), "took damage")
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            break
                                        else: print("Less that 30 mana")

        elif genom[botStep[nomerBota]] == 15:  # Применяем заклинание "Молния"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 12:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Lightning")
                                    if botMana[nomerBota] >= 70:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        break
                                    else: print("Less that 70 mana")
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Lightning")
                                    if botMana[nomerBota] >= 70:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        break
                                    else: print("Less that 70 mana")

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Lightning")
                                    if botMana[nomerBota] >= 70:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        break
                                    else: print("Less that 70 mana")
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is left, Im - ", str(nomerBota), "kast - Lightning")
                                    if botMana[nomerBota] >= 70:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        break
                                    else: print("Less that 70 mana")   
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                print("Bot is left, Im - ", str(nomerBota), "kast - Lightning")
                                if botMana[nomerBota] >= 70:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    break
                                else: print("Less that 70 mana")

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                print("Bot is right, Im - ", str(nomerBota), "kast - Lightning")
                                if botMana[nomerBota] >= 70:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    break
                                else: print("Less that 70 mana")

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Lightning")
                                if botMana[nomerBota] >= 70:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    break
                                else: print("Less that 70 mana")
 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Lightning")
                                if botMana[nomerBota] >= 70:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    break
                                else: print("Less that 70 mana") 
        
        elif genom[botStep[nomerBota]] == 16:  # Применяем заклинание "Лечение"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 22:
                    if botZdorovie[nomerBota]+45 <= botIshZdorovie[nomerBota]:
                        if botMana[nomerBota] >= 30:
                            botMana[nomerBota] -= 30
                            botZdorovie[nomerBota] += 30
                            print("Bot #", str(nomerBota), " - I was healed")
                
                        else: print("Need a mana for heal")
                    else: print("no Treatment needed")
            
        elif genom[botStep[nomerBota]] == 17:  # Применяем заклинание "Лунный обряд"        
            for n in range(15):
                if botZaklinania[nomerBota][n] == 9:
                    if botZdorovie[nomerBota]+80 <= botIshZdorovie[nomerBota]:
                        if botMana[nomerBota] >= 70:
                            botMana[nomerBota] -= 70
                            if botZdorovie[nomerBota] +70 <= botIshZdorovie[nomerBota]:
                                botZdorovie[nomerBota] += 70
                            else: botZdorovie[nomerBota] = botIshZdorovie[nomerBota]
                            print("Bot #", str(nomerBota), " - I was healed")
                        else: print("Need a mana for heal")
                    else: print("no Moon Treatment needed")   
        
        elif genom[botStep[nomerBota]] == 18:  # Применяем заклинание "Телепортация"        
            for n in range(15):
                if botZaklinania[nomerBota][n] == 3:  
                    if botMana[nomerBota] >= 150:
                        print("Bot -", str(nomerBota)," Teleportation")
                        botMana[nomerBota] -= 150
                        profit = 0
                        while profit == 0:
                            teleport = int(random.random() * 448)
                            if world[teleport] == 0:
                                world[botLocation[nomerBota]] = 0
                                botLocation[nomerBota] = teleport
                                profit = 1
                                
        elif genom[botStep[nomerBota]] == 19: # Идём вверх-влево
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]-33] == 0:
                        yBot[nomerBota] -= 32
                        xBot[nomerBota] -= 32
                        world[botLocation[nomerBota]] = 0
                        world[botLocation[nomerBota]-33] = botVariant[nomerBota]
                        botLocation[nomerBota] -= 33
                        worldUpdate()
                        pygame.display.update()  
                    
                    
        elif genom[botStep[nomerBota]] == 20: # Идём вверх-вправо
            if botLocation[nomerBota]>= 32:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                    if world[botLocation[nomerBota]-31] == 0:
                        yBot[nomerBota] -= 32
                        xBot[nomerBota] += 32
                        world[botLocation[nomerBota]] = 0
                        world[botLocation[nomerBota]-31] = botVariant[nomerBota]
                        botLocation[nomerBota] -= 31
                        worldUpdate()
                        pygame.display.update()
                    
        elif genom[botStep[nomerBota]] == 21: # Идём вниз-влево
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]+31] == 0:
                        yBot[nomerBota] += 32
                        xBot[nomerBota] -= 32
                        world[botLocation[nomerBota]] = 0
                        world[botLocation[nomerBota]+31] = botVariant[nomerBota]
                        botLocation[nomerBota] += 31
                        worldUpdate()
                        pygame.display.update()  
                    
                    
        elif genom[botStep[nomerBota]] == 22: # Идём вниз-вправо
            if botLocation[nomerBota]<= 416:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                    if world[botLocation[nomerBota]+33] == 0:
                        yBot[nomerBota] += 32
                        xBot[nomerBota] += 32
                        world[botLocation[nomerBota]] = 0
                        world[botLocation[nomerBota]+33] = botVariant[nomerBota]
                        botLocation[nomerBota] += 33
                        worldUpdate()
                        pygame.display.update()
                        
        elif genom[botStep[nomerBota]] == 23:  # Применяем заклинание "Могильный луч"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 11:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                    if botMana[nomerBota] >= 60:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        break
                                    else: print("Less that 60 mana")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                    if botMana[nomerBota] >= 60:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        break
                                    else: print("Less that 60 mana")  
                                    break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:

                                    print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                    if botMana[nomerBota] >= 60:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        break
                                    else: print("Less that 60 mana")  
                                    break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                    if botMana[nomerBota] >= 60:
                                        print("Excellent, bot ", str(n), "took damage")
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        break
                                    else: print("Less that 60 mana")
                                    break   
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева

                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                if botMana[nomerBota] >= 60:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    break
                                else: print("Less that 60 mana")
                                break

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                if botMana[nomerBota] >= 60:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    break
                                else: print("Less that 60 mana")
                                break


                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                if botMana[nomerBota] >= 60:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    break
                                else: print("Less that 60 mana")
                                break
 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                print("Bot is up, Im - ", str(nomerBota), "kast - Grave ray")
                                if botMana[nomerBota] >= 60:
                                    print("Excellent, bot ", str(n), "took damage")
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    break
                                else: print("Less that 60 mana")
                                break
                                
        elif genom[botStep[nomerBota]] == 24:  # Применяем заклинание "Доспехи Феникса"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 3:
                    if botMana[nomerBota] >= 30:
                        for m in range(15):
                            if botVozdeistvie[nomerBota][n] == 3:
                                print("I'm already bewitched by the Phoenix Armor")
                                break
                            if m == 15 and botVozdeistvie[nomerBota][n] != 3: 
                                print("The jam is already active")  
                                botVozdeistvie[nomerBota][n] = 3
                                botDeistvie[nomerBota][n] = sobitie + 700
                                botMana[nomerBota] -= 30
                                print("Conjuring Phoenix Armor")
                                break
                            
                    else: print("Need a mana for Phoenix Armor")
                    break
                    
        elif genom[botStep[nomerBota]] == 25:  # Применяем заклинание "Обман"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 5:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 50:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 5:
                                                botVozdeistvie[n][m] = 5
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 50
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 50:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 5:
                                                botVozdeistvie[n][m] = 5
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 50
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 50:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 5:
                                                botVozdeistvie[n][m] = 5
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 50
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 50:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 5:
                                                botVozdeistvie[n][m] = 5
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 50
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 50:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 5:
                                            botVozdeistvie[n][m] = 5
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 50
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 50:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 5:
                                            botVozdeistvie[n][m] = 5
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 50
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 50:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 5:
                                            botVozdeistvie[n][m] = 5
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 50
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break
 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 50:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 5:
                                            botVozdeistvie[n][m] = 5
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 50
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break 
                                    
        elif genom[botStep[nomerBota]] == 26:  # Применяем заклинание "Отравление"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 7:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 30:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 7:
                                                botVozdeistvie[n][m] = 7
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 30
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 30:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 7:
                                                botVozdeistvie[n][m] = 7
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 30
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 30:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 7:
                                                botVozdeistvie[n][m] = 7
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 30
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 30:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 7:
                                                botVozdeistvie[n][m] = 7
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 30
                                                print("Conjuring Fraud")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Fraud")
                                    break
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 30:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 7:
                                            botVozdeistvie[n][m] = 7
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 30
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Fraud")
                                break

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 30:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 7:
                                            botVozdeistvie[n][m] = 7
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 30
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Fraud")
                                break

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 30:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 7:
                                            botVozdeistvie[n][m] = 7
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 30
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Fraud")
                                break
 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 30:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 7:
                                            botVozdeistvie[n][m] = 7
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 30
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Fraud")
                                break

        elif genom[botStep[nomerBota]] == 27:  # Применяем заклинание "Кровожадность"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 8:
                    if botMana[nomerBota] >= 35:
                        for m in range(15):
                            if botVozdeistvie[nomerBota][n] == 3:
                                print("I'm already bewitched by the Phoenix Armor")
                                break
                            if m == 15 and botVozdeistvie[nomerBota][n] != 3: 
                                print("The jam is already active")  
                                botVozdeistvie[nomerBota][n] = 3
                                botDeistvie[nomerBota][n] = sobitie + 700
                                botMana[nomerBota] -= 30
                                print("Conjuring Phoenix Armor")
                                break
                            
                    else: print("Need a mana for Phoenix Armor")
                    break
                    
        elif genom[botStep[nomerBota]] == 28:  # Применяем заклинание "Мощь Природы"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 10:
                    if botMana[nomerBota] >= 65:
                        for m in range(15):
                            if botVozdeistvie[nomerBota][n] == 3:
                                print("I'm already bewitched by the Phoenix Armor")
                                break
                            if m == 15 and botVozdeistvie[nomerBota][n] != 3: 
                                print("The jam is already active")  
                                botVozdeistvie[nomerBota][n] = 3
                                botDeistvie[nomerBota][n] = sobitie + 700
                                botMana[nomerBota] -= 30
                                print("Conjuring Phoenix Armor")
                                break
                            
                    else: print("Need a mana for Phoenix Armor")
                    break
                    
        elif genom[botStep[nomerBota]] == 29:  # Применяем заклинание "Печать Хаоса"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 13:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 170:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 13:
                                                botVozdeistvie[n][m] = 13
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 170
                                                print("Conjuring Seal of Chaos")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Chaos")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 170:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 13:
                                                botVozdeistvie[n][m] = 13
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 170
                                                print("Conjuring Seal of Chaos")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Chaos")
                                    break 

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 170:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 13:
                                                botVozdeistvie[n][m] = 13
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 170
                                                print("Conjuring Seal of Chaos")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Chaos")
                                    break 
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 170:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 13:
                                                botVozdeistvie[n][m] = 13
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 170
                                                print("Conjuring Seal of Chaos")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Chaos")
                                    break 
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 170:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 13:
                                            botVozdeistvie[n][m] = 13
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 170
                                            print("Conjuring Seal of Chaos")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Chaos")
                                break 

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 170:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 13:
                                            botVozdeistvie[n][m] = 13
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 170
                                            print("Conjuring Seal of Chaos")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Chaos")
                                break 

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 170:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 13:
                                            botVozdeistvie[n][m] = 13
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 170
                                            print("Conjuring Seal of Chaos")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Chaos")
                                break 

 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 170:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 13:
                                            botVozdeistvie[n][m] = 13
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 170
                                            print("Conjuring Seal of Chaos")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Chaos")
                                break 
                    
        elif genom[botStep[nomerBota]] == 30:  # Применяем заклинание "Поцелуй Смерти"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 15:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 100:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 15:
                                                botVozdeistvie[n][m] = 15
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 100
                                                print("Conjuring Kiss of death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for The Kiss of death")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 100:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 15:
                                                botVozdeistvie[n][m] = 15
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 100
                                                print("Conjuring Kiss of death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for The Kiss of death")
                                    break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 100:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 15:
                                                botVozdeistvie[n][m] = 15
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 100
                                                print("Conjuring Kiss of death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for The Kiss of death")
                                    break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 100:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 15:
                                                botVozdeistvie[n][m] = 15
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 100
                                                print("Conjuring Kiss of death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for The Kiss of death")
                                    break 
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 100:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 15:
                                            botVozdeistvie[n][m] = 15
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 100
                                            print("Conjuring Kiss of death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for The Kiss of death")
                                break 

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 100:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 15:
                                            botVozdeistvie[n][m] = 15
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 100
                                            print("Conjuring Kiss of death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for The Kiss of death")
                                break

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 100:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 15:
                                            botVozdeistvie[n][m] = 15
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 100
                                            print("Conjuring Kiss of death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for The Kiss of death")
                                    break

 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 100:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 15:
                                            botVozdeistvie[n][m] = 15
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 100
                                            print("Conjuring Kiss of death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for The Kiss of death")
                                break
                                
                            
        elif genom[botStep[nomerBota]] == 31:  # Применяем заклинание "Печать Смерти"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 14:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 200:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 14:
                                                botVozdeistvie[n][m] = 14
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 200
                                                print("Conjuring Seal of Death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Death")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 200:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 14:
                                                botVozdeistvie[n][m] = 14
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 200
                                                print("Conjuring Seal of Death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Death")
                                    break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 200:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 14:
                                                botVozdeistvie[n][m] = 14
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 200
                                                print("Conjuring Seal of Death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Death")
                                    break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 200:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 14:
                                                botVozdeistvie[n][m] = 14
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 200
                                                print("Conjuring Seal of Death")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Death")
                                    break
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 200:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 14:
                                            botVozdeistvie[n][m] = 14
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 200
                                            print("Conjuring Seal of Death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Death")
                                break

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 200:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 14:
                                            botVozdeistvie[n][m] = 14
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 200
                                            print("Conjuring Seal of Death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Death")
                                break

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 200:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 14:
                                            botVozdeistvie[n][m] = 14
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 200
                                            print("Conjuring Seal of Death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Seal of Death")
                                    break

 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 200:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 14:
                                            botVozdeistvie[n][m] = 14
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 200
                                            print("Conjuring Seal of Death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Death")
                                break                   
                    
        elif genom[botStep[nomerBota]] == 32:  # Применяем заклинание "Проклятье"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 16:
                    for n in range(1000):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 75:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 16:
                                                botVozdeistvie[n][m] = 16
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 75
                                                print("Conjuring Curse")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Curse")
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 75:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 16:
                                                botVozdeistvie[n][m] = 16
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 75
                                                print("Conjuring Curse")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Curse")
                                    break 

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 75:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 16:
                                                botVozdeistvie[n][m] = 16
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 75
                                                print("Conjuring Curse")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Curse")
                                    break 
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 75:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 16:
                                                botVozdeistvie[n][m] = 16
                                                botDeistvie[n][m] = sobitie + 700
                                                botMana[nomerBota] -= 75
                                                print("Conjuring Curse")
                                                break
                                            if m == 15: print("The jam is already active")  
                                    else: print("Need a mana for Curse")
                                    break 
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 75:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 16:
                                            botVozdeistvie[n][m] = 16
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 75
                                            print("Conjuring Curse")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Curse")
                                break 

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 75:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 16:
                                            botVozdeistvie[n][m] = 16
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 75
                                            print("Conjuring Curse")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Curse")
                                break 

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 75:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 16:
                                            botVozdeistvie[n][m] = 16
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 75
                                            print("Conjuring Curse")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Curse")
                                break 

 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 75:
                                    for m in range(15):
                                        if botVozdeistvie[n][m] != 16:
                                            botVozdeistvie[n][m] = 16
                                            botDeistvie[n][m] = sobitie + 700
                                            botMana[nomerBota] -= 75
                                            print("Conjuring Curse")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Curse")
                                break
                                
        elif genom[botStep[nomerBota]] == 33:  # Применяем заклинание "Рассеять Чары"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 23:
                    if botMana[nomerBota] >= 100:
                        for n in range(15):
                            if botVozdeistvie[nomerBota][n] != 23:
                                botVozdeistvie[nomerBota][n] = 23
                                botDeistvie[nomerBota][n] = sobitie + 700
                                botMana[nomerBota] -= 100
                                print("Conjuring Dispel spell")
                                break
                            if n == 15: print("The jam is already active")  
                    else: print("Need a mana for Dispel spell")
                    break
                    
        elif genom[botStep[nomerBota]] == 34: # Бьём врага вверх 
            if botLocation[nomerBota]>=32:
                if world[botLocation[nomerBota]-32] >= 50: # Если сверху кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+32 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot up. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                            break                    
                    
        elif genom[botStep[nomerBota]] == 35: # Бьём врага вниз 
            if botLocation[nomerBota] <= 416:
                if world[botLocation[nomerBota]+32] >= 50: # Если снизу кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-32 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot down. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])  
                            break
        
        elif genom[botStep[nomerBota]] == 36: # Бьём врага слева
            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:

                if world[botLocation[nomerBota]-1] >= 50: # Если слева кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+1 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                            break
        
        elif genom[botStep[nomerBota]] == 37: # Бьём врага справа
            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                if world[botLocation[nomerBota]+1] >= 50: # Если справа кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-1 and botZdorovie[n] > 0: 
                            botZdorovie[n] -= botSila[nomerBota]
                            print("Im - ", str(nomerBota), " shot right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                            break

        elif genom[botStep[nomerBota]] == 38: # Бьём врага сверху-справа
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:

                    if world[botLocation[nomerBota]-31] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                                break
        
        elif genom[botStep[nomerBota]] == 39: # Бьём врага сверху-слева
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]-33] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])  
                                break
                            
        elif genom[botStep[nomerBota]] == 40: # Бьём врага снизу-справа
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:

                    if world[botLocation[nomerBota]+33] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                break
        
        elif genom[botStep[nomerBota]] == 41: # Бьём врага снизу-слева
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]+31] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                botZdorovie[n] -= botSila[nomerBota]
                                print("Im - ", str(nomerBota), " shot up-left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                break                                                     

        
        
        else:
            pass # Тут мы должны сделать перескакивание команд
    else:
        pass
        
    botStep[nomerBota] += 1
    sobitie += 1
    #botZdorovie[nomerBota] -= 1
    if sobitie > 100000: sobitie = 0
   
worldCreate()    

locations = [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63]
n = 0


botLocation[n] = locations[n]
botMana[n] = 200
botIshMana[n] = 200
botIshZdorovie[n] = 100
botZdorovie[n] = 100
botVariant[n] = 151+n
botZaklinania[n] = [1,2,0,4,5,6,7,8,9,10,11,12,13,14,15,16]
if n<5: botRasa[n] = 1
else: botRasa[n] = 2
botSila[n] = 10
world[locations[n]] = 151+n


n = 0    
pygame.display.update()   
while True:
    #clock.tick(FPS)
    if botZdorovie[n] > 0: botActivity(n)
    if botVariant[n] > 0 and botZdorovie[n] <= 0:    
            ubiraemTrup(n)      
            world[botLocation[n]] = 0
            print("Bot ", str(n), " - DEAD")
            worldUpdate()
            pygame.display.update()
    n += 1
    
    if n >= 1000: n = 0; lifeTime += 1
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()    
            
    
                
  


# 100 - Эльф 1 ур, 101 - Эльф 2 ур, 102 - Эльф 3 ур, 103 - гнолл 1 ур, 104 - гнолл 2 ур
# 105 - Гнолл 3 ур, 106 - Гном 1 ур, 107 - Гном 2 ур, 108 - Гном 3 ур, 109 - Гном 4 ур
# 110 - Гоблин 0 ур, 111 - Гоблин 1 ур, 112 - Гоблин 2 ур, 113 - Гоблин 3 ур
# 114 - Отшельник 1 ур, 115 - Отшельник 2 ур, 116 - Отшельник 3 ур
# 117 - Охотник за головами 1 ур, 118 - Человек, 119 - Монстр 1 ур, 120 - Монстр 2 ур
# 121 - Монстр 3 ур, 122 - Монстр 4 ур, 123 - Морлок 1 ур, 124 - Морлок 2 ур, 125 - Морлок 3 ур
# 126 - Наемник 1 ур, 127 - Наемник 2 ур, 128 - Наемник 3 ур, 129 - наемник 4 ур
# 130 - Некромант 5 ур, 131 - Непобедимый 6 ур, 132 - Непобедимый 7 ур, 133 - Огр 1 ур, 134 - Огр 2 ур
# 135 - Оккультист 6 ур, 136 - Орк 1 ур, 137 - Орк 2 ур, 138 - Орк 3 ур, 139 - Окр 4 ур, 140 - орк 5 ур
# 141 - Орк 6 ур, 142 - Орк 7 ур, 143 - Орк-шаман, 144 - Оккультист 7 ур., 145 - Разбойник, 146 - грабитель
# 147 - Красный огненный голем 5 ур, 148 - Скелет 1 ур, 149 - Скелет 2 ур, 150 - Скелет 3 ур
# 151 - Скелет 4 ур, 152 - Скелет 5 ур, 153 - Скелет 6 ур, 154 - Скелет 7 ур, 155 - Скелет 8 ур
# 156 - Душекрад, 157 - Странник 4 ур, 158 - Тролль 1 ур, 159 - Тролль 2 ур, 160 - Тролль 3 ур
# 161 - Тролль 4 ур, 162 - Тролль 5 ур, 163 - Тролль 6 ур, 164 - Вампир 3 ур., 165 - Колдун 5 ур
# 166 - Женщина-эльф 1 ур, 167 - Женщина-эльф 2 ур, 168 - Женщина-эльф 3 ур
# 169 - Женщина-эльф 4 ур, 170 - Женщина-эльф 5 ур, 171 - Женщина-эльф 6 ур
# 172 - Женщина-эльф 7 ур        
