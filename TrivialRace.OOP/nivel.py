
class Nivel:
    def __init__(self):
        self.vbot = 0.5
        self.vmoeda = -0.5
        self.vrelogio= -0.5
        self.rodada = 0
        self.blocosdenivel = 0
        self.subirnivel()

    def subirnivel(self):
        self.blocosdenivel = self.rodada//5
        for i in range (self.blocosdenivel):
            self.nivel = -0.5 - i/10
            self.vbot = self.nivel
            self.vmoeda = self.nivel
            self.vrelogio = self.nivel