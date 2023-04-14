import pygame.font

class Font:

    def __init__(self, calcu, num) -> None:
        self.screen = calcu.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (119, 73, 54)
        self.num = pygame.font.SysFont(None, 48)

    def render(self):
        pass

    def update_screen(self):
        pass