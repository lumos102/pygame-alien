import pygame
class Ship():
    #初始化
    def __init__(self, screen):
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #移动标志
        self.moving_right = False
        self.moving_left = False
    #绘制
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    #飞船移动
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
