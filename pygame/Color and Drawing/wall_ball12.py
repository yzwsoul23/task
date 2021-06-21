# Unit PYG05: Pygame Wall Ball Game Version 11
import pygame, sys
import pygame.freetype

pygame.init()
size = width, height = 600, 400
speed1 = [1,1]
speed2 = [1,1]
WHITE = 255, 255, 255
BLACK = 0, 0, 0
pos1 = [230, 160]
pos2 = [150, 210]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame文字绘制")
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1surf, f1rect = f1.render("世界和平", fgcolor=WHITE, size=50)
f2surf, f2rect = f1.render("世界核平", fgcolor=BLACK, size=50)
fps = 120
fclock = pygame.time.Clock()
bgcolor = pygame.Color("black")
def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))
bgcolor.r = RGBChannel((pos1[0]+pos2[0])*255/width)
bgcolor.g = RGBChannel((pos1[1]+pos2[1])*255/height)
bgcolor.b = RGBChannel(min(speed1[0],speed2[1])*255/max(speed2[0],speed1[1],1))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN: #判断是否按下键盘
            if event.key==pygame.K_LEFT: #判断是否按下左键
                speed[0]=speed[0] if speed[0] ==width+1 else speed[0]-1# 向左移动1
            elif event.key==pygame.K_RIGHT: #判断是否按下右键
                speed[0]=speed[0] if speed[0] ==width+1 else speed[0]+1# 向右移动1
            elif event.key==pygame.K_UP: #判断是否按下上键
                speed[1]=speed[1] if speed[1] ==height+1 else speed[1]-1# 向上移动1
            elif event.key==pygame.K_DOWN: #判断是否按下下键
                speed[1]=speed[1] if speed[1] ==height+1 else speed[1]+1# 向下移动1
            elif event.key==pygame.K_ESCAPE:
                sys.exit()
    if pos1[0] < 0 or pos1[0] + f1rect.width > width:
        speed1[0] = - speed1[0]
    if pos1[1] <0 or pos1[1] + f1rect.height > height:
        speed1[1] = - speed1[1]
    if pos2[0] < 0 or pos2[0] + f1rect.width > width:
        speed2[0] = - speed2[0]
    if pos2[1] <0 or pos2[1] + f1rect.height > height:
        speed2[1] = - speed2[1]
    pos1[0] = pos1[0] + speed1[0]
    pos1[1] = pos1[1] + speed1[1]
    pos2[0] = pos2[0] - speed2[0]
    pos2[1] = pos2[1] - speed2[1]
    bgcolor.r = RGBChannel(pos1[0]*255/width)
    bgcolor.g = RGBChannel(pos2[1]*255/height)
    bgcolor.b = RGBChannel(min(speed1[0],speed2[1])*255/max(speed2[0],speed1[1],1))
    screen.fill(bgcolor)
    screen.blit(f1surf, (pos1[0], pos1[1]))
    screen.blit(f2surf, (pos2[0], pos2[1]))
    pygame.display.update()
    fclock.tick(fps)