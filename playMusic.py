import pygame
import random
pygame.mixer.init()

def playMusic(start):
    pygame.mixer.music.set_volume(1.0)
    if(start): 
        pygame.mixer.music.load("shouldIStay.mp3")
    elif(not pygame.mixer.music.get_busy()):
        randTrack = random.randint(0,2)
        if randTrack == 0:
            pygame.mixer.music.load("thunderstruck.mp3")
        if randTrack == 1:
            pygame.mixer.music.load("shouldIStay.mp3")
    pygame.mixer.music.play()

def stopMusic():
    pygame.mixer.music.stop()
