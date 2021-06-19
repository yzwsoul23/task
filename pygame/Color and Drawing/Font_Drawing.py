# Unit PYG05: Pygame Font Draw
import pygame, sys
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame文字绘制")
GOLD = 255, 251, 0

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36) #选定字体，文字类型地址和字号
#f1rect = f1.render_to(screen, (100,80), "世界核平", fgcolor=GOLD, size=100) #渲染文字，位置，内容，颜色，大小
f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)#渲染文字，内容，颜色，大小
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(f1surf, (200,160)) #渲染文字，位置
    pygame.display.update()