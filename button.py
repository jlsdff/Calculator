import pygame.font

class Button:

    def __init__(self, calcu, num, x, y, width=75, height=75, fontsize=40) -> None:
        # Screen Access and attributes
        self.screen = calcu.screen
        self.screen_rect = self.screen.get_rect()
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.font_color = (248, 249, 250)
        self.button_color = (52, 58, 64)
        self.num = str(num)
        self.x = x
        self.y = y
        # Font
        font = 'assets\\fonts\\arial.TTF'
        self.font = pygame.font.Font(font, self.fontsize)
        # Button Rectangle
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.x, self.y
        self.prep_msg()
    
    def prep_msg(self):
        self.font_img = self.font.render(self.num, True, self.font_color)
        self.font_rect = self.font_img.get_rect()
        self.font_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.font_img, self.font_rect)
    
    def check_hover(self):
        highlight = self._check_hover()
        self._button_highlight(highlight)
    
    def _check_hover(self):
        highlight = False
        mouse_pos = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse_pos)
        if hover:
            highlight = True
        else:
            highlight = False
        return highlight
    
    def _button_highlight(self, highlight):
        
        if highlight:
            self.button_color = (73, 80, 87)
        else:
            self.button_color = (52, 58, 64)
        
