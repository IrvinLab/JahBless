# -*- coding: utf-8 -*-
import pygame, sys, random
 
FPS = 60
xGameMap = 16 
yGameMap = 96 
xMap = 0
yMap = 0
n = 0
newGame = 0 # Переменная, которая означает, что идёт игра

# Переменные персонажа
hero = 0 # Код персонажа
step = 172 # Исходное положение на карте
xHero = 400
yHero = 256
expirience = 0
lvl = 1
rasa = 0
inventar = []
zaklinania = []
vozdeistvie = []
zdorovie = 0
mana = 0
sila = 0
lovkost = 0
ydacha = 0
zoloto = 0
serebro = 0
bronza = 0
hod = 0

# Время мира
den = 1
mesiac = 1
god = 1

newGameButton = 0
loadButton = 0
saveButton = 0
netGameButton = 0
settingsButton = 0
world = [] # Это игровое поле
tmp = 0
temp = 0 # Отладочная переменная, нужна для отслеживания состояния поля
pygame.init()
sc = pygame.display.set_mode((1056, 896))
clock = pygame.time.Clock()
pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896)) 

for n in range(480):
    world.append(n)
    world[n] = 0

def initGame(heroSelect):  # функция инициации игры
    global xHero
    global yHero
    global world
    global step
    
    global expirience
    global lvl
    global rasa
    global inventar
    global zaklinania
    global vozdeistvie
    global zdorovie
    global mana
    global sila
    global lovkost
    global ydacha
    global zoloto
    global serebro
    global bronza
    
    global den
    global mesiac
    global god

    # Герои
