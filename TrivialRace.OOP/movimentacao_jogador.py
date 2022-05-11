import pygame
from pygame.locals import *

class MovimentacaoJogador():

    pygame.init()

    def __init__(self):
        self.xplay = 380
        self.yplay = -100
        self.fazmovimentacao()
    
    def fazmovimentacao(self):
         #faz o loop infinito
        for event in pygame.event.get():
            #Sai do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Faz as movimentações
            if(event.type == KEYDOWN):
                    if(event.key == K_LEFT):
                        if(self.xplay != 200):
                            self.xplay -= 180
                        else:
                            pass
                    
                    if(event.key == K_RIGHT):
                        if(self.xplay != 560):
                            self.xplay += 180
                        else:
                            pass
