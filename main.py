import pygame

# Imagem de fundo
track_image = pygame.image.load('img/pista.png')

# Dimensões
width_window = track_image.get_width()
height_window = track_image.get_height()

# Inicia Pygame
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((width_window, height_window))
pygame.display.set_caption('Imagem no Pygame')

run = True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Implementa imagem de fundo
  window.blit(track_image, (0,0))

  #Atualiza a janela
  pygame.display.update()

  # Limita a 30 quadros por segundo
  clock.tick(30)

# FInaliza o pygame
pygame.quit()
