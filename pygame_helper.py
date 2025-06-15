import pygame

class textBox:

    def __init__(self, font_file, text='', size=12, aa=True, text_color=(255,255,255), bg_color=None):
        self.text = text
        self.font_file = font_file
        self.size = size
        self.aa = aa
        self.text_color = text_color
        self.bg_color = bg_color
        self.pos = (0,0)
        

        font = pygame.font.Font(font_file, size)
        self.txtObj = font.render(text, aa, text_color, bg_color)
        self.rect = self.txtObj.get_rect()
    
    def _update(self):
        font = pygame.font.Font(self.font_file, self.size)
        self.txtObj = font.render(self.text, self.aa, self.text_color, self.bg_color)
        self.rect = self.txtObj.get_rect()
        self.rect.center = self.pos

    # public methods ===========================================================================================

    def render(self,screen):
        screen.blit(self.txtObj, self.rect)

    # setter methods ===========================================================================================
    
    def set_pos(self, pos):
        self.pos = pos
        self._update()

    def set_text_color(self, color):
        self.text_color = color
        self._update()
    
    def set_bg_color(self, color):
        self.bg_color = color
        self._update()

    def set_size(self, size):
        self.size = size
        self._update()
    
    # setter methods ===========================================================================================

    def get_rect(self):
        return self.rect
    
    def get_text(self):
        return self.text
    
    def get_pos(self):
        return self.pos