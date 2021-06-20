# Unit PYG05: Pygame Wall Ball Game Version 11
import pygame, sys
import pygame.freetype

pygame.init()
size = width, height = 600, 400
speed = [1,1]
GOLD = 255, 251, 0
BLACK = 0, 0, 0
pos = [230, 160]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame文字绘制")
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)
fps = 60
fclock = pygame.time.Clock()
bgcolor = pygame.Color("black")
def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))
bgcolor.r = RGBChannel(f1rect.width*255/width)
bgcolor.g = RGBChannel(f1rect.height*255/height)
bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = - speed[0]
    if pos[1] <0 or pos[1] + f1rect.height > height:
        speed[1] = - speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]
    bgcolor.r = RGBChannel(f1rect.width*255/width)
    bgcolor.g = RGBChannel(f1rect.height*255/height)
    bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))
    screen.fill(bgcolor)
    screen.blit(f1surf, (pos[0], pos[1]))
    pygame.display.update()
    fclock.tick(fps)
    print(bgcolor)