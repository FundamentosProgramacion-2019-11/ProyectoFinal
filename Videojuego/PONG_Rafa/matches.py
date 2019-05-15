import pygame   # Librería de pygame
import Files
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0,0,0)
pygame.font.init()
letra = pygame.font.Font('game_over.ttf', 150)
# Estructura básica de un programa que usa pygame para dibujar
def match():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    partidas = Files.readMatches()
    partidas=partidas[-4:]
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(NEGRO)
        Jugador1= letra.render("Jugador 1",True,BLANCO)
        ventana.blit(Jugador1,[0,0])
        Jugador2 = letra.render("Jugador 2", True, BLANCO)
        ventana.blit(Jugador2,[ANCHO-275,0])
        ventana.blit(letra.render(str(partidas[0]),True,BLANCO),[ANCHO//2-25,100])
        ventana.blit(letra.render(str(partidas[1]),True,BLANCO),[ANCHO//2-25,150])
        ventana.blit(letra.render(str(partidas[2]),True,BLANCO),[ANCHO//2-25,200])
        ventana.blit(letra.render(str(partidas[3]),True,BLANCO),[ANCHO//2-25,250])
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame