import pygame

# 初始设置
pygame.init() # 初始化pygame
screen = pygame.display.set_mode((800,600)) # 创建一个800*600像素的显示窗口
pygame.display.set_caption("Pygame绘制图形") # 给屏幕窗口添加标题Pygame绘制图形
keep_going = True # 定义了一个布尔类型keep_going控制程序的持续运行
RED = (255,5,0)  # 红色，使用RGB颜色,(红色R,绿色G,蓝色B)
radius = 80 # 设置了圆的半径，变量radius = 80

# 游戏循环
while keep_going: #如果keep_going为True游戏一直持续进行
    for event in pygame.event.get():  # 使用for循环遍历Pygame中的所有事件
        if event.type == pygame.QUIT:  # 如果用户按下关闭按钮
            keep_going = False # 量keep_going变为False,退出程序
    pygame.draw.circle(screen,RED,(400,300),radius) # 在屏幕窗口(400,300)位置上绘制半径为80的，填充颜色为RED的圆。
    pygame.display.update()  # 刷新屏幕

# 退出程序
pygame.quit() # 当用户退出游戏的时候，调用这段代码，清楚所有的设置，关闭屏幕窗口