import pygame

#CARREGAMENTO DE IMAGENS SEM REDIMENSIONAMENTO
def carregamento_Imagens(imagem):
    return pygame.image.load(imagem)

#DEFININDO A FUNCAO PARA MUDAR A ESCALA DE IMAGENS NECESSARIAS
def redimensionamento_Imagens(imagem, escala):
    imagem = pygame.image.load(imagem)
    largura = imagem.get_width()
    altura = imagem.get_height()
    imagem = pygame.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
    return imagem


imagem_pista = carregamento_Imagens("images/pista.png")
imagem_veu = carregamento_Imagens("images/veu.png")
imagem_start = carregamento_Imagens("images/start.png")
imagem_exit = carregamento_Imagens("images/exit.png")
imagem_trofeu = carregamento_Imagens("images/trofeu.png")
imagem_continue = carregamento_Imagens("images/continue.png")
imagem_restart = carregamento_Imagens("images/restart.png")
imagem_back = carregamento_Imagens("images/back.png")
imagem_ready = redimensionamento_Imagens("images/ready.png", 0.7)
imagem_set = redimensionamento_Imagens("images/set.png", 0.7)
imagem_go = redimensionamento_Imagens("images/go.png", 0.7)
imagem_moeda = redimensionamento_Imagens("images/moeda.png", 0.09)
imagem_relogio = redimensionamento_Imagens("images/relogio.png", 0.088)
imagem_carro_player = redimensionamento_Imagens("images/carro_player.png", 1.3)
imagem_carro1 = redimensionamento_Imagens("images/carro1.png", 1.3)
imagem_carro2 = redimensionamento_Imagens("images/carro2.png", 1.3)
imagem_carro3 = redimensionamento_Imagens("images/carro3.png", 1.3)
imagem_carro4 = redimensionamento_Imagens("images/carro4.png", 1.3)
imagem_carro5 = redimensionamento_Imagens("images/carro5.png", 1.3)
imagem_carro6 = redimensionamento_Imagens("images/carro6.png", 1.3)
imagem_carro7 = redimensionamento_Imagens("images/carro7.png", 1.3)
imagem_carro8 = redimensionamento_Imagens("images/carro8.png", 1.3)
imagem_carro9 = redimensionamento_Imagens("images/carro9.png", 1.3)
imagem_carro10 = redimensionamento_Imagens("images/carro10.png", 1.3)