# 50 - Аками, 51 - Артес, 52 - Владыка Смерти, 53 - Детерок, 54 - Джепотай, 55 - Фарион
# 56 - Гаритос, 57 - Гендальф, 58 - Илидан, 59 - Джайна
# 60 - Келл, 61 - Келл Тузед, 62 - Магерион, 63 - Мефистофор, 64 - Паладин, 65 - Прадмур
# 66 - Саргарас, 67 - Саурон, 68 - Сильвана, 69 - Тралл, 70 - Утер, 71 - Варомир
# 72 - Вул Джин, 73 - Задира

     # Задаём начальные параметры персонажа
    if heroSelect == 50: # Akami
        expirience = 0
        lvl = 1
        rasa = 2
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 120
        mana = 50
        sila = 14
        lovkost = 4
        ydacha = 7
        zoloto = 0
        serebro = 12
        bronza = 0
        
    elif heroSelect == 51: # Artes
        expirience = 0
        lvl = 1
        rasa = 7
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 110
        mana = 30
        sila = 12
        lovkost = 4
        ydacha = 5
        zoloto = 0
        serebro = 9
        bronza = 50
        
    elif heroSelect == 52: # Death Owner
        expirience = 0
        lvl = 1
        rasa = 7
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [5,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 90
        mana = 100
        sila = 9
        lovkost = 3
        ydacha = 9
        zoloto = 0
        serebro = 0
        bronza = 0  

    elif heroSelect == 54: # DjePoTai
        expirience = 0
        lvl = 1
        rasa = 2
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 120
        mana = 60
        sila = 15
        lovkost = 5
        ydacha = 5
        zoloto = 0
        serebro = 0
        bronza = 150

    elif heroSelect == 55: # Farion
        expirience = 0
        lvl = 1
        rasa = 6
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 110
        mana = 80
        sila = 10
        lovkost = 4
        ydacha = 6
        zoloto = 0
        serebro = 0
        bronza = 200  

    elif heroSelect == 56: # Garitos
        expirience = 0
        lvl = 1
        rasa = 1
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 130
        mana = 30
        sila = 15
        lovkost = 5
        ydacha = 7
        zoloto = 0
        serebro = 5
        bronza = 0   

    elif heroSelect == 57: # Gendalf
        expirience = 0
        lvl = 1
        rasa = 1
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 85
        mana = 120
        sila = 9
        lovkost = 4
        ydacha = 9
        zoloto = 0
        serebro = 0
        bronza = 0   

    elif heroSelect == 58: # Illidan
        expirience = 0
        lvl = 1
        rasa = 2
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 120
        mana = 60
        sila = 11
        lovkost = 5
        ydacha = 5
        zoloto = 0
        serebro = 0
        bronza = 0  

    elif heroSelect == 59: # Jaina
        expirience = 0
        lvl = 1
        rasa = 2
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 100
        mana = 50
        sila = 9
        lovkost = 5
        ydacha = 10
        zoloto = 0
        serebro = 1
        bronza = 120   

    elif heroSelect == 60: # Kell
        expirience = 0
        lvl = 1
        rasa = 7
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [8,6,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 120
        mana = 80
        sila = 14
        lovkost = 5
        ydacha = 7
        zoloto = 0
        serebro = 0
        bronza = 200  

    elif heroSelect == 70: # Uter
        expirience = 0
        lvl = 1
        rasa = 1
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 150
        mana = 0
        sila = 15
        lovkost = 4
        ydacha = 8
        zoloto = 0
        serebro = 10
        bronza = 0   

    elif heroSelect == 72: # Vul Djin
        expirience = 0
        lvl = 1
        rasa = 6
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [7,11,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 120
        mana = 100
        sila = 12
        lovkost = 4
        ydacha = 8
        zoloto = 0
        serebro = 10
        bronza = 0         
    
    elif heroSelect == 68: # Silvana
        expirience = 0
        lvl = 1
        rasa = 2
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 110
        mana = 70
        sila = 11
        lovkost = 5
        ydacha = 4
        zoloto = 0
        serebro = 0
        bronza = 50  

    elif heroSelect == 65: # Pradmur
        expirience = 0
        lvl = 1
        rasa = 1
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 100
        mana = 0
        sila = 10
        lovkost = 4
        ydacha = 9
        zoloto = 0
        serebro = 5
        bronza = 0  

    elif heroSelect == 69: # Trall
        expirience = 0
        lvl = 1
        rasa = 6
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 140
        mana = 0
        sila = 17
        lovkost = 4
        ydacha = 5
        zoloto = 0
        serebro = 0
        bronza = 0      

    elif heroSelect == 73: # Zadira
        expirience = 0
        lvl = 1
        rasa = 6
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zdorovie = 120
        mana = 0
        sila = 15
        lovkost = 4
        ydacha = 7
        zoloto = 0
        serebro = 0
        bronza = 170         
        
    temp = 0
    step = 172
    xGameMap = 16 
    yGameMap = 96 
    den = 1
    mesiac = 1
    god = 1

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
    # Тут мы генерируем объекты игрового мира 
    n = 0
    for n in range(480):
        world.append(n)
        world[n] = 0
        
    n = 0
    xMap = 16 
    yMap = 96 
    for n in range(448):
        tmp = int(random.random()*22)
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
    print(" ")
    




for yMap in range(14): # Рисуем игровое поле
    
    for xMap in range(32):
        pix = pygame.image.load('Images/weed.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xGameMap,yGameMap))
        xGameMap += 32

    xGameMap = 16
    yGameMap += 32 # Закончили рисовать



pix = pygame.image.load('Images/new_game.jpg') # Рисуем кнопки
x_len = pix.get_width()
y_len = pix.get_height() 
sc.blit(pix, (16,16))

pix = pygame.image.load('Images/load.jpg')
x_len = pix.get_width()
y_len = pix.get_height() 
sc.blit(pix, (220,16))

pix = pygame.image.load('Images/save.jpg')
x_len = pix.get_width()
y_len = pix.get_height() 
sc.blit(pix, (424,16))

pix = pygame.image.load('Images/net_game.jpg')
x_len = pix.get_width()
y_len = pix.get_height() 
sc.blit(pix, (628,16))

pix = pygame.image.load('Images/option.jpg')
x_len = pix.get_width()
y_len = pix.get_height() 
sc.blit(pix, (832,16))



pygame.display.update()
 

while True:
    n = 0  # Это сотри
    temp = 0 # И это
    clock.tick(FPS) 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
            
        elif i.type == pygame.KEYDOWN and newGame == 1:
            
            if i.key == pygame.K_LEFT and xHero >= 18 and world[step-1] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xHero,yHero))
                xHero -= 32
                world[step] = 0
                step -= 1
                world[step] = hero
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")    # =======
            elif i.key == pygame.K_RIGHT and xHero <= 990 and world[step+1] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xHero,yHero))
                xHero += 32
                world[step] = 0
                step += 1
                world[step] = hero
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")   # =======
            elif i.key == pygame.K_UP and yHero >= 96 and world[step-32] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xHero,yHero))
                yHero -= 32
                world[step] = 0
                step -= 32
                world[step] = hero
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")  # =======
            elif i.key == pygame.K_DOWN and yHero <= 510 and world[step+32] == 0: 
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xHero,yHero))
                yHero += 32
                world[step] = 0
                step += 32
                world[step] = hero
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")  # =======


    mos_x, mos_y = pygame.mouse.get_pos() # Тут мы берём координаты мыши
    if newGame == 1: # Отображаем персонажа на игровом поле
        if hero == 50:
            pix = pygame.image.load('Images/akami_32.jpg')
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 51:
            pix = pygame.image.load('Images/artes_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 52:
            pix = pygame.image.load('Images/deathOwner_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 54:
            pix = pygame.image.load('Images/djepotai_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 55:
            pix = pygame.image.load('Images/farion_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 56:
            pix = pygame.image.load('Images/garitos_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 57:
            pix = pygame.image.load('Images/gendalf_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 58:
            pix = pygame.image.load('Images/illidan_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 59:
            pix = pygame.image.load('Images/jaina_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 60:
            pix = pygame.image.load('Images/kell_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 70:
            pix = pygame.image.load('Images/uter_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 72:
            pix = pygame.image.load('Images/vulDjin_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 68:
            pix = pygame.image.load('Images/silvana_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 65:
            pix = pygame.image.load('Images/pradmur_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 69:
            pix = pygame.image.load('Images/trall_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        if hero == 73:
            pix = pygame.image.load('Images/zadira_32.jpg') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (xHero,yHero))
        pygame.display.update()
        
#============================================================================================================================================    
#======================================================ОБРАБОТКА НАЖАТИЙ КНОПОК МЕНЮ=========================================================
#============================================================================================================================================
    if mos_x>16 and (mos_x<216): # Тут проверяем находтся ли мышь на кнопке Новая игра
        x_inside = True
    else: x_inside = False
    if mos_y>16 and (mos_y<66):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: # Если мышь находится внутри кнопки
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: # Переменную newGameButton нужно перевести в ноль после загрузки игры
                 newGameButton = 1
                 pix = pygame.image.load('Images/akami.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (16,548))
                 
                 pix = pygame.image.load('Images/artes.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (84,548))
                 
                 pix = pygame.image.load('Images/deathOwner.jpg')
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (152,548))
                 
                 pix = pygame.image.load('Images/djepotai.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (220,548))
                 
                 pix = pygame.image.load('Images/farion.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (16,616))
                 
                 pix = pygame.image.load('Images/garitos.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (84,616))
                 
                 pix = pygame.image.load('Images/gendalf.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (152,616))
                 
                 pix = pygame.image.load('Images/illidan.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (220,616))
                 
                 pix = pygame.image.load('Images/jaina.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (16,684))
                 
                 pix = pygame.image.load('Images/kell.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (84,684))
                 
                 pix = pygame.image.load('Images/uter.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (152,684))
                 
                 pix = pygame.image.load('Images/vulDjin.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (220,684))
                 
                 pix = pygame.image.load('Images/silvana.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (16,752))
                 
                 pix = pygame.image.load('Images/pradmur.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (84,752))
                 
                 pix = pygame.image.load('Images/trall.jpeg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (152,752))
                 
                 pix = pygame.image.load('Images/zadira.jpg') 
                 x_len = pix.get_width()
                 y_len = pix.get_height() 
                 sc.blit(pix, (220,752))
              
                 print("new game")
                 pygame.time.delay(500)
                 pass
                 # Переменную newGameButton нужно перевести в ноль после загрузки игры
                 # ===============
                 # 
                                  
    if mos_x>220 and (mos_x<420): # Тут проверяем находтся ли мышь на кнопке Загрузить
        x_inside = True
    else: x_inside = False
    if mos_y>16 and (mos_y<66):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 
                 pygame.time.delay(500)
                 print("load")
                 pass
                 # Какое-то событие
                 # ===============
                 # ===============
                 
    if mos_x>424 and (mos_x<624): # Тут проверяем находтся ли мышь на кнопке Сохранить
        x_inside = True
    else: x_inside = False
    if mos_y>16 and (mos_y<66):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 
                 pygame.time.delay(500)
                 print("save")
                 pass
                 # Какое-то событие
                 # ===============
                 # ===============
                 
    if mos_x>628 and (mos_x<828): # Тут проверяем находтся ли мышь на кнопке Сетевая игра
        x_inside = True
    else: x_inside = False
    if mos_y>16 and (mos_y<66):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 pygame.time.delay(500)
                 print("net game")
                 pass
                 # Какое-то событие
                 # ===============
                 # ===============
                 
    if mos_x>832 and (mos_x<1032): # Тут проверяем находтся ли мышь на кнопке Настройки
        x_inside = True
    else: x_inside = False
    if mos_y>16 and (mos_y<66):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 
                 pygame.time.delay(500)
                 print("settings")
                 pass
                 # Какое-то событие
                 # ===============
                 # ===============                 
#============================================================================================================================================
#==========================================================ОБРАБОТКА СОБЫТИЙ КНОПОК ДЕЙСТВИЙ================================================= 
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
                 pass
                 
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
                 pass                 
                 
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
                 pass                   
                                                            
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
                 pass
                 
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
                 pass
                 
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
                 pass                 
                 
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
                 pass                   
                                                            
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
                 pass  
                 
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
                 pass
                 
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
                 pass                 
                 
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
                 pass                   
                                                            
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
                 pass                                 
                 
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
                 pass
                 
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
                 pass                 
                 
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
                 pass                   
                                                            
    if mos_x>220 and (mos_x<284): 
        x_inside = True
    else: x_inside = False
    if mos_y>752 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                 if newGameButton == 1:
                     hero = 73
                     newGame = 1  
                     initGame(73) 
                     newGameButton = 0
                 pygame.time.delay(500)
                 pass                  
                 
                 
                    
    pygame.display.update()
    
    
# Объекты которые могут быть на карте и их номера
# 0 - Трава, 1 - Горы, 2 - Вода, 3 - Крестьянин(0 ур)
# 8 - рынок, 9 - вспаханная земля, 10 - портал
# 11 - Полуросль, 12 - Рожь, 13 - Картофель, 23 - Сундук, 24 - Врата города
# 25 - Таверна, 26 - Портал

# Герои
# 50 - Аками, 51 - Артес, 52 - Владыка Смерти, 53 - Детерок, 54 - Джепотай, 55 - Фарион
# 56 - Гаритос, 57 - Гендальф, 58 - Илидан, 59 - Джайна
# 60 - Келл, 61 - Келл Тузед, 62 - Магерион, 63 - Мефистофор, 64 - Паладин, 65 - Прадмур
# 66 - Саргарас, 67 - Саурон, 68 - Сильвана, 69 - Тралл, 70 - Утер, 71 - Варомир
# 72 - Вул Джин, 73 - Задира

# Войны
# 100 - Эльф 1 ур, 101 - Эльф 2 ур, 102 - Эльф 3 ур, 103 - гнолл 1 ур, 104 - гнолл 2 ур
# 105 - Гнолл 3 ур, 106 - Гном 1 ур, 107 - Гном 2 ур, 108 - Гном 3 ур, 109 - Гном 4 ур
# 110 - Гоблин 0 ур, 111 - Гоблин 1 ур, 112 - Гоблин 2 ур, 113 - Гоблин 3 ур
# 114 - Отшельник 1 ур, 115 - Отшельник 2 ур, 116 - Отшельник 3 ур
# 117 - Охотник за головами 1 ур, 118 - Человек, 119 - Монстр 1 ур, 120 - Монстр 2 ур
# 121 - Монстр 3 ур, 122 - Монстр 4 ур, 123 - Морлок 1 ур, 124 - Морлок 2 ур, 125 - Морлок 3 ур
# 126 - Наемник 1 ур, 127 - Наемник 2 ур, 128 - Наемник 3 ур, 129 - наемник 4 ур
# 130 - Некромант, 131 - Непобедимый 1 ур, 132 - Непобедимый 2 ур, 133 - Огр 1 ур, 134 - Огр 2 ур
# 135 - Оккультист, 136 - Орк 1 ур, 137 - Орк 2 ур, 138 - Орк 3 ур, 139 - Окр 4 ур, 140 - орк 5 ур
# 141 - Орк 6 ур, 142 - Орк 7 ур, 143 - Орк-шаман, 144 - Отступник, 145 - Разбойник, 146 - грабитель
# 147 - Красный огненный голем, 148 - Скелет 1 ур, 149 - Скелет 2 ур, 150 - Скелет 3 ур
# 151 - Скелет 4 ур, 152 - Скелет 5 ур, 153 - Скелет 6 ур, 154 - Скелет 7 ур, 155 - Скелет 8 ур
# 156 - Душекрад, 157 - Странник, 158 - Тролль 1 ур, 159 - Тролль 2 ур, 160 - Тролль 3 ур
# 161 - Тролль 4 ур, 162 - Тролль 5 ур, 163 - Тролль 6 ур, 164 - Вампир, 165 - Колдун
# 166 - Женщина-эльф 1 ур, 167 - Женщина-эльф 2 ур, 168 - Женщина-эльф 3 ур
# 169 - Женщина-эльф 4 ур, 170 - Женщина-эльф 5 ур, 171 - Женщина-эльф 6 ур
# 172 - Женщина-эльф 7 ур    
       
# Войны
# 100 - Эльф 1 ур, 101 - Эльф 2 ур, 102 - Эльф 3 ур, 103 - гнолл 1 ур, 104 - гнолл 2 ур
# 105 - Гнолл 3 ур, 106 - Гном 1 ур, 107 - Гном 2 ур, 108 - Гном 3 ур, 109 - Гном 4 ур
# 110 - Гоблин 0 ур, 111 - Гоблин 1 ур, 112 - Гоблин 2 ур, 113 - Гоблин 3 ур
# 114 - Отшельник 1 ур, 115 - Отшельник 2 ур, 116 - Отшельник 3 ур
# 117 - Охотник за головами 1 ур, 118 - Человек, 119 - Монстр 1 ур, 120 - Монстр 2 ур
# 121 - Монстр 3 ур, 122 - Монстр 4 ур, 123 - Морлок 1 ур, 124 - Морлок 2 ур, 125 - Морлок 3 ур
# 126 - Наемник 1 ур, 127 - Наемник 2 ур, 128 - Наемник 3 ур, 129 - наемник 4 ур
# 130 - Некромант, 131 - Непобедимый 1 ур, 132 - Непобедимый 2 ур, 133 - Огр 1 ур, 134 - Огр 2 ур
# 135 - Оккультист, 136 - Орк 1 ур, 137 - Орк 2 ур, 138 - Орк 3 ур, 139 - Окр 4 ур, 140 - орк 5 ур
# 141 - Орк 6 ур, 142 - Орк 7 ур, 143 - Орк-шаман, 144 - Отступник, 145 - Разбойник, 146 - грабитель
# 147 - Красный огненный голем, 148 - Скелет 1 ур, 149 - Скелет 2 ур, 150 - Скелет 3 ур
# 151 - Скелет 4 ур, 152 - Скелет 5 ур, 153 - Скелет 6 ур, 154 - Скелет 7 ур, 155 - Скелет 8 ур
# 156 - Душекрад, 157 - Странник, 158 - Тролль 1 ур, 159 - Тролль 2 ур, 160 - Тролль 3 ур
# 161 - Тролль 4 ур, 162 - Тролль 5 ур, 163 - Тролль 6 ур, 164 - Вампир, 165 - Колдун
# 166 - Женщина-эльф 1 ур, 167 - Женщина-эльф 2 ур, 168 - Женщина-эльф 3 ур
# 169 - Женщина-эльф 4 ур, 170 - Женщина-эльф 5 ур, 171 - Женщина-эльф 6 ур
# 172 - Женщина-эльф 7 ур    