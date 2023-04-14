from pygame import mouse
from pygame.constants import K_ESCAPE, KEYDOWN
from button import Button
from screen import Display
import pygame, sys, os
from settings import Settings
from screen import Display
from button import Button

class Calculator:
    """ Class to manage the main class of calculator """
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings(self)
        self.screen_size = (self.settings.width, self.settings.height)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Calculator")
        # Classes instances
        self.display = Display(self)
        self.button0 = self.button_0()
        self.button1 = self.button_1()
        self.buttonDot = self.button_dot()
        self.button2 = self.button_2()
        self.button3 = self.button_3()
        self.button4 = self.button_4()
        self.button5 = self.button_5()
        self.button6 = self.button_6()
        self.button7 = self.button_7()
        self.button8 = self.button_8()
        self.button9 = self.button_9()
        self.buttonDel = self.button_del()
        self.buttonEquals = self.button_equals()
        self.buttonPlus = self.button_plus()
        self.buttonMinus = self.button_minus()
        self.buttonDivide = self.button_div()
        self.buttonMulti = self.button_multi()
        self.buttonNegate = self.button_negate()
        self.buttonClear = self.button_clear()
        self.buttonPercent = self.button_percent()

    
    def run_prog(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_1:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.button0.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("0")
                        elif self.button1.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("1")
                        elif self.button2.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("2")
                        elif self.button3.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("3")
                        elif self.button4.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("4")
                        elif self.button5.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("5")
                        elif self.button6.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("6")
                        elif self.button7.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("7")
                        elif self.button8.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("8")
                        elif self.button9.rect.collidepoint(mouse_pos):
                            self.display.var.add_str("9")
                        elif self.buttonDot.rect.collidepoint(mouse_pos):
                            self.display.var.add_str(".")
                        elif self.buttonDel.rect.collidepoint(mouse_pos):
                            self.display.var.del_str()
                        elif self.buttonPlus.rect.collidepoint(mouse_pos):
                            if self.display.var.operator:
                                self.display.var.continuos('+')
                            else:
                                self.display.var.op("+")
                                self.display.var.move()
                        elif self.buttonMinus.rect.collidepoint(mouse_pos):
                            if self.display.var.operator:
                                self.display.var.continuos('-')
                            else:
                                self.display.var.op("-")
                                self.display.var.move()
                        elif self.buttonMulti.rect.collidepoint(mouse_pos):
                            if self.display.var.operator:
                                self.display.var.continuos('*')
                            else:
                                self.display.var.op("*")
                                self.display.var.move()
                        elif self.buttonDivide.rect.collidepoint(mouse_pos):
                            if self.display.var.operator:
                                self.display.var.continuos('/')
                            else:
                                self.display.var.op("/")
                                self.display.var.move()
                        elif self.buttonNegate.rect.collidepoint(mouse_pos):
                            self.display.var.negate()
                        elif self.buttonEquals.rect.collidepoint(mouse_pos):
                            self.display.var.logic()
                        elif self.buttonClear.rect.collidepoint(mouse_pos):
                            self.display.var.reset()
                        elif self.buttonPercent.rect.collidepoint(mouse_pos):
                            self.display.var.sqr_root()
                    except:
                        pass

            self.screen.fill(self.settings.bg_color)
            self.display.render()
            self.display.update_screen()
            self._draw_hover_button()
            pygame.display.update()
    

    
    def str_to_float(self, num):
        return float(num)
    
    def _draw_hover_button(self):
            self.buttonDot.draw_button()
            self.buttonDot.check_hover()
            self.button0.draw_button()
            self.button0.check_hover()
            self.button1.draw_button()
            self.button1.check_hover()
            self.button2.draw_button()
            self.button2.check_hover()
            self.button3.draw_button()
            self.button3.check_hover()
            self.button4.draw_button()
            self.button4.check_hover()
            self.button5.draw_button()
            self.button5.check_hover()
            self.button6.draw_button()
            self.button6.check_hover()
            self.button7.draw_button()
            self.button7.check_hover()
            self.button8.draw_button()
            self.button8.check_hover()
            self.button9.draw_button()
            self.button9.check_hover()
            self.buttonDel.draw_button()
            self.buttonDel.check_hover()
            self.buttonEquals.draw_button()
            self.buttonEquals.check_hover()
            self.buttonPlus.draw_button()
            self.buttonPlus.check_hover()
            self.buttonMinus.draw_button()
            self.buttonMinus.check_hover()
            self.buttonDivide.draw_button()
            self.buttonDivide.check_hover()
            self.buttonMulti.draw_button()
            self.buttonMulti.check_hover()
            self.buttonNegate.draw_button()
            self.buttonNegate.check_hover()
            self.buttonClear.draw_button()
            self.buttonClear.check_hover()
            self.buttonPercent.draw_button()
            self.buttonPercent.check_hover()
        

# Classes Instances
    def button_0(self):
        self.button_x = self.settings.width-290
        self.button_y = self.settings.height - 50
        return Button(self, "0", self.button_x, self.button_y)
    def button_dot(self):
        x = self.button_x+80
        y = self.button_y
        return Button(self, ".", x, y)
    def button_1(self):
        x = self.button_x
        y = self.button_y-80
        return Button(self, "1", x, y)
    def button_2(self):
        x = self.button_x+80
        y = self.button_y-80
        return Button(self, "2", x, y)
    def button_3(self):
        x = self.button_x+160
        y = self.button_y-80
        return Button(self,"3", x, y)
    def button_4(self):
        x = self.button_x
        y = self.button_y-160
        return Button(self, "4", x, y)
    def button_5(self):
        x = self.button_x+80
        y = self.button_y-160
        return Button(self, "5", x, y)
    def button_6(self):
        x = self.button_x+160
        y = self.button_y-160
        return Button(self, "6", x, y)
    def button_7(self):
        x = self.button_x
        y = self.button_y-240
        return Button(self, "7", x, y)
    def button_8(self):
        x = self.button_x+80
        y = self.button_y-240
        return Button(self, "8", x, y)
    def button_9(self):
        x = self.button_x+160
        y = self.button_y-240
        return Button(self, "9", x, y)
    def button_del(self):
        x = self.button_x+160
        y = self.button_y
        return Button(self, 'del', x, y)
    def button_equals(self):
        x = self.button_x+240
        y = self.button_y
        return Button(self, '=', x, y)
    def button_plus(self):
        x = self.button_x+240
        y = self.button_y-80
        return Button(self, "+", x, y)
    def button_minus(self):
        x = self.button_x+240
        y = self.button_y-160
        return Button(self, '-', x, y)
    def button_div(self):
        x = self.button_x+320-80
        y = self.button_y-320
        return Button(self, "/", x, y)
    def button_multi(self):
        x = self.button_x+320-80
        y = self.button_y-240
        return Button(self, 'x', x, y)
    def button_negate(self):
        x = self.button_x+80
        y = self.button_y-320
        return Button(self,"+/-", x, y)
    def button_clear(self):
        x = self.button_x
        y = self.button_y-320
        return Button(self, "C", x, y)
    def button_percent(self):
        x = self.button_x+160
        y = self.button_y-320
        return Button(self, "√", x, y)


