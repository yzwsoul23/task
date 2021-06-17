# Unit PYG02: Pygame Hello World Game
import pygame,sys
# 初始化设置
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame游戏之旅")
# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()