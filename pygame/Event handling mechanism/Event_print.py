# Unit PYG02: Pygame Hello World Game
import pygame,sys

from pygame.constants import KEYDOWN, KEYUP
# 初始化设置
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame游戏之旅")
# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN: #键盘按下
            if event.unicode == "":
                print("[KEYDOWN]:","#",event.key,event.mod)
            else:
                print("[KEYDOWN]:",event.unicode,event.key,event.mod)#event.unicode按键的unicode码,event.key按键的常量名称,event.mod按键的修饰符组合值
        elif event.type == KEYUP: #键盘释放
            if event.unicode == "":
                print("[KEYDOWN]:","#",event.key,event.mod)
            else:
                print("[KEYDOWN]:",event.unicode,event.key,event.mod)
        elif event.type == pygame.MOUSEMOTION: #鼠标移动
            print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons) #event.pos鼠标当前位置,event.rel鼠标运动距离, event.buttons鼠标按键状态
        elif event.type == pygame.MOUSEBUTTONUP: #鼠标键释放
            print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:#鼠标键按下
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
    pygame.display.update()
