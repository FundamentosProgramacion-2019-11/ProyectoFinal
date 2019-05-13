# Guillermo De Anda Casas , A01375892
# SECTOR MERTINA (Videojuego final) [Código que contiene el trabajo final.]

import pygame  # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# Vida
xVida = 0
yVida = 350
dano = 0
vida = 10
vidaBoss = 20
# Enemigos
xEnemigo1 = ANCHO // 2
yEnemigo1 = 0
DX = + 45  # right (-1 = left)
DX2 = + 35
DX3 = + 10
# FONDO
yFondo1 = 0  # Global
yFondo2 = -600
yFondo3 = 0
yFondo4 = -600
# MOV SENOIDAL
angulo = 10  # grados
# ASTEROIDES
AY = + 15


# Estructura básica de un programa que usa pygame para dibujar
def dibujarMenu(ventana, btnPlay, logo, btnMore):
    ventana.blit(btnPlay, (300, 400))  # Calcular x,y para centrar el botón
    ventana.blit(logo, (290, 40))
    ventana.blit(btnMore, (332, 500))


def dibujarFondo1(ventana, fondoNivel1, fondoNivel1Dos):
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


def dibujarFondo2(ventana, fondoAst, fondoAst2):
    global yFondo3, yFondo4
    ventana.blit(fondoAst, (0, yFondo3))
    yFondo3 += 5
    ventana.blit(fondoAst2, (0, yFondo4))
    yFondo4 += 5
    if yFondo3 == 600:
        yFondo3 = -600
        ventana.blit(fondoAst, (0, yFondo3))
        yFondo3 += 5
    elif yFondo4 == 600:
        yFondo4 = -600
        ventana.blit(fondoAst2, (0, yFondo4))
        yFondo4 += 5


def dibujarNave(ventana, spriteJugador):
    ventana.blit(spriteJugador.image, spriteJugador.rect)


def dibujarEnemigo1(ventana, spriteEnemigo1):
    global DX, angulo
    ventana.blit(spriteEnemigo1.image, spriteEnemigo1.rect)
    spriteEnemigo1.rect.left += DX
    # probar choque
    if spriteEnemigo1.rect.left >= ANCHO - 75 or spriteEnemigo1.rect.left <= 0:  # 75 porque el enemigo es de 75 pixeles.
        DX = - DX
    # coord en y
    DY = int(5 * math.sin(math.radians(angulo)))
    spriteEnemigo1.rect.top = DY
    angulo += 15


def dibujarEnemigo2(ventana, spriteEnemigo2):
    global DX2
    ventana.blit(spriteEnemigo2.image, spriteEnemigo2.rect)
    spriteEnemigo2.rect.left += DX2
    if spriteEnemigo2.rect.left >= ANCHO - 75 or spriteEnemigo2.rect.left <= 0:  # 75 porque el enemigo es de 75 pixeles.
        DX2 = - DX2
    spriteEnemigo2.rect.top = 75


def dibujarBoss(ventana, spriteBoss):
    global DX3
    ventana.blit(spriteBoss.image, spriteBoss.rect)
    spriteBoss.rect.left += DX3
    if spriteBoss.rect.left >= ANCHO - 500 or spriteBoss.rect.left <= 0:
        DX3 = - DX3
    spriteBoss.rect.top = 10


def dibujarAsteroide1(ventana, spriteAste1):
    if spriteAste1.rect.left != -80:
        ventana.blit(spriteAste1.image, spriteAste1.rect)
        spriteAste1.rect.top += 30
        if spriteAste1.rect.top > 703:
            spriteAste1.rect.left = -1


def dibujarBala1(ventana, spriteBala1):
    if spriteBala1.rect.left != -1:
        ventana.blit(spriteBala1.image, spriteBala1.rect)
        spriteBala1.rect.top -= 25
        if spriteBala1.rect.top < -48:
            spriteBala1.rect.left = -1


def dibujarBala2(ventana, spriteBala2, spriteEnemigo1):
    if spriteBala2.rect.left != -1:
        ventana.blit(spriteBala2.image, spriteEnemigo1.rect)
        spriteBala2.rect.top += 30
        if spriteBala2.rect.top > + 615:
            spriteBala2.rect.left = -1


def danoBoss():
    global vidaBoss
    vidaBoss -= 1


def obtenerDano():
    global dano
    dano += 1
    return dano


