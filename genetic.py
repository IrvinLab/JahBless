# -*- coding: utf-8 -*-
import pygame, sys, random
import pygame.freetype
import threading
import random

n = 0 
m = 0
myGen = 1
test = 0 #0 - Стандартная игра (для удовольствия), 1 - игра в режиме тестирования с увеличенным количеством здоровья, маны и прочего

if myGen == 1:
    genom = [36, 14, 6, 33, 53, 15, 16, 2, 4, 18, 7, 10, 5, 2, 6, 18, 15, 57, 14, 25, 50, 19, 8, 15, 11, 1, 38, 8, 0, 13, 5, 10, 43, 19, 43, 9, 15, 47, 55, 47, 3, 31, 3, 36, 58, 9, 47, 12, 13, 20, 6, 9, 11, 12, 23, 26, 13, 10, 17, 17, 62, 56, 39, 10, 42, 32, 22, 49, 48, 4, 35, 10, 52, 41, 11, 23, 59, 61, 47, 21, 22, 3, 16, 24, 55, 34, 9, 22, 1, 36, 18, 19, 39, 41, 63, 43, 1, 41, 46, 51, 3, 28, 6, 29, 14, 53, 30, 29, 22, 47, 0, 8, 28, 30, 43, 47, 56, 44, 28, 42, 54, 13, 4, 6, 44, 8, 5, 45]




elif myGen == 2:
    genom = []
    for n in range(64):
        genom.append(n)
        createGen = int(random.random() * 64)
        genom[n] = createGen

print(genom)

newGame = 1
newGameButton = 0
imHero = 5
zakl = 0
posohSmerti = 0
attack = 0
hero = 52
market = [2,7,0,26,0,0,17,46,60,0,0,0,0,0,0,36]
xijina = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tmpMarket = 0
yaNaRinke = 0
buttonNextStep = 0
imBuyThis = 0
yes = 0
no = 0
hijinaMaga = 0
hijina = 0
zadanieMaga = 0
drujbaMaga= 0
tmpMagExp = 0
posohSveta = 0
posohProzrenia = 0

