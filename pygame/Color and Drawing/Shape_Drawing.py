# Unit PYG05: Pygame Shape Draw Test
import pygame, sys
from math import pi #引用pi圆周率

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame图形绘制")
GOLD = 255, 251, 0
RED = pygame.Color('red')
WHITE = 255, 255, 255
GREEN = pygame.Color('green')

#r1rect = pygame.draw.rect(screen, GOLD, (100,100,200,100), 5)
#r2rect = pygame.draw.rect(screen, RED, (210,210,200,100), 0)

e1rect = pygame.draw.ellipse(screen, GREEN, (50,50,500,300), 3) #画椭圆(左端x：50,上端y：50,宽：500,高：300), 线粗：3)
c1rect = pygame.draw.circle(screen, GOLD, (200,180), 30, 5) #画圆(左端x：200,上端y：180),高：30, 线粗：5)
c2rect = pygame.draw.circle(screen, GOLD, (400,180), 30) #画圆(左端x：400,上端y：180),高：30)
r1rect = pygame.draw.rect(screen, RED, (170, 130, 60, 10), 3) #画矩形(左端x：170,上端y：130,宽：60,高：10), 线粗：3)
r2rect = pygame.draw.rect(screen, RED, (370, 130, 60, 10)) #画矩形(左端x：370,上端y：130,宽：60,高：10))
plist = [(295,170), (285,250), (260,280), (340,280), (315,250), (305,170)]
l1rect = pygame.draw.lines(screen, GOLD, True, plist, 2) #画直线 是否要封口True, 连续多线顶点列表plist, 线宽2
alist = (95,10), (28,50),(20,95), (125,400), (31,20), (205,70)
a1aline = pygame.draw.aalines(screen,WHITE,True,alist, blend=1)
a1rect = pygame.draw.arc(screen, RED, (200,220,200,100), 1.4*pi, 1.9*pi, 3) #画弧(左端x：50,上端y：50,宽：500,高：300),取起始弧度1.4*pi,取结束弧度1.9*pi,线粗3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()