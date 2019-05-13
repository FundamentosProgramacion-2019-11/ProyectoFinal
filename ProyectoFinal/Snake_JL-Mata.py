# Autor: Jose Luis Mata Lomeli
# Crear el minijuego Snake usando Pygame

import pygame
import random

# COLORES
BLANCO= (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 155, 0)

# Dimensiones de Trabajo
ANCHO = 800
ALTO = 600

############################################################################################

def snake(ventana, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(ventana, NEGRO, [XnY[0], XnY[1], 20, 20])

def message_to_screen(ventana, msg, color, fuente, x, y):
    screen_text = fuente.render(msg, True, color)
    ventana.blit(screen_text, [x, y])


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    reloj = pygame.time.Clock()  # Para limitar los fps
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea una ventana de ANCHO x ALTO para dibujar
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    gameOver = False    # Murio o choco

    # POSICION inicial de la Serpiente
    posicion_x = ANCHO//2
    posicion_y = ALTO//2

    # Para que la Serpiente avance
    cambio_x = 0
    cambio_y = 0

    # Lista para el LARGO de la Serpiente
    snakeList = []
    snakeLength = 1


    # POSICION de la Manzana
    AppleX = round(random.randrange(0, ANCHO - 20)/20)*20
    AppleY = round(random.randrange(0, ALTO - 20)/20)*20


    # MUSICA
    pygame.mixer.init()
    pygame.mixer.music.load("MusicaFondo.mp3")
    pygame.mixer.music.play()

    # TEXTO
    fuente = pygame.font.SysFont(None, 25)


    # PUNTAJE
    score = 0


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        while gameOver == True: # Si el usuario muere...
            ventana.fill(VERDE)  # Fondo color BLANCO
            message_to_screen(ventana, "Game over, press C to play again or Q to quit", ROJO, fuente, 180, 280)  # Mensaje
            message_to_screen(ventana, ''.join(["Your score was: ", str(score)]), NEGRO, fuente,  300, 325)
            pygame.display.update()

            # Procesa los eventos que recibe
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Si el usuario hizo click en el botón de salir
                    termina = True  # Queremos terminar el ciclo
                    gameOver = False # Salir de manera directa

                if evento.type == pygame.KEYDOWN:   # Si el usuario oprime una tecla
                    if evento.key == pygame.K_c:    # Si la tecla oprimida fue la "c"...
                        dibujar()   # Volver a jugar

                    if evento.key == pygame.K_q:    # Si el usuario oprimio la tecla "q"
                        termina = True
                        gameOver = False    # El juego acaba

        # Procesa los eventos que recibe
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                termina = True

            # Si el usuario oprime una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Si la tecla oprimida fue la fecha izquierda
                    cambio_x = -20  # Mover a la izquierda
                    cambio_y = 0

                elif event.key == pygame.K_RIGHT:   # Si la tecla oprimida fue la fecha derecha
                    cambio_x = 20   # Mover a la derecha
                    cambio_y = 0

                elif event.key == pygame.K_UP:  # Si la tecla oprimida fue la fecha superior
                    cambio_y = -20  # Mover para arriba
                    cambio_x = 0

                elif event.key == pygame.K_DOWN:  # Si la tecla oprimida fue la fecha inferior
                    cambio_y = 20   # Mover para abajo
                    cambio_x = 0


        # Si la serpiente choca con el limite de la ventana...
        if posicion_x >= ANCHO or posicion_x <= 0 or posicion_y >= ALTO or posicion_y <= 0:
            gameOver = True   # Fin del Juego. Continuar?


        # Para no detenerse y sea continuo...
        posicion_x += cambio_x
        posicion_y += cambio_y

        # Fondo de la Pantalla
        ventana.fill(VERDE)


        # Mensaje para puntuacion
        message_to_screen(ventana, ''.join(["Score: ", str(score)]), NEGRO, fuente, 10, 10)

        ## TRAZOS:
        # Cuerpo de la Manzana
        pygame.draw.rect(ventana, ROJO, [AppleX, AppleY, 20, 20])

        # Cuerpo de la Serpiente
        snakeHead = []
        snakeHead.append(posicion_x)
        snakeHead.append(posicion_y)
        snakeList.append(snakeHead)

        # Si la longituud de la serpiente es mayor al largo
        if len(snakeList) > snakeLength:
            del snakeList[0]    # Borrar

        # Por cada segmento de la Serpiente (desde el final)
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:  # Si algun segmento toca alguna parte de la serpiente
                gameOver = True   # Fin del Juego

        snake(ventana, snakeList)   # Funcion para la Serpiente

        pygame.display.update()

        # Si la serpiente se come la manzana...
        if posicion_x == AppleX and posicion_y == AppleY:
            AppleX = round(random.randrange(0, ANCHO - 20) / 20) * 20   #Generar otra manzana en otras ccordenadas
            AppleY = round(random.randrange(0, ALTO - 20) / 20) * 20
            snakeLength += 1   # Aumentar la longitud de la Serpiente
            score += 5  # Sumar 5 puntos al puntaje
            message_to_screen(ventana, ''.join(["Score: ", str(score)]), NEGRO, fuente, 10, 10)  # Mensaje de puntuacion

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 10 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame
    quit()

#####################################################################################################

def main():

    dibujar()

main()

