import pygame
import numpy as np
import sys

# Configurações do jogo
WIDTH, HEIGHT = 800, 600  # Tamanho da janela
GRID_SIZE = 50            # Quantidade de células por lado (GRID_SIZE x GRID_SIZE)
CELL_SIZE = WIDTH // GRID_SIZE  # Tamanho de cada célula em pixels
FPS = 4                  # Quadros por segundo

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)


# Função principal do jogo
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Test")
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(BLACK)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        print(pygame.mouse.get_pressed())

        pygame.display.flip()
        clock.tick(FPS)

#main()

FODASE = 300

def maconha():
    global FODASE
    FODASE = 400
    print(FODASE)

maconha()

print(FODASE)