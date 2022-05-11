import pygame
import botoes
import imagens
import mecanica

pygame.init()
janela = pygame.display.set_mode((800,650))
pygame.display.set_caption("Trivial Race")

#CRIAÇÃO DE TODOS OS BOTÕES DISPONÍVEIS DOS MENUS
botao_start = botoes.Botao(200, imagens.imagem_start, 0.4, janela)
botao_exit = botoes.Botao(300, imagens.imagem_exit, 0.4, janela)
botao_trofeu = botoes.Botao(550, imagens.imagem_trofeu, 0.2, janela)
botao_trofeu_back = botoes.Botao(550, imagens.imagem_back, 0.4, janela)
botao_continue = botoes.Botao(200, imagens.imagem_continue, 0.4, janela)
botao_restart = botoes.Botao(300, imagens.imagem_restart, 0.4, janela)
botao_exit_esc = botoes.Botao(400, imagens.imagem_exit, 0.4, janela)

#TODAS AS TELAS DE MENU DO JOGO
telainicial = True
telaloading = False
telaesc = False
telatrofeu = False
telagameover = False

#CONTADOR DA TELA DE LOADING
contagem = False

run = True
while run:

    #FUNCIONAMENTO DO MENU INICIAL
    if telainicial:
        fonte = pygame.font.SysFont("calibri",80,True,True)
        texto = 'TRIVIAL RACE'
        textoinicio = fonte.render(texto,False,(255,0,0))

        janela.blit(imagens.imagem_pista, (0,0))
        janela.blit(imagens.imagem_veu, (0,0))

        janela.blit(textoinicio,(175,70))
        if botao_start.botao():
            telainicial = False
            telaloading = True
            contagem = True
        if botao_exit.botao():
            run = False
        '''if botao_trofeu.botao():
            telainicial = False
            anterior = 'start'
            telatrofeu = True'''

    #FUNCIONAMENTO DA TELA DE LOADING
    if telaloading:
        if contagem:
            countdown = 3
            last_count = pygame.time.get_ticks()
            contagem = False
        else:
            janela.blit(imagens.imagem_pista, (0,0))
            janela.blit(imagens.imagem_veu, (0,0))
            if countdown > 2:
                janela.blit(imagens.imagem_ready, ((400 - imagens.imagem_ready.get_width()/2), 200))
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -=1
                    last_count = count_timer
            else:
                if countdown > 1:
                    janela.blit(imagens.imagem_set, ((400 - imagens.imagem_set.get_width()/2), 200))
                    count_timer = pygame.time.get_ticks()
                    if count_timer - last_count > 1000:
                        countdown -=1
                        last_count = count_timer
                else:
                    if countdown > 0:
                        janela.blit(imagens.imagem_go, ((400 - imagens.imagem_go.get_width()/2), 200))
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -=1
                            last_count = count_timer
                    else:
                        telaloading = False
                        mecanica.game()

    #FUNCIONAMENTO DA TELA DE RECORDES
    '''if telatrofeu:
        janela.blit(imagens.imagem_pista, (0,0))
        janela.blit(imagens.imagem_veu, (0,0))
        if botao_trofeu_back.botao():
            if anterior == 'start':
                telainicial = True
                telatrofeu = False
            elif anterior == 'esc':
                telaesc = True
                telatrofeu = False
            elif anterior == 'gameover':
                telagameover = True
                telatrofeu = False'''

    #FUNCIONAMENTO DO MENU ESC
    if telaesc:
        janela.blit(imagens.imagem_pista, (0,0))
        janela.blit(imagens.imagem_veu, (0,0))
        if botao_continue.botao():
            telaesc = False
        if botao_restart.botao():
            telaesc = False
            telaloading = True
            contagem = True
        if botao_exit_esc.botao():
            run = False
        if botao_trofeu.botao():
            telaesc = False
            anterior = 'esc'
            telatrofeu = True

    #Controlador da janela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not telainicial:
                telaesc = True
    pygame.display.update()

pygame.QUIT()
