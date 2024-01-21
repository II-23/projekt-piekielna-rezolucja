import pygame
import os
from Config.soundtrack import MUSIC, SOUNDS
from Config.definitnios import ASSETS_DIR

class SoundtrackManager():
    '''
    Większość funkcji ma bardzo intuicyjne działanie.
    Aby wszyscy korzystali z tego samego SoundtrackManager'a nie należy tworzyć obiektu klasy,
    a raczej korzystać bezpośrednio z klasy.
    Aby puścić muzykę należy:
    1. Dodać plik dźwiękowy do assets/soundrack/
    2. W pliku src/Config/soundtrack.py w słowniku MUSIC dodać utwór w postaci:
    "NazwaPrzezKtórąBędziemySięOdwoływać" : "NazwaPliku"
    3. Wykonać SoundtrackManager.playMusic(NazwaPrzezKtórąBędziemySięOdwoływać)
    '''

    currentMusic = None
    loadedSounds = {}

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
    def setVolume(cls, volume):
        volume /= 100
        pygame.mixer.music.set_volume(volume)

    @classmethod
    @mixerCheck
    def playMusic(cls, musicName, *args, **kwargs):
        try:
            musicPath = cls.getPath(MUSIC[musicName])
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

    @classmethod
    @mixerCheck
    def playSound(cls, SoundName):
        try:
            if SoundName not in cls.loadedSounds:
                cls.loadedSounds[SoundName] = pygame.mixer.Sound(cls.getPath(SOUNDS[SoundName]))

            cls.loadedSounds[SoundName].play()
        except Exception as e:
            print(f"Wasn't able to play/load sound file: {e}")

    @classmethod
    @mixerCheck
    def stopSound(cls, SoundName):
        try:
            if SoundName not in cls.loadedSounds:
                print(f"{SoundName} isn't loaded yet")
            cls.loadedSounds[SoundName].stop()
        except Exception as e:
            print(f"Wasn't able to stop/unload music file: {e}")
