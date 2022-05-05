#importações
import pygame
from pygame.locals import *
from sys import exit
from random import randint
from datetime import datetime

pygame.init()

#determinações de dimensões do jogo e fontes
largura = 1000
altura = 700
xplay,yplay = 435,400
xbot,ybot,vbot = 435,-100,-0.5
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Trivial')
fonte = pygame.font.SysFont("calibri",20,True,True)

#funcionamento do relogio, pega o momento inicial
tempo = 60
momentoinicial = datetime.today()

#pega as imagens que vão ser rodadas no jogo
carro_player = pygame.image.load('images/carro1n.png')
carro_bot = pygame.image.load('images/carro2n.png')
fundo = pygame.image.load('images/pista.png').convert()
fundo = pygame.transform.scale(fundo,(largura, altura))

#faz a randomização
random1 = randint(1,3)


pontos = 0
#cplayer = pygame.draw.rect(tela,(255,000,000),(xplay,yplay,50,90))

while True:
    tela.fill((0,0,0))
    
    #monta a string de fazer a mensagem de pontos
    mensagem = f"PONTOS: {pontos}"
    texto = fonte.render(mensagem,False,(0,255,0))
    
    #pega a diferença de tempo em segundos entre o momentoinicial e o momentoatual, assim subtrai do tempo total do jogo para fazer o tempo regressivo
    momentoatual = datetime.today()
    diferenca = momentoatual-momentoinicial
    hora,minuto,segundo = str(diferenca).split(":")
    temporestante = tempo - float(segundo)
    mensagemtempo = f"TEMPO: {int(temporestante)}"
    textotempo =  fonte.render(mensagemtempo,False,(0,255,0))
    
    #imprime as imagens
    tela.blit(fundo, (0,0))
    ret_play = pygame.draw.rect(tela,(255,0,0),(xplay,yplay,90,169))
    ret_bot = pygame.draw.rect(tela,(0,0,255),(xbot,ybot,90,171))
    tela.blit(carro_player,(xplay,yplay))
    tela.blit(carro_bot,(xbot,ybot))
    
    #faz o loop infinito
    for event in pygame.event.get():
        #Sai do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Faz as movimentações
        if(event.type == KEYDOWN):
                if(event.key == K_LEFT):
                    if(xplay != 225):
                        xplay -= 210
                    else:
                        pass
                
                if(event.key == K_RIGHT):
                    if(xplay != 645):
                        xplay += 210
                    else:
                        pass
    
    #gera a randomização do boot
    if(random1 == 1):
        xbot = 225
        
    if(random1 == 2):
        xbot = 435
        
    if(random1 == 3):
        xbot = 645
        
    
    #organiza o X e Y do usuario
    if(ybot == altura):
        pontos += 1
        ybot = -100
        random1 = randint(1,3)
        
    if(ret_play.colliderect(ret_bot)):
        pontos = 0
        print('bateu, perdeu tudo')
        ybot = -100
        random1 = randint(1,3)
    
    #imprime as mensagem na tela
    tela.blit(texto,(865,40))
    tela.blit(textotempo,(865,90))
    
    ybot -= vbot        
    
    pygame.display.update()