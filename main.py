#self.resize(1056, 896)
# здесь подключаются модули
import pygame
 
# здесь определяются константы, классы и функции
FPS = 60
 
# здесь происходит инициация, создание объектов и др.
pygame.init()
sc = pygame.display.set_mode((1056, 896))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить объекты на экране
pygame.draw.rect(sc, (255, 255, 255), (0, 0, 1056, 896))



pygame.display.update()
 
# главный цикл
while True:
 
    # задержка
    clock.tick(FPS)
 
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()


 
    # --------
    # изменение объектов и многое др.
    # --------
 
    # обновление экрана
    pygame.display.update()
