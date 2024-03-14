import pygame
from time import sleep

"""
Esse script abre e reproduz um arquivo mp3.
"""

pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)
print('Pressione CTRL+C para sair.')
sleep(1000)