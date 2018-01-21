import  pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x =    float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''向右移动外星人'''
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x


