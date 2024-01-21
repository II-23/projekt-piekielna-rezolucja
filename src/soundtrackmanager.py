import pygame
import os
from Config.soundtrack import MUSIC
from Config.definitnios import ASSETS_DIR

class SoundtrackManager():
    def __init__(self):
        self.currentMusic = None

    def mixerCheck(func):
        def wrapper(*args, **kwargs):
            if not pygame.mixer.get_init():
                return
            func(*args, **kwargs)
        return wrapper

    def getPath(self, fileName):
        return os.path.join(ASSETS_DIR,"soundtrack",fileName)

    @mixerCheck
    def playMusic(self, fileName, *args, **kwargs):
        musicPath = self.getPath(fileName)
        try:
            pygame.mixer.music.load(musicPath)
            pygame.mixer.music.play(*args, **kwargs)
            self.currentMusic = fileName
        except Exception as e:
            print(f"Wasn't able to load/play music file {fileName}: {e}")

    @mixerCheck
    def pauseMusic(self):
        try:
            pygame.mixer.music.pause()
        except Exception as e:
            print(e)

    @mixerCheck
    def unpauseMusic(self):
        try:
            pygame.mixer.music.unpause()
        except Exception as e:
            print(e)

    @mixerCheck
    def stopMusic(self, fileName):
        musicPath = self.getPath(fileName)
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload(musicPath)
            self.currentMusic = None
        except Exception as e:
            print(f"Wasn't able to stop/unload music file {fileName}: {e}")
            