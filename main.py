# -*- coding: utf-8 -*-
import pygame, sys, random
import pygame.freetype
 
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
imHero = 0
hero = 0 # Код персонажа
step = 172 # Исходное положение на карте
xHero = 400
yHero = 256
expirience = 0
expToLvlUp = 1000 
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
botZoloto = []
botSerebro = []
botBronza = []
hod = 0
zachita = 0
attack = 0
zakl = 0
invent = 0
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
botDeistvie = [] # Сколько времени действует заклинание. Пример: botVozdeistvie[n] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                 #                                                  botDeistvie[n] = [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                 #                                             Это значит, что защита Заклинание Феникса действует 10 ходов
posohSmerti = 0  
posohSveta = 0
posohProzrenia = 0
posohVoli = 0
posohVechnoiJizni = 0 # Посохи

yes = 0
no = 0  
# Время мира
den = 1
mesiac = 1
god = 1

newGameButton = 0
loadButton = 0
saveButton = 0
netGameButton = 0
settingsButton = 0
buttonNextStep = 0 # Кнопка следующего хода
world = [] # Это игровое поле
tmp = 0
temp = 0 # Отладочная переменная, нужна для отслеживания состояния поля
zyxel = 0
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
textDescription = pygame.font.SysFont('Monospace Regular', 20) #Описание объекта
textHod = pygame.font.SysFont('Monospace Regular', 20) # Отображает количество оставшегося хода
textExpirience = pygame.font.SysFont('Monospace Regular', 20) # Отображает опыт

for n in range(480): # Забиваем мир нулями
    world.append(n)
    world[n] = 0

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
    if botInventar[imHero][dasLut-1] == 55 and yes == 1:        
        if botMana[imHero] >= 100:
            posohSmerti = 1
            yes = 0
    
    if botInventar[imHero][dasLut-1] > 0 and botInventar[imHero][dasLut-1] <= 25:
        invent = 0
        attack = 0
        botInventar[imHero][dasLut-1] = 0
        printInventar(dasLut-1)
    heroPanel(hero)
def textInventar(nomInv):
    global botInventar
    global hero
    heroPanel(hero)
    if botInventar[0][nomInv-1] == 1:
        variableName = u"Зелье здоровья 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+30 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 2:
        variableName = u"Зелье здоровья 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+65 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 3:
        variableName = u"Зелье здоровья 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+150 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 4:
        variableName = u"Зелье здоровья 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+320 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 5:
        variableName = u"Зелье здоровья 5 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+675 Здоровья "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 6:
        variableName = u"Зелье маны 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+60 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 7:
        variableName = u"Зелье маны 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+130 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 8:
        variableName = u"Зелье маны 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+260 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 9:
        variableName = u"Зелье маны 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+520 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 10:
        variableName = u"Зелье маны 5 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+1100 Маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 11:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 12:
        variableName = u"Зелье рассеивания"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Действует подобно заклинанию"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Рассеять Чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 13:
        variableName = u"Зелье Кипящей крови 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 14:
        variableName = u"Зелье Кипящей крови 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 15:
        variableName = u"Зелье Кипящей крови 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 16:
        variableName = u"Зелье Кипящей крови 4 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+20 силы на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 17:
        variableName = u"Зелье Деревянной кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 18:
        variableName = u"Зелье Каменной кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 19:
        variableName = u"Зелье Обсидиановой кожи"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 защиты на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 20:
        variableName = u"Зелье Паука"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+2 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 21:
        variableName = u"Зелье Ящерицы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+3 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 22:
        variableName = u"Зелье Пантеры"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 Ловкости на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 23:
        variableName = u"Зелье Леприкона 1 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+5 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 24:
        variableName = u"Зелье Леприкона 2 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+8 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 25:
        variableName = u"Зелье Леприкона 3 ур."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"+12 Удачи на 10 ходов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 26:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[0][nomInv-1] == 27:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[0][nomInv-1] == 28:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[0][nomInv-1] == 29:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 30:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))        
    if botInventar[0][nomInv-1] == 31:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))
    if botInventar[0][nomInv-1] == 32:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))
    if botInventar[0][nomInv-1] == 33:
        variableName = u"Книга 1"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 34:
        variableName = u"Книга 2"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 35:
        variableName = u"Книга 3"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 36:
        variableName = u"Книга 4"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560))        
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 37:
        variableName = u"Книга 5"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 38:
        variableName = u"Книга 6"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 39:
        variableName = u"Книга 7"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))       
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 40:
        variableName = u"Книга 8"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 41:
        variableName = u"Книга 9"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 42:
        variableName = u"Книга 10"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Где описание?"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 43:
        variableName = u"Ботинки Гонца (1ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Ногам удобно - двигаешься быстро"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))       
        variableName = u"+2 ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 44:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 45:
        variableName = u"Ботинки Скитальца (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Верный друг искателя приключений"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+6 Ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 45:
        variableName = u"Ботинки Скитальца (3ур.)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Верный друг искателя приключений"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+6 Ловкости"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 46:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 47:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 48:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 49:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 50:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 51:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 52:
        variableName = u"Банка"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Отнесите эту банку зельевару"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 53:
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
        variableName = u" Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 54:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 55:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 56:
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
        variableName = u"Требует 50 Маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))
    if botInventar[0][nomInv-1] == 57:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 58:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 59:
        variableName = u"Рунный браслет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Зачарованный магией Порядка браслет"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+3 Защиты +5 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 60:
        variableName = u"Меч 1 ур"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Стандартное вооружение пехотинца"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
        variableName = u"+3 Силы"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 61:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 62:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 63:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 64:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 65:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 66:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 67:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 68:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if botInventar[0][nomInv-1] == 69:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))        
    if botInventar[0][nomInv-1] == 70:
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
        variableName = u"Использовать - (Да) Выкинуть - (Нет)"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
        
    if botInventar[0][nomInv-1] > 0:
        pix = pygame.image.load('Images/yes.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (462,786))    
    
        pix = pygame.image.load('Images/no.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (530,786))    
                
            
def textMagic(numerCeil):
    global botZaklinania 
    global hero
    heroPanel(hero)
    if botZaklinania[0][numerCeil-1] == 1:
        variableName = u"Пронзающая смерть"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Мощное боевое заклинание 5 уровня "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"-200 Здоровья"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 200 маны "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        #variableName = u"и ещё много чего. У короля есть сокровища"
        #nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        #sc.blit(nameObj,(440, 640))  
        #variableName = u"которые охраняет свита отборных бойцов"
        #nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        #sc.blit(nameObj,(440, 660)) 
    if botZaklinania[0][numerCeil-1] == 2:
        variableName = u"Добить и воскресить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Базовое магическое заклинание"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"начинающего некроманта. Создаёт скелета"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"из существа при условии, чтоего здоровье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = u"меньше или равно 30."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"Требует 30 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660)) 
    if botZaklinania[0][numerCeil-1] == 3:
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
    if botZaklinania[0][numerCeil-1] == 4:
        variableName = u"Кража магии"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Отнимает всю ману противника и половину"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"отнятой маны прибавляет заклинателю"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 20 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
    if botZaklinania[0][numerCeil-1] == 5:
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
    if botZaklinania[0][numerCeil-1] == 6:
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
    if botZaklinania[0][numerCeil-1] == 7:
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
    if botZaklinania[0][numerCeil-1] == 8:
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
    if botZaklinania[0][numerCeil-1] == 9:
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
    if botZaklinania[0][numerCeil-1] == 10:
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
    if botZaklinania[0][numerCeil-1] == 11:
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
    if botZaklinania[0][numerCeil-1] == 12:
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
    if botZaklinania[0][numerCeil-1] == 13:
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
        variableName = u"Отравление, более тогоотнимает всю"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = u"ману и защиту. Защита восстанавливается"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))     
        variableName = u"через 10 ходов."
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680))             
        variableName = u"Требует 100 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 700))             
    if botZaklinania[0][numerCeil-1] == 14:
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
    if botZaklinania[0][numerCeil-1] == 15:
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
    if botZaklinania[0][numerCeil-1] == 16:
        variableName = u"Проклятье"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Заклинание Смерти 1 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"На 5 ходов защита будет равна нулю"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 75 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
    if botZaklinania[0][numerCeil-1] == 17:
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
    if botZaklinania[0][numerCeil-1] == 18:
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
    if botZaklinania[0][numerCeil-1] == 19:
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
    if botZaklinania[0][numerCeil-1] == 20:
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
    if botZaklinania[0][numerCeil-1] == 21:
        variableName = u"Пока это восстановить скелетов"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Это заклинание нужно исправить"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))
    if botZaklinania[0][numerCeil-1] == 22:
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
    if botZaklinania[0][numerCeil-1] == 23:
        variableName = u"Рассеять чары"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = u"Магия Порядка 2 уровня"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = u"Рассеивает чары вокруг заклинателя "
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = u"Требует 40 маны"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))
    if botZaklinania[0][numerCeil-1] == 24:
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
                                      
