import pygame as pg

class Botao():
    def __init__(self, posicaoy, imagem, escala, janela):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagem = pg.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
        self.posicaox = (400 - ((self.imagem.get_width())/2))
        self.retangulo = self.imagem.get_rect()
        self.retangulo.topleft = (self.posicaox, posicaoy)
        self.clicado = False
        self.janela = janela

    def botao(self):
        acao = False
        posicao = pg.mouse.get_pos()

        if self.retangulo.collidepoint(posicao):
            if pg.mouse.get_pressed()[0] == 1 and self.clicado == False:
                self.clicado = True
                acao = True
        
        if pg.mouse.get_pressed()[0] == 0:
            self.clicado = False

        self.janela.blit(self.imagem, (self.retangulo.x, self.retangulo.y))

        return acao
