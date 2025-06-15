import csv
import pygame
import random

def quiz(filename,correct_needed, jp_font_file, en_font_file,clock,screen):

    jp_font = pygame.font.Font(jp_font_file, 200)
    en_font = pygame.font.Font(en_font_file, 112)

    def render_screen():
        # fill screen background
        screen.fill("black")

        screen_width, screen_height = screen.get_size()

        # render japanese text
        jp_text = jp_font.render(active_jp, True, jp_color)
        jpRect = jp_text.get_rect()
        jpRect.center = (screen_width / 2, screen_height / 3)
        screen.blit(jp_text, jpRect)

        # render answer text
        en_text = en_font.render(answer_text, True, en_color)
        enRect = en_text.get_rect()
        enRect.center = (screen_width / 2, 2 * screen_height / 3)
        screen.blit(en_text, enRect)

        # render correct text
        c_text = en_font.render(correct_text, True, en_color)
        cRect = c_text.get_rect()
        cRect.center = (screen_width / 2, 5 * screen_height / 6)
        screen.blit(c_text, cRect)

        pygame.display.flip()


    to_quiz = []
    answer_dict = {}
    correct_dict = {}
    en_letters = [i for i in range(pygame.K_a, pygame.K_z+1)]
    # csv file setup
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for (a, b) in reader:
            answer_dict[a] = b
            correct_dict[a] = 0
            to_quiz.append(a)

    # Initialize answer text
    answer_text = ''
    en_color = (255, 255, 255)

    # Initialize jp text
    active_jp = random.choice(to_quiz)
    jp_color = (255, 255, 255)

    # Initialize correct text
    correct_text = ''

    quiz_running = True
    a_state = 0

    while quiz_running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if len(to_quiz) == 0:
                    print("Congratulations on successfully quizzing " + str(len(answer_dict)) + " items!")
                quiz_running = False

            if event.type == pygame.KEYDOWN:
                if a_state == 0:
                    if event.key == pygame.K_BACKSPACE:
                        if len(answer_text) > 0:
                            answer_text = answer_text[:-1]
                            if answer_text != answer_dict[active_jp][:len(answer_text)]:
                                en_color = (255, 0, 0)
                            else:
                                en_color = (255, 255, 255)
                    elif event.key == pygame.K_ESCAPE:
                        quiz_running = False
                    elif event.key in en_letters:
                        answer_text += event.unicode
                        if len(answer_text) > 0:
                            if answer_text == answer_dict[active_jp]:

                                # display correct answer on screen
                                correct_text = answer_dict[active_jp]
                                en_color = (0, 255, 0)
                                correct_dict[active_jp] += 1

                                render_screen()
                                pygame.time.wait(250)

                                # pick a new letter to quiz
                                new_active = random.choice(to_quiz)
                                if len(to_quiz) > 1:
                                    while new_active == active_jp:
                                        new_active = random.choice(to_quiz)
                                active_jp = new_active
                                en_color = (255, 255, 255)
                                answer_text = ''
                                correct_text = ''
                                a_state = 0

                                if correct_dict[active_jp] == correct_needed:
                                    to_quiz.remove(active_jp)
                                    if len(to_quiz) == 0:
                                        active_jp = ''
                                        answer_text = ''
                                        correct_text = 'Press Enter to restart'
                                        a_state = 1

                            elif answer_text != answer_dict[active_jp][:len(answer_text)]:
                                en_color = (255, 0, 0)
                            else:
                                en_color = (255, 255, 255)
                elif a_state == 1:
                    if event.key == pygame.K_RETURN:
                        for key in answer_dict.keys():
                            to_quiz.append(key)
                            correct_dict[key] = 0
                        active_jp = random.choice(to_quiz)
                        a_state = 0
                        correct_text = ''
                        en_color = (255, 255, 255)
                    elif event.key == pygame.K_ESCAPE:
                        quiz_running = False
            elif event.type == pygame.WINDOWRESIZED:
                print(screen.get_size())

        render_screen()

        clock.tick(60)  # limits FPS to 60

    