import pygame
from pygame_helper import textBox

def menu(en_font_file, clock, screen):

    title = textBox(
        font_file=en_font_file,
        text="JP Learner",
        text_color=(255,255,255),
        size=1
    )

    screen_width, screen_height = screen.get_size()
    title.set_size(int(screen_width / (len(title.text)*0.7)))
    title.set_pos((screen_width / 2, screen_height / 3))

    subtitle = textBox(
        font_file=en_font_file,
        text="press enter to start",
        size=100,
        text_color=(0,255,255)
    )

    subtitle.set_pos((title.pos[0],title.pos[1]+title.size))
    subtitle.set_size(int(title.size*0.5))

    def render_screen():

        screen.fill("black")        

        subtitle.render(screen)
        title.render(screen)

        pygame.display.flip()

    menu_running = True

    while(menu_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            if event.type == pygame.WINDOWRESIZED:
                screen_width, screen_height = screen.get_size()
                title.set_size(int(screen_width / (len(title.text)*0.7)))
                title.set_pos((screen_width / 2, screen_height / 3))

                subtitle.set_pos((title.pos[0],title.pos[1]+title.size))
                subtitle.set_size(int(title.size*0.5))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return -1
                if event.key == pygame.K_RETURN:
                    return 1
        
        render_screen()
        clock.tick(60)  # limits FPS to 60