#!/usr/bin/env python3
# by Yzw

## GPLv3 开放源码许可证
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame  # 加载 pygame 关键字
import sys     # 让 python 使用你的文件系统
import os      # 帮助 python 识别你的操作系统

'''
Variables
'''

worldx = 960
worldy = 720
fps   = 40  # 帧频
ani   = 4   # 动画循环
main = True
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
HWS = (119,59,101)
'''
Objects
'''
# 在这里放置 Python 类和函数

'''
Setup
'''
# 在这里放置一次性的运行代码

clock = pygame.time.Clock()
pygame.init()
world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png'))
backdropbox = world.get_rect()
'''
Main Loop
'''
# 在这里放置游戏的循环代码指令
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False


        if event.type == pygame.KEYDOWN: # 使用 Pygame 关键字来检查键盘上的按键是否已经被按下或释放
            if event.key == ord('q'): #设为q键
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    #world.blit(backdrop, backdropbox)
    world.fill(HWS)
    pygame.display.flip()
    clock.tick(fps)