# encoding: UTF-8
# Autor: Roberto Emmanuel González Muñoz
# Este juego se llama BlasterSolo, es un juego que consiste en dos
# jugadores lanzar discos y esquivarlos. Una vez alcanzados los 1000
# puntos  se muestra la puntuación y quea guardado enla lista de ganadores.
# para jugador 1 para el movimiento de izquierda a derecha  se usan las teclas "a" y "d".
# para jugador 2 para el moviemiento de izquierda a derecha se usan las teclas  "flecha izquierda" y "flecha derecha"
# para disparar con jugador 1 se usa "q" y jugador 2 usa "espacio"
# usa "escape" para volver al menu.


import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)        # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)              # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)              # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#VARIABLES GLOBALES
xEnemigo = ANCHO//2
yEnemigo = 0


def dibujarFondo(ventana,fondoJuego):
    ventana.blit(fondoJuego, (0,0))


#Dibuja el menu (botones)
def dibujarMenu(ventana, btnStart, imgMenu):
    ventana.blit(imgMenu, (0, 0))
    ventana.blit(btnStart, (300, 275))


def dibujarNave(ventana, imgNave, xNave, yNave):
    ventana.blit(imgNave, (xNave, yNave))


def dibujarEnemigo(ventana, imgEnemigo):
    ventana.blit(imgEnemigo, (xEnemigo, yEnemigo))


def dibujarBala(ventana, spriteBala):
    if spriteBala.rect.left != -1:
        ventana.blit(spriteBala.image, spriteBala.rect)
        # Actualizar bala
        spriteBala.rect.top -= 20
        if spriteBala.rect.top <= -36:
            spriteBala.rect.left = -1 #No se dibuja


def verificarColisionJugador1(spriteBala, xNave, yNave):  # , sprite enemigo
   xBala = spriteBala.rect.left
   yBala = spriteBala.rect.top
   xJugador1 = xNave
   yJugador1 = yNave

   if xBala >= xJugador1 and xBala <= xJugador1 + 50:
       if yBala >= yJugador1 and yBala <= yJugador1 + 50:
   #Colision, desaparece bala y enemigo
           #yEnemigo = -64
           spriteBala.rect.left = -1# fuera de la pantalla
           #xEnemigo = -129
           return True
   return False


def dibujarMarcador(ventana, fuente, puntos):
   texto = fuente.render("Puntos: "+ str(puntos), 1, BLANCO)
   ventana.blit(texto,(20,50))


def dibujarMarcador2(ventana, fuente, puntos2):
   texto = fuente.render("Puntos: "+ str(puntos2), 1, BLANCO)
   ventana.blit(texto,(20,500))


def crearBala(imgBala, listaBalas, xNave, yNave):
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = xNave+25
    spriteBala.rect.top = yNave
    listaBalas.append(spriteBala)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.top -= 16
        if bala.rect.top < -32:
            listaBalas.remove(bala)


def moverBalas2(listaBalas2):
    for bala in listaBalas2:
        bala.rect.top += 16
        if bala.rect.top > 600:
            listaBalas2.remove(bala)


def dibujarListaBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def dibujarListaBalas2(ventana, listaBalas2):
    for bala in listaBalas2:
        ventana.blit(bala.image, bala.rect)


def crearBala2(imgBala, listaBalas2, xEnemigo, yEnemigo):
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = xEnemigo + 25
    spriteBala.rect.top = yEnemigo
    listaBalas2.append(spriteBala)


