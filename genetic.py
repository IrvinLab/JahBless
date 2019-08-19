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

hod = 0
zachita = 0
attack = 0
zakl = 0
invent = 0
imBuyThis = 0
thisPlace = 0
market = [2,7,0,26,0,0,17,46,60,0,0,0,0,0,0,36] # В этом массиве лежит инвентарь, который доступен на рынке
yaNaRinke = 0

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
tmpMarket = 0
zyxel = 0
pygame.init()
sc = pygame.display.set_mode((1056, 896))
pygame.display.set_caption("Kings of New World")
clock = pygame.time.Clock()
pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896)) 