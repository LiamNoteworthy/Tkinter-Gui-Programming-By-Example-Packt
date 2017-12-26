import os

import pygame
from pygame import mixer
from casino import assets_folder


class SoundBoard:
    def __init__(self):
        pygame.init()
        self.sound_folder = assets_folder + '/sounds/'
        self.place_sound = self.load_sound('cardPlace1.wav')
        self.shuffle_sound = self.load_sound('cardShuffle.wav')
        self.chip_sound = self.load_sound('chipsStack6.wav')

    def load_sound(self, sound):
        file_location = self.sound_folder + sound
        if os.path.isfile(file_location):
            return mixer.Sound(file_location)
        else:
            raise Exception('file ' + file_location + ' could not be found')