class Variables:

    def __init__(self, calcu) -> None:
        self.screen = calcu.screen
        self.screen_rect = self.screen.get_rect()
        self.switch = False
        self.one = ""
        self.operator = ""
        self.two = ""
    
    def add_str(self, str1):
        self.one = self.one + str1
    def del_str(self):
        self.one = self.one[:-1]
    def op(self,operate):
        self.operator = operate
    def move(self):
        self.two = self.one
        self.one = ""
    def logic(self):
        if self.operator == '+':
            self.one = str(float(self.two) + float(self.one))
        elif self.operator == '-':
            self.one = str(float(self.two) - float(self.one))
        elif self.operator == '*':
            self.one = str(float(self.two) * float(self.one))
        elif self.operator == '/':
            self.one = str(float(self.two) / float(self.two))
    def continuos(self, operator):
        self.logic()
        self.move()
        self.operator = operator
    def reset(self):
        self.one = ''
        self.operator = ''
        self.two = ''
    def negate(self):
        if self.one:
            self.one = str(float(self.one)*-1)
        else:
            pass
    def sqr_root(self):
        if self.one:
            self.one = str(float(self.one)**0.5)
        else:
            pass