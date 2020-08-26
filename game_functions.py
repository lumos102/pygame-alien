import sys
import pygame

#监听事件
def check_events(ship):
        for event in pygame.event.get():
            #退出
            if event.type == pygame.QUIT:
                sys.exit()
            #按键按下
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            #按键抬起
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

#更新屏幕
def update_screen(screen, ship,bg_color):
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        #绘制飞船
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
