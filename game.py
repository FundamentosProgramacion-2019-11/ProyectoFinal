# Guillermo De Anda Casas , A01375892
# SECTOR MERTINA (Videojuego final) [Código que contiene el trabajo final.]

import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# Vida
xVida = 0
yVida = 350
# Enemigos
xEnemigo1 = ANCHO // 2
yEnemigo1 = 0
DX = + 8 # right (-1 = left)
# FONDO
yFondo1 = 0     # Global
yFondo2 = -600
# MOV SENOIDAL
angulo = 0  # grados
# ASTEROIDES
AY = + 10

# Estructura básica de un programa que usa pygame para dibujar
def dibujarMenu(ventana, btnPlay, logo):
    ventana.blit(btnPlay, (300, 400))   # Calcular x,y para centrar el botón
    ventana.blit(logo, (290, 40))


def dibujarFondo(ventana, fondoNivel1, fondoNivel1Dos):
    global yFondo1, yFondo2
    ventana.blit(fondoNivel1, (0, yFondo1))
    yFondo1 += 5
    ventana.blit(fondoNivel1Dos, (0, yFondo2))
    yFondo2 += 5
    if yFondo1 == 600:
        yFondo1 = -600
        ventana.blit(fondoNivel1, (0, yFondo1))
        yFondo1 += 5
    elif yFondo2 == 600:
        yFondo2 = -600
        ventana.blit(fondoNivel1Dos, (0, yFondo2))
        yFondo2 += 5


def dibujarNave(ventana, spriteJugador):
    ventana.blit(spriteJugador.image, spriteJugador.rect)


def dibujarEnemigo1(ventana, spriteEnemigo1):
    global DX, angulo
    ventana.blit(spriteEnemigo1.image, spriteEnemigo1.rect)
    spriteEnemigo1.rect.left += DX
    # probar choque
    if spriteEnemigo1.rect.left >= ANCHO - 75 or spriteEnemigo1.rect.left <= 0 : #75 porque el enemigo es de 75 pixeles.
        DX = - DX
    # coord en y
    DY = int(5 * math.sin(math.radians(angulo)))
    spriteEnemigo1.rect.top = DY
    angulo += 15


def dibujarAsteroide1(ventana, spriteAste1):
    ventana.blit(spriteAste1.image, spriteAste1.rect)

    if spriteAste1.rect.left != -1:
        ventana.blit(spriteAste1.image, spriteAste1.rect)
        spriteAste1.rect.top += 15
        if spriteAste1.rect.top < 703:
            spriteAste1.rect.left = -1


def dibujarBala1(ventana, spriteBala1):
    if spriteBala1.rect.left != -1:
        ventana.blit(spriteBala1.image, spriteBala1.rect)
        spriteBala1.rect.top -= 15
        if spriteBala1.rect.top < -48:
            spriteBala1.rect.left = -1


def dibujarBala2(ventana, spriteBala2):
    if spriteBala2.rect.left != -1:
        ventana.blit(spriteBala2.image, spriteBala2.rect)
        spriteBala2.rect.top += 15
        if spriteBala2.rect.top > + 615:
            spriteBala2.rect.left = -1


def probarColision(spriteBala1):
    global xEnemigo1
    xBala = spriteBala1.rect.left
    yBala = spriteBala1.rect.top
    if xBala>=xEnemigo1 and xBala<=xEnemigo1+75 and yBala>=yEnemigo1 and yBala<=yEnemigo1+75:

        xEnemigo1 = -80

        spriteBala1.rect.left = -1
        # efectoExplMalo.play()


'''
def correrMusica(fondo):
    global estado, MENU, menu, intro1, loop1
    playCount = 0
    if estado == 1:
        if playCount > 0:
            fondo.play()
            playCount += 1
'''


def obtenerDano(spriteJugador, spriteBala2):
    dano = 0
    if spriteBala2.rect == spriteJugador.rect:
        dano += 1
        spriteBala2.rect.top = -1
    return dano


