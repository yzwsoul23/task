# Unit PYG02: Pygame Event Post
import pygame,sys
# 初始化设置
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame事件处理")
fps = 1
fclock = pygame.time.Clock()
num = 1
# 游戏循环
while True:
    uevent = pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key":pygame.K_SPACE, "mod":pygame.KMOD_ALT})
    #创建一个事件一个键按下unicode码为123, 常量名称pygame.K_SPACE, 修饰符为pygame.KMOD_ALT
    pygame.event.post(uevent)#产生一个事件，并将其放入事件队列
    num = num + 1 #设置按键序号
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN {}]:".format(num), "#", event.key, event.mod) #显示按键状态
            else:
                print("[KEYDOWN {}]:".format(num), event.unicode, event.key, event.mod) #显示按键状态
    pygame.display.update()
    fclock.tick(fps)