def dibujarVida(ventana, dano, vida10, vida9, vida8, vida7, vida6, vida5, vida4, vida3, vida2, vida1, vida0):
    global estado, vida
    vidaActual = 10 - dano
    vida = vidaActual
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
    elif vidaActual == 0:
        vida = vida0
        pygame.mixer.Sound("explosion2.wav").play()
        pygame.mixer.Sound("wilhelm.wav").set_volume(0.6)
        pygame.mixer.Sound("wilhelm.wav").play()
        estado = 6
    ventana.blit(vida, (xVida, yVida))
    return vida


def dibujarPausa(ventana, ventanaPausa, btnContinuar, btnSalir):
    ventana.blit(ventanaPausa, (0, 0))
    ventana.blit(btnContinuar, (240, 150))
    ventana.blit(btnSalir, (285, 450))
    pygame.mixer.music.pause()


def dibujarTiempo(ventana, marcador, fuente):
    texto = fuente.render(str(marcador), 0, BLANCO)
    ventana.blit(texto, (708, 560))


def dibujarGameOver(ventana, gameOver):
    ventana.blit(gameOver, (0, 0))


def dibujarSpaceJump(ventana, spaceJump):
    ventana.blit(spaceJump, (500, 550))


def dibujarPantallaMore(ventana, ventanaMore, fondoNivel1, fondoNivel1Dos):
    dibujarFondo1(ventana, fondoNivel1, fondoNivel1Dos)
    ventana.blit(ventanaMore, (0, 0))


def generarEnemigos(listaEnemigos, enemigo1, enemigo2, enemigo3, ventana):
    enemigos = 0
    if enemigos == 6:
        pass
    else:
        for eX in range(15, 725, 140):
            eY = 150
            spriteEnemigo1 = pygame.sprite.Sprite()
            spriteEnemigo1.image = enemigo1
            spriteEnemigo1.rect = enemigo1.get_rect()
            spriteEnemigo1.rect.left = eX
            spriteEnemigo1.rect.top = eY
            listaEnemigos.append(spriteEnemigo1)
            enemigos += 1


def dibujarListaEnemigos(ventana, listaEnemigos):
    global DX, angulo

    # print(len(listaEnemigos))
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
        if enemigo.rect.left >= ANCHO - 75 or enemigo.rect.left <= 0:  # 75 porque el enemigo es de 75 pixeles.
            DX = - DX


def dibujarListaBalas1(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)
        bala.rect.top -= 35
        if bala.rect.top < -48:
            listaBalas.remove(bala)


def dibujarListaBalas2(ventana, listaBalas2):
    for bala in listaBalas2:
        ventana.blit(bala.image, bala.rect)
        bala.rect.top += 30
        if bala.rect.top > 620:
            listaBalas2.remove(bala)


def dibujarListaBalas3(ventana, listaBalas3):
    for bala in listaBalas3:
        ventana.blit(bala.image, bala.rect)
        bala.rect.top += 40
        if bala.rect.top > 660:
            listaBalas3.remove(bala)


def probarColisionBoss(listaBalas1, listaBalas3, spriteJugador, spriteBoss, score):
    for bala in listaBalas3:
        if bala.rect.colliderect(spriteJugador):
            pygame.mixer.Sound("danoJugador.wav").play()
            obtenerDano()
            bala.rect.left = -1000
    for bala in listaBalas1:
        if bala.rect.colliderect(spriteBoss):
            pygame.mixer.Sound("explosion.wav").set_volume(0.5)
            pygame.mixer.Sound("explosion.wav").play()
            danoBoss()
            bala.rect.left = -50
            score += 25


def probarColision(listaBalas1, listaBalas2, spriteJugador, listaEnemigos, spriteEnemigo1, spriteEnemigo2, listaAste):
    global score
    for bala in listaBalas1:
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo):
                pygame.mixer.Sound("explosion.wav").set_volume(0.5)
                pygame.mixer.Sound("explosion.wav").play()
                listaEnemigos.remove(enemigo)
                bala.rect.left = -50
                score += 50
    for bala in listaBalas2:
        if bala.rect.colliderect(spriteJugador):
            pygame.mixer.Sound("danoJugador.wav").play()
            obtenerDano()
            bala.rect.left = -50
    for bala in listaBalas1:
        if bala.rect.colliderect(spriteEnemigo1):
            pygame.mixer.Sound("explosion.wav").play()
            spriteEnemigo1.rect.left = -200
            bala.rect.left = -50
            score += 1000
    for bala in listaBalas1:
        if bala.rect.colliderect(spriteEnemigo2):
            pygame.mixer.Sound("explosion.wav").play()
            spriteEnemigo2.rect.left = -300
            bala.rect.left = -50
            score += 500
    for asteroide in listaAste:
        if asteroide.rect.colliderect(spriteJugador):
            pygame.mixer.Sound("danoJugador.wav").play()
            obtenerDano()


