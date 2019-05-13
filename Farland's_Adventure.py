#Roberto Castro Barrios A01748559
#Descripción: En esta aventura, tendras que luchar contra diversas oleadas de monstruos
#Nota: El punto debil del enemigo es de la boca para abajo
import pygame   # Librería de pygame
import math as m # Librería de math
import random
from time import clock
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

#Lista
ListaEnemigos = []


# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)       # Solo negro

# VARIABLES GLOBALES
# Personaje
xPersonaje = 0
yPersonaje = ALTO//2

# Enemigo
xEnemigo = 720
yEnemigo = random.randint(80, 520)
Dx = +7.5

# Estructura básica de un programa que usa pygame para dibujar
def dibujarMenu(ventana, btnPlay, btnExit, title, fondo):
    ventana.blit(fondo, (0, 0))
    ventana.blit(btnPlay, (190, 350))
    ventana.blit(btnExit, (290, 500))
    ventana.blit(title, (100, 50))

def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0,0))

def dibujarPersonaje(ventana, personaje):
    ventana.blit(personaje, (xPersonaje, yPersonaje))

def dibujarProyectil(ventana, spriteBala):
    if spriteBala.rect.left != -1: # Sirve para dibujar la bala
        ventana.blit(spriteBala.image, spriteBala.rect)  # Imagen dentro del sprite y como coordenadas pone rect.
        spriteBala.rect.left += 20
        if spriteBala.rect.left >880:
            spriteBala.rect.left = -1

def dibujarEnemigo(ventana, enemigo):
    global xEnemigo,yEnemigo, Dx
    ventana.blit(enemigo, (xEnemigo, yEnemigo))
    xEnemigo -= Dx
    #Probar choque
    if xEnemigo <= -80:
        xEnemigo = 720
        yEnemigo = random.randint(80, 520)
        return True

def probarColision(spriteBala, enemigo):
    global xEnemigo, yEnemigo
    xBala = spriteBala.rect.left
    yBala = spriteBala.rect.top
    if xBala >= xEnemigo + 10 and xBala <= xEnemigo + 40 and yBala >= yEnemigo and yBala <= yEnemigo + 40:
        xEnemigo = -30000
        yEnemigo = -30000
        return True
    else:
        return False  # No hay colisión

def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render("Puntaje: " + str(marcador), 1, BLANCO)
    ventana.blit(texto, (ANCHO//2, 0))

def comprobarLimiteEnemigo(xEnemigo):
    if xEnemigo <=0:
        return True
    else:
        return False


def comprobarGameOver(marcador):
    return xEnemigo


def marcadorFinal(ventana, marcador, fuente):
    texto = fuente.render("Tu puntaje final es: " + str(marcador), 1, BLANCO)
    ventana.blit(texto, ((ANCHO //2)-90, ALTO//2))


def dibujarGameOver(ventana, fondoGO, regresar):
    ventana.blit(fondoGO, (0, 0))
    ventana.blit(regresar, (0, 0))

def dibujar():
    global xPersonaje, yPersonaje
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Cargar Imágenes
    btnPlay = pygame.image.load("btnPlay.png")
    btnExit = pygame.image.load("btnExit.png")
    fondoJuego = pygame.image.load("fondoJuego.png")
    fondo = pygame.image.load("fondoMenuP.png")
    title = pygame.image.load("title.png")
    imgBala = pygame.image.load("shot.gif")
    personaje = pygame.image.load("player.png")
    enemigo = pygame.image.load("lizard.gif")
    fondoGO = pygame.image.load("tierraD.jpg")
    regresar = pygame.image.load("return.png")

    # SPRITES

    # Movimiento de bala
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()  # Datos de la imagen.
    spriteBala.rect.left = -1  # Coordenada en x
    spriteBala.rect.top = -1  # Coordenada en y

    # AUDIO
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("laser.wav")
    pygame.mixer.music.load("soundtrack.mp3")
    pygame.mixer.music.play(-1)

    # TEXTO
    fuente = pygame.font.SysFont("Arial", 24)
    marcador = 0

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    Game_Over = 3
    estado = MENU

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if xMouse >= 190 and xMouse <= 609 and yMouse >= 350 and yMouse <= 399:
                    # Oprimió el boton play
                    xMouse = -1
                    estado = JUGANDO
                if xMouse >= 291 and xMouse <= 503 and yMouse >= 501 and yMouse <= 551:
                    termina = True
                if xMouse >= 0 and xMouse <= 187 and yMouse >= 0 and yMouse <= 52:
                    estado = MENU
            elif evento.type == pygame.KEYDOWN:  # Oprimió una tecla
                    # Verificar qué tecla se oprimió
                if evento.key == pygame.K_RIGHT:
                    xPersonaje += 20
                elif evento.key == pygame.K_LEFT:
                    xPersonaje -= 20
                elif evento.key == pygame.K_UP:
                    yPersonaje -= 20
                elif evento.key == pygame.K_DOWN:
                    yPersonaje += 20
                elif evento.key == pygame.K_SPACE:
                    if spriteBala.rect.left == -1:
                        spriteBala.rect.left = xPersonaje + 30 - 12
                        spriteBala.rect.top = yPersonaje - 5
                        efectoDisparo.play()


        # Borrar pantalla
        ventana.fill(BLANCO)

        if estado == MENU:
            dibujarMenu(ventana, btnPlay, btnExit, title, fondo)

        elif estado == JUGANDO:
            # Actualizar Objetos
            limiteEnemigo = comprobarLimiteEnemigo(xEnemigo)
            if limiteEnemigo == True:
                marcador -= 1000
            colision = probarColision(spriteBala, enemigo)
            if colision == True:
                marcador += 200

            dibujarFondo(ventana, fondoJuego)
            dibujarPersonaje(ventana, personaje)
            dibujarEnemigo(ventana, enemigo)
            dibujarProyectil(ventana, spriteBala)
            # dibuja el texto
            dibujarMarcador(ventana, marcador, fuente)
            gameOver = comprobarGameOver(xEnemigo)
            if gameOver < 0:
                estado = Game_Over

        elif estado == Game_Over:
            dibujarGameOver(ventana, fondoGO, regresar)
            marcadorFinal(ventana, marcador, fuente)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()


# Llamas a la función principal
main()