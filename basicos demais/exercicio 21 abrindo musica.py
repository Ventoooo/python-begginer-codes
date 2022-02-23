import pygame

#incializar o pygame
pygame.init()

#inicializar o mixer do pygame
pygame.mixer.init()

#carregar a musica
pygame.mixer.music.load('/basicos demais/ex021.mp3')

#iniciar a musica
pygame.mixer.music.play()

#parar a musica
pygame.event.wait()

input()