# -*- coding: utf-8 -*-
import pygame, sys, random
import pygame.freetype
import threading

genom = [4,2,5,5,5,5,5,5,5,5,1,26,24,0,17,46,3,7,10,29,9,1,57,46,4,13,46,60,1,5,2,36,1,27,23,26,43,5,17,46,2,7,12,1,42,33,17,46,0,11,42,4,8,43,17,46,54,7,22,26,8,4,17,46]

FPS = 60
xGameMap = 16 
yGameMap = 96 
xMap = 0
yMap = 0
xHeroIcon = 0
yHeroIcon = 0
xMagic = 0
yMagic = 0
n = 0
world = []

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
    if iconka == 147: pix = pygame.image.load('Images/redFireHolem_32.png'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))
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

def botActivity(nomerBota):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto    
    
    # Обрабатываем геном
    if botStep[nomerBota] > 63: botStep[nomerBota] = 0; print("Zero DAY")
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
            if world[botLocation[nomerBota]-32] >= 50: # Если сверху кто-то есть, то...
                for n in range(10):
                    tmp = n
                    if botLocation[nomerBota] == botLocation[n]-32: botZdorovie[n] -= botSila[nomerBota]; break; print("Im shot"); botZdorovie[nomerBota] += 2

        else:
            pass # Тут мы должны сделать перескакивание команд
    else:
        if botVariant[nomerBota] > 0:    
            ubiraemTrup(nomerBota)      
            world[botLocation[nomerBota]] = 0
            worldUpdate()
            pygame.display.update()
        
    botStep[nomerBota] += 1
    botZdorovie[nomerBota] -= 1
    

    
worldCreate()    

locations = [139,171,204,131,30,77,388,149,120,124]
n = 0

for n in range(10):
    botLocation[n] = locations[n]
    botZdorovie[n] = 151
    botVariant[n] = 151+n
    if n<5: botRasa[n] = 1
    else: botRasa[n] = 2
    botSila[n] = 10
    world[locations[n]] = 151+n


n = 0    
pygame.display.update()   
while True:
    clock.tick(FPS) 
    botActivity(n)
    #print(n)
    n += 1
    
    if n >= 10: n = 0
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()    
            
    
                
            