iteration = 1
FPS = 60
xGameMap = 16 
yGameMap = 96 
xMap = 0
yMap = 0
xShift = 410
yShift = 785
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
    global world, xMap, yMap, attack, zakl, invent, market, yaNaRinke, xGameMap, yGameMap
    
    attack = 0
    zakl = 0
    invent = 0

    market = [2,7,0,26,0,0,17,46,60,0,0,0,0,0,0,36] # В этом массиве лежит инвентарь, который доступен на рынке
    yaNaRinke = 0
    xGameMap = 16
    yGameMap = 548 
    
    for yMap in range(4): # Помещаем поле действий и инвентаря
        for xMap in range(4):
            pix = pygame.image.load('Images/zero.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xGameMap,yGameMap))
            xGameMap += 68

        xGameMap = 16
        yGameMap += 68 
    xGameMap = 772
    yGameMap = 548 
    xHero = 400
    yHero = 256
    for yMap in range(4): 
    
        for xMap in range(4):
            pix = pygame.image.load('Images/zero.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xGameMap,yGameMap))
            xGameMap += 68

        xGameMap = 772
        yGameMap += 68
        
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
    world[1] = 1
    world[33] = 1
    world[32] = 1
    
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

def levelUp(nomerBota):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations  
    
    if botExpirience[nomerBota] >= 5000*(1.54**(botLvl[nomerBota]-1)):
        botLvl[nomerBota] += 1
        botExpirience[nomerBota] = 0
        botIshMana[nomerBota] += 16 * botLvl[nomerBota]
        botMana[nomerBota] = botIshMana[nomerBota]
        botIshZdorovie[nomerBota] += 20 * botLvl[nomerBota]
        botZdorovie[nomerBota] = botIshZdorovie[nomerBota]
        botSila[nomerBota] += 1
        botLovkost[nomerBota] += 1
        botYdacha[nomerBota] += 1
        botVozdeistvie[nomerBota] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botDeistvie[nomerBota] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def myAttack(kletka):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations  
    
    n = 0
    for n in range(20):
        if botLocation[n] == kletka and n != imHero:
            if botLocation[imHero] == botLocation[n]+1 or botLocation[imHero] == botLocation[n]-1 or botLocation[imHero] == botLocation[n]+32 or botLocation[imHero] == botLocation[n]-32 or botLocation[imHero] == botLocation[n]+33 or botLocation[imHero] == botLocation[n]+31 or botLocation[imHero] == botLocation[n]-33 or botLocation[imHero] == botLocation[n]-31:
                if botSila[imHero] + botUseWeapon[imHero] > botZachita[n]:
                    botZdorovie[n] -= (botSila[imHero] + botUseWeapon[imHero]) + botZachita[n]
                    botExpirience[imHero] += botSila[imHero]
                    if botZdorovie[n] <= 0: otdaiLut(imHero, n); ubiraemTrup(n)
                    botVariant[imHero]
                    worldUpdate()
                    heroPanel(hero)
                    levelUp(imHero)
                    doebaca(kletka)
                

def botKoldun(nom, poriad, vragBot): # функция колдовства (Номер колдующего бота, порядковый номер заклинания, номер вражеского бота)
    yaKastanul = 0
    
    global n
    global bot 
    global botType
    global botStep
    global xBot
    global yBot
    global botExpirience
    global botLvl
    global botRasa
    global botZaklinania 
    global botVozdeistvie
    global botInventar
    global botIshZdorovie
    global botZdorovie
    global botMana
    global botIshMana
    global botSila
    global botLovkost
    global botYdacha
    global botZachita
    global botHod
    global world
    global botNumer
    global botVariant
    global botAlgoritm
    global botLocation
    global botDeistvie
    global zyxel
    global attack
    
    print ("Колдовство: ",nom, poriad, vragBot)
        
    if botZaklinania[nom][poriad] == 1:  # Пронзающая смерть
        if botLocation[nom] == botLocation[vragBot] or botLocation[nom] == botLocation[vragBot]-1 or botLocation[nom] == botLocation[vragBot]+1 or botLocation[nom] == botLocation[vragBot]-32 or botLocation[nom] == botLocation[vragBot]-31 or botLocation[nom] == botLocation[vragBot]-33 or botLocation[nom] == botLocation[vragBot]+32 or botLocation[nom] == botLocation[vragBot]+31 or botLocation[nom] == botLocation[vragBot]+33:    
            if botMana[nom] >= 200: # Если хватает маны, то колдуем
                botMana[nom] -= 200
                botZdorovie[vragBot] -= 300
                botHod[nom] -= 1
                print("Пронзающая смерть")
                botExpirience[nom] += 100
                yaKastanul = 1
                
    if botZaklinania[nom][poriad] == 2:  # Телепортация
        print("2ch")
        if botMana[nom] >= 350:
            
            if world[vragBot] == 0:
                botMana[nom] -= 350
                world[botLocation[nom]] = 0
                world[vragBot] = botVariant[nom]
                botLocation[nom] = vragBot
                if vragBot >=0 and vragBot <= 31: xBot = 16 + 32 * vragBot; yBot = 96
                if vragBot >=32 and vragBot <= 63: xBot = 16 + 32 * (vragBot-32); yBot = 128
                if vragBot >=64 and vragBot <= 95: xBot = 16 + 32 * (vragBot-64); yBot = 160
                if vragBot >=96 and vragBot <= 127: xBot = 16 + 32 * (vragBot-96); yBot = 192
                if vragBot >=128 and vragBot <= 159: xBot = 16 + 32 * (vragBot-128); yBot = 224 
                if vragBot >=160 and vragBot <= 191: xBot = 16 + 32 * (vragBot-160); yBot = 256 
                if vragBot >=192 and vragBot <= 223: xBot = 16 + 32 * (vragBot-192); yBot = 288 
                if vragBot >=224 and vragBot <= 255: xBot = 16 + 32 * (vragBot-224); yBot = 320 
                if vragBot >=256 and vragBot <= 287: xBot = 16 + 32 * (vragBot-256); yBot = 352 
                if vragBot >=288 and vragBot <= 319: xBot = 16 + 32 * (vragBot-288); yBot = 384 
                if vragBot >=320 and vragBot <= 351: xBot = 16 + 32 * (vragBot-320); yBot = 416 
                if vragBot >=352 and vragBot <= 383: xBot = 16 + 32 * (vragBot-352); yBot = 448 
                if vragBot >=384 and vragBot <= 415: xBot = 16 + 32 * (vragBot-384); yBot = 480 
                if vragBot >=416 and vragBot <= 447: xBot = 16 + 32 * (vragBot-416); yBot = 512
                worldUpdate()                    
                                
        
        
    if botZaklinania[nom][poriad] == 3: # Доспехи Феникса
        if botMana[nom] >= 30:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 3:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botDeistvie[vragBot][n] = 700
                        botVozdeistvie[vragBot][n] = 3
                        botMana[nom] -= 30
                        botExpirience[nom] += 10
                        break        
                n = 0
                yaKastanul = 1
    
    if botZaklinania[nom][poriad] == 4: # Кража магии
        botHod[nom] -= 1
        if botMana[nom] >= 200:
            botMana[nom] -= 200
            botMana[vragBot] = 0         
            yaKastanul = 1

    if botZaklinania[nom][poriad] == 5: # Обман
        if botMana[nom] >= 50:
            botHod[nom] -= 1
            botMana[nom] -= 50
            botExpirience[nom] += 10
            botAlgoritm[vragBot] = 0
            yaKastanul = 1

    if botZaklinania[nom][poriad] == 6: # Огненная сфера
        if botLocation[nom] == botLocation[vragBot] or botLocation[nom] == botLocation[vragBot]-1 or botLocation[nom] == botLocation[vragBot]+1 or botLocation[nom] == botLocation[vragBot]-32 or botLocation[nom] == botLocation[vragBot]-31 or botLocation[nom] == botLocation[vragBot]-33 or botLocation[nom] == botLocation[vragBot]+32 or botLocation[nom] == botLocation[vragBot]+31 or botLocation[nom] == botLocation[vragBot]+33:    
            if botMana[nom] >= 25:
                botMana[nom] -= 25
                botZdorovie[vragBot] -= 30
                botExpirience[nom] += 15
                botHod[nom] -= 1
                yaKastanul = 1
        
    if botZaklinania[nom][poriad] == 7: # Яд 
        if botMana[nom] >= 15:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 7:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botVozdeistvie[vragBot][n] = 7
                        botDeistvie[vragBot][n] = 1000
                        botMana[nom] -= 15
                        botExpirience[nom] += 10
                        break        
            n = 0
            yaKastanul = 1  
    
    if botZaklinania[nom][poriad] == 8: # Кровожадность
        if botMana[nom] >= 35:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 8:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botDeistvie[vragBot][n] = 10
                        botVozdeistvie[vragBot][n] = 8
                        botMana[nom] -= 35
                        botExpirience[nom] += 10
                        break        
            n = 0
            yaKastanul = 1  
  
    if botZaklinania[nom][poriad] == 9: # Лунный обряд
        if botMana[nom] >=50 and botZdorovie[vragBot]+70 <= botIshZdorovie[vragBot]:
            botMana[nom] -= 50
            botZdorovie[vragBot] += 70
            botHod[nom] -= 1
            botExpirience[nom] += 10
            print("Исцелили: ", vragBot)
            yaKastanul = 1
        elif botMana[nom] >=50 and botZdorovie[vragBot] > botIshZdorovie[vragBot]-70:
            botZdorovie[vragBot] = botIshZdorovie[vragBot] 
            print("Исцелили: ", vragBot, "Полное здоровье")
            botHod[nom] -= 1
            botExpirience[nom] += 10
            yaKastanul = 1 
  
    if botZaklinania[nom][poriad] == 10: # Мощь природы
        if botMana[nom] >= 60:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 10:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botVozdeistvie[vragBot][n] = 10
                        botDeistvie[vragBot][n] = 10
                        botMana[nom] -= 60
                        botExpirience[nom] += 15
                        break        
            n = 0
            yaKastanul = 1  
    if botZaklinania[nom][poriad] == 11: # Могильный луч
        if botLocation[nom] == botLocation[vragBot] or botLocation[nom] == botLocation[vragBot]-1 or botLocation[nom] == botLocation[vragBot]+1 or botLocation[nom] == botLocation[vragBot]-32 or botLocation[nom] == botLocation[vragBot]-31 or botLocation[nom] == botLocation[vragBot]-33 or botLocation[nom] == botLocation[vragBot]+32 or botLocation[nom] == botLocation[vragBot]+31 or botLocation[nom] == botLocation[vragBot]+33:    
            if botMana[nom] >= 60:
                botHod[nom] -= 1
                n = 0
                botZdorovie[vragBot] -= 50
                disable = 0
                for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                    if botVozdeistvie[vragBot][n] == 11:
                        dissable = 1
                        break
                if disable == 0:        
                    for n in range(15):
                        if botVozdeistvie[vragBot][n] == 0:
                            botVozdeistvie[vragBot][n] = 11
                            botDeistvie[vragBot][n] = 5
                            botExpirience[nom] += 30
                            botMana[nom] -= 60
                            break        
                n = 0
                yaKastanul = 1  
    if botZaklinania[nom][poriad] == 12: # Молния
        if botLocation[nom] == botLocation[vragBot] or botLocation[nom] == botLocation[vragBot]-1 or botLocation[nom] == botLocation[vragBot]+1 or botLocation[nom] == botLocation[vragBot]-32 or botLocation[nom] == botLocation[vragBot]-31 or botLocation[nom] == botLocation[vragBot]-33 or botLocation[nom] == botLocation[vragBot]+32 or botLocation[nom] == botLocation[vragBot]+31 or botLocation[nom] == botLocation[vragBot]+33:    
            if botMana[nom] >= 70:
                botMana[nom] -= 70
                botZdorovie[vragBot] -= 70
                botExpirience[nom] += 40
                botHod[nom] -= 1
                yaKastanul = 1
    
    if botZaklinania[nom][poriad] == 13: # Печать Хаоса
        if botMana[nom] >= 175:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 13:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botVozdeistvie[vragBot][n] = 13
                        botDeistvie[vragBot][n] = 10
                        botMana[nom] -= 175
                        botExpirience[nom] += 40
                        break        
            n = 0
            yaKastanul = 1  
        
    if botZaklinania[nom][poriad] == 14: # Печать Смерти
        if botMana[nom] >= 230:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 14:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botVozdeistvie[vragBot][n] = 14
                        botDeistvie[vragBot][n] = 5
                        botExpirience[nom] += 70
                        botMana[nom] -= 230
                        break        
            n = 0
            yaKastanul = 1  
    if botZaklinania[nom][poriad] == 15: # Поцелуй Смерти
        if botMana[nom] >= 150:
            botHod[nom] -= 1
            n = 0
            disable = 0
            for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                if botVozdeistvie[vragBot][n] == 15:
                    dissable = 1
                    break
            if disable == 0:        
                for n in range(15):
                    if botVozdeistvie[vragBot][n] == 0:
                        botVozdeistvie[vragBot][n] = 15
                        botDeistvie[vragBot][n] = 1000
                        botExpirience[nom] += 50
                        botMana[nom] -= 150
                        break        
            n = 0
            yaKastanul = 1  
    

    if botZaklinania[nom][poriad] == 22: # Лечение
        if botMana[nom] >=30 and botZdorovie[vragBot]+30 <= botIshZdorovie[vragBot]:
            botMana[nom] -= 30
            botZdorovie[vragBot] += 30
            botHod[nom] -= 1
            botExpirience[nom] += 10
            print("Подлечили бота: ", vragBot)
            yaKastanul = 1
        elif botMana[nom] >=30 and botZdorovie[vragBot] > botIshZdorovie[vragBot]-30:
            botZdorovie[vragBot] = botIshZdorovie[vragBot] 
            print("Подлечили бота: ", vragBot, "Полное здоровье")
            botHod[nom] -= 1
            yaKastanul = 1
            botExpirience[nom] += 10            
    
    if botZaklinania[nom][poriad] == 23: # Рассеять чары 170 маны
        if botMana[nom] >= 170:
            botMana[nom] -= 170
            botDeistvie[nom] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            botVozdeistvie[nom] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    if botZdorovie[vragBot] <= 0 and attack == 0: 
        randomMoney = int(random.random()*10)
        randomBronza = int(random.random()*70) * botLvl[vragBot]
        randomSerebro = int(random.random()*5) * botLvl[vragBot]
        if randomMoney >= 4 and  randomMoney <= 9:
            botBronza[nom] += randomBronza
        if randomMoney == 2 or randomMoney == 3:
            botSerebro[nom] += randomSerebro        
        otdaiLut(nom, vragBot)
        ubiraemTrup(vragBot)    
    
    worldUpdate()
    heroPanel(hero)
    return yaKastanul 

def useInventar(dasLut):
    global botExpirience
    global botLvl
    global botRasa
    global botZaklinania 
    global botVozdeistvie
    global botIshZdorovie
    global botInventar
    global botZdorovie
    global botMana
    global botIshMana
    global botSila
    global botLovkost
    global botYdacha
    global botZachita
    global botHod
    global botLocation
    global world
    global botStep
    global botNumer
    global botVariant
    global botAlgoritm
    global botDeistvie
    global hero
    global attack
    global invent
    global posohSmerti
    global posohSveta
    global posohProzrenia
    global posohVoli
    global posohVechnoiJizni
    global yes
    
    
    if botInventar[imHero][dasLut-1] == 1:
        if botZdorovie[imHero] < botIshZdorovie[imHero] - 30: botZdorovie[imHero] += 30
        else: botZdorovie[imHero] = botIshZdorovie[imHero]
    if botInventar[imHero][dasLut-1] == 2:
        if botZdorovie[imHero] < botIshZdorovie[imHero] - 65: botZdorovie[imHero] += 65
        else: botZdorovie[imHero] = botIshZdorovie[imHero]
    if botInventar[imHero][dasLut-1] == 3:
        if botZdorovie[imHero] < botIshZdorovie[imHero] - 150: botZdorovie[imHero] += 150
        else: botZdorovie[imHero] = botIshZdorovie[imHero]
    if botInventar[imHero][dasLut-1] == 4:
        if botZdorovie[imHero] < botIshZdorovie[imHero] - 320: botZdorovie[imHero] += 320
        else: botZdorovie[imHero] = botIshZdorovie[imHero]
    if botInventar[imHero][dasLut-1] == 5:
        if botZdorovie[imHero] < botIshZdorovie[imHero] - 675: botZdorovie[imHero] += 675
        else: botZdorovie[imHero] = botIshZdorovie[imHero]
    if botInventar[imHero][dasLut-1] == 6:
        if botMana[imHero] < botIshMana[imHero] - 60: botMana[imHero] += 60
        else: botMana[imHero] = botIshMana[imHero]
    if botInventar[imHero][dasLut-1] == 7:
        if botMana[imHero] < botIshMana[imHero] - 130: botMana[imHero] += 130
        else: botMana[imHero] = botIshMana[imHero]
    if botInventar[imHero][dasLut-1] == 8:
        if botMana[imHero] < botIshMana[imHero] - 260: botMana[imHero] += 260
        else: botMana[imHero] = botIshMana[imHero]
    if botInventar[imHero][dasLut-1] == 9:
        if botMana[imHero] < botIshMana[imHero] - 520: botMana[imHero] += 520
        else: botMana[imHero] = botIshMana[imHero]
    if botInventar[imHero][dasLut-1] == 10:
        if botMana[imHero] < botIshMana[imHero] - 1100: botMana[imHero] += 1100
        else: botMana[imHero] = botIshMana[imHero]   

    if botInventar[imHero][dasLut-1] == 11: 
        botVozdeistvie[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botDeistvie[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if botMana[imHero] < botIshMana[imHero] - 500: botMana[imHero] += 500
        else: botMana[imHero] = botIshMana[imHero]
        if botZdorovie[imHero] < botIshZdorovie[imHero] - 500: botZdorovie[imHero] += 500
        else: botZdorovie[imHero] = botIshZdorovie[imHero]
    
    if botInventar[imHero][dasLut-1] == 12: 
        botVozdeistvie[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botDeistvie[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    if botInventar[imHero][dasLut-1] == 26: # Используем топор
        botUseWeapon[imHero] = 3
    
    if botInventar[imHero][dasLut-1] == 27: 
        botUseWeapon[imHero] = 6
    
    if botInventar[imHero][dasLut-1] == 28: 
        botUseWeapon[imHero] = 12
    
    if botInventar[imHero][dasLut-1] == 29: 
        botUseWeapon[imHero] = 25
 
    if botInventar[imHero][dasLut-1] == 30: 
        botUseWeapon[imHero] = 35

    if botInventar[imHero][dasLut-1] == 31: 
        botUseWeapon[imHero] = 55

    if botInventar[imHero][dasLut-1] == 32: 
        botUseWeapon[imHero] = 75       
    
    if botInventar[imHero][dasLut-1] == 33: # Это книга Пронзающая Смерть
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 1
                break
    if botInventar[imHero][dasLut-1] == 34: # Это книга Добить и воскресить
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 2
                break
    
    if botInventar[imHero][dasLut-1] == 35: # Это книга Доспехи феникса
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 3
                break
    
    if botInventar[imHero][dasLut-1] == 36: # Это книга Яд
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 7
                break
                
    if botInventar[imHero][dasLut-1] == 37: # Это книга Могильный луч
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 11
                break

    if botInventar[imHero][dasLut-1] == 38: # Это книга печать хаоса
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 13
                break
                
    if botInventar[imHero][dasLut-1] == 39: # Это книга печать смерти
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 14
                break            

    if botInventar[imHero][dasLut-1] == 40: # Это книга пронзающий крик
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 17
                break

    if botInventar[imHero][dasLut-1] == 41: # Это книга обман
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 5
                break
                
    if botInventar[imHero][dasLut-1] == 42: # Это книга рассеять чары
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 23
                break            
    
    if botInventar[imHero][dasLut-1] == 54 and yes == 1:   # Это посох Прозрения      
        if botMana[imHero] >= 100:
            posohProzrenia = 1
            yes = 0
                
    if botInventar[imHero][dasLut-1] == 55 and yes == 1:   # Это посох Смерти      
        if botMana[imHero] >= 100:
            posohSmerti = 1
            yes = 0
    
    if botInventar[imHero][dasLut-1] == 56 and yes == 1:   # Это посох Света      
        if botMana[imHero] >= 50:
            posohSveta = 1
            yes = 0        
    
    if botInventar[imHero][dasLut-1] == 46: botZachita[imHero] = 3
    if botInventar[imHero][dasLut-1] == 47: botZachita[imHero] = 5
    if botInventar[imHero][dasLut-1] == 48: botZachita[imHero] = 8
    if botInventar[imHero][dasLut-1] == 49: botZachita[imHero] = 14
    if botInventar[imHero][dasLut-1] == 50: botZachita[imHero] = 21
    if botInventar[imHero][dasLut-1] == 51: botZachita[imHero] = 30
    
    if botInventar[imHero][dasLut-1] == 60: 
        botUseWeapon[imHero] = 3
        
    if botInventar[imHero][dasLut-1] == 61: 
        botUseWeapon[imHero] = 5
        
    if botInventar[imHero][dasLut-1] == 62: 
        botUseWeapon[imHero] = 8
        
    if botInventar[imHero][dasLut-1] == 63: 
        botUseWeapon[imHero] = 14
        
    if botInventar[imHero][dasLut-1] == 64: 
        botUseWeapon[imHero] = 21
       
    if botInventar[imHero][dasLut-1] == 65: 
        botUseWeapon[imHero] = 30

    if botInventar[imHero][dasLut-1] == 67: 
        botUseWeapon[imHero] = 4

    if botInventar[imHero][dasLut-1] == 68: 
        botUseWeapon[imHero] = 6  

    if botInventar[imHero][dasLut-1] == 69: 
        botUseWeapon[imHero] = 9

    if botInventar[imHero][dasLut-1] == 70: 
        botUseWeapon[imHero] = 13       
    
    if botInventar[imHero][dasLut-1] == 71: # Это книга Лечение
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 22
                break
                
    if botInventar[imHero][dasLut-1] == 72: # Это книга Лунный обряд
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 9
                break            
    
    if botInventar[imHero][dasLut-1] == 73: # Это книга Кража магии
        n = 0
        for n in range(15):
            if botZaklinania[imHero][n] == 0:
                botZaklinania[imHero][n] = 4
                break 
    
    if botInventar[imHero][dasLut-1] > 0 and botInventar[imHero][dasLut-1] <= 25:
        invent = 0
        attack = 0
        botInventar[imHero][dasLut-1] = 0
        printInventar(dasLut-1)
    if botInventar[imHero][dasLut-1] >= 33 and botInventar[imHero][dasLut-1] <= 42:
        invent = 0
        attack = 0
        botInventar[imHero][dasLut-1] = 0
        printInventar(dasLut-1)
    if botInventar[imHero][dasLut-1] >= 71 and botInventar[imHero][dasLut-1] <= 73:
        invent = 0
        attack = 0
        botInventar[imHero][dasLut-1] = 0
        printInventar(dasLut-1)        
    heroPanel(hero)

def otdaiLut(nom, vragBot):
    if botZdorovie[vragBot] <= 0: 
        botExpirience[nom] += int(botIshZdorovie[vragBot] / 2)
        tempEnum = 0
        botBronza[nom] += botBronza[vragBot]
        botSerebro[nom] += botSerebro[vragBot]
        botZoloto[nom] += botZoloto[vragBot]
        botZoloto[vragBot] = 0
        botSerebro[vragBot] = 0
        botBronza[vragBot] = 0
        for tempEnum in range(16):
            if botInventar[vragBot][tempEnum] > 0:
                if botInventar[nom][0] == 0: botInventar[nom][0] = botInventar[vragBot][tempEnum]
                else:
                    if botInventar[nom][1] == 0: botInventar[nom][1] = botInventar[vragBot][tempEnum]
                    else:
                        if botInventar[nom][2] == 0: botInventar[nom][2] = botInventar[vragBot][tempEnum]
                        else:
                            if botInventar[nom][3] == 0: botInventar[nom][3] = botInventar[vragBot][tempEnum]
                            else:
                                if botInventar[nom][4] == 0: botInventar[nom][4] = botInventar[vragBot][tempEnum]
                                else:
                                    if botInventar[nom][5] == 0: botInventar[nom][5] = botInventar[vragBot][tempEnum]
                                    else:
                                        if botInventar[nom][6] == 0: botInventar[nom][6] = botInventar[vragBot][tempEnum]
                                        else:
                                            if botInventar[nom][7] == 0: botInventar[nom][7] = botInventar[vragBot][tempEnum]
                                            else:
                                                if botInventar[nom][8] == 0: botInventar[nom][8] = botInventar[vragBot][tempEnum]
                                                else:
                                                    if botInventar[nom][9] == 0: botInventar[nom][9] = botInventar[vragBot][tempEnum]
                                                    else:
                                                        if botInventar[nom][10] == 0: botInventar[nom][10] = botInventar[vragBot][tempEnum]
                                                        else: 
                                                            if botInventar[nom][11] == 0: botInventar[nom][11] = botInventar[vragBot][tempEnum]
                                                            else:
                                                                if botInventar[nom][12] == 0: botInventar[nom][12] = botInventar[vragBot][tempEnum]
                                                                else:
                                                                    if botInventar[nom][13] == 0: botInventar[nom][13] = botInventar[vragBot][tempEnum]
                                                                    else:
                                                                        if botInventar[nom][14] == 0: botInventar[nom][14] = botInventar[vragBot][tempEnum]
                                                                        else:
                                                                            if botInventar[nom][15] == 0: botInventar[nom][15] = botInventar[vragBot][tempEnum]

def textInventar(nomInv):
    global botInventar, hero, tmpMarket, yes, no, botBronza, botSerebro, botZoloto, yaNaRinke
    
    heroPanel(hero)
    if botInventar[imHero][nomInv-1] > 0:
        pix = pygame.image.load('Images/yes.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (462,786))    
    
        pix = pygame.image.load('Images/no.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (530,786))    
                
    if tmpMarket == 1:
        heroPanel(hero)
        randMoney = 1        
        tmpMarket = 0
        yaNaRinke = 0        
        yes = 0
        no = 0
        if botInventar[imHero][nomInv-1] == 1: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 35
            else: botBronza[imHero] += 35
        if botInventar[imHero][nomInv-1] == 2: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 55
            else: botSerebro[imHero] += 1                
        if botInventar[imHero][nomInv-1] == 3: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 84
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 4: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 155
            else: botSerebro[imHero] += 3
        if botInventar[imHero][nomInv-1] == 5: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 280
            else: botSerebro[imHero] += 5
        if botInventar[imHero][nomInv-1] == 6: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 50
            else: botSerebro[imHero] += 1
        if botInventar[imHero][nomInv-1] == 7: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 98
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 8: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 175
            else: botSerebro[imHero] += 3
        if botInventar[imHero][nomInv-1] == 9: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 250
            else: botSerebro[imHero] += 5
        if botInventar[imHero][nomInv-1] == 10: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 420
            else: botSerebro[imHero] += 8
        if botInventar[imHero][nomInv-1] == 11: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 700
            else: botSerebro[imHero] += 14
        if botInventar[imHero][nomInv-1] == 12: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 385
            else: botSerebro[imHero] += 8
        if botInventar[imHero][nomInv-1] == 13: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 70
            else: botSerebro[imHero] += 1
        if botInventar[imHero][nomInv-1] == 14: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 100
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 15: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 133
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 16: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 224
            else: botSerebro[imHero] += 4
        if botInventar[imHero][nomInv-1] == 17: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 90
            else: botSerebro[imHero] += 1
        if botInventar[imHero][nomInv-1] == 18: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 175
            else: botSerebro[imHero] += 3
        if botInventar[imHero][nomInv-1] == 19: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 280
            else: botSerebro[imHero] += 5
        if botInventar[imHero][nomInv-1] == 20: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 60
            else: botSerebro[imHero] += 1
        if botInventar[imHero][nomInv-1] == 21: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 105
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 22: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 165
            else: botSerebro[imHero] += 3
        if botInventar[imHero][nomInv-1] == 23: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 70
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 24: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 119
            else: botSerebro[imHero] += 2
        if botInventar[imHero][nomInv-1] == 25: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 165
            else: botSerebro[imHero] += 3
        if botInventar[imHero][nomInv-1] == 26: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 210
            else: botSerebro[imHero] += 4
        if botInventar[imHero][nomInv-1] == 27: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 385
            else: botSerebro[imHero] += 7
        if botInventar[imHero][nomInv-1] == 28: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 700
            else: botSerebro[imHero] += 14
        if botInventar[imHero][nomInv-1] == 29: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1750
            else: botSerebro[imHero] += 35
        if botInventar[imHero][nomInv-1] == 30: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 3500
            else: botSerebro[imHero] += 70
        if botInventar[imHero][nomInv-1] == 31: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 5950
            else: botSerebro[imHero] += 118
        if botInventar[imHero][nomInv-1] == 32: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 9450
            else: botSerebro[imHero] += 189
        if botInventar[imHero][nomInv-1] == 33: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 2800
            else: botSerebro[imHero] += 56
        if botInventar[imHero][nomInv-1] == 34: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1400
            else: botSerebro[imHero] += 28
        if botInventar[imHero][nomInv-1] == 35: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 700
            else: botSerebro[imHero] += 14
        if botInventar[imHero][nomInv-1] == 36: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1660
            else: botSerebro[imHero] += 32
        if botInventar[imHero][nomInv-1] == 37: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1750
            else: botSerebro[imHero] += 35
        if botInventar[imHero][nomInv-1] == 38: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 2100
            else: botSerebro[imHero] += 42    
        if botInventar[imHero][nomInv-1] == 39: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 2800
            else: botSerebro[imHero] += 56
        if botInventar[imHero][nomInv-1] == 40: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1610
            else: botSerebro[imHero] += 32
        if botInventar[imHero][nomInv-1] == 41: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1890
            else: botSerebro[imHero] += 38
        if botInventar[imHero][nomInv-1] == 42: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1750
            else: botSerebro[imHero] += 35
        if botInventar[imHero][nomInv-1] == 43: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 525
            else: botSerebro[imHero] += 11
        if botInventar[imHero][nomInv-1] == 44: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 945
            else: botSerebro[imHero] += 19
        if botInventar[imHero][nomInv-1] == 45: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1400
            else: botSerebro[imHero] += 28
        if botInventar[imHero][nomInv-1] == 46: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 210
            else: botSerebro[imHero] += 4
        if botInventar[imHero][nomInv-1] == 47: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 350
            else: botSerebro[imHero] += 7
        if botInventar[imHero][nomInv-1] == 48: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 595
            else: botSerebro[imHero] += 12
        if botInventar[imHero][nomInv-1] == 49: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1120
            else: botSerebro[imHero] += 22
        if botInventar[imHero][nomInv-1] == 50: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 2100
            else: botSerebro[imHero] += 42
        if botInventar[imHero][nomInv-1] == 51: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 4200
            else: botSerebro[imHero] += 84
        if botInventar[imHero][nomInv-1] == 53: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 840
            else: botSerebro[imHero] += 17
        if botInventar[imHero][nomInv-1] == 54: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 4900
            else: botSerebro[imHero] += 98
        if botInventar[imHero][nomInv-1] == 55: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 5950
            else: botSerebro[imHero] += 119
        if botInventar[imHero][nomInv-1] == 56: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 5600
            else: botSerebro[imHero] += 112
        if botInventar[imHero][nomInv-1] == 57: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 7000
            else: botSerebro[imHero] += 140
        if botInventar[imHero][nomInv-1] == 58: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 4690
            else: botSerebro[imHero] += 94
        if botInventar[imHero][nomInv-1] == 59: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 700
            else: botSerebro[imHero] += 14
        if botInventar[imHero][nomInv-1] == 60: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 175
            else: botSerebro[imHero] += 3
        if botInventar[imHero][nomInv-1] == 61: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 315
            else: botSerebro[imHero] += 6
        if botInventar[imHero][nomInv-1] == 62: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 630
            else: botSerebro[imHero] += 12
        if botInventar[imHero][nomInv-1] == 63: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1680
            else: botSerebro[imHero] += 33
        if botInventar[imHero][nomInv-1] == 64: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 3000
            else: botSerebro[imHero] += 60
        if botInventar[imHero][nomInv-1] == 65: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 4200
            else: botSerebro[imHero] += 84
        if botInventar[imHero][nomInv-1] == 66: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 14000
            else: botSerebro[imHero] += 280
        if botInventar[imHero][nomInv-1] == 67: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 280
            else: botSerebro[imHero] += 5
        if botInventar[imHero][nomInv-1] == 68: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 455
            else: botSerebro[imHero] += 9
        if botInventar[imHero][nomInv-1] == 69: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 700
            else: botSerebro[imHero] += 14              
        if botInventar[imHero][nomInv-1] == 70: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1050
            else: botSerebro[imHero] += 21 
        if botInventar[imHero][nomInv-1] == 71: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1380
            else: botSerebro[imHero] += 27 
        if botInventar[imHero][nomInv-1] == 72: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 1540
            else: botSerebro[imHero] += 30 
        if botInventar[imHero][nomInv-1] == 73: 
            botInventar[imHero][nomInv-1] = 0
            if randMoney >= 0 and randMoney <= 3:
                botBronza[imHero] += 2100
            else: botSerebro[imHero] += 42             
            
        heroPanel(hero)    
        
    if botInventar[imHero][nomInv-1] == 1:
        variableName = u"Зелье здоровья 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+30 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 50бр|1ср/35бр"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 2:
        variableName = u"Зелье здоровья 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+65 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 170бр|2ср/55бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 3:
        variableName = u"Зелье здоровья 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+150 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 280бр|3ср/84бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 4:
        variableName = u"Зелье здоровья 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+320 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 400бр|4ср/155бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 5:
        variableName = u"Зелье здоровья 5 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+675 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 800бр|8ср/280бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 6:
        variableName = u"Зелье маны 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+60 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 90бр|2ср/50бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 7:
        variableName = u"Зелье маны 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+130 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 210бр|3ср/98бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 8:
        variableName = u"Зелье маны 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+260 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 370бр|5ср/175бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 9:
        variableName = u"Зелье маны 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+520 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 700бр|7ср/250бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 10:
        variableName = u"Зелье маны 5 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+1100 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 1350бр|12ср/420бр|8ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 11:
        variableName = u"Зелье восстановления"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+500 Здоровья +500 маны, плюс зелье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"действует подобно заклинанию"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Рассеять Чары "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2650бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 12:
        variableName = u"Зелье рассеивания"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Рассеять Чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 1100бр|12ср/385бр|8ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 13:
        variableName = u"Зелье Кипящей крови 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 100бр|2ср/70бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 14:
        variableName = u"Зелье Кипящей крови 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 140бр|3ср/100бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 15:
        variableName = u"Зелье Кипящей крови 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 190бр|4ср/133бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 16:
        variableName = u"Зелье Кипящей крови 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+20 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 320бр|6ср/224бр|4ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 17:
        variableName = u"Зелье Деревянной кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 130бр|3ср/90бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 18:
        variableName = u"Зелье Каменной кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 250бр|5ср/175бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 19:
        variableName = u"Зелье Обсидиановой кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 400бр|8ср/280бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 20:
        variableName = u"Зелье Паука"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+2 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 85бр|2ср/60бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 21:
        variableName = u"Зелье Ящерицы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+3 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 150бр|3ср/105бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 22:
        variableName = u"Зелье Пантеры"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 235бр|5ср/165бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 23:
        variableName = u"Зелье Леприкона 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 100бр|3ср/70бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 24:
        variableName = u"Зелье Леприкона 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 170бр|4ср/119бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 25:
        variableName = u"Зелье Леприкона 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 240бр|5ср/165бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 26:
        variableName = u"Топор Палача (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Подобные топоры обычно используют"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"палачи для выполнения своей "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"гнусной работы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"+3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 700бр|6ср/210бр|4ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
    if botInventar[imHero][nomInv-1] == 27:
        variableName = u"Топор Королвской стражи (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Подобными топорами обычно вооружены"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"королевские стражники. Видимо это"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"оружие было отнято у одного из них"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"во времена эпохи Смуты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"+6 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 1450бр|11ср/385бр|7ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
    if botInventar[imHero][nomInv-1] == 28:
        variableName = u"Топор Гнева (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Выкован из особо острой стали."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Он разрезает плоти и кости врага как"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"горячий нож сливочное масло. Один вид"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"этого топора внушает пронзающий ужас."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"+12 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 2900бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
    if botInventar[imHero][nomInv-1] == 29:
        variableName = u"Топор Алчности (4ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот топор усилен заклинаниями боли"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"и сам тянется к твоему врагу,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"дабы вкусить его крови."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+25 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 5000бр|50ср/1750бр|35ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[imHero][nomInv-1] == 30:
        variableName = u"Топор Ярости (5ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Усиленный магией Хаоса, этот топор - "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"воплощение самой Смерти. Он обладает"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"настолько разрушительной силой, "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"что с ним можно в одинчку одолеть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"целый отряд противника"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
        variableName = u"+35 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Куп./прод. 7350бр|100ср/3500бр|70ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 720))        
    if botInventar[imHero][nomInv-1] == 31:
        variableName = u"Топор Скорбящих вдов (6ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Название говорит само за себя."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"От гнева этого оружия нет спасиния "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"никому. Вряд ли в наше время есть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"кузнецы, способные выковать нечто "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"подобное. Это историческая реликвия"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
        variableName = u"+55 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Куп./прод. 11700бр|170ср/5950бр|118ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 720))
    if botInventar[imHero][nomInv-1] == 32:
        variableName = u"Топор Божественной Воли (7ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Умереть от этого оружия - большая"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"честь для врага. Этот топор зачарован"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"магией Древних Богов. Никому из ныне"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"живущих не подсилу такие заклятия."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"+75 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 21000бр|270ср/9450бр|189ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
    if botInventar[imHero][nomInv-1] == 33:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Пронзающая смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 4000бр|80ср/2800р|56ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 34:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию доб. и воскресить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2000бр|40ср/1400бр|28ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 35:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Доспехи Феникса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 1000бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 36:
        variableName = u"Книга "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560))        
        variableName = u"Обучает заклинанию Яд"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2300бр|46ср/1600бр|32ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 37:
        variableName = u"Книга "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Могильный луч"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2500бр|50ср/1750бр|35ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 38:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Печать Хаоса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 3000бр|60ср/2100бр|42ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 39:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Печать Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 4000бр|80ср/2800р|56ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 40:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Пронз. крик"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2300бр|46ср/1610бр|32ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 41:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Обман"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2700бр|54ср/1890бр|38ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 42:
        variableName = u"Книга "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Рассеять чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2500бр|50ср/1750бр|35ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 43:
        variableName = u"Ботинки Гонца (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Ногам удобно - двигаешься быстро"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))       
        variableName = u"+2 ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 750бр|15ср/525бр|11ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 44:
        variableName = u"Ботинки Путешественника (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"С такой обувью можно обойти весь свет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"за пару недель"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))       
        variableName = u"+4 ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1350бр|27ср/945бр|19ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 45:
        variableName = u"Ботинки Скитальца (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Верный друг искателя приключений"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+6 Ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 2000бр|40ср/1400бр|28ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 46:
        variableName = u"Шлем пехотинца (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Видимо кузнец, что выковал этот шлем "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"служил при королевском дворе, раз так "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"мастерски выковал этот доспех."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+3 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 900бр|6ср/210бр|4ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[imHero][nomInv-1] == 47:
        variableName = u"Офицерский шлем (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Видимо, что выковал этот шлем служил"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"при королевском дворе, раз так "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"мастерски выковал этот доспех."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+5 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 1500бр|10ср/350бр|7ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[imHero][nomInv-1] == 48:
        variableName = u"Шлем Паладинов (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Это отличный доспех. С ним не страшно"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"выйти и одному на отряд противника"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+8 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2900бр|17ср/595бр|12ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 49:
        variableName = u"Шлем Похитителя Душ (4ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Не каждый кузнец способен выковать"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"подобный доспех, не каждый боец"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"достоин его носить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+14 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 4350бр|32ср/1120бр|22ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[imHero][nomInv-1] == 50:
        variableName = u"Шлем Божественной Миссии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Доспех 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Видимо ты избран, раз носишь этот шлем"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+21 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 6150бр|60ср/2100бр|42ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 51:
        variableName = u"Шлем Бессмертия (6ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот доспех - проклятье Вашего врага"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"С ним Вы выбертесь даже из самой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"страшной западни."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+30 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 9500бр|120ср/4200бр|84ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[imHero][nomInv-1] == 52:
        variableName = u"Банка"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Отнесите эту банку в хижину Мага"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 53:
        variableName = u"Ожерелье духов Войны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Очень редкий артефакт, большая удача"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"найти такую ценную вещь"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+7 Защиты +3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1200бр|24ср/840бр|17ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u" Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 54:
        variableName = u"Посох Прозрения"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Позволяет узнать количество маны,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"и здоровье противка, а также какими"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"заклинаниями он обладает"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 7000бр|140ср/4900бр|98ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 55:
        variableName = u"Посох Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Пронзающая Смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 100 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 8500бр|170ср/5950бр|119ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 56:
        variableName = u"Посох Света"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Рассеять чары, а также даёт"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+100 Здоровья при использовании"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 8000бр|160ср/5600бр|112ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Требует 50 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 57:
        variableName = u"Посох Вечной Жизни"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Способен сотворить скелетов до"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 40/60/85/115/150 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 10000бр|200ср/7000бр|140ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 58:
        variableName = u"Посох Воли"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Способен подчинить существо до "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"5 уровня если оно не обладает защитой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"от средней Магии Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Требует 50/70/95/130/170 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 6700бр|134ср/4690бр|94ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))        
    if botInventar[imHero][nomInv-1] == 59:
        variableName = u"Рунный браслет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Зачарованный магией Порядка браслет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+3 Защиты +5 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 1000бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 60:
        variableName = u"Меч 1 ур"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Стандартное вооружение пехотинца"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 750бр|5ср/175бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 61:
        variableName = u"Меч Офицера гвардии (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Лезвие меча выполнено из лучшей стали"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"в королевстве."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+5 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1300бр|4ср/315бр|6ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 62:
        variableName = u"Меч Паладинов (3 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этим вооружаются лучшие войны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Короля Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+8 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2350бр|18ср/630бр|12ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 63:
        variableName = u"Меч Ледяной Мощи (4 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Клинок этого меча испещрён магическими"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"рунами, придающими ему большую"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"остроту. Не позавидуешь врагу, который"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"встретит его своей грудью."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"+14 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 4000бр|48ср/1680бр|33ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))        
    if botInventar[imHero][nomInv-1] == 64:
        variableName = u"Меч Смирения (5 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Глядя на этот меч, враг поймёт, что"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"он смотрит в лицо самой Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+21 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 8900бр|86ср/3000бр|60ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 65:
        variableName = u"Меч Великого Смирения (6 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Очень редкий артефакт. Этот меч усилен"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"заклинаниями Боли, что позволяет ему"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"без проблем разрезать любой доспех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+30 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 12000бр|120ср/4200бр|84ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 66:
        variableName = u"Усиленный посох Вечной Жизни"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Позволяет призывать скелетов от пятого"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"до восьмого уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 140/180/240 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 20000бр|400ср/14000бр|280ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 67:
        variableName = u"Молот кузнеца (1 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Почему бы им не вдарить по голове"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"какого-нибудь гнолла?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+4 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 800бр|8ср/280бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 68:
        variableName = u"Палица (2 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Суровая штука, она способна своими"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"острыми зубьями перемолоть все кости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+6 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1250бр|13ср/455бр|9ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 69:
        variableName = u"Молот Славы (3 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Такой обычно вручают выдающимся бойцам"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"королевства Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+9 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2100бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[imHero][nomInv-1] == 70:
        variableName = u"Молот Паладинов (4 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Некоторые паладины предпочитают"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"сражатся тяжёлом молотом, а не мечом"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+13 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 3500бр|30ср/1050бр|21ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if botInventar[imHero][nomInv-1] == 71:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Лечение"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0))
        sc.blit(nameObj,(440, 580))        
        variableName = u"Куп./прод. 1900бр|38ср/1380бр|27ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 72:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Лунный обряд"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2200бр|44ср/1540бр|30ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[imHero][nomInv-1] == 73:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Кража Магии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 3000бр|60ср/2100бр|42ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         

def marketPlace(press):
    global hero
    global botInventar
    global botZoloto
    global botSerebro
    global botBronza
    global tmpMarket
    global market
    
    heroPanel(hero)
    
    if press == 1: #Если на рынке нажали "ДА" т.е купить и посмотреть предложения
        nMark = 0
        for nMark in range(16):
            tmpMarket = 2
            if nMark == 0: xInv = 772; yInv = 548
            if nMark == 1: xInv = 840; yInv = 548
            if nMark == 2: xInv = 908; yInv = 548
            if nMark == 3: xInv = 976; yInv = 548
            if nMark == 4: xInv = 772; yInv = 616
            if nMark == 5: xInv = 840; yInv = 616
            if nMark == 6: xInv = 908; yInv = 616
            if nMark == 7: xInv = 976; yInv = 616
            if nMark == 8: xInv = 772; yInv = 684
            if nMark == 9: xInv = 840; yInv = 684
            if nMark == 10: xInv = 908; yInv = 684
            if nMark == 11: xInv = 976; yInv = 684
            if nMark == 12: xInv = 772; yInv = 752
            if nMark == 13: xInv = 840; yInv = 752
            if nMark == 14: xInv = 908; yInv = 752
            if nMark == 15: xInv = 976; yInv = 752
            if market[nMark] == 0:
                pix = pygame.image.load('Images/zero.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 1:
                pix = pygame.image.load('Images/healtPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 2:
                pix = pygame.image.load('Images/healtPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 3:
                pix = pygame.image.load('Images/healtPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 4:
                pix = pygame.image.load('Images/healtPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 5:
                pix = pygame.image.load('Images/healtPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))                       
            if market[nMark] == 6:
                pix = pygame.image.load('Images/manaPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 7:
                pix = pygame.image.load('Images/manaPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 8:
                pix = pygame.image.load('Images/manaPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 9:
                pix = pygame.image.load('Images/manaPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 10:
                pix = pygame.image.load('Images/manaPoison.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))                
            if market[nMark] == 11:
                pix = pygame.image.load('Images/zelieVostanovlenia.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 12:
                pix = pygame.image.load('Images/zelieRasseivania.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))   
            if market[nMark] == 13:
                pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 14:
                pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 15:
                pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 16:
                pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))           
            if market[nMark] == 17:
                pix = pygame.image.load('Images/zelieZaciti.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 18:
                pix = pygame.image.load('Images/zelieZaciti.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 19:
                pix = pygame.image.load('Images/zelieZaciti.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))            
            if market[nMark] == 20:
                pix = pygame.image.load('Images/zelieLovkosti.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 21:
                pix = pygame.image.load('Images/zelieLovkosti.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 22:
                pix = pygame.image.load('Images/zelieLovkosti.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))          
            if market[nMark] == 23:
                pix = pygame.image.load('Images/zelieUdachi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 24:
                pix = pygame.image.load('Images/zelieUdachi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 25:
                pix = pygame.image.load('Images/zelieUdachi.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))        
            if market[nMark] == 26:
                pix = pygame.image.load('Images/axe.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))   
            if market[nMark] == 27:
                pix = pygame.image.load('Images/axe1.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 28:
                pix = pygame.image.load('Images/axe2.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))         
            if market[nMark] == 29:
                pix = pygame.image.load('Images/axe3.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 30:
                pix = pygame.image.load('Images/axe4.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 31:
                pix = pygame.image.load('Images/axe5.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 32:
                pix = pygame.image.load('Images/axe6.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 33:
                pix = pygame.image.load('Images/book.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 34:
                pix = pygame.image.load('Images/book1.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 35:
                pix = pygame.image.load('Images/book2.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 36:
                pix = pygame.image.load('Images/book3.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 37:
                pix = pygame.image.load('Images/book4.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 38:
                pix = pygame.image.load('Images/book5.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 39:
                pix = pygame.image.load('Images/book6.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 40:
                pix = pygame.image.load('Images/book7.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 41:
                pix = pygame.image.load('Images/book8.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 42:
                pix = pygame.image.load('Images/book9.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))  
            if market[nMark] == 43:
                pix = pygame.image.load('Images/bot1.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 44:
                pix = pygame.image.load('Images/bot2.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 45:
                pix = pygame.image.load('Images/bot3.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 46:
                pix = pygame.image.load('Images/helmet.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 47:
                pix = pygame.image.load('Images/helmet1.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 48:
                pix = pygame.image.load('Images/helmet2.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 49:
                pix = pygame.image.load('Images/helmet3.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 50:
                pix = pygame.image.load('Images/helmet4.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 51:
                pix = pygame.image.load('Images/helmet5.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 52:
                pix = pygame.image.load('Images/jar.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 53:
                pix = pygame.image.load('Images/ojerelie.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 54:
                pix = pygame.image.load('Images/posohProzrenia.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 55:
                pix = pygame.image.load('Images/posohSmerti.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))        
            if market[nMark] == 56:
                pix = pygame.image.load('Images/posohSveta.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))        
            if market[nMark] == 57:
                pix = pygame.image.load('Images/posohVechnoiJizni.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 58:
                pix = pygame.image.load('Images/posohVoli.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))      
            if market[nMark] == 59:
                pix = pygame.image.load('Images/runesBraslet.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv)) 
            if market[nMark] == 60:
                pix = pygame.image.load('Images/sword.jpeg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 61:
                pix = pygame.image.load('Images/sword1.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))     
            if market[nMark] == 62:
                pix = pygame.image.load('Images/sword2.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))         
            if market[nMark] == 63:
                pix = pygame.image.load('Images/sword3.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))         
            if market[nMark] == 64:
                pix = pygame.image.load('Images/sword4.gif') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))         
            if market[nMark] == 65:
                pix = pygame.image.load('Images/sword5.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))         
            if market[nMark] == 66:
                pix = pygame.image.load('Images/usilenniiPosohVechnoiJizni.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))   
            if market[nMark] == 67:
                pix = pygame.image.load('Images/hammer.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))         
            if market[nMark] == 68:
                pix = pygame.image.load('Images/hammer1.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 69:
                pix = pygame.image.load('Images/hammer2.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))    
            if market[nMark] == 70:
                pix = pygame.image.load('Images/hammer3.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 71:
                pix = pygame.image.load('Images/book10.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 72:
                pix = pygame.image.load('Images/book11.jpg') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))
            if market[nMark] == 73:
                pix = pygame.image.load('Images/book12.png') 
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xInv,yInv))                 
        
    if press == 2:  # Если на рынке нажали "НЕТ" т.е. продать инвентарь
        variableName = u"Нажмите на предмет, который"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560))
        variableName = u"хотите продать"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        tmpMarket = 1

def putInventar(imBuyInventar):
    global tempEnum, botInventar, imHero
    tempEnum = 0
    for tempEnum in range(16):
        if botInventar[imHero][0] == 0: botInventar[imHero][0] = imBuyInventar; break
        else:
            if botInventar[imHero][1] == 0: botInventar[imHero][1] = imBuyInventar; break
            else:
                if botInventar[imHero][2] == 0: botInventar[imHero][2] = imBuyInventar; break
                else:
                    if botInventar[imHero][3] == 0: botInventar[imHero][3] = imBuyInventar; break
                    else:
                        if botInventar[imHero][4] == 0: botInventar[imHero][4] = imBuyInventar; break
                        else:
                            if botInventar[imHero][5] == 0: botInventar[imHero][5] = imBuyInventar; break
                            else:
                                if botInventar[imHero][6] == 0: botInventar[imHero][6] = imBuyInventar; break
                                else:
                                    if botInventar[imHero][7] == 0: botInventar[imHero][7] = imBuyInventar; break
                                    else:
                                        if botInventar[imHero][8] == 0: botInventar[imHero][8] = imBuyInventar; break
                                        else:
                                            if botInventar[imHero][9] == 0: botInventar[imHero][9] = imBuyInventar; break
                                            else:
                                                if botInventar[imHero][10] == 0: botInventar[imHero][10] = imBuyInventar; break
                                                else: 
                                                    if botInventar[imHero][11] == 0: botInventar[imHero][11] = imBuyInventar; break
                                                    else:
                                                        if botInventar[imHero][12] == 0: botInventar[imHero][12] = imBuyInventar; break
                                                        else:
                                                            if botInventar[imHero][13] == 0: botInventar[imHero][13] = imBuyInventar; break
                                                            else:
                                                                if botInventar[imHero][14] == 0: botInventar[imHero][14] = imBuyInventar; break
                                                                else:
                                                                    if botInventar[imHero][15] == 0: botInventar[imHero][15] = imBuyInventar; break
        
def buyInvent(imBuy): 
    global market,yes,no,imBuyThis,thisPlace,tempEnum,imHero, yaNaRinke, botBronza
    
    pix = pygame.image.load('Images/yes.png') 
    x_len = pix.get_width()
    y_len = pix.get_height() 
    sc.blit(pix, (462,786))    
    pix = pygame.image.load('Images/no.png') 
    x_len = pix.get_width()
    y_len = pix.get_height() 
    sc.blit(pix, (530,786))
                
    imBuyThis = 1
    thisPlace = imBuy
    print("Yes="+str(yes)+" thisPlace="+str(thisPlace-1)+" imBuyThis="+str(imBuyThis))
    if yes == 5:
        if market[thisPlace-1] == 1:
            if botBronza[imHero] >= 50:
                market[thisPlace-1] = 0
                putInventar(1)
                botBronza[imHero] -= 50
        if market[thisPlace-1] == 2:
            if botBronza[imHero] >= 170:
                market[thisPlace-1] = 0
                putInventar(2)
                botBronza[imHero] -= 170
        if market[thisPlace-1] == 3:
            if botBronza[imHero] >= 280:
                market[thisPlace-1] = 0
                putInventar(3)
                botBronza[imHero] -= 280
        if market[thisPlace-1] == 4:
            if botBronza[imHero] >= 400:
                market[thisPlace-1] = 0
                putInventar(4)
                botBronza[imHero] -= 400
        if market[thisPlace-1] == 5:
            if botBronza[imHero] >= 800:
                market[thisPlace-1] = 0
                putInventar(5)
                botBronza[imHero] -= 800     
        if market[thisPlace-1] == 6:
            if botBronza[imHero] >= 90:
                market[thisPlace-1] = 0
                putInventar(6)
                botBronza[imHero] -= 90
        if market[thisPlace-1] == 7:
            if botBronza[imHero] >= 210:
                market[thisPlace-1] = 0
                putInventar(7)
                botBronza[imHero] -= 210
        if market[thisPlace-1] == 8:
            if botBronza[imHero] >= 370:
                market[thisPlace-1] = 0
                putInventar(8)
                botBronza[imHero] -= 370
        if market[thisPlace-1] == 9:
            if botBronza[imHero] >= 700:
                market[thisPlace-1] = 0
                putInventar(9)
                botBronza[imHero] -= 700
        if market[thisPlace-1] == 10:
            if botBronza[imHero] >= 1350:
                market[thisPlace-1] = 0
                putInventar(10)
                botBronza[imHero] -= 1350
        if market[thisPlace-1] == 11:
            if botBronza[imHero] >= 2650:
                market[thisPlace-1] = 0
                putInventar(11)
                botBronza[imHero] -= 2650
        if market[thisPlace-1] == 12:
            if botBronza[imHero] >= 1100:
                market[thisPlace-1] = 0
                putInventar(12)
                botBronza[imHero] -= 1100
        if market[thisPlace-1] == 13:
            if botBronza[imHero] >= 100:
                market[thisPlace-1] = 0
                putInventar(13)
                botBronza[imHero] -= 100
        if market[thisPlace-1] == 14:
            if botBronza[imHero] >= 140:
                market[thisPlace-1] = 0
                putInventar(14)
                botBronza[imHero] -= 140
        if market[thisPlace-1] == 15:
            if botBronza[imHero] >= 190:
                market[thisPlace-1] = 0
                putInventar(15)
                botBronza[imHero] -= 190
        if market[thisPlace-1] == 16:
            if botBronza[imHero] >= 320:
                market[thisPlace-1] = 0
                putInventar(16)
                botBronza[imHero] -= 320
        if market[thisPlace-1] == 17:
            if botBronza[imHero] >= 130:
                market[thisPlace-1] = 0
                putInventar(17)
                botBronza[imHero] -= 130
        if market[thisPlace-1] == 18:
            if botBronza[imHero] >= 250:
                market[thisPlace-1] = 0
                putInventar(18)
                botBronza[imHero] -= 250
        if market[thisPlace-1] == 19:
            if botBronza[imHero] >= 400:
                market[thisPlace-1] = 0
                putInventar(19)
                botBronza[imHero] -= 400
        if market[thisPlace-1] == 20:
            if botBronza[imHero] >= 85:
                market[thisPlace-1] = 0
                putInventar(20)
                botBronza[imHero] -= 85
        if market[thisPlace-1] == 21:
            if botBronza[imHero] >= 150:
                market[thisPlace-1] = 0
                putInventar(21)
                botBronza[imHero] -= 150
        if market[thisPlace-1] == 22:
            if botBronza[imHero] >= 250:
                market[thisPlace-1] = 0
                putInventar(22)
                botBronza[imHero] -= 250
        if market[thisPlace-1] == 23:
            if botBronza[imHero] >= 100:
                market[thisPlace-1] = 0
                putInventar(23)
                botBronza[imHero] -= 100
        if market[thisPlace-1] == 24:
            if botBronza[imHero] >= 170:
                market[thisPlace-1] = 0
                putInventar(24)
                botBronza[imHero] -= 170
        if market[thisPlace-1] == 25:
            if botBronza[imHero] >= 240:
                market[thisPlace-1] = 0
                putInventar(25)
                botBronza[imHero] -= 240
        if market[thisPlace-1] == 26:
            if botBronza[imHero] >= 700:
                market[thisPlace-1] = 0
                putInventar(26)
                botBronza[imHero] -= 700
        if market[thisPlace-1] == 27:
            if botBronza[imHero] >= 1450:
                market[thisPlace-1] = 0
                putInventar(27)
                botBronza[imHero] -= 1450
        if market[thisPlace-1] == 28:
            if botBronza[imHero] >= 2900:
                market[thisPlace-1] = 0
                putInventar(28)
                botBronza[imHero] -= 2900
        if market[thisPlace-1] == 29:
            if botBronza[imHero] >= 5000:
                market[thisPlace-1] = 0
                putInventar(29)
                botBronza[imHero] -= 5000
        if market[thisPlace-1] == 30:
            if botBronza[imHero] >= 7350:
                market[thisPlace-1] = 0
                putInventar(30)
                botBronza[imHero] -= 7350
        if market[thisPlace-1] == 31:
            if botBronza[imHero] >= 11700:
                market[thisPlace-1] = 0
                putInventar(31)
                botBronza[imHero] -= 11700
        if market[thisPlace-1] == 32:
            if botBronza[imHero] >= 21000:
                market[thisPlace-1] = 0
                putInventar(32)
                botBronza[imHero] -= 21000
        if market[thisPlace-1] == 33:
            if botBronza[imHero] >= 4000:
                market[thisPlace-1] = 0
                putInventar(33)
                botBronza[imHero] -= 4000
        if market[thisPlace-1] == 34:
            if botBronza[imHero] >= 2000:
                market[thisPlace-1] = 0
                putInventar(34)
                botBronza[imHero] -= 2000
        if market[thisPlace-1] == 35:
            if botBronza[imHero] >= 1000:
                market[thisPlace-1] = 0
                putInventar(35)
                botBronza[imHero] -= 1000
        if market[thisPlace-1] == 36:
            if botBronza[imHero] >= 2300:
                market[thisPlace-1] = 0
                putInventar(36)
                botBronza[imHero] -= 2300
        if market[thisPlace-1] == 37:
            if botBronza[imHero] >= 2500:
                market[thisPlace-1] = 0
                putInventar(37)
                botBronza[imHero] -= 2500
        if market[thisPlace-1] == 38:
            if botBronza[imHero] >= 3000:
                market[thisPlace-1] = 0
                putInventar(38)
                botBronza[imHero] -= 3000
        if market[thisPlace-1] == 39:
            if botBronza[imHero] >= 4000:
                market[thisPlace-1] = 0
                putInventar(39)
                botBronza[imHero] -= 4000
        if market[thisPlace-1] == 40:
            if botBronza[imHero] >= 2300:
                market[thisPlace-1] = 0
                putInventar(40)
                botBronza[imHero] -= 2300
        if market[thisPlace-1] == 41:
            if botBronza[imHero] >= 2700:
                market[thisPlace-1] = 0
                putInventar(41)
                botBronza[imHero] -= 2700
        if market[thisPlace-1] == 42:
            if botBronza[imHero] >= 2500:
                market[thisPlace-1] = 0
                putInventar(42)
                botBronza[imHero] -= 2500
        if market[thisPlace-1] == 43:
            if botBronza[imHero] >= 750:
                market[thisPlace-1] = 0
                putInventar(43)
                botBronza[imHero] -= 750
        if market[thisPlace-1] == 44:
            if botBronza[imHero] >= 1350:
                market[thisPlace-1] = 0
                putInventar(44)
                botBronza[imHero] -= 1350
        if market[thisPlace-1] == 45:
            if botBronza[imHero] >= 2000:
                market[thisPlace-1] = 0
                putInventar(45)
                botBronza[imHero] -= 2000
        if market[thisPlace-1] == 46:
            if botBronza[imHero] >= 900:
                market[thisPlace-1] = 0
                putInventar(46)
                botBronza[imHero] -= 900
        if market[thisPlace-1] == 47:
            if botBronza[imHero] >= 1500:
                market[thisPlace-1] = 0
                putInventar(47)
                botBronza[imHero] -= 1500
        if market[thisPlace-1] == 48:
            if botBronza[imHero] >= 2900:
                market[thisPlace-1] = 0
                putInventar(48)
                botBronza[imHero] -= 2900
        if market[thisPlace-1] == 49:
            if botBronza[imHero] >= 4350:
                market[thisPlace-1] = 0
                putInventar(49)
                botBronza[imHero] -= 4350
        if market[thisPlace-1] == 50:
            if botBronza[imHero] >= 6150:
                market[thisPlace-1] = 0
                putInventar(50)
                botBronza[imHero] -= 6150
        if market[thisPlace-1] == 51:
            if botBronza[imHero] >= 9500:
                market[thisPlace-1] = 0
                putInventar(51)
                botBronza[imHero] -= 9500
        if market[thisPlace-1] == 53:
            if botBronza[imHero] >= 1200:
                market[thisPlace-1] = 0
                putInventar(53)
                botBronza[imHero] -= 1200
        if market[thisPlace-1] == 54:
            if botBronza[imHero] >= 7000:
                market[thisPlace-1] = 0
                putInventar(54)
                botBronza[imHero] -= 7000
        if market[thisPlace-1] == 55:
            if botBronza[imHero] >= 8500:
                market[thisPlace-1] = 0
                putInventar(55)
                botBronza[imHero] -= 8500
        if market[thisPlace-1] == 56:
            if botBronza[imHero] >= 8000:
                market[thisPlace-1] = 0
                putInventar(56)
                botBronza[imHero] -= 8000
        if market[thisPlace-1] == 57:
            if botBronza[imHero] >= 10000:
                market[thisPlace-1] = 0
                putInventar(57)
                botBronza[imHero] -= 10000
        if market[thisPlace-1] == 58:
            if botBronza[imHero] >= 6700:
                market[thisPlace-1] = 0
                putInventar(58)
                botBronza[imHero] -= 6700
        if market[thisPlace-1] == 59:
            if botBronza[imHero] >= 1000:
                market[thisPlace-1] = 0
                putInventar(59)
                botBronza[imHero] -= 1000
        if market[thisPlace-1] == 60:
            if botBronza[imHero] >= 750:
                market[thisPlace-1] = 0
                putInventar(60)
                botBronza[imHero] -= 750
        if market[thisPlace-1] == 61:
            if botBronza[imHero] >= 1300:
                market[thisPlace-1] = 0
                putInventar(61)
                botBronza[imHero] -= 1300
        if market[thisPlace-1] == 62:
            if botBronza[imHero] >= 2350:
                market[thisPlace-1] = 0
                putInventar(62)
                botBronza[imHero] -= 2350
        if market[thisPlace-1] == 63:
            if botBronza[imHero] >= 4000:
                market[thisPlace-1] = 0
                putInventar(900)
                botBronza[imHero] -= 4000
        if market[thisPlace-1] == 64:
            if botBronza[imHero] >= 8900:
                market[thisPlace-1] = 0
                putInventar(64)
                botBronza[imHero] -= 8900
        if market[thisPlace-1] == 65:
            if botBronza[imHero] >= 12000:
                market[thisPlace-1] = 0
                putInventar(65)
                botBronza[imHero] -= 12000
        if market[thisPlace-1] == 66:
            if botBronza[imHero] >= 20000:
                market[thisPlace-1] = 0
                putInventar(66)
                botBronza[imHero] -= 20000
        if market[thisPlace-1] == 67:
            if botBronza[imHero] >= 800:
                market[thisPlace-1] = 0
                putInventar(67)
                botBronza[imHero] -= 800
        if market[thisPlace-1] == 68:
            if botBronza[imHero] >= 1250:
                market[thisPlace-1] = 0
                putInventar(68)
                botBronza[imHero] -= 1250
        if market[thisPlace-1] == 69:
            if botBronza[imHero] >= 2100:
                market[thisPlace-1] = 0
                putInventar(69)
                botBronza[imHero] -= 2100
        if market[thisPlace-1] == 70:
            if botBronza[imHero] >= 3500:
                market[thisPlace-1] = 0
                putInventar(70)
                botBronza[imHero] -= 3500
        if market[thisPlace-1] == 71:
            if botBronza[imHero] >= 1900:
                market[thisPlace-1] = 0
                putInventar(71)
                botBronza[imHero] -= 1900
        if market[thisPlace-1] == 72:
            if botBronza[imHero] >= 2200:
                market[thisPlace-1] = 0
                putInventar(72)
                botBronza[imHero] -= 2200                
        if market[thisPlace-1] == 73:
            if botBronza[imHero] >= 3000:
                market[thisPlace-1] = 0
                putInventar(73)
                botBronza[imHero] -= 3000  
                
        yes = 0
        imBuyThis = 0
        thisPlace = 0
        yaNaRinke = 0
     
    pygame.draw.rect(sc, (255, 255, 255), (405, 558, 365, 216))
    if market[imBuy-1] == 1:
        variableName = u"Зелье здоровья 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+30 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 50бр|1ср/35бр"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if market[imBuy-1] == 2:
        variableName = u"Зелье здоровья 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+65 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 170бр|2ср/55бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if market[imBuy-1] == 3:
        variableName = u"Зелье здоровья 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+150 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 280бр|3ср/84бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 4:
        variableName = u"Зелье здоровья 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+320 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 400бр|4ср/155бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 5:
        variableName = u"Зелье здоровья 5 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+675 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 800бр|8ср/280бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 6:
        variableName = u"Зелье маны 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+60 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 90бр|2ср/50бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 7:
        variableName = u"Зелье маны 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+130 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 210бр|3ср/98бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if market[imBuy-1] == 8:
        variableName = u"Зелье маны 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+260 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 370бр|5ср/175бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 9:
        variableName = u"Зелье маны 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+520 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 700бр|7ср/250бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 10:
        variableName = u"Зелье маны 5 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+1100 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 1350бр|12ср/420бр|8ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 11:
        variableName = u"Зелье восстановления"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+500 Здоровья +500 маны, плюс зелье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"действует подобно заклинанию"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Рассеять Чары "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2650бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 12:
        variableName = u"Зелье рассеивания"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Рассеять Чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 1100бр|12ср/385бр|8ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 13:
        variableName = u"Зелье Кипящей крови 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 100бр|2ср/70бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 14:
        variableName = u"Зелье Кипящей крови 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 140бр|3ср/100бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 15:
        variableName = u"Зелье Кипящей крови 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 190бр|4ср/133бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 16:
        variableName = u"Зелье Кипящей крови 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+20 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 320бр|6ср/224бр|4ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 17:
        variableName = u"Зелье Деревянной кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 130бр|3ср/90бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 18:
        variableName = u"Зелье Каменной кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 250бр|5ср/175бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 19:
        variableName = u"Зелье Обсидиановой кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 400бр|8ср/280бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 20:
        variableName = u"Зелье Паука"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+2 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 85бр|2ср/60бр|1ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 21:
        variableName = u"Зелье Ящерицы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+3 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 150бр|3ср/105бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 22:
        variableName = u"Зелье Пантеры"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 235бр|5ср/165бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 23:
        variableName = u"Зелье Леприкона 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 100бр|3ср/70бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 24:
        variableName = u"Зелье Леприкона 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 170бр|4ср/119бр|2ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 25:
        variableName = u"Зелье Леприкона 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 240бр|5ср/165бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 26:
        variableName = u"Топор Палача (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Подобные топоры обычно используют"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"палачи для выполнения своей "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"гнусной работы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"+3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 700бр|6ср/210бр|4ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
    if market[imBuy-1] == 27:
        variableName = u"Топор Королвской стражи (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Подобными топорами обычно вооружены"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"королевские стражники. Видимо это"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"оружие было отнято у одного из них"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"во времена эпохи Смуты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"+6 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 1450бр|11ср/385бр|7ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
    if market[imBuy-1] == 28:
        variableName = u"Топор Гнева (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Выкован из особо острой стали."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Он разрезает плоти и кости врага как"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"горячий нож сливочное масло. Один вид"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"этого топора внушает пронзающий ужас."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"+12 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 2900бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
    if market[imBuy-1] == 29:
        variableName = u"Топор Алчности (4ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот топор усилен заклинаниями боли"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"и сам тянется к твоему врагу,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"дабы вкусить его крови."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+25 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 5000бр|50ср/1750бр|35ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if market[imBuy-1] == 30:
        variableName = u"Топор Ярости (5ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Усиленный магией Хаоса, этот топор - "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"воплощение самой Смерти. Он обладает"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"настолько разрушительной силой, "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"что с ним можно в одинчку одолеть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"целый отряд противника"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
        variableName = u"+35 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Куп./прод. 7350бр|100ср/3500бр|70ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 720))         
    if market[imBuy-1] == 31:
        variableName = u"Топор Скорбящих вдов (6ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Название говорит само за себя."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"От гнева этого оружия нет спасиния "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"никому. Вряд ли в наше время есть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"кузнецы, способные выковать нечто "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"подобное. Это историческая реликвия"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
        variableName = u"+55 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Куп./прод. 11700бр|170ср/5950бр|118ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 720)) 
    if market[imBuy-1] == 32:
        variableName = u"Топор Божественной Воли (7ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Умереть от этого оружия - большая"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"честь для врага. Этот топор зачарован"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"магией Древних Богов. Никому из ныне"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"живущих не подсилу такие заклятия."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"+75 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 21000бр|270ср/9450бр|189ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
    if market[imBuy-1] == 33:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Пронзающая смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 4000бр|80ср/2800р|56ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 34:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию доб. и воскресить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2000бр|40ср/1400бр|28ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 35:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Доспехи Феникса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 1000бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 36:
        variableName = u"Книга "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560))        
        variableName = u"Обучает заклинанию Яд"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2300бр|46ср/1600бр|32ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 37:
        variableName = u"Книга "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Могильный луч"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2500бр|50ср/1750бр|35ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 38:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Печать Хаоса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 3000бр|60ср/2100бр|42ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 39:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Печать Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 4000бр|80ср/2800р|56ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 40:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Пронз. крик"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2300бр|46ср/1610бр|32ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 41:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Обман"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2700бр|54ср/1890бр|38ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 42:
        variableName = u"Книга "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Рассеять чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2500бр|50ср/1750бр|35ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 43:
        variableName = u"Ботинки Гонца (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Ногам удобно - двигаешься быстро"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))       
        variableName = u"+2 ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 750бр|15ср/525бр|11ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 44:
        variableName = u"Ботинки Путешественника (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"С такой обувью можно обойти весь свет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"за пару недель"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))       
        variableName = u"+4 ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1350бр|27ср/945бр|19ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 45:
        variableName = u"Ботинки Скитальца (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Верный друг искателя приключений"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+6 Ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 2000бр|40ср/1400бр|28ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 46:
        variableName = u"Шлем пехотинца (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Видимо кузнец, что выковал этот шлем "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"служил при королевском дворе, раз так "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"мастерски выковал этот доспех."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+3 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 900бр|6ср/210бр|4ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if market[imBuy-1] == 47:
        variableName = u"Офицерский шлем (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Видимо, что выковал этот шлем служил"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"при королевском дворе, раз так "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"мастерски выковал этот доспех."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+5 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 1500бр|10ср/350бр|7ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if market[imBuy-1] == 48:
        variableName = u"Шлем Паладинов (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Это отличный доспех. С ним не страшно"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"выйти и одному на отряд противника"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+8 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2900бр|17ср/595бр|12ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 49:
        variableName = u"Шлем Похитителя Душ (4ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Не каждый кузнец способен выковать"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"подобный доспех, не каждый боец"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"достоин его носить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+14 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 4350бр|32ср/1120бр|22ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if market[imBuy-1] == 50:
        variableName = u"Шлем Божественной Миссии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Доспех 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Видимо ты избран, раз носишь этот шлем"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+21 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 6150бр|60ср/2100бр|42ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 51:
        variableName = u"Шлем Бессмертия (6ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот доспех - проклятье Вашего врага"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"С ним Вы выбертесь даже из самой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"страшной западни."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+30 Защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 9500бр|120ср/4200бр|84ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if market[imBuy-1] == 53:
        variableName = u"Ожерелье духов Войны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Очень редкий артефакт, большая удача"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"найти такую ценную вещь"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+7 Защиты +3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1200бр|24ср/840бр|17ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 54:
        variableName = u"Посох Прозрения"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Позволяет узнать количество маны,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"и здоровье противка, а также какими"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"заклинаниями он обладает"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 7000бр|140ср/4900бр|98ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 55:
        variableName = u"Посох Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Пронзающая Смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 100 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 8500бр|170ср/5950бр|119ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 56:
        variableName = u"Посох Света"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Рассеять чары, а также даёт"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 110 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+100 Здоровья при использовании"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 8000бр|160ср/5600бр|112ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Требует 50 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
    if market[imBuy-1] == 57:
        variableName = u"Посох Вечной Жизни"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Способен сотворить скелетов до"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 40/60/85/115/150 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 10000бр|200ср/7000бр|140ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if market[imBuy-1] == 58:
        variableName = u"Посох Воли"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Способен подчинить существо до "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"5 уровня если оно не обладает защитой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"от средней Магии Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Требует 50/70/95/130/170 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 6700бр|134ср/4690бр|94ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))         
    if market[imBuy-1] == 59:
        variableName = u"Рунный браслет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Зачарованный магией Порядка браслет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+3 Защиты +5 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 1000бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 60:
        variableName = u"Меч 1 ур"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Стандартное вооружение пехотинца"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Куп./прод. 750бр|5ср/175бр|3ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 61:
        variableName = u"Меч Офицера гвардии (2ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Лезвие меча выполнено из лучшей стали"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"в королевстве."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+5 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1300бр|4ср/315бр|6ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 62:
        variableName = u"Меч Паладинов (3 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этим вооружаются лучшие войны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Короля Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+8 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2350бр|18ср/630бр|12ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 63:
        variableName = u"Меч Ледяной Мощи (4 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Клинок этого меча испещрён магическими"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"рунами, придающими ему большую"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"остроту. Не позавидуешь врагу, который"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"встретит его своей грудью."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"+14 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Куп./прод. 4000бр|48ср/1680бр|33ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))        
    if market[imBuy-1] == 64:
        variableName = u"Меч Смирения (5 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Глядя на этот меч, враг поймёт, что"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"он смотрит в лицо самой Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+21 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 8900бр|86ср/3000бр|60ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 65:
        variableName = u"Меч Великого Смирения (6 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Очень редкий артефакт. Этот меч усилен"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"заклинаниями Боли, что позволяет ему"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"без проблем разрезать любой доспех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"+30 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Куп./прод. 12000бр|120ср/4200бр|84ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 66:
        variableName = u"Усиленный посох Вечной Жизни"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Позволяет призывать скелетов от пятого"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"до восьмого уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Требует 140/180/240 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 20000бр|400ср/14000бр|280ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 67:
        variableName = u"Молот кузнеца (1 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Почему бы им не вдарить по голове"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"какого-нибудь гнолла?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+4 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 800бр|8ср/280бр|5ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 68:
        variableName = u"Палица (2 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Суровая штука, она способна своими"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"острыми зубьями перемолоть все кости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+6 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 1250бр|13ср/455бр|9ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if market[imBuy-1] == 69:
        variableName = u"Молот Славы (3 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Такой обычно вручают выдающимся бойцам"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"королевства Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+9 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 2100бр|20ср/700бр|14ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
    if market[imBuy-1] == 70:
        variableName = u"Молот Паладинов (4 ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Некоторые паладины предпочитают"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"сражатся тяжёлом молотом, а не мечом"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"+13 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Куп./прод. 3500бр|30ср/1050бр|21ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if market[imBuy-1] == 71:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Лечение"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580)) 
        variableName = u"Куп./прод. 1900бр|38ср/1380бр|27ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if market[imBuy-1] == 72:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Лунный обряд"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 2200бр|44ср/1540бр|30ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Купить?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if market[imBuy-1] == 73:
        variableName = u"Книга"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Обучает заклинанию Кража Магии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Куп./прод. 3000бр|60ср/2100бр|42ср"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"Купить?)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))           
            
            
            
def textMagic(numerCeil):
    global botZaklinania 
    global hero
    heroPanel(hero)
    if botZaklinania[imHero][numerCeil-1] == 1:
        variableName = u"Пронзающая смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Мощное боевое заклинание 5 уровня "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"-300 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 200 маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 2:
        variableName = u"Телепортация"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Перемещение игрока в любое указанное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"место на карте"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 350 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        
    if botZaklinania[imHero][numerCeil-1] == 3:
        variableName = u"Доспехи Феникса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Базовая магия защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"+5 к защите на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 30 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 4:
        variableName = u"Кража магии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Отнимает всю ману противника и половину"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"отнятой маны прибавляет заклинателю"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 200 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if botZaklinania[imHero][numerCeil-1] == 5:
        variableName = u"Обман"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание хаоса 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо бездействует 1 ход"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Полезно применять против сильного"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"если у него нет защиты от базовых"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"заклинаний хаоса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
        variableName = u"Требует 50 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botZaklinania[imHero][numerCeil-1] == 6:
        variableName = u"Огненный шар"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Боевая магия Хаоса 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Создаёт огненный шар, летящий во врага"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"-30 здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"Требует 25 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
    if botZaklinania[imHero][numerCeil-1] == 7:
        variableName = u"Отравление"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Смерти 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо получает 15 урона каждый ход"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Заклинание действует до тех пор пока"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"не будет применено заклинание лечения,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"или рассеивание чар. Также действие"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
        variableName = u"магии снимается зельями  лечения"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))             
        variableName = u"Требует 30 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))                     
    if botZaklinania[imHero][numerCeil-1] == 8:
        variableName = u"Кровожадность"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Хаоса 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо получает +5 силы на 5 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 35 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 9:
        variableName = u"Лунный обряд"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Природы 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"+70 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 50 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 10:
        variableName = u"Мощь природы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Природы 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Улучшающее заклинание"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"+5 Силы +5 Защиты на 5 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 11:
        variableName = u"Могильный луч"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Смерти 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо получает 50 урона, а также"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"теряет защиту на 5 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"Защита = 0 -50 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 60 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))                
    if botZaklinania[imHero][numerCeil-1] == 12:
        variableName = u"Молния"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Боевая магия 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Разряд молнии отнимает 70 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 70 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 13:
        variableName = u"Печать Хаоса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Хаоса 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Продвинутое заклинание Хаоса, "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"действует подобно заклинанию"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"Отравление, более того отнимает всю"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"ману. -15 здоровья каждый ход"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
        variableName = u"Действует 10 ходов."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))             
        variableName = u"Требует 175 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))             
    if botZaklinania[imHero][numerCeil-1] == 14:
        variableName = u"Печать смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Смерти 7 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо умирает через 5 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Заклинание можно снять Рассеиванием"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"чар или артефактом подобного действия"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 230 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
    if botZaklinania[imHero][numerCeil-1] == 15:
        variableName = u"Поцелуй смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Смерти 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо получает 40 урона каждый ход"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Заклинание действует до тех пор пока"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"не будет применено рассеивание чар."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 150 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
    if botZaklinania[imHero][numerCeil-1] == 16:
        variableName = u"Проклятье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Смерти 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"На 10 ходов защита будет равна нулю"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 75 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 17:
        variableName = u"Пронзающий крик"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Боевая магия 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"-50 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 30 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[imHero][numerCeil-1] == 18:
        variableName = u"Регенерация"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Природы 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо получает 7 здоровья до тех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"пор пока полностью не восстановит"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"исходное здоровье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 40 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
    if botZaklinania[imHero][numerCeil-1] == 19:
        variableName = u"Сжигание маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Хаоса 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Сжигает всю ману противника"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 15 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
    if botZaklinania[imHero][numerCeil-1] == 20:
        variableName = u"Вампиризм"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Смерти 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Половина нанесённого оружием урона"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"преобразуется в здоровье. Действует"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"10 ходов."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 55 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
    if botZaklinania[imHero][numerCeil-1] == 21:
        variableName = u"Пока это восстановить скелетов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Это заклинание нужно исправить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
    if botZaklinania[imHero][numerCeil-1] == 22:
        variableName = u"Лечение"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Порядка 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Преобразует ману в здоровье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"+30 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"Требует 30 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
    if botZaklinania[imHero][numerCeil-1] == 23:
        variableName = u"Рассеять чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Порядка 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Рассеивает чары вокруг заклинателя "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 170 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
    if botZaklinania[imHero][numerCeil-1] == 24:
        variableName = u"Пленить душу"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Смерти 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Существо переходит в подчинение"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"заклинателя. Действует на существ"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"до 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 100 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))       

def visibleMagic(xMag, yMag, por, whoam): # Функция, отображающая заклинания
    global botZaklinania
    if botZaklinania[whoam][por] == 0:
        pix = pygame.image.load('Images/zero.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[whoam][por] == 100:
        pix = pygame.image.load('Images/attack.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[whoam][por] == 1:
        pix = pygame.image.load('Images/pronzauchaiaSmert.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[whoam][por] == 2:
        pix = pygame.image.load('Images/dobitIvoskresit.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[whoam][por] == 3:
        pix = pygame.image.load('Images/dospechiFenicha.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 4:
        pix = pygame.image.load('Images/krajaMagii.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 5:
        pix = pygame.image.load('Images/obman.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if botZaklinania[whoam][por] == 6:
        pix = pygame.image.load('Images/ognennaiaSfera.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 7:
        pix = pygame.image.load('Images/jad.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[whoam][por] == 8:
        pix = pygame.image.load('Images/krovojadnost.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))        
    if botZaklinania[whoam][por] == 9:
        pix = pygame.image.load('Images/lunniiObriad.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 10:
        pix = pygame.image.load('Images/mochPrirodi.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 11:
        pix = pygame.image.load('Images/mogilniiLuch.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[whoam][por] == 12:
        pix = pygame.image.load('Images/molnia.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if botZaklinania[whoam][por] == 13:
        pix = pygame.image.load('Images/pechatChaosa.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if botZaklinania[whoam][por] == 14:
        pix = pygame.image.load('Images/pechatSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if botZaklinania[whoam][por] == 15:
        pix = pygame.image.load('Images/poceluiSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))      
    if botZaklinania[whoam][por] == 16:
        pix = pygame.image.load('Images/prokliatie.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if botZaklinania[whoam][por] == 17:
        pix = pygame.image.load('Images/pronzauchiiKrik.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))         
    if botZaklinania[whoam][por] == 18:
        pix = pygame.image.load('Images/reincarnation.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[whoam][por] == 19:
        pix = pygame.image.load('Images/sjiganieMani.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[whoam][por] == 20:
        pix = pygame.image.load('Images/vampirizm.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[whoam][por] == 21:
        pix = pygame.image.load('Images/vosstanovitSkeletov.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 22:
        pix = pygame.image.load('Images/lechenie.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if botZaklinania[whoam][por] == 23:
        pix = pygame.image.load('Images/rasseiatChari.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[whoam][por] == 24:
        pix = pygame.image.load('Images/plenitDuchu.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))              
                                
def visibleInventar(xInv, yInv, porNom, whoam): # Функция, отображающая заклинания
    global botInventar
    if botInventar[whoam][porNom] == 0:
        pix = pygame.image.load('Images/zero.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 1:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 2:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 3:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 4:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 5:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))                       
    if botInventar[whoam][porNom] == 6:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 7:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 8:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 9:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 10:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))                
    if botInventar[whoam][porNom] == 11:
        pix = pygame.image.load('Images/zelieVostanovlenia.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 12:
        pix = pygame.image.load('Images/zelieRasseivania.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))   
    if botInventar[whoam][porNom] == 13:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 14:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 15:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 16:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))           
    if botInventar[whoam][porNom] == 17:
        pix = pygame.image.load('Images/zelieZaciti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 18:
        pix = pygame.image.load('Images/zelieZaciti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 19:
        pix = pygame.image.load('Images/zelieZaciti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))            
    if botInventar[whoam][porNom] == 20:
        pix = pygame.image.load('Images/zelieLovkosti.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 21:
        pix = pygame.image.load('Images/zelieLovkosti.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 22:
        pix = pygame.image.load('Images/zelieLovkosti.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))          
    if botInventar[whoam][porNom] == 23:
        pix = pygame.image.load('Images/zelieUdachi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 24:
        pix = pygame.image.load('Images/zelieUdachi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 25:
        pix = pygame.image.load('Images/zelieUdachi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))        
    if botInventar[whoam][porNom] == 26:
        pix = pygame.image.load('Images/axe.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))   
    if botInventar[whoam][porNom] == 27:
        pix = pygame.image.load('Images/axe1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 28:
        pix = pygame.image.load('Images/axe2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[whoam][porNom] == 29:
        pix = pygame.image.load('Images/axe3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 30:
        pix = pygame.image.load('Images/axe4.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 31:
        pix = pygame.image.load('Images/axe5.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 32:
        pix = pygame.image.load('Images/axe6.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 33:
        pix = pygame.image.load('Images/book.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 34:
        pix = pygame.image.load('Images/book1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 35:
        pix = pygame.image.load('Images/book2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 36:
        pix = pygame.image.load('Images/book3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 37:
        pix = pygame.image.load('Images/book4.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 38:
        pix = pygame.image.load('Images/book5.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 39:
        pix = pygame.image.load('Images/book6.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 40:
        pix = pygame.image.load('Images/book7.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 41:
        pix = pygame.image.load('Images/book8.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 42:
        pix = pygame.image.load('Images/book9.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[whoam][porNom] == 43:
        pix = pygame.image.load('Images/bot1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 44:
        pix = pygame.image.load('Images/bot2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 45:
        pix = pygame.image.load('Images/bot3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 46:
        pix = pygame.image.load('Images/helmet.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 47:
        pix = pygame.image.load('Images/helmet1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 48:
        pix = pygame.image.load('Images/helmet2.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 49:
        pix = pygame.image.load('Images/helmet3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 50:
        pix = pygame.image.load('Images/helmet4.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 51:
        pix = pygame.image.load('Images/helmet5.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 52:
        pix = pygame.image.load('Images/jar.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 53:
        pix = pygame.image.load('Images/ojerelie.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 54:
        pix = pygame.image.load('Images/posohProzrenia.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 55:
        pix = pygame.image.load('Images/posohSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))        
    if botInventar[whoam][porNom] == 56:
        pix = pygame.image.load('Images/posohSveta.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))        
    if botInventar[whoam][porNom] == 57:
        pix = pygame.image.load('Images/posohVechnoiJizni.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 58:
        pix = pygame.image.load('Images/posohVoli.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))      
    if botInventar[whoam][porNom] == 59:
        pix = pygame.image.load('Images/runesBraslet.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[whoam][porNom] == 60:
        pix = pygame.image.load('Images/sword.jpeg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 61:
        pix = pygame.image.load('Images/sword1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[whoam][porNom] == 62:
        pix = pygame.image.load('Images/sword2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[whoam][porNom] == 63:
        pix = pygame.image.load('Images/sword3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[whoam][porNom] == 64:
        pix = pygame.image.load('Images/sword4.gif') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[whoam][porNom] == 65:
        pix = pygame.image.load('Images/sword5.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[whoam][porNom] == 66:
        pix = pygame.image.load('Images/usilenniiPosohVechnoiJizni.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))   
    if botInventar[whoam][porNom] == 67:
        pix = pygame.image.load('Images/hammer.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[whoam][porNom] == 68:
        pix = pygame.image.load('Images/hammer1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 69:
        pix = pygame.image.load('Images/hammer2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[whoam][porNom] == 70:
        pix = pygame.image.load('Images/hammer3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 71:
        pix = pygame.image.load('Images/book10.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 72:
        pix = pygame.image.load('Images/book11.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[whoam][porNom] == 73:
        pix = pygame.image.load('Images/book12.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))

def printMagic(numberMagic):                                # Отображаем магические способности
    if numberMagic == 0: visibleMagic(16,548,0,imHero)
    if numberMagic == 1: visibleMagic(84,548,1,imHero)
    if numberMagic == 2: visibleMagic(152,548,2,imHero)
    if numberMagic == 3: visibleMagic(220,548,3,imHero)
    if numberMagic == 4: visibleMagic(16,616,4,imHero)
    if numberMagic == 5: visibleMagic(84,616,5,imHero)
    if numberMagic == 6: visibleMagic(152,616,6,imHero)
    if numberMagic == 7: visibleMagic(220,616,7,imHero)
    if numberMagic == 8: visibleMagic(16,684,8,imHero)
    if numberMagic == 9: visibleMagic(84,684,9,imHero)
    if numberMagic == 10: visibleMagic(152,684,10,imHero)
    if numberMagic == 11: visibleMagic(220,684,11,imHero)
    if numberMagic == 12: visibleMagic(16,752,12,imHero)
    if numberMagic == 13: visibleMagic(84,752,13,imHero)
    if numberMagic == 14: visibleMagic(152,752,14,imHero)
    if numberMagic == 15: visibleMagic(220,752,15,imHero)
         
def printInventar(numberInventar):                                # Отображаем инвентарь
    if numberInventar == 0: visibleInventar(772,548,0,imHero)
    if numberInventar == 1: visibleInventar(840,548,1,imHero)
    if numberInventar == 2: visibleInventar(908,548,2,imHero)
    if numberInventar == 3: visibleInventar(976,548,3,imHero)
    if numberInventar == 4: visibleInventar(772,616,4,imHero)
    if numberInventar == 5: visibleInventar(840,616,5,imHero)
    if numberInventar == 6: visibleInventar(908,616,6,imHero)
    if numberInventar == 7: visibleInventar(976,616,7,imHero)
    if numberInventar == 8: visibleInventar(772,684,8,imHero)
    if numberInventar == 9: visibleInventar(840,684,9,imHero)
    if numberInventar == 10: visibleInventar(908,684,10,imHero)
    if numberInventar == 11: visibleInventar(976,684,11,imHero)
    if numberInventar == 12: visibleInventar(772,752,12,imHero)
    if numberInventar == 13: visibleInventar(840,752,13,imHero)
    if numberInventar == 14: visibleInventar(908,752,14,imHero)
    if numberInventar == 15: visibleInventar(976,752,15,imHero) 

def doebaca(hehmda):  #Функция отображающая информацию об объектах и позволяющая с ними взаимодействовать
    global botType, botStep, xBot, yBot, botExpirience, botLvl, botRasa, botZaklinania, botVozdeistvie, botInventar, botIshZdorovie, botZdorovie, botMana, botIshMana, botSila, botLovkost, botYdacha
    global botZachita, botHod, world, botNumer, botVariant, botAlgoritm, botLocation, attack, zakl, botDeistvie, posohSmerti, posohProzrenia, posohSveta, posohVoli, posohVechnoiJizni, yaNaRinke, yes, no, invent, hijinaMaga, zadanieMaga, tmpMagExp, drujbaMaga
    
    n = 0
    yes = no = invent = 0
    pygame.draw.rect(sc, (255, 255, 255), (405, 558, 365, 896)) 
    
    ktoZdesVrag = 0
    for ktoZdesVrag in range(50): # Определяем номер бота по клетке
        if botLocation[ktoZdesVrag] == hehmda:
            if ktoZdesVrag != imHero:
                variableName = u"Здоровье: " + str(botZdorovie[ktoZdesVrag]) + "/" + str(botIshZdorovie[ktoZdesVrag])
                nameObj = textNameHero.render(variableName, False, (0, 255, 0)) 
                sc.blit(nameObj,(440, 760))
                if posohProzrenia == 1: # Если активировали посох прозрения
                    variableName = u"Мана: " + str(botMana[ktoZdesVrag]) + "/" + str(botIshMana[ktoZdesVrag])
                    nameObj = textNameHero.render(variableName, False, (0, 255, 255)) 
                    sc.blit(nameObj,(440, 780))
                    variableName = u"Сила: " + str(botSila[ktoZdesVrag])
                    nameObj = textNameHero.render(variableName, False, (255, 0, 0)) 
                    sc.blit(nameObj,(440, 800))
                    visibleMagic(16,548,0,ktoZdesVrag)
                    visibleMagic(84,548,1,ktoZdesVrag)
                    visibleMagic(152,548,2,ktoZdesVrag)
                    visibleMagic(220,548,3,ktoZdesVrag)
                    visibleMagic(16,616,4,ktoZdesVrag)
                    visibleMagic(84,616,5,ktoZdesVrag)
                    visibleMagic(152,616,6,ktoZdesVrag)
                    visibleMagic(220,616,7,ktoZdesVrag)
                    visibleMagic(16,684,8,ktoZdesVrag)
                    visibleMagic(84,684,9,ktoZdesVrag)
                    visibleMagic(152,684,10,ktoZdesVrag)
                    visibleMagic(220,684,11,ktoZdesVrag)
                    visibleMagic(16,752,12,ktoZdesVrag)
                    visibleMagic(84,752,13,ktoZdesVrag)
                    visibleMagic(152,752,14,ktoZdesVrag)
                    visibleMagic(220,752,15,ktoZdesVrag)

                    visibleInventar(772,548,0,ktoZdesVrag)
                    visibleInventar(840,548,1,ktoZdesVrag)
                    visibleInventar(908,548,2,ktoZdesVrag)
                    visibleInventar(976,548,3,ktoZdesVrag)
                    visibleInventar(772,616,4,ktoZdesVrag)
                    visibleInventar(840,616,5,ktoZdesVrag)
                    visibleInventar(908,616,6,ktoZdesVrag)
                    visibleInventar(976,616,7,ktoZdesVrag)
                    visibleInventar(772,684,8,ktoZdesVrag)
                    visibleInventar(840,684,9,ktoZdesVrag)
                    visibleInventar(908,684,10,ktoZdesVrag)
                    visibleInventar(976,684,11,ktoZdesVrag)
                    visibleInventar(772,752,12,ktoZdesVrag)
                    visibleInventar(840,752,13,ktoZdesVrag)
                    visibleInventar(908,752,14,ktoZdesVrag)
                    visibleInventar(976,752,15,ktoZdesVrag) 
                    
            break        
    
        
    if zakl > 0 and ktoZdesVrag != 49:
        if zakl == 1: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 2: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 3: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 4: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 5: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 6: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 7: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 8: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 9: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 10: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 11: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 12: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 13: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 14: botKoldun(imHero,zakl-1,ktoZdesVrag)
        if zakl == 15: botKoldun(imHero,zakl-1,ktoZdesVrag)
                        
        zakl = 0
        attack = 0
    
    
    
    ktoZdesVrag = 0    
    
                
    if posohSveta == 1: # Посох света
        for ktoZdesVrag in range(100): # Определяем номер бота по клетке
            if botLocation[ktoZdesVrag] == hehmda:
                break  

        botDeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botVozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botMana[imHero] -= 110
        botZdorovie[ktoZdesVrag] += 100
        botExpirience[imHero] += 50
        posohSveta= 0
    
    if posohSmerti == 1:
        for ktoZdesVrag in range(100): # Определяем номер бота по клетке
            if botLocation[ktoZdesVrag] == hehmda:
                break  
        
        botMana[imHero] -= 100
        botZdorovie[ktoZdesVrag] -= 200
        botHod[imHero] -= 1
        botExpirience[imHero] += 50
        posohSmerti = 0
        if botZdorovie[ktoZdesVrag] <= 0: 
            otdaiLut(imHero, ktoZdesVrag)
            ubiraemTrup(ktoZdesVrag)
        heroPanel(hero)
        
    if attack == 1 and botHod[imHero] > 0:  # Тут мы атакуем ботов
            for ktoZdesVrag in range(200): # Определяем номер бота по клетке
                if botLocation[ktoZdesVrag] == hehmda:
                    if botLocation[imHero] == botLocation[ktoZdesVrag]+1 or botLocation[imHero] == botLocation[ktoZdesVrag]-1 or botLocation[imHero] == botLocation[ktoZdesVrag]+31 or botLocation[imHero] == botLocation[ktoZdesVrag]+32 or botLocation[imHero] == botLocation[ktoZdesVrag]+33 or botLocation[imHero] == botLocation[ktoZdesVrag]-31 or botLocation[imHero] == botLocation[ktoZdesVrag]-32 or botLocation[imHero] == botLocation[ktoZdesVrag]-33:
                        break 
            botHod[imHero] -= 1
            botZdorovie[ktoZdesVrag] -= botSila[imHero] + botAttack[imHero] - botZachita[ktoZdesVrag]
            botExpirience[imHero] += botSila[imHero] # Повышаем опыт
            attack = 0
            if botZdorovie[ktoZdesVrag] <= 0 and zakl == 0:
                randomMoney = int(random.random()*10) # Вероятность выпадения ресурсов: серебра и бронзы
                randomBronza = int(random.random()*70) * botLvl[ktoZdesVrag]
                randomSerebro = int(random.random()*5) * botLvl[ktoZdesVrag]
                if randomMoney == 4 or randomMoney == 5 or randomMoney == 6 or randomMoney == 7 or randomMoney == 8 or randomMoney == 9:
                    botBronza[imHero] += randomBronza
                if randomMoney == 2 or randomMoney == 3:
                    botSerebro[imHero] += randomSerebro  
                botExpirience[imHero] += int(botIshZdorovie[ktoZdesVrag] / 2)
                otdaiLut(imHero, ktoZdesVrag)
                ubiraemTrup(ktoZdesVrag)  
            heroPanel(hero)
            worldUpdate()        
            attack = 0
    
    if botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
        # Тут мы взаимодействуем с Хижиной Мага
        hijinaMaga = 1
        for n in range(15):     
            if n == 0: xIn = 772; yIn = 548
            if n == 1: xIn = 840; yIn = 548
            if n == 2: xIn = 908; yIn = 548
            if n == 3: xIn = 976; yIn = 548
            if n == 4: xIn = 772; yIn = 616
            if n == 5: xIn = 840; yIn = 616
            if n == 6: xIn = 908; yIn = 616
            if n == 7: xIn = 976; yIn = 616
            if n == 8: xIn = 772; yIn = 684
            if n == 9: xIn = 840; yIn = 684
            if n == 10: xIn = 908; yIn = 684
            if n == 11: xIn = 976; yIn = 684
            if n == 12: xIn = 772; yIn = 752
            if n == 13: xIn = 840; yIn = 752
            if n == 14: xIn = 908; yIn = 752
            if n == 15: xIn = 976; yIn = 752
            pix = pygame.image.load('Images/zero.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xIn,yIn))
            
        pix = pygame.image.load('Images/47641705.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (772,548))
        pix = pygame.image.load('Images/wizard.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (840,548))
        pix = pygame.image.load('Images/76611378.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (908,548))
        if zadanieMaga == 1:  # Тут мы обрабатываем условие выполнение заданий Мага
            for n in range(15):
                if botInventar[imHero][n] == 52:
                    tmpMagExp = 0
                    zadanieMaga = 2
                    botBronza[imHero] += 1000
                    botInventar[imHero][n] = 0
                    drujbaMaga += 1
                    break
        if zadanieMaga == 3:  
            for n in range(15):
                if botInventar[imHero][n] == 29:
                    tmpMagExp = 0
                    zadanieMaga = 4
                    botSerebro[imHero][n] += 7
                    botInventar[imHero][n] = 0
                    drujbaMaga += 1
                    break                    
    
                     
    if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 177 or botLocation[imHero] == 176 or botLocation[imHero] == 178 or botLocation[imHero] == 113 or botLocation[imHero] == 112 or botLocation[imHero] == 114:
        if world[hehmda] == 8:
            yaNaRinke = 1  # Это взаимодействие с рынком 
            variableName = u"Смотреть предложения - (Да)"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 660))
            variableName = u"Продать инвентарь - (Нет)"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 680))
            
            pix = pygame.image.load('Images/yes.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (462,786))    
    
            pix = pygame.image.load('Images/no.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (530,786))
            
    if world[hehmda] == 3:
        pix = pygame.image.load('Images/jilZelievara.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Жилище зельевара"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"В этом доме живёт потомственный мастер зелья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580)) 
        variableName = u"У него можно приобрести магические зелья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"под различные нужны."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"Ты можешь взять задание у зельевара,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"выполнив которые ты получишь золотые монеты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if world[hehmda] == 4:
        pix = pygame.image.load('Images/lachugaShamana.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Лачуга шамана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"В этой хижине живёт шаман племени Яки."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"За символическую сумму он обучит основам"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"магии и некоторым заклинаниям. Здесь "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"также приобрести магические артефакты."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Шаман может предложить тебе работу,если"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
        variableName = u"ты справишься он отплатит тебе серебром"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if world[hehmda] == 5:
        pix = pygame.image.load('Images/hijinaMaga.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Хижина мага"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"В этой хижине живёт старый маг, который"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"способен обучить вас основам магии, также"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"у него можно купить и продать некоторые"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"магические артефакты и зелья."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"У мага можно получить задание."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
        variableName = u"Платит маг обычно бронзой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if world[hehmda] == 6:
        pix = pygame.image.load('Images/kuznica.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Кузница"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"В этой кузнице трудятся мастера своего"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"дела. Здесь ты найдёшь доспехи и оружие"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"У кузнецов можно получить задание и"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"выполнив его получить редкие артефакты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
    if world[hehmda] == 8:
        pix = pygame.image.load('Images/market.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Рынок"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сюда ведут все дороги - на рынок."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Тут найдутся абсолютно все вещи первой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"необходимости. На рынке ты можешь "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"получить деньги подрабатывая у торговцев"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))     
    if world[hehmda] == 10:
        pix = pygame.image.load('Images/portal.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Портал"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Зайдя в него можно телепортироваться"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"в долину проклятых земель. Там ты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"найдёшь гробницу с несметными "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"сокровищами. Но она хорошо охраняется"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"нежитью. Живые в тех землях находят"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
        variableName = u"только смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))    
    if world[hehmda] == 15:
        pix = pygame.image.load('Images/city.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Городские врата"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"По ту сторону стен находится город "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"короля Альбрехта. В нём иожно нанять"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"рекрутов, потожить деньги в банк "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"и ещё много чего. У короля есть сокровища"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"которые охраняет свита отборных бойцов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 16:
        pix = pygame.image.load('Images/taverna.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Таверна"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Это находка, оазис по среди холодных гор"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Тут ты можешь нанять пару бойцов для"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"похода, получить задание, купить редкие "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"предметы и сыграть в кости."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Так же здесь ты можешь создать задание"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
        variableName = u"Возможно кто-то за него возмётся"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))  
    if world[hehmda] == 100:
        pix = pygame.image.load('Images/elf1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Эльф 1 уровня "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Рядовой боец расы эльфов. "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"В одиночку почти не представляет угрозы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Не обладает магическими навыками. "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
    if world[hehmda] == 101:
        pix = pygame.image.load('Images/elf2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Эльф 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Рядовой боец расы эльфов."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Обладает магией лечения 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if world[hehmda] == 102:
        pix = pygame.image.load('Images/elf3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Эльф 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Хороший пехотинец. "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Обладает магией лечения 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Достаточно сильная боевая единица "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))          
    if world[hehmda] == 103:
        pix = pygame.image.load('Images/gnoll1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гнолл 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабый монстр. Нападает на всех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"кого видит не раздумывая."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Существо не обладает магией "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if world[hehmda] == 104:
        pix = pygame.image.load('Images/gnoll2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гнолл 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабый монстр. Нападает на всех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"кого видит без раздумий."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Существо не обладает магией "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if world[hehmda] == 105:
        pix = pygame.image.load('Images/gnoll3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гнолл 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Относительно сильное существо"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Агрессивный и опасный монстр"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if world[hehmda] == 106:
        pix = pygame.image.load('Images/gnom1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гном 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Крепкий боец расы гномов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
    if world[hehmda] == 107:
        pix = pygame.image.load('Images/gnom2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гном 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Крепкий боец расы гномов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))     
    if world[hehmda] == 108:
        pix = pygame.image.load('Images/gnom3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Гном 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сильный воин расы гномов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Обладает магией лечения 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))      
    if world[hehmda] == 109:
        pix = pygame.image.load('Images/gnom4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гном 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сильный воин расы гномов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Обладает магией лечения 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"И заклинанием Рассеять чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if world[hehmda] == 110:
        pix = pygame.image.load('Images/goblin.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Гоблин"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Мирное существо, торговец-алхимик"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"У гоблина можно купить различные зелья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"Не обладает магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if world[hehmda] == 111:
        pix = pygame.image.load('Images/goblin1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Гоблин 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабый воин расы гоблинов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"Иногда у него можно купить артефакты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))     
    if world[hehmda] == 112:
        pix = pygame.image.load('Images/goblin2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гоблин 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабый воин расы гоблинов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"Иногда у него можно купить артефакты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))          
    if world[hehmda] == 113:
        pix = pygame.image.load('Images/goblin3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Гоблин 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Самый сильный представитель расы гоблинов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"Но шутки с ним плохи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if world[hehmda] == 114:
        pix = pygame.image.load('Images/hermit1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Отшельник 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Демонопоклонник расы людей"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Владеет навыками некромантии и способен"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"из почти мёртвого существа сделать "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"скелета, подчиняющегося его воле "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))       
    if world[hehmda] == 115:
        pix = pygame.image.load('Images/hermit2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Отшельник 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Ученик некроманта"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Способен создавать скелетов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"А также владеет магией защиты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if world[hehmda] == 116:
        pix = pygame.image.load('Images/hermit3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Отшельник 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Один из лучших учеников некроманта"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Владеет боевой и защитной магиями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))            
        variableName = u"А также способен создавать скелетов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))     
    if world[hehmda] == 117:
        pix = pygame.image.load('Images/headHunter.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Охотник за головами"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Боец-одиночка 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Живёт за счёт своих жертв, принося их"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"головы своим заказчикам."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))            
        variableName = u"Лучше не стоять у этого человека на пути"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u" Владеет магией лечения 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if world[hehmda] == 118:
        pix = pygame.image.load('Images/human.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Человек"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Мирный торговец и строитель"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Его можно нанять для постройки своей "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"крепости. Также иногда у него можно"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))            
        variableName = u"купить оружие или доспехи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
    if world[hehmda] == 119:
        pix = pygame.image.load('Images/monster1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Проклятый морлок"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Говорят, что эти морлоки - неудачный"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"эксперимент тёмных колдунов. Слабое"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"существо, нападающее на всех без разбора"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"Не владеет магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))     
    if world[hehmda] == 120:
        pix = pygame.image.load('Images/monster2.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Проклятый гнолл"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Тёмные колдуны пытались из него сделать"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"послушного бойца своей армии, но всё"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"было напрасно. Существо как и раньше"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"вымещает свою агрессию на всех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
    if world[hehmda] == 121:
        pix = pygame.image.load('Images/monster3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Проклятый носорог"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Порождение тёмных колдунов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Опасное существо, которому чужды расовые"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"предрассудки, жестоко убивает всех"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"однаково яростно."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
    if world[hehmda] == 122:
        pix = pygame.image.load('Images/monster4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Дракон"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Опасное существо 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Редкая удача встретить такого дракона"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Но лучше наблюдать за его полётом"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"из далека и не приближаться. Одолеть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"такого монстра не каждому под силу"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if world[hehmda] == 123:
        pix = pygame.image.load('Images/morlok1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Морлок 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Гадкая, болтная тварь"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не обладает магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
    if world[hehmda] == 124:
        pix = pygame.image.load('Images/morlok2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Морлок 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Гадкая, болтная тварь"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Слабое существо не обладающее магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))      
    if world[hehmda] == 125:
        pix = pygame.image.load('Images/morlok3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Морлок 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Гадкая, болтная тварь"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Слабое существо не обладающее магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
    if world[hehmda] == 126:
        pix = pygame.image.load('Images/naemnik1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Наёмник 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Солдат армии Короля Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"В одиночку почти беззащитен, однако"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"группой из 3-5 таких бойцов можно идти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"на серьёзных монстров. Его можно нанять"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = u"в городе или таверне если он там будет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
    if world[hehmda] == 127:
        pix = pygame.image.load('Images/naemnik2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Наёмник 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сержант армии Короля Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Допускается Королём к охране стен замка"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"но может и патрулировать город вместе с"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"остальными солдатами. Его можно нанять в"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"городе или таверне."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if world[hehmda] == 128:
        pix = pygame.image.load('Images/naemnik3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Наёмник 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Лейтенант армии Короля Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Допускается к охране Короля и замка его"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"величества. Сильный пехотинец, которого"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"можно нанять только в городе"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
    if world[hehmda] == 129:
        pix = pygame.image.load('Images/naemnik4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Наёмник 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Капитан армии Короля Альбрехта."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Гордость королевской пехоты и серьёзный"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"боец. В одиночку способен одолеть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"десяток скелетов."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
    if world[hehmda] == 130:
        pix = pygame.image.load('Images/nekromant.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Некромант"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Тёмный колдун 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Верный слуга демонов, обладающий"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"опасной магией. Таким волшебникам"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"позволено иметь при себе очень ценные"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
        variableName = u"магические предметы. Но не вздумайте"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
        variableName = u"пытаться у него их отнять"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if world[hehmda] == 131:
        pix = pygame.image.load('Images/nepobedimii.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Непобедимый 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Грозный страж гробницы проклятых земель"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Опасное и свирепое существо"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
    if world[hehmda] == 132:
        pix = pygame.image.load('Images/nepobedimii1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Непобедимый 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Страж гробницы проклятых земель"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Не каждому такой монстр по плечу"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Принадлежит к классу потомков проклятых"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
    if world[hehmda] == 133:
        pix = pygame.image.load('Images/ogr1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Огр 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Злобный великан-людоед"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Отностиельно слабое существо не обладающее"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
    if world[hehmda] == 134:
        pix = pygame.image.load('Images/ogr2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Огр 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Злобный великан-людоед"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Отностиельно слабое существо"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"не обладающее магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
    if world[hehmda] == 135:
        pix = pygame.image.load('Images/okylt.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Оккультист"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Тёмный маг 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Человек, достаточно хорошо обладевший"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"магией мёртвых. Знает множество"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
        variableName = u"опасных заклинаний, на такого колдуна"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"лучше идти группой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 136:
        pix = pygame.image.load('Images/ork1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Орк 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Относительно слабый воин расы орков"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Орков можно нанять в таверне или "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"в пустошах."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))        
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
    if world[hehmda] == 137:
        pix = pygame.image.load('Images/ork2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Орк 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Относительно слабый воин расы орков"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Пехотинец клана Кровавых Топоров"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Орков можно нанять в таверне или "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"в пустошах."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Не обладает магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
    if world[hehmda] == 138:
        pix = pygame.image.load('Images/ork3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Орк 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Боец расы орков. Пехотинец клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Кровавых Топоров. Достойный противник"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Орков можно нанять в таверне или "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"в пустошах."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
    if world[hehmda] == 139:
        pix = pygame.image.load('Images/ork4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Орк 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Боец расы орков. Пехотинец клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580)) 
        variableName = u"Кровавых Топоров. Достойный противник"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Орков можно нанять в таверне или "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))        
        variableName = u"в пустошах."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
    if world[hehmda] == 140:
        pix = pygame.image.load('Images/ork5.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Орк 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Грозный боец расы орков из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Кровавых Топоров. Он свиреп и безпощаден."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Орков можно нанять в таверне или "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"в пустошах."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if world[hehmda] == 141:
        pix = pygame.image.load('Images/ork6.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Орк 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Грозный боец расы орков из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Кровавых Топоров. Не обладает "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))      
    if world[hehmda] == 142:
        pix = pygame.image.load('Images/ork7.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Орк 7 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Грозный боец расы орков из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Кровавых Топоров. Ему нет равных."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
                
    if world[hehmda] == 143:
        pix = pygame.image.load('Images/ork-shaman.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Орк-шаман"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Колдун клана Кровавых Топоров"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Опасный маг 3 уровня, владеющий"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"боевыми и защитными заклинаниями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
    if world[hehmda] == 144:
        pix = pygame.image.load('Images/otstupnik.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Оккультист"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Грозный волшебник 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Такие маги часто носят при себе"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"различные книги тёмных заклинаний."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"Однако забрать их у него не просто"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
    if world[hehmda] == 145:
        pix = pygame.image.load('Images/razboinik.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Разбойник"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Принадлежит к классу хаотичных"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Обычно за его голову в Королевстве"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"дают вознаграждение. Существо не "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
    if world[hehmda] == 146:
        pix = pygame.image.load('Images/grabitel.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Грабитель"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Принадлежит к классу хаотичных"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Обычно за его голову в Королевстве"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"можно получить вознаграждение."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
    if world[hehmda] == 147:
        pix = pygame.image.load('Images/redFireHolem.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Красный огненный голем"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сильное существо 4 уровня, созданное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии посоха вечной жизни"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))    
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))      
    if world[hehmda] == 148:
        pix = pygame.image.load('Images/skelet1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Скелет 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабое существо, созданное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии. Покуда колдовские"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"чары связывают его кости, этот скелет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"подчиняются своему хозяину"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 149:
        pix = pygame.image.load('Images/skelet2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Скелет 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабое существо, созданное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии. Покуда колдовские"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"чары связывают его кости, этот скелет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"подчиняются своему хозяину"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
    if world[hehmda] == 150:
        pix = pygame.image.load('Images/skelet3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Скелет 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Бессмертное существо, созданное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии. Покуда колдовские"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"чары связывают его кости, этот скелет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"подчиняется воле своего хозяина"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 151:
        pix = pygame.image.load('Images/skelet4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Скелет 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Бессмертное существо, созданное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии. Покуда колдовские"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"чары связывают его кости, этот скелет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"подчиняется воле своего хозяина"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
    if world[hehmda] == 152:
        pix = pygame.image.load('Images/skelet5.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Скелет 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Верный боец некроманта, созданный"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии посоха Вечной Жизни."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Нужно быть достаточно сильным колдуном"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"чтобы создать такое существо"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 153:
        pix = pygame.image.load('Images/skelet6.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Скелет 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Верный боец некроманта, созданный"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии посоха Вечной Жизни."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Опасное существо, не каждый сможет ему"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"противостоять"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 154:
        pix = pygame.image.load('Images/skelet7.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Скелет 7 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сильное существо, созданное"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"с помощью магии посоха Вечной Жизни."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Этот скелет способен в одиночку"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"разделаться с пятью наёмниками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
    if world[hehmda] == 155:
        pix = pygame.image.load('Images/skelet8.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Скелет 8 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Самое опасное существо, которое может"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"быть создано посохом Вечной Жизни."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Этот скелет способен в одиночку"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"разделаться с десятком наёмников"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Не обладает магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
    if world[hehmda] == 156:
        pix = pygame.image.load('Images/soulCatcher.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Душекрад"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Нежить 10 уровня, правая рука демонов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Этот мертвец чудовищно силён"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"и владеет множеством темных заклинаний"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
    if world[hehmda] == 157:
        pix = pygame.image.load('Images/strannik.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Странник"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Не один десяток лет этот старик"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"блуждает по мирам. Не совсем ясно что"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"им движет, говорят что он раньше"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
        variableName = u"был шаманом, пока духи не овладели"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
        variableName = u"уго разумом и не свели с ума."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
        variableName = u"Относительно сильный человек 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
        variableName = u"Владеет заклинанием Обман"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
        variableName = u"У этого старца можно купить артефакты"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 720))  
    if world[hehmda] == 158:
        pix = pygame.image.load('Images/troll1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Тролль 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Относительно слабый воин из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Острого Копья. Не владеет магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
    if world[hehmda] == 159:
        pix = pygame.image.load('Images/troll2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Тролль 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Относительно слабый воин из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Острого Копья. Не владеет магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
    if world[hehmda] == 160:
        pix = pygame.image.load('Images/troll3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Тролль 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Бесстрашный боец из клана Острого"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Копья. Воин не обладает магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
    if world[hehmda] == 161:
        pix = pygame.image.load('Images/troll4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Тролль 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Бесстрашный боец из клана Острого"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Копья. Сильный и опасный воин."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Не владеет магическими способностями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if world[hehmda] == 162:
        pix = pygame.image.load('Images/troll5.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Тролль 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сильный воин и колдун из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Острого Копья. Владеет заклинаниями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Кража магии, Молния и Доспехи Феникса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
    if world[hehmda] == 163:
        pix = pygame.image.load('Images/troll6.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Тролль 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Сильный воин и колдун из клана"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Острого Копья. Владеет заклинаниями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Кража магии, Молния и Доспехи Феникса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"Весьма опасный противник."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
    if world[hehmda] == 164:
        pix = pygame.image.load('Images/vampir.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Вампир"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Нежить 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"В одиночку он представляет серьёзную"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"угрозу из-за способности Вампиризм"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"которым он восстанавливает своё"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"здоровье. "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if world[hehmda] == 165:
        pix = pygame.image.load('Images/wizard.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Колдун"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Белый Маг 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Отголосок славных лет, когда Гильдия"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Белых Магов имела серьёзный вес в"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"Королевстве. Теперь маги скитаются"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"по миру в поисках магического"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))    
        variableName = u"артефакта, способного сплотить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))   
        variableName = u"Гильдию и снова подчинить Королевство"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700)) 
    if world[hehmda] == 166:
        pix = pygame.image.load('Images/womanElf1.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Женщина-эльф 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабый воин расы эльфов."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Страж магического леса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Не владеет магическими навыками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
    if world[hehmda] == 167:
        pix = pygame.image.load('Images/womanElf2.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Женщина-эльф 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Слабый воин расы эльфов. Страж "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Магического леса. Не обладает магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
    if world[hehmda] == 168:
        pix = pygame.image.load('Images/womanElf3.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Женщина-эльф 3 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Целительница"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Относительно сильный воин. Владеет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"заклинанием Лунный обряд"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
    if world[hehmda] == 169:
        pix = pygame.image.load('Images/womanElf4.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Женщина-эльф 4 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Ученик жрицы Древа Мудрости."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))     
        variableName = u"Сильный воин владеющий боевой и"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"лечебной магией"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  
    if world[hehmda] == 170:
        pix = pygame.image.load('Images/womanElf5.jpeg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Женщина-эльф 5 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Адепт жрицы Древа Мудрости."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Она является сильным бойцом магом."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"Владеет заклинаниями боевой и защитной"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"магии."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
    if world[hehmda] == 171:
        pix = pygame.image.load('Images/womanElf6.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548)) 
        variableName = u"Женщина-эльф 6 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Адепт жрицы Древа Мудрости."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Она является сильным бойцом и опасным"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"магом. Владеет заклинаниями боевой"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"и защитной магии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
    if world[hehmda] == 172:
        pix = pygame.image.load('Images/womanElf7.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Женщина-эльф 7 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Жрица Древа Мудрости."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Боевой маг расы эльфов. в мире нет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"женщин опаснее этих эльфиек"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"Владеет заклинанием Пронзающая смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"а также защитной и лечебной магиями"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if world[hehmda] == 173:
        pix = pygame.image.load('Images/dux.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Дух-союзник"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот дух способен наделить магией и "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"тайным знанием всех к кому он благосклонен"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"Не смотря на устрашающий вид,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"дух-союзник никогда не причинит вреда"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"существам этого мира."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if world[hehmda] == 174:
        pix = pygame.image.load('Images/dux.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Дух смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Беспощадный и неумолимый дух,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"способный уничтожить одним лишь"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"прикосновением"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"Дух будет уничтожать всё на своём"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"пути пока не насытиться смертью"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))                
    if world[hehmda] == 50:
        pix = pygame.image.load('Images/akami.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Аками"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Эльф магического леса"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"В прошлом был жрецом Древа Мудрости,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"но был лишён своих регалий. Теперь он"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"вольный странник, ищущий своё"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"место в этом мире"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))   
    if world[hehmda] == 51:
        pix = pygame.image.load('Images/akami.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Артес"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Рыцарь смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Некогда подававший надежды паладин"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"решил прибегнуть к помощи тёмной"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"магии, дабы обрести силу и власть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"После такого его изгнали из Ордена"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
        variableName = u"Света и Артес стал называть себя"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))   
        variableName = u"Рыцарем Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 790))  
    if world[hehmda] == 52:
        pix = pygame.image.load('Images/deathOwner.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Владыка Смерти"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Некромант, решивший поторопить судьбу."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Он решил умерщвить своё тело раньше"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"чем ему было положено. И вместе с"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))   
        variableName = u"положенным некроманту бессмертием "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"обрёл новое тело состоящее только"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))         
        variableName = u"из костей."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))  
    if world[hehmda] == 53:
        pix = pygame.image.load('Images/akami.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = u"Детерок"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот эльф выбрал судьбу скитальца."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Уже более десяти лет он бродит по"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = u"миру в поисках новых приключений"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))  

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
    if iconka == 173: pix = pygame.image.load('Images/dux_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap)) 
    if iconka == 174: pix = pygame.image.load('Images/dux_32.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
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

def heroPanel(myHero): # Рисуем панель героя с его картинкой и параметрами
    global botExpirience
    global botLvl
    global botRasa
    global botZaklinania
    global botVozdeistvie
    global botIshZdorovie
    global botZdorovie
    global botIshMana
    global botInventar
    global botMana
    global botSila
    global botLovkost
    global botYdacha
    global botZoloto
    global botSerebro
    global botBronza
    global botZachita
    global botDeistvie
    global xShift
    global yShift
    
    global den
    global mesiac
    global god
    
    for n in range(16): # Рисуем иконки заклинаний
        printMagic(n)
    n = 0    
    for n in range(16): # Рисуем иконки инвентаря
        printInventar(n)  
    
    pygame.draw.rect(sc, (255, 255, 255), (284, 548, 481, 896)) 
    pygame.draw.rect(sc, (255, 255, 255), (405, 550, 365, 896))
   
    n = 0
    xShift = 410
    yShift = 785
    for n in range(10):
        if botVozdeistvie[imHero][n] == 3 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/dospechiFenicha_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift)) 
            xShift += 37
        elif botVozdeistvie[imHero][n] == 7 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/jad_32.png')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift)) 
            xShift += 37
        elif botVozdeistvie[imHero][n] == 8 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/krovojadnost_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift))  
            xShift += 37
        elif botVozdeistvie[imHero][n] == 10 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/mochPrirodi_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift))  
            xShift += 37           
        elif botVozdeistvie[imHero][n] == 13 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/pechatChaosa_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift))  
            xShift += 37
        elif botVozdeistvie[imHero][n] == 15 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/poceluiSmerti_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift)) 
            xShift += 37        
        elif botVozdeistvie[imHero][n] == 14 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/pechatSmerti_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift)) 
            xShift += 37
        elif botVozdeistvie[imHero][n] == 16 and botDeistvie[imHero][n] > 0:
            pix = pygame.image.load('Images/prokliatie_32.png')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xShift,yShift))  
            xShift += 37 
        elif botVozdeistvie[imHero][n] == 0 and botDeistvie[imHero][n] == 0:
            pygame.draw.rect(sc, (255, 255, 255), (xShift, 785, 32, 32))
            xShift += 37           
    
    xShift = 410
    
    xHero = 340
    yHero = 548
    if myHero == 50:
        pix = pygame.image.load('Images/akami.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Аками - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 51:
        pix = pygame.image.load('Images/artes.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Артес - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 52:
        pix = pygame.image.load('Images/deathOwner.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Мефистофор - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 54:
        pix = pygame.image.load('Images/djepotai.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Джепотай - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 55:
        pix = pygame.image.load('Images/farion.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Фарион - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 56:
        pix = pygame.image.load('Images/garitos.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Гаритос - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 57:
        pix = pygame.image.load('Images/gendalf.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Гендальф - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 58:
        pix = pygame.image.load('Images/illidan.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Иллидан - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 59:
        pix = pygame.image.load('Images/jaina.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Джайна - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 60:
        pix = pygame.image.load('Images/kell.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Келл - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 70:
        pix = pygame.image.load('Images/uter.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Утер - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 72:
        pix = pygame.image.load('Images/vulDjin.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Вул Джин - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 68:
        pix = pygame.image.load('Images/silvana.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Сильвана - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 65:
        pix = pygame.image.load('Images/pradmur.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Прадмур - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 69:
        pix = pygame.image.load('Images/trall.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Тралл - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 73:
        pix = pygame.image.load('Images/zadira.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Задира - " + str(botLvl[imHero]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    
    variableExpirience = "" + str(botExpirience[imHero]) + " XP"  # переменная типа String - опыт
    healtObj = textExpirience.render(variableExpirience, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(healtObj,(290, 631)) # Отображаем Опыт    
    
    variableHealt = "" + str(botZdorovie[imHero]) + " / " + str(botIshZdorovie[imHero]) # переменная типа String отображающая здоровье как ххх/ххх
    healtObj = healt.render(variableHealt, False, (0, 255, 0)) # Создали объект типа "текст" 
    sc.blit(healtObj,(290, 644)) # Отображаем здоровье
    
    variableMana = "" + str(botMana[imHero]) + " / " + str(botIshMana[imHero]) # переменная типа String отображающая ману как ххх/ххх
    manaObj = manna.render(variableMana, False, (0, 0, 255)) # Создали объект типа "текст" 
    sc.blit(manaObj,(290, 657)) # Отображаем ману
    
    if botUseWeapon[imHero] == 0:
        variableSila = u"Сила: " + str(botSila[imHero]) 
        silaObj = textSila.render(variableSila, False, (0, 0, 0)) # Создали объект типа "текст" 
        sc.blit(silaObj,(290, 670)) 
    else:
        variableSila = u"Сила: " + str(botSila[imHero]) + u"+" + str(botUseWeapon[imHero])
        silaObj = textSila.render(variableSila, False, (0, 255, 0)) # Создали объект типа "текст" 
        sc.blit(silaObj,(290, 670))
        
    variableLovk = u"Ловкость: " + str(botLovkost[imHero]) 
    lovkObj = textLovk.render(variableLovk, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(lovkObj,(290, 683)) 
    
    variableYdacha = u"Удача: " + str(botYdacha[imHero]) 
    ydachaObj = textYdacha.render(variableYdacha, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(ydachaObj,(290, 696))
    
    if botZachita[imHero] > 0:
        variableZachita = u"Защита: " + str(botZachita[imHero])
        zachObj = textZachita.render(variableZachita, False, (0, 255, 0)) # Создали объект типа "текст" 
        sc.blit(zachObj,(290, 709)) 
    
    variableZoloto = u"Золото: " + str(botZoloto[imHero]) 
    zolotoObj = textZoloto.render(variableZoloto, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(zolotoObj,(290, 735))
    
    variableSerebro = u"Серебро: " + str(botSerebro[imHero]) 
    serebroObj = textSerebro.render(variableSerebro, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(serebroObj,(290, 748))
    
    variableBronza = u"Бронза: " + str(botBronza[imHero]) 
    bronzaObj = textBronza.render(variableBronza, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(bronzaObj,(290, 761))
    
    pygame.display.update()  

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

def magDoIt(selectLot): #Покупаем в Хижине магов
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, world
    global botZachita, botHod, world, botNumer, botVariant, botAlgoritm, botLocation, attack, zakl, botDeistvie, posohSmerti, posohProzrenia, posohSveta, posohVoli, posohVechnoiJizni, yaNaRinke, yes, no, invent, hijinaMaga, zadanieMaga 
    
    pygame.draw.rect(sc, (255, 255, 255), (405, 550, 365, 896))
    if selectLot == 1:
        hijinaMaga = 0
        hijina = 0
        if botSerebro[imHero] >= 25:
            botSerebro[imHero] -= 25
            botIshMana[imHero] += 275
    
    if selectLot == 2:
        hijinaMaga = 0
        hijina = 0
        
        if drujbaMaga >= 2:
            slova = int(random.random() * 20)
            if slova == 0:
                variableName = u"Те кто хорошо овладел магической и"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"шаманскими практиками иногда носят"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"с собой такие предметы, за которые "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"торговцы на рынке могут выложить целое"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"состояние. Обычная казалось бы палка"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"тускло светящееся фиолетовым цветом"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"может стоить тысячи бронзовых монет."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"Хорошо, что торговцы не умеют "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"пользоваться подобными штуками."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
                variableName = u"Сколько бы хаоса породили эти алчные"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 740))
                variableName = u"твари в противном случае."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 760))
            elif slova == 1:
                variableName = u"У гномов чаще всего есть серебро"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"при себе. Они не редко ко мне забегают"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"за особым зельем, которое вызывает у"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"них необычные видения. Настанет время"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"и я тебя им тоже угощу"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
            elif slova == 2:
                variableName = u"Самые страшные создания в этом мире"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"это - Душекрады. Они владеют во истину"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"ужасающим заклинанием - Пронзающая смерть."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"Оно отнимает 300 здоровья. Есть книга"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"в которой говориться как овладеть"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"этим заклинанием. Её ты можешь найти"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"у прихвостней демонов - некромантов и"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"отшельников"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"Изучив это заклинание ты сможешь в"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
                variableName = u"одиночку одолеть целое полчище врага"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 740))
            elif slova == 3:
                variableName = u"Гноллы - самые бесполезные создания"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"в этих землях. Не знаю, что им здесь"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"нужно, они лезут из портала в этот"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"мир. Хорошо будет если ты будешь их"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"истреблять. Жаль что у них ничего"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"ценного при себе не бывает."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
            elif slova == 4:
                variableName = u"Духи-союзники иногда приходят в наши земли."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"Бывает времена когда они заглядывают"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"лишь на мгновение..."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"Если встать рядом с таким духом"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"он может увеличить твою исходную ману"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"на 100 единиц. Стой как можно дольше"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"с ним рядом. Они умеют телепортироваться"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"на довольно большие расстояния, так что"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"если хочешь стать могущественным магом"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
                variableName = u"с помощью духа-союзника, то придётся за "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 740))    
                variableName = u"ним побегать"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 760))
            elif slova == 5:
                variableName = u"На первых порах лучше покупай зелья"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"Маны, вместо зелий Здоровья"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"Так дешевле выйдет залечивать свои раны"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600))
            elif slova == 6:
                variableName = u"Когда появиться дух смерти, лучше"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"спрятаться от него подальше."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"Отряд душекрадов по сравнению с ним -"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"горстка жалких котят. Этот дух способен"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"убить любого одним лишь прикосновением"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"Они невероятно сильны и не предсказуемы."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"Ты можешь беззаботно идти на рынок,"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"чтобы продать свои трофеи, а дух встанет"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"перед тобой, ты даже не успеешь отпрыгнуть"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
                variableName = u"от него, как окажешься на том свете."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 740))   
            elif slova == 7:
                variableName = u"У эльфиек обычно много бронзы при себе"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"Они в роли посыльных на сколько мне"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"известно в городе. Их отправляют в"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"магический лес за лекарственными "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"растениями, и на рынок за снадобьями."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
            elif slova == 8 and botLvl[imHero] <= 5:
                variableName = u"Знаешь, а у меня ведь есть камень"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"который способен открыть врата для духов."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"Позже я его смогу тебе продать"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"А пока твой дух слаб, и я боюсь ты"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"не сможешь распорядиться им должным"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"образом. Ведь этот артефакт настолько"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"могущественен, что способен тебя убить"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680)) 
            elif slova == 9:
                variableName = u"Послушай, может в другой раз поговорим?"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"Я сейчас очень занят"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))
            elif slova == 10:
                variableName = u"У Некромантов и Оккультистов есть"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"особый посох. Ты можешь с помощью него"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"использовать заклинание Пронзающей"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"Смерти, направив его на врага, при этом"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"маны расходуется в два раза меньше."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"Правда им достаточно не удобно"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"пользоваться, но при должной сноровке"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"он будет служить тебе не заменимым"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"инструментом в борьбе. Мне довелось"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
                variableName = u"пользоваться таким артефактом во времена"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 740))    
                variableName = u"Великого Нашествия. От моих рук полег"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 760))
                variableName = u"не один десяток орков, и всё благодаря"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 800))
                variableName = u"этому посоху, быть может однажды я его"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 820))
                variableName = u"тебе продам"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 840))
            elif slova == 11:
                variableName = u"Когда пойдёшь охотиться на колдунов"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"прихвати с собой рассеивающее зелье"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"или что-то ему подобное. Постигшие"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"магию хаоса и смерти, колдуны а в "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"особенности некроманты, способны накладывать"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"такие заклинания как Печать Хаоса и"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"Печать Смерти. Первое не так страшно"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"от него хотя бы больше шансов спастись."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"А вот если на тебя наложат Печать Смерти"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
                variableName = u"и при тебе не будет рассеивающего зелья - "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 740))    
                variableName = u"можешь рыть себе могилу на том же месте"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 760))
            elif slova == 12:
                variableName = u"Мне доводилось пользоваться в бою"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"Посохом Прозрения. Это не заменимая вещь."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"Спомощью него легко оценить силу"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"противника. А так же он показывает "
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"Количество здоровья, маны, заклинания"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"которыми владеет существо, и даже показывает"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
                variableName = u"какой инвентарь есть у него с собой."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 680))
                variableName = u"На рынке такой посох можно купить, но он"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 700))
                variableName = u"очень дорого стоит"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 720))
            elif slova == 13:
                variableName = u"Далеко не всё можно купить на рынке."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560)) 
                variableName = u"Некоторый инвентарь добывается только в бою."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))  
                variableName = u"Например Шлем Бессмертия, который даёт"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 600)) 
                variableName = u"+30 Защиты. Чем больше ты врагов уничтожишь"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 620)) 
                variableName = u"тем велик шанс получить редкий лут."
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 640))
                variableName = u"Старайся, и однажды удача улыбнётся тебе"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 660))
            else:
                variableName = u"Молодой человек, у меня нет времени"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 560))     
                variableName = u"трепать языком с Вами о всякой ерунде"
                nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                sc.blit(nameObj,(440, 580))    
                                                      
        
    if selectLot == 3:
        hijinaMaga = 0
        hijina = 0
        if zadanieMaga == 0:
            zadanieMaga = 1
            variableName = u"У одного из представителя расы людей"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 560)) 
            variableName = u"есть банка с особым зельем. Оно мне"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 580))  
            variableName = u"нужно для моих исследований, найди её"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 600)) 
            variableName = u"Я заплачу тебе 1000 бронзовых монет "
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 620)) 
            variableName = u"если тебе удастся её мне принести"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 640))
        
        elif zadanieMaga == 2:
            zadanieMaga = 3
            variableName = u"Некоторое время назад жил маг, способный"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 560)) 
            variableName = u"кастовать заклинание Алчности. Он умер,"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 580))  
            variableName = u"непередав никому своих знаний. Я хочу"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 600)) 
            variableName = u"разгадать как ему удалось накладывать чары"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 620)) 
            variableName = u"Алчности на предметы. Предметы, зачарованные"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 640))   
            variableName = u"этим заклинанием, способны сделать кого"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 660))     
            variableName = u"угодно своим рабом. Принеси мне"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 680))
            variableName = u"Топор Алчности 4 уровня и я заплачу тебе"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 700))       
            variableName = u"7 Серебряных монет"
            nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
            sc.blit(nameObj,(440, 720))     
    
    
def magPerdun(perdun): # Взаимодействие с хижиной Мага
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, world
    global botZachita, botHod, world, botNumer, botVariant, botAlgoritm, botLocation, attack, zakl, botDeistvie, posohSmerti, posohProzrenia, posohSveta, posohVoli, posohVechnoiJizni, yaNaRinke, yes, no, invent, hijinaMaga
    
    hijinaMaga = 2
    pygame.draw.rect(sc, (255, 255, 255), (405, 550, 365, 896))
    
    pix = pygame.image.load('Images/yes.png') 
    x_len = pix.get_width()
    y_len = pix.get_height() 
    sc.blit(pix, (462,786))    
    pix = pygame.image.load('Images/no.png') 
    x_len = pix.get_width()
    y_len = pix.get_height() 
    sc.blit(pix, (530,786))
    
    if perdun == 1:
        variableName = u"Увеличить магическую силу"
        nameObj = textNameHero.render(variableName, False, (0, 255, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"За 25 серебра старый Маг может"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"увеличить исходное количество маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"на 275 единиц, тем самым Вы сможете"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"применять более могущественные "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = u"заклинания"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    elif perdun == 2:
        variableName = u"Говорить с Магом"
        nameObj = textNameHero.render(variableName, False, (0, 255, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Этот Колдун знает очень многое об"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"этом мире. Поговорив с ним, вы будете"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"действовать, как действовали маги"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = u"древности когда искали силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
    elif perdun == 3:
        variableName = u"Получить задание"
        nameObj = textNameHero.render(variableName, False, (0, 255, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Вы можете заработать немного бронзы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"выполнив поручение старого Колдуна"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))          
     

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

def loviVebalo(nomBota): # Используется если у бота нет заклинания, но бить кого-то надо
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, world 
    
    for n in range(100):
        if botLocation[nomBota] == botLocation[n]-33: # Бот сверху-слева
            if botLocation[nomBota]>=32:
                if botLocation[nomBota] != 0 and botLocation[nomBota] != 32 and botLocation[nomBota] != 64 and botLocation[nomBota] != 96 and botLocation[nomBota] != 128 and botLocation[nomBota] != 160 and botLocation[nomBota] != 192 and botLocation[nomBota] != 224 and botLocation[nomBota] != 256 and botLocation[nomBota] != 288 and botLocation[nomBota] != 320 and botLocation[nomBota] != 352 and botLocation[nomBota] != 384 and botLocation[nomBota] != 416:
                    if botZachita[n] < botSila[nomBota]: 
                        botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                        print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                    if n == imHero: heroPanel(imHero)
                    break
                            
        if botLocation[nomBota] == botLocation[n]-31: # Бот сверху-справа
            if botLocation[nomBota]>=32:
                if botLocation[nomBota] != 0 and botLocation[nomBota] != 32 and botLocation[nomBota] != 64 and botLocation[nomBota] != 96 and botLocation[nomBota] != 128 and botLocation[nomBota] != 160 and botLocation[nomBota] != 192 and botLocation[nomBota] != 224 and botLocation[nomBota] != 256 and botLocation[nomBota] != 288 and botLocation[nomBota] != 320 and botLocation[nomBota] != 352 and botLocation[nomBota] != 384 and botLocation[nomBota] != 416:
                    if botZachita[n] < botSila[nomBota]: 
                        botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                        print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                    if n == imHero: heroPanel(imHero)
                    break

        if botLocation[nomBota] == botLocation[n]+31: # Бот снизу-слева

            if botLocation[nomBota]<=416:
                if botLocation[nomBota] != 0 and botLocation[nomBota] != 32 and botLocation[nomBota] != 64 and botLocation[nomBota] != 96 and botLocation[nomBota] != 128 and botLocation[nomBota] != 160 and botLocation[nomBota] != 192 and botLocation[nomBota] != 224 and botLocation[nomBota] != 256 and botLocation[nomBota] != 288 and botLocation[nomBota] != 320 and botLocation[nomBota] != 352 and botLocation[nomBota] != 384 and botLocation[nomBota] != 416:
                    if botZachita[n] < botSila[nomBota]: 
                        botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                        print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                    if n == imHero: heroPanel(imHero)
                    break
                            
        if botLocation[nomBota] == botLocation[n]+33: # Бот снизу-справа
            if botLocation[nomBota]<=416:
                if botLocation[nomBota] != 0 and botLocation[nomBota] != 32 and botLocation[nomBota] != 64 and botLocation[nomBota] != 96 and botLocation[nomBota] != 128 and botLocation[nomBota] != 160 and botLocation[nomBota] != 192 and botLocation[nomBota] != 224 and botLocation[nomBota] != 256 and botLocation[nomBota] != 288 and botLocation[nomBota] != 320 and botLocation[nomBota] != 352 and botLocation[nomBota] != 384 and botLocation[nomBota] != 416:
                    if botZachita[n] < botSila[nomBota]: 
                        botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                        print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                    if n == imHero: heroPanel(imHero)
                    break
                
        if botLocation[nomBota] == botLocation[n]-1: # Бот слева
            if botLocation[nomBota] != 0 and botLocation[nomBota] != 32 and botLocation[nomBota] != 64 and botLocation[nomBota] != 96 and botLocation[nomBota] != 128 and botLocation[nomBota] != 160 and botLocation[nomBota] != 192 and botLocation[nomBota] != 224 and botLocation[nomBota] != 256 and botLocation[nomBota] != 288 and botLocation[nomBota] != 320 and botLocation[nomBota] != 352 and botLocation[nomBota] != 384 and botLocation[nomBota] != 416:
                if botZachita[n] < botSila[nomBota]: 
                    botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                    print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                if n == imHero: heroPanel(imHero)
                break

        if botLocation[nomBota] == botLocation[n]+1: # Бот справа
            if botLocation[nomBota] != 31 and botLocation[nomBota] != 63 and botLocation[nomBota] != 95 and botLocation[nomBota] != 127 and botLocation[nomBota] != 159 and botLocation[nomBota] != 191 and botLocation[nomBota] != 223 and botLocation[nomBota] != 255 and botLocation[nomBota] != 287 and botLocation[nomBota] != 319 and botLocation[nomBota] != 351 and botLocation[nomBota] != 383 and botLocation[nomBota] != 415 and botLocation[nomBota] != 447:
                if botZachita[n] < botSila[nomBota]: 
                    botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                    print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                if n == imHero: heroPanel(imHero)
                break

        if botLocation[nomBota] == botLocation[n]-32: # Бот сверху
            if botLocation[nomBota] >= 32:
                if botZachita[n] < botSila[nomBota]: 
                    botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                    print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                if n == imHero: heroPanel(imHero)
                break
 
        if botLocation[nomBota] == botLocation[n]+32: # Бот снизу
            if botLocation[nomBota] <= 416:
                if botZachita[n] < botSila[nomBota]: 
                    botZdorovie[n] -= botSila[nomBota]+botZachita[n]
                    print("BOT #", str(nomBota), " shot down. Step -", botStep[nomBota], "Life bot enemy -",botZdorovie[n])
                if n == imHero: heroPanel(imHero)
                break
        
                
        if botZdorovie[n] <= 0: ubiraemTrup(n); otdaiLut(nomBota, n)        
    

def bornBot(numerBurnBota, typeBurnBota):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, world, tmpMagExp, zadanieMaga  
    
    if typeBurnBota == 100 or typeBurnBota == 101 or typeBurnBota == 102 or typeBurnBota == 106 or typeBurnBota == 107 or typeBurnBota == 108 or typeBurnBota == 109 or typeBurnBota == 110 or typeBurnBota == 111 or typeBurnBota == 112 or typeBurnBota == 113 or typeBurnBota == 114 or typeBurnBota == 115 or typeBurnBota == 116 or typeBurnBota == 117 or typeBurnBota == 118 or typeBurnBota == 126 or typeBurnBota == 127 or typeBurnBota == 128 or typeBurnBota == 129 or typeBurnBota == 145 or typeBurnBota == 146 or typeBurnBota == 157 or typeBurnBota == 165 or typeBurnBota == 166 or typeBurnBota == 167 or typeBurnBota == 168 or typeBurnBota == 169 or typeBurnBota == 170 or typeBurnBota == 171 or typeBurnBota == 172:
        if zadanieMaga == 1 and tmpMagExp == 0:
            if typeBurnBota == 114 or typeBurnBota == 116 or typeBurnBota == 117 or typeBurnBota == 118 or typeBurnBota == 128 or typeBurnBota == 130 or typeBurnBota == 135 or typeBurnBota == 144 or typeBurnBota == 145 or typeBurnBota == 146 or typeBurnBota == 157:
                tmpMagExp = 1
                botInventar[numerBurnBota] = [52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
        if world[30] == 0:
            xBot[numerBurnBota] = 976
            yBot[numerBurnBota] = 96
            world[30] = typeBurnBota
            botLocation[numerBurnBota] = 30
        elif world[144] == 0:
            xBot[numerBurnBota] = 528
            yBot[numerBurnBota] = 224
            world[144] = typeBurnBota
            botLocation[numerBurnBota] = 144    
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
    
    elif typeBurnBota == 173 or typeBurnBota == 174: # Если это духи
        if world[240] == 0:
            xBot[numerBurnBota] = 528
            yBot[numerBurnBota] = 320
            world[240] = typeBurnBota
            botLocation[numerBurnBota] = 240
        elif world[241] == 0:
            xBot[numerBurnBota] = 560
            yBot[numerBurnBota] = 320
            world[241] = typeBurnBota
            botLocation[numerBurnBota] = 241
        elif world[242] == 0:
            xBot[numerBurnBota] = 592
            yBot[numerBurnBota] = 320
            world[242] = typeBurnBota
            botLocation[numerBurnBota] = 242
        elif world[243] == 0:
            xBot[numerBurnBota] = 624
            yBot[numerBurnBota] = 320
            world[243] = typeBurnBota
            botLocation[numerBurnBota] = 243
        elif world[244] == 0:
            xBot[numerBurnBota] = 656
            yBot[numerBurnBota] = 320
            world[244] = typeBurnBota
            botLocation[numerBurnBota] = 244             
    
    else:
        if world[384] == 0:
            xBot[numerBurnBota] = 16
            yBot[numerBurnBota] = 480
            world[384] = typeBurnBota
            botLocation[numerBurnBota] = 384
        elif world[177] == 0:
            xBot[numerBurnBota] = 560
            yBot[numerBurnBota] = 256
            world[177] = typeBurnBota
            botLocation[numerBurnBota] = 177       
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
           
def randomBot():
        global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, world, tmpMagExp, zadanieMaga  
        for n in range(30):
            if botZdorovie[n] <= 0: #Если бот номер N мёртв, то занимаем его ID
                botUseWeapon[n] = 0
                botZachita[n] = 0
                tmp = int(random.random()*73)+100 # Генеруем вид бота
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
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 10
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 15
                    if botRandom == 10:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 20
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
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 20
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 30
                    if botRandom == 10:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 40       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 1
                    botBronza[n] = 15
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 25
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 35 
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2
                        botBronza[n] = 45       
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
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
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
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
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
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 15
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 25
                    if botRandom == 10:
                        botInventar[n] = [67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botSerebro[n] = 1
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1 
                        botBronza[n] = 30
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1 
                        botBronza[n] = 40
                    if botRandom == 10:
                        botInventar[n] = [69,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2       
                        botBronza[n] = 50
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 1
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [68,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [69,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2 
                    if botRandom == 10:
                        botInventar[n] = [70,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 4 
                    bornBot(n, tmp)
                        
                if tmp == 109: # Гном 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 375
                    botIshZdorovie[n] = 375
                    botMana[n] = 280
                    botIshMana[n] = 280
                    botZaklinania[n]=[22,23,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[n] = 31
                    botLovkost[n] = 12
                    botYdacha[n] = 19

                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 3
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 2
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [69,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [70,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 4 
                    if botRandom == 10:
                        botInventar[n] = [70,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 5  
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
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 80
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
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
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 15
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
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

                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 10
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 20
                    if botRandom == 10:
                        botInventar[n] = [0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
                        botSerebro[n] = 2
                        botBronza[n] = 20
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
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 60
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      
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
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 60
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
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
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
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
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [61,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
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
                        botSerebro[n] = 1
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
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2       
                        botBronza[n] = 350
                    bornBot(n, tmp) 
                        
                if tmp == 122: # Монстр 4 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 770
                    botIshZdorovie[n] = 770
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
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 250
                    if botRandom == 10:
                        botInventar[n] = [51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 4       
                        botBronza[n] = 300
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 15
                    if botRandom == 10:
                        botInventar[n] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 25
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 50
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [60,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 130
                    if botRandom == 10:
                        botInventar[n] = [61,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 15
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [60,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 20
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [61,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 30
                    if botRandom == 10:
                        botInventar[n] = [62,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 45       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 80
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 300       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 3
                    if botRandom == 10:
                        botInventar[n] = [65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 300       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                    if botRandom == 10:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3   
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 20
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 30
                    if botRandom == 10:
                        botInventar[n] = [65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 30       
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
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 3
                    if botRandom == 10:
                        botInventar[n] = [51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 4      
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
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 20
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 50
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 90
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
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 70
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 110
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 1
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,53,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [10,54,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                    if botRandom == 13:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2
                        botBronza[n] = 100   
                    if botRandom == 12:
                        botInventar[n] = [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                    if botRandom == 11:
                        botInventar[n] = [57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 5
                    if botRandom == 10:
                        botInventar[n] = [66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 7      
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 40
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 50
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 60
                    if botRandom == 10:
                        botInventar[n] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 70
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 60
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 70
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 80
                    if botRandom == 10:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 1
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 300
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
                    botSila[n] = 45
                    botLovkost[n] = 6
                    botYdacha[n] = 17
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 240
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
                    botSila[n] = 62
                    botLovkost[n] = 6
                    botYdacha[n] = 17
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 150
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 250
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
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
                    botSila[n] = 85
                    botLovkost[n] = 6
                    botYdacha[n] = 27
                    botHod[n] = botLovkost[n]
                    botVozdeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[n] = 4
                    botDeistvie[n]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 4
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [32,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 5
                        botBronza[n] = 300
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3       
                        botBronza[n] = 300
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 90
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [73,53,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [10,58,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                    if botRandom == 12:
                        botInventar[n] = [56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                    if botRandom == 11:
                        botInventar[n] = [66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                    if botRandom == 10:
                        botInventar[n] = [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3     
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 40
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 65
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 2
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 200
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
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 10
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
                    bornBot(n, tmp)
                        
                if tmp == 149: # Скелет 2 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 2
                    botZdorovie[n] = 80
                    botIshZdorovie[n] = 80
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
                    bornBot(n, tmp)
                        
                if tmp == 150: # Скелет 3 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 3
                    botZdorovie[n] = 120
                    botIshZdorovie[n] = 120
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
                    bornBot(n, tmp)
                        
                if tmp == 151: # Скелет 4 ур.
                    botNumer[n] = n

                    botVariant[n] = tmp        
                    botLvl[n] = 4
                    botZdorovie[n] = 165
                    botIshZdorovie[n] = 165
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
                    bornBot(n, tmp)
                        
                if tmp == 152: # Скелет 5 ур.
                    botNumer[n] = n
                    botVariant[n] = tmp        
                    botLvl[n] = 5
                    botZdorovie[n] = 220
                    botIshZdorovie[n] = 220
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                    if botRandom == 9:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botZoloto[n] = 1
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 80
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 95
                    if botRandom == 10:
                        botInventar[n] = [56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 125       
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
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 150
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
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 100
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 1
                    if botRandom == 10:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 2
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
                    botBronza[n] = 30
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 200
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
                    botBronza[n] = 30
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 130
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 280
                    if botRandom == 10:
                        botInventar[n] = [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botSerebro[n] = 2
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 10
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 50
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [0,12,48,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [31,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 200
                    if botRandom == 10:
                        botInventar[n] = [31,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                        botBronza[n] = 300
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                        botInventar[n] = [53,0,12,0,0,0,0,0,0,0,0,0,0,0,0,0]       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 1
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [59,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botSerebro[n] = 3
                        botBronza[n] = 550       
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
                    botBronza[n] = 0
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 50
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 100
                    if botRandom == 10:
                        botInventar[n] = [0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 70
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 150
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 250
                    if botRandom == 10:
                        botInventar[n] = [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 400       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 100
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 200
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                    if botRandom == 10:
                        botInventar[n] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 400       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 170
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 270
                        botSerebro[n] = 1
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 2
                    if botRandom == 10:
                        botInventar[n] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 600       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 270
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 370
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [0,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 3
                    if botRandom == 10:
                        botInventar[n] = [72,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 800       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 80
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 280
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botBronza[n] = 300
                        botSerebro[n] = 3
                    if botRandom == 10:
                        botInventar[n] = [56,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 400       
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
                    botInventar[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botZoloto[n] = 0
                    botSerebro[n] = 0
                    botBronza[n] = 280
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[n] = [72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 380
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[n] = [11,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                        botSerebro[n] = 4
                    if botRandom == 10:
                        botInventar[n] = [58,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botBronza[n] = 500       
                    bornBot(n, tmp)                 
                
                break           

def botActivity(nomerBota):
    global botAlgoritm, botAttack, botBronza, botDeistvie, botExpirience, botHod, botInventar, botIshMana, botIshZdorovie, botLocation, botLovkost, botLvl, botMana, botMap, botNumer, botRasa, botSerebro, botSila, botStep, botType, botUseWeapon, botVariant, botVozdeistvie, botYdacha, botZachita, botZaklinania, botZdorovie, botZoloto, sobitie, locations, startBotGeneration  
    
    #print("botActivity", str(sobitie))
    
    if sobitie % 32 == 0: # тут обрабатывается действие долгодействующих ЗАКЛИНАНИЙ
        for n in range(15):
            if botVozdeistvie[nomerBota][n] == 7 and botDeistvie[nomerBota][n] > 0: # Отравление
                botZdorovie[nomerBota] -= 5
                botDeistvie[nomerBota][n] -= 1
                
            elif botVozdeistvie[nomerBota][n] == 14 and botDeistvie[nomerBota][n] > 0:  # Печать смерти
                botDeistvie[nomerBota][n] -= 1
                print("DEATH!!!")
                if botDeistvie[nomerBota][n] == 1:
                    botZdorovie[nomerBota] = -1000
                
            elif botVozdeistvie[nomerBota][n] == 13 and botDeistvie[nomerBota][n] > 0: # Печать Хаоса
                botDeistvie[nomerBota][n] -= 1
                botMana[nomerBota] = 0
                botZdorovie[nomerBota] -= 15 
            
            elif botVozdeistvie[nomerBota][n] == 15 and botDeistvie[nomerBota][n] > 0: # Поцелуй смерти
                botDeistvie[nomerBota][n] -= 1
                botMana[nomerBota] = 0
                botZdorovie[nomerBota] -= 40              
                
                
            if botDeistvie[nomerBota][n] <= 0: 
                botVozdeistvie[nomerBota][n] = 0
                botDeistvie[nomerBota][n] = 0
                
    if sobitie % 2397 == 0:
        tmpInventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for n in range(16): 
            pass
            nn = 0 
            tmp = int(random.random()*75)
            if tmp == 66 or tmp == 53 or tmp == 52 or tmp == 57 or tmp == 58 or tmp == 55 or tmp == 33 or tmp == 56 or tmp == 29 or tmp == 30 or tmp == 31 or tmp == 65, tmp == 51, tmp == 50:
                market[n] = tmpInventar[n] = 0
            else:
                market[n] = tmpInventar[n] = tmp
            lalsas1488 = int(random.random()*7)
            if lalsas1488 == 5: market[n] = tmpInventar[n] = 0
        print("Market change: " + str(market))
    
    if sobitie % 1097 == 0: mutation()
    
    
            
    if sobitie % 537 == 0: # Рожаем бота
        randBorn = int(random.random()*10)
        if randBorn >= 0 and randBorn <= 5: 
            randomBot()
            randomBot()
        elif randBorn == 6:
            randomBot()
            randomBot()
            randomBot()
        elif randBorn == 7:
            randomBot()
            randomBot()
            randomBot()    
            randomBot()   
        else:
            randomBot()   
            
        
                 
    
    if botZdorovie[0] <= 0 and botZdorovie[1] <= 0 and botZdorovie[2] <= 0 and botZdorovie[3]<= 0 and botZdorovie[4] <= 0 and botZdorovie[5] <= 0 and botZdorovie[6] <= 0 and botZdorovie[7] <= 0 and botZdorovie[8] <= 0 and  botZdorovie[9] <= 0 and botZdorovie[10] <= 0 and botZdorovie[7] <= 0 and botZdorovie[11] <= 0 and  botZdorovie[12] <= 0 and botZdorovie[13]<= 0 and botZdorovie[14] <= 0 and botZdorovie[15] <= 0 and botZdorovie[16] <= 0 and botZdorovie[17] <= 0:
        print(genom)
        print("Life time: ", lifeTime)
        mutation()        
    
    # Обрабатываем геном
    if botStep[nomerBota] > 127: botStep[nomerBota] = 0
    if botZdorovie[nomerBota] > 0 and nomerBota != imHero: # Если бот жив
        
        if genom[botStep[nomerBota]] == 0:
            if botVariant[nomerBota] == 173 or botVariant[nomerBota] == 174:
                botZdorovie[nomerBota] = 0
                ubiraemTrup(nomerBota)
        
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
                    for n in range(100):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+32 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                                botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                            #print("Im - ", str(nomerBota), " shot up. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                            if n == imHero: heroPanel(imHero)
                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                            break                    
                    
        elif genom[botStep[nomerBota]] == 6: # Бьём врага вниз 
            if botLocation[nomerBota] <= 416:
                if world[botLocation[nomerBota]+32] >= 50: # Если снизу кто-то есть, то...
                    for n in range(100):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-32 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                                botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                            #print("Im - ", str(nomerBota), " shot down. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                            if n == imHero: heroPanel(imHero)
                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                            break
        
        elif genom[botStep[nomerBota]] == 7: # Бьём врага слева
            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                if world[botLocation[nomerBota]-1] >= 50: # Если слева кто-то есть, то...
                    for n in range(100):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+1 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                                botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                            #print("Im - ", str(nomerBota), " shot left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                            if n == imHero: heroPanel(imHero)
                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                            break
        
        elif genom[botStep[nomerBota]] == 8: # Бьём врага справа
            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                if world[botLocation[nomerBota]+1] >= 50: # Если справа кто-то есть, то...
                    for n in range(100):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-1 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                                botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                            #print("Im - ", str(nomerBota), " shot right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n]) 
                            if n == imHero: heroPanel(imHero)
                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                            break

        elif genom[botStep[nomerBota]] == 9: # Бьём врага сверху-справа
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                    if world[botLocation[nomerBota]-31] >= 50: # Если справа кто-то есть, то...
                        for n in range(100):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                #print("Im - ", str(nomerBota), " shot up-right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                if n == imHero: heroPanel(imHero)
                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                break
        
        elif genom[botStep[nomerBota]] == 10: # Бьём врага сверху-слева
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]-33] >= 50: # Если справа кто-то есть, то...
                        for n in range(100):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                #print("Im - ", str(nomerBota), " shot up-left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                if n == imHero: heroPanel(imHero)
                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                break
                            
        elif genom[botStep[nomerBota]] == 11: # Бьём врага снизу-справа
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                    if world[botLocation[nomerBota]+33] >= 50: # Если справа кто-то есть, то...
                        for n in range(100):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                #print("Im - ", str(nomerBota), " shot up-right. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                if n == imHero: heroPanel(imHero)
                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                break
        
        elif genom[botStep[nomerBota]] == 12: # Бьём врага снизу-слева
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]+31] >= 50: # Если справа кто-то есть, то...
                        for n in range(100):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                #print("Im - ", str(nomerBota), " shot up-left. Step -", botStep[nomerBota], "Life bot enemy -",botZdorovie[n])
                                if n == imHero: heroPanel(imHero)
                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                break
                            
        elif genom[botStep[nomerBota]] == 13:  # Применяем заклинание "Пронзающая смерть"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 1:
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    #print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    else: pass #print("Less that 200 mana")
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    #print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    else: pass #print("Less that 200 mana")
    
                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    #print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    else: pass #print("Less that 200 mana")
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    #print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                    if botMana[nomerBota] >= 200:
                                        botMana[nomerBota] -= 200
                                        botZdorovie[n] -= 300
                                        #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    else: pass #print("Less that 200 mana")                             
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                #print("Bot is left, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                else: pass #print("Less that 200 mana")

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                #print("Bot is right, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                else: pass #print("Less that 200 mana")

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                #print("Bot is up, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                else: pass #print("Less that 200 mana")
     
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                #print("Bot is up, Im - ", str(nomerBota), "kast - Death Explode")
                                if botMana[nomerBota] >= 200:
                                    botMana[nomerBota] -= 200
                                    botZdorovie[n] -= 300
                                    #print("Excellent, bot ", str(n), "is DEATH. BotZdorovie =",botZdorovie[n])
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                else: pass #print("Less that 200 mana")  
                #if n==14 and botZaklinania[nomerBota][n] != 1: loviVebalo(nomerBota)
                        
        elif genom[botStep[nomerBota]] == 14:  # Применяем заклинание "Fair Ball"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 1:
                    for n in range(15):
                        if botZaklinania[n] == 6:
                            for n in range(300):
                                if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                                    if botLocation[nomerBota]>=32:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            if botMana[nomerBota] >= 30:
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                if n == imHero: heroPanel(imHero)
                                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                                break
                            
                                if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                                    if botLocation[nomerBota]>=32:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            if botMana[nomerBota] >= 30:
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                if n == imHero: heroPanel(imHero)
                                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                                break

                                if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                                    if botLocation[nomerBota]<=416:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            if botMana[nomerBota] >= 30:
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                if n == imHero: heroPanel(imHero)
                                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                                break
                            
                                if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                                    if botLocation[nomerBota]<=416:
                                        if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                            if botMana[nomerBota] >= 30:
                                                botMana[nomerBota] -= 30
                                                botZdorovie[n] -= 30
                                                if n == imHero: heroPanel(imHero)
                                                if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                                break
                
                                if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                                    if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                        if botMana[nomerBota] >= 30:
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            if n == imHero: heroPanel(imHero)
                                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                            break

                                if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                                    if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                        if botMana[nomerBota] >= 30:
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            if n == imHero: heroPanel(imHero)
                                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                            break
                                if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                                    if botLocation[nomerBota] >= 32:
                                        if botMana[nomerBota] >= 30:
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            if n == imHero: heroPanel(imHero)
                                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                            break
 
                                if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                                    if botLocation[nomerBota] <= 416:
                                        if botMana[nomerBota] >= 30:
                                            botMana[nomerBota] -= 30
                                            botZdorovie[n] -= 30
                                            if n == imHero: heroPanel(imHero)
                                            if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                            break
                #if n==14 and botZaklinania[nomerBota][n] != 6: loviVebalo(nomerBota)
                                           
        elif genom[botStep[nomerBota]] == 15:  # Применяем заклинание "Молния"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 12:
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 70:
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 70:
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 70:
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 70:
                                        botMana[nomerBota] -= 70
                                        botZdorovie[n] -= 70
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 70:
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 70:
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break

                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 70:
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 70:
                                    botMana[nomerBota] -= 70
                                    botZdorovie[n] -= 70
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                #if n==14 and botZaklinania[nomerBota][n] != 12: loviVebalo(nomerBota) 
        
        elif genom[botStep[nomerBota]] == 16:  # Применяем заклинание "Лечение"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 22:
                    if botZdorovie[nomerBota]+45 <= botIshZdorovie[nomerBota]:
                        if botMana[nomerBota] >= 30:
                            botMana[nomerBota] -= 30
                            botZdorovie[nomerBota] += 30
                if n==14 and botZaklinania[nomerBota][n] != 22: loviVebalo(nomerBota)
            
        elif genom[botStep[nomerBota]] == 17:  # Применяем заклинание "Лунный обряд"        
            for n in range(15):
                if botZaklinania[nomerBota][n] == 9:
                    if botZdorovie[nomerBota]+80 <= botIshZdorovie[nomerBota]:
                        if botMana[nomerBota] >= 70:
                            botMana[nomerBota] -= 70
                            if botZdorovie[nomerBota] +70 <= botIshZdorovie[nomerBota]:
                                botZdorovie[nomerBota] += 70
                            else: botZdorovie[nomerBota] = botIshZdorovie[nomerBota]
                #if n==14 and botZaklinania[nomerBota][n] != 17: loviVebalo(nomerBota)
                   
        
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
                #if n==14 and botZaklinania[nomerBota][n] != 3: loviVebalo(nomerBota)
                                
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
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 60:
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    break  
                            
                        if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 60:
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    break

                        if botLocation[nomerBota] == botLocation[n]+31: # Бот снизу-слева
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 60:
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    break
                            
                        if botLocation[nomerBota] == botLocation[n]+33: # Бот снизу-справа
                            if botLocation[nomerBota]<=416:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 60:
                                        botMana[nomerBota] -= 60
                                        botZdorovie[n] -= 50
                                        if n == imHero: heroPanel(imHero)
                                        if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                        break
                                    break   
                
                        if botLocation[nomerBota] == botLocation[n]-1: # Бот слева

                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                if botMana[nomerBota] >= 60:
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                break

                        if botLocation[nomerBota] == botLocation[n]+1: # Бот справа
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                if botMana[nomerBota] >= 60:
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                break
                                
                        if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                            if botLocation[nomerBota] >= 32:
                                if botMana[nomerBota] >= 60:
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                break
 
                        if botLocation[nomerBota] == botLocation[n]+32: # Бот снизу
                            if botLocation[nomerBota] <= 416:
                                if botMana[nomerBota] >= 60:
                                    botMana[nomerBota] -= 60
                                    botZdorovie[n] -= 50
                                    if n == imHero: heroPanel(imHero)
                                    if botZdorovie[n] <= 0: otdaiLut(nomerBota, n)
                                    break
                                break
                #if n==14 and botZaklinania[nomerBota][n] != 11: loviVebalo(nomerBota)
                                                
                                
        elif genom[botStep[nomerBota]] == 24:  # Применяем заклинание "Доспехи Феникса"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 3:
                    if botMana[nomerBota] >= 30:
                        for m in range(15):
                            if botVozdeistvie[nomerBota][n] == 3:
                                break
                            if m == 15 and botVozdeistvie[nomerBota][n] != 3: 
                                botVozdeistvie[nomerBota][n] = 3
                                botDeistvie[nomerBota][n] = 10
                                botMana[nomerBota] -= 30
                                break
                            
                    else: pass
                    break
                if n==14 and botZaklinania[nomerBota][n] != 3: loviVebalo(nomerBota)
                
                    
        
                                    
        elif genom[botStep[nomerBota]] == 26:  # Применяем заклинание "Отравление"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 7:
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 30:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 7:
                                                botVozdeistvie[n][m] = 7
                                                botDeistvie[n][m] = 700
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
                                                botDeistvie[n][m] = 700
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
                                                botDeistvie[n][m] = 700
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
                                                botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
                                            botMana[nomerBota] -= 30
                                            print("Conjuring Fraud")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Fraud")
                                break
                if n==14 and botZaklinania[nomerBota][n] != 7: loviVebalo(nomerBota)                               

        elif genom[botStep[nomerBota]] == 27:  # Применяем заклинание "Кровожадность"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 8:
                    if botMana[nomerBota] >= 35:
                        for m in range(15):
                            if botVozdeistvie[nomerBota][n] == 3:
                                print("I'm already bewitched by the Bloodthirstiness")
                                break
                            if m == 15 and botVozdeistvie[nomerBota][n] != 3: 
                                print("The jam is already active")  
                                botVozdeistvie[nomerBota][n] = 3
                                botDeistvie[nomerBota][n] = 10
                                botMana[nomerBota] -= 30
                                print("Conjuring Bloodthirstiness")
                                break
                            
                    else: print("Need a mana for Bloodthirstiness")
                    break
                #if n==14 and botZaklinania[nomerBota][n] != 8: loviVebalo(nomerBota)    
                    
        elif genom[botStep[nomerBota]] == 28:  # Применяем заклинание "Мощь Природы"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 10:
                    if botMana[nomerBota] >= 65:
                        for m in range(15):
                            if botVozdeistvie[nomerBota][n] == 3:
                                print("I'm already bewitched by the The power of nature")
                                break
                            if m == 15 and botVozdeistvie[nomerBota][n] != 3: 
                                print("The jam is already active")  
                                botVozdeistvie[nomerBota][n] = 3
                                botDeistvie[nomerBota][n] = 10
                                botMana[nomerBota] -= 30
                                print("Conjuring The power of nature")
                                break
                            
                    else: print("Need a mana for The power of nature")
                    break
                if n==14 and botZaklinania[nomerBota][n] != 10: loviVebalo(nomerBota)
                    
        elif genom[botStep[nomerBota]] == 29:  # Применяем заклинание "Печать Хаоса"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 13:
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 170:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 13:
                                                botVozdeistvie[n][m] = 13
                                                botDeistvie[n][m] = 700
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
                                                botDeistvie[n][m] = 700
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
                                                botDeistvie[n][m] = 700
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
                                                botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
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
                                            botDeistvie[n][m] = 700
                                            botMana[nomerBota] -= 170
                                            print("Conjuring Seal of Chaos")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Chaos")
                                break
                #if n==14 and botZaklinania[nomerBota][n] != 13: loviVebalo(nomerBota)
                 
                    
        elif genom[botStep[nomerBota]] == 30:  # Применяем заклинание "Поцелуй Смерти"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 15:
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 100:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 15:
                                                botVozdeistvie[n][m] = 15
                                                botDeistvie[n][m] = 7000
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
                                                botDeistvie[n][m] = 7000
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
                                                botDeistvie[n][m] = 7000
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
                                                botDeistvie[n][m] = 7000
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
                                            botDeistvie[n][m] = 7000
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
                                            botDeistvie[n][m] = 7000
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
                                            botDeistvie[n][m] = 7000
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
                                            botDeistvie[n][m] = 7000
                                            botMana[nomerBota] -= 100
                                            print("Conjuring Kiss of death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for The Kiss of death")
                                break
                if n==14 and botZaklinania[nomerBota][n] != 15: loviVebalo(nomerBota)                
                            
        elif genom[botStep[nomerBota]] == 31:  # Применяем заклинание "Печать Смерти"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 14:
                    for n in range(300):
                        if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                            if botLocation[nomerBota]>=32:
                                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                    if botMana[nomerBota] >= 200:
                                        for m in range(15):
                                            if botVozdeistvie[n][m] != 14:
                                                botVozdeistvie[n][m] = 14
                                                botDeistvie[n][m] = 5
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
                                                botDeistvie[n][m] = 5
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
                                                botDeistvie[n][m] = 5
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
                                                botDeistvie[n][m] = 5
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
                                            botDeistvie[n][m] = 5
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
                                            botDeistvie[n][m] = 5
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
                                            botDeistvie[n][m] = 5
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
                                            botDeistvie[n][m] = 5
                                            botMana[nomerBota] -= 200
                                            print("Conjuring Seal of Death")
                                            break
                                        if m == 15: print("The jam is already active")  
                                else: print("Need a mana for Seal of Death")
                                break                   
                #if n==14 and botZaklinania[nomerBota][n] != 14: loviVebalo(nomerBota)
                 
                    
        
                                 
        elif genom[botStep[nomerBota]] == 33:  # Применяем заклинание "Рассеять Чары"
            for n in range(15):
                if botZaklinania[nomerBota][n] == 23 and botVozdeistvie[nomerBota] != [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
                    if botMana[nomerBota] >= 100:
                        botVozdeistvie[nomerBota] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botDeistvie[nomerBota] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        botMana[nomerBota] -= 100

                    else: print("Need a mana for Dispel spell")
                    break
                #if n==14 and botZaklinania[nomerBota][n] != 23: loviVebalo(nomerBota) 

        elif genom[botStep[nomerBota]] == 34: # Способность духа - прибавить исходную ману 
            if botVariant[nomerBota] == 173:    
                for n in range(300):
                    if botLocation[nomerBota] == botLocation[n]-33: # Бот сверху-слева
                        if botLocation[nomerBota]>=32:
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                botIshMana[n] += 100
                                break
                                
                    if botLocation[nomerBota] == botLocation[n]-32: # Бот сверху
                        if botLocation[nomerBota]>=32:
                            botIshMana[n] += 100
                            break 
                    
                    if botLocation[nomerBota] == botLocation[n]-31: # Бот сверху-справа
                        if botLocation[nomerBota]>=32:
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                botIshMana[n] += 100
                                break

                    if botLocation[nomerBota] == botLocation[n]+33: # Бот сверху-слева
                        if botLocation[nomerBota]<=416:
                            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                                botIshMana[n] += 100
                                break
                                
                    if botLocation[nomerBota] == botLocation[n]+32: # Бот сверху
                        if botLocation[nomerBota]<=416:
                            botIshMana[n] += 100
                            break 
                    
                    if botLocation[nomerBota] == botLocation[n]+31: # Бот сверху-справа
                        if botLocation[nomerBota]<=416:
                            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                                botIshMana[n] += 100
                                break                                
                                                     
        
        elif genom[botStep[nomerBota]] == 45: # Бьём врага вверх 
            if botLocation[nomerBota]>=32:
                if world[botLocation[nomerBota]-32] >= 50: # Если сверху кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+32 and botZdorovie[n] > 0:
                            if botZachita[n] < botSila[nomerBota]: 
                               botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                               break                    
                    
        elif genom[botStep[nomerBota]] == 46: # Бьём врага вниз 
            if botLocation[nomerBota] <= 416:
                if world[botLocation[nomerBota]+32] >= 50: # Если снизу кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-32 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                               botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                               break  
        
        elif genom[botStep[nomerBota]] == 47: # Бьём врага слева
            if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:

                if world[botLocation[nomerBota]-1] >= 50: # Если слева кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]+1 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                               botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                               break  
        
        elif genom[botStep[nomerBota]] == 48: # Бьём врага справа
            if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:
                if world[botLocation[nomerBota]+1] >= 50: # Если справа кто-то есть, то...
                    for n in range(10):
                        tmp = n
                        if botLocation[nomerBota] == botLocation[n]-1 and botZdorovie[n] > 0: 
                            if botZachita[n] < botSila[nomerBota]: 
                               botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                               break  

        elif genom[botStep[nomerBota]] == 49: # Бьём врага сверху-справа
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:

                    if world[botLocation[nomerBota]-31] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                   botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                   break  
        
        elif genom[botStep[nomerBota]] == 50: # Бьём врага сверху-слева
            if botLocation[nomerBota]>=32:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]-33] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                    break  
                            
        elif genom[botStep[nomerBota]] == 51: # Бьём врага снизу-справа
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 31 and botLocation[nomerBota] != 63 and botLocation[nomerBota] != 95 and botLocation[nomerBota] != 127 and botLocation[nomerBota] != 159 and botLocation[nomerBota] != 191 and botLocation[nomerBota] != 223 and botLocation[nomerBota] != 255 and botLocation[nomerBota] != 287 and botLocation[nomerBota] != 319 and botLocation[nomerBota] != 351 and botLocation[nomerBota] != 383 and botLocation[nomerBota] != 415 and botLocation[nomerBota] != 447:

                    if world[botLocation[nomerBota]+33] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-31 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                    break 
        
        elif genom[botStep[nomerBota]] == 52: # Бьём врага снизу-слева
            if botLocation[nomerBota]<=416:
                if botLocation[nomerBota] != 0 and botLocation[nomerBota] != 32 and botLocation[nomerBota] != 64 and botLocation[nomerBota] != 96 and botLocation[nomerBota] != 128 and botLocation[nomerBota] != 160 and botLocation[nomerBota] != 192 and botLocation[nomerBota] != 224 and botLocation[nomerBota] != 256 and botLocation[nomerBota] != 288 and botLocation[nomerBota] != 320 and botLocation[nomerBota] != 352 and botLocation[nomerBota] != 384 and botLocation[nomerBota] != 416:
                    if world[botLocation[nomerBota]+31] >= 50: # Если справа кто-то есть, то...
                        for n in range(10):
                            tmp = n
                            if botLocation[nomerBota] == botLocation[n]-33 and botZdorovie[n] > 0: 
                                if botZachita[n] < botSila[nomerBota]: 
                                    botZdorovie[n] -= botSila[nomerBota]+botZachita[n]
                                    break                                                    

        
        
        else:
            pass # Тут мы должны сделать перескакивание команд
    else:
        pass
    
    
        
    botStep[nomerBota] += 1
    sobitie += 1
    #botZdorovie[nomerBota] -= 1
    if sobitie > 100000: sobitie = 0
    if botZdorovie[nomerBota] <= 0:
        if botVariant[nomerBota] == 173 and botVariant[nomerBota] == 174: ubiraemTrup(nomerBota)
        else: 
            ubiraemTrup(nomerBota)
            otdaiLut(n, nomerBota)
   
worldCreate()    

locations = [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63]
n = 0
    
if test == 0:
    botExpirience[imHero] = 0  
    botLvl[imHero] = 1
    botRasa[imHero] = 7
    botInventar[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botZaklinania[imHero] = [22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
    botVozdeistvie[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botIshZdorovie[imHero] = 200
    botZdorovie[imHero] = 200
    botMana[imHero] = 100
    botIshMana[imHero] = 100
    botSila[imHero] = 10
    botLovkost[imHero] = 5
    botYdacha[imHero] = 9
    botZoloto[imHero] = 0
    botSerebro[imHero] = 0
    botBronza[imHero] = 0
    botHod[imHero] = botLovkost[imHero]
    botAlgoritm[imHero] = 4
    botVariant[imHero] = 52
    botDeistvie[imHero]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    world[172] = 52
    botLocation[imHero] = 172 # Исходное положение на карте
    xBot[imHero] = 400
    yBot[imHero] = 256
elif test == 1:
    botExpirience[imHero] = 0  
    botLvl[imHero] = 1
    botRasa[imHero] = 7
    botInventar[imHero] = [54,56,12,11,10,10,10,10,0,0,0,0,0,0,0,0]
    botZaklinania[imHero] = [3,7,10,8,13,15,1,14,16,12,0,0,0,0,0,100]
    botVozdeistvie[imHero] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botIshZdorovie[imHero] = 1200
    botZdorovie[imHero] = 1200
    botMana[imHero] = 1000
    botIshMana[imHero] = 1000
    botSila[imHero] = 50
    botLovkost[imHero] = 5
    botYdacha[imHero] = 9
    botZoloto[imHero] = 0
    botSerebro[imHero] = 1000
    botBronza[imHero] = 100000
    botHod[imHero] = botLovkost[imHero]
    botAlgoritm[imHero] = 4
    botVariant[imHero] = 52
    botDeistvie[imHero]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    botVozdeistvie[imHero]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    world[172] = 52
    botLocation[imHero] = 172 # Исходное положение на карте
    xBot[imHero] = 400
    yBot[imHero] = 256


n = 0

for n in range(16): # Рисуем иконки заклинаний
    printMagic(n)
n = 0
for n in range(16): # Рисуем иконки инвентаря
    printInventar(n)
n = 0  

heroPanel(52)    
pygame.display.update()   
while True:
    clock.tick(160)
    if botZdorovie[n] > 0: botActivity(n)
    if botVariant[n] > 0 and botZdorovie[n] <= 0:    
            ubiraemTrup(n)      
            world[botLocation[n]] = 0
            print("Bot ", str(n), " - DEAD")
            worldUpdate()
            pygame.display.update()
    n += 1
    
    if n >= 20: n = 0; lifeTime += 1
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
            
        elif i.type == pygame.KEYDOWN and newGame == 1:
            
            if i.key == pygame.K_LEFT and xBot[imHero] >= 18 and world[botLocation[imHero]-1] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[imHero],yBot[imHero]))
                xBot[imHero] -= 32
                world[botLocation[imHero]] = 0
                world[botLocation[imHero]-1] = botVariant[imHero]
                botLocation[imHero] -= 1
                worldUpdate()
                heroPanel(botVariant[imHero])
                invent = 0
                if tmpMarket == 2: yaNaRinke = 0
                posohProzrenia = 0
                
            elif i.key == pygame.K_RIGHT and xBot[imHero] <= 990 and world[botLocation[imHero]+1] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[imHero],yBot[imHero]))
                xBot[imHero] += 32
                world[botLocation[imHero]] = 0
                world[botLocation[imHero]+1] = botVariant[imHero]
                botLocation[imHero] += 1
                worldUpdate()
                heroPanel(botVariant[imHero])
                invent = 0
                if tmpMarket == 2: yaNaRinke = 0
                posohProzrenia = 0
                
            elif i.key == pygame.K_UP and yBot[imHero] > 96 and world[botLocation[imHero]-32] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[imHero],yBot[imHero]))
                yBot[imHero] -= 32
                world[botLocation[imHero]] = 0
                world[botLocation[imHero]-32] = botVariant[imHero]
                botLocation[imHero] -= 32
                worldUpdate()
                heroPanel(botVariant[imHero])
                invent = 0
                if tmpMarket == 2: yaNaRinke = 0
                posohProzrenia = 0
                
            elif i.key == pygame.K_DOWN and yBot[imHero] <= 510 and world[botLocation[imHero]+32] == 0: 
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[imHero],yBot[imHero]))
                yBot[imHero] += 32
                world[botLocation[imHero]] = 0
                world[botLocation[imHero]+32] = botVariant[imHero]
                botLocation[imHero] += 32
                worldUpdate()
                heroPanel(botVariant[imHero])
                invent = 0
                if tmpMarket == 2: yaNaRinke = 0
                posohProzrenia = 0

    mos_x, mos_y = pygame.mouse.get_pos() # Тут мы берём координаты мыши
#============================================================================================================================================    
#==================================================ОБРАБОТКА НАЖАТИЙ КНОПОК ИГРОВОГО ПОЛЯ====================================================
#============================================================================================================================================

    #===================================================1 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(0)
            if i.button == 3: myAttack(0)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(1)
            if i.button == 3: myAttack(1)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(2)
            if i.button == 3: myAttack(2)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(3)
            if i.button == 3: myAttack(3)
                
    if mos_x>145 and (mos_x<175):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(4)
            if i.button == 3: myAttack(4)
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(5)
            if i.button == 3: myAttack(5)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(6)
            if i.button == 3: myAttack(6)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(7)
            if i.button == 3: myAttack(7)           
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(8)
            if i.button == 3: myAttack(8)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(9)
            if i.button == 3: myAttack(9)            
                
    if mos_x>337 and (mos_x<367):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(10)
            if i.button == 3: myAttack(10)
    
    if mos_x>369 and (mos_x<399):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:  doebaca(11)
            if i.button == 3: myAttack(11)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(12)
            if i.button == 3: myAttack(12)           
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(13)
            if i.button == 3: myAttack(13)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(14)
            if i.button == 3: myAttack(14)           
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(15)
            if i.button == 3: myAttack(15)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(16)
            if i.button == 3: myAttack(16)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(17)
            if i.button == 3: myAttack(17)          
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(18)
            if i.button == 3: myAttack(18)
                
    if mos_x>625 and (mos_x<655):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(19)
            if i.button == 3: myAttack(19)
                
    if mos_x>657 and (mos_x<687):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(20)
            if i.button == 3: myAttack(20)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(21)
            if i.button == 3: myAttack(21); doebaca(21)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(22)
            if i.button == 3: myAttack(22); doebaca(22)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(23)
            if i.button == 3: myAttack(23); doebaca(23)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:doebaca(24)
            if i.button == 3: myAttack(24); doebaca(24)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(25)
            if i.button == 3: myAttack(25); doebaca(25)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(26)
            if i.button == 3: myAttack(26); doebaca(26)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(27)
            if i.button == 3: myAttack(27); doebaca(27)
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(28)
            if i.button == 3: myAttack(28); doebaca(28)
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(29)
            if i.button == 3: myAttack(29); doebaca(29)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(30)
            if i.button == 3: myAttack(30); doebaca(30)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(31)
            if i.button == 3: myAttack(31); doebaca(31)
                
    #===================================================2 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(32)
            if i.button == 3: myAttack(32); doebaca(32)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(33)
            if i.button == 3: myAttack(33); doebaca(33)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(34)
            if i.button == 3: myAttack(34); doebaca(34)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(35)
            if i.button == 3: myAttack(35); doebaca(35)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(36)
            if i.button == 3: myAttack(36); doebaca(36)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(37)
            if i.button == 3: myAttack(37); doebaca(37)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(38)
            if i.button == 3: myAttack(38); doebaca(38)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(39)
            if i.button == 3: myAttack(39); doebaca(39)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(40)
            if i.button == 3: myAttack(40); doebaca(40)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(41)
            if i.button == 3: myAttack(41); doebaca(41)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(42)
            if i.button == 3: myAttack(42); doebaca(42)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(43)
            if i.button == 3: myAttack(43); doebaca(43)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(44)
            if i.button == 3: myAttack(44); doebaca(44)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(45)
            if i.button == 3: myAttack(45); doebaca(45)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(46) 
            if i.button == 3: myAttack(46); doebaca(46)
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(47)
            if i.button == 3: myAttack(47); doebaca(47)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(48)
            if i.button == 3: myAttack(48); doebaca(48)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(49)
            if i.button == 3: myAttack(49); doebaca(49)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(50)
            if i.button == 3: myAttack(50); doebaca(50)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(51)
            if i.button == 3: myAttack(51); doebaca(51)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(52)
            if i.button == 3: myAttack(52); doebaca(52)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(53)
            if i.button == 3: myAttack(53); doebaca(53)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(54)
            if i.button == 3: myAttack(54); doebaca(54)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(55)
            if i.button == 3: myAttack(55); doebaca(55)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(56)
            if i.button == 3: myAttack(56); doebaca(56)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(57)
            if i.button == 3: myAttack(57); doebaca(57)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(58)
            if i.button == 3: myAttack(58); doebaca(58)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(59)
            if i.button == 3: myAttack(59); doebaca(59)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(60)
            if i.button == 3: myAttack(60); doebaca(60)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(61)
            if i.button == 3: myAttack(61); doebaca(61)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(62)
            if i.button == 3: myAttack(62); doebaca(62)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(63)
            if i.button == 3: myAttack(63); doebaca(63)
                
    #===================================================3 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(64)
            if i.button == 3: myAttack(64)

    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(65)
            if i.button == 3: myAttack(65)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(66)
            if i.button == 3: myAttack(66) 
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(67)
            if i.button == 3: myAttack(67)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(68)
            if i.button == 3: myAttack(68)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(69)
            if i.button == 3: myAttack(69)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(70)
            if i.button == 3: myAttack(70)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(71) 
            if i.button == 3: myAttack(71)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(72)
            if i.button == 3: myAttack(72)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(73)
            if i.button == 3: myAttack(73)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(74)
            if i.button == 3: myAttack(74)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(75)
            if i.button == 3: myAttack(75)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(76)
            if i.button == 3: myAttack(76)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(77)
            if i.button == 3: myAttack(77)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(78) 
            if i.button == 3: myAttack(78)
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(79)
            if i.button == 3: myAttack(79)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(80)
            if i.button == 3: myAttack(80)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(81)
            if i.button == 3: myAttack(81)
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(82)
            if i.button == 3: myAttack(82)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(83)
            if i.button == 3: myAttack(83)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(84)
            if i.button == 3: myAttack(84)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(85)
            if i.button == 3: myAttack(85)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(86)
            if i.button == 3: myAttack(86)
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(87)
            if i.button == 3: myAttack(87)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(88)
            if i.button == 3: myAttack(88)
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(89)
            if i.button == 3: myAttack(89)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(90)
            if i.button == 3: myAttack(90)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(91)
            if i.button == 3: myAttack(91)
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(92)
            if i.button == 3: myAttack(92)
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(93)
            if i.button == 3: myAttack(93)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(94)
            if i.button == 3: myAttack(94)
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(95)
            if i.button == 3: myAttack(95)
    
    #===================================================4 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(96)
            if i.button == 3: myAttack(96)
    
    if mos_x>49 and (mos_x<79):  x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(97)
            if i.button == 3: myAttack(97)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(98)
            if i.button == 3: myAttack(98)
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(99)
            if i.button == 3: myAttack(99)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(100)
            if i.button == 3: myAttack(100)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(101)
            if i.button == 3: myAttack(101)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(102)
            if i.button == 3: myAttack(102)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(103)
            if i.button == 3: myAttack(103)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(104)
            if i.button == 3: myAttack(104)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(105)
            if i.button == 3: myAttack(105)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(106)
            if i.button == 3: myAttack(106)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(107)
            if i.button == 3: myAttack(107)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(108) 
            if i.button == 3: myAttack(108)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(109)
            if i.button == 3: myAttack(109)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(110)
            if i.button == 3: myAttack(110)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(111)
            if i.button == 3: myAttack(111)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(112)
            if i.button == 3: myAttack(112)            
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(113) 
            if i.button == 3: myAttack(113)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(114)
            if i.button == 3: myAttack(114)            
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(115)
            if i.button == 3: myAttack(115)            
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(116)
            if i.button == 3: myAttack(116)            
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(117)
            if i.button == 3: myAttack(117)            
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(118)
            if i.button == 3: myAttack(118)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(119)
            if i.button == 3: myAttack(119)            
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(120)
            if i.button == 3: myAttack(120)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(121) 
            if i.button == 3: myAttack(121)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(122)
            if i.button == 3: myAttack(122)            
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(123)
            if i.button == 3: myAttack(123)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(124)
            if i.button == 3: myAttack(124)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(125)
            if i.button == 3: myAttack(125)            
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(126)
            if i.button == 3: myAttack(126)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(127)
            if i.button == 3: myAttack(127)            
                
    #===================================================5 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(128)
            if i.button == 3: myAttack(128)            
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(129)
            if i.button == 3: myAttack(129)            
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(130)
            if i.button == 3: myAttack(130)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(131)
            if i.button == 3: myAttack(131)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(132)
            if i.button == 3: myAttack(132)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(133)
            if i.button == 3: myAttack(133)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(134)
            if i.button == 3: myAttack(134)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(135)
            if i.button == 3: myAttack(135)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(136)
            if i.button == 3: myAttack(136)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(137)
            if i.button == 3: myAttack(137)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(138)
            if i.button == 3: myAttack(138)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(139)
            if i.button == 3: myAttack(139)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(140)
            if i.button == 3: myAttack(140)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(141)
            if i.button == 3: myAttack(141)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(142)
            if i.button == 3: myAttack(142)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(143)
            if i.button == 3: myAttack(143)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(144)
            if i.button == 3: myAttack(144)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(145)
            if i.button == 3: myAttack(145)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(146)
            if i.button == 3: myAttack(146)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(147)
            if i.button == 3: myAttack(147)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(148)
            if i.button == 3: myAttack(148)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(149)
            if i.button == 3: myAttack(149)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(150)
            if i.button == 3: myAttack(150)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(151)
            if i.button == 3: myAttack(151)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(152)
            if i.button == 3: myAttack(152)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(153)
            if i.button == 3: myAttack(153)            
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(154)
            if i.button == 3: myAttack(154)            
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(155) 
            if i.button == 3: myAttack(155)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(156)
            if i.button == 3: myAttack(156)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(157) 
            if i.button == 3: myAttack(157)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(158) 
            if i.button == 3: myAttack(158)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(159)
            if i.button == 3: myAttack(159)            
                
    #===================================================6 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(160)
            if i.button == 3: myAttack(160)            
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(161)
            if i.button == 3: myAttack(161)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(162)
            if i.button == 3: myAttack(162)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(163)
            if i.button == 3: myAttack(163)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(164)
            if i.button == 3: myAttack(164)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(165)
            if i.button == 3: myAttack(165)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(166)
            if i.button == 3: myAttack(166)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(167)
            if i.button == 3: myAttack(167)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(168)
            if i.button == 3: myAttack(168)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(169)
            if i.button == 3: myAttack(169)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(170)
            if i.button == 3: myAttack(170)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(171)
            if i.button == 3: myAttack(171)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(172)
            if i.button == 3: myAttack(172)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(173)
            if i.button == 3: myAttack(173)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(174)
            if i.button == 3: myAttack(174)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(175)
            if i.button == 3: myAttack(175)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(176)
            if i.button == 3: myAttack(176)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(177)
            if i.button == 3: myAttack(177)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(178)
            if i.button == 3: myAttack(178)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(179)
            if i.button == 3: myAttack(179)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(180)
            if i.button == 3: myAttack(180)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(181)
            if i.button == 3: myAttack(181)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(182)
            if i.button == 3: myAttack(182)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(183)
            if i.button == 3: myAttack(183)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(184)
            if i.button == 3: myAttack(184)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(185)
            if i.button == 3: myAttack(185)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(186)
            if i.button == 3: myAttack(186)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(187)
            if i.button == 3: myAttack(187)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(188)
            if i.button == 3: myAttack(188)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(189)
            if i.button == 3: myAttack(189)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(190)
            if i.button == 3: myAttack(190)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(191)
            if i.button == 3: myAttack(191)            
                
    #===================================================7 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(192)
            if i.button == 3: myAttack(192)            
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(193)
            if i.button == 3: myAttack(193)            
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(194)
            if i.button == 3: myAttack(194)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(195)
            if i.button == 3: myAttack(195)            
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(196)
            if i.button == 3: myAttack(196)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(197)
            if i.button == 3: myAttack(197)            
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(198)
            if i.button == 3: myAttack(198)            
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(199)
            if i.button == 3: myAttack(199)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(200)
            if i.button == 3: myAttack(200)            
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(201)
            if i.button == 3: myAttack(201)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(202)
            if i.button == 3: myAttack(202)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(203)
            if i.button == 3: myAttack(203)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(204)
            if i.button == 3: myAttack(204)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(205)
            if i.button == 3: myAttack(205)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(206)
            if i.button == 3: myAttack(206)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(207)
            if i.button == 3: myAttack(207)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(208)
            if i.button == 3: myAttack(208)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(209)
            if i.button == 3: myAttack(209)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(210)
            if i.button == 3: myAttack(210)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(211)
            if i.button == 3: myAttack(211)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(212)
            if i.button == 3: myAttack(212)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(213)
            if i.button == 3: myAttack(213)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(214)
            if i.button == 3: myAttack(214)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(215)
            if i.button == 3: myAttack(215)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(216)
            if i.button == 3: myAttack(216)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(217)
            if i.button == 3: myAttack(217)
    
    if mos_x>849 and (mos_x<879):  x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(218)
            if i.button == 3: myAttack(218)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(219)
            if i.button == 3: myAttack(219)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(220)
            if i.button == 3: myAttack(220)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(221)
            if i.button == 3: myAttack(221)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(222)
            if i.button == 3: myAttack(222)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(223)
            if i.button == 3: myAttack(223)
            
    #===================================================8 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(224)
            if i.button == 3: myAttack(224)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(225)
            if i.button == 3: myAttack(225)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(226)
            if i.button == 3: myAttack(226)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(227)
            if i.button == 3: myAttack(227)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(228)
            if i.button == 3: myAttack(228)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(229)
            if i.button == 3: myAttack(229)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(230)
            if i.button == 3: myAttack(230)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(231)
            if i.button == 3: myAttack(231)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(232)
            if i.button == 3: myAttack(232)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(233)
            if i.button == 3: myAttack(233)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(234)
            if i.button == 3: myAttack(234)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(235)
            if i.button == 3: myAttack(235)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(236)
            if i.button == 3: myAttack(236)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(237)
            if i.button == 3: myAttack(237)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(238)
            if i.button == 3: myAttack(238)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(239)
            if i.button == 3: myAttack(239)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(240)
            if i.button == 3: myAttack(240)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(241)
            if i.button == 3: myAttack(241)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(242)
            if i.button == 3: myAttack(242)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(243)
            if i.button == 3: myAttack(243)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(244)
            if i.button == 3: myAttack(244)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(245)
            if i.button == 3: myAttack(245)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(246)
            if i.button == 3: myAttack(246)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(247)
            if i.button == 3: myAttack(247)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(248)
            if i.button == 3: myAttack(248)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(249)
            if i.button == 3: myAttack(249)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(250)
            if i.button == 3: myAttack(250)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(251)
            if i.button == 3: myAttack(251)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(252)
            if i.button == 3: myAttack(252)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(253)
            if i.button == 3: myAttack(253)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(254)
            if i.button == 3: myAttack(254)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(255)
            if i.button == 3: myAttack(255)            
            
    #===================================================9 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(256)
            if i.button == 3: myAttack(256)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(257)
            if i.button == 3: myAttack(257)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(258)
            if i.button == 3: myAttack(258)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(259)
            if i.button == 3: myAttack(259)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(260)
            if i.button == 3: myAttack(260)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(261)
            if i.button == 3: myAttack(261)            
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(262)
            if i.button == 3: myAttack(262)            
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(263)
            if i.button == 3: myAttack(263)            
    
    if mos_x>273 and (mos_x<303):  x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(264)
            if i.button == 3: myAttack(264)            
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(265)
            if i.button == 3: myAttack(265)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(266)
            if i.button == 3: myAttack(266)            
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(267)
            if i.button == 3: myAttack(267)            
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(268)
            if i.button == 3: myAttack(268)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(269)
            if i.button == 3: myAttack(269)            
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(270)
            if i.button == 3: myAttack(270)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(271)
            if i.button == 3: myAttack(271)            
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(272)
            if i.button == 3: myAttack(272)            
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(273)
            if i.button == 3: myAttack(273)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(274)
            if i.button == 3: myAttack(274)            
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(275)
            if i.button == 3: myAttack(275)            
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(276)
            if i.button == 3: myAttack(276)            
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(277)
            if i.button == 3: myAttack(277)            
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(278)
            if i.button == 3: myAttack(278)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(279)
            if i.button == 3: myAttack(279)            
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(280)
            if i.button == 3: myAttack(280)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(281)
            if i.button == 3: myAttack(281)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(282)
            if i.button == 3: myAttack(282)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(283)
            if i.button == 3: myAttack(283)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(284)
            if i.button == 3: myAttack(284)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(285)
            if i.button == 3: myAttack(285)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(286)
            if i.button == 3: myAttack(286)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(287)
            if i.button == 3: myAttack(287)            
            
    #===================================================10 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(288)
            if i.button == 3: myAttack(288)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(289)
            if i.button == 3: myAttack(289)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(290)
            if i.button == 3: myAttack(290)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(291)
            if i.button == 3: myAttack(291)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(292)
            if i.button == 3: myAttack(292)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(293)
            if i.button == 3: myAttack(293)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(294)
            if i.button == 3: myAttack(294)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(295)
            if i.button == 3: myAttack(295)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(296)
            if i.button == 3: myAttack(296)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(297)
            if i.button == 3: myAttack(297)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN: 
            if i.button == 1: doebaca(298)
            if i.button == 3: myAttack(298)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(299)
            if i.button == 3: myAttack(299)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(300)
            if i.button == 3: myAttack(300)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(301)
            if i.button == 3: myAttack(301)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(302)
            if i.button == 3: myAttack(302)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(303)
            if i.button == 3: myAttack(303)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(304)
            if i.button == 3: myAttack(304)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(305)
            if i.button == 3: myAttack(305)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(306)
            if i.button == 3: myAttack(306)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(307)
            if i.button == 3: myAttack(307)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(308)
            if i.button == 3: myAttack(308)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(309)
            if i.button == 3: myAttack(309)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(310)
            if i.button == 3: myAttack(310)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(311)
            if i.button == 3: myAttack(311)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(312)
            if i.button == 3: myAttack(312)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(313)
            if i.button == 3: myAttack(313)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(314)
            if i.button == 3: myAttack(314)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(315)
            if i.button == 3: myAttack(315)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(316)
            if i.button == 3: myAttack(316)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(317)
            if i.button == 3: myAttack(317)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(318)
            if i.button == 3: myAttack(318)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(319)
            if i.button == 3: myAttack(319)            
            
    #===================================================11 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(320)
            if i.button == 3: myAttack(320)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(321)
            if i.button == 3: myAttack(321)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(322)
            if i.button == 3: myAttack(322)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(323)
            if i.button == 3: myAttack(323)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(324)
            if i.button == 3: myAttack(324)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(325)
            if i.button == 3: myAttack(325)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(326)
            if i.button == 3: myAttack(326)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(327)
            if i.button == 3: myAttack(327)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(328)
            if i.button == 3: myAttack(328)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(329)
            if i.button == 3: myAttack(329)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(330)
            if i.button == 3: myAttack(330)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(331)
            if i.button == 3: myAttack(331)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(332)
            if i.button == 3: myAttack(332)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(333)
            if i.button == 3: myAttack(333)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(334)
            if i.button == 3: myAttack(334)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(335)
            if i.button == 3: myAttack(335)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(336)
            if i.button == 3: myAttack(336)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(337)
            if i.button == 3: myAttack(337)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(338)
            if i.button == 3: myAttack(338)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(339)
            if i.button == 3: myAttack(339)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(340)
            if i.button == 3: myAttack(340)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(341)
            if i.button == 3: myAttack(341)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(342)
            if i.button == 3: myAttack(342)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(343)
            if i.button == 3: myAttack(343)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(344)
            if i.button == 3: myAttack(344)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(345)
            if i.button == 3: myAttack(345)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(346)
            if i.button == 3: myAttack(346)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(347)
            if i.button == 3: myAttack(347)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(348)
            if i.button == 3: myAttack(348)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(349)
            if i.button == 3: myAttack(349)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(350)
            if i.button == 3: myAttack(350)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(351)
            if i.button == 3: myAttack(351)            
            
    #===================================================12 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(352)
            if i.button == 3: myAttack(352)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(353)
            if i.button == 3: myAttack(353)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(354)
            if i.button == 3: myAttack(354)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(355)
            if i.button == 3: myAttack(355)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(356)
            if i.button == 3: myAttack(356)            
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(357)
            if i.button == 3: myAttack(357)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(358)
            if i.button == 3: myAttack(358)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(359)
            if i.button == 3: myAttack(359)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(360)
            if i.button == 3: myAttack(360)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(361)
            if i.button == 3: myAttack(361)            
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(362)
            if i.button == 3: myAttack(362)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(363)
            if i.button == 3: myAttack(363)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(364)
            if i.button == 3: myAttack(364)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(365)
            if i.button == 3: myAttack(365)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(366)
            if i.button == 3: myAttack(366)            
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(367)
            if i.button == 3: myAttack(367)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(368)
            if i.button == 3: myAttack(368)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(369)
            if i.button == 3: myAttack(369)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(370)
            if i.button == 3: myAttack(370)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(371)
            if i.button == 3: myAttack(371)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(372)
            if i.button == 3: myAttack(372)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(373)
            if i.button == 3: myAttack(373)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(374)
            if i.button == 3: myAttack(374)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(375)
            if i.button == 3: myAttack(375)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(376)
            if i.button == 3: myAttack(376)            
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(377)
            if i.button == 3: myAttack(377)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(378)
            if i.button == 3: myAttack(378)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(379)
            if i.button == 3: myAttack(379)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(380)
            if i.button == 3: myAttack(380)            
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(381)
            if i.button == 3: myAttack(381)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(382)
            if i.button == 3: myAttack(382)            
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(383)
            if i.button == 3: myAttack(383)            
            
    #===================================================13 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(384)
            if i.button == 3: myAttack(384)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(385)
            if i.button == 3: myAttack(385)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(386)            
            if i.button == 3: myAttack(386)
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(387)
            if i.button == 3: myAttack(387)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(388) 
            if i.button == 3: myAttack(388)
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(389)
            if i.button == 3: myAttack(389)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(390)
            if i.button == 3: myAttack(390)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(391)            
            if i.button == 3: myAttack(391)
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(392)
            if i.button == 3: myAttack(392)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(393) 
            if i.button == 3: myAttack(393)
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(394)
            if i.button == 3: myAttack(394)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(395)
            if i.button == 3: myAttack(395)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(396)            
            if i.button == 3: myAttack(396)
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(397)
            if i.button == 3: myAttack(397)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(398) 
            if i.button == 3: myAttack(398)
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(399)
            if i.button == 3: myAttack(399)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(400)
            if i.button == 3: myAttack(400)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(401)            
            if i.button == 3: myAttack(401)
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(402)
            if i.button == 3: myAttack(402)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(403)
            if i.button == 3: myAttack(403)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(404)
            if i.button == 3: myAttack(404)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(405)
            if i.button == 3: myAttack(405)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(406)            
            if i.button == 3: myAttack(406)
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(407)
            if i.button == 3: myAttack(407)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(408) 
            if i.button == 3: myAttack(408)
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(409)
            if i.button == 3: myAttack(409)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(410)
            if i.button == 3: myAttack(410)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(411)            
            if i.button == 3: myAttack(411)
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(412)  
            if i.button == 3: myAttack(412)
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(413)
            if i.button == 3: myAttack(413)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(414)    
            if i.button == 3: myAttack(414)
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(415)     
            if i.button == 3: myAttack(415)
            
    #===================================================14 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(416)
            if i.button == 3: myAttack(416)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(417)
            if i.button == 3: myAttack(417)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(418)            
            if i.button == 3: myAttack(418)
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(419)
            if i.button == 3: myAttack(419)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(420) 
            if i.button == 3: myAttack(420)
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(421)
            if i.button == 3: myAttack(421)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(422)
            if i.button == 3: myAttack(422)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(423)            
            if i.button == 3: myAttack(423)
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(424)
            if i.button == 3: myAttack(424)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(425) 
            if i.button == 3: myAttack(425)
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(426)
            if i.button == 3: myAttack(426)
    
    if mos_x>369 and (mos_x<399):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(427)
            if i.button == 3: myAttack(427)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(428)            
            if i.button == 3: myAttack(428)
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(429)
            if i.button == 3: myAttack(429)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(430) 
            if i.button == 3: myAttack(430)
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(431)
            if i.button == 3: myAttack(431)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(432)
            if i.button == 3: myAttack(432)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(433)            
            if i.button == 3: myAttack(433)
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(434)
            if i.button == 3: myAttack(434)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(435)
            if i.button == 3: myAttack(435)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(436)
            if i.button == 3: myAttack(436)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(437)
            if i.button == 3: myAttack(437)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(438)            
            if i.button == 3: myAttack(438)
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(439)
            if i.button == 3: myAttack(439)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(440) 
            if i.button == 3: myAttack(440)
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(441)
            if i.button == 3: myAttack(441)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(442)
            if i.button == 3: myAttack(442)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(443)            
            if i.button == 3: myAttack(443)
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(444)  
            if i.button == 3: myAttack(444)
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(445)
            if i.button == 3: myAttack(445)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(446)    
            if i.button == 3: myAttack(446)
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(447)
            if i.button == 3: myAttack(447)

#============================================================================================================================================
#==========================================================ОБРАБОТКА СОБЫТИЙ КНОПОК ЗАКЛИНАНИЙ=============================================== 
#============================================================================================================================================
    

    if mos_x>16 and (mos_x<80): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     newGameButton = 0 
                     hero = 50 
                     newGame = 1
                     initGame(50)                
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 1
                     attack = 0
                     textMagic(zakl)
                     
                 
    if mos_x>84 and (mos_x<148): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     newGameButton = 0
                     hero = 51
                     newGame = 1 
                     initGame(51)  
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 2 
                     attack = 0
                     textMagic(zakl)         
                 
    if mos_x>152 and (mos_x<216): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     newGameButton = 0
                     hero = 52
                     newGame = 1  
                     initGame(52) 
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 3 
                     attack = 0
                     textMagic(zakl)
                                                            
    if mos_x>220 and (mos_x<284): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     newGameButton = 0
                     hero = 54
                     newGame = 1 
                     initGame(54)  
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 4 
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>16 and (mos_x<80): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     newGameButton = 0
                     hero = 55
                     newGame = 1 
                     initGame(55)  
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 5 
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>84 and (mos_x<148): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     newGameButton = 0
                     hero = 56
                     newGame = 1 
                     initGame(56)  
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 6
                     attack = 0
                     textMagic(zakl)    
                 
    if mos_x>152 and (mos_x<216): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 57
                     newGame = 1 
                     initGame(57)  
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 7
                     attack = 0
                     textMagic(zakl)          
                                                            
    if mos_x>220 and (mos_x<284): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 58
                     newGame = 1  
                     initGame(58) 
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 8 
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>16 and (mos_x<80): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 59
                     newGame = 1 
                     initGame(59)  
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 9 
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>84 and (mos_x<148): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 60
                     newGame = 1   
                     initGame(60)
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 10
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>152 and (mos_x<216): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 70
                     newGame = 1 
                     initGame(70)  
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 11     
                     attack = 0
                     textMagic(zakl)          
                                                            
    if mos_x>220 and (mos_x<284): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 72
                     newGame = 1 
                     initGame(72)  
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 12   
                     attack = 0
                     textMagic(zakl)                      
                 
    if mos_x>16 and (mos_x<80): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 68
                     newGame = 1  
                     initGame(68) 
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 13 
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>84 and (mos_x<148): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 65
                     newGame = 1  
                     initGame(65) 
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 14 
                     attack = 0
                     textMagic(zakl)
                 
    if mos_x>152 and (mos_x<216): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 69
                     newGame = 1 
                     initGame(69)  
                     newGameButton = 0
                 pygame.time.delay(500)
                 if newGameButton == 0 and newGame == 1:  # Нажали на заклинание 
                     zakl = 15  
                     attack = 0
                     textMagic(zakl)            
                                                            
    if mos_x>220 and (mos_x<284): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     zakl = 0
                     attack = 1      
                     pygame.draw.rect(sc, (255, 255, 255), (405, 558, 365, 896))                      
                     variableName = u"Атака"
                     nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
                     sc.blit(nameObj,(440, 560))
                 
                 if newGameButton == 1:
                     hero = 73
                     newGame = 1  
                     initGame(73) 
                     newGameButton = 0
                 pygame.time.delay(500)
    
#============================================================================================================================================
#==========================================================ОБРАБОТКА СОБЫТИЙ КНОПОК ИНВЕНТАРЯ================================================ 
#============================================================================================================================================
    

    if mos_x>772 and (mos_x<836): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(1) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 1
                     magPerdun(1)
                 else: 
                     zakl = 0
                     attack = 0
                     invent = 1
                     textInventar(invent)
                    
                 
    if mos_x>840 and (mos_x<904): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(2)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 2
                     magPerdun(2)
                 else: 
                     zakl = 0 
                     attack = 0
                     invent = 2  
                     textInventar(invent)
                       
                 
    if mos_x>908 and (mos_x<972): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(3)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 3
                     magPerdun(3)
                 else:  
                     zakl = 0 
                     attack = 0
                     invent = 3
                     textInventar(invent)
                       
                                                            
    if mos_x>976 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>548 and (mos_y<612):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(4)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 4
                     magPerdun(4)
                 else: 
                     zakl = 0
                     attack = 0
                     invent = 4
                     textInventar(invent)
                       
                 
    if mos_x>772 and (mos_x<836):  
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(5)  
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 5
                     magPerdun(5)
                 else: 
                     zakl = 0
                     attack = 0
                     invent = 5
                     textInventar(invent)
                     
                 
    if mos_x>840 and (mos_x<904): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(6) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 6
                     magPerdun(6)
                 else: 
                     zakl = 0
                     attack = 0
                     invent = 6 
                     textInventar(invent)
                      
                 
    if mos_x>908 and (mos_x<972): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(7) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 7
                     magPerdun(7)
                 else: 
                     zakl = 0
                     attack = 0
                     invent = 7         
                     textInventar(invent)
                      
                                                            
    if mos_x>976 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>616 and (mos_y<680):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(8)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 8
                     magPerdun(8)
                 else:  
                     zakl = 0
                     attack = 0
                     invent = 8
                     textInventar(invent)
                       
                 
    if mos_x>772 and (mos_x<836): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(9) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 9
                     magPerdun(9)
                 else:
                     zakl = 0
                     attack = 0
                     invent = 9
                     textInventar(invent)
                      
                 
    if mos_x>840 and (mos_x<904): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(10)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 10
                     magPerdun(10)
                 else:
                     zakl = 0
                     attack = 0
                     invent = 10
                     textInventar(invent)
                       
                 
    if mos_x>908 and (mos_x<972): 
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(11)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 11
                     magPerdun(11)
                 else:
                     zakl = 0
                     attack = 0 
                     invent = 11         
                     textInventar(invent)
                       
                                                            
    if mos_x>976 and (mos_x<1040):  
        x_inside = True
    else: x_inside = False
    if mos_y>684 and (mos_y<748):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(12) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 12
                     magPerdun(12)
                 else: 
                     zakl = 0
                     attack = 0 
                     invent = 12         
                     textInventar(invent)
                      
                 
    if mos_x>772 and (mos_x<836):  
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(13) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 13
                     magPerdun(13)
                 else:  
                     zakl = 0
                     attack = 0
                     invent = 13
                     textInventar(invent)
                      
                 
    if mos_x>840 and (mos_x<904): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(14)
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 14
                     magPerdun(14)
                 else:  
                     zakl = 0
                     attack = 0
                     invent = 14
                     textInventar(invent)
                       
                 
    if mos_x>908 and (mos_x<972): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if botLocation[imHero] == 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(15) 
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 15
                     magPerdun(15)
                 else:
                     zakl = 0
                     attack = 0            
                     invent = 15
                     textInventar(invent)
                      
                                                            
    if mos_x>976 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 0 and newGame == 1:  
                     zakl = 0
                     attack = 0
                     invent = 16
                     textInventar(invent)
                 if botLocation[imHero] != 146 or botLocation[imHero] == 144 or botLocation[imHero] == 146 or botLocation[imHero] == 113 or botLocation[imHero] == 177 or botLocation[imHero] == 112 or botLocation[imHero] == 114 or botLocation[imHero] == 176 or botLocation[imHero] == 178:
                     buyInvent(16)      
                 elif botLocation[imHero] == 299 or botLocation[imHero] == 297 or botLocation[imHero] ==  266 or botLocation[imHero] == 265 or botLocation[imHero] == 267 or botLocation[imHero] == 330 or botLocation[imHero] == 329 or botLocation[imHero] == 331:
                     hijina = 16
                     magPerdun(16)
                 else:
                     zakl = 0
                     attack = 0            
                     invent = 16
                     textInventar(invent)
    
                    
    if mos_x>462 and (mos_x<526):  # Кнопка "Да"
        x_inside = True
    else: x_inside = False
    if mos_y>786 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if newGame == 1 and buttonNextStep == 0 and invent > 0:
                    if botLocation[imHero] != 146 or botLocation[imHero] != 144 or botLocation[imHero] != 146 or botLocation[imHero] != 113 or botLocation[imHero] != 177 or botLocation[imHero] != 112 or botLocation[imHero] != 114 or botLocation[imHero] != 176 or botLocation[imHero] != 178:
                        useInventar(invent)
                        yes = 1
                    else: yaNaRinke = 1    
                if yaNaRinke == 1:
                    marketPlace(1)
                    print("yes")
                if imBuyThis == 1: yes = 5; buyInvent(thisPlace)   
                if hijina == 1: heroPanel(hero)
                if hijinaMaga == 2: magDoIt(hijina)
 
                    
    if mos_x>530 and (mos_x<594):  # Кнопка "Нет"
        x_inside = True
    else: x_inside = False
    if mos_y>786 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if newGame == 1 and buttonNextStep == 0 and invent > 0:
                    if botLocation[imHero] != 146 or botLocation[imHero] != 144 or botLocation[imHero] != 146 or botLocation[imHero] != 113 or botLocation[imHero] != 177 or botLocation[imHero] != 112 or botLocation[imHero] != 114 or botLocation[imHero] != 176 or botLocation[imHero] != 178:
                        botInventar[imHero][invent-1] = 0
                        heroPanel(hero) 
                        no = 1 
                    else: yaNaRinke = 1    
                if yaNaRinke == 1:
                    marketPlace(2)   
                    print("no")
                if imBuyThis == 1: imBuyThis = 0; thisPlace = 0            
            
    
                
  


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

# Хижина мага
# 1 - говорить с магом, 2 - увеличить магическую силу, 3 - получить задание 
#      
#
#
#
#
#
#
# 
