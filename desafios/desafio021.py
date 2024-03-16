import pygame
from time import sleep

"""
Esse script abre e reproduz um arquivo mp3.
"""

pygame.init()
musica = pygame.mixer.Sound('song.mp3')
pygame.mixer.Sound.play(musica)
duracao_da_musica = int(pygame.mixer.Sound.get_length(musica)) * 1000
print('Tocando música selecionada no código.')
print('Pressione CTRL+C para sair.')
sleep(duracao_da_musica)
