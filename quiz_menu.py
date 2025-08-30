import pygame
import os
from pygame_helper import textBox
from quiz import quiz

# Quiz Constants
QUIZ_DIR = "quiz_files/"
JP_FONT = 'jp_fonts/NotoSansJP-VariableFont_wght.ttf'
EN_FONT = 'SourceCodePro-VariableFont_wght.ttf'
CORRECT_NEEDED = 2

def quiz_menu(en_font_file, clock, screen):

    quiz_files = os.listdir("quiz_files")
    curr_quiz = 0

    title = textBox(
        font_file=en_font_file,
        text="JP Learner",
        text_color=(255,255,255),
        size=1
    )

    screen_width, screen_height = screen.get_size()
    title.set_size(int(screen_width / (len(title.text)*0.7)))
    title.set_pos((screen_width / 2, title.size))

    subtitle = textBox(
        font_file=en_font_file,
        text="press enter to start",
        size=100,
        text_color=(0,255,255)
    )

    subtitle.set_pos((title.pos[0],title.pos[1]+title.size))
    subtitle.set_size(int(title.size*0.5))

    quiz_select = textBox(
        font_file=en_font_file,
        text=quiz_files[0],
        size=80,
        text_color=(255,255,255)
    )

    quiz_select.set_pos((screen_width / 2, screen_height * 2 / 3))
    quiz_select.set_size(int(screen_width / (len(quiz_select.text))))

    def render_screen():

        screen.fill("black")        

        subtitle.render(screen)
        title.render(screen)
        quiz_select.render(screen)

        pygame.display.flip()

    menu_running = True

    while(menu_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [-1]
            
            if event.type == pygame.WINDOWRESIZED:
                screen_width, screen_height = screen.get_size()
                title.set_size(int(screen_width / (len(title.text)*0.7)))
                title.set_pos((screen_width / 2,title.size))

                subtitle.set_pos((title.pos[0],title.pos[1]+title.size))
                subtitle.set_size(int(title.size*0.5))

                quiz_select.set_pos((screen_width / 2, screen_height * 2 / 3))
                quiz_select.set_size(int(screen_width / (len(quiz_select.text))))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return [-1]
                if event.key == pygame.K_RETURN:
                    # return [1, quiz_files[curr_quiz]]
                    quiz(filename=QUIZ_DIR + quiz_files[curr_quiz], 
                        correct_needed=CORRECT_NEEDED,
                        jp_font_file=JP_FONT,
                        en_font_file=EN_FONT,
                        clock=clock,
                        screen=screen
                    )
                if event.key == pygame.K_RIGHT:
                    
                    if curr_quiz == len(quiz_files) - 1:
                        curr_quiz = 0
                    else:
                        curr_quiz += 1

                    quiz_select.set_text(quiz_files[curr_quiz])
                    quiz_select.set_size(int(screen_width / (len(quiz_select.text))))
                if event.key == pygame.K_LEFT:

                    if curr_quiz == 0:
                        curr_quiz = len(quiz_files) - 1
                    else:
                        curr_quiz -= 1

                    quiz_select.set_text(quiz_files[curr_quiz])
                    quiz_select.set_size(int(screen_width / (len(quiz_select.text))))
        
        render_screen()
        clock.tick(60)  # limits FPS to 60