#Librerias
import pygame
import numpy as np
import time

#Colores, constantes
COLOR_FO = (10, 10, 10)
COLOR_CUA = (40, 40, 40)
COLOR_CMUERTA = (170, 170, 170)
COLOR_CVIVA = (255, 255, 255)

#Funcion: Actualizar

def act(Pantalla, celds, Taman, Con_prog=False):
    update_cells = np.zeros((celds.shape[0], celds.shape[1]))
    for x, y in np.ndindex(celds.shape):
        #contador
        alive = np.sum(celds[x-1: x+2, y-1: y+2]) - celds[x, y]
        #reglas
        color = COLOR_FO if celds[x, y] == 0 else COLOR_CVIVA
        if celds[x, y] == 1:
            if alive < 2 or alive> 3:
                if Con_prog:
                    color = COLOR_CMUERTA
                
            elif 2 <= alive <= 3:
                update_cells[x, y] = 1
                if Con_prog:
                    color = COLOR_CVIVA
        else:
            if alive == 3:
                update_cells[x, y] = 1
                if Con_prog:
                    color = COLOR_CVIVA
        # Creacion cuadricula
        pygame.draw.rect(Pantalla, color, (y *Taman, x* Taman, Taman-1, Taman-1))
    return update_cells

#Funcion principal
def main():
    #Inicializacion
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    cells =np.zeros((60, 80))
    screen.fill(COLOR_CUA)
    act(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()
    # Ejecucion
    running = False
    # Bucle de "gameplay"
    while True:
        for event in pygame.event.get():
            # Comandos de juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    act(screen, cells, 10)
                    pygame.display.update()
                if event.key == pygame.K_ESCAPE:
                   running = False
                   pygame.quit()
                   pygame.display.quit()
                   break
                if event.key == pygame.K_r:
                    running = False
                    pygame.quit()
                    pygame.display.quit()
                    pygame.init()
                    screen = pygame.display.set_mode((800, 600))
                    cells =np.zeros((60, 80))
                    screen.fill(COLOR_CUA)
                    act(screen, cells, 10)
                    pygame.display.flip()
                    pygame.display.update()
                   # Rellenado de celdas  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()           
                    cells[pos[1]//10, pos[0] // 10] = 1
                    act(screen, cells, 10)
                    pygame.display.update()
                if event.button == 3:
                    pos = pygame.mouse.get_pos()           
                    cells[pos[1]//10, pos[0] // 10] = 0
                    act(screen, cells, 10)
                    pygame.display.update()
                        
        #Actualizacion de la pantalla
        if running:
            cells = act(screen, cells, 10, Con_prog=True)
            pygame.display.update()
        time.sleep(0.0001)

    

# "Bucle" de ejecucion general
if __name__ == "__main__":
    main()
    