def dibujarVida(ventana, dano, vida10, vida9, vida8, vida7, vida6, vida5, vida4, vida3, vida2, vida1):
    vidaActual = 10 - dano
    if vidaActual == 10:
        vida = vida10
    elif vidaActual == 9:
        vida = vida9
    elif vidaActual == 8:
        vida = vida8
    elif vidaActual == 7:
        vida = vida7
    elif vidaActual == 6:
        vida = vida6
    elif vidaActual == 5:
        vida = vida5
    elif vidaActual == 4:
        vida = vida4
    elif vidaActual == 3:
        vida = vida3
    elif vidaActual == 2:
        vida = vida2
    elif vidaActual == 1:
        vida = vida1
    ventana.blit(vida, (xVida, yVida))


def dibujarPausa(ventana, ventanaPausa, btnContinuar, btnSalir):
    ventana.blit(ventanaPausa, (0, 0))
    ventana.blit(btnContinuar, (240, 150))
    ventana.blit(btnSalir, (285, 450))
    pygame.mixer.music.pause()


'''
def dibujarAsteroides(ventana, spriteAste1):
     xAst1 = 400
     yAst1 = 0
     ventana.blit(ventana, (xAst1, yAst1))
     spriteAste1.rect.top -= 5
'''


def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render("PUNTOS: " + str(marcador), 0, BLANCO)
    ventana.blit(texto, (650, 550))


