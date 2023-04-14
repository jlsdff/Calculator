import pygame
from variables import Variables

class Display:
    
    def __init__(self, calcu) -> None:
        self.screen = calcu.screen
        self.screen_rect = self.screen.get_rect()
        self.var = Variables(calcu)
        # Display Properties
        self.width = 330
        self.height = 75
        self.bg_color = (52, 58, 64)
        # Display Rectangle
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.centerx, 75
        # Text
        font = 'assets\\fonts\\arial.TTF'
        self.font_color = (248, 249, 250)
        self.font = pygame.font.Font(font, 35)
        self.font2 = pygame.font.Font(font, 25)
        # var1 font
        self.font_img = self.font.render(self.var.one, True, self.font_color)
        self.font_rect = self.font_img.get_rect()
        self.font_rect.midleft = self.rect.midleft
        # var2 font
        self.font2_img = self.font2.render(self.var.two+" "+self.var.operator, True, self.font_color)
        self.font2_rect = self.font2_img.get_rect()
        self.font2_rect.top = self.rect.top


    def render(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.font_img, self.font_rect)
        self.screen.blit(self.font2_img, self.font2_rect)

    def update_screen(self):
        self.font_img = self.font.render(self.var.one, True, self.font_color)
        self.font_rect = self.font_img.get_rect()
        self.font_rect.midleft = self.rect.midleft
        # font2
        self.font2_img = self.font2.render(self.var.two+" "+self.var.operator, True, self.font_color)
        self.font2_rect = self.font2_img.get_rect()
        self.font2_rect.top = self.rect.top
        