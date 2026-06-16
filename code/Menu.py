import turtle

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:

    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/montain-menu.png')
        self.react = self.surf.get_rect(left=0, top=0)


    def run(self):
        pygame.mixer.music.load('./assets/sound.menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.react)
            self.menu_text(text_size:50, text:"Mountain", COLOR_ORANGE, text_center_pos:((WIN_WIDTH / 2), 70))
            self.menu_text(text_size:50, text: "Shooter", COLOR_ORANGE, text_center_pos:((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size:20, MENU_OPTION[i], COLOR_WHITE, text_center_pos:((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

    def menu_text(self,       text_size: int, text: str, text_color: tuple, text_center_pos tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True).convert_alpha()
        text_rect: Rect = text_surf.get.rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


