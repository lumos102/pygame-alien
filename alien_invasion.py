import sys
import pygame
from ship import Ship
import game_functions

#程序入口
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        # 监视事件
        game_functions.check_events(ship)
        #移动飞船
        ship.update()
        #更新屏幕
        game_functions.update_screen(screen,ship,(230,230,230))

run_game()