import pygame
from Scenes.BaseScene import BaseScene, setup_button
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from soundtrackmanager import SoundtrackManager
from Utils.FlameText import FlameText
from Utils.Image import Image
from Config.definitnios import ASSETS_DIR
from dataclasses import dataclass
from math import ceil
import time
import os
 
@dataclass
class Credits_Text:
    path_to_frames : str
    left_side_offset : int

@dataclass
class Credits_Image:
    path_to_image : str
    left_side_offset : int
    image_size : tuple[int, int]


class CreditsScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(52, 26, 0)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        self.section_offset = 0.2*self.height
        self.interline = 0.2 * self.height
        self.top_margin = 0.1 * self.height
        self.left_margin = 0.05 * self.width
        self.init_y_offset = 0.6*self.height
        self.animation_speed = 0.001*self.height


    def update(self, mouse=pygame.mouse):
        self.cnt += 1
        if (self.cnt % 2 == 0):
            for element in self.ui_elements:
                if isinstance(element, FlameText) or isinstance(element, Image):
                    element.pos_rect[1] -= self.animation_speed
                    if (element.pos_rect[1] <= 0):
                        element.pos_rect[1] -= 2*self.animation_speed
        super().update(mouse)

    def on_entry(self, *args, **kwargs):
        SoundtrackManager.stopMusic()
        SoundtrackManager.playMusic("CreditsMusic")
        self.ui_elements = []
        self.start_screen_button = setup_button(self.gameStateManager, 'start', (-0.1*self.width, 0.9*self.height))
        self.add_ui_element(self.start_screen_button)
        self.cnt = 0
        self.sections = []
        credits_dir = os.path.join(ASSETS_DIR, "credits")
        authors_dir = os.path.join(credits_dir, "authors")
        self.logo_section = [Credits_Text(os.path.join(credits_dir, "game_title"), 0.0 * self.width)]
        self.sections.append(self.logo_section)
        self.authors_section = []
        self.authors_title = Credits_Text(os.path.join(authors_dir, "author_title"), 0.05 * self.width)
        self.authors_section.append(self.authors_title)
        self.igor_hanczaruk = Credits_Text(os.path.join(authors_dir, "igorhanczaruk"), 0.18 * self.width)
        self.authors_section.append(self.igor_hanczaruk)
        self.adam_dziwiszek = Credits_Text(os.path.join(authors_dir, "adamdziwiszek"), 0.18 * self.width)
        self.authors_section.append(self.adam_dziwiszek)
        self.krzysztofolejnik = Credits_Text(os.path.join(authors_dir, "krzysztofolejnik"), 0.13 * self.width)
        self.authors_section.append(self.krzysztofolejnik)
        self.mateuszkatafiasz = Credits_Text(os.path.join(authors_dir, "mateuszkatafiasz"), 0.12 * self.width)
        self.authors_section.append(self.mateuszkatafiasz)
        self.olaponikowska = Credits_Text(os.path.join(authors_dir, "olaponikowska"), 0.18 * self.width)
        self.authors_section.append(self.olaponikowska)
        self.michalszwejda = Credits_Text(os.path.join(authors_dir, "michalszwejda"), 0.18 * self.width)
        self.authors_section.append(self.michalszwejda)
        self.justynaadamczyk = Credits_Text(os.path.join(authors_dir, "justynaadamczyk"), 0.13 * self.width)
        self.authors_section.append(self.justynaadamczyk)
        self.dominikagwarda = Credits_Text(os.path.join(authors_dir, "dominikagwarda"), 0.14 * self.width)
        self.authors_section.append(self.dominikagwarda)


        self.sections.append(self.authors_section)

        self.soundtrack_section = []
        soundtrack_authors_dir = os.path.join(credits_dir, "soundtrack")

        self.introduction = Credits_Text(os.path.join(soundtrack_authors_dir, "introduction"), 0.09 * self.width)
        self.soundtrack_section.append(self.introduction)
        self.ost_name_en = Credits_Text(os.path.join(soundtrack_authors_dir, "ost_name_en"), 0.02 * self.width)
        self.soundtrack_section.append(self.ost_name_en)
        self.ost_name_pl = Credits_Text(os.path.join(soundtrack_authors_dir, "ost_name_pl"), 0.03 * self.width)
        self.soundtrack_section.append(self.ost_name_pl)
        self.zostalstworzony = Credits_Text(os.path.join(soundtrack_authors_dir, "zostalstworzony"), 0.12 * self.width)
        self.soundtrack_section.append(self.zostalstworzony)
        self.najwiekszy = Credits_Text(os.path.join(soundtrack_authors_dir, "najwiekszy"), 0.29 * self.width)
        self.soundtrack_section.append(self.najwiekszy)
        self.polskizespol = Credits_Text(os.path.join(soundtrack_authors_dir, "polskizespol"), 0.21 * self.width)
        self.soundtrack_section.append(self.polskizespol)
        self.upamietniajacy = Credits_Text(os.path.join(soundtrack_authors_dir, "upamietniajacy"), 0.16 * self.width)
        self.soundtrack_section.append(self.upamietniajacy)
        self.najbardziej_znany = Credits_Text(os.path.join(soundtrack_authors_dir, "najbardziej_znany"), 0.12 * self.width)
        self.soundtrack_section.append(self.najbardziej_znany)
        self.parkwodny = Credits_Text(os.path.join(soundtrack_authors_dir, "parkwodny"), 0.01 * self.width)
        self.soundtrack_section.append(self.parkwodny)
        self.highdoosh = Credits_Text(os.path.join(soundtrack_authors_dir, "highdoosh"), 0.15 * self.width)
        self.soundtrack_section.append(self.highdoosh)
        self.wskladzie = Credits_Text(os.path.join(soundtrack_authors_dir, "wskladzie"), 0.25 * self.width)
        self.soundtrack_section.append(self.wskladzie)
        self.maks = Credits_Text(os.path.join(soundtrack_authors_dir, "maks"), 0.21 * self.width)
        self.soundtrack_section.append(self.maks)
        self.pluzin = Credits_Text(os.path.join(soundtrack_authors_dir, "pluzin"),0.25 * self.width)
        self.soundtrack_section.append(self.pluzin)
        self.matpil = Credits_Text(os.path.join(soundtrack_authors_dir, "matpil"), 0.25 * self.width)
        self.soundtrack_section.append(self.matpil)
        self.tymon = Credits_Text(os.path.join(soundtrack_authors_dir, "tymon"), 0.22 * self.width)
        self.soundtrack_section.append(self.tymon)
        self.magda = Credits_Text(os.path.join(soundtrack_authors_dir, "magda"), 0.27* self.width)
        self.soundtrack_section.append(self.magda)

        self.sections.append(self.soundtrack_section)
        text_cnt = 0

        guest_starred_dir = os.path.join(credits_dir, "guests")
        self.guest_starred_section = []

        self.guest_starred_introduction = Credits_Text(os.path.join(guest_starred_dir, "guests_introduction"), 0.10 * self.width)
        self.guest_starred_section.append(self.guest_starred_introduction)
        self.jma = Credits_Text(os.path.join(guest_starred_dir, "JMa"), 0.17 * self.width)
        self.guest_starred_section.append(self.jma)
        self.jmi = Credits_Text(os.path.join(guest_starred_dir, "JMi"), 0.20 * self.width)
        self.guest_starred_section.append(self.jmi)
        self.jmi2 = Credits_Text(os.path.join(guest_starred_dir, "JMi2"), 0.20 * self.width)
        self.guest_starred_section.append(self.jmi2)
        self.jmiimg = Credits_Image(os.path.join(ASSETS_DIR, "jmi.png"), 0.15 * self.width, (0.6 * self.width, 0.6*self.height))
        self.guest_starred_section.append(self.jmiimg)

        self.sections.append(self.guest_starred_section)

        self.respects_section = []
        respects_dir = os.path.join(credits_dir, "respects")

        self.respects = Credits_Text(respects_dir, 0 * self.width)
        self.respects_section.append(self.respects)
        self.studentdebil = Credits_Image(os.path.join(ASSETS_DIR, "studentdebil.jpg"), 0.15 * self.width, (0.6 * self.width, 0.6*self.height))
        self.respects_section.append(self.studentdebil)

        self.sections.append(self.respects_section)

        for section_idx in range(len(self.sections)):
            section = self.sections[section_idx]
            for text_idx in range(len(section)):
                if (isinstance(section[text_idx], Credits_Text)):
                    text_cnt += 1
                    text_frames = section[text_idx].path_to_frames
                    left_offset = section[text_idx].left_side_offset
                    self.add_ui_element(FlameText((self.left_margin + left_offset, self.top_margin + section_idx * self.section_offset + text_cnt * self.interline + self.init_y_offset), text_frames))
                elif isinstance(section[text_idx], Credits_Image):
                    img_path = section[text_idx].path_to_image
                    left_offset = section[text_idx].left_side_offset
                    img_size = section[text_idx].image_size
                    delta_cnt = ceil(img_size[1]/self.interline)
                    text_cnt += 1 + (delta_cnt//3)
                    img = Image((self.left_margin + left_offset, self.top_margin + section_idx * self.section_offset + text_cnt * self.interline + self.init_y_offset), img_size, img_path)
                    self.add_ui_element(img)
                    text_cnt += delta_cnt
        super().on_entry(*args)