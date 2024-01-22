import pygame
from Scenes.BaseScene import BaseScene, setup_button
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from soundtrackmanager import SoundtrackManager
 
class CreditsScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(128, 64, 0)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        self.logo = PiekielnaRezolucjaLogo((0, 0))
        self.start_screen_button = setup_button(self.gameStateManager, 'start', (100, 300))
        self.add_ui_element(self.logo)
        self.add_ui_element(self.start_screen_button)
    
    def on_entry(self, *args, **kwargs):
        SoundtrackManager.stopMusic()
        SoundtrackManager.playMusic("GameplayMusic")
        super().on_entry(*args)