def ubiraemTrup(trup):
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
    global imHero
    
    otdaiLut(imHero, trup)
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
    
    print ("Колдовство: ",nom, poriad, vragBot)
    if botLocation[nom] == botLocation[vragBot] or botLocation[nom] == botLocation[vragBot]-1 or botLocation[nom] == botLocation[vragBot]+1 or botLocation[nom] == botLocation[vragBot]-32 or botLocation[nom] == botLocation[vragBot]-31 or botLocation[nom] == botLocation[vragBot]-33 or botLocation[nom] == botLocation[vragBot]+32 or botLocation[nom] == botLocation[vragBot]+31 or botLocation[nom] == botLocation[vragBot]+33:
        if botZaklinania[nom][poriad] == 100: # Это удар мечом
            botHod[nom] -= 1
            if botSila[nom] > botZachita[vragBot]:
                botZdorovie[vragBot] -= botSila[nom] - botZachita[vragBot]
    
        if botZaklinania[nom][poriad] == 1:  # Пронзающая смерть
            if botMana[nom] >= 200: # Если хватает маны, то колдуем
                botMana[nom] -= 200
                botZdorovie[vragBot] -= 200
                botHod[nom] -= 1
                print("Пронзающая смерть")
                botExpirience[nom] += 100
                yaKastanul = 1
        
        if botZaklinania[nom][poriad] == 2: # Добить и воскресить
            if botMana[nom] >= 100 and botZdorovie[vragBot] <= 30:
                botMana[nom] -= 100
                yaKastanul = 1
                botHod[nom] -= 1
                print("Создаём скелета")
                if botLvl[vragBot] == 1 or botLvl[vragBot] == 2:
                    botVariant[vragBot] = 148
                    botLvl[vragBot] = 1
                    botZdorovie[vragBot] = 50
                    botIshZdorovie[vragBot] = 50
                    botMana[vragBot] = 0
                    botIshMana[vragBot] = 0
                    botZaklinania[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 5
                    botLovkost[vragBot] = 3
                    botYdacha[vragBot] = 1
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] == 3:
                    botVariant[vragBot] = 149 
                    botLvl[vragBot] = 2
                    botZdorovie[vragBot] = 90
                    botIshZdorovie[vragBot] = 90
                    botMana[vragBot] = 0
                    botIshMana[vragBot] = 0
                    botZaklinania[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 9
                    botLovkost[vragBot] = 4
                    botYdacha[vragBot] = 2
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] == 4:
                    botVariant[vragBot] = 150
                    botLvl[vragBot] = 3
                    botZdorovie[vragBot] = 145
                    botIshZdorovie[vragBot] = 145
                    botMana[vragBot] = 0
                    botIshMana[vragBot] = 0
                    botZaklinania[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 13
                    botLovkost[vragBot] = 4
                    botYdacha[vragBot] = 3
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] == 5:
                    botVariant[vragBot] = 151
                    botLvl[vragBot] = 4
                    botZdorovie[vragBot] = 190
                    botIshZdorovie[vragBot] = 190
                    botMana[vragBot] = 60
                    botIshMana[vragBot] = 60
                    botZaklinania[vragBot]=[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 18
                    botLovkost[vragBot] = 4
                    botYdacha[vragBot] = 3
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] == 6:
                    botVariant[vragBot] = 152 
                    botLvl[vragBot] = 5
                    botZdorovie[vragBot] = 245
                    botIshZdorovie[vragBot] = 245
                    botMana[vragBot] = 120
                    botIshMana[vragBot] = 120
                    botZaklinania[vragBot]=[2,11,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 26
                    botLovkost[vragBot] = 5
                    botYdacha[vragBot] = 5
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] == 7:
                    botVariant[vragBot] = 153
                    botLvl[vragBot] = 6
                    botZdorovie[vragBot] = 315
                    botIshZdorovie[vragBot] = 315
                    botMana[vragBot] = 170
                    botIshMana[vragBot] = 170
                    botZaklinania[vragBot]=[2,11,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 36
                    botLovkost[vragBot] = 5
                    botYdacha[vragBot] = 8
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] == 8:    
                    botVariant[vragBot] = 154
                    botLvl[vragBot] = 7
                    botZdorovie[vragBot] = 395
                    botIshZdorovie[vragBot] = 395
                    botMana[vragBot] = 240
                    botIshMana[vragBot] = 240
                    botZaklinania[vragBot]=[2,11,12,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 36
                    botLovkost[vragBot] = 5
                    botYdacha[vragBot] = 8
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if botLvl[vragBot] >= 9:        
                    botVariant[vragBot] = 155
                    botLvl[vragBot] = 8
                    botZdorovie[vragBot] = 500
                    botIshZdorovie[vragBot] = 500
                    botMana[vragBot] = 290
                    botIshMana[vragBot] = 290
                    botZaklinania[vragBot]=[2,11,12,15,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[vragBot] = 50
                    botLovkost[vragBot] = 5
                    botYdacha[vragBot] = 12
                    botHod[vragBot] = botLovkost[vragBot]
                    botVozdeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[vragBot] = botAlgoritm[nom]
                    world[botLocation[vragBot]] = botVariant[vragBot]
                    botDeistvie[vragBot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                botExpirience[nom] += 50    
            
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
                            botVozdeistvie[vragBot][n] = 3
                            botDeistvie[vragBot][n] = 10
                            botMana[nom] -= 30
                            botExpirience[nom] += 10
                            break        
                n = 0
                yaKastanul = 1
        if botZaklinania[nom][poriad] == 4: # Кража магии
            botHod[nom] -= 1
            if botMana[nom] >= 20:
                botMana[nom] -= 20
                if botMana[vragBot] > 100:
                    botMana[vragBot] -= 100
                    botExpirience[nom] += 30
                else:
                    botMana[vragBot] = 0    
                    botExpirience[nom] += 30            
                yaKastanul = 1
        if botZaklinania[nom][poriad] == 5: # Обман
            if botMana[nom] >= 50:
                botHod[nom] -= 1
                botMana[nom] -= 50
                botExpirience[nom] += 10
                botAlgoritm[vragBot] = 0
                yaKastanul = 1
        if botZaklinania[nom][poriad] == 6: # Огненная сфера
            if botMana[nom] >= 15:
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
                            botVozdeistvie[vragBot][n] = 8
                            botDeistvie[vragBot][n] = 5
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
            if botMana[nom] >= 70:
                botMana[nom] -= 70
                botZdorovie[vragBot] -= 70
                botExpirience[nom] += 40
                botHod[nom] -= 1
                yaKastanul = 1
        if botZaklinania[nom][poriad] == 13: # Печать Хаоса
            if botMana[nom] >= 100:
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
                            botMana[nom] -= 100
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
        if botZaklinania[nom][poriad] == 16: # Проклятье
            if botMana[nom] >= 75:
                botHod[nom] -= 1
                n = 0
                disable = 0
                for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                    if botVozdeistvie[vragBot][n] == 16:
                        dissable = 1
                        break
                if disable == 0:        
                    for n in range(15):
                        if botVozdeistvie[vragBot][n] == 0:
                            botVozdeistvie[vragBot][n] = 16
                            botExpirience[nom] += 20
                            botDeistvie[vragBot][n] = 1000
                            botMana[nom] -= 75
                            break        
                n = 0
                yaKastanul = 1  
        if botZaklinania[nom][poriad] == 17: # Пронзающий крик
            if botMana[nom] >= 30:
                botMana[nom] -= 30
                botZdorovie[vragBot] -= 50
                botExpirience[nom] += 20
                botHod[nom] -= 1
                yaKastanul = 1
        if botZaklinania[nom][poriad] == 18: # Регенерация
            if botMana[nom] >= 40:
                botHod[nom] -= 1
                n = 0
                disable = 0
                for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                    if botVozdeistvie[vragBot][n] == 18:
                        dissable = 1
                        break
                if disable == 0:        
                    for n in range(15):
                        if botVozdeistvie[vragBot][n] == 0:
                            botVozdeistvie[vragBot][n] = 18
                            botDeistvie[vragBot][n] = 1000
                            botMana[nom] -= 40
                            botExpirience[nom] += 10
                            break        
                n = 0
                yaKastanul = 1  
        if botZaklinania[nom][poriad] == 19: # Сжигание маны
            if botMana[nom] >= 15:
                botMana[nom] -= 15
                botExpirience[nom] += 10
                botMana[vragBot] = 0
                botHod[nom] -= 1
                yaKastanul = 1
        if botZaklinania[nom][poriad] == 20: # Вампиризм
            if botMana[nom] >= 55:
                botHod[nom] -= 1
                n = 0
                disable = 0
                for n in range(15): # Если бот не под действием этого заклинания, тогда разрешаем заклинание
                    if botVozdeistvie[vragBot][n] == 20:
                        dissable = 1
                        break
                if disable == 0:        
                    for n in range(15):
                        if botVozdeistvie[vragBot][n] == 0:
                            botVozdeistvie[vragBot][n] = 20
                            botDeistvie[vragBot][n] = 10
                            botMana[nom] -= 55
                            botExpirience[nom] += 10
                            break        
                n = 0
                yaKastanul = 1  
        if botZaklinania[nom][poriad] == 21: # Хрен знает что за заклинание
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
        if botZaklinania[nom][poriad] == 23: # Рассеять чары
            botVozdeistvie[nom] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            botDeistvie[nom] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            n = 0
            for n in range(1000):
                if botLocation[n] == botLocation[nom]-1 or botLocation[n] == botLocation[nom]+1 or botLocation[n] == botLocation[nom]-31 or botLocation[n] == botLocation[nom]-32 or botLocation[n] == botLocation[nom]-33 or botLocation[n] == botLocation[nom]+31 or botLocation[n] == botLocation[nom]+32 or botLocation[n] == botLocation[nom]+33:
                    botVozdeistvie[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botDeistvie[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    zyxel = 1
                    
                if zyxel == 1:
                    botMana[nom] -= 40
                    botExpirience[nom] += 10
                    zyxel = 0   
                    botHod[nom] -= 1 
            n = 0
        if botZaklinania[nom][poriad] == 24:
            yaKastanul = 1
        if botZaklinania[nom][poriad] == 25:
            yaKastanul = 1
        if botZaklinania[nom][poriad] == 26:
            yaKastanul = 1
        if botZaklinania[nom][poriad] == 27:
            yaKastanul = 1
        if botZaklinania[nom][poriad] == 28:
            yaKastanul = 1  
    
        
    if botZdorovie[vragBot] <= 0: 
        otdaiLut(nom, vragBot)
        ubiraemTrup(vragBot)    
    
    worldUpdate()
    heroPanel(hero)
    return yaKastanul 

def otdaiLut(nom, vragBot):
    print(botInventar[vragBot])
    if botZdorovie[vragBot] <= 0: 
        botExpirience[nom] += int(botIshZdorovie[vragBot] / 2)
        tempEnum = 0
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
    
def botVragBlizko(nomerBota, xBota, yBota, locat, vari, vrag, local):  # Обрабатываем реакцию на присутвие персонажей и NPC
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
    global zakl
    global botDeistvie
    jah = 0
    n = 1
    mag = 0
    if botRasa[nomerBota] == 1:
        for jah in range(1000):
            if botLocation[jah] == local:
                #print (vari, "Я человек, вижу бота номер:", jah, "Расы: ", botRasa[jah])
                if botAlgoritm[jah] == 3:
                    botAlgoritmes(nomerBota)
                    #print("Это свой")
                    
                if botAlgoritm[jah] != 3: # Если это враг, тогда бьём в морду
                    if botMana[n] <= 0:
                        if botSila[nomerBota] > botZachita[jah]:
                            botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                            botHod[nomerBota] -= 1
                            if botZdorovie[jah] <= 0: 
                                otdaiLut(nomerBota, jah)
                                ubiraemTrup(jah) 
                        
                    if botMana[n] > 0:
                        for mag in range(16):
                            if botZaklinania[n][mag] != 0:
                                botKoldun(n,mag,jah)
                                 
                               
    if botRasa[nomerBota] == 2:
        for jah in range(1000):
            if botLocation[jah] == local:
                print (vari, "Я эльф, вижу жижу номер:", jah, "Расы: ", botRasa[jah])
                if botAlgoritm[jah] == 3:
                    botAlgoritmes(nomerBota)
                    print ("Это свой")
                if botAlgoritm[jah] != 3:
                    if botSila[nomerBota] > botZachita[jah]:
                        botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                        botHod[nomerBota] -= 1
                        if botZdorovie[jah] <= 0: 
                                otdaiLut(nomerBota, jah)
                                ubiraemTrup(jah) 
                
    if botRasa[nomerBota] == 3:
        for jah in range(1000):
            if botLocation[jah] == local:
                #print (vari, "Я гном, вижу бота номер:", jah, "Расы: ", botRasa[jah])
                if botAlgoritm[jah] == 3:
                    botAlgoritmes(nomerBota)
                    #print ("Это свой")
                if botAlgoritm[jah] != 3:
                    if botSila[nomerBota] > botZachita[jah]:
                        botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                        botHod[nomerBota] -= 1
                        if botZdorovie[jah] <= 0: 
                                otdaiLut(nomerBota, jah)
                                ubiraemTrup(jah) 
                    
    if botRasa[nomerBota] == 4:
        for jah in range(1000):
            if botLocation[jah] == local:
                #print (vari, "Я гоблин, вижу бота номер:", jah, "Расы: ", botRasa[jah])
                if botAlgoritm[jah] == 3:
                    botAlgoritmes(nomerBota)
                    #print ("Это свой")   
                if botAlgoritm[jah] != 3:
                    if botSila[nomerBota] > botZachita[jah]:
                        botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                        botHod[nomerBota] -= 1
                        if botZdorovie[jah] <= 0: 
                                otdaiLut(nomerBota, jah)
                                ubiraemTrup(jah) 

    if botRasa[nomerBota] == 5: # Это монстр
        for jah in range(1000):
            if botLocation[jah] == local:
                if botSila[nomerBota] > botZachita[jah]:
                    botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                    botHod[nomerBota] -= 1     
                    if botZdorovie[jah] <= 0: 
                        otdaiLut(nomerBota, jah)
                        ubiraemTrup(jah)                     
    
    if botRasa[nomerBota] == 6:
        for jah in range(1000):
            if botLocation[jah] == local:
                #print (vari, "Я орк, вижу бота номер:", jah, "Расы: ", botRasa[jah])
                if botAlgoritm[jah] == 4:
                    botAlgoritmes(nomerBota)
                    #print ("Это свой") 
                if botAlgoritm[jah] != 4 or botRasa[jah] == 5:   
                    if botSila[nomerBota] > botZachita[jah]:
                        botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                        botHod[nomerBota] -= 1
                        if botZdorovie[jah] <= 0: 
                                otdaiLut(nomerBota, jah)
                                ubiraemTrup(jah) 

    if botRasa[nomerBota] == 7:
        for jah in range(1000):
            if botLocation[jah] == local:
                #print (vari, "Я нежить, вижу бота номер:", jah, "Расы: ", botRasa[jah])
                if botAlgoritm[jah] == 4:
                    botAlgoritmes(nomerBota)
                    #print ("Это свой")                       
                if botAlgoritm[jah] != 4 or botRasa[jah] == 5:
                    if botSila[nomerBota] > botZachita[jah]:
                        botZdorovie[jah] -= botSila[nomerBota] - botZachita[jah]
                        botHod[nomerBota] -= 1
                        if botZdorovie[jah] <= 0: 
                                otdaiLut(nomerBota, jah)
                                ubiraemTrup(jah) 
    
    zakl = 0
        
def botAlgoritmes(yaBot): # Тут мы обрабатываем алгоритмы ботов, их брождение по карте
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
    if botAlgoritm[yaBot] == 3: # =================================================== Алгоритм добра =======================================
        if botAlgoritm[yaBot] == 3: # Идём вниз 
            if botStep[yaBot] == 0:  # and world[botLocation[yaBot]+32] == 0
                if world[botLocation[yaBot]+32] == 0 and yBot[yaBot] < 512:   
                    pix = pygame.image.load('Images/weed.jpg')
                    x_len = pix.get_width()
                    y_len = pix.get_height() 
                    sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                    yBot[yaBot] += 32
                    world[botLocation[yaBot]] = 0
                    world[botLocation[yaBot]+32] = botVariant[yaBot]
                    botLocation[yaBot] += 32
                    worldUpdate()
                
                if world[botLocation[yaBot]+32] != 0:
                    if world[botLocation[yaBot]-1] == 0 and xBot[yaBot] > 16: # Если нельзя идти вниз то пробуем двинуться влево
                        pix = pygame.image.load('Images/weed.jpg')
                        x_len = pix.get_width()
                        y_len = pix.get_height() 
                        sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                        xBot[yaBot] -= 32
                        world[botLocation[yaBot]] = 0
                        world[botLocation[yaBot]-1] = botVariant[yaBot]
                        botLocation[yaBot] -= 1
                        worldUpdate()  
                    
                    if world[botLocation[yaBot]-1] != 0: # Если нельзя влево пойти, то мы идём вправо
                        if world[botLocation[yaBot]+1] == 0 and xBot[yaBot] < 1008:
                            pix = pygame.image.load('Images/weed.jpg')
                            x_len = pix.get_width()
                            y_len = pix.get_height() 
                            sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                            xBot[yaBot] += 32
                            world[botLocation[yaBot]] = 0
                            world[botLocation[yaBot]+1] = botVariant[yaBot]
                            botLocation[yaBot] += 1
                            worldUpdate() 
                        
                        if world[botLocation[yaBot]+1] != 0:  # Если ни влево ни в право нельзя - идём вверх
                            botStep[yaBot] = 1                
            if botLocation[yaBot] <= 416 and botLocation[yaBot] >= 384: # если дошли до низа карты, то идём налево
                botStep[yaBot] = 1 
                        
            if botStep[yaBot] == 2: # Идём налево
                if world[botLocation[yaBot]-1] == 0 and botLocation[yaBot] >= 63 and xBot[yaBot] > 16:
                    botStep[yaBot] = 1
                    pix = pygame.image.load('Images/weed.jpg')
                    x_len = pix.get_width()
                    y_len = pix.get_height() 
                    sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                    xBot[yaBot] -= 32
                    world[botLocation[yaBot]] = 0
                    world[botLocation[yaBot]-1] = botVariant[yaBot]
                    botLocation[yaBot] -= 1
                    worldUpdate()
                if world[botLocation[yaBot]-1] != 0: 
                    if world[botLocation[yaBot]+1] == 0 and xBot[yaBot] < 1008:
                        botStep[yaBot] = 1
                        pix = pygame.image.load('Images/weed.jpg')
                        x_len = pix.get_width()
                        y_len = pix.get_height() 
                        sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                        xBot[yaBot] += 32
                        world[botLocation[yaBot]] = 0
                        world[botLocation[yaBot]+1] = botVariant[yaBot]
                        botLocation[yaBot] += 1
                        worldUpdate()
                        if world[botLocation[yaBot]+1] == 0 and xBot[yaBot] < 1008:
                            botStep[yaBot] = 1
                            pix = pygame.image.load('Images/weed.jpg')
                            x_len = pix.get_width()
                            y_len = pix.get_height() 
                            sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                            xBot[yaBot] += 32
                            world[botLocation[yaBot]] = 0
                            world[botLocation[yaBot]+1] = botVariant[yaBot]
                            botLocation[yaBot] += 1
                            worldUpdate()
                                                
                
            if botStep[yaBot] == 1: # Идём вверх
                if world[botLocation[yaBot]-32] == 0 and botLocation[yaBot] >= 63 and yBot[yaBot] > 96:
                    botStep[yaBot] = 2 
                    pix = pygame.image.load('Images/weed.jpg')
                    x_len = pix.get_width()
                    y_len = pix.get_height() 
                    sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                    yBot[yaBot] -= 32
                    world[botLocation[yaBot]] = 0
                    world[botLocation[yaBot]-32] = botVariant[yaBot]
                    botLocation[yaBot] -= 32
                    worldUpdate()  
                    
                if world[botLocation[yaBot]-32] != 0:
                    botStep[yaBot] = 2                
                
                if botLocation[yaBot] >= 63 and botLocation[yaBot] <= 32:
                    botStep[yaBot] = 0                 
        
        if botStep[yaBot] == 1 or botStep[yaBot] == 2 and botLocation[yaBot] <= 33 and botLocation[yaBot] >= 62: botStep[yaBot] = 0 
        # Если дошли до второй слева клетки любого ряда то останавливаемся botStep[yaBot] = 3
        # А лучше пойти потом вправо и дойдя по крайней правой кромки повторить алгоритм
        if botLocation[yaBot] == 417 or botLocation[yaBot] == 385 or botLocation[yaBot] == 353 or botLocation[yaBot] == 321 or botLocation[yaBot] == 289 or botLocation[yaBot] == 257 or botLocation[yaBot] == 225 or botLocation[yaBot] == 193 or botLocation[yaBot] == 161 or botLocation[yaBot] == 129 or botLocation[yaBot] == 97 or botLocation[yaBot] == 65 or botLocation[yaBot] == 33 or botLocation[yaBot] == 1: botStep[yaBot] = 3
                    
    
    if botAlgoritm[yaBot] == 4: #  ==================================================== Алгоритм зла ====================================
        if botStep[yaBot] == 0: # and world[botLocation[yaBot]-32] == 0
            if world[botLocation[yaBot]-32] == 0 and yBot[yaBot] > 96:   
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                yBot[yaBot] -= 32
                world[botLocation[yaBot]] = 0
                world[botLocation[yaBot]-32] = botVariant[yaBot]
                botLocation[yaBot] -= 32
                worldUpdate()
             
            if world[botLocation[yaBot]-32] != 0:
                if world[botLocation[yaBot]+1] == 0 and xBot[yaBot]<1008: # Если нельзя идти вниз то пробуем двинуться влево
                    pix = pygame.image.load('Images/weed.jpg')
                    x_len = pix.get_width()
                    y_len = pix.get_height() 
                    sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                    xBot[yaBot] += 32
                    world[botLocation[yaBot]] = 0
                    world[botLocation[yaBot]+1] = botVariant[yaBot]
                    botLocation[yaBot] += 1
                    worldUpdate()  
                    
                if world[botLocation[yaBot]+1] != 0: # Если нельзя влево пойти, то мы идём вправо
                    if world[botLocation[yaBot]-1] == 0 and xBot[yaBot] > 32:
                        pix = pygame.image.load('Images/weed.jpg')
                        x_len = pix.get_width()
                        y_len = pix.get_height() 
                        sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                        xBot[yaBot] -= 32
                        world[botLocation[yaBot]] = 0
                        world[botLocation[yaBot]-1] = botVariant[yaBot]
                        botLocation[yaBot] -= 1
                        worldUpdate() 
                        
                    if world[botLocation[yaBot]-1] != 0:  # Если ни влево ни в право нельзя - идём вверх
                        botStep[yaBot] = 1                
        if botLocation[yaBot] <= 63 and botLocation[yaBot] >= 32: # если дошли до низа карты, то идём налево
            botStep[yaBot] = 1 
                        
        if botStep[yaBot] == 2: # Идём направо
            if world[botLocation[yaBot]+1] == 0 and botLocation[yaBot] >= 32 and xBot[yaBot] < 1008:
                botStep[yaBot] = 1
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                xBot[yaBot] += 32
                world[botLocation[yaBot]] = 0
                world[botLocation[yaBot]+1] = botVariant[yaBot]
                botLocation[yaBot] += 1
                worldUpdate()
            if world[botLocation[yaBot]+1] != 0: 
                if world[botLocation[yaBot]-1] == 0 and xBot[yaBot] > 32:
                    botStep[yaBot] = 1
                    pix = pygame.image.load('Images/weed.jpg')
                    x_len = pix.get_width()
                    y_len = pix.get_height() 
                    sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                    xBot[yaBot] -= 32
                    world[botLocation[yaBot]] = 0
                    world[botLocation[yaBot]-1] = botVariant[yaBot]
                    botLocation[yaBot] -= 1
                    worldUpdate()
                    if world[botLocation[yaBot]-1] == 0 and xBot[yaBot] > 16:
                        botStep[yaBot] = 1
                        pix = pygame.image.load('Images/weed.jpg')
                        x_len = pix.get_width()
                        y_len = pix.get_height() 
                        sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                        xBot[yaBot] -= 32
                        world[botLocation[yaBot]] = 0
                        world[botLocation[yaBot]-1] = botVariant[yaBot]
                        botLocation[yaBot] -= 1
                        worldUpdate()
                                                
                
        if botStep[yaBot] == 1: # Идём вниз
            if world[botLocation[yaBot]+32] == 0 and botLocation[yaBot] >= 32 and yBot[yaBot] < 512:
                botStep[yaBot] = 2 
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[yaBot],yBot[yaBot]))
                yBot[yaBot] += 32
                world[botLocation[yaBot]] = 0
                world[botLocation[yaBot]+32] = botVariant[yaBot]
                botLocation[yaBot] += 32
                worldUpdate()  
                    
            if world[botLocation[yaBot]+32] != 0:
                botStep[yaBot] = 2                
                
            if botLocation[yaBot] >= 384 and botLocation[yaBot] <= 415:
                botStep[yaBot] = 0                 
        
        if botStep[yaBot] == 1 or botStep[yaBot] == 2 and botLocation[yaBot] <= 33 and botLocation[yaBot] >= 62: botStep[yaBot] = 0 
        # Если дошли до второй слева клетки любого ряда то останавливаемся botStep[yaBot] = 3
        # А лучше пойти потом вправо и дойдя по крайней правой кромки повторить алгоритм
        #if botLocation[yaBot] == 417 or botLocation[yaBot] == 385 or botLocation[yaBot] == 353 or botLocation[yaBot] == 321 or botLocation[yaBot] == 289 or botLocation[yaBot] == 257 or botLocation[yaBot] == 225 or botLocation[yaBot] == 193 or botLocation[yaBot] == 161 or botLocation[yaBot] == 129 or botLocation[yaBot] == 97 or botLocation[yaBot] == 65 or botLocation[yaBot] == 33 or botLocation[yaBot] == 1: botStep[yaBot] = 3
      
    
def botGoing(): # Эта функция вызывается каждый раз когда жмётся кнопка НОЧЬ
    global n
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
    global buttonNextStep
    global botDeistvie
    
    n = 0
        
    for n in range(1000):
        i = 0
        if botZdorovie[n] > 0 and botHod[n] > 0:             
            for i in range(botLovkost[n]): # Обрабатываем ходы
                if botLocation[n] >= 1 and botLocation[n] <= 30 and imHero != n: # Если бот находится на верхней кромке карты
                    if world[botLocation[n]-1] >= 50 or world[botLocation[n]+1] >= 50 or world[botLocation[n]+33] >= 50 or world[botLocation[n]+32] >= 50 or world[botLocation[n]+31] >= 50: # Если, находясь на верхней кромке мы кого-то видим
                        if world[botLocation[n]-1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-1], botLocation[n]-1); botHod[n] -= 1
                        if world[botLocation[n]+1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+1], botLocation[n]+1); botHod[n] -= 1
                        if world[botLocation[n]+33] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+33], botLocation[n]+33); botHod[n] -= 1
                        if world[botLocation[n]+32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+32], botLocation[n]+32); botHod[n] -= 1
                        if world[botLocation[n]+31] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+31], botLocation[n]+31); botHod[n] -= 1
                    else: 
                        botAlgoritmes(n); botHod[n] -= 1   # если никого не видим, то идём вперед                 
                         
                elif botLocation[n] <= 446 and botLocation[n] >= 417 and imHero != n: # Если бот находится на нижней кромке карты
                    if world[botLocation[n]-1] >= 50 or world[botLocation[n]+1] >= 50 or world[botLocation[n]-33] >= 50 or world[botLocation[n]-32] >= 50 or world[botLocation[n]-31] >= 50:  # Если, находясь на нижней кромке мы кого-то видим      
                        if world[botLocation[n]-1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-1], botLocation[n]-1); botHod[n] -= 1
                        if world[botLocation[n]+1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+1], botLocation[n]+1); botHod[n] -= 1
                        if world[botLocation[n]-33] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-33], botLocation[n]-33); botHod[n] -= 1
                        if world[botLocation[n]-32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-32], botLocation[n]-32); botHod[n] -= 1
                        if world[botLocation[n]-31] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-31], botLocation[n]-31); botHod[n] -= 1
                    else:
                        botAlgoritmes(n); botHod[n] -= 1 
   
                elif botLocation[n] == 63 or botLocation[n] == 95 or botLocation[n] == 127 or botLocation[n] == 159 or botLocation[n] == 191 or botLocation[n] == 223 or botLocation[n] == 255 or botLocation[n] == 287 or botLocation[n] == 319 or botLocation[n] == 351 or botLocation[n] == 383 or botLocation[n] == 415 and imHero != n: # Если мы находимся на правой кромке карты
                    if world[botLocation[n]-1] >= 50 or world[botLocation[n]-32] >= 50 or world[botLocation[n]-33] >= 50 or world[botLocation[n]+32] >= 50 or world[botLocation[n]+33] >= 50: # Если, находясь на правой кромке карты мы кого-то видим
                        if world[botLocation[n]-1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-1], botLocation[n]-1); botHod[n] -= 1
                        if world[botLocation[n]-33] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-33], botLocation[n]-33); botHod[n] -= 1
                        if world[botLocation[n]-32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-32], botLocation[n]-32); botHod[n] -= 1
                        if world[botLocation[n]+32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+32], botLocation[n]+32); botHod[n] -= 1
                        if world[botLocation[n]+33] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+33], botLocation[n]+33); botHod[n] -= 1
                    else:
                        botAlgoritmes(n); botHod[n] -= 1       
                elif botLocation[n] == 32 or botLocation[n] == 64 or botLocation[n] == 96 or botLocation[n] == 128 or botLocation[n] == 160 or botLocation[n] == 192 or botLocation[n] == 224 or botLocation[n] == 256 or botLocation[n] == 288 or botLocation[n] == 320 or botLocation[n] == 352 or botLocation[n] == 384 and imHero != n:  # Если бот находится на левой кромке карты
                    if world[botLocation[n]+1] >= 50 or world[botLocation[n]-32] >= 50 or world[botLocation[n]-31] >= 50 or world[botLocation[n]+32] >= 50 or world[botLocation[n]+31] >= 50: # Если, находясь на правой кромке карты мы кого-то видим        
                        if world[botLocation[n]+1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+1], botLocation[n]+1); botHod[n] -= 1
                        if world[botLocation[n]-31] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-31], botLocation[n]-31); botHod[n] -= 1
                        if world[botLocation[n]-32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-32], botLocation[n]-32); botHod[n] -= 1
                        if world[botLocation[n]+31] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+31], botLocation[n]+31); botHod[n] -= 1
                        if world[botLocation[n]+32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+32], botLocation[n]+32); botHod[n] -= 1
                    else:
                        botAlgoritmes(n); botHod[n] -= 1
                        
                else:
                    if imHero != n:
                        if world[botLocation[n]+1] >= 50 or world[botLocation[n]-32] >= 50 or world[botLocation[n]-31] >= 50 or world[botLocation[n]-33] >= 50 or world[botLocation[n]+31] >= 50 or world[botLocation[n]-1] >= 50 or world[botLocation[n]+33] >= 50 or world[botLocation[n]+32] >= 50: 
                            if world[botLocation[n]+1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+1], botLocation[n]+1); botHod[n] -= 1
                            if world[botLocation[n]-1] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-1], botLocation[n]-1); botHod[n] -= 1
                            if world[botLocation[n]-31] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-31], botLocation[n]-31); botHod[n] -= 1
                            if world[botLocation[n]-32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-32], botLocation[n]-32); botHod[n] -= 1
                            if world[botLocation[n]+31] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+31], botLocation[n]+31); botHod[n] -= 1
                            if world[botLocation[n]+32] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+32], botLocation[n]+32); botHod[n] -= 1
                            if world[botLocation[n]-33] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]-33], botLocation[n]-33); botHod[n] -= 1
                            if world[botLocation[n]+33] >= 50: botVragBlizko(n, xBot[n], yBot[n], botLocation[n], botVariant[n], world[botLocation[n]+33], botLocation[n]-33); botHod[n] -= 1
                        else:
                            botAlgoritmes(n); botHod[n] -= 1
                       
        else:
            if botYdacha[n] > 0 and botZdorovie[n] <= 0:
                pix = pygame.image.load('Images/weed.jpg'); x_len = pix.get_width(); y_len = pix.get_height();sc.blit(pix, (xBot[n],yBot[n]))
                botType[n] = 0
                botStep[n] = 0
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
                world[botLocation[n]] = 0
                botNumer[n] = 0
                botVariant[n] = 0
                botAlgoritm[n] = 0
                botLocation[n] = 0
    
    
    buttonNextStep = 0 # Разрешаем нажатие кнопки "Следующий ход/ночь"            
    heroPanel(hero)          
 
