import pygame
import os
from Config.soundtrack import MUSIC
from Config.definitnios import ASSETS_DIR

class SoundtrackManager():
    '''
    Większość funkcji ma bardzo intuicyjne działanie.
    Aby wszyscy korzystali z tego samego SoundtrackManager'a nie należy tworzyć obiektu klasy,
    a raczej korzystać bezpośrednio z klasy.
    Aby puścić plik dźwiękowy należy:
    1. Dodać plik dźwiękowy do assets/soundrack/
    2. W pliku src/Config/soundtrack.py w słowniku MUSIC dodać utwór w postaci:
    "NazwaPrzezKtórąBędziemySięOdwoływać" : "NazwaPliku"
    3. Wykonać SoundtrackManager.playMusic(NazwaPrzezKtórąBędziemySięOdwoływać)
    '''

    currentMusic = None

    def mixerCheck(func):
        def wrapper(cls, *args, **kwargs):
            if not pygame.mixer.get_init():
                return
            func(cls, *args, **kwargs)
        return wrapper 

    @classmethod
    def getPath(cls, fileName):
        return os.path.join(ASSETS_DIR,"soundtrack",fileName)

    @classmethod
    @mixerCheck
    def playMusic(cls, musicName, *args, **kwargs):
        musicPath = cls.getPath(MUSIC[musicName])
        try:
            pygame.mixer.music.load(musicPath)
            pygame.mixer.music.play(*args, **kwargs)
            cls.currentMusic = musicName
        except Exception as e:
            print(f"Wasn't able to load/play music file {musicName}: {e}")

    @classmethod
    @mixerCheck
    def pauseMusic(cls):
        try:
            pygame.mixer.music.pause()
        except Exception as e:
            print(e)

    @classmethod
    @mixerCheck
    def unpauseMusic(cls):
        try:
            pygame.mixer.music.unpause()
        except Exception as e:
            print(e)

    @classmethod
    @mixerCheck
    def stopMusic(cls):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            cls.currentMusic = None
        except Exception as e:
            print(f"Wasn't able to stop/unload music file: {e}")
            