def dibujar():
    global xNave, yNave    # Voy a usar la variable global.
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES
    btnPlay = pygame.image.load("btnPlay.png")
    logo = pygame.image.load("logo.png")
    fondoNivel1 = pygame.image.load("Space2.png")
    fondoNivel1Dos = pygame.image.load("Space2.png")
    ventanaPausa = pygame.image.load("Pausa.png")
    btnContinuar = pygame.image.load("ResumeGame.png")
    btnSalir = pygame.image.load("QuitGame.png")
    asteroide1 = pygame.image.load("aste1.png")
    nave = pygame.image.load("Nave 1.png")
    enemigo1 = pygame.image.load("Nave 2.png")
    imgBala1 = pygame.image.load("Shot1.png")
    imgBala2 = pygame.image.load("Shot2.png")
    vida10 = pygame.image.load("LB 10.png")
    vida9 = pygame.image.load("LB 9.png")
    vida8 = pygame.image.load("LB 8.png")
    vida7 = pygame.image.load("LB 7.png")
    vida6 = pygame.image.load("LB 6.png")
    vida5 = pygame.image.load("LB 5.png")
    vida4 = pygame.image.load("LB 4.png")
    vida3 = pygame.image.load("LB 3.png")
    vida2 = pygame.image.load("LB 2.png")
    vida1 = pygame.image.load("LB 1.png")
    explosion1 = pygame.image.load("explosion1.png")

    # SPRITES
    spriteJugador = pygame.sprite.Sprite()
    spriteJugador.image = nave
    spriteJugador.rect = nave.get_rect()
    spriteJugador.rect.left = -1
    spriteJugador.rect.top = -1
    moveL = False
    moveR = False
    moveUp = False
    moveDo = False

    spriteEnemigo1 = pygame.sprite.Sprite()
    spriteEnemigo1.image = enemigo1
    spriteEnemigo1.rect = enemigo1.get_rect()
    spriteEnemigo1.rect.left = -1
    spriteEnemigo1.rect.top = -1

    spriteAste1 = pygame.sprite.Sprite()
    spriteAste1.image = asteroide1
    spriteAste1.rect = asteroide1.get_rect()
    spriteAste1.rect.left = -1
    spriteAste1.rect.top = -1

    spriteBala1 = pygame.sprite.Sprite()
    spriteBala1.image = imgBala1
    spriteBala1.rect = imgBala1.get_rect()   # Datos de la imagen
    spriteBala1.rect.left = -1   # Coordenada en x
    spriteBala1.rect.top = -1    # Coordenada en y

    spriteBala2 = pygame.sprite.Sprite()
    spriteBala2.image = imgBala2
    spriteBala2.rect = imgBala2.get_rect()
    spriteBala2.rect.left = -1
    spriteBala2.rect.top = -1


    # AUDIO
    global estado, MENU, NIVEL1
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("Pruebadisparo.wav")
    #efectoExplMalo = pygame.mixer.Sound("explosion1.wav")
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1)

    # MOUSE
    xMouse = -1
    yMouse = -1

    # ESTADOS
    MENU = 1
    PAUSA = 2
    NIVEL1 = 3
    NIVEL2 = 4
    NIVEL3 = 5
    estado = MENU

    # TEXTO
    fuente = pygame.font.SysFont("Arcade", 28)

    # TIEMPOS
    tiempoAtaque1 = 10
    tiempoAsteroide1 = 15
    texplosion1 = 1
    contador = 0


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:     # Oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse>=300 and xMouse<=500 and yMouse>=400 and yMouse<= 450:
                    # CAMBIO DE ESTADO A NIVEL1
                    xMouse = -1
                    estado = NIVEL1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("LEVEL1.mp3")
                    pygame.mixer.music.play(-1)
                    spriteJugador.rect.left = ANCHO // 2
                    spriteJugador.rect.top = ALTO // 2

            elif evento.type == pygame.KEYDOWN:     # OPRIMIÓ TECLA
                # Verificar cuál tecla se oprimió (if)

                if evento.key == pygame.K_RIGHT:
                    moveR = True

                elif evento.key == pygame.K_LEFT:
                    moveL = True

                elif evento.key == pygame.K_UP:
                    moveUp = True

                elif evento.key == pygame.K_DOWN:
                    moveDo = True

                elif evento.key == pygame.K_SPACE:
                    if spriteBala1.rect.left == -1:
                        spriteBala1.rect.left = spriteJugador.rect.left + 41 - 9
                        spriteBala1.rect.top = spriteJugador.rect.top - 48
                        efectoDisparo.play()
                elif evento.key == pygame.K_ESCAPE:

                    estado = PAUSA

            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
            elif xMouse>=240 and xMouse<=560 and yMouse>=150 and yMouse<=200:
                estado = NIVEL1

            elif xMouse>=285 and xMouse<=515 and yMouse>=450 and yMouse<=500:
                estado = MENU

            elif evento.type == pygame.KEYUP:   # SOLTÓ TECLA
                if evento.key == pygame.K_RIGHT:
                    moveR = False
                elif evento.key == pygame.K_LEFT:
                    moveL = False
                elif evento.key == pygame.K_UP:
                    moveUp = False
                elif evento.key == pygame.K_DOWN:
                    moveDo = False
        if moveR:
            spriteJugador.rect.left += 15
        elif moveL:
            spriteJugador.rect.left -= 15
        elif moveUp:
            spriteJugador.rect.top -= 15
        elif moveDo:
            spriteJugador.rect.top += 15


        # Borrar pantalla
        ventana.fill(NEGRO)


        if estado == MENU:
            dibujarMenu(ventana, btnPlay, logo)
            # correrMusica(menu)
        elif estado == NIVEL1:
            # ACTUALIZAR
            probarColision(spriteBala1)
            tiempoAtaque1 -= 1
            if tiempoAtaque1 == 0:
                if spriteBala2.rect.left == -1:
                    spriteBala2.rect.left = xEnemigo1
                    spriteBala2.rect.top = yEnemigo1
                tiempoAtaque1 = 10

            elif tiempoAsteroide1 == 0:
                if spriteAste1.rect.left == -1:
                    spriteAste1.rect.left = 690
                    spriteAste1.rect.top = 0
                    # spriteAste1.rect.top += AY
                tiempoAsteroide1 = 15

            dano = obtenerDano(spriteJugador, spriteBala2)
            # DIBUJAR
            dibujarFondo(ventana, fondoNivel1, fondoNivel1Dos)
            dibujarNave(ventana, spriteJugador)
            dibujarEnemigo1(ventana, spriteEnemigo1)
            dibujarBala1(ventana, spriteBala1)
            dibujarBala2(ventana, spriteBala2)

            dibujarVida(ventana, dano, vida10, vida9, vida8, vida7, vida6, vida5, vida4, vida3, vida2, vida1)
            #dibujarAsteroide1(ventana, spriteAste1)
            # Dibuja texto
            # dibujarMarcador(ventana, marcador, fuente)

        elif estado == PAUSA:
            dibujarPausa(ventana, ventanaPausa, btnContinuar, btnSalir)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()