def dibujarMarcadorFinal(ventana, fuente, puntos, ganador):
    texto = fuente.render("El ganador es el " + ganador + " con " + str(puntos) + " puntos", 1, BLANCO)
    ventana.blit(texto, (ANCHO//8, (ALTO//2)-25))


def verificarColisionJugador2(spriteBala, xEnemigo, yEnemigo):
    xBala = spriteBala.rect.left
    yBala = spriteBala.rect.top
    xJugador1 = xEnemigo
    yJugador1 = yEnemigo

    if xBala >= xJugador1 and xBala <= xJugador1 + 50:
        if yBala >= yJugador1 and yBala <= yJugador1 + 50:
            # Colision, desaparece bala y enemigo
            # yEnemigo = -64
            spriteBala.rect.left = -1 # fuera de la pantalla
            #xEnemigo = -129
            return True
    return False


def dibujarBotonStart(ventana, btnStart):
    ventana.blit(btnStart, (300, 420))


def dibujarBotonScore(ventana, btnScore):
    ventana.blit(btnScore, (300, 275+50))


def dibujarScoreChart(ventana, fuente, ganadores):
    texto = fuente.render("El campeón pasado es el " + str(ganadores[0]), 1, BLANCO)
    ventana.blit(texto, (ANCHO // 6, (ALTO // 2) - 25))


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    #IMAGENES
    btnStart = pygame.image.load("Imagenes/button_play.png")
    btnScore = pygame.image.load("Imagenes/button_score.png")
    fondoJuego = pygame.image.load("Imagenes/Cancha.jpg")
    imgNave = pygame.image.load("Imagenes/HandleB.png")
    imgEnemigo = pygame.image.load("Imagenes/HandleA.png")
    imgMenu = pygame.image.load("Imagenes/Menu.png")

    spriteJugador2 = pygame.sprite.Sprite()
    spriteJugador2.image = imgEnemigo
    spriteJugador2.rect = imgEnemigo.get_rect()
    spriteJugador1 = pygame.sprite.Sprite()
    spriteJugador1.image = imgNave
    spriteJugador1.rect = imgNave.get_rect()


    # Balas (sprites)
    imgBala = pygame.image.load("Imagenes/disk.png")
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = -1

    #COORDENADAS CIRCULO
    xMouse= -1
    yMouse= -1
    #COORDENADAS NAVE
    xNave = ANCHO//2          #IZQUIERDA
    yNave = ALTO-100           #DERECHA

    #ESTADOS
    MENU = 1
    JUGANDO = 2
    GANADOR1 = 3
    GANADOR2 = 4
    SCORE = 5
    ESTADO  = MENU

    # AUDIO(SONIDO)
    pygame.mixer.init()
    # sonido corto  Sound -- wav
    efectoDisparo = pygame.mixer.Sound("Sonido/shoot.wav")
    # Sonido largo Music --mp3
    pygame.mixer.music.load("Sonido/bensound-epic.mp3")
    pygame.mixer.music.play()

    # TEXTO
    fuente = pygame.font.SysFont("arial", 40)

    # puntos
    puntos = 0  # NO ES GLOBAL
    puntos2 = 0


    #LISTA DE BALAS
    listaBalas = [] #Lista vacia
    listaBalas2 = []
    ganadores = []


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 300 and xMouse <= 500 and yMouse >=275 and yMouse <=275+50:
                    xMouse = -1
                    #cambia el estado
                    puntos = 0
                    puntos2 = 0
                    ESTADO = JUGANDO #PASA A JUGANDO
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 420 and yMouse <= 420+50:
                    xMouse = -1
                    puntos = 0
                    puntos2 = 0
                    ESTADO = JUGANDO
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 325 and yMouse <= 325+50:
                    xMouse = -1
                    ESTADO = SCORE

            elif evento.type == pygame.KEYDOWN:#TECLA OPRIMIDAq
                if evento.key == pygame.K_RIGHT:#flecha derecha??
                    xNave += 40
                elif evento.key == pygame.K_LEFT:#flecha izquierda??
                    xNave -= 40
                elif evento.key == pygame.K_d:  # flecha derecha??
                    global xEnemigo
                    xEnemigo += 20
                elif evento.key == pygame.K_a:  # flecha izquierda??
                    xEnemigo -= 20
                elif evento.key == pygame.K_ESCAPE:  # flecha izquierda??
                    ESTADO = MENU
                elif evento.key == pygame.K_SPACE:
                    if len(listaBalas) < 2:
                        crearBala(imgBala, listaBalas, xNave, yNave)
                    efectoDisparo.play()
                    spriteBala.rect.left = xNave + 64 - 16  # poscisiones, Proyecto(getWidth...)
                    spriteBala.rect.top = yNave

                elif evento.key == pygame.K_q:
                    if len(listaBalas2) < 2:
                        crearBala2(imgBala, listaBalas2, xEnemigo, yEnemigo)
                    efectoDisparo.play()
                    spriteBala.rect.left = xEnemigo + 64 - 16  # poscisiones, Proyecto(getWidth...)
                    spriteBala.rect.top = yEnemigo
                elif evento.type == pygame.KEYUP:
                    MOVIENDO = False

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        if ESTADO == MENU:
            dibujarMenu(ventana, btnStart, imgMenu)
            dibujarBotonScore(ventana, btnScore)
        elif ESTADO == JUGANDO:
            # Verficar colisiones/actualizar objetoss
            colJugador2 = verificarColisionJugador2(spriteBala, xEnemigo, yEnemigo)
            colJugador1 = verificarColisionJugador1(spriteBala, xNave, yNave)
            if colJugador2 == True:
                puntos += 20
            elif colJugador1 == True:
                puntos2 += 20
            elif puntos >= 1000:
                ESTADO = GANADOR1
            elif puntos2 >= 1000:
                ESTADO = GANADOR2

            moverBalas(listaBalas)
            moverBalas2(listaBalas2)
            ventana.fill(NEGRO)
            dibujarFondo(ventana,fondoJuego)
            dibujarNave(ventana,imgNave, xNave, yNave)
            dibujarEnemigo(ventana,imgEnemigo)
            dibujarListaBalas(ventana,listaBalas)
            dibujarListaBalas2(ventana, listaBalas2)
            dibujarMarcador(ventana, fuente, puntos)
            dibujarMarcador2(ventana, fuente, puntos2)

        elif ESTADO == GANADOR1:
            ganador = "Jugador1"
            dibujarFondo(ventana,fondoJuego)
            dibujarMarcadorFinal(ventana, fuente, puntos, ganador)
            dibujarBotonStart(ventana, btnStart)
            ganadores.append(ganador)
        elif ESTADO == GANADOR2:
            ganador = "Jugador2"
            dibujarFondo(ventana, fondoJuego)
            dibujarMarcadorFinal(ventana, fuente, puntos2, ganador)
            dibujarBotonStart(ventana, btnStart)
            ganadores.append(ganador)
        elif ESTADO == SCORE:
            dibujarFondo(ventana, fondoJuego)
            dibujarScoreChart(ventana,fuente ,ganadores)
            dibujarBotonStart(ventana, btnStart)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()