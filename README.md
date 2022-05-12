# pygame-UFPE
# **🚗 Trivial Race 🚗**

### **Trivial é um jogo 2D, feito para a disciplina de Introdução à Computação da UFPE, em que o jogador precisa desviar de carros e coletar moedas, para aumentar pontuação, e relógios que acrescentam ‘bônus tempo’ durante o percurso. Conforme as rodadas acontecem, fica cada vez mais difícil permanecer na pista e evitar a temida tela game over.**

### **Membros**

- Brenda
- Glória
- Nicolas
- Sandrírames
- Ronald

### **Ferramentas e Tecnologias**    
- *Pygame* ⇒ O motivo de escolha dessa biblioteca: por ser a mais utilizada e indicada para desenvolvimento de jogos em *python*.
- *Sys* ⇒ O motivo de escolha dessa biblioteca: Importar o *Exit* dessa biblioteca, utilizado para fechar o jogo.
- *Random* ⇒ Utilizado no jogo para mecânica de ‘dropar’ os itens coletáveis e o bot (carro inimigo)
- Datetime ⇒ Utilizado no contador do jogo.
- Photoshop ⇒ Ferramenta que possibilita a edição das imagens utilizadas no jogo.
- Trello ⇒ Ferramenta para organização de atividades.
- Notion ⇒ Ferramenta para organização de atividades.

### **A divisão de trabalho dentro do grupo**

- Telas iniciais e edição de imagens - Brenda
- Mecânica - Ronald e Nícolas
- Tela Game Over - Ronald e Nícolas
- Background e Efeitos sonoros - Glória
- Versionamento do código - Glória
- Documentação - Equipe inteira
- Orientação a objetos - Sandrírames
- Slide apresentação - Sandrírames

### **Como rodar**

Execute o arquivo interface.py

### **Organização do código**

- **main.py**: Se encontra o código da interface do jogo. O código é iniciado com *pygame.init()*, para abrir a interface do jogo. É chamada a *set_caption*, função do *pygame* que serve para intitular o ‘nome do jogo’ (nome que fica em cima do *display*).  A variável ‘Janela’ é definida como o *display* do jogo, com a tela do jogo sendo aberta nas dimensões 800X650.  É importada a classe botões*.py*, que possibilita a criação dos vários objetos de botão que existem na tela inicial.
    
       As imagens são buscadas da pasta de imagens e são renderizadas em cima dos blocos. Todas as telas iniciais adquirem valores booleanos para controlar o momento em que elas aparecem. 
    
       O loop principal do jogo é declarado.  
    
    Para o funcionamento das telas uma série de *if statement* são declaradas.  Também é importado a [mecanica.py](http://mecanica.py) , o que possibilita a “junção” da lógica de funcionamento com o menu inicial do jogo.
    
    - **botoes*.py***: Classe importada na [main*.py](http://main.py)* com os atributos das características do objeto e método que retorna o clique do botão.  No botoes.*py* também é importado a biblioteca *pygame* para que seja possível a criação do método.
    - **imagens.*py*:** Módulo que redimensiona as imagens utilizadas no jogo.
    - **mecanica*.py*:** Código contendo as mensagens, tempo, e imprime as imagens do jogo. Na mecanica.py são importadas as bibliotecas: *pygame* e todos os seus *LOCALS*, o *EXIT* de SYS - utilizado para fechar o jogo, o *datetime* - utilizado no contador.
        
        São importadas as classes: MovimentacaoJogador, Nivel, Randomizacao. 
        
        É determinado as dimensões do display e as velocidades iniciais do jogador e dos objetos. 
        
        As fontes para descrever as mensagens de derrota são guardadas. Logo em seguida, o início da mecânica do ‘*time’* é imposto dessa forma: quando iniciado, o tempo desse momento é guardado, depois no loop do jogo o tempo atual do momento é guardado e é feita a diferença entre os dois períodos de tempo, o resultado dessa operação é o tempo restante do jogador.  Caracterizando assim, um tempo regressivo.  
        
        O *loop* do jogo é iniciado. 
        
        A função nivel*.py*, que incrementa a dificuldade do jogo, é chamada. 
        
        Os textos que ficam na lateral são montados, e é impresso as imagens e formas com *rect.*
        
        A função movimentacao_jogador é chamada. 
        
        A função randomizacao é chamada. 
        
        - **randomizacao*.py*:** É importada o *random*, que possibilita que os coletáveis apareçam de forma aleatória. A randomização da moeda, *bot* e relógio são definidas em metódos, que usando comando condicionais e declarando variáveis, acionam a função *random.*
        - **movimentacao_jogador.*py*:** É importado a biblioteca *pygame* e os seus *locals*, para que seja possível as ações dos botões.  O metódo fazmovimentacao, possibilita a ação dos botões, com a implementação de um *loop* infinito, e  condicionais para sair do jogo e para mover o jogador para direita e para esquerda.
        - **nivel*.py*:** A cada 5 rodadas passadas, é aumentado a velocidade dos objetos que descem no mapa ficando mais difícil não colidir com o carro e perder o jogo. Um *for loop* é utilizado para que isso seja possível.

### **Conceitos utilizados no jogo**

- laços de repetição
    
    *for loop:*  Acionado na nivel*.py*, para incremento de níveis e dificuldade ao jogo. **
    
    *While loop*: Loop principal do jogo, que permite que ‘rodar o jogo’. (main.py) (mecanica.py)
    
- Comandos condicionais
    
    *if statement:* Acionado no funcionamento do menu inicial, tela de *loading*. contador da tela de *loading* é declarado como uma variável contagem com valor booleano. o *if statement*  começa a fazer a contagem, depois disso a contagem é setada para o valor booleano contrário ao inicial possibilitando que a imagem da pista e as mensagens *Go* e *Ready* aparecem na tela. 
    
    Acionado , também, nas ações de clicar no botão *exit*, que faz o jogo parar. E no botão start, que habilita a tela de contagem. (main.py)
    
- Funções: Acionado na [mecanica.py](http://mecanica.py) para chamar as classes.
- Programação Orientada a Objeto: Criação de diferentes módulos. Os atributos e métodos possibilitam o funcionamento conjunto de todas as parte do projeto.

observação: Para evitar redundância nesse tópico, é descrito os aplicações dos conceitos que não foram citadas no tópico “ Organização do código”. 

### Desafios e erros enfrentados

- Erro Cometido: Fotos se sobrepondo na colisão.
    
    Erro corrigido criando uma condição para fazer um dos itens recuar no momento da colisão, evitando que as duas imagens ficassem sobrepostas. (comentado no código mecanica.py)
    
- Desafio:  Codar dentro de *branches*, fazendo *commits* e dando *push* nas alterações.
- Desafio enfrentado: com videochamadas para compartilhamento de conhecimentos sobre o *Git*, permitindo o versionamento do código.
- observação: Além do desafio de orientar todo o código a objeto, e  o gerenciamento de tempo.
- Lições aprendidas: Importância do trabalho em equipe, comunicação ativa durante o desenvolvimento e organização do planejamento e do código.