def botActivity():  # Создание и управление ботами
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
    global n
    botRandom = 0
    botRandom = int(random.random()*100) # Переменная для случайного распределения артефактов
    botLoad = 0    
    temp = int(random.random()*3) # Вероятность появления нового бота 1/4
    print(bot)
    if temp == 2:   
        tmp = int(random.random()*72)
        tmp += 100
        xBot.append(bot)
        yBot.append(bot)
    
        if tmp == 157 or tmp == 114 or tmp == 115 or tmp == 116 or tmp == 117 or tmp == 118 or tmp == 126 or tmp == 127 or tmp == 128 or tmp == 129 or tmp == 144 or tmp == 145 or tmp == 146 or tmp == 165:  # Если персонажи человеческой расы
            if world[30] == 0 or world[63] == 0 or world[62] == 0:
                botLoad = 1
                botRasa[bot] = 1
                if tmp == 157: # Странник 3 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг
                    botNumer[bot] = bot
                    botVariant[bot] = tmp        
                    botLvl[bot] = 3
                    botZdorovie[bot] = 185
                    botIshZdorovie[bot] = 185
                    botMana[bot] = 50
                    botIshMana[bot] = 50
                    botZaklinania[bot]=[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 22
                    botLovkost[bot] = 6
                    botYdacha[bot] = 19
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[bot] = [3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[bot] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62    
                    
                if tmp == 114: # Отшельник 1 ур.
                    if rasa == 7 or rasa == 1:
                        botType[bot] = 1
                    else:
                        botType[bot] = 2   
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 85
                    botIshZdorovie[bot] = 85
                    botMana[bot] = 100
                    botIshMana[bot] = 100
                    botZaklinania[bot]=[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 7
                    botLovkost[bot] = 5
                    botYdacha[bot] = 3
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[bot] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[bot] = [60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
                    
                if tmp == 115: # Отшельник 2 ур.
                    if rasa == 7 or rasa == 1:
                        botType[bot] = 1
                    else:
                        botType[bot] = 2   
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 105
                    botIshZdorovie[bot] = 105
                    botMana[bot] = 130
                    botIshMana[bot] = 130
                    botZaklinania[bot]=[2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 14
                    botLovkost[bot] = 6
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[bot] = [13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
                    
                if tmp == 116: # Отшельник 3 ур.
                    if rasa == 7 or rasa == 1:
                        botType[bot] = 1
                    else:
                        botType[bot] = 2    
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 125
                    botIshZdorovie[bot] = 125
                    botMana[bot] = 200
                    botIshMana[bot] = 200
                    botZaklinania[bot]=[2,3,12,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 7
                    botYdacha[bot] = 9
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 40:
                        botInventar[bot] = [3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[bot] = [21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   
                    
                if tmp == 117: # Охотник за головами.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 155
                    botIshZdorovie[bot] = 155
                    botMana[bot] = 60
                    botIshMana[bot] = 60
                    botZaklinania[bot]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 25
                    botLovkost[bot] = 7
                    botYdacha[bot] = 15
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 60:
                        botInventar[bot] = [27,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 28:
                        botInventar[bot] = [27,16,3,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [27,4,48,53,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [28,4,7,48,18,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   
                    
                if tmp == 118: # Человек
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 3 # Мирный    
                    botLvl[bot] = 1
                    botZdorovie[bot] = 30
                    botIshZdorovie[bot] = 30
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botSila[bot] = 0
                    botLovkost[bot] = 4
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 60:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[bot] = [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 12:
                        botInventar[bot] = [22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
                        
                if tmp == 126: # Наёмник 1 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг    
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 100
                    botIshZdorovie[bot] = 100
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 10
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [60,46,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [60,46,1,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [60,46,3,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [60,46,3,13,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62    
                    
                if tmp == 127: # Наёмник 2 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 140
                    botIshZdorovie[bot] = 140
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 17
                    botLovkost[bot] = 6
                    botYdacha[bot] = 8
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [60,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [60,47,1,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [60,47,2,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [60,47,3,13,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62    
                    
                if tmp == 128: # Наёмник 3 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 170
                    botIshZdorovie[bot] = 170
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 27
                    botLovkost[bot] = 7
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [61,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [61,47,2,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [61,48,3,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [61,48,3,3,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [61,48,3,13,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62     
                    
                if tmp == 129: # Наёмник 4 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 200
                    botIshZdorovie[bot] = 200
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 40
                    botLovkost[bot] = 7
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [62,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [62,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [62,48,3,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [62,48,4,3,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [62,48,53,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
                    
                if tmp == 144: # Оккультист
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2     
                    botLvl[bot] = 5
                    botZdorovie[bot] = 250
                    botIshZdorovie[bot] = 250
                    botMana[bot] = 200
                    botIshMana[bot] = 200
                    botZaklinania[bot]=[1,2,4,11,13,23,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 7
                    botYdacha[bot] = 20
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 60:
                        botInventar[bot] = [8,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [11,7,55,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [11,19,54,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   
                    
                if tmp == 145: # Разбойник
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2    
                    botLvl[bot] = 2
                    botZdorovie[bot] = 145
                    botIshZdorovie[bot] = 145
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 16
                    botLovkost[bot] = 7
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [61,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [61,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [61,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [61,3,3,59,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   
                  
                if tmp == 146: # Грабитель
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2    
                    botLvl[bot] = 2
                    botZdorovie[bot] = 150
                    botIshZdorovie[bot] = 150
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 18
                    botLovkost[bot] = 6
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [61,46,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [60,47,2,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [60,47,3,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [60,47,4,59,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62     
                    
                if tmp == 165: # Колдун
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 175
                    botIshZdorovie[bot] = 175
                    botMana[bot] = 200
                    botIshMana[bot] = 200
                    botZaklinania[bot]=[22,23,12,11,3,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 6
                    botYdacha[bot] = 25
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [8,44,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [9,44,3,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [10,11,45,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [10,11,45,15,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62                                                                                     
        
        elif tmp == 100 or tmp == 101 or tmp == 102 or tmp == 166 or tmp == 167 or tmp == 168 or tmp == 169 or tmp == 170 or tmp == 171 or tmp == 172:
            if world[30] == 0 or world[63] == 0 or world[62] == 0:
                botLoad = 1
                # Эльфы
                botRasa[bot] = 2
                if tmp == 100: # Эльф 1 ур.
                    botType.append(bot)
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 105
                    botIshZdorovie[bot] = 105
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 10
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62    
                    
                if tmp == 101: # Эльф 2 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 135
                    botIshZdorovie[bot] = 135
                    botMana[bot] = 60
                    botIshMana[bot] = 60
                    botZaklinania[bot]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 15
                    botLovkost[bot] = 6
                    botYdacha[bot] = 9
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
    
                if tmp == 102: # Эльф 3 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг   
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 165
                    botIshZdorovie[bot] = 165
                    botMana[bot] = 120
                    botIshMana[bot] = 120
                    botZaklinania[bot]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 25
                    botLovkost[bot] = 7
                    botYdacha[bot] = 13
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 26:
                        botInventar[bot] = [11,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [60,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  

                if tmp == 166: # Женщина-эльф 1 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 85
                    botIshZdorovie[bot] = 85
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 7
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
                    
                if tmp == 167: # Женщина-эльф 2 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 110
                    botIshZdorovie[bot] = 110
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 13
                    botLovkost[bot] = 6
                    botYdacha[bot] = 7
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [13,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62    

                if tmp == 168: # Женщина-эльф 3 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 140
                    botIshZdorovie[bot] = 140
                    botMana[bot] = 50
                    botIshMana[bot] = 50
                    botZaklinania[bot]=[9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 19
                    botLovkost[bot] = 6
                    botYdacha[bot] = 7
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [2,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [3,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [12,7,25,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  
                if tmp == 169: # Женщина-эльф 4 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 190
                    botIshZdorovie[bot] = 190
                    botMana[bot] = 140
                    botIshMana[bot] = 140
                    botZaklinania[bot]=[9,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 6
                    botYdacha[bot] = 7
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [4,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  

                if tmp == 170: # Женщина-эльф 5 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 5
                    botZdorovie[bot] = 260
                    botIshZdorovie[bot] = 260
                    botMana[bot] = 195
                    botIshMana[bot] = 195
                    botZaklinania[bot]=[9,12,23,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 27
                    botLovkost[bot] = 6
                    botYdacha[bot] = 14
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [54,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62                       
                    
                if tmp == 171: # Женщина-эльф 6 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 6
                    botZdorovie[bot] = 370
                    botIshZdorovie[bot] = 370
                    botMana[bot] = 250
                    botIshMana[bot] = 250
                    botZaklinania[bot]=[9,12,23,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 27
                    botLovkost[bot] = 6
                    botYdacha[bot] = 14
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  

                if tmp == 172: # Женщина-эльф 7 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг    
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 7
                    botZdorovie[bot] = 520
                    botIshZdorovie[bot] = 520
                    botMana[bot] = 400
                    botIshMana[bot] = 400
                    botZaklinania[bot]=[9,12,23,1,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 29
                    botLovkost[bot] = 6
                    botYdacha[bot] = 14
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [5,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [5,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [5,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62                       
                    
        elif tmp == 106 or tmp == 107 or tmp == 108 or tmp == 109:
            if world[30] == 0 or world[63] == 0 or world[62] == 0:
                botLoad = 1         
                botRasa[bot] = 3
                if tmp == 106: # Гном 1 ур.
                    botType.append(bot)
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг    
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 120
                    botIshZdorovie[bot] = 120
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 15
                    botLovkost[bot] = 6
                    botYdacha[bot] = 20
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [67,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [68,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [17,3,22,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  

                if tmp == 107: # Гном 2 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг   
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 180
                    botIshZdorovie[bot] = 180
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 21
                    botLovkost[bot] = 6
                    botYdacha[bot] = 25
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [68,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [68,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [68,17,14,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  

                if tmp == 108: # Гном 3 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг   
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 260
                    botIshZdorovie[bot] = 260
                    botMana[bot] = 90
                    botIshMana[bot] = 90
                    botZaklinania[bot]=[22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 29
                    botLovkost[bot] = 6
                    botYdacha[bot] = 33
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [69,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [69,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [69,4,6,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [69,4,11,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62  

                if tmp == 109: # Гном 4 ур.
                    if rasa == 2 or rasa == 1:
                        botType[bot] = 1 # Если ты человек или эльф, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 350
                    botIshZdorovie[bot] = 350
                    botMana[bot] = 130
                    botIshMana[bot] = 130
                    botZaklinania[bot]=[22,23,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 35
                    botLovkost[bot] = 6
                    botYdacha[bot] = 33
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [68,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [69,4,7,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [69,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [70,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62                     
                
        elif tmp == 110 or tmp == 111 or tmp == 112 or tmp == 113:
            if world[30] == 0 or world[63] == 0 or world[62] == 0:        
                botLoad = 1
                botRasa[bot] = 4
                if tmp == 110: # Гоблин 0 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 3 # Мирный
                    botLvl[bot] = 0
                    botZdorovie[bot] = 50
                    botIshZdorovie[bot] = 50
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botSila[bot] = 0
                    botLovkost[bot] = 6
                    botYdacha[bot] = 20
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [3,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   
                    
                if tmp == 111: # Гоблин 1 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 1    
                    botLvl[bot] = 1
                    botZdorovie[bot] = 100
                    botIshZdorovie[bot] = 100
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 15
                    botLovkost[bot] = 6
                    botYdacha[bot] = 20
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [3,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   

                if tmp == 112: # Гоблин 2 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 1  
                    botLvl[bot] = 2
                    botZdorovie[bot] = 135
                    botIshZdorovie[bot] = 135
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 19
                    botLovkost[bot] = 6
                    botYdacha[bot] = 27
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62   

                if tmp == 113: # Гоблин 3 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 1   
                    botLvl[bot] = 3
                    botZdorovie[bot] = 175
                    botIshZdorovie[bot] = 175
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 26
                    botLovkost[bot] = 6
                    botYdacha[bot] = 33
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 3
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[30] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 96
                        world[30] = tmp
                        botLocation[bot] = 30
                    elif world[63] == 0:
                        xBot[bot] = 976
                        yBot[bot] = 128
                        world[63] = tmp
                        botLocation[bot] = 63 
                    elif world[62] == 0:
                        xBot[bot] = 1008
                        yBot[bot] = 128
                        world[62] = tmp  
                        botLocation[bot] = 62                  
                
        elif tmp == 103 or tmp == 104 or tmp == 105 or tmp == 119 or tmp == 120 or tmp == 121 or tmp == 122 or tmp == 123 or tmp == 124 or tmp == 125 or tmp == 131 or tmp == 132 or tmp == 133 or tmp == 134 or tmp == 147:
            if world[384] == 0 or world[385] == 0 or world[417] == 0:
                botLoad = 1 
                botRasa[bot] = 5
                if tmp == 103: # Гнолл 1 ур
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2  
                    botLvl[bot] = 1
                    botZdorovie[bot] = 90
                    botIshZdorovie[bot] = 90
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 15
                    botLovkost[bot] = 6
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  
                    
                if tmp == 104: # Гнолл 2 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2  
                    botLvl[bot] = 2
                    botZdorovie[bot] = 135
                    botIshZdorovie[bot] = 135
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 21
                    botLovkost[bot] = 6
                    botYdacha[bot] = 7
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 105: # Гнолл 3 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2   
                    botLvl[bot] = 4
                    botZdorovie[bot] = 185
                    botIshZdorovie[bot] = 185
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 29
                    botLovkost[bot] = 6
                    botYdacha[bot] = 9
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 119: # Монстр 1 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2    
                    botLvl[bot] = 1
                    botZdorovie[bot] = 135
                    botIshZdorovie[bot] = 135
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 19
                    botLovkost[bot] = 6
                    botYdacha[bot] = 7
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 120: # Монстр 2 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2     
                    botLvl[bot] = 2
                    botZdorovie[bot] = 195
                    botIshZdorovie[bot] = 195
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 27
                    botLovkost[bot] = 6
                    botYdacha[bot] = 7
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 121: # Монстр 3 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 3
                    botLvl[bot] = 4
                    botZdorovie[bot] = 300
                    botIshZdorovie[bot] = 300
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 37
                    botLovkost[bot] = 6
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [64,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 122: # Монстр 4 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 4
                    botLvl[bot] = 6
                    botZdorovie[bot] = 560
                    botIshZdorovie[bot] = 560
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 50
                    botLovkost[bot] = 6
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [64,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [11,0,30,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [31,11,15,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 123: # Морлок 1 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2    
                    botLvl[bot] = 1
                    botZdorovie[bot] = 70
                    botIshZdorovie[bot] = 70
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 8
                    botLovkost[bot] = 5
                    botYdacha[bot] = 1
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   
    
                if tmp == 124: # Морлок 2 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2   
                    botLvl[bot] = 2
                    botZdorovie[bot] = 90
                    botIshZdorovie[bot] = 90
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 12
                    botLovkost[bot] = 6
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    
    
                if tmp == 125: # Морлок 3 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2   
                    botLvl[bot] = 3
                    botZdorovie[bot] = 130
                    botIshZdorovie[bot] = 130
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 16
                    botLovkost[bot] = 7
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  
    
                if tmp == 131: # Непобедимый 1 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 200
                    botIshZdorovie[bot] = 200
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 6
                    botYdacha[bot] = 15
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [62,46,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [62,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [63,11,59,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 132: # Непобедимый 2 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 280
                    botIshZdorovie[bot] = 280
                    botMana[bot] = 200
                    botIshMana[bot] = 200
                    botZaklinania[bot]=[13,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 30
                    botLovkost[bot] = 6
                    botYdacha[bot] = 20
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [63,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [63,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [64,49,11,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 133: # Огр 1 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2   
                    botLvl[bot] = 1
                    botZdorovie[bot] = 130
                    botIshZdorovie[bot] = 130
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 18
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 134: # Огр 2 ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2  
                    botLvl[bot] = 2
                    botZdorovie[bot] = 150
                    botIshZdorovie[bot] = 150
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 5
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 147: # Красный огненный голем ур.
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botType[bot] = 2 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 300
                    botIshZdorovie[bot] = 300
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 40
                    botLovkost[bot] = 5
                    botYdacha[bot] = 15
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417                    
      
        elif tmp == 136 or tmp == 137 or tmp == 138 or tmp == 139 or tmp == 140 or tmp == 141 or tmp == 142 or tmp == 143 or tmp == 158 or tmp == 159 or tmp == 160 or tmp == 161 or tmp == 162 or tmp == 163:
            if world[384] == 0 or world[385] == 0 or world[417] == 0: 
                botLoad = 1
                botRasa[bot] = 6
                if tmp == 136: # Орк 1 ур.
                    botType.append(bot)
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 120
                    botIshZdorovie[bot] = 120
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 15
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [26,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [26,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [26,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    
                    
                if tmp == 137: # Орк 2 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 160
                    botIshZdorovie[bot] = 160
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 19
                    botLovkost[bot] = 5
                    botYdacha[bot] = 6
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [27,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417       

                if tmp == 138: # Орк 3 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 220
                    botIshZdorovie[bot] = 220
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 27
                    botLovkost[bot] = 5
                    botYdacha[bot] = 6
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [28,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [28,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417     

                if tmp == 139: # Орк 4 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 310
                    botIshZdorovie[bot] = 310
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 37
                    botLovkost[bot] = 6
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [28,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [29,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    
        
                if tmp == 140: # Орк 5 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 5
                    botZdorovie[bot] = 390
                    botIshZdorovie[bot] = 390
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 49
                    botLovkost[bot] = 6
                    botYdacha[bot] = 12
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [28,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [28,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [29,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [30,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417     
    
                if tmp == 141: # Орк 6 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 6
                    botZdorovie[bot] = 520
                    botIshZdorovie[bot] = 520
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 60
                    botLovkost[bot] = 6
                    botYdacha[bot] = 15
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [28,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [29,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [30,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [30,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    

                if tmp == 142: # Орк 7 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 7
                    botZdorovie[bot] = 700
                    botIshZdorovie[bot] = 700
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 75
                    botLovkost[bot] = 6
                    botYdacha[bot] = 20
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [30,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [31,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [32,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 143: # Орк-шаман  3 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 240
                    botIshZdorovie[bot] = 240
                    botMana[bot] = 185
                    botIshMana[bot] = 185
                    botZaklinania[bot]=[8,22,19,11,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 23
                    botLovkost[bot] = 6
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [7,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [8,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [28,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417     

                if tmp == 158: # Тролль 1 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 100
                    botIshZdorovie[bot] = 100
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 12
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 159: # Тролль 2 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг   
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 135
                    botIshZdorovie[bot] = 135
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 16
                    botLovkost[bot] = 5
                    botYdacha[bot] = 6
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   
                    
                if tmp == 160: # Тролль 3 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 195
                    botIshZdorovie[bot] = 195
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 22
                    botLovkost[bot] = 5
                    botYdacha[bot] = 9
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417     

                if tmp == 161: # Тролль 4 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 250
                    botIshZdorovie[bot] = 250
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 28
                    botLovkost[bot] = 5
                    botYdacha[bot] = 12
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    

                if tmp == 162: # Тролль 5 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 5
                    botZdorovie[bot] = 320
                    botIshZdorovie[bot] = 320
                    botMana[bot] = 110
                    botIshMana[bot] = 110
                    botZaklinania[bot]=[4,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 35
                    botLovkost[bot] = 5
                    botYdacha[bot] = 16
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [29,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [30,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 163: # Тролль 6 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 6
                    botZdorovie[bot] = 400
                    botIshZdorovie[bot] = 400
                    botMana[bot] = 170
                    botIshMana[bot] = 170
                    botZaklinania[bot]=[4,12,3,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 47
                    botLovkost[bot] = 5
                    botYdacha[bot] = 21
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [28,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [29,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [30,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [31,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417                       
         
        elif tmp == 148 or tmp == 149 or tmp == 150 or tmp == 151 or tmp == 152 or tmp == 153 or tmp == 154 or tmp == 155 or tmp == 156 or tmp == 164 or tmp == 135 or tmp == 130: 
            if world[384] == 0 or world[385] == 0 or world[417] == 0:
                botLoad = 1 
                botRasa[bot] = 7 
                if tmp == 148: # Скелет 1 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 1
                    botZdorovie[bot] = 50
                    botIshZdorovie[bot] = 50
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 5
                    botLovkost[bot] = 3
                    botYdacha[bot] = 1
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    
                    
                if tmp == 149: # Скелет 2 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 2
                    botZdorovie[bot] = 90
                    botIshZdorovie[bot] = 90
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 9
                    botLovkost[bot] = 4
                    botYdacha[bot] = 2
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 150: # Скелет 3 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 145
                    botIshZdorovie[bot] = 145
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 13
                    botLovkost[bot] = 4
                    botYdacha[bot] = 3
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417      

                if tmp == 151: # Скелет 4 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 4
                    botZdorovie[bot] = 190
                    botIshZdorovie[bot] = 190
                    botMana[bot] = 60
                    botIshMana[bot] = 60
                    botZaklinania[bot]=[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 18
                    botLovkost[bot] = 4
                    botYdacha[bot] = 3
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [6,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [7,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 152: # Скелет 5 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 5
                    botZdorovie[bot] = 245
                    botIshZdorovie[bot] = 245
                    botMana[bot] = 120
                    botIshMana[bot] = 120
                    botZaklinania[bot]=[2,11,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 26
                    botLovkost[bot] = 5
                    botYdacha[bot] = 5
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [7,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417    

                if tmp == 153: # Скелет 6 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 6
                    botZdorovie[bot] = 315
                    botIshZdorovie[bot] = 315
                    botMana[bot] = 170
                    botIshMana[bot] = 170
                    botZaklinania[bot]=[2,11,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 36
                    botLovkost[bot] = 5
                    botYdacha[bot] = 8
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417  

                if tmp == 154: # Скелет 7 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 7
                    botZdorovie[bot] = 395
                    botIshZdorovie[bot] = 395
                    botMana[bot] = 240
                    botIshMana[bot] = 240
                    botZaklinania[bot]=[2,11,12,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 36
                    botLovkost[bot] = 5
                    botYdacha[bot] = 8
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [12,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [11,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   
    
                if tmp == 155: # Скелет 8 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 8
                    botZdorovie[bot] = 500
                    botIshZdorovie[bot] = 500
                    botMana[bot] = 290
                    botIshMana[bot] = 290
                    botZaklinania[bot]=[2,11,12,15,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 50
                    botLovkost[bot] = 5
                    botYdacha[bot] = 12
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [12,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [11,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [11,12,8,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 156: # Душекрад 10 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 10
                    botZdorovie[bot] = 1250
                    botIshZdorovie[bot] = 1250
                    botMana[bot] = 500
                    botIshMana[bot] = 500
                    botZaklinania[bot]=[1,5,11,15,21,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 150
                    botLovkost[bot] = 6
                    botYdacha[bot] = 10
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [9,9,18,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [11,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 25:
                        botInventar[bot] = [65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 12:
                        botInventar[bot] = [32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 164: # Вампир 3 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг 
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 3
                    botZdorovie[bot] = 185
                    botIshZdorovie[bot] = 185
                    botMana[bot] = 0
                    botIshMana[bot] = 0
                    botZaklinania[bot]=[20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 6
                    botYdacha[bot] = 18
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [4,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [4,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [53,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 135: # Оккультист 5 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 5
                    botZdorovie[bot] = 285
                    botIshZdorovie[bot] = 285
                    botMana[bot] = 300
                    botIshMana[bot] = 300
                    botZaklinania[bot]=[23,1,6,11,0,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 6
                    botYdacha[bot] = 9
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [0,7,11,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [59,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417   

                if tmp == 130: # Некромант 6 ур.
                    if rasa == 6 or rasa == 7:
                        botType[bot] = 1 # Если ты Нежить или Орк, то он тебе друг
                    else:
                        botType[bot] = 2 # Иначе враг  
                    botNumer[bot] = bot
                    botVariant[bot] = tmp 
                    botLvl[bot] = 6
                    botZdorovie[bot] = 340
                    botIshZdorovie[bot] = 340
                    botMana[bot] = 400
                    botIshMana[bot] = 400
                    botZaklinania[bot]=[23,1,6,11,21,0,0,0,0,0,0,0,0,0,0,100]
                    botSila[bot] = 20
                    botLovkost[bot] = 6
                    botYdacha[bot] = 9
                    botHod[bot] = botLovkost[bot]
                    botVozdeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botAlgoritm[bot] = 4
                    botDeistvie[bot]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    botInventar[bot] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 30 and botRandom <= 70:
                        botInventar[bot] = [59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if botRandom >= 20 and botRandom <= 29:
                        botInventar[bot] = [58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                    if botRandom >= 10 and botRandom <= 13:
                        botInventar[bot] = [55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if botRandom == 5:
                        botInventar[bot] = [66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
                    if world[384] == 0:
                        xBot[bot] = 16
                        yBot[bot] = 480
                        world[384] = tmp
                        botLocation[bot] = 384 
                    elif world[385] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 480
                        world[385] = tmp
                        botLocation[bot] = 385 
                    elif world[417] == 0:
                        xBot[bot] = 48
                        yBot[bot] = 512
                        world[417] = tmp
                        botLocation[bot] = 417                      
            
        else:
            print("WARNING " + str(tmp))
        if botLoad == 1:
            botLoad = 0
            bot += 1
        worldUpdate()
        # Конец создания бота
    worldUpdate() 
    botGoing()
    # ===================================================================================================================    

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
    if iconka == 172: pix = pygame.image.load('Images/womanElf7.jpg'); x_len = pix.get_width(); y_len = pix.get_height(); sc.blit(pix, (xMap,yMap))    
        
        
        
def worldUpdate():   # Отправляем данные об объекте
    n = 0
    for n in range(448):
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

def doebaca(hehmda):  #Функция отображающая информацию об объектах и позволяющая с ними взаимодействовать
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
    global attack
    global zakl
    global botDeistvie
    global posohSmerti
    global posohProzrenia
    global posohSveta
    global posohVoli
    global posohVechnoiJizni
    
    n = 0
    pygame.draw.rect(sc, (255, 255, 255), (405, 558, 365, 896)) 
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
        for n in range(1000):
            if botLocation[n] == hehmda: 
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n])
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n])
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        pix = pygame.image.load('Images/redFireHolem.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        for n in range(1000):
            if botLocation[n] == hehmda:
                print(botZdorovie[n]) 
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
        pix = pygame.image.load('Images/akami.jpg')
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
        
        
    ktoZdesVrag = 0
    for ktoZdesVrag in range(1000): # Определяем номер бота по клетке
        if botLocation[ktoZdesVrag] == hehmda:
            break        
        
    if zakl > 0 and ktoZdesVrag != 999:
        if zakl == 1: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 2: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 3: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 4: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 5: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 6: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 7: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 8: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 9: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 10: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 11: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 12: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 13: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 14: botKoldun(0,zakl-1,ktoZdesVrag)
        if zakl == 15: botKoldun(0,zakl-1,ktoZdesVrag)
                        
        zakl = 0
        attack = 0
    
    ktoZdesVrag = 0    
    if posohSmerti == 1:
        for ktoZdesVrag in range(1000): # Определяем номер бота по клетке
            if botLocation[ktoZdesVrag] == hehmda:
                break  
        
        botMana[imHero] -= 100
        botZdorovie[ktoZdesVrag] -= 200
        botHod[imHero] -= 1
        botExpirience[imHero] += 50
        posohSmerti = 0
        if botZdorovie[ktoZdesVrag] <= 0: ubiraemTrup(ktoZdesVrag)
        heroPanel(hero)
        
    if attack == 1 and botHod[0] > 0:  # Тут мы атакуем ботов
        n = 1
        for n in range(1000):
            if botLocation[0] == botLocation[n]-1 or botLocation[0] == botLocation[n]+1 or botLocation[0] == botLocation[n]-32 or botLocation[0] == botLocation[n]+32 or botLocation[0] == botLocation[n]-31 or botLocation[0] == botLocation[n]+31 or botLocation[0] == botLocation[n]-33 or botLocation[0] == botLocation[n]+33:
                print("Бот ",botLocation[n], " рядом со мной",botLocation[0], " и я его бью. Его здоровье: ", botZdorovie[n], " уровень: ",botLvl[n]," Тип: ",botVariant[n])
                botHod[0] -= 1
                botZdorovie[n] -= botSila[0] - botZachita[n]
                botExpirience[0] += botSila[0] # Повышаем опыт
                attack = 0
                if botZdorovie[n] <= 0:
                    botExpirience[0] += int(botIshZdorovie[n] / 2)
                    ubiraemTrup(n)
          
        heroPanel(hero)
        worldUpdate()        
        attack = 0
                     
        
def visibleMagic(xMag, yMag, por): # Функция, отображающая заклинания
    global botZaklinania
    if botZaklinania[0][por] == 0:
        pix = pygame.image.load('Images/zero.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[0][por] == 100:
        pix = pygame.image.load('Images/attack.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[0][por] == 1:
        pix = pygame.image.load('Images/pronzauchaiaSmert.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[0][por] == 2:
        pix = pygame.image.load('Images/dobitIvoskresit.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[0][por] == 3:
        pix = pygame.image.load('Images/dospechiFenicha.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 4:
        pix = pygame.image.load('Images/krajaMagii.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 5:
        pix = pygame.image.load('Images/obman.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if botZaklinania[0][por] == 6:
        pix = pygame.image.load('Images/ognennaiaSfera.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 7:
        pix = pygame.image.load('Images/jad.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))
    if botZaklinania[0][por] == 8:
        pix = pygame.image.load('Images/krovojadnost.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))        
    if botZaklinania[0][por] == 9:
        pix = pygame.image.load('Images/lunniiObriad.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 10:
        pix = pygame.image.load('Images/mochLda.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 11:
        pix = pygame.image.load('Images/mogilniiLuch.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[0][por] == 12:
        pix = pygame.image.load('Images/molnia.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if botZaklinania[0][por] == 13:
        pix = pygame.image.load('Images/pechatChaosa.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))    
    if botZaklinania[0][por] == 14:
        pix = pygame.image.load('Images/pechatSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if botZaklinania[0][por] == 15:
        pix = pygame.image.load('Images/poceluiSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))      
    if botZaklinania[0][por] == 16:
        pix = pygame.image.load('Images/prokliatie.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if botZaklinania[0][por] == 17:
        pix = pygame.image.load('Images/pronzauchiiKrik.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))         
    if botZaklinania[0][por] == 18:
        pix = pygame.image.load('Images/reincarnation.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[0][por] == 19:
        pix = pygame.image.load('Images/sjiganieMani.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[0][por] == 20:
        pix = pygame.image.load('Images/vampirizm.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag)) 
    if botZaklinania[0][por] == 21:
        pix = pygame.image.load('Images/vosstanovitSkeletov.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 22:
        pix = pygame.image.load('Images/lechenie.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))   
    if botZaklinania[0][por] == 23:
        pix = pygame.image.load('Images/rasseiatChari.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))  
    if botZaklinania[0][por] == 24:
        pix = pygame.image.load('Images/plenitDuchu.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xMag,yMag))              
                                
def visibleInventar(xInv, yInv, porNom): # Функция, отображающая заклинания
    global botInventar
    if botInventar[0][porNom] == 0:
        pix = pygame.image.load('Images/zero.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 1:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 2:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 3:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 4:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 5:
        pix = pygame.image.load('Images/healtPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))                       
    if botInventar[0][porNom] == 6:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 7:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 8:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 9:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 10:
        pix = pygame.image.load('Images/manaPoison.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))                
    if botInventar[0][porNom] == 11:
        pix = pygame.image.load('Images/zelieVostanovlenia.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 12:
        pix = pygame.image.load('Images/zelieRasseivania.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))   
    if botInventar[0][porNom] == 13:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 14:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 15:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 16:
        pix = pygame.image.load('Images/zelieKipacheiKrovi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))           
    if botInventar[0][porNom] == 17:
        pix = pygame.image.load('Images/zelieZaciti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 18:
        pix = pygame.image.load('Images/zelieZaciti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 19:
        pix = pygame.image.load('Images/zelieZaciti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))            
    if botInventar[0][porNom] == 20:
        pix = pygame.image.load('Images/zelieLovkosti.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 21:
        pix = pygame.image.load('Images/zelieLovkosti.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 22:
        pix = pygame.image.load('Images/zelieLovkosti.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))          
    if botInventar[0][porNom] == 23:
        pix = pygame.image.load('Images/zelieUdachi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 24:
        pix = pygame.image.load('Images/zelieUdachi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 25:
        pix = pygame.image.load('Images/zelieUdachi.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))        
    if botInventar[0][porNom] == 26:
        pix = pygame.image.load('Images/axe.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))   
    if botInventar[0][porNom] == 27:
        pix = pygame.image.load('Images/axe1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 28:
        pix = pygame.image.load('Images/axe2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[0][porNom] == 29:
        pix = pygame.image.load('Images/axe3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 30:
        pix = pygame.image.load('Images/axe4.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 31:
        pix = pygame.image.load('Images/axe5.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 32:
        pix = pygame.image.load('Images/axe6.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 33:
        pix = pygame.image.load('Images/book.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 34:
        pix = pygame.image.load('Images/book1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 35:
        pix = pygame.image.load('Images/book2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 36:
        pix = pygame.image.load('Images/book3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 37:
        pix = pygame.image.load('Images/book4.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 38:
        pix = pygame.image.load('Images/book5.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 39:
        pix = pygame.image.load('Images/book6.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 40:
        pix = pygame.image.load('Images/book7.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 41:
        pix = pygame.image.load('Images/book8.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 42:
        pix = pygame.image.load('Images/book9.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))  
    if botInventar[0][porNom] == 43:
        pix = pygame.image.load('Images/bot1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 44:
        pix = pygame.image.load('Images/bot2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 45:
        pix = pygame.image.load('Images/bot3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 46:
        pix = pygame.image.load('Images/helmet.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 47:
        pix = pygame.image.load('Images/helmet1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 48:
        pix = pygame.image.load('Images/helmet2.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 49:
        pix = pygame.image.load('Images/helmet3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 50:
        pix = pygame.image.load('Images/helmet4.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 51:
        pix = pygame.image.load('Images/helmet5.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 52:
        pix = pygame.image.load('Images/jar.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 53:
        pix = pygame.image.load('Images/ojerelie.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 54:
        pix = pygame.image.load('Images/posohProzrenia.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 55:
        pix = pygame.image.load('Images/posohSmerti.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))        
    if botInventar[0][porNom] == 56:
        pix = pygame.image.load('Images/posohSveta.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))        
    if botInventar[0][porNom] == 57:
        pix = pygame.image.load('Images/posohVechnoiJizni.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 58:
        pix = pygame.image.load('Images/posohVoli.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))      
    if botInventar[0][porNom] == 59:
        pix = pygame.image.load('Images/runesBraslet.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv)) 
    if botInventar[0][porNom] == 60:
        pix = pygame.image.load('Images/sword.jpeg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 61:
        pix = pygame.image.load('Images/sword1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))     
    if botInventar[0][porNom] == 62:
        pix = pygame.image.load('Images/sword2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[0][porNom] == 63:
        pix = pygame.image.load('Images/sword3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[0][porNom] == 64:
        pix = pygame.image.load('Images/sword4.gif') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[0][porNom] == 65:
        pix = pygame.image.load('Images/sword5.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[0][porNom] == 66:
        pix = pygame.image.load('Images/usilenniiPosohVechnoiJizni.png') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))   
    if botInventar[0][porNom] == 67:
        pix = pygame.image.load('Images/hammer.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))         
    if botInventar[0][porNom] == 68:
        pix = pygame.image.load('Images/hammer1.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))
    if botInventar[0][porNom] == 69:
        pix = pygame.image.load('Images/hammer2.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
    if botInventar[0][porNom] == 70:
        pix = pygame.image.load('Images/hammer3.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xInv,yInv))    
        
def printMagic(numberMagic):                                # Отображаем магические способности
    if numberMagic == 0: visibleMagic(16,548,0)
    if numberMagic == 1: visibleMagic(84,548,1)
    if numberMagic == 2: visibleMagic(152,548,2)
    if numberMagic == 3: visibleMagic(220,548,3)
    if numberMagic == 4: visibleMagic(16,616,4)
    if numberMagic == 5: visibleMagic(84,616,5)
    if numberMagic == 6: visibleMagic(152,616,6)
    if numberMagic == 7: visibleMagic(220,616,7)
    if numberMagic == 8: visibleMagic(16,684,8)
    if numberMagic == 9: visibleMagic(84,684,9)
    if numberMagic == 10: visibleMagic(152,684,10)
    if numberMagic == 11: visibleMagic(220,684,11)
    if numberMagic == 12: visibleMagic(16,752,12)
    if numberMagic == 13: visibleMagic(84,752,13)
    if numberMagic == 14: visibleMagic(152,752,14)
    if numberMagic == 15: visibleMagic(220,752,15)
         
def printInventar(numberInventar):                                # Отображаем инвентарь
    if numberInventar == 0: visibleInventar(772,548,0)
    if numberInventar == 1: visibleInventar(840,548,1)
    if numberInventar == 2: visibleInventar(908,548,2)
    if numberInventar == 3: visibleInventar(976,548,3)
    if numberInventar == 4: visibleInventar(772,616,4)
    if numberInventar == 5: visibleInventar(840,616,5)
    if numberInventar == 6: visibleInventar(908,616,6)
    if numberInventar == 7: visibleInventar(976,616,7)
    if numberInventar == 8: visibleInventar(772,684,8)
    if numberInventar == 9: visibleInventar(840,684,9)
    if numberInventar == 10: visibleInventar(908,684,10)
    if numberInventar == 11: visibleInventar(976,684,11)
    if numberInventar == 12: visibleInventar(772,752,12)
    if numberInventar == 13: visibleInventar(840,752,13)
    if numberInventar == 14: visibleInventar(908,752,14)
    if numberInventar == 15: visibleInventar(976,752,15)    
    
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
    
    global den
    global mesiac
    global god
    
    for n in range(16): # Рисуем иконки заклинаний
        printMagic(n)
    n = 0    
    for n in range(16): # Рисуем иконки инвентаря
        printInventar(n)  
    
    pygame.draw.rect(sc, (255, 255, 255), (284, 558, 481, 896)) 
    pygame.draw.rect(sc, (255, 255, 255), (405, 558, 365, 896))
    pix = pygame.image.load('Images/next.png') # Кнопка "Конец хода" она нужна)
    x_len = pix.get_width()
    y_len = pix.get_height() 
    sc.blit(pix, (286,786))
    
    xHero = 340
    yHero = 548
    if myHero == 50:
        pix = pygame.image.load('Images/akami.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Аками - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 51:
        pix = pygame.image.load('Images/artes.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Артес - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 52:
        pix = pygame.image.load('Images/deathOwner.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Владыка Смерти - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 54:
        pix = pygame.image.load('Images/djepotai.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Джепотай - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 55:
        pix = pygame.image.load('Images/farion.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Фарион - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 56:
        pix = pygame.image.load('Images/garitos.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Гаритос - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 57:
        pix = pygame.image.load('Images/gendalf.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Гендальф - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 58:
        pix = pygame.image.load('Images/illidan.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Иллидан - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 59:
        pix = pygame.image.load('Images/jaina.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Джайна - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 60:
        pix = pygame.image.load('Images/kell.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Келл - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 70:
        pix = pygame.image.load('Images/uter.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Утер - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 72:
        pix = pygame.image.load('Images/vulDjin.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Вул Джин - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 68:
        pix = pygame.image.load('Images/silvana.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Сильвана - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 65:
        pix = pygame.image.load('Images/pradmur.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Прадмур - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 69:
        pix = pygame.image.load('Images/trall.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Тралл - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    if myHero == 73:
        pix = pygame.image.load('Images/zadira.jpg') 
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (xHero,yHero))
        variableName = u"Задира - " + str(botLvl[0]) + " lvl"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(290, 617)) 
    
    variableExpirience = "" + str(botExpirience[0]) + " XP"  # переменная типа String - опыт
    healtObj = textExpirience.render(variableExpirience, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(healtObj,(290, 631)) # Отображаем Опыт    
    
    variableHealt = "" + str(botZdorovie[0]) + " / " + str(botIshZdorovie[0]) # переменная типа String отображающая здоровье как ххх/ххх
    healtObj = healt.render(variableHealt, False, (0, 255, 0)) # Создали объект типа "текст" 
    sc.blit(healtObj,(290, 644)) # Отображаем здоровье
    
    variableMana = "" + str(botMana[0]) + " / " + str(botIshMana[0]) # переменная типа String отображающая ману как ххх/ххх
    manaObj = manna.render(variableMana, False, (0, 0, 255)) # Создали объект типа "текст" 
    sc.blit(manaObj,(290, 657)) # Отображаем ману
    
    variableSila = u"Сила: " + str(botSila[0]) 
    silaObj = textSila.render(variableSila, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(silaObj,(290, 670)) 
    
    variableLovk = u"Ловкость: " + str(botLovkost[0]) 
    lovkObj = textLovk.render(variableLovk, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(lovkObj,(290, 683)) 
    
    variableYdacha = u"Удача: " + str(botYdacha[0]) 
    ydachaObj = textYdacha.render(variableYdacha, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(ydachaObj,(290, 696))
    
    if botHod[0] >= 1:
        variableHod = u"Остаток хода: " + str(botHod[0]) 
        hodObj = textHod.render(variableHod, False, (0, 0, 0)) # Создали объект типа "текст" 
        sc.blit(hodObj,(290, 722))
    if botHod[0] < 1:   
        variableHod = u"Остаток хода: " + str(botHod[0]) 
        hodObj = textHod.render(variableHod, False, (255, 0, 0)) # Создали объект типа "текст" 
        sc.blit(hodObj,(290, 722))    
    
    variableZoloto = u"Золото: " + str(botZoloto[0]) 
    zolotoObj = textZoloto.render(variableZoloto, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(zolotoObj,(290, 735))
    
    variableSerebro = u"Серебро: " + str(botSerebro[0]) 
    serebroObj = textSerebro.render(variableSerebro, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(serebroObj,(290, 748))
    
    variableBronza = u"Бронза: " + str(botBronza[0]) 
    bronzaObj = textBronza.render(variableBronza, False, (0, 0, 0)) # Создали объект типа "текст" 
    sc.blit(bronzaObj,(290, 761))
    
    pygame.display.update()  
    # ============================================================================================

def initGame(heroSelect):  # функция инициации игры
    global xHero
    global yHero
    global world
    global step
    
    global imHero
    global botZoloto
    global botSerebro
    global botBronza
    global bot
    global botNumer
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
    global botNumer
    global botVariant
    global botAlgoritm
    global botLocation
    global botDeistvie
    
    global den
    global mesiac
    global god
    imHero = 0
    pygame.draw.rect(sc, (255, 255, 255), (0, 548, 1056, 896)) 
    bot = 1 # Очищаем информацию о ботах
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
    n = 0  
    botLocation[0] = 172 # Исходное положение на карте
    xBot[0] = 400
    yBot[0] = 256
     # Задаём начальные параметры персонажа
    if heroSelect == 50: # Akami
        botExpirience[0] = 0
        botLvl[0] = 10                                                         #botLvl[0] = 1
        botRasa[0] = 2
        botInventar[0] = [55,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0]     #botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [22,1,2,3,4,5,6,7,8,9,10,11,12,13,14,100]           #botZaklinania[0] = [22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                  #botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 1120                                               #botIshZdorovie[0] = 120
        botZdorovie[0] = 1120                                                  #botZdorovie[0] = 120
        botMana[0] = 1000                                                      #botMana[0] = 50 
        botIshMana[0] = 1000                                                   #botIshMana[0] = 50
        botSila[0] = 50                                                        #botSila[0] = 14
        botLovkost[0] = 20                                                     #botLovkost[0] = 6
        botYdacha[0] = 7                                         
        botZoloto[0] = 100                                                     #botZoloto[0] = 0
        botSerebro[0] = 1000                                                   #botSerebro[0] = 3
        botBronza[0] = 100000                                                  #botBronza[0] = 0
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 50
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif heroSelect == 51: # Artes
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 1
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 110
        botZdorovie[0] = 110
        botMana[0] = 0
        botIshMana[0] = 0
        botSila[0] = 12
        botLovkost[0] = 6
        botYdacha[0] = 5
        botZoloto[0] = 0
        botSerebro[0] = 9
        botBronza[0] = 50
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 51
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif heroSelect == 52: # Death Owner
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 7
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [5,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 90
        botZdorovie[0] = 90
        botMana[0] = 100
        botIshMana[0] = 100
        botSila[0] = 9
        botLovkost[0] = 5
        botYdacha[0] = 9
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 0
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 52
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 54: # DjePoTai
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 2
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 120
        botZdorovie[0] = 120
        botMana[0] = 60
        botIshMana[0] = 60
        botSila[0] = 15
        botLovkost[0] = 7
        botYdacha[0] = 5
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 150
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 4
        botVariant[0] = 54
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 55: # Farion
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 6
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 110
        botZdorovie[0] = 110
        botMana[0] = 80
        botIshMana[0] = 80
        botSila[0] = 10
        botLovkost[0] = 6
        botYdacha[0] = 6
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 200
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 55
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 56: # Garitos
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 1
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 130
        botZdorovie[0] = 130
        botMana[0] = 0
        botIshMana[0] = 0
        botSila[0] = 15
        botLovkost[0] = 7
        botYdacha[0] = 7
        botZoloto[0] = 0
        botSerebro[0] = 5
        botBronza[0] = 0
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 56
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 57: # Gendalf
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 1
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [8,22,6,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 85
        botZdorovie[0] = 85
        botMana[0] = 120
        botIshMana[0] = 120
        botSila[0] = 9
        botLovkost[0] = 6
        botYdacha[0] = 9
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 0  
        botHod[0] = botLovkost[0] 
        botAlgoritm[0] = 3        
        botVariant[0] = 57
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 58: # Illidan
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 2
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 120
        botZdorovie[0] = 120
        botMana[0] = 60
        botIshMana[0] = 60
        botSila[0] = 11
        botLovkost[0] = 7
        botYdacha[0] = 5
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 0  
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 58
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 59: # Jaina
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 2
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 100
        botZdorovie[0] = 100
        botMana[0] = 50
        botIshMana[0] = 50
        botSila[0] = 9
        botLovkost[0] = 7
        botYdacha[0] = 10
        botZoloto[0] = 0
        botSerebro[0] = 1
        botBronza[0] = 120   
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 59
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 60: # Kell
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 7
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [10,12,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 120
        botZdorovie[0] = 120
        botMana[0] = 80
        botIshMana[0] = 80
        botSila[0] = 14
        botLovkost[0] = 7
        botYdacha[0] = 7
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 200
        botHod[0] = botLovkost[0]  
        botAlgoritm[0] = 4      
        botVariant[0] = 60
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 70: # Uter
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 1
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 150
        botZdorovie[0] = 150
        botMana[0] = 0
        botIshMana[0] = 0
        botSila[0] = 15
        botLovkost[0] = 6
        botYdacha[0] = 8
        botZoloto[0] = 0
        botSerebro[0] = 10
        botBronza[0] = 0 
        botHod[0] = botLovkost[0]    
        botAlgoritm[0] = 3  
        botVariant[0] = 70
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 72: # Vul Djin
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 6
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [7,11,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 120
        botZdorovie[0] = 120
        botMana[0] = 100
        botIshMana[0] = 100
        botSila[0] = 12
        botLovkost[0] = 6
        botYdacha[0] = 8
        botZoloto[0] = 0
        botSerebro[0] = 10
        botBronza[0] = 0  
        botHod[0] = botLovkost[0]    
        botAlgoritm[0] = 4    
        botVariant[0] = 72
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif heroSelect == 68: # Silvana
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 2
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 110
        botZdorovie[0] = 110
        botMana[0] = 70
        botIshMana[0] = 70
        botSila[0] = 11
        botLovkost[0] = 7
        botYdacha[0] = 4
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 50  
        botHod[0] = botLovkost[0]
        botAlgoritm[0] = 3
        botVariant[0] = 68
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif heroSelect == 65: # Pradmur
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 1
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 100
        botZdorovie[0] = 100
        botMana[0] = 0
        botIshMana[0] = 0
        botSila[0] = 10
        botLovkost[0] = 6
        botYdacha[0] = 9
        botZoloto[0] = 0
        botSerebro[0] = 5
        botBronza[0] = 0 
        botHod[0] = botLovkost[0] 
        botAlgoritm[0] = 3 
        botVariant[0] = 65
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 69: # Trall
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 6
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 140
        botZdorovie[0] = 140
        botMana[0] = 0
        botIshMana[0] = 0
        botSila[0] = 17
        botLovkost[0] = 6
        botYdacha[0] = 5
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 0   
        botHod[0] = botLovkost[0] 
        botAlgoritm[0] = 4
        botVariant[0] = 69
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif heroSelect == 73: # Zadira
        botExpirience[0] = 0
        botLvl[0] = 1
        botRasa[0] = 6
        botInventar[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botZaklinania[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100]
        botVozdeistvie[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        botIshZdorovie[0] = 120
        botZdorovie[0] = 120
        botMana[0] = 0
        botIshMana[0] = 0
        botSila[0] = 15
        botLovkost[0] = 6
        botYdacha[0] = 7
        botZoloto[0] = 0
        botSerebro[0] = 0
        botBronza[0] = 170 
        botHod[0] = botLovkost[0]  
        botAlgoritm[0] = 4
        botVariant[0] = 73
        botDeistvie[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    temp = 0
    step = 172
    xGameMap = 16 
    yGameMap = 96 
    den = 1
    mesiac = 1
    god = 1
    botVariant[0] = hero
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
    print(" ")
        
    botZachita[0] = 0 # Обнуляем защиту при новой игре
    n = 0
    for n in range(16): # Рисуем иконки заклинаний
        printMagic(n)
    n = 0
    for n in range(16): # Рисуем иконки инвентаря
        printInventar(n)
    n = 0    
    world[145] = 8  
    world[298] = 5
    world[416] = 10
    world[31] = 15
    
    worldUpdate()
    pix = pygame.image.load('Images/next.png') # Рисуем кнопку "Конец хода"
    x_len = pix.get_width()
    y_len = pix.get_height() 
    sc.blit(pix, (286,786))
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
    
    # Тут мы считаем опыт всех активных объектов
            
    
    n = 0
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
            
        elif i.type == pygame.KEYDOWN and newGame == 1 and botHod[0] > 0:
            
            if i.key == pygame.K_LEFT and xBot[0] >= 18 and world[botLocation[0]-1] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[0],yBot[0]))
                xBot[0] -= 32
                world[botLocation[0]] = 0
                world[botLocation[0]-1] = hero
                botLocation[0] -= 1
                botHod[0] -= 1
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")    # =======
                worldUpdate()
                heroPanel(hero)
            elif i.key == pygame.K_RIGHT and xBot[0] <= 990 and world[botLocation[0]+1] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[0],yBot[0]))
                xBot[0] += 32
                world[botLocation[0]] = 0
                world[botLocation[0]+1] = hero
                botLocation[0] += 1
                botHod[0] -= 1
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")   # =======
                worldUpdate()
                heroPanel(hero)
            elif i.key == pygame.K_UP and yBot[0] >= 96 and world[botLocation[0]-32] == 0:
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[0],yBot[0]))
                yBot[0] -= 32
                world[botLocation[0]] = 0
                world[botLocation[0]-32] = hero
                botLocation[0] -= 32
                botHod[0] -= 1
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")  # =======
                worldUpdate()
                heroPanel(hero)
            elif i.key == pygame.K_DOWN and yBot[0] <= 510 and world[botLocation[0]+32] == 0: 
                pix = pygame.image.load('Images/weed.jpg')
                x_len = pix.get_width()
                y_len = pix.get_height() 
                sc.blit(pix, (xBot[0],yBot[0]))
                yBot[0] += 32
                world[botLocation[0]] = 0
                world[botLocation[0]+32] = hero
                botLocation[0] += 32
                botHod[0] -= 1
                for n in range(14): # Сотри, это отладочные строки
                    print(world[temp:temp+32]) 
                    temp += 32
                print(" ")  # =======
                worldUpdate()
                heroPanel(hero)


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
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(1)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(2)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(3)
                
    if mos_x>145 and (mos_x<175):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(4) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(5)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(6)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(7)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(8)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(9) 
                
    if mos_x>337 and (mos_x<367):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(10)
    
    if mos_x>369 and (mos_x<399):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:  doebaca(11)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(12)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(13)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(14) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(15)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(16)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(17)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(18)
                
    if mos_x>625 and (mos_x<655):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(19)
                
    if mos_x>657 and (mos_x<687):  x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(20)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(21)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(22)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(23)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:doebaca(24) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(25)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(26)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(27)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(28)
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(29)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(30)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(31)
                
    #===================================================2 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(32)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(33)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(34)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(35)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(36) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(37)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(38)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(39)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(40)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(41) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(42)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(43)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(44)          
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(45)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(46) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(47)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(48)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(49)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(50)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(51)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(52)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(53)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(54)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(55)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(56) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(57)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(58)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(59)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(60)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(61)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(62)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(63)
                
    #===================================================3 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(64)

    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(65)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(66)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(67)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(68) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(69)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(70)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(71)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(72)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(73) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(74)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(75)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(76)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(77)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(78) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(79)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(80)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(81)
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(82)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(83)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(84)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(85)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(86)
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(87)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(88)
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(89)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(90)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(91)
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(92)
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(93)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(94)
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(95)
    
    #===================================================4 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(96)
    
    if mos_x>49 and (mos_x<79):  x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(97)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(98)
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(99)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(100) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(101)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(102)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(103)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(104)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(105) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(106)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(107)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(108)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(109)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(110) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(111)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(112) 
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(113)             
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(114) 
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(115) 
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(116) 
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(117) 
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(118)             
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(119) 
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(120)  
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(121) 
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(122) 
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(123)             
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(124)   
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(125) 
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(126)     
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(127)    
                
    #===================================================5 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(128) 
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(129) 
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(130)             
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(131)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(132) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(133)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(134)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(135)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(136)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(137) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(138)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(139)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(140)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(141)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(142) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(143)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(144)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(145)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(146)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(147)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(148)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(149)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(150)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(151)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(152)  
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(153) 
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(154) 
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(155)             
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(156)   
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(157) 
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(158)     
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(159)  
                
    #===================================================6 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(160) 
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(161)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(162)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(163)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(164) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(165)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(166)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(167)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(168)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(169) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(170)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(171)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(172)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(173)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(174) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(175)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(176)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(177)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(178)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(179)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(180)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(181)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(182)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(183)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(184) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(185)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(186)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(187)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(188)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(189)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(190)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(191)     
                
    #===================================================7 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(192) 
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(193) 
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(194)             
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(195) 
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(196)  
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(197) 
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(198) 
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(199)             
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(200) 
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(201) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(202)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(203)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(204)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(205)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(206) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(207)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(208)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(209)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(210)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(211)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(212)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(213)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(214)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(215)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(216) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(217)
    
    if mos_x>849 and (mos_x<879):  x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(218)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(219)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(220)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(221)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(222)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(223)
            
    #===================================================8 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(224)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(225)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(226)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(227)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(228) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(229)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(230)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(231)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(232)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(233) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(234)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(235)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(236)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(237)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(238) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(239)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(240)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(241)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(242)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(243)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(244)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(245)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(246)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(247)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(248) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(249)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(250)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(251)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(252)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(253)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(254)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(255)  
            
    #===================================================9 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(256)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(257)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(258)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(259)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(260) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(261) 
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(262) 
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(263)             
    
    if mos_x>273 and (mos_x<303):  x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(264) 
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(265)  
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(266) 
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(267) 
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(268)             
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(269) 
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(270)  
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(271) 
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(272) 
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(273)             
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(274) 
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(275) 
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(276) 
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(277) 
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(278)             
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(279) 
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(280)  
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(281)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(282)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(283)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(284)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(285)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(286)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(287)    
            
    #===================================================10 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(288)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(289)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(290)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(291)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(292) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(293)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(294)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(295)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(296)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(297) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN: 
            if i.button == 1: doebaca(298)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(299)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(300)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(301)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(302) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(303)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(304)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(305)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(306)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(307)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(308)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(309)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(310)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(311)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(312) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(313)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(314)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(315)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(316)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(317)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(318)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(319)    
            
    #===================================================11 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(320)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(321)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(322)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(323)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(324) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(325)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(326)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(327)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(328)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(329) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(330)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(331)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(332)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(333)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(334) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(335)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(336)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(337)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(338)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(339)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(340)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(341)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(342)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(343)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(344) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(345)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(346)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(347)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(348)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(349)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(350)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(351)  
            
    #===================================================12 ряд===============================================
    if mos_x>17 and (mos_x<47): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(352)
    
    if mos_x>49 and (mos_x<79): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(353)
    
    if mos_x>81 and (mos_x<111): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(354)            
    
    if mos_x>113 and (mos_x<143): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(355)
                
    if mos_x>145 and (mos_x<175): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(356) 
               
    if mos_x>176 and (mos_x<207): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(357)
    
    if mos_x>209 and (mos_x<239): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(358)
    
    if mos_x>241 and (mos_x<271): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(359)            
    
    if mos_x>273 and (mos_x<303): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(360)
                
    if mos_x>305 and (mos_x<335): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(361) 
                
    if mos_x>337 and (mos_x<367): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(362)
    
    if mos_x>369 and (mos_x<399): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(363)
    
    if mos_x>401 and (mos_x<431): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(364)            
    
    if mos_x>433 and (mos_x<463): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(365)
                
    if mos_x>465 and (mos_x<495): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(366) 
               
    if mos_x>497 and (mos_x<527): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(367)
    
    if mos_x>529 and (mos_x<559): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(368)
    
    if mos_x>561 and (mos_x<591): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(369)            
    
    if mos_x>593 and (mos_x<623): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(370)
                
    if mos_x>625 and (mos_x<655): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(371)
                
    if mos_x>657 and (mos_x<687): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(372)
    
    if mos_x>689 and (mos_x<719): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(373)
    
    if mos_x>721 and (mos_x<751): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(374)            
    
    if mos_x>753 and (mos_x<783): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(375)
                
    if mos_x>785 and (mos_x<815): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(376) 
               
    if mos_x>817 and (mos_x<847): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(377)
    
    if mos_x>849 and (mos_x<879): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(378)
    
    if mos_x>881 and (mos_x<911): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(379)            
    
    if mos_x>913 and (mos_x<943): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(380)  
                
    if mos_x>945 and (mos_x<975): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(381)
                
    if mos_x>977 and (mos_x<1007): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(382)    
                
    if mos_x>1009 and (mos_x<1040): x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: doebaca(383) 
            
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
                doebaca(384)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(385)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(386)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(387)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(388) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(389)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(390)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(391)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(392)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(393) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(394)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(395)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(396)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(397)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(398) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(399)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(400)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(401)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(402)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(403)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(404)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(405)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(406)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(407)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(408) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(409)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(410)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(411)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(412)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(413)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(414)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>481 and (mos_y<511):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(415)     
            
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
                doebaca(416)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(417)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(418)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(419)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(420) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(421)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(422)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(423)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(424)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(425) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(426)
    
    if mos_x>369 and (mos_x<399):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(427)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(428)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(429)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(430) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(431)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(432)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(433)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(434)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(435)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(436)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(437)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(438)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(439)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(440) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(441)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(442)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(443)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(444)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(445)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(446)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>513 and (mos_y<543):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(447)                                                 
                                                                                                                                            
        
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1:  
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1:  
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
                 if newGameButton == 0 and newGame == 1:
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
                 if newGameButton == 0 and newGame == 1:
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
                 if newGameButton == 0 and newGame == 1:
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
                 if newGameButton == 0 and newGame == 1: 
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
                 if newGameButton == 0 and newGame == 1:  
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
                 if newGameButton == 0 and newGame == 1:  
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
                 if newGameButton == 0 and newGame == 1:
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
    
    if mos_x>286 and (mos_x<414):  # Следующий ход
        x_inside = True
    else: x_inside = False
    if mos_y>786 and (mos_y<816):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if newGame == 1 and buttonNextStep == 0:
                    pygame.time.delay(200)
                    buttonNextStep = 1 # Переводим кнопу в неактивный режим
                    botHod[0] = botLovkost[0]
                    heroPanel(hero)
                    botActivity() 
                    zakl = 0
                    invent = 0
                    n = 0
                    for n in range(16): # Рисуем иконки заклинаний
                        printMagic(n)
                    n = 0    
                    for n in range(16): # Рисуем иконки инвентаря
                        printInventar(n)    
                    n = 1    
                    if botZdorovie[0]+3 < botIshZdorovie[0]: botZdorovie[0] += 2
                    if botMana[0]+3 < botIshMana[0]: botMana[0] += 2
                    for n in range(1000):
                        botHod[n] = botLovkost[n]
                        if botZdorovie[n]+3 < botIshZdorovie[n]: botZdorovie[n] += 2
                        if botMana[n]+3 < botIshMana[n]: botMana[n] += 2
                        
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
                    useInventar(invent)
                    yes = 1
                    
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
                    botInventar[imHero][invent-1] = 0
                    heroPanel(hero) 
                    no = 1                    
    pygame.display.update()    
    
# Объекты которые могут быть на карте и их номера
# 0 - Трава, 1 - Горы, 2 - Вода, 3 - жилище зельевара, 4 - лачуга шамана, 5 - хижина мага, 6 - кузница,
# 7 - дом коллекционера, 8 - рынок, 9 - вспаханная земля, 10 - портал
# 11 - Полуросль, 12 - Рожь, 13 - Картофель, 14 - Сундук, 15 - Врата города
# 16 - Таверна

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
# 141 - Орк 6 ур, 142 - Орк 7 ур, 143 - Орк-шаман, 144 - Оккультист, 145 - Разбойник, 146 - грабитель
# 147 - Красный огненный голем, 148 - Скелет 1 ур, 149 - Скелет 2 ур, 150 - Скелет 3 ур
# 151 - Скелет 4 ур, 152 - Скелет 5 ур, 153 - Скелет 6 ур, 154 - Скелет 7 ур, 155 - Скелет 8 ур
# 156 - Душекрад, 157 - Странник, 158 - Тролль 1 ур, 159 - Тролль 2 ур, 160 - Тролль 3 ур
# 161 - Тролль 4 ур, 162 - Тролль 5 ур, 163 - Тролль 6 ур, 164 - Вампир, 165 - Колдун
# 166 - Женщина-эльф 1 ур, 167 - Женщина-эльф 2 ур, 168 - Женщина-эльф 3 ур
# 169 - Женщина-эльф 4 ур, 170 - Женщина-эльф 5 ур, 171 - Женщина-эльф 6 ур
# 172 - Женщина-эльф 7 ур    
