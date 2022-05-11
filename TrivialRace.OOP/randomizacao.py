from random import randint

class Randomizacao:

    def __init__(self):
        self.xbot = 380
        self.ybot = -100
        self.xmoeda = 380 
        self.ymoeda = -100 
        self.xrelogio = 380 
        self.yrelogio = -100
        self.random1 = 0
        self.random_moeda = 0
        self.random_relogio = 0
        self.randomico1()
    
    def randomico1(self):
        self.random1 = randint(1,3)
        self.randomico_moeda()

    def randomico_moeda(self):
        self.random_moeda = randint(1,3)
        self.randomico_relogio()

    def randomico_relogio(self):
        self.random_relogio = randint(1,3)
        self.gera_randomizacao_bot()
    
    def gera_randomizacao_bot(self):
        if(self.random1 == 1):
            self.xbot = 200
            
        if(self.random1 == 2):
            self.xbot = 380
            
        if(self.random1 == 3):
            self.xbot = 560
            self.gera_randomizacao_moeda()
    
    def gera_randomizacao_moeda(self):
        if(self.random_moeda == 1):
            self.xmoeda = 200
            
        if(self.random_moeda == 2):
            self.xmoeda = 380
            
        if(self.random_moeda == 3):
            self.xmoeda = 560
            self.gera_randomizacao_relogio()

    def gera_randomizacao_relogio(self):
        if(self.random_relogio == 1):
            self.xrelogio = 200
            
        if(self.random_relogio == 2):
            self.xrelogio = 380
            
        if(self.random_relogio == 3):
            self.xrelogio = 560


    
    
