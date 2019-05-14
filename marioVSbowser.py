# encoding: UTF-8
# Autor: Aline Villegas Berdejo
#

import pygame  # Librería de pygame
import random
import math


# DIMENSIONES
ANCHO = 800
ALTO = 600

# COLORES
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# IMAGENES
btnJugar = pygame.image.load("button_jugar.png")
fondoMenu = pygame.image.load("fondoMenu3.jpg")
fondoJuego = pygame.image.load("fondo1.png")
imgMario = pygame.image.load("Mario.png")
imgEnemigo = pygame.image.load("enemigo1.png")
imgFuego = pygame.image.load("fuego.png")

# VARIABLES GLOBALES
vidasMario = 5
vidasBowser = 5
listaFuegoMario = []
listaFuegoBowser = []
velocidadYMario = 0


def crearFuego(spriteEnemigo, spriteMario):
    spriteFuego = pygame.sprite.Sprite()
    spriteFuego.image = imgFuego
    spriteFuego.rect = imgFuego.get_rect()
    spriteFuego.rect.left = spriteEnemigo.rect.left
    spriteFuego.rect.top = spriteEnemigo.rect.top
    dx = -(spriteEnemigo.rect.right - (spriteEnemigo.rect.width / 2)) + (
                spriteMario.rect.right - (spriteMario.rect.width / 2))
    dy = (spriteEnemigo.rect.bottom - spriteEnemigo.rect.height / 2) - (
                spriteMario.rect.bottom - spriteMario.rect.height / 2)
    angulo = math.atan2(dy, dx)
    vy = math.sin(angulo)
    vx = math.cos(angulo)
    listaFuegoBowser.append([spriteFuego, vx, vy])


