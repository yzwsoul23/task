# Unit PYG03: Pygame Wall Ball Game version 7  感知型
#引入pygame,sys
import pygame,sys
#初始化init及设置
pygame.init()
size = width,height = 600,400
speed = [1,1]
screen=pygame.display.set_mode(size,pygame.RESIZABLE) #ygame.RESIZABLE自由调节边框
#screen=pygame.display.set_mode(size,pygame.NOFRAME) pygame.NOFRAME无边框
#screen=pygame.display.set_mode(size,pygame.FULLSCREEN) pygame.FULLSCREEN根据设置像素拉伸全屏
#screen=pygame.display.set_mode(size)  
BLACK=0, 0, 0
pygame.display.set_caption('Pygame壁球')
icon = pygame.image.load("cartoon1.ico")#加载图标
pygame.display.set_icon(icon)#设定图标
ball=pygame.image.load('cartoon1.ico') #加载图像
ballrect=ball.get_rect() #pygame使用内部定义surface对象表示载入图像，.get_rect()方法是返回一个覆盖图像矩形rect对象
#Rect对象有一些重要属性,例如:
#top, bottom left, right表示上下左右
#width, height表示宽度、高度
fps=120
fclock=pygame.time.Clock() #每秒刷新频率
while True:
    #获取事件并逐类相应
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
        elif event.type == pygame.VIDEORESIZE: #新窗口大小
            size = width,height = event.size[0],event.size[1] #重新赋值size为新窗口大小
            screen=pygame.display.set_mode(size,pygame.RESIZABLE) #将屏幕大小重新设置
    if pygame.display.get_active():
        ballrect = ballrect.move(speed)#图像的移动
    #壁球的反弹运动
    #遇到左右两侧,横向速度取反
    if ballrect.left<0 or ballrect.right>width:
        speed[0]= -speed[0]
    #遇到上下两侧,纵向速度取反
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]= -speed[1]
    #填充颜色
    screen.fill(BLACK)
    #将图像绘制在另一个图像上面
    screen.blit(ball,ballrect)
    #刷新屏幕
    pygame.display.update()
    fclock.tick(fps)#每秒刷新频率