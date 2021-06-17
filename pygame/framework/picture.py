import pygame

# 初始化设置
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("加载图片")
keep_going = True
pic = pygame.image.load("python.jpg") # 从python.jpg载入图像，保存到变量pic中

# 游戏循环
while keep_going:
    for event in pygame.event.get(): # 循环遍历事件
        if event.type == pygame.QUIT:
            keep_going = False
    screen.blit(pic,(200,100)) # blit()方法将图片pic绘制到screen屏幕的（200,100）位置上
    pygame.display.update()
# 游戏退出
pygame.quit()