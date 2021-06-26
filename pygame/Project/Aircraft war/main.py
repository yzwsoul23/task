import random
import math
import pygame

# 初始化界面
pygame.init()
# 设置窗口大小
screen = pygame.display.set_mode((800,600))
# 设置窗口名称
pygame.display.set_caption('勇闯太空')
# 导入图标文件
icon = pygame.image.load('./resource/ufo.png')
# 设置窗口图标
pygame.display.set_icon(icon)
# 导入背景文件
bgimg = pygame.image.load('./resource/bg.png')
# 导入玩家角色文件
playerImg = pygame.image.load('./resource/player.png')
# 添加背景音
pygame.mixer.music.load('./resource/bg.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
# 初始化玩家角色位置及速度
playerX = 368
playerY = 500
player_step = 0
builtinboor = False

# 添加敌人
num_of_enemy = 6 # 敌人数量
# 创建敌人的类
class Enemy():
    def __init__(self):
        # 导入敌人角色文件
        self.Img = pygame.image.load('./resource/enemy.png')
        # 初始化敌人角色位置及速度
        self.x = random.randint(0,720)
        self.y = random.randint(0,150)
        self.step = random.randint(2,4)
    def reset(self): # 当被射中时,恢复位置
        self.x = random.randint(0, 720)
        self.y = random.randint(0, 150)
        self.step = random.randint(2, 4)
enemies = [] # 保存的列表
for i in range(num_of_enemy):
    enemies.append(Enemy())

# 两个点之间的距离
def distance (bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a+b*b) #勾股定理

# 创建子弹类
class Bullet():
    def __init__(self):
        # 导入子弹角色文件
        self.Img = pygame.image.load('./resource/bullet.png')
        # 子弹角色位置及速度
        self.x = playerX +16
        self.y = playerY -10
        self.step = 10
    def hit(self): # 击中敌人
        for e in enemies:
            if(distance(self.x,self.y,e.x,e.y)<40): # 射中了
                bullets.remove(self)
                e.reset()

bullets = [] # 保存现有子弹
# 定义显示敌人角色及位置移动函数
def show_enemy():
    for e in enemies:
        screen.blit(e.Img,(e.x,e.y))
        e.x += e.step
        e.y += abs(e.step/6)
        if e.x > 736 or e.x < 0:
            e.step *= -1
            e.y += 30

# 定义显示子弹角色及位置移动函数
def show_bullet():
    for b in bullets:
        screen.blit(b.Img,(b.x,b.y))
        b.hit() # 检查是否击中敌人
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)


# 定义事件响应函数
def process_event():
    global player_step,builtinboor # global将局部变量变为全局变量
    for event in pygame.event.get():
        # 游戏推出
        if event.type == pygame.QUIT:
            exit()
        # 游戏按键事件响应玩家角色移动
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_step = -5
            elif event.key == pygame.K_RIGHT:
                player_step = 5
            elif event.key == pygame.K_SPACE:
                print('发射子弹-.-.-')
                # 创建一颗子弹
                bullets.append(Bullet())
        elif event.type == pygame.KEYUP:  # 当按键抬起玩家角色不动
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_step = 0
# 定义防止玩家角色出界函数
def Prevent_out():
    global playerX,enemyX,enemyY,enemyStep
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0

# 游戏主循环
while True:
    # 设置背景及位置
    screen.blit(bgimg, (0, 0))
    # 设置玩家角色及位置
    screen.blit(playerImg,(playerX,playerY))
    # 使角色持续移动
    playerX += player_step
    # 事件响应
    process_event()
    # 防止玩家角色出界
    Prevent_out()
    show_enemy()# 设置敌人
    show_bullet()#设置子弹

    # 刷新游戏界面
    pygame.display.update()

