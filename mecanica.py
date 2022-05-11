#importações
import pygame
import imagens
from pygame.locals import *
from sys import exit
from random import randint
from datetime import datetime

def game():

    pygame.init()

    #determinações de dimensões do jogo e fontes
    largura = 800
    altura = 650
    xplay,yplay = 380,400
    xbot,ybot,vbot = 380,-100,-0.5
    xmoeda,ymoeda,vmoeda = 380,-100,-0.5
    xrelogio,yrelogio,vrelogio = 380,-100,-0.5
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Trivial Race')
    fonte = pygame.font.SysFont("calibri",20,True,True)
    fontederrota = pygame.font.SysFont("calibri",35,True,True)

    #funcionamento do relogio, pega o momento inicial
    tempo = 30
    momentoinicial = datetime.today()
    relogioscoletados = 0

    #pega as imagens que vão ser rodadas no jogo
    carro_player = pygame.image.load('images/carro_player.png')
    carro_bot = pygame.image.load('images/carro1.png')
    moeda = pygame.image.load('images/moeda.png')
    moeda = pygame.transform.scale(moeda,(40,40))
    relogio = pygame.image.load('images/relogio.png')
    relogio = pygame.transform.scale(relogio,(40,40))

    fundo = pygame.image.load('images/pista.png').convert()
    fundo = pygame.transform.scale(fundo,(largura, altura))

    #faz as randomizações
    random1 = randint(1,3)
    random_moeda = randint(1,3)
    random_relogio = randint(1,3)

    pontos = 0
    rodada = 0
    #cplayer = pygame.draw.rect(tela,(255,000,000),(xplay,yplay,50,90))

    perdeu = False
    while perdeu == False:
        tela.fill((0,0,0))

        #LÓGICA PARA INCREMENTAR DIFICULDADE
        blocosdenivel = rodada//5 #pelo que estou implementando aqui, a cada 5 rodadas o jogo ficará mais rápido
        for i in range (blocosdenivel):
            nivel = -0.5 - i/10
            vbot = nivel
            vmoeda = nivel
            vrelogio = nivel

        #print(ybot)
        #monta a string de fazer a mensagem de pontos
        mensagem = f"PONTOS: {pontos}"
        mensagemrodada = f"RODADA: {rodada}"
        texto = fonte.render(mensagem,False,(0,255,0))
        textorodada = fonte.render(mensagemrodada,False,(0,255,0))

        #pega a diferença de tempo em segundos entre o momentoinicial e o momentoatual, assim subtrai do tempo total do jogo para fazer o tempo regressivo
        momentoatual = datetime.today()
        diferenca = momentoatual-momentoinicial
        hora,minuto,segundo = str(diferenca).split(":")
        temporestantereal = tempo - float(segundo)
        temporestante = int(temporestantereal) + relogioscoletados * 1
        mensagemtempo = f"TEMPO: {temporestante}"
        textotempo =  fonte.render(mensagemtempo,False,(0,255,0))
        #print(temporestante)

        #imprime as imagens e formas
        ret_bot = pygame.draw.rect(tela,(0,0,255),(xbot,ybot,63,91))
        ret_play = pygame.draw.rect(tela,(255,0,0),(xplay,yplay,58,93))
        ret_moeda = pygame.draw.rect(tela,(0,255,255),(xmoeda,ymoeda,40,40))
        ret_relogio = pygame.draw.rect(tela,(255,0,255),(xrelogio,yrelogio,40,40))
        tela.blit(fundo, (0,0))
        tela.blit(relogio,(xrelogio,yrelogio))
        tela.blit(moeda,(xmoeda,ymoeda))
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
                        if(xplay != 200):
                            xplay -= 180
                        else:
                            pass

                    if(event.key == K_RIGHT):
                        if(xplay != 560):
                            xplay += 180
                        else:
                            pass

        #gera a randomização do boot
        if(random1 == 1):
            xbot = 200

        if(random1 == 2):
            xbot = 380

        if(random1 == 3):
            xbot = 560

        #gera a randomização da moeda
        if(random_moeda == 1):
            xmoeda = 200

        if(random_moeda == 2):
            xmoeda = 380

        if(random_moeda == 3):
            xmoeda = 560

        #gera a randomização do relogio
        if(random_relogio == 1):
            xrelogio = 200

        if(random_relogio == 2):
            xrelogio = 380

        if(random_relogio == 3):
            xrelogio = 560

        #organiza o X e Y do bot
        if(ybot >= altura):
            rodada += 1
            ybot = -100
            random1 = randint(1,3)

        if(ret_play.colliderect(ret_bot)):
            ##AQUI TEM QUE PUXAR O GAME OVER TMJ!!!!!!!!!!!!!!!!
            tela.blit(imagens.imagem_pista, (0,0))
            tela.blit(imagens.imagem_veu, (0,0))
            #tela.fill((0,0,0))
            fonte = pygame.font.SysFont("calibri",80,True,True)
            texto8 = 'TRIVIAL RACE'
            textoinicio = fonte.render(texto8,False,(255,0,0))
            mensagemderrota = 'SUA PARTICIPAÇÃO NO JOGO FOI TRIVIAL'
            textoderrota = fontederrota.render(mensagemderrota,False,(255,0,0))
            tela.blit(textoderrota,(75,200))
            texto1 = fontederrota.render(mensagem,False,(255,0,0))
            textorodada = fontederrota.render(mensagemrodada,False,(255,0,0))
            mensagemrodada = f'{textorodada}'
            resumo = 'RESUMO DO JOGO:'
            resu = fontederrota.render(resumo,False,(255,0,0))
            texto3 = f'TEMPO QUE RESTAVA: {temporestante}Seg'
            mensagem_tempo_over = fontederrota.render(texto3,False,(255,0,0))
            tela.blit(textoinicio,(175,70))
            tela.blit(resu,(75,320))
            tela.blit(mensagem_tempo_over,(75,350))
            tela.blit(texto1,(75,380))
            tela.blit(textorodada,(75,410))
            perdeu = True

        #organiza o X e Y da moeda
        if(ymoeda >= altura):
            ymoeda = -100
            random_moeda = randint(1,3)

        if(ret_play.colliderect(ret_moeda)):
            pontos += 1
            ymoeda = -100
            random_moeda = randint(1,3)

        #organiza o X e Y do relogio
        if(yrelogio >= altura):
            yrelogio = -100
            random_relogio = randint(1,3)

        if(ret_play.colliderect(ret_relogio)):
            relogioscoletados += 1
            yrelogio = -100
            random_relogio = randint(1,3)

        if(temporestante <= 0):
             ##AQUI TEM QUE PUXAR O GAME OVER TMJ!!!!!!!!!!!!!!!!
            tela.blit(imagens.imagem_pista, (0,0))
            tela.blit(imagens.imagem_veu, (0,0))
            #tela.fill((0,0,0))
            mensagemderrota = 'SEM TEMPO IRMÃO'
            textoderrota = fontederrota.render(mensagemderrota,False,(255,0,0))
            tela.blit(textoderrota,(280,150))
            fonte = pygame.font.SysFont("calibri",80,True,True)
            texto8 = 'TRIVIAL RACE'
            textoinicio = fonte.render(texto8,False,(255,0,0))
            mensagemderrota = 'SUA PARTICIPAÇÃO NO JOGO FOI TRIVIAL'
            textoderrota = fontederrota.render(mensagemderrota,False,(255,0,0))
            tela.blit(textoderrota,(75,200))
            texto1 = fontederrota.render(mensagem,False,(255,0,0))
            textorodada = fontederrota.render(mensagemrodada,False,(255,0,0))
            mensagemrodada = f'{textorodada}'
            resumo = 'RESUMO DO JOGO:'
            resu = fontederrota.render(resumo,False,(255,0,0))
            texto3 = f'TEMPO QUE RESTAVA: {temporestante}Seg'
            mensagem_tempo_over = fontederrota.render(texto3,False,(255,0,0))
            tela.blit(textoinicio,(175,70))
            tela.blit(resu,(75,320))
            tela.blit(mensagem_tempo_over,(75,350))
            tela.blit(texto1,(75,380))
            tela.blit(textorodada,(75,410))
            perdeu = True

        #Resolve a questão de um drop sobrepor o outro
        if(ret_bot.colliderect(ret_moeda)):
            ymoeda -= 120
        if(ret_bot.colliderect(ret_relogio)):
            yrelogio -= 120
        if(ret_moeda.colliderect(ret_relogio)):
            yrelogio -= 120

        ybot -= vbot
        ymoeda -= vmoeda
        yrelogio -= vrelogio

        #imprime as mensagem na tela
        if((not ret_play.colliderect(ret_bot)) and ( not (temporestante <= 0))):
            tela.blit(texto,(680,40))
            tela.blit(textotempo,(680,90))
            tela.blit(textorodada,(680,140))

        pygame.display.update()
