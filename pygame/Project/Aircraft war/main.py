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
# 初始化玩家角色位置及速度
playerX = 368
playerY = 500
player_step = 0
# 导入敌人角色文件
enemyImg = pygame.image.load('./resource/enemy.png')
# 初始化敌人角色位置及速度
enemyX = 0
enemyY = 0
enemyStep = 4
# 定义敌人角色及位置函数
def show_enemy():
    global enemyX,enemyY
    screen.blit(enemyImg,(enemyX,enemyY))
    enemyX += enemyStep
    enemyY += abs(enemyStep/6)
# 定义事件响应函数
def process_event():
    global player_step
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
        elif event.type == pygame.KEYUP: # 当按键抬起玩家角色不动
            player_step = 0
# 定义防止玩家角色出界函数
def Prevent_out():
    global playerX,enemyX,enemyStep
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0
    elif enemyX > 736 or enemyX < 0:
        enemyStep = -enemyStep

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
    show_enemy()
    # 刷新游戏界面
    pygame.display.update()

