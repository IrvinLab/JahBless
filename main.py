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
textDescription = pygame.font.SysFont('Monospace Regular', 20) #Описание объекта

for n in range(480): # Забиваем мир нулями
    world.append(n)
    world[n] = 0

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
    
        
        
        
def worldUpdate():   # Отправляем данные об объекте
    n = 0
    for n in range(448):
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
    pygame.draw.rect(sc, (255, 255, 255), (405, 558, 360, 896)) 
    if world[hehmda] == 3:
        pix = pygame.image.load('Images/jilZelievara.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = "Jiliche Zelievara"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = "V etoi hijine jivet starii master zelii, kotorii"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580)) 
        variableName = "za skromnuiu cenu prodast vam mnojectvo"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = "razlichnih zelii"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620)) 
        variableName = "Y zelievara mojno poluchit zadanie i"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))  
        variableName = "zarabotat dengi i opit za ego vipolnenie"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))
    if world[hehmda] == 4:
        pix = pygame.image.load('Images/lachugaShamana.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = "Lachuga Shamana"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = "V etoi hijine jivet shaman, kotorii sposoben"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = "za simvolicheskuiu ceny obuchit vas azam magii"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = "a takje mojet prodat vam knigi s zaklinaniami,"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = "i magicheskie predmeti"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640)) 
        variableName = "Y shamana mojno poluchit zadanie i zarabotat"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
        variableName = "dengi i opit za ego vipolnenie"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if world[hehmda] == 5:
        pix = pygame.image.load('Images/hijinaMaga.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = "Hijina Maga"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = "V etoi hijine jivet ochen starii mag, kotorii"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = "sposoben obuchit vas azam magii, a takje"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = "y nego mojno kupit i prodat nekotorie"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = "magicheskie artefacti i zelia"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))    
        variableName = "Y maga mojno poluchit zadanie i zarabotat"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 660))  
        variableName = "dengi i opit za ego vipolnenie"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 680)) 
    if world[hehmda] == 6:
        pix = pygame.image.load('Images/kuznica.png')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = "Kuznica"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = "V etoi kuznice trudiatse mastera svoego dela"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = "Zdes vi naidete dospehi i orujie"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600))  
        variableName = "Y kuzneca mojno poluchit zadanie i zarabotat"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = "dengi i opit za ego vipolnenie"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))   
    if world[hehmda] == 8:
        pix = pygame.image.load('Images/market.jpg')
        x_len = pix.get_width()
        y_len = pix.get_height() 
        sc.blit(pix, (340,548))
        variableName = "Rinok"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 560)) 
        variableName = "Suda vedut vse dorogi - na rinok"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 580))  
        variableName = "Da, chego tut tolko net. Vse za vashi dengi"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 600)) 
        variableName = "Tut vi mojete takje prodat nenujnie vechi"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 620))    
        variableName = "magicheskie artefacti i zelia"
        nameObj = textNameHero.render(variableName, False, (0, 0, 0)) 
        sc.blit(nameObj,(440, 640))     
        
        
        
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
    
    pygame.draw.rect(sc, (255, 255, 255), (405, 558, 360, 896)) 
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
    
    world[145] = 100  
    
    worldUpdate()
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
                worldUpdate()
                heroPanel(hero)
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
                worldUpdate()
                heroPanel(hero)
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
                worldUpdate()
                heroPanel(hero)
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
                worldUpdate()
                heroPanel(hero)


    mos_x, mos_y = pygame.mouse.get_pos() # Тут мы берём координаты мыши
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
                doebaca(0)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(1)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(2)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(3)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(4) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(5)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(6)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(7)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(8)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(9) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(10)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(11)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(12)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(13)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(14) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(15)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(16)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(17)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(18)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(19)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(20)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(21)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(22)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(23)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(24) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(25)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(26)
    
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
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(28)
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(29)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(30)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>97 and (mos_y<127):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(31) 
                
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
                doebaca(32)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(33)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(34)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(35)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(36) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(37)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(38)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(39)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(40)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(41) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(42)
    
    if mos_x>369 and (mos_x<399):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(43)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(44)          
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(45)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(46) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(47)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(48)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(49)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(50)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(51)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(52)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(53)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(54)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(55)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(56) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(57)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(58)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(59)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(60)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(61)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(62)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>129 and (mos_y<159):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(63)    
                
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
                doebaca(64)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(65)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(66)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(67)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(68) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(69)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(70)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(71)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(72)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(73) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(74)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(75)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(76)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(77)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(78) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(79)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(80)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(81)
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(82)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(83)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(84)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(85)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(86)
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(87)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(88)
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(89)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(90)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(91)
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(92)
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(93)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(94)
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>161 and (mos_y<191):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(95)
    
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
                doebaca(96)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(97)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(98)
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(99)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(100) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(101)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(102)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(103)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(104)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(105) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(106)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(107)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(108)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(109)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(110) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(111)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(112) 
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(113)             
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(114) 
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(115) 
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(116) 
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(117) 
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(118)             
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(119) 
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(120)  
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(121) 
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(122) 
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(123)             
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(124)   
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(125) 
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(126)     
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>193 and (mos_y<223):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(127)    
                
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
                doebaca(128) 
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(129) 
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(130)             
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(131)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(132) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(133)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(134)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(135)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(136)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(137) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(138)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(139)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(140)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(141)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(142) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(143)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(144)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(145)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(146)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(147)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(148)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(149)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(150)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(151)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(152)  
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(153) 
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(154) 
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(155)             
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(156)   
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(157) 
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(158)     
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>225 and (mos_y<255):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(159)  
                
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
                doebaca(160) 
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(161)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(162)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(163)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(164) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(165)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(166)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(167)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(168)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(169) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(170)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(171)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(172)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(173)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(174) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(175)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(176)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(177)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(178)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(179)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(180)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(181)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(182)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(183)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(184) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(185)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(186)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(187)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(188)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(189)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(190)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>257 and (mos_y<287):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(191)     
                
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
                doebaca(192) 
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(193) 
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(194)             
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(195) 
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(196)  
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(197) 
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(198) 
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(199)             
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(200) 
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(201) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(202)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(203)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(204)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(205)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(206) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(207)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(208)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(209)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(210)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(211)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(212)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(213)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(214)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(215)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(216) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(217)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(218)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(219)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(220)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(221)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(222)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>289 and (mos_y<319):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(223)
            
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
                doebaca(224)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(225)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(226)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(227)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(228) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(229)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(230)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(231)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(232)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(233) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(234)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(235)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(236)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(237)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(238) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(239)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(240)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(241)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(242)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(243)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(244)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(245)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(246)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(247)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(248) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(249)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(250)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(251)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(252)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(253)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(254)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>321 and (mos_y<351):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(255)  
            
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
                doebaca(256)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(257)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(258)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(259)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(260) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(261) 
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(262) 
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(263)             
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(264) 
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(265)  
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(266) 
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(267) 
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(268)             
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(269) 
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(270)  
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(271) 
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(272) 
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(273)             
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(274) 
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(275) 
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(276) 
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(277) 
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(278)             
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(279) 
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(280)  
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(281)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(282)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(283)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(284)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(285)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(286)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>353 and (mos_y<383):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(287)    
            
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
                doebaca(288)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(289)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(290)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(291)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(292) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(293)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(294)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(295)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(296)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(297) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(298)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(299)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(300)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(301)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(302) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(303)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(304)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(305)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(306)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(307)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(308)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(309)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(310)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(311)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(312) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(313)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(314)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(315)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(316)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(317)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(318)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>385 and (mos_y<415):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(319)    
            
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
                doebaca(320)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(321)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(322)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(323)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(324) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(325)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(326)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(327)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(328)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(329) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(330)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(331)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(332)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(333)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(334) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(335)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(336)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(337)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(338)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(339)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(340)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(341)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(342)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(343)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(344) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(345)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(346)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(347)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(348)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(349)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(350)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>417 and (mos_y<447):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(351)  
            
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
                doebaca(352)
    
    if mos_x>49 and (mos_x<79): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(353)
    
    if mos_x>81 and (mos_x<111): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(354)            
    
    if mos_x>113 and (mos_x<143):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(355)
                
    if mos_x>145 and (mos_x<175): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(356) 
               
    if mos_x>176 and (mos_x<207): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(357)
    
    if mos_x>209 and (mos_x<239): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(358)
    
    if mos_x>241 and (mos_x<271): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(359)            
    
    if mos_x>273 and (mos_x<303): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(360)
                
    if mos_x>305 and (mos_x<335):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(361) 
                
    if mos_x>337 and (mos_x<367): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(362)
    
    if mos_x>369 and (mos_x<399): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(363)
    
    if mos_x>401 and (mos_x<431):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(364)            
    
    if mos_x>433 and (mos_x<463):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(365)
                
    if mos_x>465 and (mos_x<495): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(366) 
               
    if mos_x>497 and (mos_x<527): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(367)
    
    if mos_x>529 and (mos_x<559): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(368)
    
    if mos_x>561 and (mos_x<591):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(369)            
    
    if mos_x>593 and (mos_x<623): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(370)
                
    if mos_x>625 and (mos_x<655): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(371)
                
    if mos_x>657 and (mos_x<687): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(372)
    
    if mos_x>689 and (mos_x<719):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(373)
    
    if mos_x>721 and (mos_x<751): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(374)            
    
    if mos_x>753 and (mos_x<783): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(375)
                
    if mos_x>785 and (mos_x<815): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(376) 
               
    if mos_x>817 and (mos_x<847): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(377)
    
    if mos_x>849 and (mos_x<879): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(378)
    
    if mos_x>881 and (mos_x<911): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(379)            
    
    if mos_x>913 and (mos_x<943):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(380)  
                
    if mos_x>945 and (mos_x<975):
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(381)
                
    if mos_x>977 and (mos_x<1007): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(382)    
                
    if mos_x>1009 and (mos_x<1040): 
        x_inside = True
    else: x_inside = False
    if mos_y>449 and (mos_y<479):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                doebaca(383) 
            
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
