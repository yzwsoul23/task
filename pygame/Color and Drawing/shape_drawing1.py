# 导入一个名为pygame的函数库
import pygame
from math import pi
 
# 初始化游戏引擎
pygame.init()
 
# 定义我们将使用RGB格式的颜色
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# 设置屏幕的高度和宽度
size = [600, 400]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
# 循环，直到用户单击关闭按钮
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # 这将while循环限制为每秒最多10次。
    # 去掉这个，我们将使用所有的CPU我们可以。
    clock.tick(10)
     
    for event in pygame.event.get(): # 用户做了一些
        if event.type == pygame.QUIT: # 如果用户点击关闭
            done=True # 标记完成，退出循环
 
    # 所有绘图代码都发生在for循环和but之后
    # 在main while done==False循环
     
    # 清除屏幕并设置屏幕背景
    screen.fill(BLACK)
 
    # 在屏幕上从(0,0)到(50,30)画一条绿线
    # 5像素宽
    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
 
    # 在屏幕上画3条黑线，每条5像素宽。
    # “False”表示第一个点和最后一个点没有连接。
    pygame.draw.lines(screen, WHITE, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    
    # 在屏幕上从(0,50)到(50,80)绘制一条绿线
    # 因为它是反锯齿线，它是1像素宽。
    pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)

    # 绘制一个矩形轮廓线
    pygame.draw.rect(screen, WHITE, [75, 10, 50, 20], 2)
     
    # 绘制一个实心矩形
    pygame.draw.rect(screen, WHITE, [150, 10, 50, 20])

    # 画一个圆角矩形
    pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
    pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=15, border_top_left_radius=0,
                     border_bottom_right_radius=15)

    # 绘制一个椭圆轮廓线，使用一个矩形作为外部边界
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

    # 绘制一个实心椭圆，使用一个矩形作为外部边界
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20]) 
 
    # 它使用polygon命令绘制一个三角形
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
  
    # 画一条弧作为椭圆的一部分
    # 使用弧度确定绘制的角度
    pygame.draw.arc(screen, WHITE,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
    pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    
    # 绘制一个圆
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

    # 绘制一个圆的四分之一
    pygame.draw.circle(screen, BLUE, [250, 250], 40, 0, draw_top_right=True)
    pygame.draw.circle(screen, RED, [250, 250], 40, 30, draw_top_left=True)
    pygame.draw.circle(screen, GREEN, [250, 250], 40, 20, draw_bottom_left=True)
    pygame.draw.circle(screen, WHITE, [250, 250], 40, 10, draw_bottom_right=True)

    # 继续并使用我们所绘制的内容更新屏幕。
    # 这必须发生在所有其他绘制命令之后。
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()