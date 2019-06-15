# -*- coding: utf-8 -*-
import pygame, sys, random
 
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
ishZdorovie = 0
zdorovie = 0
ishMana = 0
mana = 0
sila = 0
lovkost = 0
ydacha = 0
zoloto = 0
serebro = 0
bronza = 0
hod = 0
zachita = 0

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
pygame.display.set_caption("Kings of New World")
clock = pygame.time.Clock()
pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896)) 

pygame.font.init()    
textNameHero = pygame.font.SysFont('Monospace Regular Bold', 23) # Текст отображающий имя игрока               
healt = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Здоровье
manna = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Ману
textSila = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Силу
textLovk = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Ловкость
textYdacha = pygame.font.SysFont('Monospace Regular', 20) # Текст отображающий Удачу
textZoloto = pygame.font.SysFont('Monospace Regular', 20)
textSerebro = pygame.font.SysFont('Monospace Regular', 20)
textBronza = pygame.font.SysFont('Monospace Regular', 20)

for n in range(480): # Забиваем мир нулями
    world.append(n)
    world[n] = 0

def visibleMagic(xMag, yMag, por): # Функция, отображающая заклинания
    global zaklinania
    print(zaklinania[por])
    if zaklinania[por] == 0:
        pix = pygame.image.load('Images/zero.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if zaklinania[por] == 100:
        pix = pygame.image.load('Images/attack.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if zaklinania[por] == 1:
        pix = pygame.image.load('Images/pronzauchaiaSmert.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if zaklinania[por] == 2:
        pix = pygame.image.load('Images/dobitIvoskresit.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if zaklinania[por] == 3:
        pix = pygame.image.load('Images/dospechiFenicha.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 4:
        pix = pygame.image.load('Images/krajaMagii.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 5:
        pix = pygame.image.load('Images/obman.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if zaklinania[por] == 6:
        pix = pygame.image.load('Images/ognennaiaSfera.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 7:
        pix = pygame.image.load('Images/jad.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if zaklinania[por] == 8:
        pix = pygame.image.load('Images/krovojadnost.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))        
    if zaklinania[por] == 9:
        pix = pygame.image.load('Images/lunniiObriad.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 10:
        pix = pygame.image.load('Images/mochLda.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 11:
        pix = pygame.image.load('Images/mogilniiLuch.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if zaklinania[por] == 12:
        pix = pygame.image.load('Images/molnia.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if zaklinania[por] == 13:
        pix = pygame.image.load('Images/pechatChaosa.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if zaklinania[por] == 14:
        pix = pygame.image.load('Images/pechatSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if zaklinania[por] == 15:
        pix = pygame.image.load('Images/poceluiSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))      
    if zaklinania[por] == 16:
        pix = pygame.image.load('Images/prokliatie.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if zaklinania[por] == 17:
        pix = pygame.image.load('Images/pronzauchiiKrik.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))         
    if zaklinania[por] == 18:
        pix = pygame.image.load('Images/reincarnation.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if zaklinania[por] == 19:
        pix = pygame.image.load('Images/sjiganieMani.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if zaklinania[por] == 20:
        pix = pygame.image.load('Images/vampirizm.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if zaklinania[por] == 21:
        pix = pygame.image.load('Images/vosstanovitSkeletov.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 22:
        pix = pygame.image.load('Images/lechenie.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if zaklinania[por] == 23:
        pix = pygame.image.load('Images/rasseiatChari.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if zaklinania[por] == 24:
        pix = pygame.image.load('Images/plenitDuchu.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))              
                                

def printMagic(numberMagic):
    if numberMagic == 0:
        visibleMagic(16,548,0)
    if numberMagic == 1:
        visibleMagic(84,548,1)
    if numberMagic == 2:
        visibleMagic(152,548,2)
    if numberMagic == 3:
        visibleMagic(220,548,3)
    if numberMagic == 4:
        visibleMagic(16,616,4)
    if numberMagic == 5:
        visibleMagic(84,616,5)
    if numberMagic == 6:
        visibleMagic(152,616,6)
    if numberMagic == 7:
        visibleMagic(220,616,7)
    if numberMagic == 8:
        visibleMagic(16,684,8)
    if numberMagic == 9:
        visibleMagic(84,684,9)
    if numberMagic == 10:
        visibleMagic(152,684,10)
    if numberMagic == 11:
        visibleMagic(220,684,11)
    if numberMagic == 12:
        visibleMagic(16,752,12)
    if numberMagic == 13:
        visibleMagic(84,752,13)
    if numberMagic == 14:
        visibleMagic(152,752,14)
    if numberMagic == 15:
        visibleMagic(220,752,15)
         
    
    
def heroPanel(myHero): # Рисуем панель героя с его картинкой и параметрами
    global expirience
    global lvl
    global rasa
    global inventar
    global zaklinania
    global vozdeistvie
    global ishZdorovie
    global zdorovie
    global ishMana
    global mana
    global sila
    global lovkost
    global ydacha
    global zoloto
    global serebro
    global bronza
    global zachita
    
    global den
    global mesiac
    global god
    
    xHero = 340
    yHero = 548
    if myHero == 50:
        pix = pygame.image.load('Images/akami.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Akami - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 51:
        pix = pygame.image.load('Images/artes.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Artes - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 52:
        pix = pygame.image.load('Images/deathOwner.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Death Owner - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 54:
        pix = pygame.image.load('Images/djepotai.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Dje Potai - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 55:
        pix = pygame.image.load('Images/farion.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Farion - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 56:
        pix = pygame.image.load('Images/garitos.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Garitos - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 57:
        pix = pygame.image.load('Images/gendalf.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Gendalf - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 58:
        pix = pygame.image.load('Images/illidan.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Illidan - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 59:
        pix = pygame.image.load('Images/jaina.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Jaina - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 60:
        pix = pygame.image.load('Images/kell.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Kell - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 70:
        pix = pygame.image.load('Images/uter.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Uter - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 72:
        pix = pygame.image.load('Images/vulDjin.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Vul Djin - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 68:
        pix = pygame.image.load('Images/silvana.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Silvana - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 65:
        pix = pygame.image.load('Images/pradmur.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Pradmur - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 69:
        pix = pygame.image.load('Images/trall.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Trall - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 73:
        pix = pygame.image.load('Images/zadira.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = "Zadira - " + str(lvl) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
       
    
    variableHealt = "" + str(zdorovie) + " / " + str(ishZdorovie) # переменная типа String отображающая здоровье как ххх/ххх
    healtObj = healt.render(variableHealt, False, (0, 255, 0)) # Создали объект типа "текст" 
    sc.blit(healtObj,(290, 631)) # Отображаем здоровье
    
    variableMana = "" + str(mana) + " / " + str(ishMana) # переменная типа String отображающая ману как ххх/ххх
    manaObj = manna.render(variableMana, False, (0, 0, 255)) # Создали объект типа "текст" 
    sc.blit(manaObj,(290, 644)) # Отображаем ману
    
    variableSila = "Sila: " + str(sila) 
    silaObj = textSila.render(variableSila, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(silaObj,(290, 657)) 
    
    variableLovk = "Lovkost: " + str(lovkost) 
    lovkObj = textLovk.render(variableLovk, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(lovkObj,(290, 670)) 
    
    variableYdacha = "Ydacha: " + str(ydacha) 
    ydachaObj = textYdacha.render(variableYdacha, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(ydachaObj,(290, 683))
    
    variableZoloto = "Zoloto: " + str(zoloto) 
    zolotoObj = textZoloto.render(variableZoloto, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(zolotoObj,(290, 709))
    
    variableSerebro = "Serebro: " + str(serebro) 
    serebroObj = textSerebro.render(variableSerebro, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(serebroObj,(290, 722))
    
    variableBronza = "Bronza: " + str(bronza) 
    bronzaObj = textBronza.render(variableBronza, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(bronzaObj,(290, 735))
    
    pygame.display.update()  
    # ============================================================================================

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
    global ishZdorovie
    global zdorovie
    global ishMana
    global mana
    global sila
    global lovkost
    global ydacha
    global zoloto
    global serebro
    global bronza
    global zachita
    
    global den
    global mesiac
    global god
    pygame.draw.rect(sc, (255, 255, 255), (0, 548, 1056, 896)) 
     # Задаём начальные параметры персонажа
    if heroSelect == 50: # Akami
        expirience = 0
        lvl = 1
        rasa = 2
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ishZdorovie = 120
        zdorovie = 120
        mana = 50
        ishMana = 50
        sila = 14
        lovkost = 4
        ydacha = 7
        zoloto = 0
        serebro = 3
        bronza = 0
        
    elif heroSelect == 51: # Artes
        expirience = 0
        lvl = 1
        rasa = 7
        inventar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        zaklinania = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ishZdorovie = 110
        zdorovie = 110
        mana = 0
        ishMana = 0
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
        ishZdorovie = 90
        zdorovie = 90
        mana = 100
        ishMana = 100
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
        ishZdorovie = 120
        zdorovie = 120
        mana = 60
        ishMana = 60
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
        ishZdorovie = 110
        zdorovie = 110
        mana = 80
        ishMana = 80
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
        ishZdorovie = 130
        zdorovie = 130
        mana = 0
        ishMana = 0
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
        zaklinania = [8,22,6,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ishZdorovie = 85
        zdorovie = 85
        mana = 120
        ishMana = 120
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
        ishZdorovie = 120
        zdorovie = 120
        mana = 60
        ishMana = 60
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
        ishZdorovie = 100
        zdorovie = 100
        mana = 50
        ishMana = 50
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
        zaklinania = [10,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        vozdeistvie = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ishZdorovie = 120
        zdorovie = 120
        mana = 80
        ishMana = 80
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
        ishZdorovie = 150
        zdorovie = 150
        mana = 0
        ishMana = 0
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
        ishZdorovie = 120
        zdorovie = 120
        mana = 100
        ishMana = 100
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
        ishZdorovie = 110
        zdorovie = 110
        mana = 70
        ishMana = 70
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
        ishZdorovie = 100
        zdorovie = 100
        mana = 0
        ishMana = 0
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
        ishZdorovie = 140
        zdorovie = 140
        mana = 0
        ishMana = 0
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
        ishZdorovie = 120
        zdorovie = 120
        mana = 0
        ishMana = 0
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
    
    
    heroPanel(heroSelect)  # Вызов функции рисования панели
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
    zachita = 0 # Обнуляем защиту при новой игре
    n = 0
    for n in range(16): # Рисуем иконки заклинаний
        #print(n)
        printMagic(n)
    # ==========================================================================================




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
    if newGame == 1: # Отображаем персонажей на игровом поле
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
#==================================================ОБРАБОТКА НАЖАТИЙ КНОПОК ИГРОВОГО ПОЛЯ====================================================
#============================================================================================================================================

    #===================================================1 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    #===================================================2 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    #===================================================3 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass                                                                                                         
    
    #===================================================4 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass   
                
    #===================================================5 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    #===================================================6 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    #===================================================7 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass
            
    #===================================================8 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass  
            
    #===================================================9 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass    
            
    #===================================================10 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass    
            
    #===================================================11 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass  
            
    #===================================================12 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass 
            
    #===================================================13 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass     
            
    #===================================================14 ряд===============================================
    if mos_x>17 and (mos_x<47): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>369 and (mos_x<339): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
            pass                                                 
                                                                                                                                            
        
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
                 
                 pix = pygame.image.load('Images/trall.jpg') 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1:  # Нажали на заклинание 
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
                 if newGameButton == 0 and newGame == 1: # Нажали на заклинание 
                     pass 
                 
                 
                    
    pygame.display.update()
    
    
# Объекты которые могут быть на карте и их номера
# 0 - Трава, 1 - Горы, 2 - Вода, 3 - жилище зельевара, 4 - лачуга шамана, 5 - хижина мага, 6 - кузница,
# 7 - дом коллекционера, 8 - рынок, 9 - вспаханная земля, 10 - портал
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
