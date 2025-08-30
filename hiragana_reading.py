import csv
import pygame
import random
from pygame_helper import textBox

HIRAGANA_FILE = "quiz_files/hiragana_full.csv"
READING_LENGTH = 5

def hiragana_reading(jp_font_file, en_font_file,clock,screen):

    jp_font = pygame.font.Font(jp_font_file, 200)
    en_font = pygame.font.Font(en_font_file, 112)

    jp_text = textBox(
        font_file=jp_font_file,
        text='',
        text_color=(255,255,255),
    )

    en_text = textBox(
        font_file=en_font_file,
        text='',
        text_color=(255,255,255)
    )

    c_text = textBox(
        font_file=en_font_file,
        text='',
        text_color=(255,255,255)
    )

    def render_screen():
        # fill screen background
        screen.fill("black")

        screen_width, screen_height = screen.get_size()

        jp_text.render(screen)

        

        # render japanese text
        
        
        # jp_font.render(active_jp, True, jp_color)
        
        # jpRect = jp_text.get_rect()
        # jpRect.size = 
        # jpRect.center = (screen_width / 2, screen_height / 3)
        # screen.blit(jp_text, jpRect)

        # render answer text
        
        en_text.render(screen)

        # en_text = en_font.render(answer_text, True, en_color)
        # enRect = en_text.get_rect()
        # enRect.center = (screen_width / 2, 2 * screen_height / 3)
        # screen.blit(en_text, enRect)

        # render correct text
        c_text.set_text(correct_text)
        c_text.render(screen)
        # c_text = en_font.render(correct_text, True, en_color)
        # cRect = c_text.get_rect()
        # cRect.center = (screen_width / 2, 5 * screen_height / 6)
        # screen.blit(c_text, cRect)

        pygame.display.flip()

    answer_dict = {}
    hiragana_list = []
    en_letters = [i for i in range(pygame.K_a, pygame.K_z+1)]
    # csv file setup
    with open(HIRAGANA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for (a, b) in reader:
            answer_dict[a] = b
            hiragana_list.append(a)

    screen_width, screen_height = screen.get_size()
    # Initialize answer text
    answer_text = ''
    en_text.set_pos((screen_width / 2, 2 * screen_height / 3))
    # en_text.set_size(int(screen_width / (READING_LENGTH * 1.2)))
    en_text.set_text_color((255, 255, 255))
    en_text.set_text(answer_text)

    # Initialize jp text
    active_jp = ''
    answer = ''
    for i in range(READING_LENGTH):
        random_key = random.choice(hiragana_list)
        active_jp = active_jp + random_key
        answer = answer + answer_dict[random_key]

    
    jp_text.set_pos((screen_width / 2, screen_height / 3))
    jp_text.set_size(int(screen_width / (READING_LENGTH * 1.2)))
    jp_text.set_text_color((255, 255, 255))
    jp_text.set_text(active_jp)

    en_text.set_size(int(screen_width / (len(answer) * 1.2)))

    
    # active_jp.set_size(int(screen_width / (READING_LENGTH*0.7)))
    # active_jp.set_pos((screen_width / 2, title.size))

    # Initialize correct text
    correct_text = ''

    quiz_running = True

    while quiz_running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.WINDOWRESIZED:
                screen_width, screen_height = screen.get_size()
                jp_text.set_pos((screen_width / 2, screen_height / 3))
                jp_text.set_size(int(screen_width / (READING_LENGTH * 1.2)))
                en_text.set_pos((screen_width / 2, 2 * screen_height / 3))
                en_text.set_size(int(screen_width / (len(answer) * 1.2)))


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(answer_text) > 0:
                        answer_text = answer_text[:-1]
                        en_text.set_text(answer_text)
                        if answer_text != answer[:len(answer_text)]:
                            en_text.set_text_color((255,0,0))
                            c_text.set_text_color((255,0,0))
                        else:
                            en_text.set_text_color((255,255,255))
                            c_text.set_text_color((255,255,255))
                elif event.key == pygame.K_ESCAPE:
                    quiz_running = False
                elif event.key in en_letters:
                    
                    answer_text += event.unicode
                    en_text.set_text(answer_text)
                    if len(answer_text) > 0:
                        if answer_text == answer:

                            # display correct answer on screen
                            correct_text = answer
                            en_text.set_text_color((0,255,0))
                            c_text.set_text_color((0,255,0))

                            render_screen()
                            pygame.time.wait(250)

                            # pick a new set of characters to quiz

                            active_jp = ''
                            answer = ''
                            for i in range(READING_LENGTH):
                                random_key = random.choice(hiragana_list)
                                active_jp = active_jp + random_key
                                answer = answer + answer_dict[random_key]
                            jp_text.set_text_color((255, 255, 255))
                            jp_text.set_text(active_jp)
                            en_text.set_size(int(screen_width / (len(answer) * 1.2)))
                            

                            en_text.set_text_color((255,255,255))
                            c_text.set_text_color((255,255,255))
                            answer_text = ''
                            correct_text = ''
                            en_text.set_text(answer_text)

                        elif answer_text != answer[:len(answer_text)]:
                            en_text.set_text_color((255,0,0))
                            c_text.set_text_color((255,0,0))
                        else:
                            en_text.set_text_color((255,255,255))
                            c_text.set_text_color((255,255,255))

        render_screen()

        clock.tick(60)  # limits FPS to 60

    