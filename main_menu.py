import pygame
import os
from pygame_helper import textBox
from pygame_helper import textButton
from quiz_menu import quiz_menu
from hiragana_reading import hiragana_reading

JP_FONT = 'jp_fonts/NotoSansJP-VariableFont_wght.ttf'
EN_FONT = 'SourceCodePro-VariableFont_wght.ttf'

def main_menu(en_font_file, clock, screen):

    title = textBox(
        font_file=en_font_file,
        text="JP Learner",
        text_color=(255,255,255),
        size=1
    )

    screen_width, screen_height = screen.get_size()
    title.set_size(int(screen_width / (len(title.text)*0.7)))
    title.set_pos((screen_width / 2, title.size))

    quiz_button = textButton(
        font_file=en_font_file,
        text="H/K Quiz",
        bg_color=(100,100,100),
        size=80,
        text_color=(255,255,255),
        action=lambda:
            quiz_menu(
            en_font_file=en_font_file,
            clock=clock,
            screen=screen
            )
    )

    reading_button = textButton(
        font_file=en_font_file,
        text="Hiragana Reading",
        bg_color=(100,100,100),
        size=80,
        text_color=(255,255,255),
        action=lambda:
            hiragana_reading(
                jp_font_file=JP_FONT,
                en_font_file=EN_FONT,
                clock=clock,
                screen=screen
            )
    )
    reading_button.set_pos((screen_width / 2, screen_height * 2 / 3 + 80))
    reading_button.set_size(int(screen_width / (len(reading_button.text))))

    quiz_button.set_pos((screen_width / 2, screen_height * 2 / 3))
    quiz_button.set_size(int(screen_width / (len(quiz_button.text))))

    def render_screen():

        screen.fill("black")
        title.render(screen)
        quiz_button.render(screen)
        reading_button.render(screen)

        pygame.display.flip()

    menu_running = True

    while(menu_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
            
            if event.type == pygame.WINDOWRESIZED or quiz_button.click(event) or reading_button.click(event):
                screen_width, screen_height = screen.get_size()
                title.set_size(int(screen_width / (len(title.text)*0.7)))
                title.set_pos((screen_width / 2,title.size))

                quiz_button.set_pos((screen_width / 2, screen_height * 2 / 3))
                quiz_button.set_size(int(screen_width / (len(quiz_button.text))))

                reading_button.set_pos((screen_width / 2, screen_height * 2 / 3 + 80))
                reading_button.set_size(int(screen_width / (len(reading_button.text))))

            # quiz_button.click(event)
            # reading_button.click(event)
        render_screen()
        clock.tick(60)  # limits FPS to 60