def crearFuegoMario(spriteMario):
    spriteFuego = pygame.sprite.Sprite()
    spriteFuego.image = imgFuego
    spriteFuego.rect = imgFuego.get_rect()
    spriteFuego.rect.left = (spriteMario.rect.right - (spriteMario.rect.width // 4))
    spriteFuego.rect.top = (spriteMario.rect.bottom - spriteMario.rect.height // 4)
    xm, ym = pygame.mouse.get_pos()
    xm -= (spriteMario.rect.right - (spriteMario.rect.width / 2))
    ym -= (spriteMario.rect.bottom - spriteMario.rect.height / 2)
    angulo = math.atan2(ym, xm)
    vy = math.sin(angulo)
    vx = math.cos(angulo)
    listaFuegoMario.append([spriteFuego, vx, vy])


def moverFuego(listaFuego):
    for fuego in listaFuego:
        fuego[0].rect.right += fuego[1] * 5
        fuego[0].rect.top += fuego[2] * 5
        if not 0 < fuego[0].rect.left < ANCHO or not 0 < fuego[0].rect.top < ALTO:  # Salió de la pantalla
            listaFuego.remove(fuego)


def actualizarBowser(ventana, spriteEnemigo, spriteMario, efectoDisparo):
    if random.randint(0, 200) == 0:
        crearFuego(spriteEnemigo, spriteMario)
        efectoDisparo.play()
    ventana.blit(spriteEnemigo.image, spriteEnemigo.rect)
    moverFuego(listaFuegoBowser)
    for spriteFuego in listaFuegoBowser:
        ventana.blit(spriteFuego[0].image, spriteFuego[0].rect)
        # Actualizar Fuego
        if not 0 < spriteFuego[0].rect.left < ANCHO or not 0 < spriteFuego[0].rect.top < ALTO:
            listaFuegoBowser.remove(spriteFuego)


def actualizarMario(ventana, spriteMario):
    global velocidadYMario
    if spriteMario.rect.bottom < ALTO - 50:
        velocidadYMario /= 1.2
    spriteMario.rect.bottom = ALTO - 50 - velocidadYMario
    ventana.blit(spriteMario.image, spriteMario.rect)
    moverFuego(listaFuegoBowser)
    for spriteFuego in listaFuegoMario:
        ventana.blit(spriteFuego[0].image, spriteFuego[0].rect)
        if not 0 < spriteFuego[0].rect.left < ANCHO or not 0 < spriteFuego[0].rect.top < ALTO:
            listaFuegoMario.remove(spriteFuego)


def verificarColisionFuegoEnemigo(spriteMario):
    global vidasMario
    for fuego in listaFuegoBowser:
        if fuego[0].rect.colliderect(spriteMario):
            vidasMario -= 1
            listaFuegoBowser.remove(fuego)
            if vidasMario == 0:
                return True
    return False


def verificarColisionesBowser(spriteEnemigo):
    global vidasBowser
    for fuego in listaFuegoMario:
        if fuego[0].rect.colliderect(spriteEnemigo):  # Prueba colisión
            vidasBowser -= 1
            listaFuegoMario.remove(fuego)
            if vidasBowser == 0:
                return True
    return False


def dibujarMarcador(ventana, fuente, puntos, fuente2, marcador):
    texto = fuente.render("Vidas", 1, BLANCO)
    ventana.blit(texto, (ANCHO // 2 - 130, 50))
    texto2 = fuente2.render("Bowser: " + str(vidasBowser), 1, BLANCO)
    ventana.blit(texto2, (150, 100))
    texto3 = fuente2.render("Mario: " + str(vidasMario), 1, BLANCO)
    ventana.blit(texto3, (ANCHO // 2, 100))


# Dibuja el menú (botones)
def dibujarMenu(ventana, btnJugar, fondoMenu, fuente2, juegoGanado):
    ventana.blit(fondoMenu, (0, 0))  # Dibuja el fondo del menú
    ventana.blit(btnJugar, (300, 400))  # Dibuja el botón jugar
    if juegoGanado == 0:
        texto = fuente2.render("La última vez ganó Bowser", 1, BLANCO)
    else:
        texto = fuente2.render("La última vez ganó Mario", 1, BLANCO)
    ventana.blit(texto, (180, 100))


def dibujarFondo(ventana):
    ventana.blit(fondoJuego, (0, 0))


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    juegoGanado = open("PartidaPasada.txt", "r")
    juegoGanado = int(juegoGanado.readline())

    # BOWSER (sprite)
    spriteEnemigo = pygame.sprite.Sprite()
    spriteEnemigo.image = imgEnemigo
    spriteEnemigo.rect = imgEnemigo.get_rect()
    spriteEnemigo.rect.right = 600
    spriteEnemigo.rect.bottom = ALTO - 50

    # MARIO (sprite)
    spriteMario = pygame.sprite.Sprite()
    spriteMario.image = imgMario
    spriteMario.rect = imgMario.get_rect()
    spriteMario.rect.left = 100
    spriteMario.rect.bottom = ALTO - 60

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    PERDISTE = 3
    GANASTE = 4
    estado = MENU  # Al inicio muestra el menú

    # AUDIO (SONIDO)
    pygame.mixer.init()
    # Sonido corto    Soud -- wav
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    # Sonido largo  Music  -- mp3
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play()

    # TEXTO
    fuente = pygame.font.SysFont("Arial", 72)
    fuente2 = pygame.font.SysFont("Arial", 50)
    marcador = 500

    # TIEMPO
    tiempoAtaque = 100

    # Puntos
    puntos = 300  # No es global

    # CONTADOR DE TIEMPO PARA SALTO
    tiempoSalto = 25

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        global velocidadYMario
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == MENU:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    if xMouse >= 300 and xMouse <= 500 and yMouse >= 400 and yMouse <= 500:
                        estado = JUGANDO  # PASA A JUGAR

        keys = pygame.key.get_pressed()

        if estado == JUGANDO:
            if keys[pygame.K_RIGHT] and spriteMario.rect.right < spriteEnemigo.rect.left:
                spriteMario.rect.left += 15
            elif keys[pygame.K_LEFT] and spriteMario.rect.left > 0:
                spriteMario.rect.left -= 20
            elif keys[pygame.K_UP] and tiempoSalto > 40:
                if tiempoSalto > 40:
                    velocidadYMario = 300
                    tiempoSalto = 0
            elif keys[pygame.K_SPACE]:  # Disparar
                if tiempoAtaque < 0:
                    crearFuegoMario(spriteMario)
                    tiempoAtaque = 100
                    efectoDisparo.play()

        if estado == MENU:
            dibujarMenu(ventana, btnJugar, fondoMenu, fuente2, juegoGanado)


        elif estado == JUGANDO:
            if verificarColisionFuegoEnemigo(spriteMario):
                estado = PERDISTE

            if verificarColisionesBowser(spriteEnemigo):
                estado = GANASTE

            moverFuego(listaFuegoBowser)
            moverFuego(listaFuegoMario)
            dibujarFondo(ventana)
            actualizarMario(ventana, spriteMario)
            actualizarBowser(ventana, spriteEnemigo, spriteMario, efectoDisparo)
            dibujarMarcador(ventana, fuente, puntos, fuente2, marcador)

        tiempoAtaque -= 1

        # CUENTA VUELTAS PARA EL SALTO
        tiempoSalto += 10

        if estado == PERDISTE:
            texto = fuente2.render("Perdiste, intenta de nuevo!", 1, BLANCO)
            # ventana.blit(perdiste, (0,0))
            ventana.blit(texto, (170, 165))

            juegoGanado = open("PartidaPasada.txt", "w")
            juegoGanado.write("0")


        elif estado == GANASTE:
            texto = fuente2.render("Felicidades, ganaste!", 1, BLANCO)
            #  ventana.blit(ganaste, (0,0))
            ventana.blit(texto, (170, 165))

            juegoGanado = open("PartidaPasada.txt", "w")
            juegoGanado.write("1")

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# contador para tiempo de flamas


# Llamas a la función principal
main()

