
import pygame
import imagens
from pygame.locals import *
from sys import exit
from datetime import datetime
from randomizacao import Randomizacao
from movimentacao_jogador import MovimentacaoJogador
from nivel import Nivel

movimentacao_jogador = MovimentacaoJogador()
randomizacao = Randomizacao()
nivel = Nivel()

def game():

    pygame.init()

    #determinações de dimensões do jogo e fontes
    largura = 800
    altura = 650
    xplay,movimentacao_jogador.yplay = 380,400
    vbot = -0.5
    vmoeda = -0.5
    vrelogio = -0.5
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Trivial Race')
    fonte = pygame.font.SysFont("calibri",20,True,True)
    fontederrota = pygame.font.SysFont("calibri",35,True,True)
    

    #funcionamento do relogio, pega o momento inicial
    tempo = 60
    momentoinicial = datetime.today()
    relogioscoletados = 0

    #pega as imagens que vão ser rodadas no jogo
    carro_player = pygame.image.load('images/carro.png')
    carro_bot = pygame.image.load('images/carro1.png')
    moeda = pygame.image.load('images/moeda.png')
    moeda = pygame.transform.scale(moeda,(40,40))
    relogio = pygame.image.load('images/relogio.png')
    relogio = pygame.transform.scale(relogio,(40,40))
    
    fundo = pygame.image.load('images/pista.png').convert()
    fundo = pygame.transform.scale(fundo,(largura, altura))

    pontos = 0
   
    perdeu = False
    while perdeu == False:
        tela.fill((0,0,0))
        
        nivel.subirnivel()
        
        #monta a string de fazer a mensagem de pontos
        mensagem = f"PONTOS: {pontos}"
        mensagemrodada = f"RODADA: {nivel.rodada}"
        texto = fonte.render(mensagem,False,(0,255,0))
        textorodada = fonte.render(mensagemrodada,False,(0,255,0))
        
        #pega a diferença de tempo em segundos entre o momentoinicial e o momentoatual, assim subtrai do tempo total do jogo para fazer o tempo regressivo        
        momentoatual = datetime.today()
        diferenca = momentoatual-momentoinicial
        hora,minuto,segundo = str(diferenca).split(":")
        temporestantereal = tempo - float(segundo)
        temporestante = int(temporestantereal) + relogioscoletados * 1
        mensagemtempo = f"TEMPO: {temporestante}"
        textotempo = fonte.render(mensagemtempo,False,(0,255,0)) 
    
        
        #imprime as imagens e formas
        ret_bot = pygame.draw.rect(tela,(0,0,255),(randomizacao.xbot,randomizacao.ybot,63,91))
        ret_play = pygame.draw.rect(tela,(255,0,0),(movimentacao_jogador.xplay,movimentacao_jogador.yplay,58,93))
        ret_moeda = pygame.draw.rect(tela,(0,255,255),(randomizacao.xmoeda,randomizacao.ymoeda,40,40))
        ret_relogio = pygame.draw.rect(tela,(255,0,255),(randomizacao.xrelogio,randomizacao.yrelogio,40,40))

        tela.blit(fundo, (0,0))
        tela.blit(relogio,(randomizacao.xrelogio,randomizacao.yrelogio))
        tela.blit(moeda,(randomizacao.xmoeda,randomizacao.ymoeda))
        tela.blit(carro_player,(movimentacao_jogador.xplay,movimentacao_jogador.yplay))
        tela.blit(carro_bot,(randomizacao.xbot,randomizacao.ybot))
        
        movimentacao_jogador.fazmovimentacao()
        
        #organiza o X e Y do bot
        if(randomizacao.ybot >= altura):
            nivel.rodada += 1
            randomizacao.ybot = -100
            randomizacao.randomico1() 
            
        if(ret_play.colliderect(ret_bot)):
            tela.blit(imagens.imagem_pista, (0,0))
            tela.blit(imagens.imagem_veu, (0,0))
            #tela.fill((0,0,0))
            fonte =   pygame.font.SysFont("calibri",80,True,True)
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
        if(randomizacao.ymoeda >= altura):
            randomizacao.ymoeda = -100
            randomizacao.randomico_moeda()
            
        if(ret_play.colliderect(ret_moeda)):
            pontos += 1
            randomizacao.ymoeda = -100
            randomizacao.randomico_relogio() 
        
        #organiza o X e Y do relogio
        if(randomizacao.yrelogio >= altura):
            randomizacao.yrelogio = -100
            randomizacao.randomico_relogio()
            
        if(ret_play.colliderect(ret_relogio)):
            relogioscoletados += 2
            randomizacao.yrelogio = -100
            randomizacao.randomico_relogio()
        
        if(temporestante <= 0):
            tela.fill((0,0,0))
            mensagemderrota = 'SEM TEMPO IRMÃO'
            textoderrota = fontederrota.render(mensagemderrota,False,(255,0,0))
            tela.blit(textoderrota,(300,200))
            print('SEM TEMPO IRMÃO')
            perdeu = True
        
        #Resolve a questão de um drop sobrepor o outro
        if(ret_bot.colliderect(ret_moeda)):
            randomizacao.ymoeda -= 120
        if(ret_bot.colliderect(ret_relogio)):
            randomizacao.yrelogio -= 120
        if(ret_moeda.colliderect(ret_relogio)):
            randomizacao.yrelogio -= 120
        
        randomizacao.ybot -= vbot 
        randomizacao.ymoeda -= vmoeda
        randomizacao.yrelogio -= vrelogio
        
        #imprime as mensagem na tela
        if(not ret_play.colliderect(ret_bot)):
            tela.blit(texto,(680,40))
            tela.blit(textotempo,(680,90))
            tela.blit(textorodada,(680,140))
        
        pygame.display.update()