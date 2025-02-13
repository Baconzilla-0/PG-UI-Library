import pygame

class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.Volume = 1

    def Play(self, File, Loop = False):
        pygame.mixer.music.load(File) 
        pygame.mixer.music.set_volume(self.Volume) 
        if Loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
