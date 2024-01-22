import pygame
from Scenes.BaseScene import BaseScene, setup_button
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from soundtrackmanager import SoundtrackManager
from Utils.FlameText import FlameText
from Config.definitnios import ASSETS_DIR
from dataclasses import dataclass
import os
 
@dataclass
class Credits_Text:
    path_to_frames : str
    left_side_offset : int


class CreditsScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(52, 26, 0)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        self.section_offset = 0.2*self.height
        self.interline = 0.1 * self.height
        self.top_margin = 0.1 * self.height
        self.left_margin = 0.2 * self.width
        self.init_y_offset = self.height
        self.animation_speed = 0.001*self.height
        self.start_screen_button = setup_button(self.gameStateManager, 'start', (100, 300))
        self.add_ui_element(self.start_screen_button)

        self.sections = []
        self.logo_section = [Credits_Text(os.path.join(ASSETS_DIR, "piekielna_rezolucja_gif"), 0.1 * self.width)]
        self.sections.append(self.logo_section)
        self.authors_section = []
        self.authors_title = Credits_Text(os.path.join(ASSETS_DIR, "credits", "authors", "author_title"), 0.12 * self.width)
        self.authors_section.append(self.authors_title)

        self.sections.append(self.authors_section)

        for section_idx in range(len(self.sections)):
            section = self.sections[section_idx]
            for text_idx in range(len(section)):
                text_frames = section[text_idx].path_to_frames
                left_offset = section[text_idx].left_side_offset
                self.add_ui_element(FlameText((self.left_margin + left_offset, self.top_margin + section_idx * self.section_offset + text_idx * self.interline + self.init_y_offset), text_frames))

    def update(self, mouse=pygame.mouse):
        for element in self.ui_elements:
            if isinstance(element, FlameText) or isinstance(element, PiekielnaRezolucjaLogo):
                element.pos_rect[1] -= self.animation_speed
                if (element.pos_rect[1] <= 0):
                    element.pos_rect[1] -= 2*self.animation_speed
                print(element.pos_rect)
        super().update(mouse)

    def on_entry(self, *args, **kwargs):
        SoundtrackManager.stopMusic()
        SoundtrackManager.playMusic("GameplayMusic")
        super().on_entry(*args)