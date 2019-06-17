import pygame
from pygame.locals import *

pygame.init()

pygame.mixer.music.load("teste1.ogg")
print("Carregando Música")

pygame.mixer.music.play()
print("Tocando Música")




input("Pressione algo para sair")
sys.exit()