def dibujarPoints(ventana, points):
    ventana.blit(points, (502, 530))


def dibujarMarcador(ventana, score, fuente):
    texto = fuente.render(str(score), 0, BLANCO)
    ventana.blit(texto, (580, 530))


def dibujarLitaAste(ventana, listaAste):
    for asteroide in listaAste:
        ventana.blit(asteroide.image, asteroide.rect)
        asteroide.rect.top += 50
        if asteroide.rect.top > 800:
            listaAste.remove(asteroide)


def dibujarGanar(ventana, ventanaGanar):
    ventana.blit(ventanaGanar, (0, 0))


def imprimirPuntaje(ventana, score, fuente, listaScore):
    texto = fuente.render(str(score), 1, BLANCO)
    ventana.blit(texto, (410, 400))
    listaScore.append(score)


def imprimirHiScore(ventana, listaScore, fuente):
    hiScore = max(listaScore)
    texto = fuente.render(str(hiScore), 1, BLANCO)
    ventana.blit(texto, (440, 150))


def dibujar():
    global xNave, yNave, vida, tiempoMover, score, tiempoAtaque1  # Voy a usar la variable global.

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES
    btnPlay = pygame.image.load("btnPlay.png")
    btnMore = pygame.image.load("More.png")
    logo = pygame.image.load("logo.png")
    fondoNivel1 = pygame.image.load("Space2.png")
    fondoNivel1Dos = pygame.image.load("Space2.png")
    fondoNivel2 = pygame.image.load("Space3.png")
    fondoNivel2Dos = pygame.image.load("Space3.png")
    ventanaPausa = pygame.image.load("Pausa.png")
    ventanaMore = pygame.image.load("MoreScreen.png")
    ventanaGanar = pygame.image.load("win.png")
    btnContinuar = pygame.image.load("ResumeGame.png")
    btnSalir = pygame.image.load("QuitGame.png")
    asteroide1 = pygame.image.load("aste1.png")
    nave = pygame.image.load("Nave 1.png")
    enemigo1 = pygame.image.load("Nave 2.png")
    enemigo2 = pygame.image.load("Nave 3.png")
    enemigo3 = pygame.image.load("Nave 4.png")
    boss = pygame.image.load("BOSS.png")
    imgBala1 = pygame.image.load("Shot1.png")
    imgBala2 = pygame.image.load("Shot2.png")
    imgBala3 = pygame.image.load("Shot3.png")
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
    vida0 = pygame.image.load("LB 0.png")
    spaceJump = pygame.image.load("SpaceJump.png")
    gameOver = pygame.image.load("Game Over.png")
    points = pygame.image.load("Points.png")

    # LISTA DE ENEMIGOS
    listaEnemigos = []

    # LISTA BALAS1
    listaBalas1 = []

    # LISTA BALAS 2
    listaBalas2 = []

    # LISTA BALAS 3
    listaBalas3 = []

    # LISTA ASTEROIDES
    listaAste = []

    # LISTA PUNTAJES
    listaScore = [0]

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
    spriteEnemigo1.image = enemigo3
    spriteEnemigo1.rect = enemigo3.get_rect()
    spriteEnemigo1.rect.left = -1
    spriteEnemigo1.rect.top = -1

    spriteEnemigo2 = pygame.sprite.Sprite()
    spriteEnemigo2.image = enemigo2
    spriteEnemigo2.rect = enemigo2.get_rect()
    spriteEnemigo2.rect.left = -1
    spriteEnemigo2.rect.top = -1

    spriteBoss = pygame.sprite.Sprite()
    spriteBoss.image = boss
    spriteBoss.rect = boss.get_rect()
    spriteBoss.rect.left = -1
    spriteBoss.rect.top = -1

    # AUDIO
    global estado, MENU, NIVEL1, NIVEL2
    pygame.mixer.init(44100, -16, 1)
    pygame.mixer.pre_init()
    pygame.mixer.set_num_channels(16)
    efectoDisparo = pygame.mixer.Sound("Shot1.wav")
    # efectoExplMalo = pygame.mixer.Sound("explosion1.wav")
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
    GAMEOVER = 6
    MORE = 7
    WIN = 8
    estado = MENU

    # TEXTO
    fuente = pygame.font.SysFont("Arcade", 28)

    # TIEMPOS
    tiempoSalto = 250
    tiempoSalto2 = 500
    tiempoSalto3 = 1500
    tiempoAtaque1 = random.randint(10, 31)
    tiempoAtaque2 = random.randint(10, 21)
    tiempoAtaque3 = random.randint(10, 16)
    tiempoAtaque4 = random.randint(10, 16)
    tiempoAsteroide1 = 25
    score = 0
    tiempoMover = 10

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 400 and yMouse <= 450 and estado == MENU:
                    # CAMBIO DE ESTADO A NIVEL1
                    xMouse = -1
                    estado = NIVEL1
                    pygame.mixer.Sound("start.wav").set_volume(0.7)
                    pygame.mixer.Sound("start.wav").play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("LEVEL1comp.mp3")
                    pygame.mixer.music.play(-1)
                    spriteJugador.rect.left = (ANCHO // 2) - 35
                    spriteJugador.rect.top = ALTO // 1.5

            elif evento.type == pygame.KEYDOWN:  # OPRIMIÓ TECLA
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
                    pygame.mixer.Sound("Shot1.wav").play()
                    spriteBala1 = pygame.sprite.Sprite()
                    spriteBala1.image = imgBala1
                    spriteBala1.rect = imgBala1.get_rect()  # Datos de la imagen
                    spriteBala1.rect.left = spriteJugador.rect.left + 33  # Coordenada en x
                    spriteBala1.rect.top = spriteJugador.rect.top - 35  # Coordenada en y
                    listaBalas1.append(spriteBala1)


                elif evento.key == pygame.K_ESCAPE and estado == NIVEL1:
                    pygame.mixer.Sound("start.wav").set_volume(0.7)
                    pygame.mixer.Sound("start.wav").play()
                    estado = PAUSA
                    pygame.mixer.music.pause()

            elif xMouse >= 240 and xMouse <= 560 and yMouse >= 150 and yMouse <= 200 and estado == MENU:
                estado = NIVEL1

            elif xMouse >= 240 and xMouse <= 560 and yMouse >= 450 and yMouse <= 570 and estado == MENU:
                estado = MORE
                pygame.mixer.Sound("start.wav").set_volume(0.7)
                pygame.mixer.Sound("start.wav").play()
            elif xMouse >= 50 and xMouse <= 250 and yMouse >= 540 and yMouse <= 650 and estado == MORE:
                estado = MENU
                pygame.mixer.Sound("menuback.wav").play()
            elif xMouse >= 225 and xMouse <= 550 and yMouse >= 150 and yMouse <= 300 and estado == PAUSA:
                estado = NIVEL1
                pygame.mixer.music.unpause()
                pygame.mixer.Sound("menuback.wav").play()

            elif xMouse >= 285 and xMouse <= 515 and yMouse >= 450 and yMouse <= 500 and estado == PAUSA:
                estado = MENU
                pygame.mixer.Sound("menuback.wav").play()
                pygame.mixer.music.load("menu.mp3")
                pygame.mixer.music.play(-1)

            elif xMouse >= 550 and xMouse <= 800 and yMouse >= 500 and yMouse <= 600 and estado == WIN:
                estado = MENU
                pygame.mixer.Sound("menuback.wav").play()
                pygame.mixer.music.load("menu.mp3")
                pygame.mixer.music.play(-1)


            elif evento.type == pygame.KEYUP:  # SOLTÓ TECLA
                if evento.key == pygame.K_RIGHT:
                    moveR = False
                elif evento.key == pygame.K_LEFT:
                    moveL = False
                elif evento.key == pygame.K_UP:
                    moveUp = False
                elif evento.key == pygame.K_DOWN:
                    moveDo = False
        if moveR and spriteJugador.rect.left < 715:
            spriteJugador.rect.left += 20
        elif moveL and spriteJugador.rect.left > 0:
            spriteJugador.rect.left -= 20
        elif moveUp and spriteJugador.rect.top > 150:
            spriteJugador.rect.top -= 15
        elif moveDo and spriteJugador.rect.top < 525:
            spriteJugador.rect.top += 7

        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarMenu(ventana, btnPlay, logo, btnMore)

        elif estado == MORE:
            dibujarPantallaMore(ventana, ventanaMore, fondoNivel1, fondoNivel1Dos)
            imprimirHiScore(ventana, listaScore, fuente)

        elif estado == GAMEOVER:
            dibujarGameOver(ventana, gameOver)

            if xMouse >= 285 and xMouse <= 515 and yMouse >= 450 and yMouse <= 500:
                estado = MENU
                pygame.mixer.Sound("menuback.wav").play()
                pygame.mixer.music.load("menu.mp3")
                pygame.mixer.music.play(-1)

        elif estado == PAUSA:
            dibujarPausa(ventana, ventanaPausa, btnContinuar, btnSalir)

        elif estado == WIN:
            dibujarGanar(ventana, ventanaGanar)
            imprimirPuntaje(ventana, score, fuente, listaScore)


        # INICIA NIVEL 1!
        elif estado == NIVEL1:
            # ACTUALIZAR
            tiempoSalto -= 1
            tiempoAtaque1 -= 1
            tiempoAtaque2 -= 1

            probarColision(listaBalas1, listaBalas2, spriteJugador, listaEnemigos, spriteEnemigo1, spriteEnemigo2,
                           listaAste)
            # DIBUJAR
            dibujarFondo1(ventana, fondoNivel1, fondoNivel1Dos)
            dibujarNave(ventana, spriteJugador)
            dibujarEnemigo1(ventana, spriteEnemigo1)
            dibujarEnemigo2(ventana, spriteEnemigo2)

            dibujarListaEnemigos(ventana, listaEnemigos)
            dibujarListaBalas1(ventana, listaBalas1)

            dibujarListaBalas2(ventana, listaBalas2)

            if tiempoAtaque1 == 0:
                if spriteEnemigo1.rect.left == -200:
                    pass
                else:
                    spriteBala2 = pygame.sprite.Sprite()
                    spriteBala2.image = imgBala2
                    spriteBala2.rect = imgBala2.get_rect()
                    spriteBala2.rect.left = spriteEnemigo1.rect.left + 30
                    spriteBala2.rect.top = spriteEnemigo1.rect.top + 33
                    listaBalas2.append(spriteBala2)
                    pygame.mixer.Sound("Shot2.wav").play()
                    tiempoAtaque1 = random.randint(10, 31)

            elif tiempoAtaque2 == 0:
                if spriteEnemigo2.rect.left == -300:
                    pass
                else:
                    spriteBala2 = pygame.sprite.Sprite()
                    spriteBala2.image = imgBala2
                    spriteBala2.rect = imgBala2.get_rect()
                    spriteBala2.rect.left = spriteEnemigo2.rect.left + 30
                    spriteBala2.rect.top = spriteEnemigo2.rect.top + 33
                    listaBalas2.append(spriteBala2)
                    pygame.mixer.Sound("Shot2.wav").play()
                    tiempoAtaque2 = random.randint(10, 21)

            dibujarTiempo(ventana, tiempoSalto, fuente)
            dibujarMarcador(ventana, score, fuente)
            dibujarVida(ventana, dano, vida10, vida9, vida8, vida7, vida6, vida5, vida4, vida3, vida2, vida1, vida0)
            dibujarSpaceJump(ventana, spaceJump)
            dibujarPoints(ventana, points)
            generarEnemigos(listaEnemigos, enemigo1, enemigo2, enemigo3, ventana)

            if tiempoSalto == 0 or score >= 2000:
                estado = NIVEL2

        # INICIA EL NIVEL 2!

        elif estado == NIVEL2:
            # ACTUALIZAR
            tiempoAsteroide1 -= 1
            tiempoSalto2 -= 1
            tiempoAtaque1 -= 1
            tiempoAtaque2 -= 1

            probarColision(listaBalas1, listaBalas2, spriteJugador, listaEnemigos, spriteEnemigo1, spriteEnemigo2,
                           listaAste)
            # DIBUJAR
            dibujarFondo1(ventana, fondoNivel2, fondoNivel2Dos)
            dibujarNave(ventana, spriteJugador)
            dibujarEnemigo1(ventana, spriteEnemigo1)
            dibujarEnemigo2(ventana, spriteEnemigo2)
            dibujarListaEnemigos(ventana, listaEnemigos)

            if spriteEnemigo1.rect.left == -200:
                spriteEnemigo1.rect.left = -1
                dibujarListaBalas2(ventana, listaBalas2)

            elif spriteEnemigo2.rect.left == -300:
                spriteEnemigo2.rect.left = -1
                dibujarListaBalas2(ventana, listaBalas2)

            dibujarListaBalas1(ventana, listaBalas1)
            dibujarListaBalas2(ventana, listaBalas2)
            dibujarLitaAste(ventana, listaAste)

            if tiempoAtaque1 == 0:
                if spriteEnemigo1.rect.left == -200:
                    pass
                else:
                    spriteBala2 = pygame.sprite.Sprite()
                    spriteBala2.image = imgBala2
                    spriteBala2.rect = imgBala2.get_rect()
                    spriteBala2.rect.left = spriteEnemigo1.rect.left + 30
                    spriteBala2.rect.top = spriteEnemigo1.rect.top + 33
                    listaBalas2.append(spriteBala2)
                    pygame.mixer.Sound("Shot2.wav").play()
                    tiempoAtaque1 = random.randint(10, 31)

            elif tiempoAtaque2 == 0:
                if spriteEnemigo2.rect.left == -300:
                    pass
                else:
                    spriteBala2 = pygame.sprite.Sprite()
                    spriteBala2.image = imgBala2
                    spriteBala2.rect = imgBala2.get_rect()
                    spriteBala2.rect.left = spriteEnemigo2.rect.left + 30
                    spriteBala2.rect.top = spriteEnemigo2.rect.top + 33
                    listaBalas2.append(spriteBala2)
                    pygame.mixer.Sound("Shot2.wav").play()
                    tiempoAtaque2 = random.randint(10, 21)

            elif tiempoAsteroide1 == 0:
                spriteAste1 = pygame.sprite.Sprite()
                spriteAste1.image = asteroide1
                spriteAste1.rect = asteroide1.get_rect()
                spriteAste1.rect.left = random.randint(1, 601)
                spriteAste1.rect.top = -80
                listaAste.append(spriteAste1)
                tiempoAsteroide1 = 25

            dibujarTiempo(ventana, tiempoSalto, fuente)
            dibujarMarcador(ventana, score, fuente)
            dibujarVida(ventana, dano, vida10, vida9, vida8, vida7, vida6, vida5, vida4, vida3, vida2, vida1, vida0)
            dibujarSpaceJump(ventana, spaceJump)
            dibujarPoints(ventana, points)
            generarEnemigos(listaEnemigos, enemigo1, enemigo2, enemigo3, ventana)

            if tiempoSalto2 == 0 or score >= 7500:
                estado = NIVEL3

        # INICIA EL NIVEL 3!

        elif estado == NIVEL3:
            # ACTUALIZAR
            tiempoSalto3 -= 1
            tiempoAtaque3 -= 1
            tiempoAtaque4 -= 1

            probarColisionBoss(listaBalas1, listaBalas3, spriteJugador, spriteBoss, score)

            # DIBUJAR
            dibujarFondo1(ventana, fondoNivel2, fondoNivel2Dos)
            dibujarNave(ventana, spriteJugador)
            dibujarBoss(ventana, spriteBoss)
            dibujarListaBalas1(ventana, listaBalas1)
            dibujarListaBalas3(ventana, listaBalas3)

            if tiempoAtaque3 == 0:
                spriteBala3 = pygame.sprite.Sprite()
                spriteBala3.image = imgBala3
                spriteBala3.rect = imgBala3.get_rect()
                spriteBala3.rect.left = spriteBoss.rect.left + 100
                spriteBala3.rect.top = spriteBoss.rect.top + 250
                listaBalas3.append(spriteBala3)
                pygame.mixer.Sound("Shot2.wav").play()
                tiempoAtaque3 = random.randint(10, 16)

            elif tiempoAtaque4 == 0:
                spriteBala3 = pygame.sprite.Sprite()
                spriteBala3.image = imgBala3
                spriteBala3.rect = imgBala3.get_rect()
                spriteBala3.rect.left = spriteBoss.rect.left + 400
                spriteBala3.rect.top = spriteBoss.rect.top + 250
                listaBalas3.append(spriteBala3)
                pygame.mixer.Sound("Shot2.wav").play()
                tiempoAtaque4 = random.randint(10, 16)

            dibujarTiempo(ventana, tiempoSalto3, fuente)
            dibujarMarcador(ventana, score, fuente)
            dibujarVida(ventana, dano, vida10, vida9, vida8, vida7, vida6, vida5, vida4, vida3, vida2, vida1, vida0)
            dibujarSpaceJump(ventana, spaceJump)
            dibujarPoints(ventana, points)

            if vidaBoss == 0:
                score += 10000

            if tiempoSalto3 == 0 or vidaBoss == 0:
                estado = WIN

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# Llamas a la función principal
main()
