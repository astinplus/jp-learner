# Example file showing a basic pygame "game loop"
import pygame
import csv
import random
from quiz import quiz
from menu import menu


QUIZ_CSV = "quiz_files/hiragana_vowels.csv"
JP_FONT = 'jp_fonts/NotoSansJP-VariableFont_wght.ttf'
EN_FONT = 'SourceCodePro-VariableFont_wght.ttf'
CORRECT_NEEDED = 2

# pygame setup
pygame.init()
pygame.font.init()
Screen = pygame.display.set_mode((275, 515), pygame.RESIZABLE)
pygame.display.set_caption('Japanese Learner')
Clock = pygame.time.Clock()

# load fonts and colors
jp_font = pygame.font.Font(JP_FONT, 200)
jp_color = (255, 255, 255)
en_font = pygame.font.Font(EN_FONT, 112)
en_color = (255, 255, 255)
a_state = 0

running = menu(
    en_font_file=EN_FONT,
    clock=Clock,
    screen=Screen
)

while(running != -1):
    if running == 1:
        quiz(filename=QUIZ_CSV, 
             correct_needed=CORRECT_NEEDED,
             jp_font_file=JP_FONT,
             en_font_file=EN_FONT,
             clock=Clock,
             screen=Screen
        )

    running = menu(
        en_font_file=EN_FONT,
        clock=Clock,
        screen=Screen
    )


pygame.font.quit()
pygame.quit()
